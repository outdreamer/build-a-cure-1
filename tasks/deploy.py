import os, csv, json, uuid, re
import boto3
import pandas as pd
import numpy as np

from import_elk import import_to_elk
from sanitize import sanitize_data

'''
which strategies will the models use?

	- standard data analysis (pca, feature reduction, relationship metrics)

	- use object detection api's with language-structure map

	- initial version:

		- templates
			- after applying standardization function to compare overall structure, intent, & meaning
			- without standardization, to compare to custom user-specific model
		- unsupervised learning (k means, nearest neighbors)
		- anomaly detection algorithms
		
	 - secondary version depending on data access:

	 	- intent/cause/meaning model, optionally with assumption/implication/conclusions integrated
	 		- do functions with these intents enable an overall malicious intent when executed in a sequence?
	 		- every resource access, including function calls, is a possible target of a malicious agent
	 		- apply filters on resources (valuable resources, enabling resources, access-granting resources, etc)

	 		- does this request have the preceding/following request that we'd expect from a request with this intent (cause)

	 		- initial implementation can be with object definition routes mapped to language map structures, then to system map structures

	 	- distortion/base model
	 		- given a particular base (request type, user group, intent), what distortion functions apply?
	 		- what ranges of distortion functions overlap?
	 		- what change types of distortion functions indicate a type or base change?

	 	- change model
	 		- is this function or data point in a state of flux or does it clearly fall into a known category?

'''

def create_instance(client):
	instance_name = 'API_spam'
	on_start_content = None
	with open('on_start.sh', 'r') as f:
		on_start_content = f.read()
		f.close()
	if on_start_content:
		encoded = base64.base64_encode(on_start_content)
		if encoded:
			config_response = client.create_notebook_instance_lifecycle_config(
				NotebookInstanceLifecycleConfigName='API_config',
				OnStart=[{'Content': encoded}]
			)
			if config_response:
				print('config created')
				instance_response = client.create_notebook_instance(
					NotebookInstanceName=instance_name,
					InstanceType='ml.t2.medium',
					SubnetId='',
					SecurityGroupIds=[],
					RoleArn='',
					KmsKeyId='',
					Tags=[{'Key': '','Value': ''}],
					LifecycleConfigName='API_config',
					DirectInternetAccess='Enabled',
					VolumeSizeInGB=123,
					AcceleratorTypes=['ml.eia1.medium'],
					DefaultCodeRepository='',
					RootAccess='Enabled'
				)
				if instance_response:
					print('waiting')
					waited = wait_instance(client, instance_name)
					if waited:
						print('instance created')
						return True
	return False

def stop_instance(client, instance_name):
	try:
		response = client.stop_notebook_instance(NotebookInstanceName=instance_name)
	except Exception as e:
		print('Exception: stop_instance', e)
		return False
	return True

def start_instance(client, instance_name):
	try:
		response = client.start_notebook_instance(NotebookInstanceName=instance_name)
	except Exception as e:
		print('Exception: start_instance', e)
		return False
	return True

def wait_instance(client, instance_name):
	print('sagemaker waiters', client.waiter_names)
	waiter = client.get_waiter('instance_created')
	try:
		waiter.wait(
			NotebookInstanceName=instance_name,
			WaiterConfig={
				'Delay': 600,
				'MaxAttempts': 10
			}
		)
	except Exception as e:
		print('Exception: wait_instance', e)
		return False
	return True

def connect_to_instance(client, instance_name):
	''' for ec2/ecs '''
	return False

def install_dependencies(client, connection, instance_name, dependency_type):
	if dependency_type == 'python':
		pass
	elif dependency_type == 'elk':
		pass
	elif dependency_type == 'model':
		pass
	else:
		pass
	return False

def run_tasks(client, connection, instance_name, task_type, params):
	if task_type == 'train':
		model_path = apply_algorithm(params['data'], params['algorithm'])		

	elif task_type == 'deploy_api':
		deployed = deploy_api(params['model_path'])

	elif task_type == 'start_instance':
		start_instance(client, instance_name)

	elif task_type == 'stop_instance':
		stop_instance(client, instance_name)

	elif task_type == 'start_elk':
		pass
	elif task_type == 'stop_elk':
		pass
	elif task_type == 'upload_data':
		upload_data(client, connection, instance_name, params['filename'], params['target_dir'])

	elif task_type == 'import_data':
		data = sanitize_data()
		if data:
			print('len data', len(data))
			import_ratio = import_to_elk('fgt_event', data, '/data/event/')

	elif task_type == 'create_graph':
		graph_data(client, connection, instance_name, params['graph_type'])

	else:
		print('unknown task type')
	return False

def upload_data(client, connection, instance_name, filename, target_dir):
	''' upload data or script in filename '''
	s3_client = boto3.client('s3')
	key_filename = '/'.join([target_dir, filename])
	try:
		response = s3_client.upload_file(key_filename, 'default-bucket')
	except ClientError as e:
		print('s3 upload error', e)
		return False
	return True

''' sample scripts '''

'''
script to spin up aws instance & upload data, run install.py for model dependencies & train.py, and api.py to start api server for model

'''
def deploy_trained_prediction_model():
	client = boto3.client('sagemaker')
	created = create_instance(client)
	if created:
		started = start_instance(client, instance_name)
		connection = connect_to_instance(instance_name)
		if connection:
			uploaded = upload_data(client, connection, instance_name, filename, target_dir)
			for dep_type in ['python', 'model']:
				install_dependencies(client, connection, instance_name, dep_type)
			for task_type in ['upload_data', 'train', 'deploy_api']:
				run_tasks(client, connection, instance_name, task_type, params)

'''
script to spin up aws instance, upload data, run install.py for elk stack & import.py, generate default kibana vieual config & return kibana dashboard url

'''
def deploy_elk_stack():
	client = boto3.client('sagemaker')
	created = create_instance(client)
	if created:
		started = start_instance(client, instance_name)
		connection = connect_to_instance(instance_name)
		if connection:
			uploaded = upload_data(client, connection, instance_name, filename, target_dir)
			for dep_type in ['python', 'elk']:
				install_dependencies(client, connection, instance_name, dep_type)
			for task_type in ['upload_data', 'start_elk', 'import_data']:
				run_tasks(client, connection, instance_name, task_type, params)

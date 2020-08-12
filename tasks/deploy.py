import os, csv, json, uuid, re
import boto3
import pandas as pd
import numpy as np

from import_elk import import_to_elk
from sanitize import sanitize_data

'''
which strategies will the models use?

	- initial version:

		- templates
		- unsupervised learning (k means, nearest neighbors)
		- anomaly detection algorithms
		
	 - secondary version depending on data access:

	 	- intent/cause/meaning model, optionally with assumption/implication/conclusions integrated
	 		- do functions with these intents enable an overall malicious intent when executed in a sequence?
	 		- every resource access, including function calls, is a possible target of a malicious agent
	 		- apply filters on resources (valuable resources, enabling resources, access-granting resources, etc)

	 		- initial implementation can be with object definition routes mapped to language map structures, then to system map structures

	 	- distortion/base model
	 		- given a particular base, what distortion functions apply?

	 	- change model
	 		- is this function or data point in a state of flux or does it clearly fall into a known category?
'''

def create_instance():
	instance_name = 'API_spam'
	on_start_content = None
	with open('on_start.sh', 'r') as f:
		on_start_content = f.read()
		f.close()
	if on_start_content:
		encoded = base64.base64_encode(on_start_content)
		if encoded:
			client = boto3.client('sagemaker')
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

def connect_to_instance():
	return False

def install_dependencies(connection, dependency_type, instance_name):
	if dependency_type == 'python':
		pass
	elif dependency_type == 'elk':
		pass
	elif dependency_type == 'model':
		pass
	else:
		pass
	return False

def run_tasks(connection, task_type, param, instance_name):
	'''
	if task_type == 'train':

	elif task_type == 'start_api':

	elif task_type == 'stop_api':

	elif task_type == 'start_elk':

	elif task_type == 'stop_elk':

	elif task_type == 'upload_data':

	elif task_type == 'import_data':
		data = sanitize_data()
		if data:
			print('len data', len(data))
			import_ratio = import_to_elk('fgt_event', data)

	elif task_type == 'create_graph':
		visualize_data(connection, param, instance_name)

	else:
		print('unknown task type')
	return False
	'''

''' VIZ '''

def visualize_data(connection, visual_type, instance_name):
	''' add options like network graph, word stats, clusters and create an image that can be retrieved by api '''
	image_url = ''
	api_url = ''.join(['https://', instance_ip, 'api_url'])
	if visual_type == 'graph':
		''' create network graph of data '''
		pass
	elif visual_type == 'prediction_function':
		''' graph prediction function with reduced vars '''
		pass
	else:
		print('unknown visual type', visual_type)
	return False

def upload_data(filename, instance_name):
	''' upload data or script in filename '''
	return False

''' sample scripts '''

'''
script to spin up aws instance & upload data, run install.py for model dependencies & train.py, and api.py to start api server for model

'''
def deploy_trained_prediction_model():
	created = create_instance()
	if created:
		started = start_instance(client, instance_name)
		connection = connect_to_instance(instance_name)
		if connection:
			uploaded = upload_data(filename, instance_name)
			for dep_type in ['python', 'model']:
				install_dependencies(connection, dep_type, instance_name)
			for task_type in ['upload_data', 'train', 'start_api']:
				run_tasks(connection, task_type, instance_name)

'''
script to spin up aws instance, upload data, run install.py for elk stack & import.py

'''
def deploy_elk_stack():
	created = create_instance()
	if created:
		started = start_instance(client, instance_name)
		connection = connect_to_instance(instance_name)
		if connection:
			uploaded = upload_data(filename, instance_name)
			for dep_type in ['python', 'elk']:
				install_dependencies(connection, dep_type, instance_name)
			for task_type in ['upload_data', 'start_elk', 'import_data']:
				run_tasks(connection, task_type, instance_name)

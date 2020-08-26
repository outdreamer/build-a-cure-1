import boto3
import sagemaker
import tarfile

from sagemaker import get_execution_role
from sagemaker.tensorflow.model import TensorFlowModel

import logging
logging.basicConfig(level=logging.DEBUG)
root_logger = logging.getLogger()
ch = logging.StreamHandler(sys.stdout)
root_logger.addHandler(ch)

''' deploys an api on instance after:
	1. model training
	2. saving weights
	3. conversion of model to json format '''

def deploy_api(model_path):
	sagemaker_session = sagemaker.Session()
	model = load_model(model_path, sagemaker_session):
	if model:
		deployed_api_url = deploy_api_from_model(role, sagemaker_session)
		if deployed_api_url:
			return deployed_api_url
	return False

def load_model(model_path, model_weights_path, sagemaker_session):
	''' assume role '''
	archive_path = 'model.tar.gz'
	role = get_execution_role()
	loaded_model_json = open(model_path, 'r').read()
	if loaded_model_json:
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights(model_weights_path)
	with tarfile.open(archive_path, mode='w:gz') as archive:
	    archive.add('export', recursive=True)
	try:
		inputs = sagemaker_session.upload_data(path=archive_path, key_prefix='model')
	except Exception as e:
		print('upload compressed model error', e)
	return False

def deploy_api_from_model(role, sagemaker_session):
	''' to do: check if create_endpoint call is needed before using entry_point '''
	''' define entry point to api '''
	with open('entry_point.py', 'w') as f:
		f.write('\n')
		f.close()
	''' define sagemaker predictor object with s3 model file '''
	try:
		s3_model_file = 's3://' + sagemaker_session.default_bucket() + '/model/model.tar.gz'
		sagemaker_model = TensorFlowModel(
				model_data = s3_model_file,
		        role = role,
		        framework_version = '1.12',
		        entry_point = 'entry_point.py'
		)
	except Exception as e:
		print('define api model error', e)
	''' deploy api from sagemaker predictor object '''
	try:
		predictor = sagemaker_model.deploy(initial_instance_count=1, instance_type='ml.t2.medium')
		if predictor:
			''' get endpoint to build arn from deploy response '''
			return predictor
	except Exception as e:
		print('deploy api model error', e)
	return False

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

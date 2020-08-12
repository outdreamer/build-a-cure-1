import boto3
import sagemaker
import tarfile

from sagemaker import get_execution_role
from sagemaker.tensorflow.model import TensorFlowModel

''' this occurs after:
	1. model training
	2. saving weights
	3. conversion of model to json format

	to deploy api on instance '''

def deploy_api(model_path):
	sagemaker_session = sagemaker.Session()
	model = load_model(model_path, sagemaker_session):
	if model:
		deployed_api_url = deploy_api_from_model(role, sagemaker_session)
		if deployed_api_url:
			results = api_test(deployed_api_url)
			if results:
				return True
	return False

def load_model(model_path, sagemaker_session):
	''' assume role '''
	role = get_execution_role()

	''' load model & weights '''
	model_dir = '/home/ec2-user/model/'
	model_path = ''.join([model_dir, 'model.json'])
	model_weights_path =''.join([model_dir, 'weights.h5'])

	loaded_model_json = None
	with open(model_path, 'r') as f:
		loaded_model_json = f.read()
		f.close()
	if loaded_model_json:
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights(model_weights_path)

	''' compress '''
	with tarfile.open('model.tar.gz', mode='w:gz') as archive:
	    archive.add('export', recursive=True)

	''' upload compressed model to s3 '''
	try:
		inputs = sagemaker_session.upload_data(path='model.tar.gz', key_prefix='model')
	except Exception as e:
		print('upload compressed model error', e)

	return False

def deploy_session_api_from_model(role, sagemaker_session):
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
			api_url = ''
			return api_url
	except Exception as e:
		print('deploy api model error', e)

	return False

def api_test(api_url):
	'''
	use aws signature for authorization - requires api secret & access keys, region
	'''
	headers = {'Content-Type': 'application/json'}
	return False
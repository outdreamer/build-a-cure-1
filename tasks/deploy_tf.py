import boto3
import botocore
import paramiko
import requests
from python_terraform import *
import os, sys, time, subprocess, logging

from task_type_resources import get_tf_config
from create_script_for_task import generate_script_for_task

logging.basicConfig(level=logging.DEBUG)
root_logger = logging.getLogger()
ch = logging.StreamHandler(sys.stdout)
root_logger.addHandler(ch)

def run_remote_tasks(params):
	client, connection = connect_to_instance(params)
	if client and connection:
		''' executing commands can be done in userdata, but if not this is another way '''
		execute_script_command = ''.join(['python3 ', params['task_script_path']]) if '.py' in params['task_script_path'] else ''.join([params['task_script_path']])
		stdout, stderr = execute_remote_command(client, execute_script_command)
		if stdout:
			print('executed', execute_script_command, stdout.read())
		if stderr:
			print('execution error', execute_script_command, stderr.read())
	return False

def connect_to_instance(params):
	''' "ssh -o "PasswordAuthentication=no" -i testing.pem root@ip" '''
	keypath = "testing.pem" if os.path.exists("testing.pem") else params['keypath'] if os.path.exists(params['keypath']) else None
	if keypath:
		key = paramiko.RSAKey.from_private_key_file(keypath)
		client = paramiko.SSHClient()
		if client:
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			try:
				connection = client.connect(hostname=params['output_public_ip'], username=params['user'], pkey=key)
				if connection:
					return client, connection
			except Exception as e:
				print('connect exception', e)
	return False, False

def execute_remote_command(client, command):
	if client and command:
		try:
			stdin, stdout, stderr = client.exec_command(command)
			if stdout:
				return stdout, stderr
		except Exception as e:
			print('execute_remote_command exception', e)
	return False, False

def generate_config(params):
	cloud_resources = {'aws': ['ec2', 'ssh']}
	tf_config = get_tf_config(params)
	if tf_config:
		deployment_resources_lines = []
		for category in ['vars', 'resources', 'output']:
			if params['cloud'] in cloud_resources:
				for item in cloud_resources[params['cloud']]:
					if item in tf_config[category]:
						deployment_resources_lines.append('\n'.join(tf_config[category][item]))
		if len(deployment_resources_lines) > 0:
			''' write generated config '''
			open(params['tf_config_path'], 'w').write('\n'.join(deployment_resources_lines))
	return True

def deploy_generated_tf_config(params):
	t = Terraform()
	for command in params['tf_commands']['create']: # validate, init, apply
		print('running tf command', command)
		result = None
		try:
			if command == 'terraform validate':
				result, stdout, stderr = t.validate()
			elif command == 'terraform init':
				result, stdout, stderr = t.init()
			elif command == 'terraform plan':
				result, stdout, stderr = t.plan(out=params['plan_path'], detailed_exitcode=False)
			elif command == 'terraform apply':
				result, stdout, stderr = t.apply(skip_plan=True) #, vars = {'region': params['region']})	
				if stdout and result == 0:
					okeys = {}
					add_flag = 0
					okeys['output_private_key'] = []
					for i, subline in enumerate(stdout.split('\n')):
						if 'output_private_key' in subline:
							add_flag = i
						if 'output_public_ip' not in subline:
							if add_flag > 0 and i >= add_flag:
								okeys['output_private_key'].append(subline.strip())
						else:
							break
					okeys['output_private_key'] = '\n'.join(okeys['output_private_key']).replace('output_private_key = ', '')
					okeys['output_private_key'] = okeys['output_private_key'][0:-1] if okeys['output_private_key'][-1] == '\n' else okeys['output_private_key']
					open('testing.pem', 'w').write(okeys['output_private_key'])
					os.system('chmod 600 testing.pem')
					for line in stdout.split('\n'):
						for ok in params['output_keys']:
							if ok != 'output_private_key' and ok in line:
								okeys[ok] = line.replace(ok, '').replace('=','').strip()
					if okeys:
						return okeys
		except Exception as e:
			print('tf exception', e)
		print('tf command result', command, result) # result is 0 if without error
	return False

def install_local_tf_cloud(params):
	''' install terraform/aws cli on local, awscli & terraform should already be installed from requirements.txt, if not re-run '''
	credential_content = [
		''.join(["[default]\naws_access_key_id=", params['access_key'], "\naws_secret_access_key=", params['secret_key']])
	]
	open(params['credential_path'], 'w').write('\n'.join(credential_content))
	dependencies = {
		'language': {
			'python3 --version': 'brew install python3'
		},
		'package_manager': {
			'pip3 -help': 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py'
		},
		'script': {
			'terraform -help': 'brew install terraform', 
			'aws --version': 'pip3 install -r requirements.txt'
		}
	}
	install_commands = []
	for dependency_type in ['script']: #['language', 'package_manager', 'script']:
		for program, install_command in dependencies[dependency_type].items():
			try:
				tf_installed_result = subprocess.check_output(program, shell = True)
			except Exception as e:
				print('dependency not installed exception', e) # Command 'terraform -help' returned non-zero exit status 127
				install_commands.append(install_command)	
				try:
					result = os.system(command)
					print('install_tf_cloud env vars result', command, result)
				except Exception as e:
					print('install error', e)
	return True

def mkdir_structure(file_path, params):
	folders = []
	folders_path = ''
	for folder in file_path.split('/')[0:-1]: # skip last item which is assumed to be a file
		folders.append(folder)
		user_dir = '/'.join(os.getcwd().split('/')[0:3])
		folders_path = ''.join([user_dir, '/'.join(folders)])
		if not os.path.isdir(folders_path):
			os.mkdir(folders_path)
	folders_path = ''.join([folders_path, '/'])
	return folders_path

def open_output_in_browser(ip, params):
	''' open notebook/api graph or elk kibana login '''
	host = ''.join(['ec2-', ip.replace('.','-'), '.', params['region'], '.compute.amazonaws.com']) if params['cloud'] == 'ec2' else ip
	url = ''.join(['http://', host, ':5601']) if params['task'] == 'elk' else ''.join(['http://', host, '/api/predict-test'])
	response = None
	try:
		response = requests.get(url) #, params = {}, args = {})
	except Exception as e:
		print('request error', url, e)
	if response:
		print('response', url, response)
		if response.status_code == 200:
			webbrowser.open(url, new=0, autoraise=True) # webbrowser.get('firefox').open_new_tab(url)
			return True
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

''' to do: create install scripts install_boot_elk.sh and install_boot_model.sh '''
def deploy(params):
	''' make sure local has terraform & cloud cli's installed '''
	local_install = install_local_tf_cloud(params)
	if local_install:
		print('installed cloud config, env var, python3 pip reqs for this script')
		''' specify task dependencies in the install.sh for the task '''
		install_script = generate_script_for_task(params)
		if install_script:
			''' generate terraform config with resources & install script for the task '''
			configured = generate_config(params) 
			if configured:
				print('generated config at config_path', params['tf_config_path'])
				''' create resources & execute install script '''
				output_keys = deploy_generated_tf_config(params)
				if output_keys:
					print('deployed resources with output', output_keys)
					for ok, val in output_keys.items():
						params[ok] = val

					''' save ec2 id for cleanup task '''
					output_tracker = '\n'.join([''.join([key, '=', params[key]]) for key in ['output_instance_id'] if key in params])
					if output_tracker:
						open('output.txt', 'w').write(output_tracker)

					''' to do: add waiter for resource creation '''
					''' open generated resources '''
					for i in range(0, 20):
						print('trying to connect to url', i, output_keys['output_public_ip'])
						opened = open_output_in_browser(output_keys['output_public_ip'], params)
						if not opened:
							time.sleep(60)
						else:
							return params
			else:
				print('could not deploy')
	return False

def remove_generated_config(params):
	for file_to_mkdir in ['credential_path', 'keypath']:
		if 'key' not in file_to_mkdir:
			folder_created = mkdir_structure(params[file_to_mkdir], params)
			if folder_created:
				params[file_to_mkdir] = ''.join([folder_created, '', params[file_to_mkdir].split('/')[-1]])
		user_dir = '/'.join(os.getcwd().split('/')[0:3])
		params[file_to_mkdir] = '/'.join([user_dir, params[file_to_mkdir]]) if user_dir not in params[file_to_mkdir] else params[file_to_mkdir]
		if os.path.exists(params[file_to_mkdir]):
			os.remove(params[file_to_mkdir]) # remove original file if you need to re-create on each run
	for file_to_remove in ['tf_config_path', 'plan_path']:
		if os.path.exists(params[file_to_remove]):
			os.remove(params[file_to_remove]) # remove original file if you need to re-create on each run
	return params

def destroy_resources(params):
	''' to do: delete tls_private_key '''
	exceptions = []
	instance_ids = []
	if os.path.exists('output.txt'):
		data = open('output.txt', 'r').readlines()
		instance_ids = [line.split('=')[1] for line in data if line.split('=')[0] == 'output_instance_id']
	ec2 = boto3.client('ec2')
	iam = boto3.client('iam')
	key_name = 'deploy_key'
	try:
		deleted_key_pair = ec2.delete_key_pair(KeyName=key_name)	
	except Exception as e:
		print('key pair exception', e)
		exceptions.append('_'.join(['key pair', key_name]))
	try:
		if len(instance_ids) > 0:
			deleted_ec2_instance = ec2.terminate_instances(InstanceIds=instance_ids)
			if deleted_ec2_instance:
				os.path.remove('output.txt')
	except Exception as e:
		print('ec2 exception', e)
		exceptions.append('_'.join(['ec2', ','.join([instance_ids])]))
	try:
		deleted_sg = ec2.delete_security_group(GroupName='ec2_sg')
	except Exception as e:
		print('sg exception', e)
		exceptions.append('_'.join(['sg', 'ec2_sg']))
	try:
		removed_role = iam.remove_role_from_instance_profile(InstanceProfileName='ec2_profile', RoleName='ec2_role')
	except Exception as e:
		print('remove role from instance profile exception', e)
		exceptions.append('_'.join(['iam role-profile', 'ec2_profile', 'ec2_role']))
	try:
		deleted_instance_profile = iam.delete_instance_profile(InstanceProfileName='ec2_profile')
	except Exception as e:
		print('instance profile exception', e)
		exceptions.append('_'.join(['iam profile', 'ec2_profile', 'ec2_role']))
	try:
		deleted_role = iam.delete_role(RoleName='ec2_role')
	except Exception as e:
		print('role exception', e)
		exceptions.append('_'.join(['iam role', 'ec2_profile', 'ec2_role']))
	if len(exceptions) == 0:
		return True
	return exceptions

params = {'cloud': 'aws', 'task': 'elk', 'instance': 'demo', 'secret_key': '', 'access_key': '', 'keypath': ''}
params['tagname'] = ''.join(['task_', '_', params['task']])

params['credential_path'] = '/.aws/credentials_tf/credentials.ini'
params['tf_config_path'] = ''.join([os.getcwd(), '/', params['cloud'], '_', params['task'], '_config.tf'])
params['plan_path'] = params['tf_config_path'].replace('_config.tf', '_plan_config.bin')
params['task_script_path'] = ''.join([os.getcwd(), '/', params['task'], '.py']) if params['task'] not in ['elk', 'model'] else ''.join(['install_', params['task'], '.sh'])

params['ami'] = 'ami-0baeabdd230a4e508' # centos 7
params['region'] = 'us-west-2'
params['user'] = 'ec2-user' if params['cloud'] == 'aws' else ''
params['remote_dir'] = '/home/ec2-user' if params['cloud'] == 'aws' else ''
params['instance_type'] = 't2.micro' if params['task'] == 'elk' else 'm2.medium'
params['output_keys'] = ['output_public_ip', 'output_instance_id', 'output_private_key']

params['tf_commands'] = {
	'check': 'terraform -help', 
	'create': ['terraform init', 'terraform validate', 'terraform plan', 'terraform apply'], 
	'view': ['terraform show'], 
	'destroy': ['terraform destroy']
}

stored_env = {}
for i, arg in enumerate(sys.argv):
	if (i + 1) < len(sys.argv):
		if 'secret' in arg:
			params['secret_key'] = sys.argv[i + 1]
		elif 'access' in arg:
			params['access_key'] = sys.argv[i + 1]
		for key in ['cloud', 'task', 'region', 'tagname']:
			if key in arg:
				params[key] = sys.argv[i + 1]
		if 'remove_config' in arg:
			if sys.argv[i + 1] == "1":
				''' flag to remove previously generated terraform config/plan, generated keys/credentials from previous sys.argv '''
				params = remove_generated_config(params)
		if 'destroy_before_run' in arg:
			if sys.argv[i + 1] == "1":
				params['destroy_before_run'] = "1"
		if 'destroy_after_run' in arg:
			if sys.argv[i + 1] == "1":
				params['destroy_after_creation'] = "1"

if params['access_key'] != '' and params['secret_key'] != '':

	params['env'] = {
		'AWS_SHARED_CREDENTIALS_FILE': params['credential_path'], 
		'AWS_REGION': params['region'], 
		'AWS_DEFAULT_REGION': params['region'], 
		'AWS_ACCESS_KEY_ID': params['access_key'], 
		'AWS_SECRET_ACCESS_KEY': params['secret_key']
	}

	for env, val in params['env'].items():
		stored_env[env] = os.environ.get(env)
		os.environ[env] = val

	if 'destroy_before_run' in params:

		if params['destroy_before_run'] == '1':
			destroyed = destroy_resources(params)
			if destroyed:
				print('resources removed before run', destroyed)

	if 'task' in params:

		print('running task', params['task'], ' with params', params)

		if params['task'] not in ['elk', 'model']:
			ran_task = run_remote_task(params)
			print('ran task', ran_task)
		else:
			deploy_params_to_clean = deploy(params)
			if deploy_params_to_clean:
				print('deploy_params_to_clean', deploy_params_to_clean)

	if 'env' in params:

		''' cleanup task to remove access & secret key from env vars or restore previous config for those env vars '''
		for env, val in params['env'].items():
			os.environ[env] = '' if env not in stored_env else stored_env[env] if stored_env[env] is not None else ''

	if 'destroy_after_run' in params:

		if params['destroy_after_run'] == '1':
			destroyed = destroy_resources(params)
			if destroyed:
				print('resources removed after run', destroyed)

import boto3
import botocore
import paramiko
import requests
import webbrowser
from python_terraform import *
import os, sys, time, subprocess, logging

from task_type_resources import get_tf_config
from create_script_for_task import generate_script_for_task
from sanitize import json_to_csv
from import_elk import import_to_elk

logging.basicConfig(level=logging.DEBUG)
root_logger = logging.getLogger()
ch = logging.StreamHandler(sys.stdout)
root_logger.addHandler(ch)

def run_remote_task(params):
	''' tasks include: data upload/import/download, service setup/management, scheduled bulk operations/queries/reports 
	import: requires data_path & service (logstash/elasticsearch) params
	upload/download: requires source/destination params
	train_model: requires data source & algorithm params

	to do: add logging to output.txt of errors in functions applied as one-line commands like apply_algorithm or create_graph
	'''
	command = None

	client = connect_to_instance(params)
	if client:
		''' executing commands can be done in userdata, but if not this is another way '''
		command = ''.join(['python3 ', params['task_script_path']]) if '.py' in params['task_script_path'] else ''.join([params['task_script_path']])
		if params['task'] == 'start_elk':
			command = 'systemctl start elasticsearch'
		elif params['task'] == 'stop_elk':
			command = 'systemctl stop elasticsearch'
		elif params['task'] == 'start_api':
			command = 'flask run' # 'sagemaker start
		elif params['task'] == 'stop_api':
			command = '' # sagemaker stop
		elif params['task'] == 'model':
			command = ''.join(["python3 -c apply_algorithm(", params['data'], ", ", params['algorithm'], ")"])
		elif params['task'] == 'create_graph':
			''' this should have params like data set, dependent var, graph type, which we'll translate to matplotlib graph layers, axis labels, etc '''
			command = ''.join(["python3 -c graph_data(", params['graph_type'], ")"])
		else:
			print('unsupported task', params)
		if command:
			stdout, stderr = execute_remote_command(client, command)
			if stdout:
				print('executed', execute_script_command, stdout.read())
			if stderr:
				print('execution error', execute_script_command, stderr.read())
	return False

def connect_to_instance(params):
	''' "ssh -o "PasswordAuthentication=no" -i testing.pem root@ip" '''
	if 'keypath' in params:
		if params['keypath'] != '' and os.path.exists(params['keypath']):
			key = paramiko.RSAKey.from_private_key_file(params['keypath'])
			client = paramiko.SSHClient()
			if client:
				client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				try:
					task_ip_output = '_'.join([params['task'], 'output_public_ip'])
					connection = client.connect(hostname=params[task_ip_output], username=params['user'], pkey=key)
					if connection:
						return client
				except Exception as e:
					print('connect exception', e)
	return False

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
	params['my_ip_addr'] = None
	if os.path.exists('ip.txt'):
		params['my_ip_addr'] = open('ip.txt', 'r').read()
	if params['my_ip_addr'] is None or params['my_ip_addr'] == '':
		os.system("curl ipecho.net/plain >> ip.txt")
		if os.path.exists('ip.txt'):
			params['my_ip_addr'] = open('ip.txt', 'r').read()
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
	for command in ['terraform init', 'terraform validate', 'terraform plan', 'terraform apply']: # validate, init, apply
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
					task_key_output = '_'.join([params['task'], 'output_private_key'])
					task_ip_output = '_'.join([params['task'], 'output_public_ip'])

					''' add key in output '''
					okeys[task_key_output] = []
					for i, subline in enumerate(stdout.split('\n')):
						if task_key_output in subline:
							add_flag = i
						if task_ip_output not in subline:
							if add_flag > 0 and i >= add_flag:
								okeys[task_key_output].append(subline.strip())
						else:
							break
					okeys[task_key_output] = '\n'.join(okeys[task_key_output]).replace(task_key_output, '').replace(' = ', '')
					okeys[task_key_output] = okeys[task_key_output][0:-1] if okeys[task_key_output][-1] == '\n' else okeys[task_key_output]

					print('generated key', okeys[task_key_output])
					open(params['keypath'], 'w').write(okeys[task_key_output])

					os.system(''.join(['chmod 600 ', params['keypath']]))
					for line in stdout.split('\n'):
						for ok in params['output_keys']:
							if ok != task_key_output and ok in line:
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
		if params['user_dir'] not in folders_path:
			folders_path = ''.join([params['user_dir'], '/'.join(folders)])
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

def deploy(params):
	''' make sure local has terraform & cloud cli's installed '''
	local_install = install_local_tf_cloud(params)
	if local_install:
		print('installed cloud config, env var, python3 pip reqs for this script')
		''' specify task dependencies in the install.sh for the task '''
		install_script = generate_script_for_task(params)
		if install_script:
			print('generated task script at task_script_path', install_script)
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
					task_id_output = '_'.join([params['task'], 'output_instance_id'])
					output_tracker = ''.join([task_id_output, '=', params[task_id_output]])
					if output_tracker:
						open('output.txt', 'w').write(output_tracker)

					''' to do: add waiter for resource creation '''
					''' open generated resources '''
					for i in range(0, 20):
						task_ip_output = '_'.join([params['task'], 'output_public_ip'])
						print('trying to connect to url', i, output_keys[task_ip_output])
						opened = open_output_in_browser(output_keys[task_ip_output], params)
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
	for file_to_remove in ['tf_config_path', 'plan_path']:
		if file_to_remove in params:
			if params['user_dir'] not in params[file_to_remove]:
				params[file_to_remove] = '/'.join([params['user_dir'], params[file_to_remove]])
			if os.path.exists(params[file_to_remove]):
				os.remove(params[file_to_remove]) # remove original file if you need to re-create on each run
	return params

def destroy_resources(params, before_after):

	exceptions = []
	functions = {
		'ec2': {
			'terminate_instances': ['InstanceIds'], 
			'delete_key_pair': ['KeyName'],
			'delete_security_group': ['GroupName']
		},
		'iam': {
			'remove_role_from_instance_profile': ['InstanceProfileName', 'RoleName'], 
			'delete_instance_profile': ['InstanceProfileName'],
			'delete_role': ['RoleName']
		}
	}
	iam_functions = ['remove_role_from_instance_profile', 'delete_instance_profile', 'delete_role']

	for task in params['all_tasks']:

		print('task', task)
		instance_ids = []
		task_id_output = ''.join([task, '_output_instance_id'])
		if task_id_output in params:
			instance_ids = [params[task_id_output]] if params[task_id_output] != '' else []
		if params['task'] == 'destroy_before_run' and before_after == 'before':
			if os.path.exists('output.txt'):
				data = open('output.txt', 'r').readlines()
				for line in data:
					if line.split('=')[0] == task_id_output:
						instance_ids.append(line.split('=')[1].replace('\n',''))
		args = {
			'InstanceProfileName': ''.join([task, '_ec2_profile']),
			'RoleName': ''.join([task, '_ec2_role']), 
			'InstanceIds': instance_ids, 
			'KeyName': 'deploy_key', 
			'GroupName': ''.join([task, '_ec2_sg'])
		}

		''' iam has order-dependent actions '''
		for service_name, function_dict in functions.items():
			if service_name == 'iam':
				for function_name in iam_functions:
					parameters = functions[service_name][function_name]
					new_exceptions = execute_function(parameters, args, service_name, function_name, function_dict)	
					if len(new_exceptions) > 0:
						exceptions.append(new_exceptions)				
			else:
				for function_name, parameters in function_dict.items():
					new_exceptions = execute_function(parameters, args, service_name, function_name, function_dict)	
					if len(new_exceptions) > 0:
						exceptions.append(new_exceptions)	
	cwd = os.getcwd()
	for cur, _dirs, files in os.walk(cwd):
		for original_filename in files:
			filename = ''.join([cur, '/', original_filename])
			if filename[-3:] == '.tf' or filename[-3:] == '.sh':
				os.remove(filename)
				print('destroy_resources: removed', filename)
			elif 'ip.txt' in filename or 'output.txt' in filename:
				os.remove(filename)
			#elif 'testing.pem' in filename:
			#	os.remove(filename)
	if len(exceptions) == 0:
		return True
	return exceptions

def execute_function(parameters, args, service_name, function_name, function_dict):
	service = None
	exceptions = []
	ec2 = boto3.client('ec2')
	iam = boto3.client('iam')
	key_vals = {key: args[key] for key in parameters}
	key_val_str = ','.join([':'.join([key, val]) if type(val) == str else ':'.join([key, ','.join(val)]) for key, val in key_vals.items()])
	try:
		service = boto3.client(service_name)
	except Exception as e:
		print('service not found', e)
		exceptions.append(''.join(['service not found', service_name]))
	if service is not None:
		try:
			function_call = getattr(service, function_name)(**key_vals)
			if function_call:
				print('destroy function_call', function_call)
		except Exception as e:
			print('destroy function call error', e)
			if 'response' in dir(e):
				message = e.response['Error']['Message'] if 'Error' in e.response and 'Message' in e.response['Error'] else ''
				exceptions.append('::'.join(['destroy function call error ', service_name, function_name, key_val_str, message]))
			else:
				exceptions.append('::'.join(['destroy function call error ', service_name, function_name, key_val_str]))
	return exceptions

def get_params_from_args(args, params):
	for i, arg in enumerate(args):
		if (i + 1) < len(args):
			if 'secret' in arg:
				params['secret_key'] = args[i + 1]
			elif 'access' in arg:
				params['access_key'] = args[i + 1]
			for key in ['cloud', 'task', 'region', 'tagname']:
				if key in arg:
					params[key] = args[i + 1]
	params['env'] = {
		'AWS_SHARED_CREDENTIALS_FILE': params['credential_path'], 
		'AWS_REGION': params['region'], 
		'AWS_DEFAULT_REGION': params['region'], 
		'AWS_ACCESS_KEY_ID': params['access_key'], 
		'AWS_SECRET_ACCESS_KEY': params['secret_key']
	}
	stored_env = {}
	for env, val in params['env'].items():
		stored_env[env] = os.environ.get(env)
		os.environ[env] = val
	return params, stored_env
	



params = {'cloud': 'aws', 'task': '', 'secret_key': '', 'access_key': '', 'keypath': ''}
local_tasks = ['destroy_before_run', 'destroy_after_run', 'remove_config', 'import', 'upload', 'download', 'elk']
remote_tasks = ['stop_elk', 'start_elk', 'start_api', 'stop_api', 'model']
params['all_tasks'] = [item for item in local_tasks]
params['all_tasks'].extend(remote_tasks)

params['user_dir'] = '/'.join(os.getcwd().split('/')[0:3])
params['credential_path'] = ''.join([params['user_dir'], '/.aws/credentials_tf/credentials.ini'])
params['keypath'] = 'testing.pem'
params['ami'] = 'ami-0baeabdd230a4e508' # centos 7
params['region'] = 'us-west-2'
params['user'] = 'ec2-user' if params['cloud'] == 'aws' else ''
params['remote_dir'] = '/home/ec2-user' if params['cloud'] == 'aws' else ''

params, stored_env = get_params_from_args(sys.argv, params)

task_key_output = '_'.join([params['task'], 'output_private_key'])
task_ip_output = '_'.join([params['task'], 'output_public_ip'])
task_id_output = '_'.join([params['task'], 'output_instance_id'])
params['output_keys'] = [task_ip_output, task_id_output, task_key_output]
params['remote_ip'] = ''

# import task
params['es_host'] = 'localhost' # check that you can import to remote from local, otherwise set for internal requests on server
params['data_path'] = '/data/event/'
params['index_name'] = 'fgt_event'
# upload/download task
params['source'] = ''
params['target'] = ''
# train model task
params['data_path'] = ''

if params['access_key'] != '' and params['secret_key'] != '':
	if 'task' in params:
		if params['task'] != '':
			print('running task', params['task'], ' with params', params)
			if params['task'] == 'destroy_before_run' or params['task'] == 'destroy_after_run':
				timing = 'after' if params['task'] == 'destroy_after_run' else 'before'
				destroyed = destroy_resources(params, timing)
				if destroyed:
					print('resources removal exceptions ', timing, ' run: ', destroyed)
			elif params['task'] == 'remove_config':
				''' remove previously generated terraform config/plan, generated keys/credentials '''
				#params = remove_generated_config(params)
				pass
			elif params['task'] == 'import':
				data = json_to_csv(params['data_path'])
				if data:
					params['data'] = data
					print('len data to import', len(params['data']))
					import_ratio = import_to_elk(params)
					print('import_ratio', import_ratio)
			elif params['task'] == 'upload':
				upload_command = ''.join(['scp -o "PasswordAuthentication=no" -i ', params['keypath'], ' ', params['source'], ' ', params['user'], '@', params['remote_ip'], ':', params['target']])
				os.system(upload_command)
			elif params['task'] == 'download':
				download_command = ''.join(['scp -o "PasswordAuthentication=no" -i ', params['keypath'], ' ', params['user'], '@', params['remote_ip'], ':', params['target'], ' ', params['source']])
				os.system(download_command)
			elif params['task'] == 'test':
				pass
			elif params['task'] in ['elk', 'model']:
				''' remove previously generated terraform config/plan, generated keys/credentials '''
				params = remove_generated_config(params)
				params['task_script_path'] = ''.join([os.getcwd(), '/', params['task'], '.py']) if params['task'] not in ['elk', 'model'] else ''.join(['install_', params['task'], '.sh'])
				params['tagname'] = ''.join(['task_', params['task']])
				params['tf_config_path'] = ''.join([os.getcwd(), '/', params['cloud'], '_', params['task'], '_config.tf'])
				params['instance_type'] = 'm5.large' if params['task'] == 'model' else 't2.medium'
				params['plan_path'] = params['tf_config_path'].replace('_config.tf', '_plan_config.bin')
				deploy_params_to_clean = deploy(params)
				if deploy_params_to_clean:
					print('deploy_params_to_clean', deploy_params_to_clean)
			elif params['task'] in remote_tasks:
				ran_task = run_remote_task(params)
				if ran_task:
					print('ran task', ran_task)
	if 'env' in params:
		''' cleanup task to remove access & secret key from env vars, and restore previous config for those env vars if any found '''
		for env, val in params['env'].items():
			os.environ[env] = '' if env not in stored_env else stored_env[env] if stored_env[env] is not None else ''

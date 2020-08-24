import boto3
import botocore
import paramiko
from python_terraform import *
import os, sys, subprocess	

''' to add remote_exec rather than user data, add tf_command_lines to tf config output to a resource
remote_commands = open(task_script_path, 'r').readlines()
remote_tf_exec_commands = ["  provisioner \"remote-exec\" {", "	inline = ["]
for command in remote_commands:
	remote_tf_exec_commands.append(''.join(["	  \"", command, "\","]))
remote_tf_exec_commands.extend(["	]", "  }"])

add_connection_lines = [
	"  provisioner \"remote-exec\" {",
	"    script        = \"${path.module}/elasticsearch.sh\"",
	"\n",   
	"    connection {",
	"      type        = \"ssh\""<
	"      user        = \"ubuntu\"",
	"      private_key = \"${var.private_key}\"",
	"    }",
	"  }"
]

config_content = [
	''.join(["[default] aws_access_key_id=", default_access_key,  " aws_secret_access_key=", default_secret_key]),
	''.join(["[profile testing] aws_access_key_id=", access_key, " aws_secret_access_key=", secret_key, " region=", region])
]
config_path = "~/.aws/config/config.ini"
connection = connect_to_instance(ip, params['keypath'], params['user'])
if connection:
	executing commands should be done in userdata
	install_boot_command = ''.join(['cd ', '/home/', params['user'], ' && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build-a-cure/ && ./install_boot_', params['task'], '.sh', 
	executed, err = execute_remote_command(install_boot_command, connection)

def connect_to_instance(ip, params):
	key = paramiko.RSAKey.from_private_key_file(params['keypath'])
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		connection = client.connect(hostname=ip, username=params['user'], pkey=key)
		if connection:
			return connection
	except Exception as e:
		print('connect exception', e)
	return False

def execute_remote_command(command, connection):
	# execute install command on instance
	try:
		stdin, stdout, stderr = client.exec_command(command)
		if stdout:
			print('executed command', command, stdout.read(), stderr)
			return stdout, stderr
	except Exception as e:
		print('execute_command exception', e)
	return False, False
'''

def get_tf_config(params):
	tf_config = {
		'vars': {
			'ssh': [
				"variable \"keypath\" {",
				"  description = \"Path to SSH private key to SSH-connect to instances\"",
				''.join(["  default = \"", params['keypath'], "\""]),
				"}"
			]
		},
		'resources': {
			'ssh': [
				"connection {",
				"	type	 = \"ssh\"",
				''.join(["	user	 = \"", params['user'], "\""]),
				"	private_key = file(var.keypath)",
				"	host	 = aws_instance.task_ec2_instance.public_ip",
				"}",
				"resource \"aws_key_pair\" \"task_key_pair\" {",
				"  key_name   = \"terraform-demo\"",
				''.join(["  public_key = file(\"", params['pub_key_path'], "\")"]),
				"}"
			]
		},
		'remote_exec': [], # alt to userdata or remote session login with connect_to_instance
		'output': {}
	}
	tf_config = {
		'vars': {},
		'resources': {
			'ec2': [
				"resource \"aws_instance\" \"task_ec2_instance\" {",
				''.join(["  ami		   = \"", params['ami'], "\""]),
				''.join(["  instance_type = \"", params['instance_type'], "\""]),
				''.join(["  user_data	 = file(\"", params['task_script_path'], "\")"]),
				"  tags = {",
				''.join(["    Name  = \"", params['tagname'], "\""]),
				"  }",
				"}"
			]
		},
		'output': {
			'ec2': [
				"output \"output_public_ip\" {",
				"  value = aws_instance.task_ec2_instance.public_ip",
				"}"
			]
		}
	}
	return tf_config

def generate_config(params):
	deployment_resources_lines = []
	aws_resource_list = ['ec2', 'ssh']
	tf_config = get_tf_config(params)
	if tf_config:
		for category in ['vars', 'resources', 'output']:
			for item in aws_resource_list:
				if item in tf_config[category]:
					deployment_resources_lines.append('\n'.join(tf_config[category][item]))
		if len(deployment_resources_lines) > 0:
			''' write generated config '''
			open(params['tf_config_path'], 'w').write('\n'.join(deployment_resources_lines))
	return True

def deploy_generated_tf_config(params):
	tf_commands = {
		'check': 'terraform -help', 
		'create': ['terraform init', 'terraform validate', 'terraform apply'], 
		'view': ['terraform show'], 
		'destroy': ['terraform destroy']
	}
	t = Terraform()
	for command in tf_commands['create']: # validate, init, apply
		print('running tf command', command)
		result = None
		try:
			if command == 'terraform validate':
				result, stdout, stderr = t.validate(vars = {'region': params['region']})
			elif command == 'terraform init':
				result, stdout, stderr = t.init(vars = {'region': params['region']})
			elif command == 'terraform apply':
				result, stdout, stderr = t.apply(vars = {'region': params['region']})
		except Exception as e:
			print('tf exception', e)
		print('tf command result', command, result) # result is 0 if without error
		if command == 'apply':
			for line in result.readlines():
				print('stdout line', line)
				if output_key in line:
					print('\n\n****found line with output_key', line)
					return line.replace(output_key, '').strip()
	return False

def install_local_tf_cloud(params):
	''' install terraform/aws cli on local, awscli & terraform should already be installed from requirements.txt, if not re-run '''
	credential_content = [
		''.join(["[default] aws_access_key_id=", params['access_key'], " aws_secret_access_key=", params['secret_key']]), 
		''.join(["[testing] aws_access_key_id=", params['access_key'], " aws_secret_access_key=", params['secret_key']])
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
	for env, val in params['env'].items():
		os.environ[env] = val
	return True

def mkdir_structure(file_path, params):
	folders = []
	folders_path = ''
	for folder in file_path.split('/')[0:-1]: # skip last item which is assumed to be a file
		folders.append(folder)
		folders_path = ''.join([params['user_dir'], '/', '/'.join(folders)])
		if not os.path.isdir(folders_path):
			os.mkdir(folders_path)
	return folders_path

def generate_key(keypath):
	''' ssh-keygen -t rsa, keypath, 'N' for passphrase skip, Enter '''
	keygen = None
	try:
		keygen = paramiko.RSAKey.generate(1024)
	except Exception as e:
		print('generate key error', e)
	if keygen:
		open(params['keypath'], 'w').write('')
		keygen.write_private_key_file(keypath)
		pub_key_path = keypath.replace('.pem', '.pub')
		open(pub_key_path ,"w").write(keygen.get_base64())
		return keypath
	return False

def open_output_in_browser(ip, params):
	''' open notebook/api graph or elk kibana login '''
	url = ''.join(['http://', ip, ':5601']) if params['task'] == 'elk' else ''.join(['http://', ip, '/api/predict-test'])
	response = requests.get(url) #, params = {}, args = {})
	if response:
		print('response', url, response)
		if response.status_code == 200:
			webbrowser.open(url, new=0, autoraise=True) # webbrowser.get('firefox').open_new_tab(url)
	return False

''' to do: create install scriptss install_boot_elk.sh and install_boot_model.sh '''
def deploy(params):
	generated = generate_key(params['keypath'])
	if generated:
		print('generated key', generated)
		local_install = install_local_tf_cloud(params)
		if local_install:
			print('installed aws config, env var, pip reqs')
			configured = generate_config(params)
			if configured:
				print('generated config at config_path', params['tf_config_path'])
				output_key = deploy_generated_tf_config(params)
				if output_key:
					print('deployed resources with output', output_key)
					open_output_in_browser(output_key, params)
				else:
					print('could not deploy')
	return False

''' 
- task 'elk', requires ecs with python requirements.txt install
- task 'model' requires xgboost, hardware of a certain size, python requirements.txt 
'''

params = {'cloud': 'aws', 'task': 'elk', 'instance': 'demo'}
params['user_dir'] = '/'.join(os.getcwd().split('/')[0:3])
params['keypath'] = ''.join([params['user_dir'], '/tf_deploy.pem'])
params['pub_key_path'] = params['keypath'].replace('.pem', '.pub')
params['credential_path'] = '/.aws/credentials/credentials.ini'
params['tf_config_path'] = ''.join([os.getcwd(), '/', params['cloud'], '_', params['task'], '_config.tf'])

for file_to_remove in ['credential_path', 'keypath', 'pub_key_path']:
	if 'key' not in file_to_remove:
		folder_created = mkdir_structure(params[file_to_remove], params)
		if folder_created:
			params[file_to_remove] = ''.join([folder_created, '/', params[file_to_remove].split('/')[-1]])
	params[file_to_remove] = '/'.join([params['user_dir'], params[file_to_remove]]) if params['user_dir'] not in params[file_to_remove] else params[file_to_remove]
	if os.path.exists(params[file_to_remove]):
		os.remove(params[file_to_remove]) # remove original file if you need to re-create on each run

params['secret_key'] = ''
params['access_key'] = ''
params['ami'] = 'ami-024d1b90da07e64a6' # python3 with flask installed, centos 7 087c4938c7f618b53
params['region'] = 'us-west-2'
params['user'] = 'ec2-user' if params['cloud'] == 'aws' else None
params['instance_type'] = 't2.micro' if params['task'] == 'elk' else 'm2.medium'
params['output_key'] = 'output_public_ip'
params['tagname'] = ''.join(['task_ec2_instance', '_', params['task']])
params['task_script_path'] = ''.join([os.getcwd(), '/', 'tasks/install_boot_', params['task'], '.sh'])
for i, arg in enumerate(sys.argv):
	if (i + 1) < len(sys.argv):
		if 'secret' in arg:
			params['secret_key'] = sys.argv[i + 1]
		elif 'access' in arg:
			params['access_key'] = sys.argv[i + 1]
if params['access_key'] != '' and params['secret_key'] != '':
	params['env'] = {'AWS_SHARED_CREDENTIALS_FILE': params['credential_path'], 'AWS_REGION': params['region'], 'AWS_ACCESS_KEY_ID': params['access_key'], 'AWS_SECRET_ACCESS_KEY': params['secret_key']}
	deploy(params)
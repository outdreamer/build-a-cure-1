import boto3
import botocore
import paramiko
import requests
from python_terraform import *
import os, sys, time, subprocess, logging

logging.basicConfig(level=logging.DEBUG)
root_logger = logging.getLogger()
ch = logging.StreamHandler(sys.stdout)
root_logger.addHandler(ch)

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

def generate_key(keypath):
	OpenSSH public key format (the format in ~/.ssh/authorized_keys). If you connect using SSH while using the EC2 Instance Connect API, the SSH2 format is also supported.
	Base64 encoded DER format
	SSH public key file format as specified in RFC4716
	SSH private key file format must be PEM (for example, use ssh-keygen -m PEM to convert the OpenSSH key into the PEM format)
	# ssh-keygen -t rsa -b 4096 -f
	gen_key = ''.join(['ssh-keygen -P "" -t rsa -b 2048 -m pem -f ', params['keypath']])
	generated = subprocess.check_output(gen_key, shell=True)
	os.system(''.join(["chmod 400 ", params['keypath']]))
	convert = ''.join(['ssh-keygen -f ', params['keypath'], ' -e -m pem'])
	# ssh-keygen -y -f /path_to_key_pair/my-key-pair.pem - get pub key
	converted = subprocess.check_output(convert, shell=True)
	open(params['pub_key_path'], 'w').write(converted.decode('utf-8'))
	os.system(''.join(["chmod 600 ", params['pub_key_path']]))
	ec2 = boto3.client('ec2')
	keypair = ec2.create_key_pair(KeyName='deploy_key') # 'KeyMaterial' : An unencrypted PEM encoded RSA private key.
	if keypair:
		open(params['keypath'], 'w').write(keypair['KeyMaterial'])
		os.system(''.join(["chmod 400 ", params['keypath']]))
		convert = ''.join(['ssh-keygen -y -f ', params['keypath'], ' > ', params['pub_key_path']])
		converted = subprocess.check_output(convert, shell=True)
		# open(params['pub_key_path'], 'w').write(converted.decode('utf-8'))
		os.system(''.join(["chmod 600 ", params['pub_key_path']]))
	return keypath
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
			]
		},
		'remote_exec': [], # alt to userdata or remote session login with connect_to_instance
		'output': {}
	}
	'''
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": ["*"]
	'''
	tf_config = {
		'vars': {},
		'resources': {
			'ec2': [
				"provider \"aws\" {",
				''.join(["  region  = \"", params['region'], "\""]),
				''.join(["  shared_credentials_file = \"", params['credential_path'], "\""]),
				"}",
				"",
				"resource \"aws_security_group\" \"ec2_sg\" {",
				"  name   = \"ec2_sg\"# SSH access from anywhere",
				"  ingress {",
				"    from_port   = 22",
				"    to_port     = 22",
				"    protocol    = \"tcp\"",
				"    cidr_blocks = [\"0.0.0.0/0\"]",
				"  }",
				"  ingress {",
				"    from_port   = 80",
				"    to_port     = 80",
				"    protocol    = \"tcp\"",
				"    cidr_blocks = [\"0.0.0.0/0\"]",
				"  }",
				"   ingress {",
				"    from_port   = 5601",
				"    to_port     = 5601",
				"    protocol    = \"tcp\"",
				"    cidr_blocks = [\"0.0.0.0/0\"]",
				"  }",
				"   ingress {",
				"    from_port   = 9200",
				"    to_port     = 9200",
				"    protocol    = \"tcp\"",
				"    cidr_blocks = [\"0.0.0.0/0\"]",
				"  }",
				"  egress {",
				"    from_port   = 0",
				"    to_port     = 0",
				"    protocol    = \"-1\"",
				"    cidr_blocks = [\"0.0.0.0/0\"]",
				"  }",
				"}",
				"",
				"resource \"aws_iam_role\" \"ec2_role\" {",
				"  name = \"ec2_role\"",
				"  assume_role_policy = <<EOF",
				"{",
				"  \"Version\": \"2012-10-17\",",
				"  \"Statement\": [",
				"    {",
				"      \"Effect\": \"Allow\",",
				"      \"Principal\": { \"Service\": \"ec2.amazonaws.com\"},",
				"      \"Action\": \"sts:AssumeRole\"",
				"    }",
				"  ]",
				"}",
				"EOF",
				"}",
				"",
				"resource \"tls_private_key\" \"ec2_key\" {",
				"  algorithm = \"RSA\"",
				"  rsa_bits  = 4096",
				"}",
				"",
				"resource \"aws_key_pair\" \"generated_key\" {",
				"  key_name   = \"deploy_key\"",
				"  public_key = tls_private_key.ec2_key.public_key_openssh",
				"}",
				"",
				"resource \"aws_iam_instance_profile\" \"ec2_profile\" {",
				"  name = \"ec2_profile\"",
				"  role = aws_iam_role.ec2_role.name",
				"}",
				"",
				"resource \"aws_instance\" \"task_ec2_instance\" {",
				''.join(["  ami		   = \"", params['ami'], "\""]),
				''.join(["  instance_type = \"", params['instance_type'], "\""]),
				''.join(["  user_data	 = file(\"", params['task_script_path'], "\")"]),
				"  tags = {",
				''.join(["    Name  = \"", params['tagname'], "\""]),
				"  }",
				"  vpc_security_group_ids = [aws_security_group.ec2_sg.id]",
				"  key_name               = aws_key_pair.generated_key.key_name",
				"  iam_instance_profile   = \"ec2_profile\"",
				"}",
				"",
			]
		},
		'output': {
			'ec2': [
				"output \"output_public_ip\" {",
				"  value = aws_instance.task_ec2_instance.public_ip",
				"}",
				"",
				"output \"output_instance_id\" {",
				"  value = aws_instance.task_ec2_instance.id",
				"}",
				"",
				"output \"output_private_key\" {",
				"  value = tls_private_key.ec2_key.private_key_pem",
				"}"
			]
		}
	}
	'''

	'''
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
		'create': ['terraform init', 'terraform validate', 'terraform plan', 'terraform apply'], 
		'view': ['terraform show'], 
		'destroy': ['terraform destroy']
	}
	t = Terraform()
	for command in tf_commands['create']: # validate, init, apply
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

def remove_generated_config(params):
	for file_to_mkdir in ['credential_path', 'keypath', 'pub_key_path']:
		if 'key' not in file_to_mkdir:
			folder_created = mkdir_structure(params[file_to_mkdir], params)
			if folder_created:
				params[file_to_mkdir] = ''.join([folder_created, '', params[file_to_mkdir].split('/')[-1]])
		params[file_to_mkdir] = '/'.join([params['user_dir'], params[file_to_mkdir]]) if params['user_dir'] not in params[file_to_mkdir] else params[file_to_mkdir]
		if os.path.exists(params[file_to_mkdir]):
			os.remove(params[file_to_mkdir]) # remove original file if you need to re-create on each run
	for file_to_remove in ['tf_config_path', 'plan_path']:
		if os.path.exists(params[file_to_remove]):
			os.remove(params[file_to_remove]) # remove original file if you need to re-create on each run
	return params

''' to do: create install scripts install_boot_elk.sh and install_boot_model.sh '''
def deploy(params):
	#generated = generate_key(params['keypath'])
	#if generated:
		#print('generated key', generated)
	local_install = install_local_tf_cloud(params)
	if local_install:
		print('installed aws config, env var, pip reqs')
		configured = generate_config(params)
		if configured:
			print('generated config at config_path', params['tf_config_path'])
			output_keys = deploy_generated_tf_config(params)
			print('deployed resources with output', output_keys)
			if output_keys:
				for ok, val in output_keys.items():
					params[ok] = val
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

def destroy_resources(params):
	''' to do: delete tls_private_key '''
	instance_ids = []
	if os.path.exists('output.txt'):
		data = open('output.txt', 'r').readlines()
		print('output from previous execution', data)
		for line in data:
			key = line.split('=')[0]
			val = line.split('=')[1]
			''' cleaning before initializing resources '''
			if key == 'output_instance_id':
				instance_ids.append(val)

	ec2 = boto3.client('ec2')
	iam = boto3.client('iam')
	try:
		deleted_key_pair = ec2.delete_key_pair(KeyName='deploy_key') # 'deploy_key'	
	except Exception as e:
		print('key pair exception', e)
	try:
		if len(instance_ids) > 0:
			deleted_ec2_instance = ec2.terminate_instances(InstanceIds=instance_ids)
	except Exception as e:
		print('ec2 exception', e)
	try:
		deleted_sg = ec2.delete_security_group(GroupName='ec2_sg')
	except Exception as e:
		print('sg exception', e)
	try:
		removed_role = iam.remove_role_from_instance_profile(InstanceProfileName='ec2_profile', RoleName='ec2_role')
	except Exception as e:
		print('remove role from instance profile exception', e)
	try:
		deleted_instance_profile = iam.delete_instance_profile(InstanceProfileName='ec2_profile')
	except Exception as e:
		print('instance profile exception', e)
	try:
		deleted_role = iam.delete_role(RoleName='ec2_role')
	except Exception as e:
		print('role exception', e)
	return True

''' 
- task 'elk', requires ecs with python requirements.txt install
- task 'model' requires xgboost, hardware of a certain size, python requirements.txt 
'''

params = {'cloud': 'aws', 'task': 'elk', 'instance': 'demo'}
params['user_dir'] = '/'.join(os.getcwd().split('/')[0:3])
params['keypath'] = ''.join([params['user_dir'], '/tf_deploy.pem'])
params['pub_key_path'] = params['keypath'].replace('.pem', '.pub')
params['credential_path'] = '/.aws/credentials_tf/credentials.ini'
params['tf_config_path'] = ''.join([os.getcwd(), '/', params['cloud'], '_', params['task'], '_config.tf'])
params['plan_path'] = params['tf_config_path'].replace('_config.tf', '_plan_config.bin')
params = remove_generated_config(params)
params['secret_key'] = ''
params['access_key'] = ''
params['ami'] = 'ami-0baeabdd230a4e508' # centos 7
params['region'] = 'us-west-2'
params['user'] = 'ec2-user' if params['cloud'] == 'aws' else None
params['instance_type'] = 't2.micro' if params['task'] == 'elk' else 'm2.medium'
params['output_keys'] = ['output_public_ip', 'output_instance_id', 'output_private_key']
params['output_instance_id'] = 'i-04ad6517520e8d781'
params['tagname'] = ''.join(['task_ec2_instance', '_', params['task']])
params['task_script_path'] = ''.join([os.getcwd(), '/', 'install_boot_', params['task'], '.sh'])

stored_env = {}
for i, arg in enumerate(sys.argv):
	if (i + 1) < len(sys.argv):
		if 'secret' in arg:
			params['secret_key'] = sys.argv[i + 1]
		elif 'access' in arg:
			params['access_key'] = sys.argv[i + 1]
		''' to do: add support for other cli params
		for key in params:
			if key in arg:
				params[key] = sys.argv[i + 1]
		'''
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

	destroy_resources(params)

	clean_params = deploy(params)
	if clean_params:
		print('clean_params', clean_params)

	output_tracker = '\n'.join([''.join([key, '=', params[key]])for key in ['output_instance_id'] if key in params])
	if output_tracker:
		open('output.txt', 'w').write(output_tracker)

	''' cleanup task '''
	for env, val in params['env'].items():
		os.environ[env] = '' if env not in stored_env else stored_env[env] if stored_env[env] is not None else ''
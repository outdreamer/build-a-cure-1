import boto3
import botocore
import paramiko
import python_terraform
import os, sys, subprocess	

def install_tf_cloud(params):
	''' install terraform/aws cli on local '''
	env_var_commmands = [
		''.join(["export AWS_SHARED_CREDENTIALS_FILE=", credential_path]) 
		# ''.join(["export AWS_CONFIG_FILE=", config_path])
	]
	config_path = "~/.aws/config/config.ini"
	credential_path = "~/.aws/credentials/credentials.ini"
	credential_content = [
		''.join(["[default] aws_access_key_id=", params['access_key'], " aws_secret_access_key=", params['secret_key']]), 
		''.join(["[testing] aws_access_key_id=", params['access_key'], " aws_secret_access_key=", params['secret_key']])
	]
	'''
	config_content = [
		''.join(["[default] aws_access_key_id=", default_access_key,  " aws_secret_access_key=", default_secret_key]),
	   	''.join(["[profile testing] aws_access_key_id=", access_key, " aws_secret_access_key=", secret_key, " region=", region])
	]
	'''
	with open(credential_path, 'w') as f:
		f.write('\n'.join(credential_content))
		f.close()
	for command in env_var_commmands:
		result = subprocess.run([sys.executable, "-c", command])
		print('install_tf_cloud env vars result', command, result)
	return False

def generate_config(params):
	''' 
	params = {
		'cloud': ['aws', 'gc'],
		'task': ['model', 'elk'],
		'instance': ['test', 'demo']
	}
	'''
	deployment_resources_lines = []
	ec2_resource_list = ['ec2', 'iam', 'ssh']
	tf_config = get_tf_config(params)

	if tf_config:

		if params['cloud'] == 'aws':

			config_path = os.getcwd()
			if params['task'] == 'elk':
				''' elk requires ecs with python requirements.txt install, iam '''
				config_path = ''.join([config_path, 'aws_elk_config.tf'])
			elif params['task'] == 'model':
				''' model requires xgboost, hardware of a certain size, python requirements.txt, iam '''
				config_path = ''.join([config_path, 'aws_model_config.tf'])
			else:
				print('unsupported task', params)
			''' need an ec2 regardless so add that instance, as well as its requirements (launch config, iam, ssh) '''

			for category in ['vars', 'resources', 'output']:
				for item in ec2_resource_list
					if item in tf_config[category]:
						deployment_resources_lines.append(tf_config[category][item])

			''' to add remote_exec rather than user data, add tf_command_lines to tf config output
			userdata_content = open(task_script_path, 'r').readlines()
			tf_commands = ["  provisioner \"remote-exec\" {", "    inline = ["]
			for command in userdata_content:
				tf_command_line = ''.join(["      \"", command, "\","]),
				tf_commands.append(tf_command_line)
			tf_command_line.append("    ]")
			tf_command_line.append("  }")
			'''

			if config_path and len(deployment_resources_lines) > 0:
				''' write generated config '''
				with open(config_path, 'w') as f:
					f.write('\n'.join(deployment_resources_lines))
					f.close()

	return config_path

def deploy_generated_tf_config(config_path, output_key):
	''' terraform show will have a line with the public ip attribute 
	'public_ip                    = "54.166.19.244"' 
	'''
	t = Terraform()
	for command in tf_commands['create']: # validate, init, apply
		print('running tf command', command)
		return_code, stdout, stderr = t.cmd(command) #, *arguments, **options)
		if return_code == 200:
			print('tf command', command, 'output', type(stdout), stdout, stderr)
			for line in stdout.readlines():
				print('stdout line', line)
				if command == 'apply':
					if output_key in line:
						print('\n\n****found line', line)
						return line.replace(output_key, '').strip()
	return False

def generate_key(keypath):
	''' ssh-keygen -t rsa, keypath, 'N' for passphrase skip, Enter '''
	keygen = None
	try:
		keygen = paramiko.RSAKey.generate(1024)
	except Exception as e:
		print('generate key error', e)
	if keygen:
	    keygen.write_private_key_file(keypath, password='')
	    pub_key_path = keypath.replace('.pem', '.pub')
	    o = open(pub_key_path ,"w").write(k.get_base64())
	    return keypath
    return False

def open_output_in_browser(ip, params):
	''' open notebook/api graph or elk kibana login '''
	url = ''.join(['http://', ip, '/kibana']) if params['task'] == 'elk' else ''.join(['http://', ip, '/api/predict-test'])
	response = requests.get(url) #, params = {}, args = {})
	if response:
		print('response', url, response)
		if response.status_code == 200:
			webbrowser.open(url, new=0, autoraise=True) # webbrowser.get('firefox').open_new_tab(url)
	return False

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
	''' execute install command on instance '''
	try:
		stdin, stdout, stderr = client.exec_command(command)
		if stdout:
		    print('executed command', command, stdout.read(), stderr)
	    	return stdout, stderr
	except Exception as e:
		print('execute_command exception', e)
	return False, False

''' to do: create install scriptss install_boot_elk.sh and install_boot_model.sh '''
def deploy(params):
	generated = generate_key(params['keypath'])
	local_install = install_tf_cloud(params)
	if local_install:
		config_path = generate_config(params)
		output_key = deploy_generated_tf_config(config_path, params['output_key'])
		if output_key:
			''' to do: find ip & ssh key for instance from tf output'''
			'''
			connection = connect_to_instance(ip, params['keypath'], params['user'])
			if connection:
				executing commands should be done in userdata
				install_boot_command = ''.join(['cd ', '/home/', params['user'], ' && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build-a-cure/ && ./install_boot_', params['task'], '.sh', 
				executed, err = execute_remote_command(install_boot_command, connection)
				# if booted, test & execute display task (open notebook/api graph of model visuals or elk stack login in browser)
			else:
				print('could not connect', stdout, stderr, ip, params['keypath'], params['user'])
			'''
			open_output_in_browser(output_key, params)
		else:
			print('could not deploy', return_code, stdout, stderr)
	return False

tf_commands = {'check': 'terraform -help', 'create': ['terraform validate', 'terraform init', 'terraform apply'], 'view': ['terraform show'], 'destroy': ['terraform destroy']}

params = {'cloud': 'aws', 'task': 'elk', 'instance': 'demo'}
params['secret_key'] = ''
params['access_key'] = ''
params['keypath'] = "~/tf_deploy.pem"
params['region'] = 'us-west-2'
params['user'] = 'ec2-user' if params['cloud'] == 'aws' else None
params['instance_type'] = 't2.micro' if params['task'] == 'elk' else 'm2.medium'
params['pub_key_path'] = params['keypath'].replace('.pem', '.pub')
params['output_key'] = 'output_public_ip'
params['tagname'] = ''.join(['task_ec2_instance', params['task']])
params['task_script_path'] = ''.join(['install_boot_', params['task'], '.sh'])

''' to do: check pub key generation '''

def get_tf_config(params):
	tf_config = {
		'vars': {
			'ssh': [
				"variable \"keypath\" {",
				"  description = \"Path to SSH private key to SSH-connect to instances\"",
				"  default = \"", params['keypath'], "\"",
				"}"
			]
		},
		'resources': {
			'ssh': [
				"connection {",
				"    type     = \"ssh\"",
				''.join(["    user     = \"", params['user'], "\""]),
				"    private_key = \"${file(var.keypath)}\"",
				"    host     = aws_instance.task_ec2_instance.public_ip",
				"}",
				"resource \"aws_key_pair\" \"task_key_pair\" {",
				"  key_name   = \"terraform-demo\"",
				''.join(["  public_key = \"${file(", params['pub_key_path'], ")}\""]),
				"}"
			],
			'ec2': [
				"resource \"aws_instance\" \"task_ec2_instance\" {\"",
				''.join(["  ami           = \"", params['ami'], "\""]),
				''.join(["  region           = \"", params['region'], "\""]),
				''.join(["  instance_type = \"", params['instance_type'], "\""]),
				"  key_name      = \"${aws_key_pair.task_key_pair.key_name}\"",
				''.join(["  user_data     = \"${file(", params['task_script_path'], ")}\""]),
				"  tags = {",
				''.join(["    Name  = \"", params['tagname'], "\""]),
				"  }",
				"}"
			]
		},
		'remote_exec': [],
		'output': {
			'ec2': [
				"output \"output_public_ip\" {",
				"  value = \"${aws_instance.task_ec2_instance.public_ip}\"",
				"}"
			]
		}
	}
	return tf_config

deploy(params)
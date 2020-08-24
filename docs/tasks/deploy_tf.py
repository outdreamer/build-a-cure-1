import boto3
import botocore
import paramiko
	
def install_tf_cloud():
	''' install terraform/aws cli on local '''
	with open(credential_path, 'w') as f:
		f.write('\n'.join(credentials))
		f.close()
	env_var_commmands = [
		''.join(["export AWS_SHARED_CREDENTIALS_FILE=", credential_path]), 
		''.join(["export AWS_CONFIG_FILE=", config_path])
	]
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
		for item in ec2_resource_list
			if item in tf_config['vars']:
				deployment_resources_lines.append(tf_config['vars'][item])
		for item in ec2_resource_list:
			deployment_resources_lines.append(tf_config[item])
		if config_path and len(deployment_resources_lines) > 0:
			''' write generated config '''
			with open(config_path, 'w') as f:
				f.write('\n'.join(deployment_resources_lines))
				f.close()
	return config_path

''' to do: create install scriptss install_and_boot_elk.sh and install_and_boot_model.sh '''
def deploy(params):
	local_install = install_tf_cloud()
	if local_install:
		config_path = generate_config(params)
		return_code, stdout, stderr = deploy_generated_tf_config(config_path)
		if return_code == 200:
			''' to do: find ip & ssh key for instance from tf output'''
			ip, keypath = find_instance_info_in_output(stdout, params)
			connection = connect_to_instance(ip, keypath, user)
			if connection:
				install_and_boot_command = ''.join(['cd ', user_dir, ' && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build-a-cure/ && ./install_and_boot_', params['task'], '.sh', 
				executed, err = execute_command(install_and_boot_command, connection)
				if executed:
					''' if its booted, test & execute display task (open notebook/api graph of model visuals or elk stack login in browser) '''
					open_output_in_browser(ip, params)
			else:
				print('could not connect', stdout, stderr, ip, keypath, user)
		else:
			print('could not deploy', return_code, stdout, stderr)

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

def execute_command(command, connection):
	''' execute install command on instance '''
	try:
		stdin, stdout, stderr = client.exec_command(command)
		if stdout:
		    print('executed command', command, stdout.read(), stderr)
	    	return stdout, stderr
	except Exception as e:
		print('execute_command exception', e)
	return False, False

def find_instance_info_in_output(stdout, params):
	ip = ''

	return False, False

def deploy_generated_tf_config(config_path):
	from python_terraform import *
	t = Terraform()
	return_code, stdout, stderr = t.cmd(<cmd_name>, *arguments, **options)

def connect_to_instance(ip, keypath, user):
	key = paramiko.RSAKey.from_private_key_file(keypath)
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
	    connection = client.connect(hostname=ip, username=user, pkey=key)
	    if connection:
	    	return connection
	except Exception as e:
	    print('connect exception', e)
	return False

params = {'cloud': 'aws', 'task': 'elk', 'instance': 'demo'}
keypath = "~\\tf_deploy.pem"
region = 'us-west-2'
access_key = ''
default_access_key = ''
secret_key = ''
default_secret_key = ''
user = 'ec2-user' if params['cloud'] == 'aws' else None
user_dir = ''.join([['/home/', user])
install_local_commands = ['brew install terraform']
tf_commands = {'check': 'terraform -help', 'create': ['terraform init', 'terraform apply'], 'destroy': ['terraform destroy']}
aws_commands = {}
credential_content = [
	''.join(["[default] aws_access_key_id=", access_key, " aws_secret_access_key=", secret_key]), 
	''.join(["[testing] aws_access_key_id=", access_key, " aws_secret_access_key=", secret_key])
]
config_content = [
	''.join(["[default] aws_access_key_id=", default_access_key,  " aws_secret_access_key=", default_secret_key]),
   	''.join(["[profile testing] aws_access_key_id=", access_key, " aws_secret_access_key=", secret_key, " region=", region])
]
config_path = "~/.aws/config/config.ini"
credential_path = "~/.aws/credentials/credentials.ini"
tf_config = {
	'vars': {
		'ec2': [
			"variable \"cluster_member_count\" {",
  			"	description = \"Number of instances in the cluster\"",
  			"	default = \"3\"",
			"}"
		],
		'ssh': [
			"variable \"keypath\" {",
			"  description = \"Path to SSH private key to SSH-connect to instances\"",
			"  default = \"", keypath, "\"",
			"}"
		]
	},
	'ssh': [
		"connection {",
		"    type     = \"ssh\"",
		''.join(["    user     = \"", user, "\""]),
		"    private_key = \"${file(var.keypath)}\"",
		"    host     = aws_instance.web.public_ip",
		"}"
	],
	'ec2': [
		"resource \"aws_instance\" \"task_ec2_instance\" {\"",
		"  count = \"${var.instance_count}\"",
		"}"
	],
	'ecs': [

	],
	'iam': [

	],
	'output': [
		'ip': 'aws_instance.task_ec2_instance.*.public_ip'
	]
}

deploy(params)
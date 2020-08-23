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
	config_path = os.getcwd()
	if params['cloud'] == 'aws':
		if params['task'] == 'elk':
			''' elk requires ecs with python requirements.txt install, iam '''
			config_path = ''.join([config_path, 'aws_elk_config.tf'])
		elif params['task'] == 'model':
			''' model requires xgboost, hardware of a certain size, python requirements.txt, iam '''
			config_path = ''.join([config_path, 'aws_model_config.tf'])
		else:
			print('unsupported task', params)
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
				executed = execute_command(install_and_boot_command, connection)
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
	return False

def execute_command(install_and_boot_command, connection):
	''' execute install command on instance '''
	return False

def find_instance_info_in_output(stdout, params):
	ip = ''
	keypath = '~/'
	return False, False

def deploy_generated_tf_config(config_path):
	from python_terraform import *
	t = Terraform()
	return_code, stdout, stderr = t.cmd(<cmd_name>, *arguments, **options)

def connect_to_instance(instance_ip, keypath, user):
	ssh_command = ''.join(["ssh -i ", keypath, " ", user, "@", ip])


params = {'cloud': 'aws', 'task': 'elk', 'instance': 'demo'}

gen_key_path = "~\\tf_deploy.pem"
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
	'ssh_connection': [
		"connection {",
		"    type     = \"ssh\"",
		''.join(["    user     = \"", user_name, "\""]),
		"    private_key = file(gen_key_path)",
		"    host     = aws_instance.web.public_ip",
		"}"
	]
}

deploy(params)
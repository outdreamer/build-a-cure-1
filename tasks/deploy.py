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

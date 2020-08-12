'''
which strategies will the models use?

	- initially:
		- templates
		- unsupervised learning (k means, nearest neighbors)
		- anomaly detection algorithms
		
	 - later:
	 	- intent/cause/meaning model, optionally with assumption/implication/conclusions integrated
	 		- do functions with these intents enable an overall malicious intent when executed in a sequence?
	 		- every resource access, including function calls, is a possible target of a malicious agent
	 		- apply filters on resources (valuable resources, enabling resources, access-granting resources, etc)
	 	- distortion/base model
	 		- given a particular base, what distortion functions apply?
	 	- change model
	 		- is this function or data point in a state of flux or does it clearly fall into a known category?
'''

def create_instance():
	return False

def check_instance_availability():
	return False

def connect_to_instance():
	return False

def upload_data_to_instance():
	return False

def sanitize_data():
	''' use import functionality of elk or apply json data schema templates '''
	return False

def import_to_elk():
	return False

def upload_script():
	return False

def install_python_script_dependencies():
	return False

def install_elk_dependencies():
	return False

def install_model_dependencies():
	return False

def train_model():
	return False


'''
script to spin up aws instance & upload data, install dependencies & train.py, & run train.py to aws

'''


'''
script to spin up aws instance & install elk stack, upload data, run sanitize.py & import.py

'''
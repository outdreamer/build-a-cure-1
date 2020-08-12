import os, csv, json, uuid
import boto3
import pandas as pd
import numpy as np

from import_elk import import_to_elk
from sanitize import sanitize_data

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

''' DEPLOY '''

def create_instance():
	return False

def check_instance_availability():
	return False

def connect_to_instance():
	return False

''' VIZ '''

def visualize_data():
	''' add options like network graph, word stats, clusters '''
	return False

''' UPLOAD '''

def upload_data_to_instance():
	return False

def upload_script():
	return False

''' PIP '''

def install_python_script_dependencies():
	return False

''' ELK '''

def install_elk_dependencies():
	return False

''' MODEL '''

def install_model_dependencies():
	return False

def train_model():
	return False

''' API '''
def api_get_prediction():
	return False

def api_test():
	return False

def start_api_server():
	return False

data = sanitize_data()
if data:
	print('len data', len(data))
	import_to_elk('fgt_event', data)

'''
script to spin up aws instance & upload data, run sanitize.py, install.py for model dependencies & train.py, and api.py to start api server for model

'''

'''
script to spin up aws instance, upload data, run sanitize.py install.py for elk stack & import.py

'''
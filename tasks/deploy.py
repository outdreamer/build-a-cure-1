import os, csv, json, uuid
import boto3
import pandas as pd
import numpy as np

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
	cwd = os.getcwd()
	origin_path = ''.join([cwd, '/data/event/'])
	for cur, _dirs, files in os.walk(origin_path):
		for filename in files:
			filename = ''.join([cur, '/', filename])
			if '.json' in filename:
				print('filename', filename)
				csv_path = filename.replace('.json', '.csv')
				with open(csv_path, 'w') as csv_file:
					with open(filename, 'r') as f:
						''' assemble & write header '''
						all_columns = ['uuid']
						cols_not_found = set()
						lines = []
						for line in f:
							data = json.loads(line)
							if data:
								if 'result' in data:
									for a in data['result'].keys():
										if a not in all_columns:
											all_columns.append(a)
									lines.append(data['result'])
						if len(all_columns) > 0:
							csv_file.write(','.join(all_columns))
							csv_file.write('\n')

						''' assign values '''
						for line in lines:
							value_list = [str(uuid.uuid4())]
							for c in all_columns:
								if c in line:
									v = line[c]
									value = '::'.join(v) if type(v) == list or type(v) == tuple or type(v) == set else '::'.join(['_'.join([k, c]) for k, c in v.items()]) if type(v) == dict else v
									value_list.append(value.strip().replace(',','__'))
								else:
									cols_not_found.add(c)
									value_list.append('0')
							if len(value_list) > 0:
								csv_file.write(','.join(value_list))
								csv_file.write('\n')

						print('cols not found', cols_not_found)

						f.close()
					csv_file.close()

				df = data_processing(csv_path)
	return False

def data_processing(csv_path):
	df = pd.read_csv(csv_path)
	print('df head', df.head()) #head(10)
	df.set_index('uuid')
	print('dtype value counts', df.dtypes.value_counts())
	df = df.applymap(sanitize_all_values)
	for column in df:
		#print('column', df[column]) #, 'type', df[column].dtype)
		#null_ratio = get_null_ratio(df, column)
		isolated_subset_column = execute_operation_on_column(df[column], 'subset', r'^(\d{4})', None)
		numeric_column = execute_operation_on_column(df[column], 'numeric', None, None)
	print('df head', df.head())
	return df

def sanitize_all_values(value):
	value = value.strip() if type(value) == str else value
	return value

def execute_operation_on_column(column, operation, regex, replacement):
	data_type = column.dtype.name
	#print('column dtype', column.dtype.name, operation)
	new_column = None
	if operation == 'numeric':
		if data_type == 'int64':
			new_column = pd.to_numeric(column)
	elif operation == 'capitalize':
		if data_type == 'object':
			new_column = pd.capitalize(column)
	elif operation == 'replace':
		if regex is not None and replacement is not None:
			new_column = np.where(regex, replacement, column)
	elif operation == 'subset':
		if regex is not None and data_type == 'object':
			new_column = column.str.extract(regex, expand=False)
	else:
		pass
	if new_column is not None:
		return new_column
	return False

def get_null_ratio(df_data, df_column):
	if df_column in df_data:
		return df_data[df_column].isnull().sum() / len(df_data)
	return False

sanitize_data()

def visualize_data():
	''' add options like network graph, word stats, clusters '''
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
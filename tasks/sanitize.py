import os, csv, json, uuid
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, StandardScaler

def convert_data(data, label_column_name, remove_types):
	''' 
		- sanitize data
		- encode categorical data
		- to do: remove columns of type in remove_types, like date or text columns
		- to do: vectorize text data
		- to do: apply scaler 
		- map trajectories of text data
	'''

	#check number of rows and columns in dataset
	print('shape (rows, columns)', data.shape)
	print('data.describe()', data.describe())

	categorical = data.iloc[:,:].select_dtypes('object').columns
	print('categorical', categorical)
	print('groups count', sum(data[categorical].nunique()))
	print('dtype value counts', data.dtypes.value_counts())
	numeric_data = data._get_numeric_data().astype('float64')
	print('numerical', numeric_data)
	# data.set_index('uuid')
	#data = data[col != low_count_col_value]
	text_columns = {}
	text_column_threshold = 100

	for col in data.keys():
		sample_value = data[col].values[0]
		unique_values = data[col].unique()
		print('column', col, 'sample value', sample_value)
		''' exclude columns with low-count values'''
		if len(unique_values) > 1:
			if data[col].dtype.name == 'object':
				datetime_object_type = None
				if len(sample_value) < text_column_threshold:
					chars_to_remove = '' # add any extra chars to remove
					# data[col] = ''.join([char for char in data[col] if char not in chars_to_remove]) 
					numeric_chars = ''.join([char for char in data[col] if char in '0123456789,.'])
					if len(numeric_chars) == len(data[col]):
						data[col] = data[col].replace(',','').astype('float64')	
						#scaler = StandardScaler()
						#data[col] = scaler.fit_transform(np.array(data[col]).reshape(-1, 1))
					elif 'time' in col or 'date' in col or ':' in sample_value or '-' in sample_value or '/' in sample_value:
						''' 
						convert date values into datetime objects
						to do: handle lowercase values 'sunday' 
						'''
						day_month_name_formats = ["%A", "%B"]
						numerical_date_formats = ["%Y", "%Y-%m-%d", "%y-%m-%d", "%m-%d-%y", "%m-%d-%Y", "%m-%d-%Y %H:%M:%S", "%m-%d-%Y %H:%M:%S.%Z", "%H:%M:%S"]
						for format_list in [day_month_name_formats, numerical_date_formats]:
							for format in format_list:
								datetime_object = None
								try:
									datetime_object = pd.to_datetime(data[col], format=format)
								except Exception as error:
									print('could not convert to date with format', format, data[col][0])
								if datetime_object is not None:
									data[col] = datetime_object
									datetime_object_type = format_list
						if datetime_object_type is None:
							number_col = None
							''' order by exclusive/common type if there is one '''
							for number_type in ['int64', 'float64']:
								try:
									number_col = data[col].astype(number_type)
								except Exception as error:
									print('could not convert to', number_type, number_col)
								if number_col and datetime_object_type is None:
									number_col_sample = number_col.values()[0]
									if number_col_sample >= 0 and number_col_sample < 60:
										''' to do: handle possible minute, second, hour, month, day column '''
										datetime_object_type = 'possible_numerical_date'
										data[col] = number_col
										#scaler = StandardScaler()
										#data[col] = scaler.fit_transform(np.array(data[col]).reshape(-1, 1))
										print('scaler col', col, data[col])
				print('datetime_object_type', col, datetime_object_type)
				if datetime_object_type is None:
					''' encode label/categorical data '''
					if col == label_column_name:
						encoder = LabelEncoder()
						data[col] = encoder.fit_transform(data[col].values)
						print('encoded labels', data[col])
						print('classes', col, encoder.classes_)
					else:
						enc = OneHotEncoder() # drop='first') # ignore='unknown'
						''' data[col] = np.array(data[col]).reshape(-1, 1) '''
						values_array = data[col].values.reshape(-1, 1)
						data[col] = enc.fit_transform(values_array)
						print('one hot categories', enc.categories_)
						'''
							index: (0, 2)	1.0 <class 'scipy.sparse.csr.csr_matrix'>
							encoded_values_array.toarray(): [[0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
						'''
						print('one hot encoded col values', col, data[col]) #print('feature names', enc.get_feature_names(data))
				else:
					text_columns[col] = sample_value
			elif data[col].dtype.name == 'int64':
				data[col] = data[col].astype('float64')
				#scaler = StandardScaler()
				#data[col] = scaler.fit_transform(data[col].values.reshape(-1, 1))
			else:
				print('unhandled type', col.dtype, col)			
	print('found text cols', text_columns)
	print('transformed data', data.head())
	return data
	
def json_to_csv():
	''' use import functionality of elk or apply json data schema templates '''
	all_new_dicts = []
	cwd = os.getcwd()
	print('cwd', cwd)
	origin_path = ''.join([cwd, '/tasks/data/event/'])
	for cur, _dirs, files in os.walk(origin_path):
		for original_filename in files:
			filename = ''.join([cur, '/', original_filename])
			if '.json' in filename and 'new_' not in filename:
				csv_path = filename.replace('.json', '.csv')
				new_json = ''.join([cur, '/new_', original_filename])
				with open(csv_path, 'w') as csv_file:
					with open(filename, 'r') as f:
						print('loading json', filename)
						''' assemble & write header '''
						all_columns = [] # 'uuid'
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
						print('got json data', lines[0])
						if len(all_columns) > 0:
							csv_file.write(','.join(all_columns))
							csv_file.write('\n')
						''' assign values '''
						for line in lines:
							value_list = [] # [str(uuid.uuid4())]
							new_dict = {}
							for c in all_columns:
								if c in line:
									v = line[c]
									value = '::'.join(v) if type(v) == list or type(v) == tuple or type(v) == set else '::'.join(['_'.join([k, c]) for k, c in v.items()]) if type(v) == dict else v
									value = value.strip().replace(',',';')
									new_dict[c] = value
									value_list.append(value)
								else:
									cols_not_found.add(c)
									new_dict[c] = '0'
									value_list.append('0')
							if len(value_list) > 0:
								csv_file.write(','.join(value_list))
								csv_file.write('\n')
								all_new_dicts.append(new_dict)
						print('cols not found', cols_not_found)
						f.close()
						with open(new_json, 'w') as nf:
							all_vals = []
							for new_dict in all_new_dicts:
								new_val = ','.join(['_'.join([k, v]) for k, v in new_dict.items()])
								all_vals.append(new_val)
							formatted_json = json.dumps(all_vals)
							print('formatted_json', type(formatted_json), formatted_json)
							nf.write(formatted_json)
							nf.close()
					csv_file.close()
				df = pd.read_csv(csv_path)
				if df:
					df = data_processing(df)
	if len(all_new_dicts) > 0:
		return all_new_dicts
	return False

def data_processing(data):
	print('data processing: head', data.head()) #head(10)
	data = data.applymap(sanitize_all_values)
	for column in data:
		isolated_subset_column = execute_operation_on_column(data[column], 'subset', r'^(\d{4})', None)
		numeric_column = execute_operation_on_column(data[column], 'numeric', None, None)
	print('data head', data.head())
	return data

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

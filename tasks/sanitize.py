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

		- to do: standardize params None/len checks
		
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
	low_value_threshold = 1
	remove_types = ['one_hot_encoding', 'datetime', 'numeric', 'categorical', 'low_value', 'text'] if remove_types is None else remove_types
	removed_cols = {r: {} for r in remove_types}

	for col in data.keys():
		avg_length = sum([len(str(val)) for val in data[col].values]) / len(data[col].values)
		sample_value = data[col].values[0]
		unique_values = data[col].unique()
		print('column', col, 'sample value', sample_value, 'avg_length', avg_length, 'uniq', unique_values)
		''' exclude columns with low-count values'''
		if len(unique_values) > low_value_threshold:
			if data[col].dtype.name == 'object':
				datetime_object_type = None
				if avg_length < text_column_threshold:
					chars_to_remove = '' # add any extra chars to remove
					# data[col] = ''.join([char for char in data[col] if char not in chars_to_remove]) 
					numeric_chars = ''.join([char for char in data[col] if char in '0123456789,.'])
					if len(numeric_chars) == len(data[col]):
						print('numeric', col)
						data[col] = data[col].replace(',','').astype('float64')	
						#scaler = StandardScaler()
						#data[col] = scaler.fit_transform(np.array(data[col]).reshape(-1, 1))
					elif 'time' in col or 'date' in col or ':' in sample_value or '-' in sample_value or '/' in sample_value:
						''' 
						convert date values into datetime objects
						to do: handle lowercase values 'sunday' 
						'''
						if col == 'date_month':
							print('date col', col, sample_value)
							day_month_name_formats = ["%A", "%B"]
							numerical_date_formats = ["%Y", "%Y-%m-%d", "%y-%m-%d", "%m-%d-%y", "%m-%d-%Y", "%m-%d-%Y %H:%M:%S", "%m-%d-%Y %H:%M:%S.%Z", "%H:%M:%S"]
							for format_list in [day_month_name_formats, numerical_date_formats]:
								for format in format_list:
									print('format', format)
									if datetime_object_type is None:
										data[col] = data[col].str.upper() if format in day_month_name_formats else data[col]
										try:
											data[col] = pd.to_datetime(data[col], format=format)
											print('found datetime object with format', format, data[col])
											datetime_object_type = format_list
										except Exception as error:
											print('could not convert to date with format', format, data[col][0])										
							if datetime_object_type is None:
								''' no date/time found in col, check if numeric '''
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
							if datetime_object_type is not None and 'datetime' in remove_types:
								removed_cols['datetime'][col] = data[col]
								del data[col]
							exit()
					label_encoder = LabelEncoder()
					if datetime_object_type is None:
						''' encode label/categorical data '''
						if col == label_column_name:
							data[col] = label_encoder.fit_transform(data[col].values)
							print('encoded labels', data[col])
							print('classes', col, label_encoder.classes_)
						else:
							print('original col', data[col].values)
							enc = OneHotEncoder() # drop='first') # ignore='unknown'
							''' data[col] = np.array(data[col]).reshape(-1, 1) '''
							data_col_encoded = label_encoder.fit_transform(data[col].values)
							data_col_encoded = 	np.array(data_col_encoded).reshape(-1, 1)
							onehotlabels = enc.fit_transform(data_col_encoded).toarray()
							''' this extra encoder is just for tracking original column values & their encoded values '''
							new_enc = OneHotEncoder()
							values_array = data[col].values.reshape(-1, 1)
							new_cols = new_enc.fit_transform(values_array).toarray()
							value_map = {}
							for i, item in enumerate(enc.categories_[0]):
								value_map[item] = new_enc.categories_[0][i] if i < len(new_enc.categories_[0]) else None
							print('value_map', value_map)
							''' add new cols to dataframe '''
							cols = {}
							cols_with_cat = {}
							for row in onehotlabels:
								for index, val in enumerate(row):
									value_index = value_map[index] if index in value_map else None
									if value_index:
										col_name = '_'.join([col, value_index])
										if col_name not in cols:
											cols[col_name] = []
										if col_name not in cols_with_cat:
											cols_with_cat[col_name] = []
										cols[col_name].append(val)
										if val == 0:
											cols_with_cat[col_name].append(0)
										else:
											cols_with_cat[col_name].append(value_index)
							print('cols', cols)
							print('cols_with_cat', cols_with_cat)
							''' to do: check for existing column conflicts with new name '''
							for col_name, values in cols.items():
								data[col_name] = values
							''' 
							cols is the set of new columns, one for each possible value of data[col] 
							cols_with_cat is the set of new columns, with original values instead of encoded value, for validation
							'''

							'''
							data_col_encoded = [1 3 0 0 3 0 2 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0]
							col: interface
							value_map {0: '0', 1: 'internal1', 2: 'internal3', 3: 'internal5'}
							onehotlabels.shape (50, 4)
							enc.categories_ [array([0, 1, 2, 3])]
							new_cols.shape (50, 4)
							new_enc.categories_ [array(['0', 'internal1', 'internal3', 'internal5'], dtype=object)]
							onehotlabels == new_cols == [[0. 1. 0. 0.], [0. 0. 0. 1.] ...]
							'''
							''' new_rows_with_labels is the one-hot encoded version with labels instead of codes, just for validation '''
							if onehotlabels.all() == new_cols.all():
								new_rows_with_labels = []
								for row in new_cols:
									new_row = []
									for i, val in enumerate(row):
										if val != 0:
											label = value_map[i]
											new_row.append(label)
										else:
											new_row.append(val)
									new_rows_with_labels.append(new_row)
								print('new rows', new_rows_with_labels)
							else:
								print('error: diff in encoding output', new_cols, onehotlabels)
							''' to do: remove cols encoded as multiple columns with one-hot '''
							if col in data.keys():
								removed_cols['one_hot_encoding'][col] = data[col]
								del data[col]
							print('remaining cols', data.keys())
							'''
								index: (0, 2)	1.0 <class 'scipy.sparse.csr.csr_matrix'>
								encoded_values_array.toarray(): [[0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
							'''
							print('one hot encoded col values', col) #print('feature names', enc.get_feature_names(data))
							print('new cols in data', data.keys())
				else:
					text_columns[col] = sample_value
					removed_cols['text'][col] = data[col]
					del data[col]
			elif data[col].dtype.name == 'int64':
				data[col] = data[col].astype('float64')
				#scaler = StandardScaler()
				#data[col] = scaler.fit_transform(data[col].values.reshape(-1, 1))
			else:
				print('unhandled type', col.dtype, col)	
		else:
			removed_cols['low_value'][col] = data[col]
			del data[col]

	print('found text cols', text_columns)
	print('transformed data', data.head())
	for col in data:
		print('col', col, type(data[col]), data[col].values)
	return data, removed_cols
	
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

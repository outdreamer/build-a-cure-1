import os, csv, json, uuid
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, StandardScaler

def convert_data_to_numeric(data, label_column_name):
	''' 
		- sanitize data
		- encode categorical data
		- vectorize text data
		- map trajectories of text data
	'''

	categorical = data.iloc[:,:].select_dtypes('object').columns
	print('categorical', categorical)
	'''
	for i in categorical:
		print('categorical group count', data[i].unique())
	'''
	print('groups count', sum(data[categorical].nunique()))
	print('data.describe()', data.describe())
	print('dtype value counts', data.dtypes.value_counts())

	''' to do: skip dates '''
	numeric_data = data._get_numeric_data().astype('float64')
	print('numerical', numeric_data)
	return numeric_data
	
	''' to do: exclude low-count values if necessary '''
	#data = data[col != low_count_col_value]
	
	categorical_names = {}
	scaler = StandardScaler()
	for col in data.columns:
		''' to do: encode label/categorical data '''
		if col.dtype.name == 'object':
			if col == label_column_name:
				encoder = LabelEncoder()
				data[col] = encoder.fit_transform(data[col])
				categorical_names[col] = encoder.classes_
			else:
				enc = OneHotEncoder(drop='first') # ignore='unknown'
				enc.fit(x_features)
				print('one hot categories', enc.categories_)
				data[col] = enc.transform(data[col]).toarray()
				# enc.get_feature_names(cols)
		''' to do: scalar takes in np.array format '''
		data[col] = np.array(data[col]).reshape(-1, 1)
		data[col] = scaler.fit_transform(data[col])
	print('categorical_names', categorical_names)
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
				df = data_processing(csv_path)
	if len(all_new_dicts) > 0:
		return all_new_dicts
	return False

def data_processing(csv_path):
	df = pd.read_csv(csv_path)
	print('df head', df.head()) #head(10)
	# df.set_index('uuid')
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

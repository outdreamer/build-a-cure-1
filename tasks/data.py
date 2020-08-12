def convert_data_to_numeric(data):
	''' 
		- sanitize data
		- encode categorical data
		- vectorize text data
		- map trajectories of text data
	'''
	return False

def reduce_features(data):
	''' apply pca & other feature reduction methods once data is filtered to numeric variables '''
	return False

def confusion_matrix(data):
	''' generate confusion matrix '''
	return False

def graph_data(client, connection, instance_name, graph_type):
	''' add options like network graph, word stats, clusters and create an image that can be retrieved by api '''
	image_url = ''
	api_url = ''.join(['https://', instance_ip, 'api_url'])
	if graph_type == 'network_graph':
		''' create network graph of data '''
		pass
	elif graph_type == 'prediction_function':
		''' graph prediction function with reduced vars '''
		pass
	else:
		print('unknown visual type', visual_type)
	return False

def split_data_by_algorithm(data):
	''' split into nlp/clustering/decision tree data variables & associated predicted independent variables '''
	return False

def apply_algorithm(data, algorithm):

	if algorithm == 'decision_forest':

	elif algorithm == 'xgboost':

	elif algorithm == 'nearest_neighbors':

	elif algorithm == 'kmeans':

	elif algorithm == 'linear_regression':

	else:
		print('unhandled algorithm', algorithm)

	results = test_model(model)
	if results:
		if results['score'] > 0.5:
			''' save model & weights files that api pulls from '''
				model_dir = '/home/ec2-user/model/'
				model_path = ''.join([model_dir, 'model.json'])
				model_weights_path =''.join([model_dir, 'weights.h5'])
				''' to do: save '''

	return False

def test_model(model):
	''' add test metrics & output a score '''
	return False


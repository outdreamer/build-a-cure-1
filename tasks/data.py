import itertools, os, json, sys

import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

import networkx as nx
import networkx.generators.small as gs

import numpy as np
from numpy import array

import scipy
from scipy.sparse import random as sparse_random

#import xgboost

# to do: add regressors for classifiers if available
# from xgboost import XGBClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA, LatentDirichletAllocation, TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, StandardScaler

from sklearn.random_projection import sparse_random_matrix
from sklearn.metrics import accuracy_score, f1_score, classification_report,confusion_matrix

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from graph import add_graph, save_graph
from reduction import reduce_features
from sanitize import convert_data, json_to_csv

mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["r", "k", "c"]) 

def get_features(data, label_column_name):
	'''
	df.loc['index_col_value'] # get row for index col value
	df.loc['index_col_value', 'col_name'] # select value at row, column
	df.loc[['index_col_value1', 'index_col_value2']] # return df containing the two rows referenced
	df.loc[df['col_name1'] > 6, ['col_name2']] # filter values by col_name1 filter_condition, returning col_name2

	# Rows:
	data.iloc[0] # first row of data frame - Note a Series data type output.
	data.iloc[1] # second row of data frame
	data.iloc[-1] # last row of data frame 
	
	# Columns:
	data.iloc[:,0] # first column of data frame (first_name)
	data.iloc[:,1] # second column of data frame (last_name)
	data.iloc[:,-1] # last column of data frame (id)

	# Multiple row and column selections using iloc and DataFrame
	data.iloc[0:5] # first five rows of dataframe
	data.iloc[:, 0:2] # first two columns of data frame with all rows
	data.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
	data.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).
	'''
	''' assume last column without additional info, 
		and if label column name not found,
		or column with other predicted variable attributes isnt found (boolean, average variance level that isnt unique id, etc)
	'''
	if label_column_name is None:
		for col_name in data.columns:
			print('col', col_name, type(data[col_name]), data[col_name], 'col name', data[col_name].name)
		x_features = data.iloc[:,:-1]
	else:
		x_features = data
		if label_column_name in x_features.keys():
			x_features = x_features.drop(columns=label_column_name)
	print('get_features', len(x_features), x_features.keys())
	if len(x_features) > 0:
		return x_features
	return False

def get_label_column(data):
	y_labels = data.iloc[:,-1]
	print('get_label_column', type(y_labels), y_labels)
	return y_labels

def filter_reduced_features(results):
	''' to do: evaluate reductions & select remaining features '''
	return False

def regularize_data(data, regularizations):
	return False

def split_data_by_algorithm(data):
	''' split into nlp/clustering/decision tree data variables & associated predicted independent variables '''
	return False

def explain_model(model):
	''' add lime & other explanatory tools '''
	return False

def predict_class_probabilities(y_labels, model):
	''' predict probability of a class '''
	probabilities = {}
	for category in set(y_labels):
		probability = model.predict_proba(category)
		print('category', category, 'probability', probability)	
		probabilities[category] = probability
	if probabilities:
		return probabilities
	return False

def pull_function_def(algorithm):
	code = []
	params = {}
	reqs = []
	return False

def check_params_for_data(algorithm, params, data):
	return False

def update_params(algorithm, params, data):
	return False

def check_requirements_for_data(algorithm, requirements, params, data):
	return False

def check_algorithm(algorithm, data):
	result = {}
	''''
	code, params, requirements = pull_function_def(algorithm)
	params_pass = check_params_for_data(algorithm, params, data)
	if not params_pass:
		params = update_params(algorithm, params, data)
	reqs_pass = check_requirements_for_data(algorithm, requirements, params, data)
	if reqs_pass:
		return result
	'''
	return True

def select_algorithms_for_data(data, problem_type, reductions, algorithms, model_tasks, graphs):
	'''
		- sanitize & transform data
		- reduce features with reductions passed in
		- if classification, apply algorithms passed in
		- otherwise, apply training algorithms passed in
		- if results found, analyze prediction results
		- integrate results to produce insights on data set
		- visualize integrated results
	'''
	''' to do: filter options by problem type & data set '''

	standard_nns = ['cnn', 'mlp', 'gan', 'recurrent', 'ltsm']
	ensemble = ['adaboost', 'boosting', 'bagging', 'xgb', 'gradient_boosted_decision_tree', 'gradient_boosting_machine', 'random_forest', 'stacked_generalization']
	# unsupervised clustering with methods appropriate according to varying density measures
	clustering = ['knn', 'kmeans', 'dbscan', 'expectation-maximization', 'hierarchical', 'random_forest']
	# unsupervised
	unsupervised = ['hierarchical_clustering', 'gan', 'kmeans', 'mixture', 'dbscan', 'local_outlier_factor', 'autoencoder', 'deep_belief', 'self_organizing_map', 'expectation-maximization', 'pca', 'ica', 'nmf', 'svd']
	# supervised
	supervised = ['svm', 'knn', 'regression', 'decision_tree', 'naive_bayes', 'lda', 'learning_vector_quant']
	# dimensionality reduction
	reductions = ['dirichlet', 'pca', 'lda', 'svd', 'tsne', 'ica', 'nmf', 'mds', 'autoencoder', 'self_organizing_map'] # multidimensional scaling, non-negative matrix factorization
	regressions = ['linear', 'binary', 'mixed', 'nonparametric', 'nonlinear', 'polynomial', 'binomial', 'poisson', 'ordinal', 'logreg', 'gaussian_process', 'partial_least_squares', 'principal_components']
	anomaly = ['autoencoder', 'variational_autoencoders', 'local_outlier_factor', 'lstm', 'bayesian', 'hidden_markov', 'cluster_analysis_outlier_detection', 'knn', 'one-class svm', 'bagging', 'score_normalization']	
	# hierarchical_linear_models = ['random_effects'] # kernel_functions = ['radial_basis_function'] # function_approximation = ['radial_basis_function']
	
	''' default params '''
	model_tasks = ['apply_most_reduced_features', 'reduce', 'train', 'score']
	processes = ['sanitize', 'standardize', 'convert_type', 'regularize']
	regularizations = ['ridge', 'lasso', 'elastic_net']
	graphs = ['feature', 'variance', 'confusion', 'regression']
	algorithms = ['mlp', 'random_forest', 'xgb', 'ensemble', 'mixed'] # if a category is listed, decide if you need to pick one or use all
	
	if problem_type == 'anomaly':
		algorithms = anomaly
	elif problem_type == 'cluster':
		algorithms = clustering
	elif problem_type == 'supervised':
		algorithms = supervised
	elif problem_type == 'unsupervised':
		algorithms = unsupervised
	elif problem_type == 'regression':
		algorithms = regressions
	elif problem_type == 'standard_nns':
		algorithms = standard_nns
	elif problem_type == 'reduce_dimensions':
		''' just reduce & return features '''
		algorithms = reductions
	else:
		print('unknown problem type', problem_type)
	if len(algorithms) > 0:
		return algorithms
	return False

def apply_algorithm(algorithm, reductions, x_features, y_labels, model_tasks, components_count, graphs, params):
	model = None
	if algorithm == 'random_forest':
		model = RandomForestClassifier() # has methods: decision_path(X) & apply
	elif algorithm == 'xgb':
		model = XGBClassifier()
	elif algorithm == 'knn':
		model = KNeighborsClassifier()
	elif algorithm == 'kmeans':
		model = KMeans() 
		'''
		- fast
		- fails in local minima
		- If the algorithm stops before fully converging, the cluster_centers wont be the labels_ (means of each center)
		- labels_ are reassigned after last prediction
		attributes: cluster_centers (ndarray), labels (ndarray), inertia (float), n_iter (number of iterations run)
		variants: MiniBatchKMeans may be faster for large number of samples, does incremental updates of the centers positions using mini-batches
		methods: 
			- fit_predict(X[, y, sample_weight]) - Compute cluster centers and predict cluster index for each sample
			- has sample_weight param for its fit/transform/predict methods
		params: n_clusters=8, *, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='deprecated', verbose=0, random_state=None, copy_x=True, n_jobs='deprecated', algorithm='auto'
		'''
	elif algorithm == 'linear_regression':
		model = LinearRegression()
		'''
		params: *, fit_intercept=True, normalize=False, copy_X=True, n_jobs=None
		attributes: coef_, rank_, singular_, intercept_
		methods:
			- has sample_weight param for its fit/score methods
		'''
	elif algorithm == 'logreg':
		model = LogisticRegression()
	elif algorithm == 'ridge':
		model = Ridge()
	elif algorithm == 'lasso':
		model = Lasso()
		'''
		params: alpha=1.0, *, fit_intercept=True, normalize=False, precompute=False, copy_X=True, max_iter=1000, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic'
		'''
	elif algorithm == 'elastic_net':
		model = ElasticNet()
		'''
		params: alpha=1.0, *, l1_ratio=0.5, fit_intercept=True, normalize=False, precompute=False, max_iter=1000, copy_X=True, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')[source]
		attributes: coef_, sparse_coef_, intercept_, n_iter_
		methods:
			- has sample_weight param for its fit/score methods
			- path(X, y, *[, l1_ratio, eps, n_alphas, …]) - compute elastic net path with coordinate descent
		variants:
			ElasticNetCV: Elastic net model with best model selection by cross-validation.
			SGDRegressor: implements elastic net regression with incremental training.
			SGDClassifier: implements logistic regression with elastic net penalty (SGDClassifier(loss="log", penalty="elasticnet"))
		'''
	elif algorithm == 'dirichlet':
		model = LatentDirichletAllocation() 
	elif algorithm == 'lda':
		model = LinearDiscriminantAnalysis()
	elif algorithm == 'mlp':
		model = MLPClassifier()	
	else:
		print('unhandled algorithm', algorithm)
		''' algorithm will also be null if we're just applying reductions '''

	if model is not None or 'reduce' in model_tasks:
		results = {}
		if algorithm and model:
			for k, v in params[algorithm].items():
				model = model.set_params(**{k: v})
			''' train the original model '''
			result = model_train(algorithm, model, x_features, y_labels, model_tasks, components_count, graphs)
			if result:
				results['original'] = result
		if 'reduce' in model_tasks:
			''' reduce features and train a new model on each reduced feature set '''
			iterative_reduced_features = x_features if 'iterative_reduce' in model_tasks else None					
			for reduction in reductions:
				features_to_reduce = iterative_reduced_features if 'iterative_reduce' in model_tasks else x_features
				reduced_feature_result = reduce_features(features_to_reduce, y_labels, components_count, algorithm)
				if reduced_feature_result:
					print('starting features to reduce', features_to_reduce, 'reduced features', reduced_feature_result['features'])
					''' update iteratively reduced feature set '''
					iterative_reduced_features = reduced_feature_result['features'] if 'iterative_reduce' in model_tasks else iterative_reduced_features
					''' train new model on reduced features '''
					if 'score' in model_tasks or 'train' in model_tasks:
						reduced_feature_model = model_train(algorithm, model, reduced_feature_result['features'], y_labels, model_tasks, components_count, graphs)
						if reduced_feature_model:
							iteration_name = ''.join(['iteration', reduction])
							results[iteration_name] = reduced_feature_model
		if results:
			if 'apply_most_reduced_features' in model_tasks:
				''' find most reduced feature set across all reduced feature sets & train new model on that most reduced set'''
				reduced_features = filter_reduced_features(results)
				if reduced_features:
					reduced_feature_model = model_train(algorithm, model, reduced_features, y_labels, model_tasks, components_count, graphs)
					if reduced_feature_model:
						results['iteration_most_reduced'] = reduced_feature_model
			return results
	return False

def model_train(algorithm, model, x_features, y_labels, model_tasks, components_count, graphs):
	x_train, x_test, y_train, y_test = train_test_split(x_features, y_labels, test_size=0.2, random_state=27)
	print('x_train', type(x_train), len(x_train), 'any', x_train.any(), x_train.head())
	print('x_test', type(x_test), len(x_test), 'any', x_test.any(), x_test.head())
	print('y_train', type(y_train), len(y_train), 'any', y_train.any(), y_train.head())
	print('y_test', type(y_test), len(y_test), 'any', y_test.any(), y_test.head())
	print(dir(model))
	if not x_train.empty and not x_test.empty and not y_train.empty and not y_test.empty:
		model_methods = dir(model)
		result = {}
		result['model'] = model
		result['features'] = model.fit_transform(x_features, y_labels) if 'fit_transform' in model_methods else model.fit(x_features, y_labels)
		result['components'] = model.components_ if 'components_' in model_methods else None
		result['predictions'] = model.predict(x_test)
		result['class_probabilities'] = predict_class_probabilities(y_labels, model) if 'predict_proba' in model_methods else None
		result['coef'] if 'coef_' in model_methods else None # array of shape (n_features, ) or (n_targets, n_features) based on how many targets are passed in
		result['intercept'] if 'intercept_' in model_methods else None
		# add rank_ & singular_ attributes of matrix for regression where applicable
		result['explained_variance'] = model.explained_variance_ if 'explained_variance_' in model_methods else None
		result['score'] = model.score(x_test, y_test)
		# result['cv_scores'] = cross_val_score(model, x_test, y_test, cv=5) # take the average of cross validation scores
		result['acc'] = accuracy_score(y_test, result['predictions'])
		'''
		result['f1'] = f1_score(y_test, result['predictions'])
		'''
		print('result', result)

		if 'save' in model_tasks:
			model_dir = '/home/ec2-user/model/'
			model_path = ''.join([model_dir, algorithm, '_', '-'.join(model_tasks), '_model.json'])
			model_weights_path =''.join([model_dir, algorithm, '_', '-'.join(model_tasks), '_weights.h5'])
			save(model, model_path, model_weights_path)

		if 'train' in model_tasks:
			return {'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test, 'new_features': x_features, 'model': model}

		if len(graphs) > 0:
			for graph in graphs:
				if graph == 'variance' and 'explained_variance' in result:
					variance_image_path = save_graph(result['explained_variance'], 'bar', ''.join([algorithm, 'feature variance']), algorithm, 'explained variance', None)
					if variance_image_path:
						result['variance_image'] = variance_image_path
				if graph == 'feature' and 'features' in result:
					feature_image_path = save_graph(result['features'], 'scatter', ''.join([algorithm, 'features with components: ', components_count]), 'variation', 'features', None)
					if feature_image_path:
						result['feature_image'] = feature_image_path
				if graph == 'confusion' and not y_test.empty and len(result['predictions']) > 0:
					result['confusion_matrix'] = confusion_matrix(y_test, result['predictions'])
					result['classification_report'] = classification_report(y_test, result['predictions'])
					confusion_image = save_graph(result['confusion_matrix'], 'confusion', 'confusion_matrix', '', '', None)
					if confusion_image:
						result['confusion_image'] = confusion_image
	return result

def convert_reduce_classify_train_score_graph(data, label_column_name, problem_type, processes, reductions, regularizations, algorithms, model_tasks, graphs):
	''' to do: add custom processes, reductions, regularization & model_tasks according to data set/algorithm '''

	''' to do: retain original copy of data if processing is done before this function call '''

	if label_column_name is None:
		label_column_name = y_labels.name

	if 'convert_type' in processes:
		''' to do: add data type check '''
		''' to do: derive label_column_name if not present '''
		converted_data, removed_cols = convert_data(data, label_column_name, ['datetime', 'one_hot_encoding', 'low_value', 'text'])
		if removed_cols:
			print('removed_cols', removed_cols)
		if converted_data.empty:
			data = converted_data

	print('converted', data.head())

	y_labels = data[label_column_name] if label_column_name in data else get_label_column(data)

	if 'regularize' in processes:
		regularized_data = regularize_data(data, regularizations)
		if regularized_data:
			data = regularized_data
	
	print('label column', label_column_name, 'y label', y_labels)
	x_features = get_features(data, label_column_name)
	print('x features', x_features.keys())
	
	components_count = len(x_features) # int(round(len(x_features) / 3, 0)) if len(x_features) < 100 else int(round(len(x_features) / 10, 0))
	print('components count', components_count)

	if algorithms is None or len(algorithms) == 0:
		algorithms = select_algorithms_for_data(data, problem_type, reductions, algorithms, model_tasks, graphs)

	if algorithms:
		algorithm_results = []
		for algorithm in algorithms:
			passed = check_algorithm(algorithm, data)
			if passed:
				''' passed contains updated params, given data & requirements & algorithm '''
				''' to do: calculate params for data set '''
				params = {
					'ridge': {'alpha': 0.5},
					'lasso': {'alpha': 0.5},
					'elastic_net': {'alpha': 0.5},
					'knn': {'n_neighbors': 5},
					'random_forest': {'max_depth': 2, 'random_state': 0},
					'xgb': {'n_estimators': 600, 'objective': 'binary:logistic', 'silent': True, 'nthread': 1},
					'lda': {'n_components': components_count},
					'mlp': {'solver': 'adam', 'alpha': 0.0001, 'activation': 'relu', 'batch_size': 150, 'hidden_layer_sizes': (200, 100), 'random_state': 1},
					'dirichlet': {'n_components': components_count, 'random_state': 0}
				}
				results = apply_algorithm(algorithm, reductions, x_features, y_labels, model_tasks, components_count, graphs, params)
				if results:
					algorithm_results.append(results)
		if len(algorithm_results) > 0:
			return algorithm_results
	return False

csv_path = ''.join([os.getcwd(), '/tasks/data/event/botsv1.fgt_event_50.csv'])
data = pd.read_csv(csv_path)
print('df head', data.head()) #head(10)
#         convert_reduce_classify_train_score_graph(data, label_column_name, problem_type, processes, reductions, regularizations, algorithms, model_tasks, graphs):
results = convert_reduce_classify_train_score_graph(data, 'level', 'score', ['convert_type'], [], [], ['mlp'], ['reduce', 'score'], []) #, ['variance', 'feature', 'confusion'])

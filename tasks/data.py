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

import xgboost

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.decomposition import PCA, LatentDirichletAllocation, TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.random_projection import sparse_random_matrix
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["r", "k", "c"]) 

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
	code, params, requirements = pull_function_def(algorithm)
	params_pass = check_params_for_data(algorithm, params, data)
	if not params_pass:
		params = update_params(algorithm, params, data)
	reqs_pass = check_requirements_for_data(algorithm, requirements, params, data)
	if reqs_pass:
		return result
	return False

def select_algorithms_for_data(data, problem_type, reductions, classifiers, algorithms, intents, graphs):
	'''
		- sanitize & transform data
		- reduce features with reductions passed in
		- if classification, apply classifiers passed in
		- otherwise, apply training algorithms passed in
		- if results found, analyze prediction results
		- integrate results to produce insights on data set
		- visualize integrated results
	'''
	''' to do: filter options by problem type & data set '''

	standard_nns = ['cnn', 'mlp', 'gan', 'recurrent', 'ltsm']
	ensemble = ['adaboost', 'boosting', 'bagging', 'xgb', 'gradient_boosted_decision_tree', 'gradient_boosting_machine', 'random_forest', 'stacked_generalization']
	# unsupervised clustering with methods appropriate according to varying density measures
	clustering = ['knn', 'kmeans', 'dbscan', 'expectation-maximization', 'hierarchical']
	# unsupervised
	unsupervised = ['hierarchical_clustering', 'gan', 'kmeans', 'mixture', 'dbscan', 'local_outlier_factor', 'autoencoder', 'deep_belief', 'self_organizing_map', 'expectation-maximization', 'pca', 'ica', 'nmf', 'svd']
	# supervised
	supervised = ['svm', 'nearest_neighbors', 'regression', 'decision_tree', 'naive_bayes', 'lda', 'knn', 'learning_vector_quant']
	# dimensionality reduction
	reductions = ['dirichlet', 'pca', 'lda', 'svd', 'tsne', 'ica', 'nmf', 'mds', 'autoencoder', 'self_organizing_map'] # multidimensional scaling, non-negative matrix factorization
	regressions = ['linear', 'binary', 'mixed', 'nonparametric', 'nonlinear', 'polynomial', 'binomial', 'poisson', 'ordinal', 'logreg', 'gaussian_process', 'partial_least_squares', 'principal_components']
	anomaly = ['autoencoder', 'variational_autoencoders', 'local_outlier_factor', 'lstm', 'bayesian', 'hidden_markov', 'cluster_analysis_outlier_detection', 'knn', 'one-class svm', 'bagging', 'score_normalization']	
	# hierarchical_linear_models = ['random_effects']
	# kernel_functions = ['radial_basis_function'] # function_approximation = ['radial_basis_function']

	''' default params '''
	intents = ['apply_most_reduced_features', 'reduce', 'train', 'score']
	processes = ['sanitize', 'standardize', 'convert_type', 'regularize']
	regularizations = ['ridge', 'lasso']
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

def get_features_label_columns(data):
	''' assume last column without additional info '''
	y_labels = data.iloc[:, 0]
	X_features = data.iloc[:,1:] # drop y label
	return x_features, y_labels, 'label'

def filter_reduced_features(results):
	''' to do: evaluate reductions & select remaining features '''
	return False

def convert_reduce_classify_train_score_graph(data, problem_type, processes, reductions, regularizations, algorithms, intents, graphs):
	if 'convert_type' in processes:
		''' to do: add data type check '''
		''' to do: derive label_column_name if not present '''
		numeric_data = convert_data_to_numeric(data, label_column_name)
		if numeric_data:
			data = numeric_data
	if 'regularize' in processes:
		regularized_data = regularize_data(data, regularizations)
		if regularized_data:
			data = regularized_data
	x_features, y_labels, label_column_name = get_features_label_columns(data)
	components_count = int(round(len(x_features) / 3, 0)) if len(x_features) < 100 else int(round(len(x_features) / 10, 0))
	if algorithms is None or len(algorithms) == 0:
		algorithms = select_algorithms_for_data(data, problem_type, reductions, algorithms, intents, graphs)
	if algorithms:
		algorithm_results = []
		for algorithm in algorithms:
			passed = check_algorithm(algorithm, data)
			if passed:
				''' passed contains updated params, given data & requirements & algorithm '''
				results = apply_algorithm(algorithm, reductions, x_features, y_labels, intents, components_count, graphs)
				if results:
					algorithm_results.append(results)
		if len(algorithm_results) > 0:
			return algorithm_results
	return False

def regularize_data(data, regularizations):
	return False

def convert_data_to_numeric(data, label_column_name):
	''' 
		- sanitize data
		- encode categorical data
		- vectorize text data
		- map trajectories of text data
	'''

	categorical = data.iloc[:,:-1].select_dtypes('object').columns
	print('categorical', categorical)
	for i in categorical:
		print('categorical group count', data[i].unique())
	print('groups count', sum(data[categorical].nunique()))
	numeric = data._get_numeric_data()
	print('numerical', numeric)
	# convert numeric to float64
	data[numeric] = data[numeric].astype('float64')
	# data.describe() # outputs stats

	for col in data.columns:
		counts = col.value_counts()		
		print('counts', col, counts)
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

def confusion_matrix(x_features, y_labels, result):
	''' generate confusion matrix '''
	return False

def identify_algorithm_for_data(data):
	''' select an algorithm to use if one is not specified '''
	return False

def split_data_by_algorithm(data):
	''' split into nlp/clustering/decision tree data variables & associated predicted independent variables '''
	return False

def test_model(model):
	''' add test metrics & output a score '''
	return False

def explain_model(model):
	''' add lime & other explanatory tools '''
	return False

def fit_regression_model(method_name, x_features, y_labels):
	''' apply linear regression or other applicable regression type '''
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

def apply_algorithm(algorithm, reductions, x_features, y_labels, intents, components_count, graphs):
	model = None
	if algorithm == 'random_forest':
		pass
	elif algorithm == 'xgb':
		pass
	elif algorithm == 'knn':
		pass
	elif algorithm == 'kmeans':
		pass
	elif algorithm == 'linear_regression':
		pass
	elif algorithm == 'logreg':
		model = LogisticRegression()
	elif algorithm == 'dirichlet':
		model = LatentDirichletAllocation() if components_count is None else LatentDirichletAllocation(n_components=components_count) # random_state=0)
	elif algorithm == 'lda':
		model = LinearDiscriminantAnalysis() if components_count is None else LinearDiscriminantAnalysis(n_components=components_count)
	elif algorithm == 'xgb':
		model = xgboost.XGBClassifier(n_estimators=600, objective='binary:logistic', silent=True, nthread=1)
	elif algorithm == 'mlp':
		model = MLPClassifier(solver='adam', alpha=0.0001, activation='relu', batch_size=150, hidden_layer_sizes=(200, 100), random_state=1)
	else:
		print('unhandled algorithm', algorithm)
		''' algorithm will also be null if we're just applying reductions '''
	if model is not None or 'reduce' in intents:
		results = {}
		if algorithm and model:
			''' train the original model '''
			result = model_train(algorithm, model, x_features, y_labels, intents, components_count, graphs)
			if result:
				results['original'] = result
		if 'reduce' in intents:
			''' reduce features and train a new model on each reduced feature set '''
			iterative_reduced_features = x_features if 'iterative_reduce' in intents else None					
			for reduction in reductions:
				features_to_reduce = iterative_reduced_features if 'iterative_reduce' in intents else x_features
				reduced_feature_result = reduce_features(features_to_reduce, y_labels, components_count, algorithm)
				if reduced_feature_result:
					''' update iteratively reduced feature set '''
					iterative_reduced_features = reduced_feature_result['features'] if 'iterative_reduce' in intents else iterative_reduced_features
					''' train new model on reduced features '''
					if 'score' in intents or 'train' in intents:
						reduced_feature_model = model_train(algorithm, model, reduced_feature_result['features'], y_labels, intents, components_count, graphs)
						if reduced_feature_model:
							iteration_name = ''.join(['iteration', reduction])
							results[iteration_name] = reduced_feature_model
		if results:
			if 'apply_most_reduced_features' in intents:
				''' find most reduced feature set across all reduced feature sets & train new model on that most reduced set'''
				reduced_features = filter_reduced_features(results)
				if reduced_features:
					reduced_feature_model = model_train(algorithm, model, reduced_features, y_labels, intents, components_count, graphs)
					if reduced_feature_model:
						results['iteration_most_reduced'] = reduced_feature_model
			return results
		return result
	return False

def model_train(algorithm, model, x_features, y_labels, intents, components_count, graphs):
	x_train, x_val, y_train, y_val = train_test_split(x_features, y_labels, test_size=0.2, random_state=27)
	if x_train and x_val and y_train and y_val:
		if 'save' in intents:
			model_dir = '/home/ec2-user/model/'
			model_path = ''.join([model_dir, algorithm, '_', '-'.join(intents), '_model.json'])
			model_weights_path =''.join([model_dir, algorithm, '_', '-'.join(intents), '_weights.h5'])
			save(model, model_path, model_weights_path)
		if 'train' in intents:
			return {'x_train': x_train, 'x_val': x_val, 'y_train': y_train, 'y_val': y_val, 'new_features': x_features, 'model': model}
		result['model'] = model
		result['predictions'] = model.predict(x_val)
		result['score'] = model.score(x_val, y_val)
		result['acc'] = accuracy_score(y_val, result['predictions'])
		result['f1'] = f1_score(y_val, result['predictions'])
		result['explained_variance'] = model.explained_variance_
		result['features'] = model.fit_transform(x_features)
		result['components'] = model.components_
		if len(graphs) > 0:
			for graph in graphs:
				if graph == 'variance':
					variance_image_path = save_graph(result['explained_variance'], 'bar', ''.join([algorithm, 'feature variance']), algorithm, 'explained variance', None)
					if variance_image_path:
						result['variance_image'] = variance_image_path
				if graph == 'feature':
					feature_image_path = save_graph(result['features'], 'scatter', ''.join([algorithm, 'features with components: ', components_count]), 'variation', 'features', None)
					if feature_image_path:
						result['feature_image'] = feature_image_path
				if graph == 'confusion':
					confusion_matrix = confusion_matrix(x_features, y_labels, result)
					if confusion_matrix:
						result['confusion_image'] = confusion_matrix
	return result

def reduce_features(X_features, y_labels, components_count, reduction_name):
	''' 
	X_features is in a dataframe, output by pandas.read_csv()
	components_count is the number of features to reduce to
	apply svd, lda, pca, t-sne & other feature reduction methods once data is filtered to numeric variables 
	'''
	'''
	transform() & fit_transform():
		- apply dimensionality reduction to x, returns x_new, array-like shape(samples, components)
		- dirichlet.transform() returns doc_topic_distribution shape(samples, components)
		- lda.transform() projects data to maximize class separation
		- tsne.transform() doesnt exist
	'''
	reduction_method = None
	if reduction_name == 'pca':
		'''
		PCA (n_components=None, *, copy=True, whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None)

		alt: KernelPCA

		method:
			- find top features explaining variance with eigenvalues of eigenvectors
		'''
		reduction_method = PCA() if components_count is None else PCA(n_components=components_count) # svd_solver='full', 'arpack')
	elif reduction_name == 'svd':
		'''
		"TruncatedSVD/lsa (n_components=2, *, algorithm='randomized', n_iter=5, random_state=None, tol=0.0):
			- Contrary to PCA, this estimator does not center the data before computing the singular value decomposition. This means it can work with sparse matrices efficiently
			- truncated SVD works on term count/tf-idf matrices as returned by the vectorizers in sklearn.feature_extraction.text. In that context, it is known as latent semantic analysis (LSA)
			- supports two algorithms: a fast randomized SVD solver, and a “naive” algorithm that uses ARPACK as an eigensolver on X * X.T or X.T * X, whichever is more efficient
			- SVD suffers from a problem called “sign indeterminacy”, which means the sign of the components_ and the output from transform depend on the algorithm and random state.
			  To work around this, fit instances of this class to data once, then keep the instance around to do transformations."

		method:
			- select explanatory left features of output matrix, using:
				- singular-to-diagonal transform executed by multiplying:
				 	- orthogonal matrix U x * x, diagonal matrix D x * y, and orthogonal matrix V y * y that approximate original matrix A

		'''
		reduction_method = TruncatedSVD() if components_count is None else TruncatedSVD(n_components=components_count, algorithm='randomized') 
		# n_components = 100 for lsa, n_iter & random_state for randomized solver, tol for arpack
	elif reduction_name == 'dirichlet':
		''' 
		LatentDirichletAllocation (n_components=10, *, doc_topic_prior=None, topic_word_prior=None, learning_method='batch', learning_decay=0.7, learning_offset=10.0, max_iter=10, batch_size=128, 
		evaluate_every=-1, total_samples=1000000.0, perp_tol=0.1, mean_change_tol=0.001, max_doc_update_iter=100, n_jobs=None, verbose=0, random_state=None)
		
		input: array-like or sparse matrix, [samples, features]

		output: doc_topic_distribution for X, shape= (samples, components)

		method: learns a model using variational bayes, then transforms to fit that model
		'''
		#X, _ = make_multilabel_classification(random_state=0)
		reduction_method = LatentDirichletAllocation() if components_count is None else LatentDirichletAllocation(n_components=components_count) # random_state=0)

	elif reduction_name == 'lda':
		'''
		LinearDiscriminantAnalysis (*, solver='svd', shrinkage=None, priors=None, n_components=None, store_covariance=False, tol=0.0001) # solver = ‘svd’ (doesnt compute cov unless store_covariance is True), ‘lsqr’, ‘eigen’

		"A classifier with a linear decision boundary, generated by fitting class conditional densities to the data and using Bayes’ rule.
		The model fits a Gaussian density to each class, assuming that all classes share the same covariance matrix.
		The fitted model can also be used to reduce the dimensionality of the input by projecting it to the most discriminative directions, using the transform method."

		attributes:

		    coef_ - ndarray of shape (n_features,) or (n_classes, n_features) Weight vector(s).
		    intercept_ - ndarray of shape (n_classes,) Intercept term.
		    covariance_ - array-like of shape (n_features, n_features) Weighted within-class covariance matrix. 
		    	It corresponds to sum_k prior_k * C_k where C_k is the covariance matrix of the samples in class k. 
		    	The C_k are estimated using the (potentially shrunk) biased estimator of covariance. If solver is ‘svd’, only exists when store_covariance is True.
		    explained_variance_ratio_ - ndarray of shape (n_components,)
		    means_ - array-like of shape (n_classes, n_features) Class-wise means.
		    priors_ - array-like of shape (n_classes,) Class priors (sum to 1).
		    scalings_ - array-like of shape (rank, n_classes - 1) Scaling of the features in the space spanned by the class centroids. Only available for ‘svd’ and ‘eigen’ solvers.
		    xbar_ - array-like of shape (n_features,) Overall mean. Only present if solver is ‘svd’.
		    classes_ - array-like of shape (n_classes,) Unique class labels.

		method:
			- separate classes with line by mapping features into lower dimensional space (assuming means are far from each other)
				- calculate class means distance or inter-class variance 
					- calculate intra-class variance (distance between mean & sample)
						- construct lower-dimensional space maximizing inter-class variance
		'''

		reduction_method = LinearDiscriminantAnalysis()
		# reduction_method.predict([[-0.8, -1]])

	elif reduction_name == 'tsne':

		''' tsne (n_components=2, *, perplexity=30.0, early_exaggeration=12.0, learning_rate=200.0, n_iter=1000, n_iter_without_progress=300, min_grad_norm=1e-07, 
			metric='euclidean', init='random', verbose=0, random_state=None, method='barnes_hut', angle=0.5, n_jobs=None)

			"converts similarities between data points to joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data. t-SNE has a cost function that is not convex, i.e. with different initializations we can get different results.
			It is highly recommended to use another dimensionality reduction method (e.g. PCA for dense data or TruncatedSVD for sparse data) to reduce the number of dimensions to a reasonable amount (e.g. 50) if the number of features is very high"

			attributes:
				embedding_ - array-like, shape (n_samples, n_components) - Stores the embedding vectors 
	    		kl_divergence_ - float - Kullback-Leibler divergence after optimization.
				n_iter_ - int - number of iterations run

			output: Embedding of the training data in low-dimensional space

		'''
		reduction_method = TSNE(n_components=components_count) # reduction_method.shape
	else:
		print('unknown method', reduction_name)

	if reduction_method:
		result = {'reduction_method': reduction_method}
		result['features'] = reduction_method.fit_transform(X_features) # input is array-like shape(samples, features), returns X_new, ndarray array of shape(samples, components)
		result['y_labels'] = y_labels
		result['model'] = reduction_method
		result['components'] = reduction_method.components_ # principal axes, sorted by explained_variance_
		result['singular_values'] = reduction_method.singular_values_ # singular values of components (2-norms of components in lower dimensional space)
		result['explained_variance'] = reduction_method.explained_variance_ # amount of variance explained by each feature
		result['explained_variance_ratio'] = reduction_method.explained_variance_ratio_
		print('feature reduction', reduction_name, '\n\tOriginal feature #', X_features.shape[1], '\n\tReduced feature #', result['features'].shape[1])
		return result
	return False

def save_graph(data, graph_type, graph_label, xlabel, ylabel, zlabel):
	mkdir('graphs')
	formatted_graph_label = ''.join([g for g in graph_label.lower() if g in 'abcdefghijklmnopqrstuvwxyz-_ ']).replace(' ', '_')
	image_path = ''.join(['graphs/', formatted_graph_label, '_', graph_type, '.png'])
	data['x'] = array(data['x']) if 'x' in data else []
	data['y'] = array(data['y']) if 'y' in data else [] #ndarray
	data['z'] = array(data['z']) if 'z' in data else [0 for x in xs]
	fig = plt.figure()
	plt.legend()
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	axs = Axes3D(fig) if len(data['z']) > 0 else Axes2D
	if zlabel is not None:
		plt.zlabel(zlabel)
	cm = plt.get_cmap("RdYlGn")
	colors = [cm(float(i)/len(data['x'])) for i in range(len(data['x']))]
	if graph_type in ['regression', 'scatter', 'line']:
		if graph_type == 'regression':
			scatter_fig, scatter_axs = add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel)
			fig, axs = add_graph(data, scatter_fig, scatter_axs, graph_type, graph_label, xlabel, ylabel, zlabel)
		elif graph_type == 'line' or graph_type == 'scatter':
			fig, axs = add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel)
	elif graph_type == 'bar':
		plt.figure(figsize=(8, 6))
		plt.bar(range(22), data, alpha=0.5, align='center', label=graph_label) # data is pca.explained_variance_ 
	elif graph_type == 'network':
		graph = add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel)
	if graph or fig:
		''' to do: detect runtime env and show if in notebook or save if not '''
		#plt.show()
		plt.savefig(image_path)
	plt.close()
	return image_path

def add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel):
	''' to do: determine dimensions & range '''	
	''' add options like network graph, word stats, clusters and create an image that can be retrieved by api '''
	image_url = ''
	# api_url = ''.join(['https://', instance_ip, 'api_url'])

	if graph_type in ['scatter', 'line']:
		if graph_type == 'line':
		    points = np.array([data['x'], data['y']]).T.reshape(-1, 1, 2)
		    segments = np.concatenate([points[:-1], points[1:]], axis=1)
		    fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
		    norm = plt.Normalize(0, data['y'].max())
		    lc = LineCollection(segments, cmap='viridis') #, norm=norm)
		    lc.set_array(position)
		    lc.set_linewidth(2)
		    line = axs[0].add_collection(lc)
		    fig.colorbar(line, ax=axs[0])
		    axs[0].set_xlim(0, data['x'].max())
		    axs[0].set_ylim(0, data['y'].max())
		    fig.delaxes(axs[1])
		else:
		    #default = ax.scatter3D(data['x'], data['y'], data['z'], c=colors, cmap=cm)
		    if 'class' in data:
			    plt.scatter(data[:,0], data[:,5], c=data['class'])
		    elif 'z' in data:
		    	axs.plot3D(data['x'], data['y'], data['z'], 'gray')
		    else:
		    	axs.plot2D(data['x'], data['y'], 'gray')
		return fig, axs
	elif graph_type == 'network':
		G = nx.Graph() # graph_object = nx.read_gml(data)
		for i in data:
			G.add_node(i['source'], nodelabel=i['source_label'])
			G.add_node(i['target'], nodelabel=i['target_label'])
			G.add_edge(i['source'], i['target'])
		G[i['source']][i['target']]['color'] = 'blue'
		nx.write_gml(G, data)
		graph = nx.draw(G, with_labels=True)
		return graph
	return False
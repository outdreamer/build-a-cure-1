	
	kernel_functions = ['radial_basis_function'] # weighting
	ann = ['cnn', 'mlp', 'gan', 'recurrent', 'ltsm']
	ensemble = ['adaboost', 'boosting', 'bagging', 'xgb', 'gradient_boosted_decision_tree', 'gradient_boosting_machine', 'random_forest', 'stacked_generalization']
	clustering = ['knn', 'kmeans', 'dbscan', 'expectation-maximization', 'hierarchical', 'svm_clustering']
	unsupervised = ['hierarchical_clustering', 'gan', 'kmeans', 'mixture', 'dbscan', 'local_outlier_factor', 'autoencoder', 'deep_belief', 'self_organizing_map', 'expectation-maximization', 'pca', 'ica', 'nmf', 'svd']
	supervised = ['svm', 'nearest_neighbors', 'regression', 'decision_tree', 'naive_bayes', 'lda', 'knn', 'learning_vector_quant']
	reductions = ['dirichlet', 'pca', 'lda', 'svd', 'tsne', 'ica', 'nmf', 'mds', 'autoencoder', 'self_organizing_map'] # multidimensional scaling, non-negative matrix factorization
	regressions = ['linear', 'binary', 'mixed', 'nonparametric', 'nonlinear', 'polynomial', 'binomial', 'poisson', 'ordinal', 'logreg', 'gaussian_process', 'partial_least_squares', 'principal_components']
	anomaly = ['autoencoder', 'variational_autoencoders', 'local_outlier_factor', 'lstm', 'bayesian', 'hidden_markov', 'cluster_analysis_outlier_detection', 'knn', 'one-class svm', 'bagging', 'score_normalization']
	regularizations = ['ridge', 'lasso']
	parameters = []
	metrics = []
	limits = []
	assumptions = [
		'random variable', 'regression linearity', 'homogeneity of error variances', 'independence/normality of error terms', 'homogeneity of regression slopes', 'independence/orthogonality of variables'
	]
	problems = ['multicollinearity', 'bias', 'assumption', 'method_mismatch']
	efficiencies = [
		'similar structures like a boundary and a phase shift', 
		'phase shifts like when a change type converts to another', 
		'existing differences as an input/source of other differences'
	] # why some information is more adjacently mappable to other information
	all_intents = {
		'regression': {}, 
		'predict', 
		'classify': {
			'linear',
			'nonlinear with kernel function'
		}
		'normalize', 
		'regularize', 
		'detect outlier', 
		'identify clusters', 
		'differentiate clusters', 
		'combine'
	}
	alternatives = {}
	alternatives['cov_adjustments'] = ['ANCOVA', 'random_effects'] # analysis of covariance
	alternatives['dependent_mean_equality_across_independent_category_without_continuous_covariates'] = ['ANOVA/regression', 'ANCOVA']
	definition_schema = {
		'name': {
			'definitions': []
			'related_objects': {},
			'alternatives': [], # interchangeable or alternate methods, not variants of this method
			'assumptions': [],
			'variants': {
				'reason_why_it_varies_varied_attribute_or_variant_type': {
					'attribute_or_function': 'specific_variant'
				}
			},
			'types': [],
			'usage_intents': [], # used for, used in
			'problems': [], # problems are also indexed in intents::strategies, where intents include solving problems
			'intents::strategies': [
				'general_intent_or_priority': ['specific_intent'],
				'specific_intent': {
					'general strategy': 'specific strategy'
				}
			],
			'functional_reasons': {}, # this is reasons why a structure/method combination works, like why aggregating into an ensemble method is effective
			'insights': [],
			'method_steps': []
		}
	}
	methods = {
		'multidimensional_scaling': {
			'definitions': [
				'visualize similarity (pairwise distance) across data points in cartesian space', 
				'principal coordinates analysis', 
				'input pair-difference matrix & output coordinate matrix minimizing strain loss function'
			],
			'related_objects': {},
			'alternatives': [], 
			'assumptions': ['euclidean distance'],
			'variants': {
				'general': {
					'metricMDS': 'cost function is residual sum of squares'
				}
			},
			'types': [],
			'usage_intents': [],
			'problems': [],
			'intents::strategies': {},
			'functional_reasons': {},
			'insights': ["coordinate matrix x can be derived from b = x * x' with eigenvalue decomposition, and b can be computed from proximity matrix d with double centering"],
			'method_steps': [
				'find squared proximity matrix d',
				'apply double centering to compute b, using centering matrix J, with n as number of objects',
				'determine m largest eigenvalues & their eigenvectors of b, with m as number of target dimensions',
				'x is eigenvector matrix multiplied by square root of diagonal matrix of eigenvalues of b'
			],
			
		},
		'svm': {
			'definitions': [
				'non-probabilistic binary linear classifier',
				'assigns new data to one category or the other, given labeled data with two label categories',
				'maximizes difference between example data points of different categories, predicting category by side of gap'
			]
			'related_objects': {},
			'alternatives': [], # interchangeable or alternate methods, not variants of this method
			'assumptions': [],
			'variants': {
				'type': {
					'probabilistic': 'platt_scaling'
				},
				'unsupervised': {
					'clustering': 'support_vector_clustering'
				}
			},
			'types': [
				'supervised'
			],
			'usage_intents': [],
			'problems': [],
			'intents::strategies': [
				'classification': ['linear', 'nonlinear with kernel map to higher dimensional spaces'],
				'regression',
				'find_svm_classifier': {
					'descent': ['sub-gradient', 'coordinate']
				}
			],
			'functional_reasons': {},
			'insights': [],
			'method_steps': []
		},
		'kernel': {
			'definitions': [
				'method of mapping an input-output relationship to a space where different sets are linearly separable'
			]
			'related_objects': {
				'kernel_function': {
					'function': {
						'integration/aggregation': 'weighted sum function', 
						'differentiation': ''.join([
							"function that calculates a weighted sum of similarities of new x' to origin data set x-values (similarities found with the kernel mapping x to x'),",
							"with weights applied to each origin input x-value's similarity to x' indicating importance of that origin input in determining y",
							"to find output y for each new x'"
						])
					}
				}
			},
			'alternatives': [],
			'assumptions': [],
			'variants': {
				'reason_why_it_varies_varied_attribute_or_variant_type': {
					'attribute_or_function': 'specific_variant'
				}
			},
			'types': [],
			'usage_intents': {
				'functions': [
					'compute differences with a lower-dimensional calculation',
					'convert function into a higher-dimensional function by replacing features with kernel function',
				],
				'neural networks': ['svm', 'kernel perceptron', 'gaussian_process', 'pca', 'canonical_correlation_analysis', 'ridge_regression', 'spectral_clustering', 'linear_adaptive_filters']
			},
			'problems': [],
			'intents::strategies': [
				'general_intent': ['specific_intent'],
				'specific_intent': {
					'general strategy': 'specific strategy'
				}
			],
			'functional_reasons': {},
			'insights': [
				'avoids computation cost of explicitly mapping a data set to another space with a feature map, using kernel functions to map to inner product spaces using existing variables'
			],
			'method_steps': []
		}

	}
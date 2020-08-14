	assumptions = ['random variable', 'regression linearity', 'homogeneity of error variances', 'independence/normality of error terms', 'homogeneity of regression slopes', 'independence/orthogonality of variables']
	problems = ['multicollinearity', 'bias', 'assumption', 'method_mismatch']
	methods = {
		'multidimensional_scaling': {
			'definitions': [
				'visualize similarity (pairwise distance) across data points in cartesian space', 
				'principal coordinates analysis', 
				'input pair-difference matrix & output coordinate matrix minimizing strain loss function'
			],
			'assumptions': ['euclidean distance'],
			'insights': ["coordinate matrix x can be derived from b = x * x' with eigenvalue decomposition, and b can be computed from proximity matrix d with double centering"],
			'steps': [
				'find squared proximity matrix d',
				'apply double centering to compute b, using centering matrix J, with n as number of objects',
				'determine m largest eigenvalues & their eigenvectors of b, with m as number of target dimensions',
				'x is eigenvector matrix multiplied by square root of diagonal matrix of eigenvalues of b'
			],
			'variants': {
				'general': {
					'metricMDS': 'cost function is residual sum of squares'
				}
			}
		},
		'svm': {
			'definitions': [
				'non-probabilistic binary linear classifier',
				'assigns new data to one category or the other, given labeled data with two label categories',
				'maximizes difference between example data points of different categories, predicting category by side of gap'
			]
			'variants': {
				'permutation': {
					'probabilistic': 'platt_scaling'
				},
				'unsupervised': {
					'clustering': 'support_vector_clustering'
				}

			},
			'types': [
				'supervised'
			],
			'intents': [
				'classification': ['linear classification', 'nonlinear classification with kernel trick'],
				'regression'
			],
			'insights': [

			],
			'methods': {
				'finding_svm_classifier': {
					'descent': ['sub-gradient', 'coordinate']
				}
			}
		}
	}

	alternatives = {}
	alternatives['cov_adjustments'] = ['ANCOVA', 'random_effects'] # analysis of covariance
	alternatives['dependent_mean_equality_across_independent_category_without_continuous_covariates'] = ['ANOVA/regression', 'ANCOVA']

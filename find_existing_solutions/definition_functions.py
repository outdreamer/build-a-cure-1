from utils import *

def get_function_metadata(fdef, delimiter):
	function_items = fdef.split(delimiter)
	if len(function_items) > 0:
		function = function_items[1].replace('):', '').split('(')
		if len(function) > 1:
			print('function', function)
			function_name = function[0]
			syntax_function_name = ''.join(['def ', function_name, '('])
			function_params = function[1].replace(' ','').split(',')
			function_code = []
			start_adding = False
			function_path = ''.join([function_items[0], '.py'])
			if os.path.exists(function_path):
				code = get_data(function_path)
				if code:
					for line in code.split('\n'):
						if syntax_function_name in line:
							start_adding = True
						else:
							if start_adding:
								if 'def ' in line:
									start_adding = False
								else:
									''' to do: add filter for comments '''
									function_code.append(line)
				function_def = {'name': function_name, 'params': function_params, 'code': function_code}
				return function_def
	return False

def get_problem_metadata(problem_def_path):
	print('function::get_problem_metadata')
	'''
		1. Identify problem metadata
			- problem type
			- default/original problem type (position on problem type network)
			- adjacent problem types
			- component problem types
			- related problem types
			- combination problem types

			- problem structure
				- space (output dimensions to measure solutions)
				- structure (gap/limit/force/conflict/intersection)

			- problem attributes
				- interfaces (dimensions that frame or highlight variable value change rules)
	'''
	''' to do: add metadata id functions '''
	problem_metadata_path = 'workflow1_problem_metadata.json'
	problem_metadata = get_data(problem_metadata_path)
	if problem_metadata:
		return problem_metadata
	problem_def = get_data(problem_def_path)
	if problem_def:
		return problem_def
	return False
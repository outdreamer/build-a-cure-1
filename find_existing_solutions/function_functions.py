from utils import *
	
def get_function_prerequisites(function_name, function_order):
	'''
		function_order = {
			"find": "process",
			"process": "balance",
		}
		to do: add iteration for additional degrees of prerequisites
	'''
	prerequisites = []
	if function_order:
		for key, value in function_order.items():
			if function_name == value:
				''' if its in the value, that means theres a predecessor '''
				if key in function_order.values():
					for k, v in function_order.items():
						if v == key:
							prerequisites.append(k)
		if len(prerequisites) > 0:
			return prerequisites
	return False

def get_functions_for_object_combination(solution_object, solution_functions):
	print('solution_functions', solution_functions)
	object_functions = []
	solution_object = solution_object if type(solution_object) == str else ' '.join(solution_object) 
	function_order = get_data('function_order.json')
	if function_order:
		if solution_functions:
			for function in solution_functions:
				new_relationship = ' '.join([function, solution_object])
				prereqs = get_function_prerequisites(function, function_order)
				if prereqs:
					for pr in prereqs:
						replaced_relationship = new_relationship.replace(function, pr)
						object_functions.append(replaced_relationship)
				object_functions.append(new_relationship)
		else:
			object_functions.append(solution_object)	
		if len(object_functions) > 0:
			return object_functions
	return False
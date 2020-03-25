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

from definition_functions import get_function_metadata
from utils import *

def find_type(problem_object, solution_objects):
	''' solution_objects = ['info', 'asymmetry'], problem_object = 'incentive', return solution_object 'info'

	- to do:
		- this assumes the solution object is the type/more abstract than the problem object

	- the optimal implementation to match_type would:
		- derive 'reason' from 'incentive',
		- get 'reward' from 'reason', 
		- then match the context of reward to optimization language or markets, 
			both of which are frequently modeled using info about the systems, like in agent-based algorithms or game theory
		- then match the context of the solution_object 'info' based on this connection

	- or it'd rule out the other solution objects like 'asymmetry' in this example, which isnt relevant on its own without the info_asymmetry term, 
		although info_asymmetry matches the 'incentive' problem_object, because:
			- there is implied but not explicit info that the incentivized behavior is good (incentivized behaviors are sometimes just defaults or emerging incentives that are unplanned)
			- there is implied but not explicit info about costs/side effects of the incentivized behavior (incentives can come with costs like lack of variation)
		but the 'info' object is a closer match, and we're looking for 1-1 relationships to reduce complexity

	- other routes to identify 'incentive' as info:
		- lookup definition of info (standard definition: 'message received an understood', or system schema definition, which is 'structure')
		- derive or look up that info object has core operations (derive, apply, find) 
			from common relationships ('find information' is a common phrase) 
			or definition 'structure has common operations like find, match, fill'
		- classify functions that serve each operation (get is a function type used for find functionality)
		- query for get/find functions
		- api functions could retrieve info objects (query codebase for functions that get objects & check for an incentive object or attribute, indicating this is a type of information
	'''

	''' this is a specific solution given that we have a system object 'info' defined and find_* functions for various info types, as a placeholder for codebase queries '''

	codebase_functions = get_codebase_functions()
	if codebase_functions:
		print('get_codebase_functions', codebase_functions)
		object_defs = get_data('object_schema.json')
		if object_defs:
			print('object_defs', object_defs)
			for solution_object in solution_objects:
				for key, values in object_defs.items():
					''' key = 'interface_objects' '''
					for k, v in values.items():
						if k == solution_object:
							print('solution_object', solution_object)
							solution_def = object_defs[key][solution_object]
							print('solution_def', solution_def)
							system_definition = solution_def['definitions']['system'] if 'definitions' in solution_def and 'system' in solution_def['definitions'] else None
							if 'functions' in solution_def:
								for abstract_operation, specific_operations in solution_def['functions'].items():
									for function in codebase_functions: # globals():
										for item in ['name', 'params', 'code']:
											if item in function:
												if abstract_operation in function[item] and problem_object in function[item]:
													return solution_object
												for specific_operation in specific_operations:
													if specific_operation in function[item]:
														if problem_object in function[item]:
															''' this problem_object 'incentive' is a type of system object 'info' '''
															return solution_object
	return False

	solution_defs = Word(solution_object).definitions
	print('solution_defs', solution_object, solution_defs)
	if solution_defs:
		matching_problem_objects = {}
		problem_defs = Word(problem_object).definitions
		''' add filtering of words in defs '''
		if problem_defs:
			print('problem_defs', problem_object, problem_defs)
			problem_definition_string = remove_stopwords(' '.join(problem_defs))
			''' 'info' in 'incentive' definition '''
			if solution_object in problem_definition_string:
				return solution_object
			solution_definition_string = remove_stopwords(' '.join(solution_defs))
			''' 'incentive' in 'info' definition '''
			if problem_object in solution_definition_string:
				return solution_object
			matching_problem_words = 0
			for solution_def in solution_defs:
				for solution_word in solution_def.split(' '):
					''' 'info' definition word in 'incentive' definition '''
					if solution_word in problem_definition_string:
						matching_problem_words += 1
			if (matching_problem_words/solution_definition_string.count(' ')) > 0.5:
				return solution_object
			''' 'info' synonyms similar to 'incentive' synonyms '''
			problem_synsets = Word(problem_object).get_synsets(pos=NOUN)
			solution_synsets = Word(solution_object).get_synsets(pos=NOUN)
			print('problem_synsets', problem_synsets)
			print('solution_synsets', solution_synsets)
			matching_synsets = 0
			for ps in problem_synsets:
				print('problem synsets', dir(ps))
				ps = ps.name.split('.')[-1]
				if ps in solution_synsets:
					matching_synsets += 1
			if matching_synsets/len(solution_synsets) > 0.5:
				return solution_object
	return False

def remove_stopwords(definition):
	return definition

def get_codebase_functions():
	import subprocess
	cwd = os.getcwd()
	output_name = '/'.join([cwd, 'code_function_names.txt'])
	if os.path.exists(output_name):
		function_defs = get_data(output_name)
		if function_defs:
			return function_defs
	cmd = [f"""grep -r 'def ' {cwd} --include='*.py' >> {output_name}"""]
	output = subprocess.check_output(cmd,shell=True)
	''' /Users/jjezewski/Documents/build_a_cure/find_existing_solutions/get_vars.py:def get_partial_match(av, word, match_type): '''
	if os.path.exists(output_name):
		function_defs = get_data(output_name)
		if function_defs:
			print('type defs', type(function_defs))
			if len(function_defs) > 0:
				removed = True # remove_file(output_name) remove if you need to re-generate every time
				if removed:
					print('removed', removed)
					new_defs = []
					for fdef in function_defs.split('\n'):
						print('fdef', fdef)
						delimiter = '.py:def '
						if delimiter in fdef:
							''' validate that this is a function definition '''
							function_metadata = get_function_metadata(fdef, delimiter)
							if function_metadata:
								new_defs.append(function_metadata)
					if len(new_defs) > 0:
						return new_defs
	return False

from type_functions import *

def get_object_map(problem_metadata, solution_metadata):
	print('function::get_object_map')
	# solution_objects = ['info', 'asymmetry', 'info_asymmetry']
	object_map = {}
	problem_objects = problem_metadata['objects']
	for problem_object in problem_objects:
		matched_solution_object = find_matching_object_in_problem_space(problem_metadata, problem_object, solution_metadata)
		if matched_solution_object:
			object_map[problem_object] = matched_solution_object
	problem_functions = problem_metadata['functions']
	for problem_function in problem_functions:
		matched_solution_function = find_matching_object_in_problem_space(problem_metadata, problem_function, solution_metadata)
		if matched_solution_function:
			object_map[problem_function] = matched_solution_function
	print('object_map', object_map)
	'''
		- target output for info-persuasion object map (object_map):
			'info': [
				'incentive/intent to change positions',
				'incentives/inefficiencies preventing position change',
				'benefits/costs of position change'
			],
			'info_asymmetry': [
				'subject does not have info of reasons to change position'
			],
			'balance': [
				'distribute reasons to change to subject', # if lack of reasons is the problem
				'distribute info to enable access of change position functions to subject so subject finds it easier to move', # if lack of function accessibility is the problem
				'align reason to change & reason to stay so subject identifies misclassification error', # if misclassification of reason is the problem
			]
	'''
	return object_map

def find_matching_object_in_problem_space(problem_metadata, problem_object, solution_metadata):
	''' for a solution_object like 'info', find the corresponding object in the problem like 'incentives/reasons/intents/efficiencies/cost/benefit' 
		- to do: 
			- add solution_function support
			- add type checking support, either to problem index or add a derivation function
			- add check if problem attribute is a required input to the solution object, increasing likelihood that objects match
	'''
	solution_object = find_type(problem_object, solution_metadata['objects'])
	if solution_object:
		return solution_object
	matched_problem_object = {}
	if matched_problem_object:
		new_problem_solution_map = makes_sense(problem_metadata, problem_object, matched_problem_object, solution_metadata['objects'])
		if new_problem_solution_map:
			return new_problem_solution_map
	return False

def makes_sense(problem_metadata, problem_object, matched_problem_object, solution_objects):
	print('function::makes_sense')
	''' 
		this is basically a system structure-fitting function, with logically consistency/validity checks
		- if its logically consistent with known logical rules, 
			- it matches known logical rules using known connections between them (inputs/outputs/paths)
			- it has no missing components or gaps in logic
		now that youve verified these objects match in some way, you need to check if mapping this solution object & this problem object makes sense with the problem definition
		check that mapping 'reason' to 'info' makes sense 

		- this function requires that the system being checked against is already formatted by its metadata (object/function/attributes)
		- we're looking for the first violation of problem space (problem_metadata) logic rules that the solution_object 
			(object like 'incentive', attribute like 'relevance or function like 'combine') 
			has when applied to the problem_metadata system according to its matching problem object

		- in addition to the system object rules, specific rules of problem space logic can apply
			- the success metric of the problem needs to be improved by the solution, if the solution makes sense when applied to that problem space
	'''
	for solution_object in solution_objects:
		logical_rules = get_data('system_logic_rules.json')
		if logical_rules:
			new_problem_solution_map = {}
			attributes_to_check = ['type']
			sense = 0
			for attribute in matched_problem_object[problem_object]:
				if attribute in problem_metadata:
					''' standard definition validation '''
					if solution_object in problem_metadata[attribute]:
						''' is 'info' included in problem['type'] list? '''
						sense += 1
					if solution_object in stringify_metadata(problem_metadata):
						''' is 'reason' in 'info' solution object metadata? '''
						sense += 1
					if problem_object in stringify_metadata(solution_metadata):
						''' is 'reason' in 'info' solution object metadata? '''
						sense += 1
			if sense > 0:
				new_problem_solution_map[problem_object] = matched_problem_object[o]
			if new_problem_solution_map:
				return new_problem_solution_map 
	return False
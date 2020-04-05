import itertools
from fit_functions import get_relationship_between_objects
from map_functions import get_object_map
from filter_functions import get_relevant_path, get_relevance_filters
from definition_functions import get_object_metadata
from get_functions import get_solution_type
from derive_functions import get_functions_for_object_combination

def apply_solution_to_problem(problem_metadata, abstract_solution_type):
	print('function::apply_solution_to_problem', abstract_solution_type)
	''' 1b/4. apply solution for converted problem type
		to do: 
		- decide if you want to return multiple solutions if there are any
		- make sure solution step lists are handled differently than abstract solution types 
		- filter solution steps, removing repeated combinations of the same step
	'''
	solution_metadata = get_object_metadata(abstract_solution_type, 'solution')
	solution_type = get_solution_type(abstract_solution_type)
	if solution_type == 'type':
		# this is a solution type, not a specific solution
		solution_steps = get_steps_from_solution_type(abstract_solution_type, solution_metadata)		
		'''
			abstract_solution_type = 'balance_info_asymmetry'
			solution = ['find info', 'find info asymmetry', 'balance info']
			problem_steps = {
				'find_info': 'find_incentives_to_change_position'
			}
		'''
		if solution_steps:
			print('solution steps from type', abstract_solution_type, '\n', solution_steps)
			solution_metadata['steps'] = solution_steps
			problem_steps = convert_solution_steps_to_problem_steps(problem_metadata, solution_metadata)
			''' replaced 'asymmetry' with 'interactions' 
				should replace 'info' with 'incentives'
				then should add 'to change position'
			'''
			print('\nproblem_steps', problem_steps, '\n')
			if problem_steps:
				solved_problem = apply_solution(problem_metadata, problem_steps)
				if solved_problem:
					return solved_problem
	return False

def get_steps_from_solution_type(abstract_solution_type, solution_metadata):
	'''
	solution_metadata = {
		'objects': ['info', 'asymmetry']
		'function': 'balance', 
		'steps': [
			'find_info',
			'find_info_asymmetry',
			'balance_info'
		]
	}
	'''
	'''
	abstract_solution_type = 'balance_info_asymmetry' 
	1. derive solution type steps with get_object_metadata():
		solution_steps = ["find info", "find info_asymmetry", "balance info"]

	to do: 
		- this should converte balance_info_asymmetry to list above, currently stored in insights.json under solutions 
		- if balance isn't included in solution_type, its derivable from core object set, which is 'info' and 'imbalance'
			combined_relationships = [balance info, balance info_asymmetry, balance asymmetry]
			now filter this list, 
				- removing any that are too abstract to have a clear structural meaning or other metrics of relevance
				- identifying where a relationship could use further structuring
				- identifying where a relationship doesnt have its inputs covered (balance info requires first finding info)
			# assumption = 'info exists', 'info is known' for step 'balance info'
			# info exists isnt an assumption likely to be calculatable, but info is known is calculatable
	'''
	print('solution_metadata', solution_metadata)
	all_relationships = []
	for solution_object in solution_metadata['objects']:
		object_functions = get_functions_for_object_combination(solution_object, solution_metadata['functions'])
		if object_functions:
			all_relationships.extend(object_functions)
	if len(solution_metadata['objects']) > 1:
		object_combinations = itertools.permutations(solution_metadata['objects'], 2)
		for object_combination in object_combinations:
			if solution_metadata['functions']:
				object_functions = get_functions_for_object_combination(object_combination, solution_metadata['functions'])
				if object_functions:
					all_relationships.extend(object_functions)
			else:
				all_relationships.append(object_combination)			
	original_relationship = abstract_solution_type.replace('_', ' ') if type(abstract_solution_type) == str else ' '.join(abstract_solution_type)
	print('original_relationship', original_relationship)
	if original_relationship in all_relationships:
		all_relationships.remove(original_relationship)
	if len(all_relationships) > 0:
		return all_relationships
	return False

def convert_solution_steps_to_problem_steps(problem_metadata, solution_metadata):
	print('function::convert_solution_steps_to_problem_steps', solution_metadata)
	'''
	2. then find map between solution & problem objects with get_object_map():
		object_map['info'] = {
			'reasons', # list of attributes they have in common or deemed relevant/important
			'incentives',
			'efficiencies'
		}
	'''
	print('problem objects', problem_metadata)
	if 'objects' in problem_metadata and 'objects' in solution_metadata:
		object_map = get_object_map(problem_metadata, solution_metadata)
		print('object_map', object_map)
		if object_map:
			problem_steps = []
			for solution_step in solution_metadata['steps']:
				'''
				3. then apply solution_type_steps to object_map to get abstract_problem_steps:
					object_map = {'info': 'incentives'}
					abstract_problem_steps = {
						'find_info': [
							'find reasons/efficiencies/incentives/intents'
						]
					}
					abstract_problem_steps = {
						'solution_type_step': [
							'abstract_problem_step'
						]
					}
				'''
				print('solution_step', solution_step)
				abstract_problem_step = convert_solution_to_problem_step(object_map, solution_step)
				if abstract_problem_step:
					specific_problem_step = get_specific_solution(abstract_problem_step, problem_metadata)
					if specific_problem_step:
						print('specific_problem_step', specific_problem_step)
						problem_steps.append(specific_problem_step)
			if len(problem_steps) > 0:
				return problem_steps
	return False

def convert_solution_to_problem_step(object_map, solution_step):
	''' fix processing '''
	problem_step = []
	for solution_word in solution_step.split(' '):
		for key, value in object_map.items():
			if solution_word in value:
				problem_step.append(key)
			else:
				if solution_word not in problem_step:
					problem_step.append(solution_word)
	if len(problem_step) > 0:
		return ' '.join(problem_step)
	return solution_step

def get_specific_solution(abstract_solution, problem_metadata):
	print('function::get_specific_solution')
	''' 
		this is an example of the 'apply' function, 
		where we are applying the abstract_solution to the problem_metadata object 
		(inject abstract_solution to problem_metadata object) 

	'''
	'''
		to do: decide if you want to return interim version in dict structure 
		4. then apply modifiers to make abstract_problem_steps relevant to problem with get_specific_solution():
			relevant_problem_step = 'find reasons/efficiencies/incentives/intents to change position'

		- with matching problem objects, apply solution_type to get solution
			- the solution type 'balance the info asymmetry' applied to a problem like 'persuasion' translates to the solution:
				# find info
					- find reasons to change position
					- find reasons to stay in current position
				# find info asymmetry
					- subject doesnt have info (reasons, incentives) to call change_position function
				# balance info
					- map some reason to change (safety) with some reason to stay (safety)
	'''
	'''
	solution_steps = ['find_info', 'find_info_asymmetry', 'balance_info']
	object_map = {'info': ['incentives', 'efficiencies', 'intents']}
	specific_steps = {
		'find_info': 'find_incentives_to_change_position'
	}
	'''
	''' convert abstract_solution = 'find_incentives' into modified relevant solution like 'find incentives to change position', 
		which is highly relevant to the condensed problem definition ("change_position_of_subject")
		- by adding modifiers, we are answering the question: 
			- how is 'find_incentive' related to the problem of 'persuasion' (change position of subject)?
	'''
	''' 
		to do: 
			- add formatting for modifiers of a certain type, like:
				"problem_object [relationship_to_function "input" ] required_problem_function"
			- add check for relevance of modifying attribute/object in relevant_problem_objects

			- generate relevant modifiers/functions/filters for a particular abstract solution step

				- this means generating a relevance filter ['required', 'function'] to find modifiers for an abstract solution step like 'find_incentive' 
					(which was converted to relevant to problem from 'find_info')

				- how would you know that 'required', and 'function' are the right combination to apply as a relevance filter, to find modifiers for 'find_incentive'?

					- 'incentive' is in the problem_metadata['functions'] dict 
						- specifically its under the input.required dict of the change_position function

					- we know that change_position is important bc its necessary for the solution success 
						(its implied in the problem definition statement, the subject needs to change their position & the persuader needs to persuade them to do it)
					
					- why are we applying 'find_incentive'? 
						to input that incentive to the 'change_position' function, which requires 'incentives' as an input

					- why are we applying 'change_position'?
						- to solve the problem 

					- given required functions to solve the problem, metadata of those functions (function_name) may be useful in modifying an abstract solution 
						which includes other metadata of that function (incentive)

				- logical flow:
					- incentive is an input to the change_position function of the 'persuasion' problem, and 'change_position' is a required function for solving the problem 
					- an input of a function increases possibility of calling that function, a required input even more so
					- this indicates why we would include the function_name ('change_position') in our modified/relevant version of the solution_step (find_info/find_incentive):
						- 'incentive to change position' is required/important info to solve the problem
						- we want to add info that increases the relevance of the solution step, 
							so we dont forget why we are implementing a particular solution step, 
							and so the impact of that step is clearer/more measurable

	problem_metadata = {
		"functions": {
			"interactions": {
				"change_position": {
					"input": {
						"required": ["incentive", "efficiency", "intent"]
					}
				}
			}
		}
	}
	given that relevance_filter = ["required", "functions"], 
		if the abstract solution keyword is in the required function inputs,
			we want to return function name "change_position" rather than function_type ("interactions") 
			bc the name is more specific & we're trying to add specificity

	- to get intent of a problem_step, find required inputs of functions

	'''
	relevant_solutions = []
	relevance_intents = ['specificity', 'intent']
	relevance_filters = get_relevance_filters(relevance_intents, problem_metadata) # getting filters for a certain type of modification
	if relevance_filters:
		for relevance_filter in relevance_filters:
			''' get relevant items from flattened & order in relevant_path '''
			relevant_path, specific_attribute_values = get_relevant_path(problem_metadata, relevance_filters)
			if relevant_path and specific_attribute_values:
				print('relevant_path', relevant_path)
				if len(relevant_path) > 0:
					''' find the adjacent object name for the target object (required function inputs) which should be at the end of this list '''
					for item in relevance_filter:
						if item in relevant_path:
							relevant_path.remove(item)
					''' to do: given that the object of interest is a function (highest level key of problem_metadata), 
						we should be able to derive that you wouldnt want to use the function type name '''
					# relevant_path is now ['interactions', 'change_position', 'input']
					''' remove object types from relevant_path, because we're trying to isolate a specific name 
						that is most adjacent to object of interest (required function inputs) '''
					for item in relevant_path:
						item_object = get_objects_in_string(item)
						if item_object:
							if item == item_object or item in item_object:
								if item in relevant_path:
									relevant_path.remove(item)
					# relevant_path is now ['interactions', 'change_position']
					''' given that we know the target is at the end of the list, 
					the most adjacent object to the target is the last item in the list with objects & relevance filters removed '''
					if len(relevant_path) > 0:
						abstract_solution_words = abstract_solution.split('_')
						for abstract_solution_word in abstract_solution_words: # [find, incentive]
							if abstract_solution_word in specific_attribute_values:
								'''
								if 'incentive' in ["incentive", "efficiency", "intent"],
									then we found a word from the abstract solution "incentive" 
									in the problem_metadata specific_attribute_values (required inputs to change_position function), 
									fulfilling the relevance_filter ["required", "functions"] for ['specificity', 'intent'] with specific intents
								'''
								''' to do: 
									- save object_type items for this call to get_relationship_between_objects()
									- given that this is an input, the relationship function between an input and a function is 'in order to', or briefly 'to'
								'''
								join_keyword = get_relationship_between_objects('input', 'function') 
								# the input's intent is to apply the function, so 'incentive' is to 'change_position', so return 'to'
								relevant_solution = '_'.join([abstract_solution_words, join_keyword, relevant_path[-1]])
								''' relevant_solution = 'find_incentives_to_change_position" '''
								relevant_solutions.append(relevant_solution)
	if len(relevant_solutions) > 0:
		return relevant_solutions
	return abstract_solution
	''' 
		alternate methods to find modifiers to make this abstract solution more relevant to the problem:
		- apply relevance_filter [function, required] to problem_metadata 
			to look for modifiers like function_name 
			to attach to abstract_solution containing a required function input
		- query for metadata as you hit each object if its an object type (function, input are object types)
			function_metadata = ["input"]
		- remove non-adjacent name keys that are clearly not object types 
			(remove "intersections", which is a function type name and not in the relevance filter, and not adjacent above the nearest object type (input)
		- store position of object types in problem_metadata['functions'] and apply that to fetch required inputs & check if abstract solution matches required inputs
			type_position = 1
			name_position = 2
			input_position = 3
			required_position = 4
	'''

def apply_solution(problem_metadata, solution):
	print('function::apply_solution', solution)
	'''
		solution = relevant_steps = {
			'find_info': 'find_incentives_to_change_position'
		}
	'''
	for relevant_problem_step in solution:
		new_problem_metadata = apply_step(problem_metadata, relevant_problem_step)
		if new_problem_metadata:
			problem_metadata = new_problem_metadata
	''' problem_metadata['state'] should be changed at this point '''
	if problem_metadata:
		return problem_metadata
	return False

def apply_step(problem_metadata, problem_step):
	''' this function applies a step like 'balance incentives' to a problem definition,
		removing all remaining ambiguities by pulling specific functions for each abstract function, specific objects for each type, etc
		for example, 'balance incentives' would rearrange incentives in one of the balancing implementations (evenly distribute, remove from all positions, etc)
	''' 
	return False


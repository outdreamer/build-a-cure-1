import nltk, os, json, itertools
from nltk import pos_tag, word_tokenize
from textblob import TextBlob, Sentence, Word, WordList
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset
from get_conceptual_objects import *
from get_structural_objects import *

''' OBJECT DEFINITION '''

def get_problem_metadata(problem_def):
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
	return problem_def

def condense_problem_statement(problem_metadata):
	print('function::condense_problem_statement')
	'''
		to do:
			- we want to output 'change_position_of_subject' from the problem statement:
				"statement": "move other agent to new position (despite dis-incentives like inefficiencies & costs)"

			- we also want to include the aspect 'voluntary' by emphasizing that the move should be done by the subject, not the persuader: 
				- the persuader should not exert force to persuade, 
				 	- otherwise the definition of 'persuade' does not apply, which is:
				 		- 'give subject a reason to move to target position that persuader has assigned to them as an optimal move',
				 	- and does not allow for the use of force, 
				 		- since the persuader is specifically applying the 'giving' function, not applying just any function
	'''
	condensed_problem_statement = 'change_position_of_subject'
	if 'problem_definition' in problem_metadata:
		if 'statement' in problem_metadata['problem_definition']:
			if condensed_problem_statement:
					return condensed_problem_statement
	return False

'''
	Workflow 1a: Transform into combination of solved problems
	Workflow 1b: Transform into an interface problem type (problem type that can frame all problems, like route optimization, a market trade problem, an inefficiency, or a filtering problem)
		This version skips the problem type analysis & just fetches a solution for common problem types with which other problems can be framed
'''

''' to do:
	- finish apply_solutions
	- abstract method of mapping problem-solution object
	- write insight-application function 
	- then do convert_to_solved_problem
'''

''' the problem type for this example: persuasion (make an argument that changes a behavior metric (like direction) '''

'''
{
	"problem_space": {
		"dimensions": [
			"position",
			"system_impact",
			"efficiency"
		]
	},
	"problem_definition": {
		"statement": "move other agent to new position (despite dis-incentives like inefficiencies & costs)"
	},
	"problem_metadata": {
		"types": {
			"default": "connecting points to form an argument",
			# related problems to be filled in with insights['related_problems'] of insights, since insights are relationships between objects
			"related": [], 
			"component": ["make point"],
			# adjacent problems are low-degree transforms away from this problem 
			"adjacent": ["forming a cohesive system"]
		},
		"dependencies": {
			"variables": ["subject_position"],
			"objects": ["persuader agent"],
			"assumptions": ["source and target position are different"],
			"requirements": ["info about the subject's resources, incentives, intents, and functions"],
			"inputs": ["subject"],
			"outputs": ["path_from_source_to_target_position"]
		},
		"functions": {
			"intents": ["connect"],
			"generation_function": [
				"convert conclusions to positions", # to generate the 'persuasion' problem
				"identify optimal position", # identify target
				"differentiate optimal & source position", # check that source & target positions arent the same
				# there has to be a reason why persuasion is difficult, or they'd already be moving to the optimal position, rather than stabilizing in the current position
				"identify incentives to stay in current position",
				# if it was easy to move to the other position, they would be able to do it with low-degree combinations of accessible/core functions
				"identify inability of accessible functions to move to target position"
			],
			"interaction_functions": ["change_position"]
		},
		"cause": {}	
	}
}
'''

def solve_problem_with_problem_type_conversion(problem_metadata):
	print('function::solve_problem_with_problem_type_conversion')

	converted_problem = None
	if problem_metadata:
		''' 1a. get insights, including any related solutions '''
		problem_metadata['insights'] = get_insights(problem_metadata)
		'''
		insights = {
			"insights": [
				"persuasion is successful when benefits are clear",
				"an example efficiency is: removing unnecessary middlemen"
			],
			"solutions": [
				["find_info", "find_info_asymmetry", "balance_info"],
				["list benefits", "find efficiencies", "apply efficiencies", "list reduced costs"]
			],
			"related_problems": [
				"identify optimal path to target", # persuasion problem super-type
				"differentiating objects (cost/benefits)" # related problem of this problem's insights
			]
		}
		'''
		''' 1b. try solutions identified as related to this problem or problem type before converting '''
		if 'solutions' in problem_metadata['insights']:
			''' found insights about solutions for this problem type '''
			for s in problem_metadata['insights']['solutions']:
				solved_problem = apply_solution_to_problem(problem_metadata, s)
				if solved_problem:
					return solved_problem 

		''' if solutions of this problem type didnt work, try solutions of related problems '''
		if 'related_problems' in problem_metadata['insights']:
			for p in problem_metadata['insights']['related_problems']:
				converted_problem = convert_to_solved_problem(problem_metadata, p)

		''' if there are no related problem types/related problems, convert to an interface problem type '''
		if converted_problem is None:
			converted_problem = convert_to_interface_problem(problem_metadata)

		if converted_problem:
			''' apply solutions for converted problem '''
			''' get solutions from insights for the converted problem '''
			converted_problem['insights'] = get_insights(converted_problem)
			if 'solutions' in converted_problem['insights']:
				''' found insights about solutions for related problem type '''
				for rps in converted_problem['insights']['solutions']:
					solved_converted_problem = apply_solution_to_problem(converted_problem, rps)
					if solved_converted_problem:
						solved_original_problem = convert_solved_problem_to_problem_type(solved_converted_problem, problem_metadata)
						if solved_original_problem:
							solved = test_solution(problem_metadata, solved_original_problem)
							return solved
	return False

''' APPLY DEFINITION '''

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
	return False

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
	print('problem objects', problem_metadata['problem_metadata']['dependencies'])
	if 'objects' in problem_metadata['problem_metadata']['dependencies'] and 'objects' in solution_metadata:
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
				abstract_problem_step = get_problem_solution_step(object_map, solution_step)
				relevant_step = get_specific_step(solution_step, abstract_problem_step, problem_metadata)
				if relevant_step:
					problem_steps.append(relevant_step)
			if len(problem_steps) > 0:
				return problem_steps
	return False

def get_problem_solution_step(object_map, solution_step):
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

def get_specific_step(solution_step, abstract_problem_step, problem_metadata):
	'''
		to do: decide if you want to return interim version in dict structure 
		4. then apply modifiers to make abstract_problem_steps relevant to problem with get_relevant_solution():
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
	specific_steps = {}
	specific_problem_step = get_relevant_solution(abstract_problem_step, problem_metadata)
	print('specific_problem_step', specific_problem_step)
	if specific_problem_step:
		specific_steps[solution_step] = specific_problem_step
	'''
	solution_steps = ['find_info', 'find_info_asymmetry', 'balance_info']
	object_map = {'info': ['incentives', 'efficiencies', 'intents']}
	specific_steps = {
		'find_info': 'find_incentives_to_change_position'
	}
	'''
	if specific_steps:
		return specific_steps
	return False


def get_relevant_solution(abstract_solution, problem_metadata):
	print('function::get_relevant_solution')

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
		"problem_metadata": {
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
	}
	given that relevance_filter = ["required", "function"], 
		if the abstract solution keyword is in the required function inputs,
			we want to return function name "change_position"
	'''
	abstract_solution_words = abstract_solution.split('_')
	relevance_filter = ['required', 'functions']
	other_filters = relevance_filter
	''' get relevant items from flattened & order in relevant_list '''
	relevant_list = []
	last_item_values = []
	for key, value in problem_metadata['problem_metadata'].items():
		if key in relevance_filter: # functions or whichever filtering key comes first in dict
			other_filters.remove(key)
			if type(value) == dict:
				for function_type, functions in value.items():
					if type(functions) == dict:
						flattened_sub_dict = flatten_dict(functions)
						for rf in other_filters:
							if rf in flattened_sub_dict.keys() or rf in flattened_sub_dict.values():
								''' check if dict can cast to str or dump json, check that this sub-dict is worth pursuing '''
								for function_name, function_metadata in functions.items():
									if type(function_metadata) == dict:
										flattened_function = flatten_dict(function_metadata)
										if flattened_function:
											if rf in flattened_function:
												for attribute, attribute_metadata in function_metadata.items():
													if type(attribute_metadata) == dict:
														for attribute_name, attribute_values in attribute_metadata.items():
															if attribute_name == rf: # required
																if type(attribute_values) == list:
																	relevant_list = [key, function_type, function_name, attribute, attribute_name]
																	last_item_values = attribute_values
	''' relevant_list = ['functions', 'interactions', 'change_position', 'input', 'required'] '''
	print('relevant_list', relevant_list)
	relevant_solution = None
	if len(relevant_list) > 0:
		''' find the adjacent object name for the target object (required function inputs) which should be at the end of this list '''
		for item in relevance_filter:
			if item in relevant_list:
				relevant_list.remove(item)
		''' to do: given that the object of interest is a function (highest level key of problem_metadata), we should be able to derive that you wouldnt want to use the function type name '''
		# relevant_list is now ['interactions', 'change_position', 'input']
		''' remove object types from relevant_list, because we're trying to isolate a specific name that is most adjacent to object of interest (required function inputs) '''
		for item in relevant_list:
			item_object = get_objects_in_string(item)
			if item_object:
				if item == item_object or item in item_object:
					if item in relevant_list:
						relevant_list.remove(item)
		# relevant_list is now ['interactions', 'change_position']
		''' given that we know the target is at the end of the list, the most adjacent object to the target is the last item in the list with objects & relevance filters removed '''
		adjacent_name = relevant_list[-1] if len(relevant_list) > 0 else None
		for abstract_solution_word in abstract_solution_words: # [find, incentive]
			if abstract_solution_word in last_item_values:
				'''
				if 'incentive' in ["incentive", "efficiency", "intent"],
					then we found a word from the abstract solution "incentive" 
					in the problem_metadata last_item_values (required inputs to change_position function), 
					therefore fulfilling the relevance_filter ["required", "functions"]
				'''
				''' to do: 
					- save object_type items for this call to get_relationship_between_objects()
					- given that this is an input, the relationship function between an input and a function is 'in order to', or briefly 'to'
				'''
				join_keyword = get_relationship_between_objects('input', 'function')
				if adjacent_name is not None:
					relevant_solution = '_'.join([abstract_solution_words, join_keyword, adjacent_name])
					''' relevant_solution = 'find_incentives_to_change_position" '''
					print('relevant_solution', relevant_solution)
					return relevant_solution
				return abstract_solution_words
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
	return abstract_solution

def get_relationship_between_objects(source, target):
	print('function::get_relationship_between_objects')
	join_keyword = 'in order to'
	brief_join_keyword = get_brief_keyword(join_keyword)
	if brief_join_keyword:
		return brief_join_keyword
	return join_keyword

def get_brief_keyword(keyword):
	print('function::get_brief_keyword')
	return 'to'

def flatten_dict(problem_metadata):
	flattened = {}
	for key, values in problem_metadata.items():
		flattened = iterate_dict(key, values, flattened)
	if flattened:
		return flattened
	return False

def iterate_dict(key, values, flattened):
	if type(values) == dict:
		# print('dict values', key, values.keys())
		for k, v in values.items():
			if type(v) != dict:
				flattened[k] = v
			else:
				flattened = iterate_dict(k, v, flattened)
	else:
		''' to do: add support for nested items other than dicts '''
		# print('list values', key)
		flattened[key] = values
	return flattened

def get_object_map(problem_metadata, solution_metadata):
	print('function::get_object_map')
	# solution_objects = ['info', 'asymmetry', 'info_asymmetry']
	object_map = {}
	problem_objects = problem_metadata['problem_metadata']['dependencies']['objects']
	for problem_object in problem_objects:
		matched_solution_object = find_matching_object_in_problem_space(problem_metadata, problem_object, solution_metadata)
		if matched_solution_object:
			object_map[problem_object] = matched_solution_object
	problem_functions = problem_metadata['problem_metadata']['functions']
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

def find_type(problem_object, solution_objects):
	''' solution_objects = ['info', 'asymmetry'], problem_object = 'incentive'

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
	system_defs = {'info': 'structure'}
	core_operations = {'structure': ['find', 'match', 'apply', 'fill']}
	abstract_specific_function_type_map = {'find': 'get'}
	for solution_object in solution_objects:
		print('solution_object', solution_object, 'problem_object', problem_object)
		if solution_object in system_defs:
			solution_definition = system_defs[solution_object]
			if solution_definition in core_operations:
				for solution_operation in core_operations[solution_definition]:
					# function_type = get_function_type(solution_operation)
					if solution_operation in abstract_specific_function_type_map:
						specific_operation = abstract_specific_function_type_map[solution_operation]
						global_functions = globals()
						for function_name in global_functions:
							if specific_operation in function_name or solution_operation in function_name:
								function_code = 'query'
								function_params = 'object_id'
								''' found a get/find function '''
								if problem_object in function_name or problem_object in function_code or problem_object in function_params:
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
		new_problem_solution_map = makes_sense(problem_metadata, problem_object, matched_problem_object)
		if new_problem_solution_map:
			return new_problem_solution_map
	return False

def makes_sense(problem_metadata, problem_object, matched_problem_object):
	print('function::makes_sense')
	new_problem_solution_map = {}
	''' 
		to do: 
			- convert to structure-fitting function

		now that youve verified these objects match in some way, you need to check if mapping this solution object & this problem object makes sense with the problem definition
		check that mapping 'reason' to 'info' makes sense 
	'''
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

def get_object_metadata(object_name, object_type):
	print('function::get_object_metadata')
	''' object_name can be an abstract solution type string, or a solution step list '''
	object_name = object_name if type(object_name) == str else ' '.join(object_name)
	if object_type == 'solution':
		objects = get_objects_in_string(object_name)
		functions = get_function_in_string(object_name)
		if objects:
			object_metadata = {
				'objects': objects, #'info_asymmetry', 
				'functions': functions, 
				'steps': []
			}
		return object_metadata
	object_type_path = ''.join([object_type, '.json'])
	if os.path.exists(object_type_path):
		object_metadata = get_data(object_type_path)
		if object_metadata:
			return object_metadata
	''' otherwise construct the object '''
	constructed_object = build_object(object_type, object_name)
	if constructed_object:
		return constructed_object
	return False

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
	''' this function applies a step like 'balance incentives' to a problem definition
		for example, 'balance incentives' would rearrange incentives in one of the balancing implementations (evenly distribute, remove from all positions, etc)
	''' 
	return False

def get_solution_type(solution_step):
	print('function::get_solution_type')
	type_words = get_type_words()
	solution_words = ' '.join(solution_step).split(' ')
	solution_word_count = len(set(solution_words))
	union_count = len(type_words.union(solution_words))
	''' if difference ratio between total solution step words & common words with type words is small '''
	if union_count / len(type_words) > 0.5:
		return 'type'
	return 'specific'

def get_type_words():
	print('function::get_type_words')
	''' return list of abstract/interface/structural words '''
	type_words = ['info', 'symmetry']
	return set(type_words)

''' QUERY '''

def get_insights(problem_metadata):
	print('function::get_insights')
	''''
		2. are there insights related to objects in problem metadata?
			- fetch common cross-system insights
			- are there related solution types for the problem, the problem type, the problem components, or related problem types?
	'''
	insights = {'insights': [], 'solutions': []}
	insight_path = 'insights.json'
	insights = get_data(insight_path)
	return insights


''' CONVERSION '''

def convert_to_solved_problem(problem_metadata, target_problem_type):
	print('function::convert_to_solved_problem')
	'''
		3. if related solution types are found for original/related problem types, how to convert between original & solved problem
			- fetch insights on converting problems to a target problem 
			- if no insights found, apply default process:
				- query source & target problem metadata for common attributes & check for a space that could frame their differentiating attributes 
					(the original problem sapce, the target problem space, or an interim/other dimensional space for conversion)
	'''
	solved_problem = {}
	return solved_problem

def convert_to_interface_problem(problem_metadata):
	print('function::convert_to_interface_problem')
	interface_problem = {}
	return interface_problem

def convert_solved_problem_to_problem_type(solved_converted_problem, original_problem_metadata):
	print('function::convert_solved_problem_to_problem_type')
	'''
		5. convert to original problem type
	'''
	solved_original_problem = convert_problem_to_problem_type(solved_converted_problem, original_problem_metadata)
	if solved_original_problem:
		return solved_original_problem
	return False

def convert_problem_to_problem_type(source_problem_type_metadata, target_problem_type_metadata):
	print('function::convert_problem_to_problem_type')
	converted_problem = {}
	if converted_problem:
		return converted_problem
	return False

''' TEST '''

def test_solution(solved_original_problem, problem_metadata):
	print('function::test_solution')
	'''
		6. test if solution actually reduces or solves original problem
	'''
	passed = is_problem_reduced(problem_metadata, solved_original_problem)
	return passed

def is_problem_reduced(problem_metadata, solved_original_problem):
	print('function::is_problem_reduced')
	passed = False
	return passed

''' PROCESSING '''

def build_object(object_type, object_name):
	print('function::build_object')
	''' check for example objects in database '''
	''' check for definition of object type '''
	''' check for examples of related object types '''
	''' check for system containing object reference, to derive object definition '''
	object_instance = {}
	return False

def stringify_metadata(metadata_object):
	print('function::stringify_metadata')
	stringified = '_'.join([metadata_object.values()])
	return stringified

def get_function_list():
	function_list = []
	functions = get_data('functions.json')
	if functions:
		new_functions = flatten_dict(functions)
		for key, values in new_functions.items():
			function_list.extend(values)
		if len(function_list) > 0:
			function_list = set(function_list)
			return function_list
	return False

def get_function_in_string(string):
	print('function::get_function_in_string')
	found_functions = []
	function_list = get_function_list()
	if function_list:
		words = string.replace(' ','_').split('_')
		if len(words) > 0:
			for word in words:
				if word in function_list:
					found_functions.append(word)
	found_functions = set(found_functions)
	if len(found_functions) > 0:
		return found_functions
	return False

def get_objects_in_string(string):
	''' solution_type = 'balance_info_asymmetry' '''
	function_list = get_function_list()
	if function_list:
		words = string.replace(' ', '_').split('_')
		if len(words) > 0:
			objects = []
			for word in words:
				pos_type = get_pos(word)
				if word not in function_list and pos_type != 'verb':
					objects.append(word)
			objects = set(objects)
			if len(objects) > 0:
				return objects
	return False

def get_data(file_path):
	if os.path.exists(file_path):
		objects = None
		with open(file_path, 'r') as f:
			objects = json.load(f)
			f.close()
		if objects:
			return objects
	return False

def get_pos(word):
	tagged = pos_tag(word_tokenize(word))
	for item in tagged:
		if 'V' in item[1]:
			return 'verb'
		else:
			return 'noun'
	return False

problem_def = get_data('problem.json')
problem_metadata = get_problem_metadata(problem_def)
if problem_metadata:
	condensed_problem_statement = condense_problem_statement(problem_metadata)
	solved = solve_problem_with_problem_type_conversion(problem_metadata)
	print('solved', solved)

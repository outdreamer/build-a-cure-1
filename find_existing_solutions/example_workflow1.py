import nltk, os, json
from nltk import pos_tag, word_tokenize

def get_data(file_path):
	if os.path.exists(file_path):
		objects = None
		with open(file_path, 'r') as f:
			objects = json.load(f)
			f.close()
		if objects:
			return objects
	return False

''' OBJECT DEFINITION '''

def get_problem_metadata(problem_def):
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
			"requirements": ["information about the subject's resources, incentives, intents, and functions"],
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
				solved_problem = apply_solutions(problem_metadata, s)
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
					solved_converted_problem = apply_solutions(converted_problem, rps)
					if solved_converted_problem:
						solved_original_problem = convert_solved_problem_to_problem_type(solved_converted_problem, problem_metadata)
						if solved_original_problem:
							solved = test_solution(problem_metadata, solved_original_problem)
							return solved
	return False

''' APPLY DEFINITION '''

def	apply_solutions(problem_metadata, solutions):
	''' to do: decide if you want to return multiple solutions if there are any '''
	'''
	solutions = [
		["find information", "find info_asymmetry", "balance information"],
		["list benefits", "find efficiencies", "apply efficiencies", "list reduced costs"]
	]
	'''
	solved_problems = {}
	solved_problem = None
	for s in solutions:
		solved_problem = apply_solution_to_problem(problem_metadata, s)
		if solved_problem:
			return solved_problem 
	return False

def apply_solution_to_problem(problem_metadata, solution_def):
	'''
		1b/4. apply solution for converted problem type
	'''
	'''
	solution = ["find information", "find info_asymmetry", "balance information"]
	'''
	solution = None
	solved_problem = {}
	solution_type = get_solution_type(solution_def)
	if solution_type == 'type':
		# this is a solution type, not a specific solution
		solution = get_solution_from_type(problem_metadata, solution_def)
		if solution:
			'''
			solution = relevant_steps = {
				'find_information': 'find_incentives_to_change_position'
			}
			'''
			solved_problem = apply_solution(problem_metadata, solution)
	if not solved_problem:
		solved_problem = apply_solution(problem_metadata, solution)
	if solved_problem:
		return solved_problem
	return False

def get_solution_from_type(problem_metadata, solution_type):
	'''
	1. derive solution type steps with get_object_metadata():
		solution_metadata['steps'] = ["find information", "find info_asymmetry", "balance information"]
	'''
	solution_type = 'balance_info_asymmetry'
	solution_metadata = get_object_metadata(solution_type, 'solution')
	# solution_metadata = {'objects': ['info', 'info_asymmetry'], 'function': 'balance', 'steps': ['find_info', 'find_info_asymmetry', 'balance_info']}
	''' to do: if balance isn't included in solution_type, its derivable from core object set, which is 'info' and 'imbalance' '''

	'''
	2. then find map between solution & problem objects with get_object_map():
		object_map['info'] = {
			'reasons': [], # list of attributes they have in common or deemed relevant/important
			'incentives': [],
			'efficiencies': []
		}
	'''
	if 'objects' in problem_metadata and 'objects' in solution_metadata:
		object_map = get_object_map(problem_metadata, solution_metadata)
		object_map = {'info': ['incentives', 'efficiencies', 'intents']}
		if object_map:
			'''
			3. then apply solution_type_steps to object_map to get abstract_problem_steps:
				object_map = {'information': 'incentives'}
				abstract_problem_steps = {
					'find_information': [
						'find reasons/efficiencies/incentives/intents'
					]
				}
				abstract_problem_steps = {
					'solution_type_step': [
						'abstract_problem_step'
					]
				}
			'''
			abstract_problem_steps = get_problem_solution_steps(object_map, solution_metadata['steps'])
			'''
				to do: decide if you want to return interim version in dict structure 
				4. then apply modifiers to make abstract_problem_steps relevant to problem with get_relevant_solution():
					relevant_problem_step = 'find reasons/efficiencies/incentives/intents to change position'
			'''
			relevant_steps = {}
			for solution_step, abstract_problem_step in abstract_problem_steps.items():
				relevant_problem_step = get_relevant_solution(abstract_problem_step)
				if relevant_problem_step:
					relevant_steps[solution_step] = relevant_problem_step
				'''
					5. return problem-related modified specific solution steps
						return modified_specific_solution_steps
				'''
				relevant_steps = {
					'find_information': 'find_incentives_to_change_position'
				}
				if relevant_steps:
					return relevant_steps
				''' apply solution for solution type to object_map, if modifiers dont already map the problem_object to the solution '''
			''' since we already applied modifiers, we need to classify the problem operations with the solution operations & check that theyre in the right position '''
			'''
			- with matching problem objects, apply solution_type to get solution
				- the solution type 'balance the info asymmetry' applied to a problem like 'persuasion' translates to the solution:
					# find information
						- find reasons to change position
						- find reasons to stay in current position
					# find information asymmetry
						- subject doesnt have information (reasons, incentives) to call change_position function
					# balance information
						- map some reason to change (safety) with some reason to stay (safety)
			'''
	return False

def get_problem_solution_steps(object_map, solution_metadata_steps):
	#solution_metadata_steps = ['find_info', 'find_info_asymmetry', 'balance_info']
	#object_map = {'info': ['incentives', 'efficiencies', 'intents']}
	problem_solution_steps = {}
	for abstract_step in solution_metadata_steps:
		problem_step_words = abstract_step.split('_')
		for i, problem_step_word in enumerate(problem_step_words):
			for key, value in object_map.items():
				if step_word == key:
					problem_step_words[i] = ','.join(values)
		if len(problem_step_words) > 0:
			problem_solution_steps[abstract_step] = ' '.join(problem_step_words)
	if problem_solution_steps:
		return problem_solution_steps
	return False

def get_relevant_solution(abstract_solution, problem_metadata):
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
					(which was converted to relevant to problem from 'find_information')

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
						- 'incentive to change position' is required/important information to solve the problem
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
	relevant_solution = None
	relevance_filter = ['required', 'functions']
	flattened = flatten_dict(problem_metadata)
	relevant_list = []
	for rf in relevance_filter:
		''' get relevant items from flattened & order in relevant_list '''
		relevant_dict = {}
		if rf in flattened:
			relevant_list.append(rf)
			first_word = flattened[rf]
			relevant_list.append(first_word)
			if first_word in flattened:
				second_word = flattened[first_word]
				relevant_list.append(second_word)
				if second_word in flattened:
					third_word = flattened[second_word]
					relevant_list.append(third_word)
					if third_word in flattened:
						fourth_word = flattened[third_word]
						relevant_list.append(fourth_word)
	print('relevant_dict', relevant_dict)
	'''
		relevant_dict = {
			"functions": "interactions",
			"interactions": "change_position",
			"change_position": "input",
			"input": "required",
			"required": ["incentive", "efficiency", "intent"]
		}
		relevant_list = ['functions', 'interactions', 'change_position', 'input', 'required']
	'''
	if len(relevant_list) > 0:
		last_item_values = flattened[relevant_list[-1]]
		''' find the adjacent object name for the target object (required function inputs) which should be at the end of this list '''
		for item in relevance_filter:
			relevant_list.remove(item)
		''' to do: given that the object of interest is a function (highest level key of problem_metadata), we should be able to derive that you wouldnt want to use the function type name '''
		# relevant_list is now ['interactions', 'change_position', 'input']
		''' remove object types from relevant_list, because we're trying to isolate a specific name that is most adjacent to object of interest (required function inputs) '''
		for item in relevant_list:
			item_object = get_objects_in_string(item)
			if item == item_object or item in item_object:
				relevant_list.remove(item)
		# relevant_list is now ['interactions', 'change_position']
		''' given that we know the target is at the end of the list, the most adjacent object to the target is the last item in the list with objects & relevance filters removed '''
		adjacent_name = relevant_list[-1]
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
				relevant_solution = '_'.join([abstract_solution_words, join_keyword, adjacent_name])
				''' relevant_solution = 'find_incentives_to_change_position" '''
				return relevant_solution
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
	return False

def get_relationship_between_objects(source, target):
	join_keyword = 'in order to'
	brief_join_keyword = get_brief_keyword(join_keyword)
	if brief_join_keyword:
		return brief_join_keyword
	return join_keyword

def get_brief_keyword(keyword):
	return 'to'

def flatten_dict(problem_metadata):
	flattened = {}
	for key, values in problem_metadata.items():
		flattened = iterate_dict(values, flattened)
	if flattened:
		return flattened
	return False

def iterate_dict(values, flattened):
	for k, v in values.items():
		if type(v) != dict:
			flattened[k] = v
		else:
			flattened = iterate_dict(v, flattened)
	return flattened

def get_object_map(problem_metadata, solution_metadata):
	# solution_objects = ['info', 'asymmetry', 'info_asymmetry']
	object_map = {}
	for so in solution_metadata['objects']:
		matched_problem_object = find_matching_object_in_problem_space(problem_metadata, so)
		if matched_problem_object:
			object_map[so] = matched_problem_object
	for f in solution_metadata['function']:
		matched_problem_object = find_matching_object_in_problem_space(problem_metadata, f)
		if matched_problem_object:
			object_map[f] = matched_problem_object
	print('object_map', object_map)
	object_map = {'info': ['incentives', 'efficiencies', 'intents']}
	'''
		- target output for info-persuasion object map (object_map):
			'info': [
				'incentive/intent to change positions',
				'incentives/inefficiencies preventing position change',
				'benefits/costs of position change'
			],
			'info_asymmetry': [
				'subject does not have information of reasons to change position'
			],
			'balance': [
				'distribute reasons to change to subject', # if lack of reasons is the problem
				'distribute information to enable access of change position functions to subject so subject finds it easier to move', # if lack of function accessibility is the problem
				'align reason to change & reason to stay so subject identifies misclassification error', # if misclassification of reason is the problem
			]
	'''
	return object_map

def find_matching_object_in_problem_space(problem_metadata, solution_object):
	''' for a solution_object like 'info', find the corresponding object in the problem like 'reasons to change position' '''
	solution_object = 'info'
	solution_object_metadata = get_object_metadata(solution_object, 'solution')
	''' find solution_object 'info' in problem '''
	matched_problem_objects = {}
	new_problem_solution_map = {}
	for problem_object in problem_metadata['objects']:
		for problem_attribute in problem_metadata:
			if problem_attribute in solution_object_metadata:
				if 'requirements' in solution_object_metadata:
					if problem_attribute in solution_object_metadata['requirements']:
						''' this attribute is a required input to the solution object, increasing the likelihood that these objects match '''
						if problem_object not in matched_problem_objects:
							matched_problem_objects[problem_object].append(problem_attribute)
							''' add problem object like incentive/efficiency/reason to map indicating relationship to solution object 'info' '''
		if problem_object in matched_problem_objects:
			new_problem_solution_map = makes_sense(problem_metadata, problem_object, matched_problem_objects)
	if new_problem_solution_map:
		print('new_problem_solution_map', new_problem_solution_map)
		'''
		- most objects in the problem match this solution_type object 'info' bc this is already converted to an information problem type, so little work is required to check for a relationship 
			problem_objects = {
				'efficiency': [],
				'incentive': [],
				'intent': [],
				'cost': [],
				'benefit': []
			}
		'''
		''' find solution_object = 'info' in problem objects ['efficiency', 'intent', 'incentive', 'cost', 'benefit', 'position'] '''
	return False

def makes_sense(problem_metadata, problem_object, matched_problem_objects):
	new_problem_solution_map = {}
	''' now that youve verified these objects match in some way, you need to check if mapping this solution object & this problem object makes sense with the problem definition '''
	''' check that mapping 'reason' to 'info' makes sense '''
	attributes_to_check = ['type']
	sense = 0
	for attribute in matched_problem_objects[problem_object]:
		if attribute in problem_metadata:
			''' standard definition validation '''
			if solution_object in problem_metadata[attribute]:
				''' is 'info' included in problem['type'] list? '''
				sense += 1
			if solution_object in stringify_metadata(problem_metadata):
				''' is 'reason' in 'info' solution object metadata? '''
				sense += 1
			if problem_object in stringify_metadata(solution_object_metadata):
				''' is 'reason' in 'info' solution object metadata? '''
				sense += 1
	if sense > 0:
		new_problem_solution_map[problem_object] = matched_problem_objects[o]
	if new_problem_solution_map:
		return new_problem_solution_map 
	return False

def get_object_metadata(object_name, object_type):
	if object_type == 'solution':
		solution_objects = get_objects_in_string(solution_type)
		solution_function = get_function_in_string(solution_type)
		if solution_objects:
			solution_metadata = {
				'objects': solution_objects, #'info_asymmetry', 
				'function': solution_function, 
				'steps': [
					'find_information',
					'find_information_asymmetry',
					'balance_information'
				]
			}
		return solution_metadata
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
	'''
		solution = relevant_steps = {
			'find_information': 'find_incentives_to_change_position'
		}
	'''
	solved_problem = None
	for abstract_step, relevant_problem_step in solution.items():
		new_problem_metadata = apply_step(problem_metadata, relevant_problem_step)
		if new_problem_metadata:
			problem_metadata = new_problem_metadata
	if solved_problem:
		return solved_problem
	return problem_metadata

def get_solution_type(solution):
	type_words = get_type_words()
	solution_words = ' '.join(solution).split(' ')
	solution_word_count = len(set(solution_words))
	union = len(type_words.union(solution_words))
	if (solution_word_count - union)/solution_word_count < 0.3:
		return True
	return False

def get_type_words():
	''' return list of abstract/interface/structural words '''
	type_words = ['info', 'symmetry']
	return set(type_words)

''' QUERY '''

def get_insights(problem_metadata):
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
	interface_problem = {}
	return interface_problem

def convert_solved_problem_to_problem_type(solved_converted_problem, original_problem_metadata):
	'''
		5. convert to original problem type
	'''
	solved_original_problem = convert_problem_to_problem_type(solved_converted_problem, original_problem_metadata)
	if solved_original_problem:
		return solved_original_problem
	return False

def convert_problem_to_problem_type(source_problem_type_metadata, target_problem_type_metadata):
	converted_problem = {}
	if converted_problem:
		return converted_problem
	return False


''' TEST '''

def test_solution(solved_original_problem, problem_metadata):
	'''
		6. test if solution actually reduces or solves original problem
	'''
	passed = is_problem_reduced(problem_metadata, solved_original_problem)
	return passed

def is_problem_reduced(problem_metadata, solved_original_problem):
	passed = False
	return passed


''' PROCESSING '''

def build_object(object_type, object_name):
	''' check for example objects in database '''
	''' check for definition of object type '''
	''' check for examples of related object types '''
	''' check for system containing object reference, to derive object definition '''
	object_instance = {}
	return False

def stringify_metadata(metadata_object):
	stringified = '_'.join([metadata_object.values()])
	return stringified

def get_function_in_string(string):
	function_list = get_data('functions.json')
	words = string.replace('_',' ').split(' ')
	if function_list:
		for function in function_list:
			if function in words:
				return function
	return False

def get_objects_in_string(string):
	''' solution_type = 'balance_info_asymmetry' '''
	function_list = get_data('functions.json')
	if function_list:
		# function_list = ['balance', 'distribute', 'allocate']
		objects = []
		words = string.split('_')
		if len(words) > 0:
			pos_type = get_pos(word)
			for word in words:
				if word not in function_list or pos_type != 'verb':
					objects.append(word)
			if len(objects) > 0:
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

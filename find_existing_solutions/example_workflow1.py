import nltk
from nltk import pos_tag, word_tokenize

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

problem_def = get_data('problem.json')
problem_metadata = get_problem_metadata(problem_def)
if problem_metadata:
	solved = solve_problem_with_problem_type_conversion(problem_metadata)
	print('solved', solved)

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
	solved_problem = {}
	solution_type = get_solution_type(solution_def)
	if solution_type == 'type':
		# this is a solution type, not a specific solution
		solution = get_solution_from_type(problem_metadata, solution_def)
		if solution:
			solved_problem = apply_solution(problem_metadata, solution)
	if not solved_problem:
		solved_problem = apply_solution(problem_metadata, solution)
	if solved_problem:
		return solved_problem
	return False

def get_solution_from_type(problem_metadata, solution_type):
	''' from solution_type = 'balance_info_asymmetry':

	1. derive solution type steps with get_object_metadata():
		solution_type_steps = ["find information", "find info_asymmetry", "balance information"]

	2. then find map between solution & problem objects: 
		map['info'] = {
			'reasons': [], # list of attributes they have in common or deemed relevant/important
			'incentives': [],
			'efficiencies': []
		}

	3. then apply solution_type_steps to problem to get specific solution steps:
		specific_solution_steps = {
			'find_information': [
				'find reasons/efficiencies/incentives/intents'
			]
		}

	4. then apply modifiers to make specific solution steps relevant to problem:
		modified_specific_solution_steps = [
			'find reasons/efficiencies/incentives/intents to change position'
		]

	5. return problem-related modified specific solution steps
		return modified_specific_solution_steps
	'''

	object_map = {}
	solution_metadata = get_object_metadata(solution_type, 'solution')
	# solution_metadata = {'object': 'info_asymmetry', 'function': 'balance', 'steps': ['find_info', 'find_info_asymmetry', 'balance_info']}
	if 'objects' in problem:
		# solution_objects = ['info', 'asymmetry', 'info_asymmetry']
		if 'objects' in solution_metadata:
			for so in solution_objects:
				matched_problem_object = find_matching_object_in_problem_space(problem_metadata, so)
				if matched_problem_object:
					object_map[so] = matched_problem_object

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
		if object_map:
			''' apply solution for solution type to problem_solution_object_map if modifiers dont already map the problem_object to the solution '''
			'''
			- with matching problem objects, apply solution_type to get solution (solution being a list of specific operations to execute)
				- 'balance the info asymmetry' in a problem like 'persuasion' translates to the steps:

					- find information
						- find reasons to change position
						- find reasons to stay in current position

					- find information asymmetry
						- subject doesnt have information (reasons, incentives) to call change_position function

					- balance information
						- map some reason to change (safety) with some reason to stay (safety)
			'''

			''' since we already applied modifiers, we need to classify the problem operations with the solution operations & check that theyre in the right position '''
			solution_steps = []
			for step in solution_metadata['steps']:
				for problem_object in problem_solution_object_map:
					if approximately_equal(problem_object, step):
						solution_steps.append(problem_object)
			if len(solution_steps) > 0:
				return solution_steps
	return False

def find_matching_object_in_problem_space(problem_metadata, solution_object):
	''' for a solution_object like 'info', find the corresponding object in the problem like 'reasons to change position' '''
	solution_object = 'info'
	''' find 'info' in problem '''
	matched_problem_objects = {}
	new_problem_solution_object_map = {}
	solution_object_metadata = get_object_metadata(solution_object, 'solution')
	for o in problem['objects']:
		for problem_attribute in problem_metadata:
			if problem_attribute in solution_object_metadata:
				if problem_attribute in solution_object_metadata['requirements']:
					''' this attribute is a required input to the solution object, increasing the likelihood that these objects match '''
					if o not in matched_problem_objects:
						matched_problem_objects[o].append(problem_attribute)
						''' add problem object like incentive/efficiency/reason to map indicating relationship to solution object 'info' '''
		if o in matched_problem_objects:
			''' now that youve verified these objects match in some way, you need to check if mapping this solution object & this problem object makes sense with the problem definition '''
			''' check that mapping 'reason' to 'info' makes sense '''
			attributes_to_check = ['type']
			sense = 0
			for attribute in matched_problem_objects[o]:
				if attribute in problem_metadata:
					''' standard definition validation '''
					if solution_object in problem_metadata[attribute]:
						''' is 'info' included in problem['type'] list? '''
						sense += 1
					if solution_object in stringify_metadata(problem_metadata):
						''' is 'reason' in 'info' solution object metadata? '''
						sense += 1
					if problem_object in stringify_metadata(solution_object_metadata)
						''' is 'reason' in 'info' solution object metadata? '''
						sense += 1
			if sense > 0:
				new_problem_solution_map[o] = matched_problem_objects[o]
	if new_problem_solution_object_map:
		print('new_problem_solution_object_map', new_problem_solution_object_map)
		'''
		- most objects in the problem match this solution_type object 'info' bc this is already converted to an information problem type, so little work is required to check for a relationship 
			matched_problem_objects = {
				'efficiency': [],
				'incentive': [],
				'intent': [],
				'cost': [],
				'benefit': []
			}
		'''
		''' find solution_object = 'info' in problem objects ['efficiency', 'intent', 'incentive', 'cost', 'benefit', 'position'] '''
		''' apply relevance modifiers to matching problem objects '''
		''' once you have the matched_problem_objects, you need to find relevant modifiers/functions applied to them that are relevant to the problem/solution '''

		relevant_problem_objects = ['required_function']
		matching_modified_problem_objects = []
		for problem_object, attributes in matched_problem_objects.items():
			''' how is 'incentive' related to problem of 'persuasion'? '''
			modified_problem_object = None
			''' 
			to do: 
				- add formatting for modifiers of a certain type, like:
					"problem_object [relationship_to_function "input" ] required_problem_function"
				- add check for relevance of modifying attribute/object in relevant_problem_objects
			 '''
			for key, values in problem_metadata.items():
				if problem_object == key:
					modified_problem_object = '_'.join([problem_object])
				else:
					if problem_object in values:
						modified_problem_object = '_'.join([key, problem_object])
					if type(values) == dict:
						for k, v in values.items():
							if type(v) == dict:
								if problem_object in v.keys():
									modified_problem_object = '_'.join([key, k, v[problem_object]])
								elif problem_object in v.values():
									modified_problem_object = '_'.join([key, k, problem_object])
					elif type(values) == list:
						if problem_object in values:
							modified_problem_object = '_'.join([key, problem_object])
					elif type(values) == str:
						modified_problem_object = '_'.join([key, problem_object, values])
				if modified_problem_object is not None:
					''' modified_problem_object should be 'incentive to change position' for a problem_object of 'incentive' ''' 
					matching_modified_problem_objects.append(modified_problem_object)
					'''
					- inputs to 'change_position' function of 'persuasion' problem metadata (in 'workflow1_problem_metadata.json')
						- intent
						- incentive
					- incentive is an input to the change_position function of the 'persuasion' problem, and 'change_position' is a required function for solving the problem 
					- an input of a function increases possibility of calling that function
					- so the 'information' of 'incentive' is the modified problem object (applying problem relevance to object):
					- this indicates why we would include 'incentive' in our mapping to 'info' solution type:
						- 'incentive to change position' is required/important information to solve the problem
					'''
		if len(matching_modified_problem_objects) > 0:
			return matching_modified_problem_objects
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
	return solved_problem

def get_solution_type(solution):
	type_words = get_type_words()
	solution_words = len(set(' '.join(solution).split(' ')))
	union = len(type_words.union(solution_words))
	if (solution_words - union)/solution_words < 0.3:
		return True
	return False

def get_type_words():
	''' return list of abstract/interface/structural words '''
	type_words = ['info', 'symmetry']
	return set(type_words)


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

def get_data(file_path):
	if os.path.exists(file_path):
		objects = None
		with open(file_path, 'r') as f:
			objects = f.read()
			f.close()
		if objects:
			json_objects = json.load(objects)
			if json_objects:
				return json_objects
	return False

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
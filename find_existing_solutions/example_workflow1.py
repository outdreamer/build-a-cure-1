'''
	Workflow 1a: Transform into combination of solved problems
	Workflow 1b: Transform into an interface problem type (problem type that can frame all problems, like route optimization, a market trade problem, an inefficiency, or a filtering problem)
		This version skips the problem type analysis & just fetches a solution for common problem types with which other problems can be framed
'''

''' the problem type for this example: persuasion (make an argument that changes a behavior metric (like direction) '''

problem_metadata = {}
problem_path = 'problem.json'
problem_def = get_data(problem_path)
if problem_def:
	solved = solve_problem_with_problem_type_conversion(problem_def)
	print('solved', solved)

def solve_problem_with_problem_type_conversion(problem_def):

	solved_problem = None
	converted_problem = None

	if problem_def:

		problem_metadata = get_problem_metadata(problem_def)

		''' fetch insights related to this problem '''
		insights = fetch_related_insights(problem_metadata)
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
				# persuasion problem super-type
				"identify optimal path to target",
				# these are related problems of this problem's insights
				"differentiating objects (cost/benefits)"
			]
		}
		'''

		''' try solutions identified as related to this problem or problem type before converting '''
		if 'solutions' in insights:
			''' found insights about solutions for this problem type '''
			solved_problem = apply_solutions(problem_metadata, insights['solutions'])
			if solved_problem:
				return solved_problem 

		''' if solutions of this problem type didnt work, try solutions of related problems '''
		if 'related_problems' in insights:
			for p in insights['related_problems']:
				converted_problem = convert_to_solved_problem(problem_metadata, p)

		''' if there are no related problem types/related problems, convert to an interface problem type '''
		if converted_problem is None:
			converted_problem = convert_to_interface_problem(problem_metadata)

		''' apply solutions for converted problem '''

		''' to do: before converting to a problem type, check that there are solutions/types available for that problem type '''

		if converted_problem:
			''' get solutions from insights for the converted problem '''
			related_problem_insights = fetch_related_insights(converted_problem)
			if related_problem_insights:
				if 'solutions' in related_problem_insights:
					''' found insights about solutions for related problem type '''
					related_problem_solutions = related_problem_insights['solutions']
					if related_problem_solutions:
						solved_converted_problem = apply_solutions(converted_problem, related_problem_solutions)
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

def apply_solution_to_problem(problem_metadata, solution):
	'''
		4. apply solution for converted problem type
	'''
	'''
	solution = ["list benefits", "find efficiencies", "apply efficiencies", "list reduced costs"]
	'''
	solved_problem = {}
	if 'solution_type' in solution:
		if solution['solution_type'] == 'solution_type':
			# this is a solution type, not a specific solution
			solution = apply_solution_type(problem_metadata, s)
			if solution:
				solved_problem = apply_solution(problem_metadata, solution)
		else:
			solved_problem = apply_solution(problem_metadata, s)
		if solved_problem:
			return solved_problem
	return False

def apply_solution_type(problem_metadata, solution_type):
	solution = None
	'''
		- get solution & problem definition
		if solution_type = 'balance_info_asymmetry', you can implement this solution_type to get a solution for a problem space:
			- find objects in problem that match solution_type objects
				- find information
					- 'reason to change positions'
					- 'incentives/inefficiencies preventing position change'
					- 'benefits/costs of position change'
				- find information asymmetry 
					- 'interaction of (reason to change positions) and (subjects' (current information or focus))'
					# focus can act as a proxy for information, making a change seem important/relevant just by enabling the subject to focus on some benefit rather than a cost
				- find balance implementation in problem 
					(what does balance mean for this problem - equal distribution? removal of information? distributing info derivation methods?)
					- balance as 'matching' or 'alignment'
						- match (reason to change position) with (intent (need, incentive) to change position)
			- with matching problem objects, apply solution_type to get solution (solution being a list of specific operations to execute)
				- 'balance the info asymmetry' in a problem like 'persuasion' translates to the steps:
					- find information
						- find reasons to change position
						- find reasons to stay in current position
					- balance information
						- map some reason to change (safety) with some reason to stay (safety)
	'''

	problem_solution_object_map = {}
	if solution and problem_metadata:
		''' solution_type should have a function and an object '''
		solution_metadata = get_solution_metadata(solution_type)
		# solution_metadata = {'object': 'info_asymmetry', 'function': 'balance'
		if solution_type == 'balance_info_asymmetry':
			if 'objects' in problem:
				solution_objects = get_objects(solution_metadata['object'])
				# solution_objects = ['info', 'asymmetry', 'info_asymmetry']
				if solution_objects:
					for so in solution_objects:
						matched_problem_object = find_matching_object_in_problem_space(problem_metadata, so)
						if matched_problem_object:
							problem_solution_object_map[so] = matched_problem_object

		'''
		- target output for info-persuasion object map (problem_solution_object_map):
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
		if problem_solution_object_map:
			''' apply solution for solution type to problem_solution_object_map '''

			'''
			- with matching problem objects, apply solution_type to get solution (solution being a list of specific operations to execute)
				- 'balance the info asymmetry' in a problem like 'persuasion' translates to the steps:
					- find information
						- find reasons to change position
						- find reasons to stay in current position
					- balance information
						- map some reason to change (safety) with some reason to stay (safety)
			'''
			
	return solution

def get_object_metadata(object_name):
	return object_metadata

def find_matching_object_in_problem_space(problem_metadata, solution_object):
	''' for a solution_object like 'info', find the corresponding object in the problem like 'reasons to change position' '''
	solution_object = 'info'
	''' find 'info' in problem '''
	matched_problem_objects = {}
	new_problem_solution_object_map = {}
	solution_object_metadata = get_object_metadata(solution_object)
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

		'''
		- find solution_object = 'info' in problem objects ['efficiency', 'intent', 'incentive', 'cost', 'benefit', 'position']
		'''

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

def stringify_metadata(metadata_object):
	stringified = '_'.join([metadata_object.values()])
	return stringified

def get_solution_metadata(solution_type):
	solution_metadata = {'object': 'info_asymmetry', 'function': 'balance'}
	return solution_metadata

def get_objects(solution_type):
	''' solution_type = 'info_asymmetry' '''
	solution_objects = []
	return solution_objects

def apply_solution(problem_metadata, solution):
	return solved_problem


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
	return problem_metadata


''' QUERY '''

def fetch_related_insights(problem_metadata):
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


''' PROCESSING '''

def get_data(file_path):
	if os.path.exists(file_path):
		with open(file_path, 'r') as f:
		objects = f.read()
		f.close()
		return objects
	return False
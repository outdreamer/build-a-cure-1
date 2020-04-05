from type_functions import *

'''

	mapping requires:

      - attribute/object/function match functions

      - specific interface identification function

      - standardization network-framing function to describe a system as a network (the standard structure) & position each object, identifying connecting functions

      - system analysis function (identify boundaries, gaps, limits, layers, incentives/intents/questions, & other system objects)

      - isolation function, representating function/attribute changes independent of system context with respect to position or time (snapshot/state or subset)

      - function to define (isolate an object/concept/function for identification, identify definition routes)

          - alternative routes to an object (create & retrieve info from definition_routes.json if its already in interface_networks.json or definition_routes.json)
          - definition_routes.json can be generated from the paths in interface_networks.json, which just describes the links in networks of concepts/intents & other interface networks
        
          - identify definition routes:
            - function to map non-structural interface object/function/system to structural object/function/system
              - function to map object/system/function type/set/chain to a shape in various contexts (linking nodes, depicting an attribute set, etc)

          - identify interface trajectory between other interfaces
            - may involve navigating sub-networks within an interface, not just mapping between interfaces
            - trajectories such as: most efficient path, and destination in same position on other interface)
            - uses interface_networks.json if it exists and if not, interface identification, network mapping, and similarity testing
          
            - this is an extension of the system analysis function, adding structure to the system definition as well as efficient paths, generative paths, identifying paths, etc

      - to map a function/object/system to a structure, you need:
        - the definition
        - system analysis of the definition
        - objects from system analysis like implication
        - structures/functions mapped to the objects (like copy implication is that position of the duplicate object must be different from the original object)
        
        - these objects can be framed in many structural ways:
          - as a set of filters (generating the object/function/system)
          - as a set of vectors (indicating the key attributes or functions generating/determining the object/function/system)
          - as a set of shape structures (indicating how the object's logic works internally (how attributes are related to functions, as in a shape)
          - as a set of embedded dimensions (where an embedded graph indicates internal or subset processing/objects)
          - as a set of related graphs (where each graph depicts structure of some attribute set of the original object/function/system)

      - to map attributes (identifying/differentiating measurable properties of an object like relevance or connectivity), you need:
        - a base object structure 
        - a dimension to frame values & their differences added by the attribute
        - the attribute can be in an embedded dimension set (to indicate differences in value on multiple parameters of the attribute, like when the differences offered by an attribute vary by change type & change rate), but the base object should be included in the structural representation if possible

      - to map a system, you need:
        - nodes with boundaries, indicating objects & components of objects
        - functions linking nodes:
          - vectors with direction, indicating causal direction, input/output flow, intent direction, and other direction-structurable attributes
          - functions whose shape indicates relationship type 
        - system boundaries/layers/gaps/potential and other system structures if they exist

      - to map a type, you need:
        - subset shapes to indicate attribute sets, and structures linked to each attribute to indicate attribute value, range, type & other metadata
        - nodes indicating types 
        - links indicating any causal directions between types
'''

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
		logical_rules = get_data('rules.json')
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
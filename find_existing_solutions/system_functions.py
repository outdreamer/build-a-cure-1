from interface_functions import identify_interfaces
'''
    - function metadata:
        - position/role in a system
        - function to derive role (intended subset of intent stack)
        - function type
        - emergent side effects in edge cases, rule change states, & interacting with other system layers
    - object identification function
    - attribute identification function
    - function identification function
    - attribute (like similarity) testing function
    - function application function
'''
system = [
	'vdj recombination uses variable, diversity, and joining segments',
	'these segments are recombinated using core operations like delete and copy',
	'constant segments are also involved',
	'antibodies or t-cell receptors can be formed using vdj recombination',
]
''' from this system described as a function set:
	objects = [variable segment, diversity segment, joining segment, constant segment, antibodies, t-cell receptors, receptors, t-cells]
	attributes = [constant, variable, diverse, joined, involved, core, like, possible/can, with]
	functions = [vdj recombination, delete copy, recombine, combine, use/apply, apply process, create/form]
	system_rules = [full set of rules filled in by system analysis to describe probable system dynamics given input rule subset]
'''
random_set = ['membranes', 'bonds', 'checkpoints', 'pressure', 'neutralizing process', 'competition']
''' out of this system described as a set of different type instances:
	objects = [membranes, bonds, checkpoints, points, checks, pressure]
	attributes = [limit, pressure, force, neutral, opposing]
	functions = [neutralize, press/apply pressure, check, limit, connect, process, compete]
'''
def define_system(system):
	''' system can be an object or a function or a set, like functions extracted from a paragraph describing the system 
	      - system analysis function (identify boundaries, gaps, limits, layers, & other system objects)
	'''
	system_analysis_questions = []
	rules = get_data('system_logic_rules.json')
	if rules:
		if 'system_analysis_questions' in rules:
			system_analysis_questions = rules['system_analysis_questions'] 
	system_def = {'objects': [], 'attributes': [], 'functions': [], 'interfaces': []}
	objects = identify_objects(system)
	if objects:
		system_def['objects'] = objects
	attributes = identify_attributes(system)
	if attributes:
		system_def['attributes'] = attributes
	functions = identify_functions(system)
	if functions:
		system_def['functions'] = functions
	interfaces = identify_interfaces(system, interface_type=None)
	if interfaces:
		system_def['interfaces'] = interfaces
	return system_def

def identify_objects(system):
	modifiers = ['processing']
	agency_keywords = ['acts', 'exerts']
	''' 
	- this will also apply general system patterns to isolate objects by predicting their existence & narrowing down their identities using filters 
		
		- given that we know that systems generally have layers, what objects act like layers or are there any traces of layers in the function set?
			- if so, what other attributes do they have in common with the layer object
		
		- we know systems generally have filters & gaps in enforcement - do any rules or objects show signs of those?

		- this is applicable when we dont have a full description of the system or need to classify an object in the function set as the overriding object type 
			- a membrane may not just be a boundary, it may also act as a filter, and that function may be more important so it should be classified as that
	
	- methods to identify objects:
		- start by applying general system patterns to theorize existence of objects and see if any are found in expected positions
		- replace theorized objects with other object keywords and see if the system still makes sense (is logically consistent, with no invalid rules)
		- rule out functions/attributes
	'''

	'''
		functions & attributes can be framed as objects, how to differentiate from actual objects:
			- objects have state that is operated on by associated functions
			- objects have types which are determined by associated attribute sets & values
			- attributes can describe many other objects/attributes/functions 
			- functions can be applied to other objects/attributes/functions to change them
	'''

	return False

def identify_attributes(system):
	''' attributes may need to be derived and arent as explicitly defined as often as objects 

	attributes & functions can both describe objects' behavior & identity, how to differentiate:
		- attributes are often defined as a combination of other attributes 
		- if you define functions in terms of attributes, there will usually be differences in implementation
		- functions may directly change the structure/state of an object (whereas an 'importance' attribute might not)
		- attributes may describe the state of an object (charged)
		- attributes referring to functionality (an 'ionizing' substance) can be directly mapped to functions
		- attributes have an associated value, like function parameters can have an associated value
		- functions have clearly defined inputs/outputs and an attribute might not
	'''

	return False

def identify_functions(system):
	''' functions may be easily mapped to verbs, but emerging functions need to be derived 

	functions & objects both have inputs & outputs & internal logic, how to differentiate:
		- functions are treated as a means to an end rather than a destination, unless its a system to find the right function
		- functions will have more similarities to paths/lines than points
	'''

	return False

def identify_sub_systems(system):
	return False



'''
    - object identification function
        - membranes/bonds
        - checkpoints
        - pressure
        - neutralizing processes
        - competition
        
    - attribute identification function
    - function identification function
    - attribute (like similarity) testing function
    - function application function
'''

def identify_objects(system):
	''' system can be an object or a function or a set, like functions extracted from a paragraph describing the system '''
	modifiers = ['processing']
	agency_keywords = ['acts', 'exerts']
	''' 
		this will also apply general system patterns to isolate objects by predicting their existence & narrowing down their identities using filters 
		
		- given that we know that systems generally have layers, what objects act like layers or are there any traces of layers in the function set?
			- if so, what other attributes do they have in common with the layer object
		
		- we know systems generally have filters & gaps in enforcement - do any rules or objects show signs of those?

		- this is applicable when we dont have a full description of the system or need to classify an object in the function set as the overriding object type 
			- a membrane may not just be a boundary, it may also act as a filter, and that function may be more important so it should be classified as that
	
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
	'''

	random_set = [
		'membranes',
		'bonds',
		'checkpoints',
		'pressure',
		'neutralizing process',
		'competition'
	]
	''' out of this system described as a set of different type instances:
		objects = [membranes, bonds, checkpoints, points, checks, pressure]
		attributes = [limit, pressure, force, neutral, opposing]
		functions = [neutralize, press/apply pressure, check, limit, connect, process, compete]
	'''

	return False

def identify_attributes(system):
	''' system can be an object or a function '''

	''' attributes may need to be derived and arent as explicitly defined as often as objects '''

	return False

def identify_functions(system):
	''' system can be an object or a function '''

	''' functions may be easily mapped to verbs, but emerging functions need to be derived '''

	return False
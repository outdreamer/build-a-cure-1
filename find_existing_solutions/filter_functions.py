def get_concepts():
	''' retrieve concept definitions '''
	concepts = get_data('concepts.json')
	if concepts:
		return concepts
	return False

def identify_concepts(system):
	''' identify the concepts in a system, explicit and emerging '''
	return False

def get_structures_for_system(system):
	''' this function maps a system to a structure like a common shape '''
	return False

def derive_concepts_from_structure(structure):
	''' this function uses rules of common concept patterns & filtering rules to remove other objects '''
	concept_attributes = ['abstract version of structural attribute', 'not directly mappable to one structure', 'isolatable']
	abstract_concept_attributes = ['cant be further simplified', 'core concept', 'occupy every system']
	sub_concept_attributes = ['not directly mappable to structure', 'not an abstract attribute', 'is a specific version of an abstract concept with attributes added']
	
	type_attributes = ['position in type hierarchy', 'has parent type']
	function_attributes = ['changes objects using ordered rule set']
	object_attributes = ['attribute set that is not a concept, function, or the system being checked for concepts itself', 'has functionality that can be activated conditionally out of order']
	system_attributes = ['isolated from other systems with a limit or boundary', 'contains objects and functions']
	
	concept_patterns = ['change definitions across systems', 'have multiple definitions', 'have multi-layer definitions', 'occupy many systems', 'abstraction of structural attributes or sets']
	''' apply additional hard-coded filters like:
		- checking if the concept can be framed as a function, input, type, object, or other system object like a layer
	'''
	''' this rule set should filter the system the most to start, after which remaining objects can be filtered using attribute rules '''
	filtered_structure = structure
	for filter_rule in concept_patterns:
		new_filtered_structure = apply_filter(structure, filter_rule)
		if new_filtered_structure:
			filtered_structure = new_filtered_structure
	if filtered_structure:
		concept_arguments = {}
		for attribute in concept_attributes:
			attribute_found, objects_found = check_for_attribute(filtered_structure, attribute)
			if attribute_found and objects_found:
				if attribute_found not in concept_arguments:
					concept_arguments[attribute_found] = set()
				concept_arguments[attribute_found] = concept_arguments[attribute_found].union(objects_found)
		if len(concept_arguments) > 0:
			''' add additional filtering for abstract_concept_attributes & sub_concept_attributes '''
			return concept_arguments
	return False

def check_for_attribute(structure, attribute):
	return False

def apply_filter(structure, filter_rule):
	''' 
		- the filtering rule should be converted to an instruction, that is directly mappable to objects in the structure 

		- 'apply' is the process of injecting an object to another 
			- injecting the structure to the filtering rule in this case

		- example:
			- filtering a structure like 'square' by the rule 'convert angles to parallel' should convert the square into four parallel lines


	'''
	return False

def derive_concepts(system):
	''' identify the concepts in a structure 
		this function examines the relationships in a structure/system,
		and checks those relationships/types for a corresponding concept with a matching/similar structure
	'''
	concepts = None
	structures = None
	if 'structures' in system:
		if len(system['structures']) > 0:
			structures = system['structures']
	if not structures:
		structures = get_structures_for_system(system)
	if structures:
		for structure in structures:
			for concept in concepts:
				found_concept = find_concept_in_structure(concept, structure)
				if found_concept:
					concepts.append([found_concept, structure])
			derived_concepts = derive_concepts_from_structure(structure)
			if derived_concepts:
				for derived_concept in derived_concepts:
					concepts.append([derived_concept, structure])
	''' as an alternative if none are found, pull the list of stored concepts & check for partial matches '''
	if len(concepts) > 0:
		return concepts
	return False 

def find_concept_in_structure(concept, structure):
	'''
		- this can be used to find out if a structure (like an invention or current product) produces a target concept 
      
      	- function to find if a concept definition matches any component of a structure:

	      	- get concept definition
	        - get list of structure objects
	        - check if any structure objects match definition relationship objects
	        - if so, get relationship between those structure objects
	        - check if that structure relationship matches concept definition relationship

	        - example:
	        
	          - pull definition for concept

	          trust: [
	            'depend on limited/specific inputs',
	            'check at intervals'
	          ]

	          - structure: 'test applied daily'
	            - structure objects: 'test'
	            - relationship: 'apply test daily'

	          - matching objects: 
	            'test', 'check'
	            'daily', 'interval'

	          - matching relationship:
	            'check at intervals' matches 'apply test daily'

        	  - this structure 'apply test daily' is a potential source of trust in a system (the only time info about the object being tested is not trusted is during the test)
    '''
    return False

def get_relevant_path(problem_metadata, relevance_filters):
	other_filters = relevance_filters
	relevant_path = []
	specific_attribute_values = []
	for key, value in problem_metadata.items():
		if key in relevance_filters: # functions or whichever filtering key comes first in dict
			other_filters.remove(key)
			if type(value) == dict:
				for function_type, functions in value.items():
					if type(functions) == dict:
						flattened_sub_dict = flatten_dict(functions)
						for rf in other_filters:
							''' if rf = 'required' in functions '''
							if rf in ' '.join(flattened_sub_dict.keys()) or rf in ' '.join(flattened_sub_dict.values()):
								''' check if dict can cast to str or dump json, check that this sub-dict is worth pursuing '''
								for function_name, function_metadata in functions.items():
									''' function_name = change_position '''
									if type(function_metadata) == dict:
										flattened_function = flatten_dict(function_metadata)
										if flattened_function:
											if rf in ' '.join(flattened_function.keys()) or rf in ' '.join(flattened_function.values()):
												''' if rf = 'required' in {"input": {"required": ["incentive", "efficiency", "intent"]}} '''
												for attribute, attribute_metadata in function_metadata.items():
													''' attribute = 'input' '''
													if type(attribute_metadata) == dict:
														for attribute_name, specific_attribute_values in attribute_metadata.items():
															''' attribute_name = 'required' '''
															if attribute_name == rf: # required
																if type(specific_attribute_values) == list:
																	relevant_path = [key, function_type, function_name, attribute, attribute_name]
																	''' relevant_path = ['functions', 'interactions', 'change_position', 'input', 'required'] '''
	if len(relevant_path) > 0 and len(specific_attribute_values) > 0:
		return relevant_path, specific_attribute_values
	return False, False

def get_relevance_filters(relevance_intents, problem_object):

	''' for an intent like 'specificity', which we interpret as 'add conditions/modifiers',
		and a sub-intent like 'find reason/intent', 
			we look up:
				- required inputs 
				- specific intents

		to get guaranteed aspects of the problem object that can be used to modify a general problem step like 'find incentives'
			to add a reason for that step, 
			such as the name/function intents of functions using incentives as an input,
			where the 'reason for the problem_step' is the item we've identified as relevant for the goal of 'find specific intent' for the problem_step
	'''
	search_intents = get_data('search_intents.json')
	if search_intents:
		if 'problem' in search_intents:
			'''
			problem_search_intents = {
				'specificity': [
					['required', 'functions']
				],
				'intent': [
					['required', 'functions'],
					['intents', 'functions']
				]
			}
			'''
			for relevance_intent in relevance_intents:
				if relevance_intent in search_intents['problem']:
					if type(search_intents['problem'][relevance_intent]) == list:
						return search_intents['problem'][relevance_intent]
	return False
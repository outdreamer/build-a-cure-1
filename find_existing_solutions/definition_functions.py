from utils import *

def get_shapes():
	''' retrieve shape definitions 
	get functions can:
		- retrieve stored objects
		- find objects in a system
		- call get_object_metadata to describe the metadata of a stored/found object
	'''
	shapes = get_data('shapes.json')
	if shapes:
		return shapes
	return False

def get_object_metadata(object_name, object_type):
	print('function::get_object_metadata')
	''' object_name can be an abstract solution type string, or a solution step list '''
	object_name = object_name if type(object_name) == str else ' '.join(object_name)
	object_metadata = {
		'objects': [], #'info_asymmetry', 
		'functions': [], 
		'steps': []
	}
	objects = get_objects_in_string(object_name)
	functions = get_function_in_string(object_name)
	if objects:
		object_metadata['objects'] = objects #'info_asymmetry'
	if functions:
		object_metadata['functions'] = functions
	if object_type == 'solution':
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

def get_concept_metadata(concept_name):
	concepts = get_data('concepts.json')
	if concepts:
		if concept_name in concepts:
			concept = concepts[concept_name]
			''' get definition for concept '''
			definitions = get_data('definition_routes.json')
			if definitions:
				if concept_name in definitions:
					concept['definitions'] = definitions[concept_name]
			if 'functions' not in concept:
				concept['functions'] = []
			functions = get_data('functions.json')
			if functions:
				if concept_name in functions['interface_functions']['concept_functions']:
					concept['functions'].extend(functions['interface_functions']['concept_functions'][concept_name])
				rules = get_data('system_logic_rules.json')
				if rules:
					if concept_name in ' '.join(rules.keys()):
						for key, val in rules.items():
							if concept_name in key:
								if type(val) == list:
									concept['functions'].extend(val)
				concept_functions = find_functions_in_dict(functions, [], search_term)
				if concept_functions:
					concept['functions'].extend(concept_functions)
			return concept
	''' to do: make call to define concept if no definition is found '''
	abstract_system = get_system('abstract.json')
	all_attributes = get_attributes(abstract_system, ['all'])
	concept['attributes'] = {'unique': {}}
	for attribute in all_attributes:
		has_attribute = has_attribute(concept, attribute)
		if has_attribute:
			''' get objects with similar attributes & attribute values because these are the objects to differentiate from '''
			concept['attributes'][attribute] = {'value': None, 'objects': {}}
			attribute_value = get_attribute_value(abstract_system, concept, attribute)
			if attribute_value:
				concept['attributes'][attribute]['value'] = attribute_value
			objects_with_attribute = get_objects_with_attribute(abstract_system, attribute)
			if objects_with_attribute:
				objects_with_attribute_value = get_objects_with_attribute_value(abstract_system, attribute, attribute_value)
				for object_with_attribute in objects_with_attribute:
					concept['attributes'][attribute]['objects'][object_with_attribute] = None
					if object_with_attribute in objects_with_attribute_value:
						if objects_with_attribute_value[object_with_attribute] == attribute_value:
							''' this object attribute value equals that of the concept we're isolating '''
							concept['attributes']['equal'][object_with_attribute] = {attribute: attribute_value}
						else:
							''' this object's attribute value is not equal to the concept's attribute value, so log its own value in the objects array '''
							concept['attributes'][attribute]['objects'][object_with_attribute] = objects_with_attribute_value[object_with_attribute]
			else:
				''' no other objects with this attribute '''
				concept['attributes']['unique'][attribute] = attribute_value
	print('attributes', concept['attributes'])
	''' 
		once you have the related objects with equal attribute values or attributes that are unique to this concept, 
		and a list of related objects with the same attributes, you can differentiate this concept further

		the objects with equal attributes may be a prior version or causal object for this concept, 
		in which case this concept may be definable using a path between those objects, 
		if this concept's unique attributes can emerge from that path
	'''
	return False

def get_attribute_value(system, concept, attribute):
	return False

def get_objects_with_attribute(system, attribute):
	return False

def get_objects_with_attribute_value(system, attribute, attribute_value):
	return False

def get_system(system_name, system):
	''' to do: add support for assembling system if system attributes/components are passed in rather than system name '''
	system_definition = get_data(system_name)
	if system_definition:
		return system_definition
	if system_attributes:
		assembled_system = build_system(system)
		if assembled_system:
			return assembled_system
	return False

def build_system(system):
	return False

def describe_system(system, description_type):
	''' description_type can support all, attributes, functions, generative, filters, etc '''
	return False

def get_attributes(system, attribute_types):
	''' to do: add support for getting attributes specific to an object/function/system 

	attribute_types can be a list of types like:
	- direct/indirect
	- hub 
	- causal
	- input/output
	- variable
	- descriptive
	- functional
	- type
	- cross system (difference, importance)
	- abstract
	- alternate/substitute
	'''
	attributes = get_data('attributes.json')
	if attributes:
		return attributes
	described_system = describe_system_attributes(system)
	if described_system:
		return described_system
	return False

def get_function_metadata(fdef, delimiter):
	function_items = fdef.split(delimiter)
	if len(function_items) > 0:
		function = function_items[1].replace('):', '').split('(')
		if len(function) > 1:
			function_name = function[0]
			syntax_function_name = ''.join(['def ', function_name, '('])
			function_params = function[1].replace(' ','').split(',')
			function_code = []
			start_adding = False
			function_path = ''.join([function_items[0], '.py'])
			if os.path.exists(function_path):
				code = get_data(function_path)
				if code:
					for line in code.split('\n'):
						if syntax_function_name in line:
							start_adding = True
						else:
							if start_adding:
								if 'def ' in line:
									start_adding = False
								else:
									''' to do: add filter for comments '''
									function_code.append(line)
				function_def = {'name': function_name, 'params': function_params, 'code': function_code}
				return function_def
	return False

def get_problem_metadata(problem_def_path):
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
	problem_def = get_data(problem_def_path)
	if problem_def:
		return problem_def
	return False
def identify_interfaces(system, interface_type):
	''' identify interfaces in a system 
		- here we are identifying common inputs to functions in a system, which are candidates for interfaces
		- to do:
			- interface: a standard or base which highlights differences of a certain type for comparison, 
				hosting changes within the range of that type so further changes within that type range can be compared,
				frameable as a filter set
			- add filters to identify variables that cause or provide a platform for other variables for develop
			- transfer key checks to validation
			- pull from interface_networks.json if it exists
	'''
	abstract_interfaces = set()
	abstract_interface_objects = {}
	system_item_types = ['objects', 'functions', 'attributes']
	if interface_type in ['all', 'abstract']:
		if 'objects' in system and 'functions' in system:
			''' identify abstract interface objects '''
			for interface in interfaces:
				interface_path = ''.join([interface, '.json'])
				interface_objects = get_data(interface_path)
				if interface_objects:
					for interface_object_name, values in interface_objects.items():
						''' given this object definition, do any system objects match, either on an attribute set or function set '''
						for interface_item in system_item_types:
							if interface_item in values:
								for interface_item in values[interface_item]:
									for system_item in system_item_types:
										if system_item in system:
											for system_item_name, system_item_value in system[system_item].items():
												''' here we check for a direct match, an intent match, a type match, etc '''
												match_found = matches(interface_item, system_item_name, system[system_item])
												if match_found:
													if interface_object_name not in abstract_interface_objects:
														abstract_interface_objects[interface_object_name] = {'objects': [], 'attributes': [], 'functions': []}
													if system_item not in abstract_interface_objects[interface_object_name]:
														abstract_interface_objects[interface_object_name][system_item] = []
													abstract_interface_objects[interface_object_name][system_item].append(system_item_name)
													abstract_interfaces.add(system_item_name)
			print('abstract_interface_objects', abstract_interface_objects)
		if interface_type in ['all', 'general']:
			''' identify general interfaces likely for this system '''
			''' for example, bio systems are likely to have one-directional interface chains, communication interfaces, & certain priority interfaces like efficiency '''
			''' first pull rules about system interfaces for this system type '''
			general_interfaces = set()
			logic_rules = get_data('system_logic_rules.json')
			if logic_rules:
				if 'general_interfaces' in logic_rules:
					for rule in logic_rules['general_interfaces']:
						rule_objects = get_objects_in_string(rule)
						rule_functions = get_functions_in_string(rule)
						rule_attributes = get_attributes_in_string(rule)
						rule_def = {'objects': [], 'functions': [], 'attributes': []}
						rule_def['objects'] = rule_objects if rule_objects else []
						rule_def['functions'] = rule_functions if rule_functions else []
						rule_def['attributes'] = rule_attributes if rule_attributes else []
						for key, rule_values in rule_def.items():
							for rule_value in rule_values:
								for system_item in system_item_types:
									if system_item in system:
										for system_item_name, system_item_value in system[system_item].items():
											''' here we check for a direct match, an intent match, a type match, etc '''
											match_found = matches(rule_value, system_item_name, system[system_item])
											if match_found:
												general_interfaces.add(system_item_name)
		if interface_type in ['all', 'specific']:
			''' identify specific interfaces in a system '''
			function_inputs = set()
			object_dependencies = set()
			for system_object in system['objects']:
				if 'attributes' in system_object:
					for attribute in system_object['attributes']:
						attribute_definition = get_definition(attribute)
						if attribute_definition:
							if 'dependencies' in attribute_definition:
								for dependency in attribute_definition['dependencies']:
									if 'type' in dependency and 'name' in dependency:
										if dependency['type'] == 'input':
											dependencies.add(dependency['name'])
			for system_function in system['functions']:
				if 'inputs' in system_function:
					for function_input in system_function['inputs']:
						function_inputs.add(function_input)
			common_specific_interfaces = function_inputs.union(dependencies)
			''' to do: 
				- apply filters based on the definition of interface:
					- causes other changes
					- system-wide or common attribute 
					- standard for comparison
					- used as an anchor or platform for change
			'''
		if interface_type == 'all':
			all_interfaces = abstract_interfaces.union(general_interfaces).union(common_specific_interfaces)
		elif interface_type == 'abstract':
			if len(abstract_interfaces) > 0:
				return abstract_interfaces
		elif interface_type == 'general':
			if len(general_interfaces) > 0:
				return general_interfaces
		elif interface_type == 'specific':
			if len(common_specific_interfaces) > 0:
				return common_specific_interfaces
	return False	

def define_interface(system):
	''' once an interface is identified, describe its generative objects/functions & store the definition 
		the standard metadata for an interface:

		- the attribute determining the interface filter set (type/intent/structure)
		- the filter set (conversion functions)

	'''
	return False

def convert_to_interface(system, interface):
	''' 
	- convert a system to an interface, 
		deriving the interface-relevant objects for each system object/attribute/function,
		and returning the set of derived objects as a converted system 
	
	- this means applying the filter set in the definition of the interface 

	'''
	return False

def match_interface(system):
	''' this is usually just determining which interface an object/attribute/function is most relevant to or clearly a member of 

	- if an object isnt listed as a member of an interface in interface_networks.json, the interface most likely to be relevant can be evaluated
		- with testing functions (what does it act like, what is it similar to, what groups is it a member of, what is it definitely not
		- apply a structure to the object, and ifnd what structure matches the most (is it a direction? thats probably an intent)
	'''
	return False
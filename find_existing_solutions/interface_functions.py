def identify_interfaces(system):
	''' identify interfaces in a system 
		this includes:
			- identifying relevant abstract interfaces
			- identifying relevant general interfaces expected for a type 
			- identifying relevant specific interfaces
	'''
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
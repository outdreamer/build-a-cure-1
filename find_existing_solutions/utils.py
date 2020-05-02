import os, json
import nltk
from nltk import pos_tag, word_tokenize
from textblob import TextBlob, Sentence, Word, WordList
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from get_pos import *
from get_vars import *
from get_structural_objects import *
from get_metadata import get_metadata, get_structural_metadata, get_data_from_source

def find_subdict_in_dict(function_dict, found_dict, search_term):
	for k, v in function_dict.items():
		if search_term in k:
			found_dict[k] = v
		else:
			if type(v) == list:
				for value in v:
					if search_term in value:
						found_dict[k] = value
			elif type(v) == str:
				if search_term in v:
					found_dict[k] = v
			elif type(v) == dict:
				found_dict = find_subdict_in_dict(v, found_dict, search_term)
	if found_dict:
		return found_dict
	return False

def find_functions_in_dict(function_dict, found_functions, search_term):
	for k, v in function_dict.items():
		if search_term in k:
			found_functions.append(k)
		else:
			if type(v) == list:
				for value in v:
					if search_term in value:
						found_functions.append(value)
			elif type(v) == str:
				if search_term in v:
					found_functions.append(v)
			elif type(v) == dict:
				found_functions = find_functions_in_dict(v, found_functions, search_term)
	if found_functions:
		if len(found_functions) > 0:
			return found_functions
	return False

def flatten_dict(problem_metadata):
	flattened = {}
	for key, values in problem_metadata.items():
		flattened = iterate_dict(key, values, flattened)
	if flattened:
		return flattened
	return False

def iterate_dict(key, values, flattened):
	if type(values) == dict:
		# print('dict values', key, values.keys())
		for k, v in values.items():
			if type(v) != dict:
				flattened[k] = v
			else:
				flattened = iterate_dict(k, v, flattened)
	else:
		''' to do: add support for nested items other than dicts '''
		# print('list values', key)
		flattened[key] = values
	return flattened

def remove_file(file_path):
	if os.path.exists(file_path):
		os.remove(file_path)
		if os.path.exists(file_path):
			return False
	return True

def get_pos(word):
	tagged = pos_tag(word_tokenize(word))
	for item in tagged:
		if 'V' in item[1]:
			return 'verb'
		else:
			return 'noun'
	return False

def get_data(file_path):
	if os.path.exists(file_path):
		objects = None
		with open(file_path, 'r') as f:
			objects = json.load(f) if '.json' in file_path else f.read()
			f.close()
		if objects:
			return objects
	return False

def stringify_metadata(metadata_object):
	print('function::stringify_metadata')
	stringified = '_'.join([metadata_object.values()])
	return stringified

def get_function_in_string(string):
	print('function::get_function_in_string')
	found_functions = []
	function_list = get_function_list()
	if function_list:
		words = string.replace(' ','_').split('_')
		if len(words) > 0:
			for word in words:
				if word in function_list:
					found_functions.append(word)
	found_functions = set(found_functions)
	if len(found_functions) > 0:
		return found_functions
	return False

def get_objects_in_string(string):
	''' solution_type = 'balance_info_asymmetry' '''
	function_list = get_function_list()
	if function_list:
		words = string.replace(' ', '_').split('_')
		if len(words) > 0:
			objects = []
			for word in words:
				pos_type = get_pos(word)
				if word not in function_list and pos_type != 'verb':
					objects.append(word)
			objects = set(objects)
			if len(objects) > 0:
				return objects
	return False

def get_function_list():
	function_list = []
	functions = get_data('functions.json')
	if functions:
		new_functions = flatten_dict(functions)
		for key, values in new_functions.items():
			function_list.append(key)
			function_list.extend(values)
		if len(function_list) > 0:
			function_list = set(function_list)
			return function_list
	return False

def get_type_words():
	print('function::get_type_words')
	''' return list of abstract/interface/structural words '''
	type_words = ['info', 'symmetry']
	return set(type_words)

def convert_sentence(sentence, av):
    word_map = {}
    word_map, av = standard_text_processing(sentence, av)
    if word_map:
        print('word_map', word_map)
    row = get_empty_index(av)                   
    row['line'] = sentence
    row['word_map'] = word_map
    row['original_line'] = sentence
    #row = replace_names(row, av)
    #row = get_similarity_to_title(title, row)
    row = get_structural_metadata(row, av)
    print('metadata', row)
    
'''
av = get_vars()
for key in av:
	if 'index' in key:
		print('\n\nkey', key, av[key])

'''
'''
sentence = 'first find clause, then find second'
convert_sentence(sentence, av)

to do:
	- fix conjugate
	- plural: 'line': 'firsts finds claus thens finds seconds'
	- unaltered: 'operator': {'first find1 clause, then find4 second'}

defs first [
	'the first element in a countable series'
]
defs clause [
	'(grammar) an expression including a subject and predicate but not constituting a complete sentence'
]
'''

#functions = get_data('system_analysis/maps/functions.json')
#structures = get_data('system_analysis/maps/structures.json')
core_functions = [
    "find",
    "move",
    "embed",
    "filter",
    "build",
    "wrap",
    "change",
    "connect",
    "separate",
    "aim",
    "align",
    "compare",
    "compete",
    "combine",
    "share",
    "activate", 
    "store",
    "return",
    "remove",
    "compress",
    "chain",
    "stack",
    "split"
]
core_attributes = ['dependency', 'importance', 'position']
core_objects = ['function', 'attribute']
function_pairs = set()
object_pairs = set()
attribute_pairs = set()
mixed_pairs = set()
mixed_function_object_pairs = set()
mixed_function_attribute_pairs = set()
mixed_attribute_object_pairs = set()

new_cf_copy = [item for item in core_functions]
new_co_copy = [item for item in core_objects]
new_ca_copy = [item for item in core_attributes]
combinations = itertools.product(core_objects, core_objects)
for cl in combinations:
	object_pairs.add(' '.join(cl))

combinations = itertools.product(core_functions, core_functions)
for cl in combinations:
	function_pairs.add(' '.join(cl))

combinations = itertools.product(core_attributes, core_attributes)
for cl in combinations:
	attribute_pairs.add(' '.join(cl))

''' functions, attributes '''

fa_copy = core_functions
fa_copy.extend(core_attributes)
combinations = itertools.product(fa_copy, fa_copy)

print('new_cf_copy', new_cf_copy)
for cl in combinations:
	ff = [item for item in cl if item in new_cf_copy]
	atf = [item for item in cl if item not in new_cf_copy]
	if len(ff) == 1 and len(atf) == 1:
		mixed_function_attribute_pairs.add(' '.join(cl))

''' attributes, objects '''
ao_copy = core_attributes
ao_copy.extend(core_objects)
combinations = itertools.product(ao_copy, ao_copy)
for cl in combinations:
	of = [item for item in cl if item in new_co_copy]
	af = [item for item in cl if item not in new_co_copy]
	if len(of) == 1 and len(af) == 1:
		mixed_attribute_object_pairs.add(' '.join(cl))

''' functions, objects '''
fo_copy = core_functions
fo_copy.extend(core_objects)
combinations = itertools.product(fo_copy, fo_copy)
for cl in combinations:
	functions_found = [item for item in cl if item in new_cf_copy]
	objects_found = [item for item in cl if item not in new_cf_copy]
	if len(functions_found) == 1 and len(objects_found) == 1:
		mixed_function_object_pairs.add(' '.join(cl))

all_pairs = [item for item in core_functions]
all_pairs.extend(new_co_copy)
all_pairs.extend(new_ca_copy)

combinations = itertools.product(all_pairs, all_pairs)
for cl in combinations:
	mixed_pairs.add(' '.join(cl))

print('\nobject_pairs', object_pairs)
print('\nfunction_pairs', function_pairs)
print('\nattribute_pairs', attribute_pairs)

print('\nmixed_pairs', mixed_pairs)
print('\nmixed_function_attribute_pairs', mixed_function_attribute_pairs)
print('\nmixed_attribute_object_pairs', mixed_attribute_object_pairs)
print('\nmixed_function_object_pairs', mixed_function_object_pairs)

'''
	- in this layer you should have common objects like 'variable' ('attribute change' meaning an attribute with a change function) and 'type' ('attribute combine' meaning an attribute set)
	now we can filter the list to identify certain objects that are more useful

	- iterated versions included more sophisticated objects like:
	'variable' ('attribute change apply' meaning an attribute with a change function that can be applied to it)
	'variable version' ('attribute value change' meaning a change to the attribute value)
	'variable state' ('attribute change position' meaning a specific version of the attribute value)

	this is how we can produce definition routes to an object

	- interpretations of combinations

		- chain of attributes:

			- 'position position'

				- embedding: 'a position of a position'

				- type: 'a position type of position'


		- chain of functions:

			- 'change change':

				- injection: a change applied to a change/a direction to apply a change to a change
				- sequential: change the first way, then change the second way
				- type: an unexpected value in a change, all relevant changes, or the definition of change (a change type added)

				- this function combination could be used to assess change rates, change types, or change ratios
				
			- 'share embed'

				- sequential: share, then embed
				- injection: share the embedding, embed the share
				
				- you could use this function combination for more sophisticated functions like 'deploy' or 'distribute'


		- chain of objects:

			- standard definitions:

				- function attribute:
					- an attribute of a function

				- function function
					- a function that applies to, can be activated by, or can generate a function

				- attribute attribute
					- an attribute that describes an attribute (attribute metadata)

				- attribute function
					- a function that generates or describes an attribute

		- these involve:
			- embedding one object in the other (an attribute of a function means an attribute contained in the function object)
			- applying one object to the other
			- causing/depending on the other
			- one following the other in a sequence
			- one acting as a function on the other, by qualifying/modifying the other ('a change change' = 'a change type of change')

	- mixed combination of functions/objects/attributes 

		- attribute function

			- 'dependency change':
				- injection: a change applied to the dependency or one of its components
				- type: a change applied to all dependencies or the definition of dependencies
				- sequential: change the dependency attribute (to something else) 
					- which, given its definition, could mean a reversal of cause (a related object of dependencies), or a type change (to another attribute or converting it to a function)

		- function attribute object 

			- 'change position tree' could refer to:
				- an object: 'a tree storing change positions'
				- a function: 'change the position tree'
				- an attribute: 'a tree attribute of the change position object'


	- how could you identify useful objects like a pattern intersection, an unenforced rule, or an attribute alignment, once you generate the set of n-degree combinations of core components?

	- an 'unenforced rule' is an 'attribute object' and would have the definition combinations:

		- 'subset rule' (a partially implemented rule)
		- 'function without limit' or 'function without filter' (a rule without validation)
		- 'intent condition mismatch' (a function whose intent doesnt match the conditions in it)

	- how would you identify that object of an unenforced rule as a particularly important one, even if you didnt know that it was causing errors?

		- first you would try to identify which structures of the 'subset rule' are valid

			- valid in this context means "what is 'subset rule' referring to" - a partially implemented rule, or a subset of the complete rule

			- system analysis questions about the generated 'subset rule' object:

				- intent: what are subsets used for?

					- does this fall in one of those categories (find, separate, identify)

						- find:
							- given that the 'find' intent could be applied to errors (a related function object), is there an error in the subset

						- identify:
							- is there something unique about the subset

						- separate:
							- should the subset not interact with the other subset 
							- is the other subset supposed to be derived from this subset
							- what information is lost if the other subset is not stored or derived

					- is it premature to store a subset object separately, without something to find/identify in the set, or a reason to separate the subsets

					- is the other subset automatically stored or is it lost

				- change: how are subsets usually changed?

					- would this ever be restored to the full set
					- are there rules to ensure that will happen

				- definition: is a subset of a rule just another rule set?

					- is there a reason to make a distinction between the subset and the rule


		- the output of that analysis should include: 'partially implemented function' or 'function with errors' or 'function without validation checks'

		- iterate through the different structures of 'subset rule'

		- then identify the intent of the target output (function)

			- you build a function to automate a process, to reduce non-natural (manmade) errors

		- then youd identify how a 'subset rule' structured as a 'partially implemented function' could happen

			- lack of resources to implement the full rule set to complete a function

		- then youd identify the causes of those ways it could occur

			- lack of planning/organization (adjacent to lack of bias, or randomness)

		- 'injecting randomness into an ordered system' is associated with objects like experiments

		- if the enabled intent of 'subset rule' structure 'partially implemented function' (enabled intent meaning 'function building') is not randomness, there is a mismatch between the objects/attributes of:
			- the 'subset rule' object cause (lack of planning - randomness) 
			- the enabled 'function building' intent (organized ordered processes)

		- a mismatch could be important bc its a common problem type, especially if 'lack of planning' or 'randomness' is a common occurrences 
			(which we'd know if we derived where randomness could occur given its definition)

		- edge case: if your function is to generate randomness, this process would have to examine other metadata, to find that:
			- a partially implemented randomness function (with errors) doesnt generate the target randomness type (evenly distributed output probabilities)


		- the general overview of this method to filter the most important objects in core object combinations is:

			- derive metadata of the core object combination (subset rule) with system analysis
			- find & iterate through structures of core object combination intents (structure in which it would be found, like 'partially implemented function')
			- find & iterate through metadata of structures
				- target intents like 'function-building' have intents like 'reducing manmade error')
				- causes like 'lack of organization'
			- pull any related definitions (randomness definition)
			- iterate through problem types like mismatch, and iterate through metadata of the objects, looking for inconsistencies, assuming that the structure is intentional 
				(youd intentionally implement a 'partially implemented function' in order to do what intents - to 'inject randomness in an ordered system'?
			- check if each problem type instance found is useful in some way (does it generate randomness, and is that the intent of the function?)
			- if not, and if this is an important problem type to avoid, the object 'subset rule' is probably an important specific instance of that problem type 
				('function missing validation', or an 'unenforced rule')
'''

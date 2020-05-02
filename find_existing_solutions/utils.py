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
core_objects = ['function', 'attribute']
function_pairs = set()
object_pairs = set()
mixed_pairs = set()

combinations = itertools.product(core_objects, core_objects)
for cl in combinations:
	object_pairs.add(' '.join(cl))

combinations = itertools.product(core_functions, core_functions)
for cl in combinations:
	function_pairs.add(' '.join(cl))

core_functions.extend(core_objects)
combinations = itertools.product(core_functions, core_functions)
for cl in combinations:
	mixed_pairs.add(' '.join(cl))

print('object_pairs', object_pairs)
print('function_pairs', function_pairs)
print('mixed_pairs', mixed_pairs)

''' 
	- in this layer you should have common objects like 'variable' ('attribute change' meaning an attribute with a change function) and 'type' ('attribute combine' meaning an attribute set)
	now we can filter the list to identify certain objects that are more useful

	- iterated versions included more sophisticated objects like:
	'variable' ('attribute change apply' meaning an attribute with a change function that can be applied to it)
	'variable' ('attribute value change' meaning a change to the attribute value)

	this is how we can produce definition routes to an object

	- various ways to interpret a chain of functions

		- 'change change':

			- injection: a change applied to a change/a direction to apply a change to a change
			- sequential: change the first way, then change the second way
			- type: an unexpected value in a change, all relevant changes, or the definition of change (a change type added)

			- this function combination could be used to assess change rates, change types, or change ratios
			
		- 'share embed'

			- sequential: share, then embed
			- injection: share the embedding, embed the share
			
			- you could use this function combination for more sophisticated functions like 'deploy' or 'distribute'

	- 

'''


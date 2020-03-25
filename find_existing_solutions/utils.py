import os, json
import nltk
from nltk import pos_tag, word_tokenize
from textblob import TextBlob, Sentence, Word, WordList
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

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
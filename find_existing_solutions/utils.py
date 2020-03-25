import os, json
import nltk
from nltk import pos_tag, word_tokenize
from textblob import TextBlob, Sentence, Word, WordList
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

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
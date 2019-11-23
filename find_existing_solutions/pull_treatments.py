# https://libraries.mit.edu/scholarly/publishing/apis-for-scholarly-resources/

# https://dev.elsevier.com/sd_apis.html

'''
https://www.mediawiki.org/wiki/REST_API
https://en.wikipedia.org/api/rest_v1/page/summary/Stack_Overflow
http://export.arxiv.org/api/query?search_query=all:electron
ftp://ftp.ncbi.nlm.nih.gov/
'''
import os
import urllib
from xml.dom.minidom import parse
import xml.dom.minidom
import requests
import nltk
'''
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download() # first download all the corpuses, then download punkt
nltk.download('punkt')
'''


from nltk.corpus import wordnet
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

# initial output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
# type output should be: ['azole', 'essential oils from plant genus x']
# functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole


''' NAA to Cr ratio ratio is reduced in HIV positive patients 
	and is a marker for HIV infection of the brain even in the absence of 
	imaging findings of HIV encephalopathy or when the patient is symptomatic 
	due to neurological disease of other etiologies.
'''
#['naa', 'cr', 'ratio ratio', 'hiv', 'positive patients', 'neurological disease']
#default noun output should be:
#['naa', 'cr', 'ratio', 'hiv', 'marker', 'infection', 'brain', 'findings', 'encephalopathy', 'patient', 'neurological disease', 'etiologies']


def save(path, data):
	with open(path, 'w') as f:
		f.write(data)
		f.close()

def read(path):
	data = None
	if os.path.exists(path):
		with open(path, 'r') as f:
			data = f.read()
			f.close()
	return data

def get_reason(treatment):
	''' get the reason why this worked or failed, meaning the mechanism of action, 
	so you can do searches for other compounds with similar activity '''

def get_role(treatment):
  ''' for fluconazole, this should be "inhibitor of cyp3a4" '''
  ''' the difference between the role and the reason is the 
  reason is a specific process and the role can be more complex '''

def get_other_treatments_with_role(role, original_treatment):
  ''' find other inhibitors of cyp3a4, in addition to fluconazole '''

def get_known_treatments(condition_keyword):
	''' fetch treatments from research studies '''
	just_summary = True
	articles = pull_all_data(condition_keyword, just_summary)
	return articles

def get_similarity(base_word, new_word):
	#word.synsets # [Synset('octopus.n.01'), Synset('octopus.n.02')]
	new_synsets = Word(new_word).get_synsets(pos=VERB)
	base_synsets = Word(base_word).get_synsets(pos=VERB)
	#Word("octopus").definitions
	return base_synsets.path_similarity(new_synsets)

def get_correlation_of_relationship(line):
	''' this processes a relationship like:
	"this protein activates this gene" or "this compound had a synergistic effect"
	and outputs whether this is a positive association for the condition, 
	meaning it can be used as a treatment, or a meaningless one
	'''
	blob = TextBlob(line)
	print("sentiment", blob.sentiment, "from line", line)#polarity, subjectivity
	return blob.sentiment.polarity

def process_entries(entries, just_summary):
	articles = []
	objects = []
	verbs = set()
	treatments = {'successful': [], 'failed': []}
	for entry in entries:
		for node in entry.childNodes:
			if just_summary is True:
				if node.nodeName == 'summary':
					for subnode in node.childNodes:
						lines = subnode.wholeText.replace('\n', ' ').replace('"', '').replace(',','').split('.')
						for line in lines:
							import re
							line = re.sub(r'\+', '', line.strip())
							line = line + '.'
							print('line', line)
							if line not in articles:
								line_objects = pull_objects_from_doc(line)
								if line_objects:
									new_objects = []
									for ao in line_objects:
										if ao not in objects:
											objects.append(ao)
										if ao not in new_objects:
											new_objects.append(ao)
									relationships = get_relationships(new_objects, line)
									for r in relationships:
										if len(r) > 2:
											verbs.add(r[1])
											correlation = get_correlation_of_relationship(line)
											object_relationship = ' '.join(r)
											print('object relationship', correlation, object_relationship)
											if correlation > 0.1:
												if object_relationship not in treatments['successful']:
													treatments['successful'].append(object_relationship)
											else:
												if object_relationship not in treatments['failed']:
													treatments['failed'].append(object_relationship)
									articles.append(line)
			else:
				article = {'id': '', 'published': '', 'title': '', 'summary': '', 'category': ''}
				if node.nodeName == 'category':
					article[key] = ''.join([node.getAttribute('scheme'), '::', node.getAttribute('term')])
				elif node.nodeName in article:
					article[key] = node.nodeValue
				articles.append(article)
	save('verbs.txt', '\n'.join(verbs))
	save('treatments.txt', '\n'.join(treatments))
	save('objects.txt', '\n'.join(objects))
	save('articles.txt', '\n'.join(articles))
	return articles, objects, treatments

def pull_all_data(keyword, just_summary):
	''' get data from research study api '''
	start = 0
	total_results = 0
	max_results = 10
	page_number = 1
	articles = []
	for i in range(0, page_number):
		url = ''.join(['http://export.arxiv.org/api/query?search_query=all:', keyword, '&start=', str(start), '&max_results=', str(max_results)])
		print('url', url)
		response = requests.get(url)
		DOMTree = xml.dom.minidom.parseString(response.content)
		collection = DOMTree.documentElement #feed
		entries = collection.getElementsByTagName("entry")
		print('entries length', len(entries))
		if total_results == 0:
			results_tag = collection.getElementsByTagName("opensearch:totalResults")
			for r in results_tag:
				total_results = r.nodeValue if r.nodeValue is not None else 10
			page_number = ((total_results - max_results) / max_results) + 1
			print('results count', total_results)
		new_articles = process_entries(entries, just_summary)
		if type(new_articles) == set or type(new_articles) == list:
			for ar in new_articles:
				if ar not in articles:
					articles.append(ar)
		else:
			articles.append(new_articles)
		start = start + len(new_articles)
	return articles

def get_string_from_synset(synset):
	return synset.name().split('.')[0]

def pull_objects_from_doc(line):
    ''' from a research abstract, this should return the treatment, condition, 
    	and inputs/outputs of any functions relating them '''
    print(line)
    ''' also include anything that is not a word for bio data '''
    full_list = []
    for word in line.split(' '):
        word_synsets = Word(word).get_synsets(pos=NOUN)
        if len(word_synsets) > 0:
            ws_string = get_string_from_synset(word_synsets[0])
            print("nouns", ws_string, "from word", word)
            if ws_string in line:
                full_list.append(ws_string)
        else:
            if word.lower() != word:
                full_list.append(word)
    print('full list', full_list)
    return full_list

def get_relationships(objects, line):
    ''' this should identify the relationships between objects identified in 
    	pull_objects_from_doc, standardize them, storing them in a dict '''
    print('get relationships', objects, line)
    ''' returned object should be a three-item list of the acting subject, the verb, and the object acted on:
    line = 'the condition was treated by the chemical'
    return ['chemical', 'treated', 'condition']
    '''
    relationships = []
    blob = TextBlob(line)
    prior_speech = ''
    for word in line.split(' '):
        print('word', word, 'objects', objects)
        synonym = get_synonym(word)
        if synonym:
            print('adding synonym', synonym)
            prior_speech = 'verb'
            #if we found a verb, remove the previous noun from the previous list and start a new one 
            if len(relationships) > 0:
	            last_item = relationships.pop()
	            relationships.append('xxx')
	            relationships.append(last_item)
	            relationships.append(synonym)
        else:
            if word in objects and word not in relationships:
                relationships.append(word)
                #if prior_speech == 'verb':
                    #relationships.append('xxx')
                prior_speech = 'noun'
            #print('could not classify word', word)
    print('relationships', relationships)
    final_list = []
    properties = []
    relationship_list = [r.split('yyy') for r in 'yyy'.join(relationships).split('xxx')]
    for sub_list in relationship_list:
    	new_sub_list = [x for x in sub_list if x != '']
    	if 'be' in new_sub_list:
    		if 'be' == new_sub_list[0]:
    			new_sub_list.remove('be')
    		if len(new_sub_list) > 0:
	    		properties.append(new_sub_list[0]) # get properties like 'is a marker' from the sublist ['be', 'marker']
    	final_list.append(new_sub_list)
    print('properties', properties)
    print('relationship_list', final_list)
	# final_list should look like [ ['chemical', 'caused', 'reaction'], ['experiment', 'was', 'successful'] ]
    #relationship_list [['ratio', 'be', 'reduce', 'positive'], ['be', 'marker'], ['infection', 'brain', 'flush', 'absence'], ['image', 'find', 'patient'], ['be', 'due'], ['disease']]
    # ['ratio'], ['reduce'], ['positive', 'be', 'marker'], ['infection'], ['brain', 'flush'], ['absence'], ['image', 'find'], ['patient', 'be', 'due', 'disease']
    '''
    get relationships 
    ['ratio', 'positive', 'patient', 'marker', 'infection', 'brain', 'absence', 'findings', 'due', 'disease'] 
    NAA to Cr ratio is reduced 
    	in HIV positive patients and
        is a marker for HIV infection of the brain 
            even in the absence of imaging findings of HIV encephalopathy 
            or when the patient is symptomatic due to neurological disease of other etiologies.

    Actually you should be identifying core objects: patient, condition, symptom, compound & their identifying properties:
    	signal:
    		'naa to cr ratio': 'reduced'
    	condition: 'hiv'
    	compound: ''
    	symptoms: 
    		'encephalopathy': 'no imaging findings'
    		'neurological disease': 'other'
    	patient: ['HIV-positive', 'symptomatic', 'has neurological disease']
    '''

    return final_list

def is_unique_relationship(relationship, objects):
    ''' check the relationship dict to see if this relationship exists, in a different order or with a different verb '''
    print('relationship', relationship)
    return relationship

def get_synonym(relationship_verb):
    ''' this should standardize a verb like 'enhance' to a verb like 'increase' '''
    print('get synonym', relationship_verb)
    synonyms = Word(relationship_verb).get_synsets(pos=VERB)
    for s in synonyms:
        standard_relationships.append(s.name().split('.')[0])
        #if h.name() in standard_relationships:
        return s.name().split('.')[0]
    return False

# store common relationship types in verbs.txt
standard_relationships = read('verbs.txt')
standard_relationships = [] #if standard_relationships is None else standard_relationships
treatments = get_known_treatments('meningitis')
print('standard_relationships', standard_relationships)
save('verbs.txt', '\n'.join(standard_relationships))


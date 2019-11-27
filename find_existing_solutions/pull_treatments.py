# https://libraries.mit.edu/scholarly/publishing/apis-for-scholarly-resources/

# https://dev.elsevier.com/sd_apis.html

#python3 pull_treatments.py --metadata "all" --condition "diabetes"

import sys 
for arg in sys.argv:
	print(arg)

# metadata options include: 'properties', 'functions', 'contraindications', 'side effects', 'interactions', 'symptoms', 'conditions', 'all'
# condition param should be scientific name of condition as used in science research studies
# symptom param will be supported in future

''' make table of useful patterns as you pull data, replacing common objects with abstract type keywords:

Example:
	Cytotoxicity in cancer cells
	anti-tumor
	suppress/interfere/inhibit activity of carcinog/canc/tum

Patterns:
	<component object>-toxicity
	anti-<component object of illness>
	suppress/interfere/inhibit activity of drug/medication/enzyme
'''

'''
https://www.mediawiki.org/wiki/REST_API
https://en.wikipedia.org/api/rest_v1/page/summary/Stack_Overflow
http://export.arxiv.org/api/query?search_query=all:electron
ftp://ftp.ncbi.nlm.nih.gov/
'''
import os
import re
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

nltk.download() 
# first download all the corpuses by running nltk.download() and selecting it manually in the gui that pops up, 
# then download punkt
nltk.download('punkt')
'''

''' test cases
	-  identify the processes & bio markers related to the condition as you go through search results so you can do secondary searches
		- target metric to inhibit/increase
		- cooperative metrics: synergistic compounds that enhance the effect of drugs without debilitating side effects
			- search for these & the stressors that deactivate/activate them
			Example: MUC1 - bacteria exposed to a split tail activates it
		- antagonistic metrics: any compounds that can neutralize the drug & the supplements/foods that contain them
			- get these inhibitors by looking up existing treatment pharmacokinetics/dynamics & interactions
				- search for inhibit, induce, substrate
				- check for synergistic effects & any effects that prevent the drug from being metabolized, which may be required to activate it
				- once you find a treatment, you need to check it against context provided by user to filter the list of treatments or style it differently
		- metrics further up the causal stack 
			- if you decrease hunger, diabetes doesnt happen, which is also a treatment (fasting)

I. diabetes 

	- treatments should include: 
		- amylase & glucosidase inhibitors (caffeoyl, galloyl, and prenyl groups)
		- berberine
		- carb blockers like white kidney bean extract
		- insulin
		- fasting
		- sweet defeat (sugar taste blockers)
		- as well as any compounds that can target the processes/receptors involved (ghrelin, metabolism, dopamine, GLUT-4 receptor) 

	- treatment strategies should include:
		- inhibit glucose absorption 
		- insulin-mimicking activity
		- enhanced glucose uptake
		- regulation of insulin signaling pathways
		- translocation of GLUT-4 receptor 
		- activation of the PPARγ

II. fungal meningitis 

	- treatments should include:
		- carvacrol, thymol, eugenol
		- sertraline
		- ecgc
		- inhibitors of CYP2C9, CYP2C19, CYP3A4 
		- azole drugs
		- any other substances that can bind to the fungal cell membrane or process ergosterol into something harmless

	- treatment strategies should include:
		- convert ergosterol to vitamin d
		- bind to ergosterol to break fungal cell membrane

	- insights should include:
		- inhibits [cytochrome p450] enzyme [14α-demethylase] in fungus but not mammals
		- inhibiting [cytochrome p450] enzyme [14α-demethylase] prevents production of ergosterol from lanosterol & accumulation of [14α-methyl] sterols
		- ergosterol is a required input of the fungal cell membrane
		- breaking cell components [membranes] is a way to kill an organism
		- once you break the membrane, your system can handle the components of the cell
		- required inputs (enzymes) to inputs (ergosterol) of object components [cell membranes] are a key target to break those components
			(this insight should already exist in your insight db without those specifics)
		- some natural processes break cell membranes

	- standard system analysis questions should include:
		- what are the limits of your system handling broken fungal cells?
		- does combination therapy work (convert ergosterol to vitamin d & prevent ergosterol production) without system damage?

	- drug attributes should include:
		- fungistatic
		- fungicidal (cryptococcus)

III. cancer

	- relevant processes/attributes/systems:
		- communication, stressor distribution, & boundaries
		- immune system 
		- system & process error types

	- treatments should include:
		- anthrax for bladder cancer
		- known cancer drugs

	- treatment strategies should include:
	  	- promote circulation in the organ (like caffeoquinone acid in the liver) to increasee cell communication, or push them to a place with greater blood flow or cell communication
	  	- identity set of stressors to activate helpful cell division
	  	- need a way to detect tumors using existing bio metrics
	  	- isolate tumors with a compound that they will interpret as the boundary of the host so they dont replicate further
	  	- make a list of anti-inflammatories & fit them to the stressor model
	  	- determine which organisms can borrow genes & look for link to cancer
	  	- determine the ratio of stress that optimizes learning without killing the host; ideally the solution would use the extra cell division potential to make useful cells
	  	- make a list of the common types of error the immune system makes (h pylori, cancer) & figure out if adjusting immune system function is the best layer to attack from
'''

from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

custom_removal = ['the', ',', '.']
# to do: get full list of keywords
keywords = {
    'conditions': ['with', 'having', 'suffering', '-positive', '-negative', 'patients', 'disease', 'disorder', 'dysfunction', 'affects', '-a', '-al', '-pathy', '-emia', '-itis' ],
    'symptoms': ['experience', 'patient', 'afflicted', 'affected', 'population', 'demographic', 'subject', 'test subject', 'volunteer'],
    'compounds': ['-azole', '-ol', 'acid', '-oic', '-ase', '-ose', '-id', '-ein', '-ate', '-ite', 'supplement', 'solution', 'tincture', 'assay', 'mixture'],
    'metric': ['ratio', 'degree', 'ml', 'g', 'oz', 'mg', 'mm', 'ph', 'test']
}

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

def get_strategy(treatment):
    ''' get the strategy explaining why this worked or failed, meaning the mechanism of action, 
    so you can do searches for other compounds with similar activity '''
    # initial treatment output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
    # type output should be: ['azole', 'essential oils from plant genus x']
    # functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole

def get_role(treatment):
  ''' for fluconazole, this should be: "antifungal", "inhibitor of cyp3a4" '''
  ''' the difference between the role and the reason is the 
  reason is a specific process and the role can be more complex & abstract if it has cross-system effects '''

def get_other_treatments_with_role(role, original_treatment):
  ''' find other inhibitors of cyp3a4, in addition to fluconazole '''

def get_known_treatments(condition_keyword):
    ''' fetch treatments from research studies '''
    data = {
    'conditions': [],
    'symptoms': [],
    'compounds': [],
    'treatments': {'successful': [], 'failed': []},
    'metadata': [],
    'objects': [],
    'metric': [],
    'insights': [],
    'verbs': set()
}
    just_summary = True
    articles, data = pull_all_data(condition_keyword, just_summary, data)
    return data

def get_similarity(base_word, new_word):
    #word.synsets # [Synset('octopus.n.01'), Synset('octopus.n.02')]
    new_synsets = Word(new_word).get_synsets(pos=VERB)
    base_synsets = Word(base_word).get_synsets(pos=VERB)
    #Word("octopus").definitions
    return base_synsets.path_similarity(new_synsets)

def get_correlation_of_relationship(line):
    ''' this will process a relationship like:
    "this protein activates this gene" or "this compound had a synergistic effect"
    and outputs whether this is a positive association for the condition, 
    meaning it can be used as a treatment, or a meaningless one
    - "prevents production" => reduce
    '''
    blob = TextBlob(line)
    print("sentiment", blob.sentiment, "from line", line) #polarity, subjectivity
    return blob.sentiment.polarity

def get_metadata(line, data):
    '''
    NAA to Cr ratio 
        is reduced in HIV positive patients and
        is a marker for HIV infection of the brain 
            even in the absence of imaging findings of HIV encephalopathy 
            or when the patient is symptomatic due to neurological disease of other etiologies.

    Actually you should be identifying core objects: patient, condition, symptom, compound & their identifying properties:
        metric:
            'naa to cr ratio': 'reduced'
        condition: 'hiv', 'encephalopathy'
        organs: 'brain'
        compounds: ''
        insights:
            'naa-to-cr ratio is reduced in hiv patients', 
            'naa-to-cr ratio is a marker for hiv brain infection'
        symptoms: 
            'encephalopathy': 'no imaging findings'
            'neurological disease': 'other'
        patient: ['HIV-positive', 'symptomatic', 'has neurological disease']
    sentence = {
        'metric': get_metric(line),
        'condition': get_conditions(line),
        'symptoms': get_symptoms(line),
        'compounds': get_compounds(line)
    }
    '''
    
    ''' within conditions, you need to find the primary condition being studied, 
    to differentiate from other conditions or complications mentioned '''
    filtered_sentence = ' '.join([w for w in line.lower().split(' ') if w not in stopwords.words('english')])
    filtered_sentence = ' '.join([w for w in filtered_sentence.lower().split(' ') if w not in custom_removal])
    print('filtered sentence', filtered_sentence)
    # to do: add filtering to skip sentences without any symptoms or bio metrics, like:
    # The meningitis belt is a region in sub-Saharan Africa where annual outbreaks of meningitis occur with large epidemics observed cyclically.
    ''' NAA Cr ratio ratio reduced HIV positive patients marker HIV infection brain even absence imaging findings HIV encephalopathy patient symptomatic due neurological disease etiologies '''
    de_duplicated_sentence = remove_duplicates(filtered_sentence)
    formatted_line = de_duplicated_sentence.replace(',', '')
    line_objects = pull_objects(formatted_line)
    blob = TextBlob(formatted_line)
    print('phrases', blob.noun_phrases)
    # to do: process suffixes/prefixes with dash character
    data = update_data(blob.noun_phrases, data)
    print('data', data)
    verbs = get_verbs(formatted_line)
    print('verbs', verbs)
    relationships = get_relationships_from_verbs(verbs)
    data = update_data(relationships, data)
    print('relationships', relationships)
    data['insights'] = relationships # to do: add filtering of insights
    print('data', data)
    return data

def update_data(elements, data):
    order_of_keywords = ['conditions', 'symptoms', 'compounds', 'metric']
    for r in elements:
        for keyword_type in order_of_keywords:
            for k in keywords[keyword_type]:
            	if r not in data[keyword_type]:
	                if k in r:
	                    #r = r[2:] # remove subject & verb in first two positions
	                    data[keyword_type].append(r)
	                else:
	                    if '-' in k:
	                        adjusted_k = k.replace('-', '')
	                        for word in r.split(' '):
	                        	# to do: add prefix/suffix processing to ensure adjusted_k is first/last string in list
	                            if len(word.split(adjusted_k)) > 1:
	                                data[keyword_type].append(r)
    return data

def get_relationships_from_verbs(verbs):
    relationships = []
    for verb in verbs:
        phrase = verbs[verb]
        objects = pull_objects(' '.join(phrase))
        relationship = verbs['subject']
        if verb != 'subject':
            relationship.append(verb)
        for o in objects:
            if o not in relationship:
                relationship.append(o)
        relationship_string = ' '.join(relationship)
        if relationship_string not in relationships:
            relationships.append(relationship_string)
    return relationships

def get_verbs(line):
    verb_dict = {'subject': []}
    current_verb = 'subject'
    for word in line.split(' '):
        synonyms = Word(word).get_synsets(pos=VERB)
        if synonyms:
            for s in synonyms:
                verb_dict[word] = []
                current_verb = word
                verb_dict[current_verb] = []
        else:
            verb_dict[current_verb].append(word)
    return verb_dict

def remove_duplicates(line):
    word_list = []
    if type(line) == list:
    	for x in line:
    		if x not in word_list:
    			word_list.append(x)
    	return word_list
    else:
	    for x in line.split(' '):
	        if x not in word_list:
	            word_list.append(x)
    	return ' '.join(word_list)
    return False

def process_entries(condition_keyword, entries, just_summary, data):
    articles = []
    for entry in entries:
        for node in entry.childNodes:
            if just_summary is True:
                if node.nodeName == 'summary':
                    for subnode in node.childNodes:
                        lines = subnode.wholeText.replace('\n', ' ').replace('"', '').split('.') #taking comma out here removes lists embedded in sentences
                        for line in lines:
                            line = re.sub(r'\+', '', line.strip())
                            line = line + '.'
                            print('line', line)
                            if line not in articles:
                                line, data = process_line(line, data) #standard nlp
                                data = get_metadata(line, data) #custom analysis
                                articles.append(line)
            else:
                article = {'id': '', 'published': '', 'title': '', 'summary': '', 'category': ''}
                if node.nodeName == 'category':
                    article[key] = ''.join([node.getAttribute('scheme'), '::', node.getAttribute('term')])
                elif node.nodeName in article:
                    article[key] = node.nodeValue
                articles.append(article)

    for datatype in ['verbs', 'treatments', 'objects']:
    	data[datatype] = remove_duplicates(data[datatype])
	for datatype in data['metadata'].keys():
    	data['metadata'][datatype] = remove_duplicates(data['metadata'][datatype])
    print('metadata', data['metadata'])
    print('verbs', data['verbs'])
    print('treatments', data['treatments'])
    print('objects', data['objects'])

    save('verbs.txt', '\n'.join(data['verbs']))
    save('treatments.txt', '\n'.join(data['treatments']))
    save('objects.txt', '\n'.join(data['objects']))
    save('articles.txt', '\n'.join(articles))
    save('metadata.txt', '\n'.join(data['metadata']))
    return articles, data

def process_line(line, data):
    filtered_sentence = ' '.join([w for w in line.lower().split(' ') if w not in stopwords.words('english')])
    formatted_line = ' '.join([w for w in filtered_sentence.lower().split(' ') if w not in custom_removal])
    line_objects = pull_objects(formatted_line)
    if line_objects:
        new_objects = []
        for ao in line_objects:
            if ao not in data['objects']:
                data['objects'].append(ao)
            if ao not in new_objects:
                new_objects.append(ao)
        verb_dict = get_verbs(line)
        data['verbs'].extend(verb_dict.keys())
        relationships = get_relationships(new_objects, formatted_line)
        for r in relationships:
            if len(r) > 1:
                correlation = get_correlation_of_relationship(formatted_line)
                object_relationship = ' '.join(r)
                print('object relationship', correlation, object_relationship)
                if correlation > 0.3:
                    if object_relationship not in data['treatments']['successful']:
                        data['treatments']['successful'].append(object_relationship)
                else:
                    if object_relationship not in data['treatments']['failed']:
                        data['treatments']['failed'].append(object_relationship)
    return formatted_line, data


def pull_all_data(keyword, just_summary, data):
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
        new_articles, data = process_entries(keyword, entries, just_summary, data)
        if type(new_articles) == set or type(new_articles) == list:
            for ar in new_articles:
                if ar not in articles:
                    articles.append(ar)
        else:
            articles.append(new_articles)
        start = start + len(new_articles)
    return articles, data

def get_string_from_synset(synset):
    return synset.name().split('.')[0]

def pull_objects(line):
    ''' from a research abstract, this should return the treatment, condition, 
        and inputs/outputs of any functions relating them '''
    print(line)
    ''' also include anything that is not a word for bio data '''
    full_list = []
    for word in line.split(' '):
        word_synsets = Word(word).get_synsets(pos=NOUN)
        if len(word_synsets) > 0:
            ws_string = get_string_from_synset(word_synsets[0])
            if ws_string in line:
                full_list.append(ws_string)
        else:
            if word.lower() != word:
                full_list.append(word) #save proper nouns
    print('nouns full list', full_list)
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
        #print('word', word, 'objects', objects)
        synonym = get_synonym(word)
        if synonym:
            print('adding synonym', word, synonym)
            prior_speech = 'verb'
            #if we found a verb, remove the previous noun from the previous list and start a new one 
            if len(relationships) > 0:
                last_item = relationships.pop()
                relationships.append('----')
                relationships.append(last_item)
                relationships.append(synonym)
        else:
            if word in objects and word not in relationships:
                relationships.append(word)
                #if prior_speech == 'verb':
                    #relationships.append('----')
                prior_speech = 'noun'
            #print('could not classify word', word)
    print('relationships', relationships)
    final_list = []
    properties = []
    relationship_list = [r.split('____') for r in '____'.join(relationships).split('----')]
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
    ''' get relationships 
    ['ratio', 'positive', 'patient', 'marker', 'infection', 'brain', 'absence', 'findings', 'due', 'disease'] 
    '''
    return final_list

def is_unique_relationship(relationship, objects):
    ''' check the relationship dict to see if this relationship exists, in a different order or with a different verb '''
    print('relationship', relationship)
    return relationship

def get_synonym(relationship_verb):
    ''' this should standardize a verb like 'enhance' to a verb like 'increase' '''
    # to do: fix nouns being identified as a verb like belt -> belt_out
    #print('get synonym', relationship_verb)
    synonyms = Word(relationship_verb).get_synsets(pos=VERB)
    for s in synonyms:
        if h.name().split('.')[0] in standard_relationships:
        	return s.name().split('.')[0]
    return relationship_verb

# store common relationship types in verbs.txt
verb_mapping = {
	'increase': ['induce', 'enhance'],
	'decrease': ['inhibit']
}
#standard_relationships = read('verbs.txt')
standard_relationships = ['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate'] #if standard_relationships is None else standard_relationships
treatments = get_known_treatments('meningitis')
print('treatments', treatments)
save('verbs.txt', '\n'.join(standard_relationships))


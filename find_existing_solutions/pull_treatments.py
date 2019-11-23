# https://libraries.mit.edu/scholarly/publishing/apis-for-scholarly-resources/

# https://dev.elsevier.com/sd_apis.html

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
nltk.download() # first download all the corpuses, then download punkt
nltk.download('punkt')
'''
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

custom_removal = ['the', ',', '.']
keywords = {
    'conditions': ['with', 'having', 'suffering', '-positive', '-negative', 'patients', 'disease', 'disorder', 'dysfunction', 'affects', '-a', '-al', '-pathy', '-emia', '-itis' ],
    'symptoms': ['experience', 'patient', 'afflicted', 'affected', 'population', 'demographic', 'subject', 'test subject', 'volunteer'],
    'compounds': ['-azole', '-ol', 'acid', '-oic'],
    'metric': ['ratio', 'mg', 'mm', 'ph', 'test']
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

def get_reason(treatment):
    ''' get the reason why this worked or failed, meaning the mechanism of action, 
    so you can do searches for other compounds with similar activity '''

    # initial treatment output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
    # type output should be: ['azole', 'essential oils from plant genus x']
    # functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole

def get_role(treatment):
  ''' for fluconazole, this should be "inhibitor of cyp3a4" '''
  ''' the difference between the role and the reason is the 
  reason is a specific process and the role can be more complex '''

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
    ''' this processes a relationship like:
    "this protein activates this gene" or "this compound had a synergistic effect"
    and outputs whether this is a positive association for the condition, 
    meaning it can be used as a treatment, or a meaningless one
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
    filtered_sentence = ' '.join([w for w in filtered_sentence.lower().split(' ')if w not in custom_removal])
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
                if k in r and r not in data[keyword_type]:
                    #r = r[2:] # remove subject & verb in first two positions
                    data[keyword_type].append(r)
                else:
                    if '-' in k:
                        adjusted_k = k.replace('-', '')
                        klen = len(adjusted_k) * -1
                        words = r.split(' ')
                        for w in words:
                            if len(w) <= klen:
                                if w[klen] == adjusted_k:
                                    if r not in data[keyword_type]:
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
    for x in line.split(' '):
        if x not in word_list:
            word_list.append(x)
    return ' '.join(word_list)

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
                                line, data = process_line(line, data)
                                data = get_metadata(line, data)
                                articles.append(line)
            else:
                article = {'id': '', 'published': '', 'title': '', 'summary': '', 'category': ''}
                if node.nodeName == 'category':
                    article[key] = ''.join([node.getAttribute('scheme'), '::', node.getAttribute('term')])
                elif node.nodeName in article:
                    article[key] = node.nodeValue
                articles.append(article)
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
        data['verbs'] = verb_dict.keys()
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
    return line, data


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
        standard_relationships.append(s.name().split('.')[0])
        #if h.name() in standard_relationships:
        return s.name().split('.')[0]
    return False

# store common relationship types in verbs.txt
standard_relationships = read('verbs.txt')
standard_relationships = [] #if standard_relationships is None else standard_relationships
treatments = get_known_treatments('meningitis')
print('standard_relationships', standard_relationships)
print('treatments', treatments)
save('verbs.txt', '\n'.join(standard_relationships))


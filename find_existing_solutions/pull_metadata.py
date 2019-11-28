import sys, json, os, re, urllib
from xml.dom.minidom import parse
import xml.dom.minidom
import requests
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

'''
for arg in sys.argv:
    print(arg)
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# download all the corpuses by running nltk.download() & selecting it manually in the gui that pops up, 
nltk.download() 
nltk.download('punkt')
'''

def get_side_effects(treatment, condition, data, patient_data):
    return treatment

def get_symptoms(condition_keyword, data):
    return condition_keyword

def get_treatments(condition_keyword, data):
    ''' fetch treatments from research studies '''
    just_summary = True # this indicates if you want metadata like id, title, & published data or just the summary text
    articles, data = pull_summary_data(condition_keyword, just_summary, data)
    # to do: add other data sources here
    return data

def pull_summary_data(keyword, just_summary, data):
    ''' get data from research study api providing summaries '''
    start = 0
    total_results = 0
    max_results = 10
    page_number = 1
    articles = set()
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
        new_articles, data = process_articles(keyword, entries, just_summary, data)
        if type(new_articles) == set:
            for ar in new_articles:
                if ar not in articles:
                    articles.add(ar)
        else:
            articles.add(new_articles)
        start += max_results
    return articles, data

def process_articles(condition_keyword, entries, just_summary, data):
    articles = set()
    for entry in entries:
        for node in entry.childNodes:
            if just_summary is True:
                if node.nodeName == 'summary':
                    for subnode in node.childNodes:
                        lines = subnode.wholeText.replace('\n', ' ').replace('"', '').split('.') #taking comma out here removes lists embedded in sentences
                        for line in lines:
                            line = re.sub(r'\+', '', line.strip())
                            line = line + '.'
                            print('process_articles line', line)
                            if line not in articles:
                                line, data = get_specific_objects(line, data) #standard nlp
                                data = get_metadata(line, data) #custom analysis
                                articles.add(line)
            else:
                article = {'id': '', 'published': '', 'title': '', 'summary': '', 'category': ''}
                if node.nodeName == 'category':
                    article[key] = ''.join([node.getAttribute('scheme'), '::', node.getAttribute('term')])
                elif node.nodeName in article:
                    article[key] = node.nodeValue
                articles.add(article)
    #for datatype in ['verbs', 'treatments', 'objects']:
    #    data[datatype] = remove_duplicates(data[datatype])
    # to do: add semantic & keyword equivalence checks to remove_duplicates
    for key in data:
        print(key, type(data[key]), data[key])
        data_list = []
        data_string = ''
        if type(data[key]) == list:
            for sub_list in data[key]:
                if type(sub_list) == list:
                    for x in sub_list:
                        data_list.append(x)
        if len(data_list) > 0:
        	data_string = '\n'.join(data_list)
        elif type(data[key]) == str:
            data_string = data[key]
        else:
            data_string = '\n'.join(data[key])
        save(''.join([key, '.txt']), data_string)
    return articles, data

def get_specific_objects(line, data):
    '''
    this function is a supplement to get_metadata, 
    which fetches conceptual metadata like insights & strategies
    this function determines conditions, symptoms, & treatments in the sentence 
    '''
    formatted_line = ' '.join([w for w in line.lower().split(' ') if w not in stopwords.words('english') and w not in custom_removal])
    formatted_line = remove_duplicates(formatted_line)
    print('get_specific_objects: de-duplicated sentence', formatted_line)
    line_objects = pull_objects(formatted_line)
    if line_objects:
        for ao in line_objects:
            data['objects'].add(ao)
        verb_dict = get_verbs(line)
        for key in verb_dict.keys():
            data['verbs'].add(key)
        new_relationships = get_relationships(line_objects, formatted_line)
        data['relationships'].extend(new_relationships)
        for r in new_relationships:
            if len(r) > 1:
                object_relationship = ' '.join(r)
                correlation = get_correlation_of_relationship(object_relationship)
                print('object relationship', correlation, object_relationship)
                if correlation > 0.3:
                    if object_relationship not in data['treatments']['successful']:
                        data['treatments']['successful'].add(object_relationship)
                else:
                    if object_relationship not in data['treatments']['failed']:
                        data['treatments']['failed'].add(object_relationship)
    return formatted_line, data

def pull_objects(line):
    ''' - this should return the treatment, condition, 
        & other key elements like inputs/outputs of functions relating them 
        - also include anything that is not a word or a verb for bio data '''
    full_list = set()
    word_set = line.split(' ') if type(line) == str else line
    for word in word_set:
        noun_synsets = Word(word).get_synsets(pos=NOUN)
        verb_synsets = Word(word).get_synsets(pos=VERB)
        if len(verb_synsets) == 0:
            if len(noun_synsets) > 0:
                ws_string = get_string_from_synset(noun_synsets[0])
                if ws_string in line:
                    full_list.add(ws_string)
            else:
                if word.lower() != word:
                    full_list.add(word) #save proper nouns
    print('pull_objects', full_list, line)
    return full_list

def get_metadata(line, data):
    ''' 
    this function is a supplement to get_specific_objects, 
    which fetches condition, symptom, & treatment metadata,
    while this function fetches conceptual metadata like strategies & insights
    '''

    ''' to do: 
        - add filtering to skip sentences without any symptoms or bio metrics, like:
            "The meningitis belt is a region in sub-Saharan Africa where annual outbreaks of meningitis occur with large epidemics observed cyclically."
        - add filtering of insights to apply directly to the condition or mechanisms involved
        - add standardization of acronyms using search with keywords so you get n-acetylaspartic acid from naa and creatine from cr
        - find the primary condition being studied to differentiate from other conditions or complications mentioned 
        - add mechanisms of action keywords & patterns to get strategies
        - use sentence tree analysis to do more advanced processing on semantics http://www.nltk.org/book/ch08.html#ex-elephant
            NAA to Cr ratio 
                is reduced in HIV positive patients and
                is a marker for HIV infection of the brain 
                       even in the absence of imaging findings of HIV encephalopathy 
                         or when the patient is symptomatic due to neurological disease of other etiologies.
    '''

    ''' data = {
            metrics: {'naa-cr ratio': 'reduced'}
            conditions: 'hiv', 'encephalopathy'
            organs: ['brain', 'immune system']
            compounds: ['naa', 'cr']
            insights: [
                'naa-to-cr ratio is reduced in hiv patients', 
                'naa-to-cr ratio is a marker for hiv brain infection'
            ]
            strategies: [
                'target bio markers that change with illness for testing',
                'consider other conditions like lack/excess of signals from diagnostic tests & interfering diseases'
            ]
            symptoms: [
                'encephalopathy': 'no imaging findings'
                'neurological disease': 'other'
            ]
            patient: ['HIV-positive', 'symptoms of neurological disease']
        }
    '''
    ''' NAA Cr ratio reduced HIV positive patients marker infection brain even absence imaging findings encephalopathy patient symptomatic due neurological disease etiologies '''
    formatted_line = line.replace(',', '') 
    # commas can be used to identify clauses, but you want to remove as many words as possible without changing the meaning
    # line_objects = pull_objects(formatted_line)
    blob = TextBlob(formatted_line)
    print('get_metadata: phrases', blob.noun_phrases)
    data = update_index(blob.noun_phrases, data)
    print('get_metadata: data', data)
    verbs = get_verbs(formatted_line)
    print('get_metadata: verbs', verbs)
    relationships = get_relationships_from_verbs(verbs)
    print('get_metadata: relationships', relationships)
    data = update_index(relationships, data)
    print('get_metadata: data', data)
    data['insights'] = relationships
    mechanisms = get_mechanisms_of_action(relationships)
    data['strategies'] = mechanisms
    print('get_metadata: data', data)
    return data

def update_index(elements, data):
    ''' this function checks elements for any matches with keywords &
     adds any matching elements to the data dict to create an index of 
     these categories for this condition query '''

    ''' grab surrounding keywords & check if they need to be added to stopwords
     to do: 
     - add more advanced analysis for linguistic patterns of symptoms 'fever that gets worse when x'
     - add prefix/suffix processing to ensure k is in the right position of word
     - add regex for numerically indexed prefixes like 14alpha-
    '''
    for r in elements:
        for keyword_type in ['conditions', 'symptoms', 'compounds', 'metrics']:
            for k in keywords[keyword_type]:
                position = 'suffix' if '-' == k[0] else 'prefix' if '-' == k[len(k) - 1] else 'other'
                k = k.replace('-', '') if '-' in k else k
                split_element = r if type(r) == set else r.split(' ')
                for i, word in enumerate(split_element):
                    if (
                        (position == 'suffix' and k == word[len(word) - 1 - len(k) : len(word) - 1]) or 
                        (position == 'prefix' and k == word[0:len(k)])
                    ):
                        data[keyword_type].add(word)
                    elif k in word:                        
                        if i > 0 and split_element[i - 1] not in data[keyword_type]:
                            data[keyword_type].add(split_element[i - 1])
                        if split_element[i] not in data[keyword_type]:
                            data[keyword_type].add(split_element[i])
                        if i < (len(split_element) - 1) and split_element[i + 1] not in data[keyword_type]:
                            data[keyword_type].add(split_element[i + 1])
                # data = fit_patterns(split_element, data) 
    return data

def get_metrics(line):
    ''' find any metrics in this line
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information '''
    metrics = set()
    split_line = line.split(' ')
    for key in keywords['metrics']:
        if key in line:
            for i, word in enumerate(split_line):
                if word == key or key in word:
                    numbers = word.replace(key, '')
                    if int(numbers):
                        metrics.add(word) # '3mg'
                    else:
                        # get previous word '3 mg'
                        previous_word = split_line[i - 1]
                        if int(previous_word):
                            metrics.add(previous_word)
    return metrics

def get_strategy(treatment):
    ''' get the strategy explaining why this worked or failed, meaning the mechanism of action, 
    so you can do searches for other compounds with similar activity '''
    # initial treatment output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
    # type output should be: ['azole', 'essential oils from plant genus x']
    # functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole
    return treatment

def get_role(treatment):
  ''' for fluconazole, this should be: "antifungal", "inhibitor of cyp3a4" '''
  ''' the difference between the role and the reason is the 
  reason is a specific process and the role can be more complex & abstract if it has cross-system effects '''
  return treatment

def get_other_treatments_with_role(role, original_treatment):
  ''' find other inhibitors of cyp3a4, in addition to fluconazole '''
  other_treatments = set()
  return other_treatments

def is_valid(smile_formula):
    '''
    check apis with formula search from:
    https://cactus.nci.nih.gov/links/chem_www.html
    '''
    return False

def get_similarity(base_word, new_word):
    #word.synsets # [Synset('octopus.n.01'), Synset('octopus.n.02')]
    # to do: validate synsets are found
    new_synsets = Word(new_word).get_synsets(pos=VERB)
    base_synsets = Word(base_word).get_synsets(pos=VERB)
    print('get similarity', new_synsets, base_synsets, dir(new_synsets))
    #Word("octopus").definitions
    return base_synsets.path_similarity(new_synsets)

def get_correlation_of_relationship(line):
    ''' this will process a relationship like:
    "this protein activates this gene" or "this compound had a synergistic effect"
    and outputs whether this is a positive association for the condition, 
    meaning it can be used as a treatment, or a meaningless one
    - "prevents production" => reduce
    '''
    line_string = ' '.join(line) if type(line) != str else line
    blob = TextBlob(line_string)
    print("sentiment", blob.sentiment, "from line", line) #polarity, subjectivity
    return blob.sentiment.polarity

def get_part_of_speech(word):
    return word

def filter_sentence(line):
    ''' remove as many words as possible '''
    return line

def get_relationships(objects, line):
    ''' this should identify relationships between objects from pull_objects, standardize them, & store them in a dict '''
    ''' response object should be a minimal list of the acting subject, verb, and object acted on:
    line = 'the condition was treated by the chemical'
    return ['chemical', 'treated', 'condition']
    '''
    print('get relationships', objects, line)
    line_string = ' '.join(line) if type(line) != str else line
    line_string = line_string.replace('.', '').replace(',','')
    relationships = set()
    final_list = []
    properties = []
    prior_speech = ''
    for word in line_string.split(' '):
        pos = get_part_of_speech(word)
        synonym = get_standard_verb(word)
        if synonym:
            prior_speech = 'verb'
            #if we found a verb, remove the previous noun from the previous list and start a new one 
            if len(relationships) > 0:
                last_item = relationships.pop()
                relationships.add('----')
                relationships.add(last_item)
                relationships.add(synonym)
        else:
            if word in objects and word not in relationships:
                relationships.add(word)
                #if prior_speech == 'verb':
                    #relationships.add('----')
                prior_speech = 'noun'
            #print('could not classify word', word)
    print('relationships', relationships)
    relationship_list = [r.split('____') for r in '____'.join(relationships).split('----')]
    for sub_list in relationship_list:
        new_sub_set = [x for x in sub_list if x != '']
        if 'be' in new_sub_set:
            if 'be' == new_sub_set[0]:
                new_sub_set.remove('be')
            if len(new_sub_set) > 0:
                properties.append(new_sub_set[0]) # get properties like 'is a marker' from the sublist ['be', 'marker']
        if len(new_sub_set) > 1:
            final_list.append(new_sub_set)
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

def get_relationships_from_verbs(verbs):
    relationships = set()
    for verb in verbs:
        phrase = verbs[verb]
        objects = pull_objects(' '.join(phrase))
        relationship = set(verbs['subject'])
        if verb != 'subject':
            relationship.add(verb)
        for o in objects:
            relationship.add(o)
        relationships.add(' '.join(relationship))
    return relationships

def get_standard_verb(relationship_verb):
    ''' this should standardize a verb like 'enhance' to a verb like 'increase' '''
    # to do: fix nouns being identified as a verb like belt -> belt_out
    #print('get synonym', relationship_verb)
    synonym_set = Word(relationship_verb).get_synsets(pos=VERB)
    if len(synonym_set) > 0:
        counts = {}
        for s in synonym_set:
            sname = s.name().split('.')[0]
            if sname in counts:
                counts[sname] += 1
            else:
                counts[sname] = 1
        count_values = [counts[x] for x in counts]
        max_value = max(count_values)
        max_synonyms = [c for c in counts if counts[c] == max_value]
        if len(max_synonyms) > 1:
            for ms in max_synonyms:
                '''
                supported_synonyms has synonyms of common functions like increase, enhance, activate
                standard_relationships has common verbs found in medical abstracts
                '''
                if ms in supported_synonyms or ms in standard_relationships:
                    return ms
            print('not in supported synonyms or standard relationships', ms, max_synonyms[0])
            return max_synonyms[0]
    return False

def get_verbs(line):
    verb_dict = {'subject': set()}
    current_verb = 'subject'
    for word in line.split(' '):
        is_a_verb = Word(word).get_synsets(pos=VERB)
        print('checking if is a verb', is_a_verb, word)
        if len(is_a_verb) > 0:
            current_verb = word
            verb_dict[current_verb] = set()
        verb_dict[current_verb].add(word)
    return verb_dict

def save(path, data):
    with open(path, 'w') as f:
        if 'json' in path:
            json.dump(data)
        else:
            f.write(data)
        f.close()
    return True

def read(path):
    data = None
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f) if 'json' in path else f.read()
            f.close()
    return data

def remove_duplicates(line):
    if type(line) == str:
        return ' '.join(set(x for x in line.split(' ')))
    else:
        return set(x for x in line.split(' '))

def get_string_from_synset(synset):
    return synset.name().split('.')[0]

def get_mechanisms_of_action(relationships):
    ''' get any relationships which are also mechanisms of action '''
    return relationships 
    
def fit_patterns(elements, data):
    ''' this function looks for matches in elements with basic keyword patterns like alpha-<compound>-ic acid '''
    return data

options = [
    'properties', 'treatments', 'contraindications', 'metrics',
    'side effects', 'interactions', 'symptoms', 'conditions', 
    'functions', 'insights', 'strategies', 'patterns', 'all'
]
custom_removal = ['the', ',', '.', 'a', 'an', 'them', 'they']

# to do: get full list of keywords

keywords = {
    'conditions': ['with', 'having', 'suffering', '-positive', '-negative', 'patients', 'disease', 'disorder', 'dysfunction', 'affects', '-a', '-al', '-pathy', '-emia', '-itis' ],
    'symptoms': ['experience', 'patient', 'afflicted', 'affected', 'population', 'demographic', 'subject', 'test subject', 'volunteer'],
    'compounds': ['-azole', '-ol', 'acid', '-oic', '-ase', '-ose', '-id', '-ein', '-ate', '-ite', 'supplement', 'solution', 'tincture', 'assay', 'mixture'],
    'metrics': ['ratio', 'degree', 'ml', 'g', 'oz', 'mg', 'gram', 'mm', 'ph', 'test']
}

# this model isolates treatments from symptoms, metrics, etc - so make sure treatments contain that data or a reference to it
data = {
    'verbs': set(), # set of relationship verbs in the data set
    'objects': set(), # nouns like the name of condition, name of treatment, etc
    'relationships': [],
    'conditions': set(),
    'patient_data': {
        'conditions': set(),
        'symptoms': set(),
        'metrics': set()
    }, # this is where you can store info about patient states for use with bio-metric params
    'symptoms': set(),
    'compounds': set(),
    'metrics': set(), # metric used to measure effectiveness of treatment
    'treatments': {'successful': set(), 'failed': set()},
    'patterns': set(),
    'functions': set(),
    'insights': set(), # useful sentences in data set that have bio rules in them - for abstracts this will likely just be the treatment success sentence
    'strategies': set(), # insights relevant to methods/mechanisms of action/processes or patterns of problem-solving
}
verb_map = read('synonyms.json')
supported_core_functions = verb_map['standard_words'].keys()
supported_synonyms = set()
for x in verb_map['standard_words'].keys():
    for y in verb_map['standard_words'][x]:
        supported_synonyms.add(y)
print('supported_core_functions', supported_core_functions)
print('supported synonyms', supported_synonyms)
verb_contents = read('verbs.txt')
standard_relationships = set(verb_contents.split('\n'))
print('standard relationships', standard_relationships)
relationship_types = ['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable'] #if standard_relationships is None else standard_relationships
treatments = get_treatments('meningitis', data)
print('treatments', treatments)


import sys, json, os, re, urllib, csv
from xml.dom.minidom import parse
import xml.dom.minidom
import requests
# import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize, pos_tag, ne_chunk

from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from utils import get_verbs, get_standard_word, save, read, remove_duplicates, write_csv
from get_index_def import get_empty_index
from get_objects import identify_elements, get_metrics, get_patterns, get_intent, get_strategies, get_functions, get_side_effects, get_types, get_dependencies, get_related_components, get_symptoms, get_treatments, get_mechanisms_of_action, get_index

'''
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# download all the corpuses by running nltk.download() & selecting it manually in the gui that pops up, 
#nltk.download() 
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
'''

def get_entries(source, keyword, start, max_results, total_results):
    url = source['url'].replace('<KEY>', keyword).replace('<START>', str(start)).replace('<MAX>', str(max_results))
    print('url', url)
    response = requests.get(url)
    response_string = xml.dom.minidom.parseString(response.content)
    if response_string:
        if total_results == 0:
            total_results = int(response_string.documentElement.getElementsByTagName(source['results_tag'])[0].childNodes[0].nodeValue)
        entries = response_string.documentElement.getElementsByTagName(source['tag'])
    else:
        entries = json.loads(response.content)
    return entries

def pull_summary_data(sources, metadata, generate_source, generate_target, args, filters):
    ''' get index from research study api providing summaries '''
    print('pull metadata', metadata, args)
    ''' we assume the primary argument comes first - right now only supports one argument'''
    articles = []
    rows = []
    index = get_empty_index(metadata)
    for arg in args:
        for keyword in args[arg]:
            total_results = 0
            max_results = 10
            for source in sources:
                for i in range(0, 10):
                    start = i * max_results
                    if total_results > start or total_results == 0:
                        entries = get_entries(source, keyword, start, max_results, total_results)
                        if len(entries) > 0:
                            for entry in entries:
                                print('\n------- article -------')
                                for node in entry.childNodes:
                                    summary = set()
                                    if node.nodeName == 'title':
                                        for subnode in node.childNodes:
                                            if len(subnode.wholeText) > 0:
                                                print('title', subnode.wholeText)
                                                summary.add(subnode.wholeText)
                                    if node.nodeName == 'summary':
                                        for subnode in node.childNodes:
                                            lines = subnode.wholeText.replace('\n', ' ').replace('"', '').replace('(', '').replace(')', '').split('.') 
                                            #taking comma out here removes lists embedded in sentences
                                            new_lines = []
                                            for i, line in enumerate(lines):
                                                if len(line) > 0:
                                                    if i > 0 and line[0] in numbers:
                                                        line = ''.join([lines[i - 1], line])
                                                        if len(new_lines) > 0:
                                                            new_lines.pop()
                                                    if len(line.replace(' ', '')) > 0:
                                                        new_lines.append(line.strip())
                                            print('lines', new_lines)
                                            for line in new_lines:
                                                line = line.strip()
                                                if ' ' in line and len(line.split(' ')) > 1:
                                                    line = remove_duplicates(line)
                                                    formatted_line = ''.join([x for x in line.lower() if x in alphabet])
                                                    print('\n\tline', formatted_line)
                                                    if len(formatted_line) > 0:
                                                        row = identify_elements(supported_core, formatted_line, None, metadata)
                                                        row = get_medical_objects(line, formatted_line, row, metadata) #standard nlp
                                                        row = { key: str(','.join(val)) for key, val in row.items() }
                                                        #index, row = get_metadata(formatted_line, index, row) #custom analysis
                                                        if row != empty_index:
                                                            print('row', row)
                                                            rows.append(row)
                                                            for key, val in row.items():
                                                                index[key] = index[key].union(set(val.split(','))) if type(val) == str else index[key].union(val)
                                                            print('new index', index)
                                                        summary.add(formatted_line)
                                    if len(summary) > 0:
                                        articles.append('\n'.join(summary))
    if len(articles) > 0:
    	save('data/articles.txt', '\n'.join(articles))
    if len(rows) > 0:
        write_csv(rows, index.keys(), 'data/rows.csv')
        if generate_target == 'all' and generate_source == 'all':
            generate_all_datasets(index.keys(), rows)
    for key in index:
        print('\t\twriting', key, type(index[key]), index[key])
        index_string = index[key] if type(index[key]) == str else '\n'.join(index[key])
        save(''.join(['data/', key, '.txt']), index_string)
    return articles, index, rows

def get_word_type(word):
    ''' look through synonyms to find out which index element contains this word '''
    return word

def get_medical_objects(line, formatted_line, row, metadata):
    '''
    - this function determines conditions, symptoms, & treatments in the sentence 
    - this function is a supplement to get_metadata, 
    which fetches conceptual metadata like insights & strategies

    to do: 
        - add treatment keyword check & add treatment keywords
        - add metadata check to make sure they requested this data
    '''
    row = get_relationships(line, row)
    if len(row['relationships']) > 0:
        for r in row['relationships']:
            '''
            outputs = get_dependencies('outputs', line, relationships, 3)
            row['metrics'] = row['metrics'].union(get_metrics(line))
            row['side_effects'] = row['side_effects'].union(get_side_effects(line)).union(outputs)
            row['symptoms'] = row['symptoms'].union(get_symptoms(line))
            row['treatments'] = row['treatments'].union(get_treatments(line))
            row['mechanisms'] = row['mechanisms'].union(get_mechanisms_of_action(line))
            row['types'] = row['types'].union(get_types(line))
            row['variables'] = row['variables'].union(get_dependencies('inputs', line, row['relationships'], 1))
            row['alternatives'] = get_related_components(line)    
            intent = get_intent(summary)    
            '''
            intent = None
            correlation = get_correlation_of_relationship(intent, r)
            print('\tget_medical_objects: object relationship', correlation, r)
            if correlation > 0.3:
                row['treatments_successful'].add(r)
            else:
                row['treatments_failed'].add(r)
    return row

def get_metadata(line, index, row):
    ''' 
    this function is a supplement to get_specific_objects, 
    which fetches condition, symptom, & treatment metadata,
    while this function fetches conceptual metadata like strategies & insights
    '''
    ''' to do: 
        - add filtering to skip sentences without any symptoms or bio metrics, like:
        - add filtering of insights to apply directly to the condition or mechanisms involved
        - add standardization of acronyms using search with keywords so you get n-acetylaspartic acid from naa and creatine from cr
        - find the primary condition being studied to differentiate from other conditions or complications mentioned 
        - add mechanisms of action keywords & patterns to get strategies
    '''
    '''
    filtered_line = filter_line(line)
    if len(filtered_line) < 3:
        return index
    '''
    row['functions'] = get_functions(row['relationships'])
    row['insights'] = get_insights(row['relationships'])
    row['strategies'] = get_strategies(row['relationships'])
    row['mechanisms'] = get_mechanisms_of_action(row['relationships'])
    index['insights'] = index['insights'].union(row['insights'])
    index['strategies'] = index['strategies'].union(row['mechanisms']).union(row['strategies'])
    return index, row

def get_correlation_of_relationship(intent, line):
    '''
    this will process a relationship like:
    "this protein activates this gene" or "this compound had a synergistic effect"
    & tests if this is a positive association for the condition, so it can be used as a treatment
    '''
    line_string = ' '.join(line) if type(line) != str else line
    #print("\tline sentiment", TextBlob(line_string).sentiment, "line", line)
    if intent:
        print("\tintent sentiment", TextBlob(intent).sentiment, "intent", intent)
    return TextBlob(line_string).sentiment.polarity

def get_success_of_relationship(intent, hypothesis, line):
    '''
    this will process a relationship like:
    "this protein activates this gene" or "this compound had a synergistic effect"
    & tests if this is a positive association for the condition, so it can be used as a treatment

    if the intent is to check for correlation:
        if the hypothesis is "drug reduced blood pressure":
            if the sentence is:
                "drug did not reduce blood pressure"
                that's a negative correlation (failure) or a negative intent (reduce)
            if the sentence is:
                "drug did reduce blood pressure"
                that's a positive correlation (success) or a negative intent (reduce)
    '''
    line_string = ' '.join(line) if type(line) != str else line
    print("\tline sentiment", TextBlob(line_string).sentiment, "line", line)
    print("\tintent sentiment", TextBlob(intent).sentiment, "intent", intent)
    line_sentiment = TextBlob(line_string).sentiment.polarity
    intent_sentiment = TextBlob(intent).sentiment.polarity
    if (line_sentiment - intent_sentiment) < 0.3:
        return True
    return False

def get_relationships(line, row):
    '''
    - this identifies relationships between subject and objects in line
    - the response object should be a list of the acting subject, verb, & object:
    relationships = ['chemical', 'caused', 'reaction'], ['experiment', 'was', 'successful'] ]
    '''
    line = ' '.join(line) if type(line) != str else line
    line = line.replace('.','').replace(',','').replace('(','').replace(')','')
    print('\tget_relationships: line', line)
    tagged = pos_tag(word_tokenize(line))
    print('tagged', tagged)
    common_words = ['patient', 'due', 'disease']
    take_out_pos = ['NNS', 'RB', 'VBG']
    leave_in_pos = ['NN', 'JJ', 'VBP', 'VBD', 'VBN', 'VBZ']
    noun_pos = ['NN']
    verb_pos = [ 'VBP', 'VBD', 'VBN', 'VBZ']
    blob = TextBlob(line)
    phrases = blob.noun_phrases
    print('phrases', phrases)
    relationship = []
    #[('naa', 'JJ'), ('cr', 'NN'), ('ratio', 'NN'), ('reduce', 'VB'), ('hiv', 'NNS'), ('positive', 'JJ'), ('patients', 'NNS'), ('marker', 'VBP'), ('infection', 'NN'), ('brain', 'NN'), ('even', 'RB'), ('absence', 'JJ'), ('image', 'NN'), ('find', 'VBP'), ('conditions', 'NNS'), ('patient', 'JJ'), ('symptomatic', 'JJ'), ('due', 'JJ'), ('conditions', 'NNS'), ('disease', 'VBP'), ('etiology', 'NN')]
    for item in tagged:
        print('item', len(item), item)
        if len(item) == 2:
            if item[0] not in common_words:
                if item[1] in leave_in_pos:
                    relationship.append(item[0])
                if item[1] in noun_pos:
                    row['components'].add(item[0]) # compounds, symptoms, treatments, metrics, conditions, stressors, types, variables
                elif item[1] in verb_pos:
                    row['functions'].add(item[0])
    row['relationships'] = [' '.join(relationship)] # intents, functions, insights, strategies, mechanisms, patterns, systems
    print('relationships', row['relationships'])
    '''
      naa/JJ
      cr/NN
      ratio/NN
        reduced/VBD
      hiv/JJ
      positive/JJ
        marker/VBP
      infection/NN
      brain/NN
      encephalopathy/JJ
      patient/JJ
      symptomatic/JJ
      due/JJ
      neurological/JJ
      disease/NN
    '''
    # now put it through the other noun processor
    for word in row['relationships']:
        verb_synsets = Word(word).get_synsets(pos=VERB)
        noun_synsets = Word(word).get_synsets(pos=NOUN)
        if len(verb_synsets) == 0:
            print('noun', word, noun_synsets)
        else:
            print('verb', word, verb_synsets)
    print('get_relationships: row', row)
    return row

def generate_all_datasets(component_list, rows):
    '''
    iterate through all combinations of elements in rows and 
    generate a dataset for each one to check for relationships
    '''
    combination_list = []
    for i in range(0, len(component_list)):
        new_combination = itertools.combinations(component_list, i)
        print('\tgenerate_all_datasets: generating index set for elements', new_combination, 'to predict', new_combination[-1])
        # this doesnt invalidate target_variable param bc we might not always use it in this function
        generate_dataset(new_combination, new_combination[-1], rows, True)
        combination_list.extend(new_combination)
    print('\tgenerate_all_datasets: combination_list', combination_list)
    #list(zip(bio_component_set, meta_component_set))

def generate_dataset(element_list, rows, write):
    '''
    the intent of this function is to combine two elements like symptoms & conditions into a data set,
    with the goal of exploring all possible prediction relationships between variable sets
    the target_variable is the element youre trying to predict ('condition')
    '''
    dataset = []
    #make sure target variable isnt included in index set except in last position
    for r in rows:
        row = {}
        for field in r:
            if field in element_list:
                row[field] = ','.join(r[field]) if type(r[field]) == set else r[field]
        dataset.add(row)
    filename = ''.join([s[0] for s in element_list]) if len(element_list) > 3 else '_'.join(element_list)
    element_path = ''.join(['datasets/', filename, '.csv'])
    if len(dataset) > 0:
        if write:
            write_csv(rows, element_list, element_path)
        return dataset
    return False

numbers = '0123456789'
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789- '
empty_index = get_empty_index('all')
supported_params = [
    'metadata', 'generate',
    'properties', 'treatments', 'contraindications', 'metrics',
    'side-effects', 'interactions', 'symptoms', 'conditions', 
    'bio-metrics', 'bio-symptoms', 'bio-conditions',
    'components', 'stressors', 'outputs', 'inputs', 'filters',
    'functions', 'insights', 'strategies', 'patterns'
]
metadata_key = ''
generate_source = ''
generate_target = ''
args_index = {}
filters_index = {}
standard_verbs = set(['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable'])
for i, arg in enumerate(sys.argv):
    arg_key = arg.replace('-', '')
    if arg_key in supported_params:
        arg_val = sys.argv[i + 1]
        if arg_key == 'metadata':
            if arg_val in empty_index.keys() or arg_val == 'all':
                metadata_key = arg_val
        elif arg_key == 'filters':
            # --filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
            filters_index = { key: val.split(',') for key, val in arg_val.split(',') } # val will be metricC::metricvalue for metric
        elif arg_key == 'generate':
            generate_list = arg_val.split('::')
            generate_source = generate_list[0].split(',')
            new_source = [s for s in generate_source if s in supported_params]
            generate_source = new_source
            generate_target = generate_list[1]
        else:
            args_index[arg_key] = arg_val.split(',')

print('args_index', args_index)
print('filters', filters_index)
print('metadata', metadata_key)
print('generate', generate_target, generate_source)

sources = [
    {
        'url': 'http://export.arxiv.org/api/query?search_query=all:<KEY>&start=<START>&max_results=<MAX>',
        'results_tag': 'opensearch:totalResults',
        'tag': 'entry'
    }
]

if len(args_index.keys()) == 1:
    word_map = read('synonyms.json')
    supported_core = word_map['standard_words']
    supported_synonyms = set()
    for x in word_map['standard_words'].keys():
        for y in word_map['standard_words'][x]:
            supported_synonyms.add(y)
    for path in ['data', 'datasets']:
        if not os.path.exists(path):
            os.mkdir(path)
    verb_contents = read('data/verbs.txt')
    standard_verbs = set(verb_contents.split('\n')) if verb_contents is not None else standard_verbs
    articles, index, rows = pull_summary_data(sources, metadata_key, generate_source, generate_target, args_index, filters_index)
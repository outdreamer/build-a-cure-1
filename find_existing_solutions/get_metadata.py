import sys, json, os, re, urllib, csv, ssl, random
import wikipedia
from wikipedia.exceptions import DisambiguationError
from xml.dom.minidom import parse
import xml.dom.minidom
import requests
# import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import stopwords

from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from utils import *
from get_index_def import get_empty_index
from get_structure import get_pos, get_structural_metadata
from generate_datasets import generate_datasets 
from get_vars import get_vars, get_args
from get_structural_objects import get_relationships_from_clauses
from get_conceptual_objects import *
from get_medical_objects import *

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

def pull_summary_data(sources, metadata_keys, generate_source, generate_target, args, filters, all_vars):
    ''' get index from research study api providing summaries '''
    print('pull metadata', metadata_keys, 'args', 'generate_source', generate_source, 'generate target', generate_target, args, 'filters', filters)
    ''' we assume the primary argument comes first - right now only supports one argument'''
    metadata_keys = 'all' if metadata_keys == '' else metadata_keys
    articles = []
    rows = []
    empty_index = get_empty_index(metadata_keys, all_vars['full_params'])
    index = get_empty_index(metadata_keys, all_vars['full_params'])
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
                                    title = ''
                                    if node.nodeName == 'title':
                                        for subnode in node.childNodes:
                                            if len(subnode.wholeText) > 0:
                                                title = subnode.wholeText
                                                print('title', title)
                                    if node.nodeName == 'summary':
                                        for subnode in node.childNodes:
                                            text = remove_standard_punctuation(subnode.wholeText)
                                            lines = text.replace('\n', ' ').split('. ') 
                                            #taking comma out here removes lists embedded in sentences
                                            for line in lines:
                                                if ' ' in line and len(line.split(' ')) > 1:
                                                    line = remove_duplicates(line)
                                                    formatted_line = ''.join([x for x in line.lower() if x == ' ' or x in all_vars['alphabet']])
                                                    print('\n\tline', formatted_line)
                                                    if len(formatted_line) > 0:
                                                        #row = identify_elements(all_vars['supported_core'], formatted_line, None, metadata_keys, all_vars['full_params'])
                                                        row = empty_index
                                                        index, row = get_structural_metadata(line, title, lines, text, index, row, metadata_keys, all_vars)
                                                        index, row = get_medical_metadata(line, formatted_line, title, index, row, metadata_keys, all_vars)
                                                        index, row = get_conceptual_metadata(formatted_line, title, index, row, metadata_keys) #custom analysis
                                                        print('row', row)
                                                        if row != empty_index:
                                                            for key, val in row.items():
                                                                if type(val) == dict:
                                                                    val = '::'.join(['_'.join([k,v]) for k,v in val.items()])
                                                                elif type(val) == set or type(val) == list:
                                                                    val = str(','.join(set(val)))
                                                                elif type(val) == bool:
                                                                    val = '1' if val is True else '0'
                                                                if type(index[key]) == set:
                                                                    ''' to do: figure out if you need to handle merging dicts here '''
                                                                    set_val = set(val.split(',')) if ',' in val else set(val)
                                                                    index[key] = index[key].union(set_val)
                                                                row[key] = val
                                                            rows.append(row)
                                                            print('new index', index)
                                                        summary.add(formatted_line)
                                    if len(summary) > 0:
                                        articles.append('\n'.join(summary))
    if len(articles) > 0:
        save('data/articles.txt', '\n'.join(articles))
    if len(rows) > 0:
        write_csv(rows, index.keys(), 'data/rows.csv')
        if generate_source == 'all':
            generate_keys = index.keys()
        else:
            generate_keys = generate_source.split(',')
        datasets = generate_datasets(generate_keys, generate_target, index, rows)
        print('datasets', datasets)
    for key in index:
        print('\t\twriting', key, type(index[key]), index[key])
        index_string = index[key] if type(index[key]) == str else '\n'.join(index[key])
        save(''.join(['data/', key, '.txt']), index_string)
    return articles, index, rows

def get_index_type(word, all_vars, categories):
    ''' look through synonyms to find out which index element contains this word '''
    index_type = None
    full_keys = [
        'condition_keywords', 'state', 'treatment_keywords', 'elements', 'compounds', 'metrics', 
        'organisms', 'functions', 'causal_layers', 'symptom_keywords', 'side_effects'
    ]
    param_map = {}
    for keyword in full_keys:
        keyword = keyword.replace('_keywords', 's')
        param_map[keyword] = keyword
    for keyword in ['condition_keywords', 'state']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'conditions'
    for keyword in ['treatment_keywords', 'elements', 'compounds']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'compounds' 
            # not every compound will be a treatment
    for keyword in ['metrics']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'metrics'
    for keyword in ['organisms']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'organisms'
    for keyword in ['functions', 'causal_layers']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'functions'
    for keyword in ['symptom_keywords', 'side_effects']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'symptoms'
            # assume its a symptom until you can associate it with a compound
    if len(categories) > 0:
        for c in categories:
            c_split = c.split(' ')
            for term in c_split:
                if term in param_map:
                    index_type = param_map[term]
        if not index_type:
            index_type = categories[0]
    return index_type

def get_medical_metadata(line, formatted_line, title, index, row, metadata, all_vars):
    '''
    - this function determines conditions, symptoms, & treatments in the sentence 
    - this function is a supplement to get_metadata, 
      which fetches conceptual metadata like insights & strategies
    to do: 
        - add treatment keyword check & add treatment keywords
        - add metadata check to make sure they requested this data
    '''
    intent = None
    hypothesis = None
    row = get_treatments(intent, hypothesis, line, title, row, metadata, all_vars)
    return index, row

def get_conceptual_metadata(line, title, index, row, metadata_keys):
    ''' 
    this function is a supplement to get_medical_objects, 
    which fetches condition, symptom, & treatment metadata,
    while this function fetches conceptual metadata like types, strategies & insights

    to do: 
        - add filtering to skip sentences without any symptoms or bio metrics, like:
        - add filtering of insights to apply directly to the condition or mechanisms involved
        - add standardization of acronyms using search with keywords so you get n-acetylaspartic acid from naa and creatine from cr
        - find the primary condition being studied to differentiate from other conditions or complications mentioned 
        - add mechanisms of action keywords & patterns to get strategies
    '''

    '''
    output = wikipedia.search(suggested, results=1)
    images_urls = wikipedia.page(suggested).images
    summary = wikipedia.summary(suggested)
    print('summary', summary) 
    '''
    wikipedia.set_lang("en")
    suggested = None
    index_type = None
    leave_in_pos = ['NNS', 'NN', 'NNP', 'NNPS']
    for r in row['relationships']:
        for word in r.split(' '):
            pos = get_pos(word)
            if pos == 'noun':
                ''' make sure this is a noun before querying '''
                if word[0] == word[0].upper() and word[1] != word[1].upper():
                    suggested = get_generic_medication(word)
                suggested = wikipedia.suggest(word) if not suggested else suggested
                print('suggested', suggested, word)
                try:
                    content = wikipedia.page(suggested).content
                    section_list = [s.strip().replace(' ','_').lower() for s in content.split('==') if '.' not in s and len(s) < 100]
                    index['section_list'] = index['section_list'].union(section_list)
                    print('section list', section_list)
                    categories = wikipedia.page(suggested).categories
                    if len(categories) > 0:
                        row['types'] = row['types'].union(set(categories))
                        print('categories', categories)
                        if len(section_list) > 0:
                            ''' use section list to determine type first '''
                            for key, val in all_vars['section_map'].items():
                                for section in section_list:
                                    if key in section:
                                        index_type =  val
                        else:
                            index_type = get_index_type(suggested, all_vars['supported_core'], categories)
                            if index_type:
                                print('found index type', index_type, word)
                                if index_type in row:
                                    if index_type != 'dependencies':
                                        output = get_index_objects(index_type, r)
                                        if output != r:
                                            for k in output:
                                                row[k] = output[k]
                except Exception as e:
                    print('summary exception', e)
    row['dependencies'] = get_dependencies('all', None, row['relationships'], 3)
    return index, row

def get_correlation_of_relationship(intent, line):
    print("\tline sentiment", TextBlob(line).sentiment, "line", line)
    if intent:
        print("\tintent sentiment", TextBlob(intent).sentiment, "intent", intent)
    return get_polarity(line)

def downloads(paths):
    for path in paths:
        if not os.path.exists(path):
            ''' this is the first run so download packages '''
            os.mkdir(path)
            try:
                _create_unverified_https_context = ssl._create_unverified_context
            except AttributeError:
                pass
            else:
                ssl._create_default_https_context = _create_unverified_https_context
            # download all the corpuses by running nltk.download() & selecting it manually in the gui that pops up, 
            nltk.download()
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
            nltk.download('maxent_ne_chunker')
    return True

# common_words = [] # to do: store common words that dont fit other categories & read them into list
# if it doesnt have a word ending in one of these suffixes, its probably not relevant
stemmer = SnowballStemmer("english")
stop = set(stopwords.words('english'))
medical_sentence_terms = ['y', 'ic', 'ia', 'al', 'ment', 'tion'] 
all_vars = get_vars() # replace all subelements with reference
print('supported params', all_vars['supported_params'])
if all_vars:
    done = downloads(['data', 'datasets'])
    if done:
        args_index, filters_index, metadata_keys, generate_target, generate_source = get_args(sys.argv, all_vars)
        if len(args_index.keys()) == 1:
            verb_contents = read('data/verbs.txt')
            standard_verbs = set(['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable'])
            standard_verbs = set(verb_contents.split('\n')) if verb_contents is not None else standard_verbs
            sources = read('sources.json')
            if sources:
                articles, index, rows = pull_summary_data(sources, metadata_keys, generate_source, generate_target, args_index, filters_index, all_vars)
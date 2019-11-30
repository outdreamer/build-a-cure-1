import sys, json, os, re, urllib, csv
from xml.dom.minidom import parse
import xml.dom.minidom
import requests
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from utils import get_verbs, get_standard_word, save, read, remove_duplicates
from get_index_def import get_empty_index
from get_objects import identify_elements, get_metrics, get_patterns, get_intent, get_strategies, get_functions, get_side_effects, get_types, get_dependencies, get_related_components, get_symptoms, get_treatments, get_mechanisms_of_action, get_index

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

def pull_summary_data(keyword, just_summary):
    ''' get index from research study api providing summaries '''
    start = 0
    total_results = 0
    max_results = 10
    page_number = 1
    articles = []
    rows = []
    index = get_empty_index()
    for i in range(0, 10):
        start = i * max_results
        sources = [
            ''.join(['http://export.arxiv.org/api/query?search_query=all:', keyword, '&start=', str(start), '&max_results=', str(max_results)])
        ]
        print('sources', sources)
        for url in sources:
            response = requests.get(url)
            response_string = xml.dom.minidom.parseString(response.content)
            if response_string:
                total_results = int(response_string.documentElement.getElementsByTagName("opensearch:totalResults")[0].childNodes[0].nodeValue)
                entries = response_string.documentElement.getElementsByTagName("entry")
            else:
                entries = json.loads(response.content)
            new_articles, index, new_rows = process_articles(keyword, entries, index, just_summary)
            if len(new_rows) > 0:
                rows.extend(new_rows)
            if len(new_articles) > 0:
                articles.extend(new_articles)
        if total_results < (start + max_results):
            break
    #verbs,relationships,components,conditions,symptoms,compounds,metrics,stressors,patient_conditions,patient_symptoms,patient_metrics,patient_stressors,
    #treatments_successful,treatments_failed,patterns,functions,insights,strategies,systems,variables,intents,types,causal_layers
    if len(rows) > 0:
        write_csv(rows, index.keys(), 'data/rows.csv')
    return articles, index, rows

def process_articles(condition_keyword, entries, index, just_summary):
    rows = []
    articles = []
    empty_index = get_empty_index()
    for entry in entries:
        for node in entry.childNodes:
            if just_summary is True:
                if node.nodeName == 'summary':
                    for subnode in node.childNodes:
                        summary = set()
                        lines = subnode.wholeText.replace('\n', ' ').replace('"', '').split('.') #taking comma out here removes lists embedded in sentences
                        new_lines = []
                        for i, line in enumerate(lines):
                            print('line', line)
                            if len(line) > 0:
                                if i > 0 and line[0] in '0123456789':
                                    line = ''.join([lines[i - 1], line])
                                    if len(new_lines) > 0:
                                        new_lines.pop()
                                new_lines.append(line)
                        for line in new_lines:
                            line = line.strip()
                            if ' ' in line and len(line.split(' ')) > 1:
                                line = re.sub(r'\+', '', line)
                                line = line + '.'
                                print('line', line)
                                formatted_line = remove_duplicates(line)
                                if len(formatted_line) > 0:
                                    row = identify_elements(supported_core, formatted_line, None)
                                    row = get_medical_objects(formatted_line, row) #standard nlp
                                    #index, row = get_metadata(formatted_line, index, row) #custom analysis
                                    if row != empty_index:
                                        rows.append(row)
                                    summary.add(formatted_line)
                        articles.append('\n'.join(summary))
            else:
                article = {'id': '', 'published': '', 'title': '', 'summary': '', 'category': ''}
                if node.nodeName == 'category':
                    article[key] = ''.join([node.getAttribute('scheme'), '::', node.getAttribute('term')])
                elif node.nodeName in article:
                    article[key] = node.nodeValue
                articles.append(str(article))
    '''
    for datatype in ['verbs', 'treatments', 'components']:
        index[datatype] = remove_duplicates(index[datatype])
    '''
    for key in index:
        #print(key, type(index[key]), index[key])
        index_set = set()
        if type(index[key]) == set:
            for sub_item in index[key]:
                if type(sub_item) == set:
                    for x in sub_item:
                        index_set.add(x)
                else:
                    index_set.add(sub_item)
        index_string = index[key] if type(index[key]) == str else '\n'.join(index_set) if len(index_set) > 0 else '\n'.join(index[key])
        save(''.join(['data/', key, '.txt']), index_string)
    return articles, index, rows

def get_medical_objects(line, row):
    '''
    - this function determines conditions, symptoms, & treatments in the sentence 
    - this function is a supplement to get_metadata, 
    which fetches conceptual metadata like insights & strategies
    '''
    row['verbs'] = get_verbs(line)
    row['relationships'] = get_relationships(line, row)
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
        '''
        # to do: add treatment keyword check & add treatment keywords
        #intent = get_intent(summary)
        intent = None
        correlation = get_correlation_of_relationship(intent, r)
        print('get_medical_objects: object relationship', correlation, r)
        if correlation > 0.3:
            if r not in row['treatments_successful']:
                row['treatments_successful'].add(r)
        else:
            if r not in row['treatments_failed']:
                row['treatments_failed'].add(r)
    return row

def filter_line(line):
    ''' filter places & names of anything that doesnt fit into component list
    skip sentences like:
        "The meningitis belt is a region in sub-Saharan Africa where annual outbreaks of meningitis occur with large epidemics observed cyclically."
    '''
    return line

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
    formatted_line = line.replace(',', '')
    row['functions'] = get_functions(row['relationships'])
    row['insights'] = get_insights(row['relationships'])
    row['strategies'] = get_strategies(row['relationships'])
    row['mechanisms'] = get_mechanisms_of_action(row['relationships'])
    index['insights'] = index['insights'].union(row['insights'])
    index['strategies'] = index['strategies'].union(row['mechanisms']).union(row['strategies'])
    return index, row

def is_valid(smile_formula):
    '''
    check apis with formula search from:
    https://cactus.nci.nih.gov/links/chem_www.html
    '''
    return False

def get_correlation_of_relationship(intent, line):
    '''
    this will process a relationship like:
    "this protein activates this gene" or "this compound had a synergistic effect"
    & tests if this is a positive association for the condition, so it can be used as a treatment
    '''
    line_string = ' '.join(line) if type(line) != str else line
    #print("line sentiment", TextBlob(line_string).sentiment, "line", line)
    if intent:
        print("intent sentiment", TextBlob(intent).sentiment, "intent", intent)
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
    print("line sentiment", TextBlob(line_string).sentiment, "line", line)
    print("intent sentiment", TextBlob(intent).sentiment, "intent", intent)
    line_sentiment = TextBlob(line_string).sentiment.polarity
    intent_sentiment = TextBlob(intent).sentiment.polarity
    if (line_sentiment - intent_sentiment) < 0.3:
        return True
    return False

def get_relationships(line, row):
    '''
    - this identifies relationships between element_list in line
    - the response object should be a list of the acting subject, verb, & object:
    line = 'the condition was treated by the chemical'
    return [ ['chemical', 'caused', 'reaction'], ['experiment', 'was', 'successful'] ]
    '''
    
    '''
    to do: split line by clause keywords, then split by verbs 
    make sure youre handling original line unformatted
    '''
    element_list = [item for key in row for item in row[key]]
    clause_keys = [] #[',', 'because', 'since', 'due']
    condition_keys = ['and', 'or', 'even', 'as if', 'as', 'like', 'except', 'which', 'in case', 'if', 'then']
    relationships = set()
    current_set = set()
    line = ' '.join(line) if type(line) != str else line
    print('get relationships', line)
    split_line = line.replace('.', '').replace(',', ' ,').split(' ')
    for i, word in enumerate(split_line):
        numbers = ''.join([w for w in word if w in '0123456789']) # missing 3mg
        if len(word) == len(numbers):
            current_set.add(word)
        else:
            standard_word = get_standard_word(row, word, supported_core, supported_synonyms, standard_verbs)
            if standard_word:
                if len(Word(word).get_synsets(pos=NOUN)) > 0:
                    # check that this is one of the identified elements
                    if word in element_list:
                        current_set.add(standard_word)
                    if (i == (len(split_line) - 1)) or (word in clause_keys):
                        if len(current_set) > 1:
                            relationships.add(' '.join(current_set))
                            current_set = set()
                elif len(Word(word).get_synsets(pos=VERB)) > 0:
                    current_set.add(standard_word)
            else:
                current_set.add(word)
    print('relationships', relationships)
    return relationships

def generate_all_datasets(component_list, rows):
    '''
    iterate through all combinations of elements in rows and 
    generate a dataset for each one to check for relationships
    '''
    combination_list = []
    for i in range(0, len(component_list)):
        new_combination = itertools.combinations(component_list, i)
        print('generate_all_datasets: generating index set for elements', new_combination, 'to predict', new_combination[-1])
        # this doesnt invalidate target_variable param bc we might not always use it in this function
        generate_dataset(new_combination, new_combination[-1], rows, True)
        combination_list.extend(new_combination)
    print('generate_all_datasets: combination_list', combination_list)
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

def write_csv(rows, header_list, path):
    with open(path, 'wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header_list)
        csv_writer.writeheader()
        csv_writer.writerows(rows)
        f.close()

options = [
    'properties', 'treatments', 'contraindications', 'metrics',
    'side effects', 'interactions', 'symptoms', 'conditions', 
    'functions', 'insights', 'strategies', 'patterns', 'all'
]
word_map = read('synonyms.json')
supported_core = word_map['standard_words']
supported_synonyms = set()
for x in word_map['standard_words'].keys():
    for y in word_map['standard_words'][x]:
        supported_synonyms.add(y)
for path in ['data', 'dataset']:
    if not os.path.exists(path):
        os.mkdir(path)
standard_verbs = set(['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable'])
if os.path.exists('data/verbs.txt'):
    verb_contents = read('verbs.txt')
    if verb_contents is not None:
        standard_verbs = set(verb_contents.split('\n'))
just_summary = True # this indicates if you want all article metadata like id, title, & published index or just the summary text
articles, index, rows = pull_summary_data('meningitis', just_summary)
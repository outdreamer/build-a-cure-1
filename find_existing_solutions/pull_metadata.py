import sys, json, os, re, urllib, csv, ssl, random
import wikipedia
from wikipedia.exceptions import DisambiguationError
from xml.dom.minidom import parse
import xml.dom.minidom
import requests
# import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize, pos_tag, ne_chunk

from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from utils import get_standard_word, save, read, remove_duplicates, write_csv
from get_index_def import get_empty_index
from get_objects import identify_elements, get_index_objects
from get_structure import get_pos, get_structural_metadata
from generate_datasets import generate_datasets 

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

def pull_summary_data(sources, metadata_keys, generate_source, generate_target, args, filters, full_params):
    ''' get index from research study api providing summaries '''
    print('pull metadata', metadata_keys, 'args', 'generate_source', generate_source, 'generate target', generate_target, args, 'filters', filters)
    ''' we assume the primary argument comes first - right now only supports one argument'''
    articles = []
    rows = []
    empty_index = get_empty_index(metadata_keys, full_params)
    index = get_empty_index(metadata_keys, full_params)
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
                                                    formatted_line = ''.join([x for x in line.lower() if x in alphabet])
                                                    print('\n\tline', formatted_line)
                                                    if len(formatted_line) > 0:
                                                        row = identify_elements(supported_core, formatted_line, None, metadata_keys, full_params)
                                                        index, row = get_structural_metadata(line, title, data_words, data, index, row, metadata_keys)
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

def get_index_type(word, supported_core, categories):
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
        for key in supported_core[keyword]:
            param_map[key] = 'conditions'
    for keyword in ['treatment_keywords', 'elements', 'compounds']:
        for key in supported_core[keyword]:
            param_map[key] = 'compounds' 
            # not every compound will be a treatment
    for keyword in ['metrics']:
        for key in supported_core[keyword]:
            param_map[key] = 'metrics'
    for keyword in ['organisms']:
        for key in supported_core[keyword]:
            param_map[key] = 'organisms'
    for keyword in ['functions', 'causal_layers']:
        for key in supported_core[keyword]:
            param_map[key] = 'functions'
    for keyword in ['symptom_keywords', 'side_effects']:
        for key in supported_core[keyword]:
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

def get_medical_objects(line, formatted_line, title, index, row, metadata):
    '''
    - this function determines conditions, symptoms, & treatments in the sentence 
    - this function is a supplement to get_metadata, 
      which fetches conceptual metadata like insights & strategies
    to do: 
        - add treatment keyword check & add treatment keywords
        - add metadata check to make sure they requested this data
    '''
    return index, row

def get_generic_medication(brand_name):
    keyword = None
    original_content = None
    generic_content = None
    try:
        original_content = wikipedia.page(brand_name).content
    except Exception as e:
        print(e)
        for item in e:
            if brand_name.lower() not in item.lower() and 'medica' in item.lower():
                keyword = item
    try:
        generic_page = wikipedia.page(item)
        generic_title = generic_page.title
        generic_content = generic_page.content
        for i, s in enumerate(content.split('\n')):
            if '==' in s and '.' not in s:
                sname = s.replace('=','').strip().replace(' ','_').lower()
                if sname in section_map:
                    return generic_title
        if 'a medication' in generic_content:
            return generic_title
    except Exception as e:
        print('keyword e', keyword, e)
    return False

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
    section_list = []
    categories = []
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
                    print('section list', section_list)
                    categories = wikipedia.page(suggested).categories
                    if len(categories) > 0:
                        row['types'] = row['types'].union(set(categories))
                        print('categories', categories)
                        if len(section_list) > 0:
                            ''' use section list to determine type first '''
                            for key, val in section_map.items():
                                for section in section_list:
                                if key in section:
                                    index_type =  val
                        else:
                            index_type = get_index_type(suggested, supported_core, categories)
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
    index['section_list'] = index['section_list'].union(section_list)
    row['dependencies'] = get_dependencies('all', None, row['relationships'], 3)
    return index, row

def get_correlation_of_relationship(intent, line):
    line_string = ' '.join(line) if type(line) != str else line
    #print("\tline sentiment", TextBlob(line_string).sentiment, "line", line)
    if intent:
        print("\tintent sentiment", TextBlob(intent).sentiment, "intent", intent)
    return get_polarity(line_string)

def get_treatment_potential(intent, hypothesis, line, title, metadata):
    '''
    hypothesis & intent can be Null for now 

    this function will process a relationship like:

    intent='check_correlation', line="this protein activates this gene known to cause this condition"

    the line must have these conditions met before it should be analyzed as a treatment:
        - check if it has words similar to the title to indicate relevance to study intent 
        - then check that the objects are in the names or medical objects indexes
        - the condition being studied or a marker of it is mentioned as well

    then it analyzes the positivity of the relationship between objects in the line,
     & tests if this is a positive association for the condition, so it can be used as a treatment:

        - returns "positive" for line above to indicate a potential treatment
        - returns "positive" for "this compound had a synergistic effect with a drug to treat the condition"
        - returns "negative" for "this compound reduced disease inhibition"

    - "intents" are similar to "effects" or "outputs", but assumed to be the purpose of an operation once known
    
    when you have intent & hypothesis functions done, you can do logic like:
    if the intent is check_correlation:
        if the hypothesis is "drug reduced blood pressure":
            if the sentence is:
                "drug did not reduce blood pressure" => negative correlation (failure) or a negative intent (reduce)
            if the sentence is:
                "drug did reduce blood pressure" => positive correlation (success) or a negative intent (reduce)
    '''

    print("\tline sentiment", TextBlob(line).sentiment, "line", line)
    if hypothesis:
        print("\thypothesis sentiment", TextBlob(hypothesis).sentiment, "hypothesis", hypothesis)
    if intent:
        print("\tintent sentiment", TextBlob(intent).sentiment, "intent", intent)

    derived_treatment_relationships = []
    for c in metadata['clauses']:
        clause_metadata = get_relationships_from_clauses(c, metadata['nouns'])
        print('clause', clause)
        modifiers = get_modifiers(clause)
        print('modifiers', modifiers)
        derived_treatment_relationships = derived_treatment_relationships.union(clause_metadata)
        '''
        row['variables'] = row['variables'].union(get_dependencies('inputs', line, row['relationships'], 1))  
        '''
        intent = None
        correlation = get_correlation_of_relationship(intent, r)
        print('\tget_medical_objects: correlation', correlation, r)
        if correlation > 0.3:
            row['treatments_successful'].add(r)
        else:
            row['treatments_failed'].add(r)

    line_sentiment = TextBlob(line).sentiment.polarity
    intent_sentiment = TextBlob(intent).sentiment.polarity
    if (line_sentiment - intent_sentiment) < 0.3:
        return True
    return False

def get_modifiers(clause, nouns):

def remove_unnecessary_words(line, phrases, clauses):
    ''' this should remove all excessive language where phrases or clauses dont add meaning '''
    return line 

def rearrange_sentence(line):
    '''
    this function is to format your sentences in the same way

    this means fulfilling the following expectations:
    - having conditionals at the end rather than the beginning
    - standardized words when synonyms are found
    - simplified language where clearly mappable

    so a sentence like: 
    "in the event of onset, symptoms appear at light speed, even if you take vitamin c at max dose"

    is reduced to:
    "symptoms appear even with vitamin c max dose"
    '''
    return line

def get_conditionals(line, nouns, clauses):
    ''' 
    this function assumes rearrange_sentence
    was already called on line used to generate sentence_pieces 
    '''

    ''' in the following sentence:
    NAA to Cr ratio 
        is reduced in HIV positive patients and
        is a marker for HIV infection of the brain 
            even in the absence of imaging findings of HIV encephalopathy 
            or when the patient is symptomatic due to neurological disease of other etiologies.
    this function would return the last two items 
    '''
    clause_delimiters = ['and', 'or', 'because', 'but', 'however', 'since', 'as']
    keywords = ['even', 'while', 'during', 'yet', 'when', 'if', 'then', 'with', 'without']
    all_sentence_pieces = []
    items = {'conditional': [], 'other': []}
    for sp in clauses:
        for cd in clause_delimiters:
            if cd in sp:
                found_keyword = False
                for k in keywords:
                    if k in nsp:
                        all_sentence_pieces.extend(sp.split(k))
                        found_keyword = True
                if not found_keyword:
                    all_sentence_pieces.extend(sp.split(cd))
    print('all_sentence_pieces', all_sentence_pieces)
    for i, asp in enumerate(all_sentence_pieces):
        if i > 0:
            asp_words = asp.split(' ')
            if len(asp_words) > 1:
                first_word = get_first_non_stopword(asp_words)
                if first_word:
                    pos = get_pos(first_word)
                    if pos != 'verb':
                        items['conditional'].append(asp)
                    else:
                        items['other'].append(asp)
    print('conditionals', items)
    return items

def get_first_non_stopword(words):
    for word in words:
        if word not in stop:
            return word
    return False

def get_relationships_from_clauses(line, sentence_pieces, clauses, nouns):
    '''
    this function is to catch all the meaning in phrases like: 
        "x reduced b inhibitor" => "x - (i - b)"
    and your current logic will only capture: 
        "x reduced b"
    when in reality youd want to store the full clause so the relationships can be derived:
        "x increases b" => "x + b"
        "x reduces inhibitor" => "x - i"
        "inhibitor reduces b" => "i - b"
    so use get_modifiers to find the modifying words like inhibitor and apply them to the verb 
    to get the final version of the relationship

    to do: 
     - add more advanced analysis for linguistic patterns of symptoms 
        'fever that gets worse when x', or 'x reduced y and diminished z even in condition x or condition a', 
        which should have condition x added to the previous relationships
     - add this pattern to clause processing "x is y and is b" => x should be related to y and b
            NAA to Cr ratio 
                is reduced in HIV positive patients and
                is a marker for HIV infection of the brain 
                    even in the absence of imaging findings of HIV encephalopathy 
                    or when the patient is symptomatic due to neurological disease of other etiologies.
    '''
    conditional_items = get_conditionals(line, nouns, clauses)
    operator_clauses = {}
    variables = {}
    ''' process non-conditionals first '''
    all_relationships = []
    for item_type in ['other', 'conditional']:
        for original_clause in conditional_items['other']:
            operator_clause = []
            for word in original_clause.split(' '):
                if word not in nouns:
                    operator = get_operator(word)
                    if operator:
                        operator_clause.append(operator)
                    else:
                        print('could not find operator', word)
                        exit()
                else:
                    operator_clause.append(word)
            operator_clause = ' '.join(operator_clause)
            operator_clauses[operator_clause] = original_clause
        print('operator_clauses', operator_clauses)
    operator_sentence = ' '.join(operator_clauses.keys())
    print('operator sentence', operator_sentence)
    placeholder_clauses = []
    for operator_clause in operator_clauses:
        placeholder = replace_with_placeholders(operator_clause, operator_sentence, line, variables)   
        placeholder_clauses.append(placeholder)
        relationships_with_vars = extract_relationships(replaced_sentence, variables)
        relationships_with_values = replace_with_values(relationships_with_vars, variables)
        if len(relationships_with_values) > 0:
            all_relationships.extend(relationships_with_values)
    if len(all_relationships) > 0:
        print('all_relationships', all_relationships)
        return all_relationships
    return False

def replace_with_values(relationships_with_vars, variables):
    relationships_with_values = set()
    for r in relationships_with_vars:
        new_words = []
        words = r.split(' ')
        for w in words:
            if w in variables.keys():
                new_words.append(variables[w])
            else:
                new_words.append(w)
        new_relation = ' '.join(new_words)
        relationships_with_values.add(new_relation)
    return relationships_with_values

def extract_relationships(replaced_sentence, variables):

    return replaced_sentence

def get_new_key(dictionary):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    current_keys = dictionary.keys()
    for k in current_keys:
        random_letter = random.choices(alphabet, 1)
        new_key = '_'.join([k, random_letter])
        return new_key
    return False 

def replace_with_placeholders(operator_clause, operator_sentence, line, variables):
    ''' what differentiates a variable from a normal word? 
        variables are used to refer to components of sub-logic that include 
        an embedded relationship which must be handled associatively 
        so that x - (a - b) ends up as two relationships: x - a and x + b

        right now this just supports identifying basic units of sub-logic such as:
        - modifiers, like "enzyme extractor"
        - conditional clauses
    '''
        if operator_clause in conditional_items['conditionals']:
            operator_sentence = replace_with_placeholders(operator_clauses, operator_sentence, variables)
            new_key = get_new_key(variables)
            variables[new_key] = operator_clause
            operator_sentence = operator_sentence.replace(operator_clause, new_key)
        for word in operator_clause:
            if word == '+' or word == '-':
                relation.add(word)
            else:
                is_modifier = get_modifier(word)
                if is_modifier:
                    modified_word = get_modified_word(operator_clause, word)
                    modifier_clause = [word, 'of', modified_word]
                    new_key = get_new_key(variables)
                    variables[new_key] = modifier_clause
                    operator_sentence = operator_sentence.replace(modifier_clause, new_key)
                last_item_added = relation[-1]
                if last_item_added not in nouns:
                    ''' previous word was a verb, so add this noun & reset relation '''
                    relation.add(word)
                    clauses_with_vars.add(relation)
                    relation = set()
    '''
    *** Important Info ***

    - in order to preserve order of operations:
        1. first converting "b inhibitor" to { var: modifier relationship}
            {"a": "(i - b)"}
        2. then converting "x - (i - b)" to "x - a" and storing in clauses_with_vars
        3. then converting "x - a" to permuted relationship set:
            "x - i" and "x + b"
        4. conditionals should be applied last

    - variables should be a dict like: 
        { var : modifier relationship }:
        "a": "(i - b)"

    - clauses_with_vars should be the original clauses but with operators instead of verbs
        and with variable names instead of modifier relationships:
        ["x - a"]
        so it can do substitutions and derive the alternate relationships in step 3
        
    '''

def get_modifier(prev_word, word, next_word):
    ''' if this is a modifier, return True 
    - the reason we're isolating modifiers is because theyre embedded relationships 
    so in order to process them correctly, we have to extract them 
    & format them the same as other relationships 
    - then we can do more straightforward calculations with the operator_clause 
    & generate the full set of relationships in the original clause
    - we can easily identify modifiers that are in supported_synonyms 
    but for others we need standard pos patterns
    '''
    modifier_score = 0
    modifier_substrings = [
        "or",
        "er",
    ]
    modifier_patterns = [
        'noun-noun', # the second noun has a verb root, ie "enzyme inhibitor"
        'noun noun', 
    ]
    word_pos = get_pos(word)
    stem_pos = get_pos(stemmer.stem(word))
    if stem_pos in ['VBP', 'VBD', 'VBN', 'VBZ', 'VBG'] and modifier_pos in ['NN', 'JJ', 'JJR', 'NNS', 'NNP', 'NNPS', 'RB']:
        modifier_score += 1
    for m in modifier_substrings:
        if m in word:
            index = len(word) - len(m) - 1
            if word[index:] == m:
                modifier_score += 1
    for p in modifier_patterns:
        found = find_pattern(word, word_pos, pattern)
        if found:
            modifier_score += 1
    if modifier_score > 3:
        return True
    return False

def get_modified_word(operator_clause, nouns, modifier):
    ''' to do: this will fail if you removed the modified word or put it in the next clause '''
    print('get_modified_word: operator_clause', operator_clause, 'modifier', modifier)
    split_clause = operator_clause.strip().split(modifier)
    if len(split_clause) > 1:
        prev_word = split_clause[0].split(' ')[-1]
        next_word = split_clause[1].split(' ')[0]
        print('previous', prev_word, 'next', next_word)
        prev_pos = get_pos(prev_word) if prev_word not in ['+', '-', '='] else ''
        next_pos = get_pos(next_word) if next_word not in ['+', '-', '='] else ''
        if prev_pos == 'noun':
            return prev_word
        elif next_pos == 'noun':
            return next_word
        else:
            ''' apply same logic but get next object & previous object '''
    return False

def get_operator(verb):
    ''' this is to map a verb to an operator like +, -, =
    to simplify sentence sentiment analysis 
    right now we're just supporting positive, negative, or equal 
    to do: 
    - implement positive/negative prefix/suffix checking, like 'dis-' is often a negative prefix
    '''
    pos = get_pos(verb)
    if pos == 'verb':
        stem = stemmer.stem(verb)
        polarity = get_polarity(verb)
        print('get_treatment_potential: polarity', polarity, pos, stem, verb)
        if verb in synonym_list['negative'].keys() or stem in synonym_list['negative'].values() or polarity < 0.0:
            return '-'
        elif verb in synonym_list['positive'].keys() or stem in synonym_list['positive'].values() or polarity > 0.0:
            return '+'
        elif verb in synonym_list['equal'].keys() or stem in synonym_list['equal'].values(): # to do: assess equal word polarity 
            return '='
    return False

def get_polarity(line):
    return TextBlob(line).sentiment.polarity

section_map = {
    'signs_and_symptoms': 'conditions',
    'medical_uses': 'treatments',
    'chemical_and_physical_properties': 'compounds', # this refers to a compound that is not a known treatment or is a sub component of a treatment
    'applications': 'compounds',
    'growth': 'organisms',
    'adverse_effects': 'treatments',
    'side_effects': 'treatments',
    'contraindications': 'treatments',
    'interactions': 'treatments',
    'pharmacology': 'treatments',
    'common_names': 'organism',
    'cause': 'symptoms',
    'pathophysiology': 'symptoms',
    'diagnostic_approach': 'symptoms',
    'management': 'symptoms',
    'epidemiology': 'symptoms',
    'uses': 'organism', # https://en.wikipedia.org/wiki/Boesenbergia_rotunda
}
numbers = '0123456789'
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789- '
key_map = {
    'negative': ['worsen', 'decrease', 'inhibit', 'reduce', 'deactivate', 'disable', 'negative_substrings'],
    'positive': ['improve', 'increase', 'induce', 'enhance', 'activate', 'enable', 'positive_substrings'],
    'equal': ['equal']
}
full_params = {
    'request': ['metadata', 'generate', 'filters'], # request params
    'wiki': ['section_list'],
    'pos': ['verbs', 'nouns', 'subjects', 'clauses', 'common_words', 'counts', 'names', 'relationships', 'taken_out', 'phrases', 'title_similarities'], # elements organized by structure
    'experiment': ['hypothesis', 'tests', 'metrics', 'properties'], # experiment elements
    'compound': ['compounds', 'contraindications', 'interactions', 'side_effects', 'treatments_successful', 'treatments_failed'], # drug elements
    'condition': ['symptoms', 'conditions'], # condition elements
    'context': ['bio_metrics', 'bio_symptoms', 'bio_conditions', 'bio_stressors'], # context elements
    'synthesis': ['instructions', 'parameters', 'optimal_parameter_values', 'required_compounds', 'substitutes', 'equipment_links', 'adjacent_compound_synthesis'],
    'interaction': ['components', 'related', 'alternatives', 'substitutes', 'adjacent', 'stressors', 'dependencies'], # interaction elements
    'conceptual': ['variables', 'systems', 'functions', 'insights', 'strategies', 'patterns', 'priorities', 'intents', 'types', 'causal_layers'] # conceptual elements
}
supported_params = []
for key, val in full_params.items():
    supported_params.extend(val)
metadata_keys = ''
generate_source = ''
generate_target = ''
args_index = {}
filters_index = {}
for i, arg in enumerate(sys.argv):
    arg_key = arg.replace('-', '_')
    if arg_key in supported_params:
        arg_val = sys.argv[i + 1]
        if arg_key == 'metadata':
            if arg_val in supported_params or arg_val == 'all':
                metadata_keys = arg_val.split(',')
        elif arg_key == 'filters':
            # --filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
            filters_index = { key: val.split(',') for key, val in arg_val.split(',') } # val will be metricC::metricvalue for metric
        elif arg_key == 'generate':
            generate_list = arg_val.split('::')
            generate_source = [s for s in generate_list[0].split(',') if s in supported_params]
            generate_target = generate_list[1]
        else:
            args_index[arg_key] = arg_val.split(',')
print('args_index', args_index)
print('filters', filters_index)
print('metadata', metadata_keys)
print('generate', generate_target, generate_source)
sources = [
    {
        'url': 'http://export.arxiv.org/api/query?search_query=all:<KEY>&start=<START>&max_results=<MAX>',
        'results_tag': 'opensearch:totalResults',
        'tag': 'entry'
    }
]
synonym_list = {}
common_words = [] # to do: store common words that dont fit other categories & read them into list
 # if it doesnt have a word ending in one of these suffixes, its probably not relevant
medical_sentence_terms = ['y', 'ic', 'ia', 'al', 'ment', 'tion'] 

if len(args_index.keys()) == 1:
    word_map = read('synonyms.json')
    if word_map:
        supported_core = word_map['standard_words'] if 'standard_words' in word_map else {}
        supported_synonyms = set()
        for x in supported_core.keys():
            supported_synonyms.add(x)
            for y in supported_core[x]:
                supported_synonyms.add(y)
        synonym_list = {
            'negative': get_synonym_list(supported_core, key_map, 'negative') # antagonist, reduce, inhibit, deactivate, toxic, prevents
            'positive': get_synonym_list(supported_core, key_map, 'positive') # help, assist, enhance, induce, synergetic, sympathetic, leads to
            'equal': get_synonym_list(supported_core, key_map, 'equal') # means, signifies, indicates, implies, is, equates to
        }
        for path in ['data', 'datasets']:
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
        verb_contents = read('data/verbs.txt')
        standard_verbs = set(['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable'])
        standard_verbs = set(verb_contents.split('\n')) if verb_contents is not None else standard_verbs
        articles, index, rows = pull_summary_data(sources, metadata_keys, generate_source, generate_target, args_index, filters_index, full_params)
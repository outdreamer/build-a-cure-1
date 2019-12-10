from nltk import CFG
from nltk import word_tokenize, pos_tag, ne_chunk

from get_index_def import get_empty_index

''' conceptual relationships:
    priority = direction
    observation = insight = function = result = relationship
    conclusion = ordered_list(observations) + guess = coefficients + bias
    strategy = ordered_list(insights)
    strategy = insight + context
    problem = (combination of intents having different priorities) or (an resource distribution imbalance)
    intent = strategy + priority
    solution = (combination of strategies operating on variables with insight functions that reduce dimensions of problem (function-combination) or (resource-imbalance))
    type = combination(attributes)
'''

def get_data_store(sources, index_type, metadata_keys, param_keys):
    '''
    this assembles an index out of sources for the index type,
    pulling from data sources like wiki to generate a dataset, 
    if there isnt already a dataset stored locally
    '''
    index = get_empty_index(metadata_keys, param_keys)
    return index

def get_index_objects(index_type, relationship):
    print('get_index_objects', index_type, relationship)
    function_name = ''.join(['get_', index_type])
    globals_dict = globals()
    if function_name in globals_dict:
        print('found function in globals', function_name)
        function = globals_dict[function_name]
        print('function', function)
        output = function(relationship)
        print('output', output)
        return output
    return False

''' these functions do more advanced linguistic processing than 
    keyword matching as in identify_elements '''

def get_variables(line):
    ''' use this to determine parameters for synthesis function too '''

def identify_key_sentences(article):
    '''
    key_sentences should have an item from each sentence_type that is relevant to the study intent
    '''
    key_sentences = {}
    intents = get_study_intent(article)
    if intents:
        key_sentences['intent'] = ','.join(intents)
    for line in article.split('\n'):
        sentence_type = get_sentence_type(line)
        if sentence_type:
            key_sentences[sentence_type] = line
    return key_sentences

def get_sentence_type(line):
    ''' out of sentence_types, determine which this is likeliest to be 
    to do: 
    - implement keyword check for each sentence type
    - add linguistic patterns for each sentence type
    '''
    sentence_types = {
        'hypothesis': [],
        'assumption': [],
        'test': [],
        'intent': [],
        'synthesis_instruction': [],
        'function': [],
        'result': [],
        'treatment': []
    }
    sentence_type_values = [ x for k, v in sentence_types.items() for x in v ]
    elements = get_elements(line)
    element_sentence_pattern = ' '.join(elements)
    for k, v in sentence_types.items():
        if element_sentence_pattern in v:
            return k
    return False

def get_elements(line):
    elements = []
    for word in line.split(' '):
        index_type = get_index_type(word)
        if index_type:
            if index_type not in index_scores:
                elements.append(index_type)
            else:
                elements.append(index_type)
        else:
            elements.append(word)
    return elements

def get_causal_layer(row, index, line, article):
    return row

def get_article_intent(article):
    '''
    this should capture the core intent which should be one of the supported intents
    all intents are inherently relationships so most could be standardized to:
     'find', 'test', 'build', 'compare', or 'verify'
    but you want to find which one fits more given their subtle differences
    for example:
        - 'test' indicates a known relationship was tested
        - 'find' indicates a new relationship was tested

        - 'verify' indicates replication of a research object (result, study)
        - 'compare' indicates analysis of related research objects (study/study, result/protocol)

        - 'build' contains instructions on how to synthesize something
        - 'find' would indicate info about a relationship between the input & output in the study, 
            but not necessarily include the instructions
    '''
    '''
    for studies that have a 'test' intent (to confirm a theorized relationship),
        the relationship youre trying to find is between:
         'method'/'compound' and 'success'/'failure'
    for other studies that are exploratory (to find a new relationship),
        the relationship may be to find correlation between two medical factors:
        'condition' and 'treatment' or 'condition' and 'symptom' or 'treatment' and 'symptom'
    '''

    study_intents = {
        'test': 'to confirm a relationship (between x=success)', 
        'find': 'to find a relationship (between x=y)', 
        'verify': 'to confirm an object (study, method, result)',
        'compare': 'to compare objects (study=study, method=method, result=protocol)', 
        # compare => check that all studies confirm each other, or check that a method-implementation or result-derivation followed protocol
        'build': 'to build object (compound, symptom, treatment, condition, state)' 
        # to get 'health', follow build protocol 'x', to get 'compound', follow build protocol 'y'
    }
    abstract_verbs = ['find', 'derive', 'build', 'test']
    med_objects = ['treatment', 'compound', 'test', 'metric', 'mechanism']
    study_objects = ['relationship', 'limit', 'type', 'method']
    conceptual_objects = ['relationship', 'problem', 'strategy', 'process', 'insight', 'function', 'variable', 'system', 'theory', 'opinion', 'conclusion', 'observation']
    sentence_intents = {
        'describe': ['introduce', 'detail']
        'organize': ['list', 'categorize', 'summarize']
    }
    intent_map = {
        'find_limit',
        'find_relationship': {
            'condition': {
                'treat': ['test_treatment_compound', 'test_treatment_method'],
                'diagnose': ['test_diagnostic_method']
            }
            'synthesize_compound': ['test_synthesis_method']
        }
        'review': {
            'compare': ['meta_review', 'peer_review'],
            'verify': ['retract_study', 'replicate_result']
        }
    }
    intents = []
    for line in article.split('\n'):
        intent = get_intent(line)
        if intent:
            intents.append(intent)

    return intents

def get_intents(line):
    ''' this function is checking for any purpose-related keywords
    to find priority data of bio components, 
    like 'bacteria seek to optimize efficiency' would return 'efficiency'
    '''
    return line
    
def get_strategies(line):
    '''
    get the strategy explaining why this worked or failed, 
    which may be equal to the mechanism of action, 
    so you can do searches for other compounds with similar activity
    '''
    # initial treatment output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
    # type output should be: ['azole', 'essential oils from plant genus x']
    # functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole
    return line

def get_insights(line):
    return line

def get_functions(line):
    ''' for fluconazole, this should be: "antifungal", "inhibitor of cyp3a4" '''
    return line

def get_hypothesis(summary):
    '''
    with an overall intent like 'diagnose',
    if its relevant to the hypothesis of the study
    '''
    intents = ['diagnose', 'check_correlation', 'find_limit', 'evaluate_method']
    return summary

def get_priorities(line):
    return line 

def get_types(line):
    ''' this returns the type stack in a component '''
    return line

def get_function_decomposition(line):
    return line

def get_dependencies(io_type, component, relationships, n):
    ''' 
    this should return a list of outputs, n operations away

    - relationships is a list of lists containing ordered causal relationships
    - io_type is 'input' or 'output'

    outputs = get_outputs('nutrient', [['nutrient', 'stomach', 'liver', 'digestive system', 'amino acid']], 3)
    outputs should be:
        [['stomach', 'liver', 'digestive system']]
    '''
    dependencies = []
    return dependencies


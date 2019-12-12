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

''' these functions do more advanced linguistic processing than 
    keyword matching as in identify_elements '''

def get_variables(line):
    ''' use this to determine parameters for synthesis function too '''
    ''' variables are the inputs to functions '''
    ''' this can mean the subject of a sentence, or the inputs of that subject (resources, context) '''
    return line

def identify_key_sentences(article):
    '''
    key_sentences should have an item from each sentence_type that is relevant to the study intent
    '''
    key_sentences = {}
    intents = get_article_intents(article)
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
        'instruction': [],
        'function': [], # describing processes
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

def get_article_intents(article):
    '''
    this function is checking for any purpose-related keywords
    to find priority data of bio components, 
    like 'bacteria seek to optimize efficiency' would return 'efficiency'

    if something (object, process, attribute) is a known output of a function, 
        its assumed to be the intent

    to do: replace get_pos_in_line with call to get structural/medical metadata 
    '''

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

def get_object_intents(line):
    intents = {}
    row = get_pos_in_line(row, None, all_vars)
    if row:
        if 'nouns' in row:
            for n in row['nouns']:
                functions = get_functions(n)
                if functions:
                    for f in functions:
                        if 'outputs' in f:
                            if n not in intents:
                                intents[n] = []
                            intents[n].append(f['outputs'])
                related_components = get_related_components(n)
                if related_components:
                    for rc in related_components:
                        functions = get_functions(n)
                        if functions:
                            for rcf in functions:
                                if 'outputs' in rcf:
                                    if n not in intents:
                                        intents[n] = []
                                    intents[n].append(rcf['outputs'])
    return intents
    
def get_net_impact(functions, object_name):
    '''
        function to combine functions by intent:
          - if you have these two functions:
                - switch on process A
                - switch off processing of B which creates input for process A
          - the output intent is:
                - neutralize process A (assuming the two functions are equal in power)
    '''
    impact = None
    for f in functions:
        f_impact = get_impact(f, object_name)
        if f_impact:
            if impact:
                if not impact_match(f_impact, impact, object_name):
                    impact = update_impact(f_impact, impact, object_name)
            else:
                impact = f_impact
    if impact:
        return impact
    return False

def impact_match(f_impact, impact, object_name):

def update_impact(f_impact, impact, object_name):

def get_impact(function, object_name):
    '''
    function_string='this compound activates b', object_name='b'
    should return a standard verb like 'activate', 'enable'

    - the object_name is the subject of the sentence
        - make sure the impact verb is acting on that subject so switch if its passive 
    '''
    if object_name in function:
        row = get_pos_in_line(function, None, all_vars)
        if row:
            if 'verbs' in row:
                for v in row['verbs']:
                    standard_verb, check_type = find_matching_synonym(v, ['synonym'], None, 'word', all_vars)
                    if standard_verb and check_type:
                        return standard_verb
                    else:
                        ''' 
                        no supported synonym found for this verb, 
                        check for any other matches other than pos matches
                        '''
                        verbs, check_type = find_matching_synonym(v, None, ['pos', 'synonym'], 'list', all_vars)
                        if verbs and check_type:
                            for sv in verbs:
                                standard, check_type = find_matching_synonym(sv, ['synonym'], None, 'word', all_vars)
                                if standard and check_type:
                                    return standard_verb
    return False

def get_functions(line, local_database):
    ''' for fluconazole, this should be: "antifungal", "inhibitor of cyp3a4" '''
    row = get_structural_metadata(line, None, None, all_vars)
    if row:
        if 'functions' in row:
            return row['functions']
    if local_database:
        ''' to do: add query functions to get objects from local data store '''
        return local_database
    return False

def get_strategies(line, intent):
    '''
     - get the strategy explaining why this method worked or failed for the intent, 
        which may be equal to the mechanism of action, 
        so you can do searches for other compounds with similar activity

     - these are processes used by an organism or used on a compound

    - strategies are the reason for success/failure of a method/treatment, including processes & mechanisms of action
        - "this structure on the compound tears the cell barrier"
        - "induces apoptosis by depriving it of contrary signals"
        - "chlorpromazine increases valproic acid levels, which can be derived from valerian (valerian suppressed cyp3a4), 
        which is a function in common with other compounds with activity against pathogen x"

    - drugs need a way to handle common mutation strategies of pathogens
      - up regulating CDR genes
      - reduced sensitivity of the target enzyme to inhibition by the agent
      - mutations in the ERG11 gene, which codes for 14α-demethylase. 
        These mutations prevent the azole drug from binding, 
        while still allowing binding of the enzyme's natural substrate, lanosterol
    '''
    # initial treatment output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
    # type output should be: ['azole', 'essential oils from plant genus x']
    # functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole
    return line

def get_insights(line):
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


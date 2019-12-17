from nltk import word_tokenize, pos_tag, ne_chunk

from get_index_def import get_empty_index

''' these functions do more advanced linguistic processing than 
    keyword or pattern matching as in identify_elements '''

def find_article_intents(article, all_vars):
    '''
    this function is checking for any purpose-related keywords
    to find priority data of bio components, 
    like 'bacteria seek to optimize efficiency' would return 'efficiency'

    if something (object, process, attribute) is a known output of a function, 
        its assumed to be the intent

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

    for studies that have a 'test' intent (to confirm a theorized relationship),
        the relationship youre trying to find is between:
         'method'/'compound' and 'success'/'failure'
    for other studies that are exploratory (to find a new relationship),
        the relationship may be to find correlation between two medical factors:
        'condition' and 'treatment' or 'condition' and 'symptom' or 'treatment' and 'symptom'
    '''
    intents = []
    for line in article.split('\n'):
        intent = get_intent(line)
        if intent:
            intents.append(intent)
    if len(intents) > 0:
        return intents
    return False

def find_key_sentences(article, all_vars):
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

def find_sentence_type(line, all_vars):
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
        'result': [], # conclusion
        'treatment': []
    }
    sentence_type_values = [ x for k, v in sentence_types.items() for x in v ]
    elements = get_elements(line)
    element_sentence_pattern = ' '.join(elements)
    for k, v in sentence_types.items():
        if element_sentence_pattern in v:
            return k
    return False

def find_hypothesis(article):
    '''
    with an overall intent like 'diagnose',
    if its relevant to the hypothesis of the study
    '''
    intents = ['diagnose', 'check_correlation', 'find_limit', 'evaluate_method']
    return article

def find_fact(pattern, matches, row, all_vars):
    ''' function to identify common article intents to identify false info '''
    return row

def find_topic(pattern, matches, row, all_vars):
    '''
      this function will be used in remove_unnecessary_words
      to filter out words that are either non-medical or too specific to be useful (names)

      test cases:
          permeability => ['structure']
          medicine => ['medical']
          plausibility => ['logic']
    '''
    topics = ['structural', 'logical']
    return row

def find_variable(pattern, matches, row, all_vars):
    ''' use this to determine parameters for synthesis function too '''
    ''' variables are the inputs to functions '''
    ''' this can mean the subject of a sentence, or the inputs of that subject (resources, context) '''
    return row

def find_element(pattern, matches, row, all_vars):
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

def find_causal_layer(pattern, matches, row, all_vars):
    return row

def find_intent(pattern, matches, row, all_vars):
    intents = {}
    row = get_structural_metadata(line, all_vars)
    if row:
        if 'noun' in row:
            for n in row['noun']:
                functions = get_functions(n)
                if functions:
                    for f in functions:
                        if 'output' in f:
                            if n not in intents:
                                intents[n] = []
                            intents[n].append(f['output'])
                related_components = get_related_components(n)
                if related_components:
                    for rc in related_components:
                        functions = get_functions(n)
                        if functions:
                            for rcf in functions:
                                if 'output' in rcf:
                                    if n not in intents:
                                        intents[n] = []
                                    intents[n].append(rcf['output'])
    return intents
    
def find_function(pattern, matches, row, all_vars):
    ''' for fluconazole, this should be: "antifungal", "inhibits cyp3a4" '''
    return False

def find_strategy(pattern, matches, row, all_vars):
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
    return row

def find_insight(pattern, matches, row, all_vars):
    return row

def find_priority(pattern, matches, row, all_vars):
    return row 

def find_type(pattern, matches, row, all_vars):
    ''' this returns the type stack in a component '''
    return row

def find_core_function(pattern, matches, row, all_vars):
    return row

def find_dependency(pattern, matches, row, all_vars):
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

def find_impact(pattern, matches, row, all_vars):
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
        f_impact = get_verb_impact(f, object_name, all_vars)
        if f_impact:
            if impact:
                if not impact_match(f_impact, impact, object_name, all_vars):
                    impact = update_impact(f_impact, impact, object_name, all_vars)
            else:
                impact = f_impact
    if impact:
        return impact
    return False

def impact_match(f_impact, impact, object_name, all_vars):
    return f_impact

def update_impact(f_impact, impact, object_name, all_vars):
    return f_impact

def get_verb_impact(function, object_name, all_vars):
    '''
    - function='this compound activates b', object_name='b'
        should return a standard verb like 'activate', 'enable'
    - the object_name is the subject of the sentence
        - make sure the impact verb is acting on that subject so switch if its passive 
    '''
    if object_name in function:
        row = get_pos_metadata(function, all_vars)
        if row:
            if 'verb' in row:
                for v in row['verb']:
                    if v in all_vars['supported_synonyms']:
                        return all_vars['supported_synonyms'][v]
    return False

from textblob import TextBlob, Word
from get_index_def import get_empty_index
from utils import get_subword_match

''' GET INDEX OF ELEMENTS '''

def identify_elements(supported_core, elements, index):
    '''
    this function is to identify which type of object can be found in elements
    - elements may be a set/list of sentences/phrases/words
    - if index is not None, it adds the identified word to the master index 
      otherwise it adds to the new index generated for this element

    to do: 
     - add more advanced analysis for linguistic patterns of symptoms 'fever that gets worse when x'
     - add regex for numerically indexed prefixes like 14alpha-
     - use sentence tree analysis to do more advanced processing on semantics http://www.nltk.org/book/ch08.html#ex-elephant
            NAA to Cr ratio 
                is reduced in HIV positive patients and
                is a marker for HIV infection of the brain 
                    even in the absence of imaging findings of HIV encephalopathy 
                    or when the patient is symptomatic due to neurological disease of other etiologies.
    '''
    if type(elements) == str and ' ' in elements:
        blob = TextBlob(elements)
        phrases = blob.noun_phrases
    empty_index = get_empty_index()
    element_keys = [ key for key in empty_index.keys() if key in supported_core ]
    elements = elements.split(' ') if type(elements) == str else elements
    identified_elements = get_empty_index()
    for element in elements:
        for keyword_type in element_keys:
            split_element = element if type(element) == set or type(element) == list else element.split(' ')
            for i, word in enumerate(split_element):
                matched = get_subword_match(supported_core[keyword_type], word)
                if matched:
                    if index:
                        index[keyword_type].add(word)
                    else:
                        identified_elements[keyword_type].add(word)
                else:
                    ''' fetch the previous & subsequent word to index items like multi-hyphenated compounds '''
                    for k in supported_core[keyword_type]:
                        if k in word and len(split_element) > 1:
                            new_element_list = []
                            if i == 0:
                                new_element_list = [split_element[i], split_element[i + 1]]
                            elif (i + 1) == len(split_element):
                                new_element_list = [split_element[i - 1], split_element[i]]
                            else:
                                new_element_list = [split_element[i - 1], split_element[i], split_element[i + 1]]
                            if len(new_element_list) > 0:
                                new_element = ' '.join(new_element_list)
                            if index:
                                index[keyword_type].add(new_element) # should be a string like 'alpha-nucleic acid'
                            else:
                                identified_elements[keyword_type].add(new_element)
    if index:
        return index
    print('\tidentified elements', identified_elements)
    return identified_elements

def get_metrics(line):
    ''' find any metrics in this line
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information '''
    metrics = set()
    split_line = line.split(' ')
    for key in supported_core['metrics']:
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

''' these functions do more advanced linguistic processing than 
    keyword matching as in identify_elements '''

def get_primary_condition(summary, index):
    '''
    get the primary condition being studied
    which should equal the keyword passed to get_summary_data
    '''
    return summary 

def get_patterns(elements, index):
    ''' this function looks for matches in elements with basic keyword patterns like alpha-<compound>-ic acid '''
    return index

def identify_key_sentences(summary):
    '''
    response should be:
    summary = {
        'intent': '',
        'key_sentences': {
            'hypothesis': '',
            'treatment': '',
            'conclusion': ''
    }
    '''
    return summary

def get_study_intent(hypothesis):
    '''
    this should capture the core intent which should be one of the supported intents:
    intents = ['diagnose', 'check_correlation', 'find_limit', 'evaluate_method']
    '''
    return hypothesis

def get_intent(line):
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

def get_side_effects(line):
    '''
    this should pull from data in standard sites like wiki, drugs, webmd, & rxlist 
    as well as forum data to find rare symptoms & interactions not listed elsewhere
    '''
    return line

def get_symptoms(line):
    return line

def get_treatments(line):
    return line

def get_mechanisms_of_action(line):
    ''' get specific process explaining how this compound works '''
    return line

def get_types(line):
    ''' this returns the type stack in a component '''
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

def get_related_components(component):
    '''
    this should return all primary sub-components & outputs known for the component,
    such as important adjacent compounds which this one frequently turns into
    or other variations of the compound which have very different functionality
    '''
    return component

def get_index(sources, index_type):
    '''
    this assembles an index out of sources for the index type,
    pulling from data sources like wiki to generate a dataset, 
    if there isnt already a dataset stored locally
    '''
    index = get_empty_index()
    return index
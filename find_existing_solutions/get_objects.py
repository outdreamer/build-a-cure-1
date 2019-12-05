from nltk import CFG
from nltk import word_tokenize, pos_tag, ne_chunk

from textblob import TextBlob, Word
from get_index_def import get_empty_index
from utils import get_subword_match

'''
  naa/JJ
  cr/NN
  ratio/NN
    reduced/VBD
  hiv/JJ
  positive/JJ
    patients/NNS
  marker/VBP
  infection/NN
  brain/NN
    even/RB
    absence/RB
    imaging/VBG
    findings/NNS
  encephalopathy/JJ
  patient/JJ
  symptomatic/JJ
  due/JJ
  neurological/JJ
  disease/NN
    etiologies/NNS

CC: Coordinating conjunction
CD: Cardinal number
DT: Determiner
EX: Existential there
FW: Foreign word
IN: Preposition or subordinating conjunction
JJ: Adjective
VP: Verb Phrase
JJR: Adjective, comparative
JJS: Adjective, superlative
LS: List item marker
MD: Modal
NN: Noun, singular or mass
NNS: Noun, plural
PP: Preposition Phrase
NNP: Proper noun, singular Phrase
NNPS: Proper noun, plural
PDT: Pre determiner
POS: Possessive ending
PRP: Personal pronoun Phrase
PRP: Possessive pronoun Phrase
RB: Adverb
RBR: Adverb, comparative
RBS: Adverb, superlative
RP: Particle
S: Simple declarative clause
SBAR: Clause introduced by a (possibly empty) subordinating conjunction
SBARQ: Direct question introduced by a wh-word or a wh-phrase.
SINV: Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.
SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
SYM: Symbol
VBD: Verb, past tense
VBG: Verb, gerund or present participle
VBN: Verb, past participle
VBP: Verb, non-3rd person singular present
VBZ: Verb, 3rd person singular present
WDT: Wh-determiner
WP: Wh-pronoun
WP: Possessive wh-pronoun
WRB: Wh-adverb
'''

''' GET INDEX OF ELEMENTS '''

def get_trees(line):
    print('getting trees for line', line)
    grammar_entries = ['S -> NP VP', 'PP -> P NP', 'NP -> Det N | NP PP', 'VP -> V NP | VP PP']
    tagged = nltk.pos_tag(word_tokenize(line)) # [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('Foo', 'NNP'), ('Bar', 'NNP'), ('sentence', 'NN'), ('.', '.')]
    print('tagged', tagged)
    grammar_dict = {}
    for item in tagged:
        pos = item[1]
        value = item[0]
        if pos != value:
            if pos not in grammar_dict:
                grammar_dict[pos] = [value]
            else:
                grammar_dict[pos].append(value)
    for key, val in grammar_dict.items():
        if len(val) > 1 and type(val) == list:
            new_grammar_entry = ''.join([key, ' -> ', ' | '.join(val)])
            grammar_entries.append(new_grammar_entry)
    grammar_definition = '\n'.join(grammar_entries) if len(grammar_entries) > 0 else None
    print('grammar_def', grammar_definition)
    if grammar_definition:
        grammar = CFG.fromstring(grammar_definition)
        parser = nltk.ChartParser(grammar)
        for tree in parser.parse(line):
             print('tree', tree)
    trees = ne_chunk(tagged)
    # Tree('S', [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), Tree('ORGANIZATION', [('Foo', 'NNP'), ('Bar', 'NNP')]), ('sentence', 'NN'), ('.', '.')])
    print('trees', trees)
    return trees

def identify_elements(supported_core, elements, index, metadata, param_keys):
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
    empty_index = get_empty_index(metadata, param_keys)
    element_keys = [ key for key in empty_index.keys() if key in supported_core ]
    elements = elements.split(' ') if type(elements) == str else elements
    identified_elements = get_empty_index(metadata, param_keys)
    for element in elements:
        for keyword_type in element_keys:
            split_element = element if type(element) == set or type(element) == list else element.split(' ')
            for i, word in enumerate(split_element):
                with_previous = word if i == 0 else ' '.join([split_element[i - 1], word])
                with_next = word if i == (len(split_element) - 1) else ' '.join([word, split_element[i + 1]])
                matched = get_subword_match(supported_core[keyword_type], word, 'bool')
                if matched and len(word) > 1:
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
                            if len(new_element) > 1:
                                if index:
                                    index[keyword_type].add(new_element) # should be a string like 'alpha-nucleic acid'
                                else:
                                    identified_elements[keyword_type].add(new_element)
    if index:
        return index
    print('\tidentified elements', identified_elements)
    return identified_elements

def get_index(sources, index_type, metadata, param_keys):
    '''
    this assembles an index out of sources for the index type,
    pulling from data sources like wiki to generate a dataset, 
    if there isnt already a dataset stored locally
    '''
    index = get_empty_index(metadata, param_keys)
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

def get_primary_condition(summary, index):
    '''
    get the primary condition being studied
    which should be the keyword passed to get_summary_data
    if it was a condition
    or the subject of the study
    '''
    return summary 

def identify_key_sentences(summary):
    '''
    response should be:
    summary = {
        'intent': '',
        'key_sentences': {
            'hypothesis': '',
            'assumptions': [],
            'method': '',
            'tests': [],
            'treatments': [],
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

def get_metrics(line):
    '''
    find any metrics in this line
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information
    '''
    metrics = set()
    split_line = line.split(' ')
    for i, word in enumerate(split_line):
        numbers = [w for w in word if w.isnumeric()]
        if len(numbers) > 0:
            if len(numbers) == len(word):
                next_word = split_line[i + 1]
                if len(next_word) < 5:
                    # to do: add extra processing rather than assuming its a unit of measurement
                    metrics.add(word)
                    metrics.add(next_word) # '3 mg'
            else:
                metrics.add(word) # '3mg'
    return metrics

def get_patterns(line):
    ''' this function looks for matches in elements with basic keyword patterns like alpha-<compound>-ic acid '''
    return line

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

def get_mechanisms(line):
    ''' get specific process explaining how this compound works '''
    return line

def get_tests(line):
    return line

def get_types(line):
    ''' this returns the type stack in a component '''
    return line

def get_related_components(component):
    '''
    this should return all primary sub-components & outputs known for the component,
    such as important adjacent compounds which this one frequently turns into
    or other variations of the compound which have very different functionality
    '''
    return component

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


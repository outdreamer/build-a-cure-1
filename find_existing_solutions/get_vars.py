import os
from utils import *
from get_pos import *

def get_pattern_config(all_vars):
    all_vars['passive'] = [" by ", " from ", " of "]
    ''' to do: assess which operator combinations neutralize or negate a relationship '''
    all_vars['combined_map'] = {
        '=': ['=-', '-=', '=+', '+=', '=='], #"x = (i - b)" => x and b equal i
        '-': ['-+', '+-', '=-', '-=', '==-', '=-=', '-==', '-=-', '---'],
        '+': ['--', '++', '+=', '=+', '==+', '=+=', '+==', '+=+', '+++'],
        '#': [
            '# &', # even with x
            '# !', # even without x
            '! -', # not decrease
            '! +', # not increase ('neutral' or 'independent', 'does not increase' doesnt mean 'decrease')
            '! >', # not change
            '~ !' # does not increase =>
        ]
    }
    all_vars['key_map'] = {
        '-': ['worsen', 'decrease', 'inhibit', 'reduce', 'deactivate', 'disable'],
        '+': ['improve', 'increase', 'induce', 'enhance', 'activate', 'enable'],
        '=': ['equal', 'alternate'],
        '>': ['creates'],
        '@': ['changes'],
        '~': ['functions']
    }
    all_vars['charge'] = {
        '-': aggregate_synonyms_of_type(all_vars, '-'), # antagonist, reduce, inhibit, deactivate, toxic, prevents
        '+': aggregate_synonyms_of_type(all_vars, '+'), # help, assist, enhance, induce, synergetic, sympathetic, leads to
        '=': aggregate_synonyms_of_type(all_vars, '=') # means, signifies, indicates, implies, is, equates to
    }
    ''' this maps operators to lists of operator keyword to use as clause delimiters '''
    all_vars['clause_map'] = {
        '-' : ["decrease"], # attacks
        '+' : ["increase"], # helps
        '=': ['is', 'like', 'equate', 'equal', 'describe', 'indicate', 'delineate', 'same', 'like', 'similar', 'implies', 'signifies', 'means'],
        '&': ['and', 'with'],
        '|': ['or'],
        '^': ['but', 'yet', 'but yet', 'but rather', 'but actually', 'still', 'without', 'however', 'nevertheless' 'in the absence of', 'lacking'], # except and without
        '%': [
            'because', 'as', 'since', 'if', 'then', 'from', 'due', 'when', 'while', 'during', 'for', 'given',
            'in case', 'in the event that', 'caused by', 'respective of', 'during', 'later', 'after', 'before', 'pre-', 'post-'
        ], # x of y is contextual "x in the context of y"
        '#': ['even', 'still', 'despite', 'otherwise', 'in spite of', 'regardless', 'heedless', 'irrespective'],
        '!': ['not', 'without'],
        '~': ['functions', 'that'],
        '>': ['creates', 'becomes', 'changes into', 'transforms', 'produces', 'leads to', 'converts into'],
        '@': ['changes', 'impacts', 'influences', 'adjusts', 'modulates', 'modifies', 'alters', 'affects'],
        '<': ['subset'] #'x is a subset of y'
    }
    ''' this maps operators to standard words to replace them with '''
    all_vars['operator_map'] = {
        '-' : "decrease", # attacks
        '+' : "increase", # helps
        '=' : "equal", # is
        '&' : "union", # with, union
        '|' : "alternate", # or
        '^' : "exception", # without
        '%' : "dependent", # apply
        '#' : "independent", # by standard
        '!' : "not", # negating an noun or verb
        '~' : 'functions',
        '>' : 'creates', # should add changes as well as creates
        '@' : 'changes',
        '<' : 'is subset of'
    }

    ''' sort clause delimiters so the longer strings are matched first '''
    for key in all_vars['clause_map']:
        all_vars['clause_map'][key] = reverse_sort(all_vars['clause_map'][key])

    all_vars['clause_delimiters'] = []
    for k, v in all_vars['clause_map'].items():
        all_vars['clause_delimiters'].extend(v)
    all_vars['clause_delimiters'].extend([',', ':', ';'])

    ''' *** IMPORTANT PATTERN CONFIG INFO ***
        - for pattern configurations, always put the extended pattern first
            - if you put '<noun>' before "<noun> <noun>',
                you'll miss phrases like 'compound acid' returning matches like:
                     ['compound acid']
                and will instead get matches for the '<noun>' pattern:
                    ['compound', 'acid']
                so make sure thats what you want before ignoring this rule
        - pattern_syntax: 
            __a__ : an optional item
            |a b c| : a set of alternatives
        - note that we are also supporting pos names in the patterns, in case you want to include all tags from that pos type
        - if you include 'noun' in your pattern, it'll replace it with all the noun pos tags, like |NN NNS NNP NNPS| etc
    '''

    all_vars['keywords'] = {
        'treatments': [],
        'compounds': {
            'object': ['ion', 'acid'],
            'modifiers': [
                'oral', 'liquid', 'topical', 'intravenous', 'iv', 
                'injection', 'gavage', 'capsule', 'gel', 'powder', 
                'supplement', 'solution', 'spray', 'tincture', 'mixture'
            ],
        },
        'patient': all_vars['supported_core']['participants']
    }
    # use participant instead of patient bc that has other meanings
    '''
        VBZ: Verb, 3rd person singular present - asks is does has
        VBG: Verb, gerund or present participle - asking, being, doing, having
        VBD: Verb, past tense - asked, was/were, did, had
    '''
    all_vars['pattern_maps'] = {
        'passive_to_active': {
            'x of y': 'y x', # to do: add support for new characters in target_pattern like 'y-x'
            'x was VBD by y': 'y VBZ x', # alkalization of x => x alkalizer => alkalizes x
            'x that has y': 'x with y',
            'the N1 VBD VBN IN the N2': 'the N2 VBZ the N1', # x was bitten by y => y bit x
            'x VBD VBD IN y': 'y VBN x',
            'x VBD VBN by y': 'y VBN x',
            'x VBZ VBN by y': 'y VBN x',
            'x that y z': 'z y x', # "protein that modulates a (signaling pathway)" => "(signaling pathway)-changing protein" 
            'x that does VBG': 'x VBZ', # x that does inhibiting => x inhibits
            'x that does VBG': 'x VBZ', # x that does inhibiting => x inhibits 
            'x with y functionality': 'x y', 
            'x has ability to do y': 'x y',
            'JJ1 NN1 of JJ2 NN2': 'JJ2 NN2 JJ1 NN1',
            'x is an item in list b': 'x is in list b'
        }
    }
    all_vars['supported_pattern_variables'] = ['N', 'V', 'ADJ', 'ADV', 'DPC', 'C', 'D', 'P']
    all_vars['pattern_vars'] = ['N', 'ALL_N', 'V', 'ALL_V', 'ADJ', 'ADV', 'DPC', 'C', 'D', 'P', 'modifiers', 'clauses', 'phrases', 'noun_phrases', 'verb_phrases']
    ''' to do: add full_params objects to pattern_vars & standardize to singular keys '''
    all_vars['pattern_index'] = {
        'passive': [
            '|VB VBP VBN VBD| |VB VBP VBN VBD|', # is done, was done
            'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', # having been done
            '|VB VBP VBN VBD| |TO IN PP|', # finish by, done by
            '|VBD| VBN VBN |TO IN PP|', # has been done by
            '|noun_phrases| of |noun_phrases|' # enzyme inhibitor of protein synthesis
        ],
        'subjects': [
            'ALL_N ALL_V',
        ],
        'modifiers': [
            #'(?)', # add support for an any character 
            '|N V| |N ADV ADJ V|', # compound isolate
            'NNP ALL_N', # Diabetes mellitus
            'N N', # the second noun may have a verb root, ie "enzyme-inhibitor"
            'N V',
            'JJ NN'
        ],
        'phrases': [
            'ALL_N DPC |ADJ ADV VB VBG VBD| ALL_N', # converter of ionic/ionized/ionizing radiation, necrotizing spondylosis
            'ALL_N DPC ALL_N |VBG VBD|', # metabolite of radiation poisoning
            'ALL_N DPC ALL_N', # metabolite/metabolizer/inhibitor/alkalization of radiation, 
            'modifiers DPC modifiers'
        ],
        'clauses': [
            'DPC NP VP NP',
            'DPC NP DPC NP',
            'DPC VP NP',
            'DPC VP',
            'DPC NP',
        ],
        'relationships': [
            'clauses',
            'clauses CC clauses'
        ],
        'noun_phrases': [
            'ALL_N ALL_N',
            'ALL_N ALL_N ALL_N', # HIV-positive patients => NNP JJ NNS
        ],
        'verb_phrases': [
            'ADV ALL_V',
            'ADJ ALL_V',
            'ALL_V ALL_V', #'associating alkalizing with compound x'
            'ALL_V ALL_V',
            'plays a |VB NN| role',
            '|functions works operates interacts acts| as __a__ |VB NN|'
        ],
        'compounds': [
            "administration_method of compound",
            "compound compound"
        ],
        'symptoms': [
            'fever that gets worse when x',
            'x reduced y and diminished z even in condition x or condition a'
        ],
         'types': [
            'ADJ N', # Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')
        ],
        'roles': [
            '|ADV V N|', # Ex: 'emulsifying protein' (role = 'emulsifier')
            'N of N', # Ex: 'components of immune system' (role = 'component', system = 'immune system')
            '|V N| role', # Ex: functional role (role => 'function')
            '|functions works operates interacts acts| as (a) |V N|' # Ex: acts as an intermediary (role => 'intermediary')
        ]
    }

    ''' sort pattern_index so the longer patterns are checked first '''
    for key in all_vars['pattern_index']:
        all_vars['pattern_index'][key] = reverse_sort(all_vars['pattern_index'][key])

    '''
    if there are files with the 'data/objecttype_patterns.txt' name pattern, 
    pull that data and add it to pattern_index dict 
    '''
    for key in all_vars:
        cwd = os.getcwd()
        pattern_filename = ''.join([cwd, 'data/patterns_', key, '.txt'])
        if os.path.exists(pattern_filename):
            pattern_contents = read(pattern_filename)
            if pattern_contents:
                pattern_lines = pattern_contents.split('\n')
                if len(pattern_lines) > 0:
                    if key not in all_vars['pattern_index']:
                        all_vars['pattern_index'][key] = []
                    for line in pattern_lines:
                        pattern = line.split('_')[0] 
                        # just fetching the pattern, not the matches stored after the '_'         
                        all_vars['pattern_index'][key].append(pattern)
    converted_all_vars = convert_pos_names_to_nltk_tags(all_vars)
    if converted_all_vars:
        return converted_all_vars
    return all_vars

def reverse_sort(map_list):
    '''
    - before parsing patterns, sort the patterns by number of spaces 
        so the longest patterns get parsed first as a safeguard
    - also sort clause delimiters by length before applying them so you apply 
        "but actually" as a delimiter before applying "but"
    '''
    sorted_val_list = []
    length_index = {}
    for key in map_list:
        length_index[key] = len(key)
    if length_index:
        for length in reversed(sorted(length_index.values())):
            for k, v in length_index.items():
                if v == length:
                    sorted_val_list.append(k)
    if len(sorted_val_list) > 0:
        return sorted_val_list
    return False

def get_args(arg_list, all_vars):
    metadata_keys = ''
    generate_source = ''
    generate_target = ''
    args_index = {}
    filters_index = {}
    for i, arg in enumerate(arg_list):
        arg_key = arg.replace('--', '').replace('-', '_')
        if arg_key in all_vars['supported_params']:
            arg_val = arg_list[i + 1] if (i + 1) < len(arg_list) else ''
            if arg_key == 'metadata':
                if arg_val in all_vars['supported_params'] or arg_val == 'all':
                    metadata_keys = arg_val.split(',')
            elif arg_key == 'filters':
                # |filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
                filters_index = { key: val.split(',') for key, val in arg_val.split(',') } # val will be metricC::metricvalue for metric
            elif arg_key == 'generate':
                generate_list = arg_val.split('::')
                generate_source = [s for s in generate_list[0].split(',') if s in all_vars['supported_params']]
                generate_target = generate_list[1]
            else:
                args_index[arg_key] = arg_val.split(',')
    print('args_index', args_index)
    print('filters', filters_index)
    print('metadata', metadata_keys, 'generate', generate_target, generate_source)
    metadata_keys = 'all' if metadata_keys == '' else metadata_keys
    return args_index, filters_index, metadata_keys, generate_target, generate_source

def get_vars():
    verb_contents = read('data/verbs.txt')
    standard_verbs = set(['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable'])
    all_vars = {}
    all_vars['standard_verbs'] = set(verb_contents.split('\n')) if verb_contents is not None else standard_verbs
    all_vars['numbers'] = '0123456789'
    all_vars['alphanumeric'] = 'abcdefghijklmnopqrstuvwxyz0123456789- '
    all_vars['alphabet'] = 'abcdefghijklmnopqrstuvwxyz'    
    plural_keys = [
        'conditions', 'tests', 'states', 'limits', 'participants', 'mechanisms', 'causal_layers', 'side_effects', 
        'metrics', 'alternates', 'observations', 'results', 'conclusions', 'symptoms', 'treatments', 'hypotheses', 
        'strategies', 'compounds', 'components', 'intents'
    ]
    all_vars['plural_map'] = {}
    for pk in plural_keys:
        all_vars['plural_map'][pk] = get_singular(pk)
    all_vars['clause_analysis_chars'] = [' ', '-', ':', ';', '(', ')']
    all_vars['full_params'] = {
        'request': ['metadata', 'generate', 'filters', 'data'], # request params
        'wiki': ['section_list'],
        'pos': ['pos', 'verbs', 'nouns', 'common_words', 'counts', 'taken_out', 'line', 'prep', 'conj', 'det', 'descriptors', 'original_line', 'word_map'],
        'structure': ['types', 'names', 'ngrams', 'modifiers', 'phrases', 'clauses', 'subjects', 'relationships', 'patterns', 'similar_lines'], # structural
        'experiment': ['hypothesis', 'tests', 'metrics', 'properties', 'assumptions'], # experiment elements
        'compound': ['compounds', 'contraindications', 'interactions', 'side_effects', 'treatments_successful', 'treatments_failed'], # drug elements
        'organism': ['genes', 'gene_expressions', 'evolution', 'organs', 'cells', 'nutrients'],
        'condition': ['symptoms', 'conditions', 'diagnosis', 'phases'], # separate diagnosis bc theyre not always accurate so not equivalent to condition
        'context': ['bio_metrics', 'bio_symptoms', 'bio_conditions', 'bio_stressors'], # context elements
        'synthesis': ['instructions', 'parameters', 'optimal_parameter_values', 'required_compounds', 'substitutes', 'equipment_links'],
        'relational': ['components', 'related', 'alternates', 'substitutes', 'sub', 'adjacents', 'stressors', 'dependencies'],
        'conceptual': ['concepts', 'variables', 'functions', 'causal_stack', 'insights', 'strategies', 'prediction', 'priorities', 'intents', 'systems']
    }
    '''
    some of these types have type mappings:
        condition = state
        symptom = function = side_effects
        function = relationship
        synthesis = build process
        structure = pattern
    so generalize when you can
    '''
    object_type_keys = {
        'medical_types': ['experiment', 'compound', 'organism', 'condition', 'context', 'synthesis'],
        'conceptual_types': ['conceptual', 'relational'],
        'structural_types': ['pos', 'structure']
    }
    for key, val in object_type_keys.items():
        for ref in val:
            all_vars[key] = [item for item in all_vars['full_params'][ref]]
    all_vars['supported_params'] = []
    for key, val in all_vars['full_params'].items():
        all_vars['supported_params'].extend(val)
    all_vars['pos_tags'] = get_pos_tags()
    ''' retrieve synonyms from maps/*.json '''
    all_vars = fill_synonyms('maps', all_vars)
    all_vars['section_map'] = {
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
    all_vars = get_pattern_config(all_vars)
    return all_vars


def aggregate_synonyms_of_type(all_vars, synonym_type):
    type_synonyms = set()
    if synonym_type in all_vars['key_map']:
        for keyword in all_vars['key_map'][synonym_type]:
            if keyword in all_vars['supported_core']:
                if type(all_vars['supported_core'][keyword]) == dict:
                    for k, v in all_vars['supported_core'][keyword]:
                        type_synonyms.add(k)
                        type_synonyms.add(v)
                elif type(all_vars['supported_core'][keyword]) == list:
                    for x in all_vars['supported_core'][keyword]:
                        type_synonyms.add(x)
    return type_synonyms

def fill_synonyms(path, all_vars):
    ''' get maps in path & assemble into synonym lists '''
    cwd = os.getcwd()
    all_vars['supported_core'] = {}
    all_vars['supported_synonyms'] = {}
    all_vars['supported_stems'] = {}
    if not os.path.exists(path) or not os.path.isdir(path):
        path = '/'.join([cwd, path])
    if os.path.exists(path) and os.path.isdir(path):
        for filename in os.listdir(path):

            full_path = '/'.join([path, filename]) 
            if os.path.exists(full_path) and os.path.isfile(full_path):
                word_map = read(full_path)
                if word_map:
                    if 'sources' not in filename:
                        for top_element in word_map:
                            all_vars['supported_core'][top_element] = word_map[top_element]
                            all_vars['supported_stems'][top_element] = set()
                            if type(word_map[top_element]) == list:
                                for y in word_map[top_element]:
                                    all_vars = process_synonym_element(y, top_element, all_vars)
                            elif type(word_map[top_element]) == dict:
                                for k, y in word_map[top_element].items():
                                    all_vars['supported_stems'][top_element].add(get_stem(k))
                                    all_vars = process_synonym_element(y, top_element, all_vars)
                                    all_vars = process_synonym_element(y, k, all_vars)     
                    else:
                        print('word map', word_map)
                        all_vars['sources'] = word_map
    return all_vars

def process_synonym_element(y, keyword, all_vars):
    if type(y) == list:
        for x in y:
            all_vars['supported_stems'][keyword].add(get_stem(x))
            all_vars['supported_synonyms'][x] = keyword
    elif type(y) == dict:
        for k, v in y.items():
            all_vars['supported_stems'][keyword].add(get_stem(k))
            all_vars['supported_stems'][k].add(get_stem(v))
            all_vars['supported_synonyms'][k] = keyword
            all_vars['supported_synonyms'][v] = k
    elif type(y) == str:
        all_vars['supported_stems'][keyword].add(get_stem(y))
        all_vars['supported_synonyms'][y] = keyword
    return all_vars                                    

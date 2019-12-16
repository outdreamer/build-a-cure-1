import os, random
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
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
    all_vars['pattern_maps'] = {
        'passive_to_active': {
            'the N1 VBD VBN IN the N2': 'the N2 VBZ the N1'
        }
    }
    all_vars['supported_pattern_variables'] = ['N', 'V', 'ADJ', 'ADV', 'DPC', 'C', 'D', 'P']
    all_vars['pattern_vars'] = ['N', 'ALL_N', 'V', 'ALL_V', 'ADJ', 'ADV', 'DPC', 'C', 'D', 'P']
    ''' to do: add full_params objects to pattern_vars & standardize to singular keys '''
    all_vars['type_pattern_index'] = {
        'passive': [
            'noun_phrases1 of noun_phrases2' # enzyme inhibitor of protein synthesis
        ],
        'phrases': [
            'modifiers1 DPC modifiers2'
        ],
        'clauses': [
            'clauses1 DPC clauses2'
        ],
        'relationships': [
            'clauses',
            'phrases1 phrases2 V clauses',
            'clauses1 DPC clauses2'
        ],
        'rules': [],
        'contexts': [],
        'compounds': [
            "rules of compounds",
            "compounds1 compounds2"
        ],
        'conditions': [],
        'symptoms': [
            'N that gets worse when contexts1',
            'x - y & - z even in conditions1 or conditions2'
        ]
    }
    all_vars['pattern_index'] = {
        'passive': [
            '|VB VBP VBN VBD| |VB VBP VBN VBD|', # is done, was done
            'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', # having been done
            '|VB VBP VBN VBD| |TO IN PP|', # finish by, done by
            '|VBD| VBN VBN |TO IN PP|', # has been done by
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
        ],
        'clauses': [
            'DPC NP VP NP',
            'DPC NP DPC NP',
            'DPC VP NP',
            'DPC VP',
            'DPC NP',
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

    for key in all_vars['type_pattern_index']:
        all_vars['pattern_vars'].append(key)
    for key in all_vars['pattern_index']:
        all_vars['pattern_vars'].append(key)
    all_vars['pattern_vars'] = set(all_vars['pattern_vars'])

    all_vars['all_version_types'] = ['correct', 'repeated', 'nested', 'alt', 'pos', 'type', 'synonym', 'operator', 'function']

    for key in ['pattern_index', 'type_pattern_index']:
        for pattern_key, patterns in all_vars[key].items():
            new_patterns = []
            for pattern in patterns:
                generated_patterns = get_all_versions(pattern, 'all', all_vars) 
                if generated_patterns:
                    for gp in generated_patterns:
                        new_patterns.append(gp)
            all_vars[key][pattern_key] = reversed(sorted(new_patterns))

    for pattern_map_key, pattern_map in all_vars['pattern_maps'].items():
        new_pattern_map = {}
        for sp, tp in pattern_map.items():
            sp_patterns = get_all_versions(sp, 'all', all_vars) 
            if sp_patterns:
                for sp_pattern in sp_patterns:
                    tp_patterns = get_all_versions(tp, 'all', all_vars) 
                    if tp_patterns:
                        for tp_pattern in tp_patterns:
                            new_pattern_map[sp_pattern] = tp_pattern
        if new_pattern_map:
            all_vars['pattern_maps'][pattern_map_key] = new_pattern_map

    ''' 
    now that pattern lists are generated, 
    populate pattern types from type_pattern_index[key[
    with all variants from the corresponding list in pattern_index[key]
    '''
    for key, type_pattern_index in all_vars['type_pattern_index'].items():
        new_type_pattern_index = []
        for type_pattern in type_pattern_index:
            for sub_pattern_type, sub_pattern_list in all_vars['pattern_index'].items():
                nonnumeric_index_type = get_nonnumeric(sub_pattern_type, all_vars)
                nonnumeric_type_pattern = get_nonnumeric(type_pattern, all_vars)
                ''' if 'modifiers' in ['modifiers', 'DPC', 'modifiers'] '''
                if nonnumeric_index_type in nonnumeric_type_pattern.split(' '):
                    ''' iterate through modifiers pattern_index, replacing nonnumeric_index_type with index pattern '''
                    for sub_pattern in sub_pattern_list:
                        new_type_pattern = nonnumeric_type_pattern.replace(nonnumeric_index_type, sub_pattern)
                        new_type_pattern_index.append(' '.join(new_type_pattern))
        if len(new_type_pattern_index) > 0:
            all_vars['type_pattern_index'][key] = new_type_pattern_index

    ''' 
        sort pattern_index so the longer patterns are checked first
        for key in all_vars['pattern_index']:
        all_vars['pattern_index'][key] = reverse_sort(all_vars['pattern_index'][key])
    '''
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

def get_nested_patterns(pattern, pattern_type, source_vars, all_vars):
    '''
    support for nested alts in patterns like: '__|a an|__' and '|VB NN |VB ADV|| VB'
    pattern = '|VB NN x| VB' and variables['x'] = '|VB ADV|'
    returns nested_patterns = ['VB VB', 'NN VB', 'x VB']

    to do: 
        - add operator support for char other than '|'
        - A&B or VB&VB should be logged as a variable
    '''
    new_patterns = [] 
    new_pattern = []
    variables = {}
    delimiters = ['|']
    space_count = pattern.count(' ') - 2
    for d in delimiters:
        original_pattern_length = get_original_pattern_length(pattern, d)
        for i, subset in enumerate(pattern.split(d)):
            words = subset.strip().split(' ')
            ''' delimiter section is beginning or ending '''
            if len(new_pattern) == (original_pattern_length - space_count):
                new_pattern.extend(words)
                new_patterns.append(' '.join(new_pattern))
                new_pattern = []
            if i > 0 and (i / 2) != int(i / 2):
                ''' make sure only sub-patterns with pos_tags are logged as a variable '''
                is_tag_section = False
                for var in words:
                    nonnumeric_var = get_nonnumeric(var, all_vars)
                    is_supported = is_supported_tag(nonnumeric_var, all_vars)
                    if is_supported:
                        is_tag_section = True
                if is_tag_section:
                    var_value = ' '.join(words)
                    if source_vars:
                        if var_value in source_vars.values():
                            for k, v in source_vars.items():
                                if v == var_value:
                                    variables[k] = v
                                    new_pattern.append(k) # *** var
                        else:
                            new_key = get_new_key(variables.keys(), subset, all_vars)
                            variables[new_key] = var_value # *** '-_-'.join(words)
                            new_pattern.append(new_key) # *** var
                    else:
                        new_key = get_new_key(variables.keys(), subset, all_vars)
                        variables[new_key] = var_value # *** '-_-'.join(words)
                        new_pattern.append(new_key) # *** var
            else:
                new_pattern.extend(words)
    if len(new_patterns) > 0:
        return new_patterns, variables
    return [pattern], variables

def get_alt_patterns(pattern, nested_variables, all_vars):
    ''' 
    this functions returns ['VB NN D1 D2', 'VB JJ D1 D2'] 
    from pattern = 'VB x D1 D2' and nested_variables['x'] = 'NN JJ'
    - alternatives are indicated by options separated by spaces within pairs of '|'
    - optional string are indicated by: __optionalstring__
    - you could also replace 'VB' with 'V' and do a match on those
    '''
    pattern = pattern.strip()
    all_patterns = []
    delimiter = find_delimiter(pattern, all_vars)
    if delimiter:
        # you could also create a list of lists & iterate with counters
        # pattern_sets should be a list of pos with alts separated by spaces ['NN VB', 'VB'] or ['NN', 'NP']
        '''
        pattern = '|VB NN x| VB' and variables['x'] = 'VB ADV'
        pattern = '|VB NN VB&ADV|' means 'VB or NN or VB & ADV'
        this function needs to support nested patterns, so when iterating, 
        check for any var chars and if found, iterate through variable values & replace with each value
        '''
        new_all_patterns = add_sub_patterns(pattern.split(delimiter), nested_variables)
        if new_all_patterns:
            if len(new_all_patterns) > 0:
                for nap in new_all_patterns:
                    all_patterns.append(nap)
        if len(all_patterns) > 0:
            return all_patterns
    # all_patterns should be a list of combined patterns like ['NN VB', 'VB VB'],
    # which is both combinations possible of the set ['NN VB', 'VB']
    ''' move to add_sub_patterns so vars are supported as well
    if all_patterns:
        #now replace optional strings with an empty string and add that pattern
        for pattern in all_patterns:
            all_patterns_with_alts = []
            if '__' in pattern:
                new_pattern = pattern
                for item in pattern.split('__'):
                    if ' ' not in item:
                        optional_word = ''.join(['__', item, '__'])
                        if optional_word in pattern:
                            new_pattern = new_pattern.replace(optional_word, '')
                new_pattern = new_pattern.replace('  ', ' ')
                # add the alternative pattern with optional strings replaced
                all_patterns_with_alts.append(new_pattern) 
            all_patterns_with_alts.append(pattern)
        if len(all_patterns_with_alts) > 0:
            return all_patterns_with_alts
    '''
    return False

def add_sub_patterns(pattern_list, nested_variables):
    ''' get subsequent patterns since pattern_list[i] was a list
        if set is complete according to len(pattern_list), reset trackers & add to all_patterns
        you can replace these with a variable just like you replaced nested patterns with variables
    '''
    ''' you could generate a dict of lists with initial vars or indexes as keys 
        or create sets of variable replacement values and then iterate through pattern_list, 
        replacing vars with those in order
    '''
    all_sub_patterns = []
    pattern_string = ' '.join(pattern_list)
    new_pattern_words = []
    var_sets = []
    var_set = []
    variable_lists = {}
    ''' nested_variables = { 'x': 'NN ADV RR Q', 'y': 'JJ ADJ B' } '''
    #positions of x & y = [0, 2]
    #generate every non-repeating combination of them: [0, 2] and [2, 0]
    # pattern_list = ['x', 'of', 'y']
    value_sets = []
    final_sets = []
    all_list_strings = []
    ordered_var_lists = []
    sorted_keys = sorted(nested_variables.keys())
    for key in sorted_keys:
        val_list = nested_variables[key].split(' ')
        value_sets.extend(val_list)
        ordered_var_lists.append(val_list)
    list_length = len(nested_variables.keys())
    combinations = itertools.combinations(value_sets, list_length)
    for c in combinations:
        for i, key in enumerate(sorted_keys):
            new_list = []
            for j, item in enumerate(c):
                if item in ordered_var_lists[j]:
                    new_list.append(item)
            if len(new_list) == list_length:
                new_list_string = ' '.join(new_list)
                if new_list_string not in all_list_strings:
                    final_sets.append(new_list)
                    all_list_strings.append(new_list_string)
    new_lists = []
    for varset in final_sets:
        new_list = []
        for i, piece in enumerate(pattern_list):
            if piece in nested_variables:
                var_index = sorted_keys.index(piece)
                var_value = varset[var_index]
                new_list.append(var_value)
            else:
                new_list.append(piece)
        if len(new_list) > 0:
            new_list_string = ' '.join(new_list)
            new_lists.append(new_list_string)
    if len(new_lists) > 0:
        return new_lists
    return False

def get_repeated_patterns(pattern, all_vars):
    ''' this function adds an integer index to any repeated items '''
    new_words = []
    for i, w in enumerate(pattern):
        ''' w = V, V1, VB, VB1, the, the1 '''
        nonnumeric_w = get_nonnumeric(w, all_vars)
        if w == nonnumeric_w:
            if variant_pattern.count(w) > 1:
                new_word = ''.join([w, str(i)])
            else:
                new_word = w
        else:
            new_word = w
        new_words.append(new_word)
    if len(new_words) > 0:
        return ' '.join(new_words)
    return pattern
    
def get_correct_patterns(pattern, all_vars):
    '''
        - words like 'bear', 'worm', 'rat' will be logged as a verb even when preceded by determiner
        - add pattern_map word_pos entries to convert words to the correct pos: 
            'DT V1 V2 V3' => 'DT N V1 V2' if V1 can be a noun
        - this function corrects patterns with incorrect mappings like:
             'the VB VB VB IN the NN' to 'the NN VB VB IN the NN'
    '''
    return pattern

def get_type_patterns(pattern, all_vars):
    ''' 
    to do: implement after get_types 
        Cytotoxicity in cancer cells => <component object>-toxicity, anti-tumor => anti-<component object of illness>
        suppress/interfere/inhibit activity of carcinog/canc/tumz => suppress/interfere/inhibit activity of drug/medication/enzyme
    '''
    return [pattern]

def get_synonym_patterns(pattern, all_vars):
    return [pattern]

def get_operator_patterns(pattern, all_vars):
    return [pattern]

def get_function_patterns(pattern, all_vars):
    ''' find functions in pattern & replace with their core function decomposition '''
    functions = get_functions(pattern)
    if functions:
        for f in functions:
            core_functions = get_core_functions(f)
            if core_functions:
                ''' replace f with core_functions in pattern '''
                for cf in core_functions:
                    pattern = pattern.replace(function, cf)
    return [pattern]

def get_all_versions(pattern, version_types, all_vars):
    ''' this is to generate patterns with standardized synonyms, operators, & types in configured patterns '''
    processing_types = ['correct', 'repeated']
    chained_types = ['nested', 'alt', 'pos', 'type', 'synonym', 'operator']
    extra_processing = ['function']
    ''' if its a function, replace it with its core function decomposition '''
    version_types = all_vars['all_version_types'] if version_types == 'all' or len(version_types) == 0 else version_types
    for process in processing_types:
        function_name = ''.join(['get_', process, '_patterns'])
        if function_name in locals():
            try:
                function = getattr(locals(), function_name)
                if function:
                    new_pattern = function(pattern)
                    pattern = new_pattern if new_pattern else pattern
            except Exception as e:
                print('e', e)

    ''' pattern = 'VB |JJ NN|' '''
    ''' feed output of each chained_types function into the next '''

    patterns_to_iterate = []
    nested_patterns, nested_variables = get_nested_patterns(pattern, 'pattern', {}, all_vars)
    ''' nested_patterns = 'VB x', nested_variables = {'x': 'JJ NN'} '''

    for np in nested_patterns:
        alt_patterns = get_alt_patterns(np, nested_variables, all_vars)
        if alt_patterns:
            for ap in alt_patterns:
                patterns_to_iterate.append(ap)
    ''' patterns_to_iterate = ['VB JJ', VB NN'] '''

    all_patterns = []
    if len(patterns_to_iterate) > 0:
        for p in patterns_to_iterate:
            ''' 
            get_pos_patterns creates a list of nonnumeric/general/specific 
            pattern variants for each word pos type 
            '''
            variant_patterns = get_pos_patterns(p, all_vars)
            if variant_patterns:
                for vp in variant_patterns:
                    type_patterns = get_type_patterns(vp, all_vars)
                    if type_patterns:
                        for tp in type_patterns:
                            synonym_patterns = get_synonym_patterns(tp, all_vars)
                            if synonym_patterns:
                                for sp in synonym_patterns:
                                    operator_patterns = get_operator_patterns(sp, all_vars)
                                    if operator_patterns:
                                        for op in operator_patterns:
                                            all_patterns.append(op)
    if len(all_patterns) > 0:
        return all_patterns
    return False

def generate_patterns_for_pattern(pattern, all_vars):
    patterns = []
    all_patterns = get_all_versions(pattern, 'all', all_vars)
    if all_patterns:
        patterns.extend(alt_patterns)
    if len(patterns) > 0:
        return patterns, variables
    return False, False

def get_original_pattern_length(pattern, delimiter):
    ''' for a pattern like  '|VB NN x| VB', should return 2 '''
    delimiter_count = pattern.count(delimiter)
    delimiter_pair_count = delimiter_count / 2
    delimiter_index = 0
    reduced_pattern = []
    for i, char in enumerate(pattern):    
        if char == delimiter:
            delimiter_index += 1
        elif delimiter_index == 0 or (delimiter_index/2 == int(delimiter_index/2)):
            reduced_pattern.append(char)
    reduced_pattern_string = ''.join(reduced_pattern)
    reduced_pattern_string = reduced_pattern_string.replace('  ',' ')
    space_count = reduced_pattern_string.count(' ')
    final_count = delimiter_count + space_count
    if final_count > 0:
        return final_count
    return False

def get_pos_patterns(pattern, all_vars):
    ''' this function generates all the pos_type variants of a pattern 
        - this is necessary for pattern maps where the source pos type & target pos type 
            are a set:subset relationship (V: VBD, V1: VBD2) rather than equivalent (VBD: VBD, VBD1: VBD2)
            or patterns that have specific source words (the) vs. their target pos type (DT, DT1)

        - rather than check counts with counts in a comparison pattern, we're generating all pattern variants

        to do:
            - add support for mapping a source var like V1 to a target var like VB1

        pattern = 'the0 N1 VBD the1' should produce a list: [
            'the0 N1 VBD the1', # original pattern
            'the N VBD the', # numbers removed
            'the0 N1 V the1', # specific pos_tags converted to general pos_types

            'DT0 N1 VBD DT1', # original pattern with words converted to specific pos_type
            'DT N VBD DT', # numbers removed
            'DT0 N1 V DT1', # specific pos_tags converted to general pos_types & words converted to specific pos_type

            'D0 N1 VBD D1', # original pattern with words converted to general pos_type
            'D N VBD D', # numbers removed
            'D0 N1 V D1', # specific pos_tags converted to general pos_types & words converted to general pos_type
        ]
    '''
    delimiters = ['|', '__', '&']
    for d in delimiters:
        pattern = pattern.replace(d, '')
    all_indexed_patterns = []
    ''' all words converted the same '''
    all_s = []
    all_g = []
    nonnumeric = []
    nonnumeric_s = []
    nonnumeric_g = []
    ''' different conversions tag/word '''
    sg_tag = []
    gs_tag = []
    sg_tag_word_s = []
    sg_tag_word_g = []
    gs_tag_word_s = []
    gs_tag_word_g = []
    for w in pattern.split(' '):
        nonnumeric_w = get_nonnumeric(w, all_vars)
        nonnumeric.append(nonnumeric_w)
        specific = convert_to_pos_type(w, nonnumeric_w, 'specific', all_vars)
        if specific:
            all_s.append(specific)
            nonnumeric_specific = get_nonnumeric(specific, all_vars)
            nonnumeric_s.append(nonnumeric_specific)
        general = convert_to_pos_type(w, nonnumeric_w, 'general', all_vars)
        if general:
            all_g.append(general)
            nonnumeric_general = get_nonnumeric(general, all_vars)
            nonnumeric_g.append(nonnumeric_general)
        is_supported = is_supported_tag(nonnumeric_w, all_vars)
        if is_supported:
            if nonnumeric_w in all_vars['pos_tags']:
                ''' general tag '''
                if specific:
                    gs_tag_word_s.append(specific)
                    gs_tag_word_g.append(specific)
            else:
                ''' specific tag '''
                if general:
                    sg_tag_word_s.append(general)
                    sg_tag_word_g.append(general)
        else:
            ''' word '''
            if specific:
                gs_tag_word_s.append(specific)
                gs_tag_word_g.append(specific)
            if general:
                sg_tag_word_s.append(general)
                sg_tag_word_g.append(general)
            ''' no conversion for word '''
            sg_tag.append(w)
            gs_tag.append(w)
    pattern_list = [pattern, all_s, all_g, nonnumeric, nonnumeric_s, nonnumeric_g, sg_tag, gs_tag]
    pattern_list.append(sg_tag_word_s)
    pattern_list.append(sg_tag_word_g)
    pattern_list.append(gs_tag_word_s)
    pattern_list.append(gs_tag_word_g)
    if len(pattern_list) > 0:
        return pattern_list[0]
    return [pattern]

def convert_to_pos_type(word, nonnumeric_w, pos_type, all_vars):
    is_supported = is_supported_tag(nonnumeric_w, all_vars)
    if is_supported:
        ''' pos type '''
        if pos_type == 'specific':
            return nonnumeric_w
        else:
            for pos_key, values in all_vars['pos_tags'].items():
                if nonnumeric_w in values:
                    return pos_key
    else:
        ''' word '''
        pos = get_nltk_pos(nonnumeric_w, all_vars)
        if pos:
            if pos_type == 'specific':
                return pos
            else:
                for pos_key, values in all_vars['pos_tags'].items():
                    if pos in values:
                        return pos_key
    return False

def get_partial_pos(pattern, all_vars):
    new_pattern_words = []
    for w in pattern.split(' '):
        nonnumeric_w = get_nonnumeric(w, all_vars)        
        if nonnumeric_w in all_vars['pos_tags']['ALL']:
            for pos_key in ['V', 'N', 'D', 'P', 'C', 'ADV', 'ADJ']:
                if nonnumeric_w in all_vars['pos_tags'][pos_key] or nonnumeric_w == pos_key:
                    new_pattern_words.append(pos_key)
        else:
            new_pattern_words.append(w)
    if len(new_pattern_words) > 0:
        return ' '.join(new_pattern_words)
    return pattern

def is_supported_tag(var, all_vars):
    if var in all_vars['pos_tags']['ALL'] or var in all_vars['pos_tags']:
        return True
    return False

def get_nonnumeric(var, all_vars):
    nonnumeric_var = ''.join([x for x in var if x.lower() in all_vars['alphabet']])
    if len(nonnumeric_var) > 0:
        return nonnumeric_var
    return var

def get_new_key(key_dict, source_line, all_vars):
    new_key = None
    upper_limit = len(all_vars['alphabet']) - 1
    random_index = random.randint(0, upper_limit)
    random_letter = all_vars['alphabet'][random_index]
    if key_dict:
        for k in key_dict:
            new_key = ''.join([k, random_letter])
    else:
        new_key = random_letter
    if new_key:
        if new_key in key_dict or new_key in source_line.split(' '):
            return get_new_key(key_dict, source_line, all_vars)
        else:
            return new_key
    return False 

def read(path):
    index = None
    if 'DS_Store' not in path:
        if os.path.exists(path):
            with open(path, 'r') as f:
                index = json.load(f) if 'json' in path else f.read()
                f.close()
    return index

def get_singular(word):
    wl = WordList((word))
    singular_list = wl.singularize()
    if len(singular_list) > 0:
        for item in singular_list:
            return item
    return False

def get_stem(word):
    stem = stemmer.stem(word)
    if stem:
        return stem 
    return word

def find_delimiter(line, all_vars):
    delimiters = [c for c in line if c.lower() not in all_vars['alphabet']] 
    if len(delimiters) > 0:
        max_delimiter = max(delimiters)
        if max_delimiter:
            return max_delimiter
    delimiter = ' ' if ' ' in line else ''
    return delimiter
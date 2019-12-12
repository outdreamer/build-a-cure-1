from utils import *
from get_pos import *
from get_synonyms import fill_synonyms, aggregate_synonyms_of_type

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
    all_vars['medical_sentence_terms'] = ['y', 'ic', 'ia', 'al', 'ment', 'tion'] 
    plural_keys = [
        'conditions', 'tests', 'states', 'limits', 'participants', 'mechanisms', 'causal_layers', 'side_effects', 
        'metrics', 'alternates', 'observations', 'results', 'conclusions', 'symptoms', 'treatments', 'hypotheses', 
        'strategies', 'compounds', 'components', 'intents'
    ]
    all_vars['plural_map'] = {}
    for pk in plural_keys:
        all_vars['plural_map'][pk] = get_singular(pk)

    all_vars['full_params'] = {
        'request': ['metadata', 'generate', 'filters', 'data'], # request params
        'wiki': ['section_list'],
        'pos': ['verbs', 'nouns', 'common_words', 'counts', 'taken_out'],
        'structure': ['types', 'names', 'modifiers', 'phrases', 'clauses', 'subjects', 'patterns', 'variables', 'relationships', 'similar_lines'], # structural
        'experiment': ['hypothesis', 'tests', 'metrics', 'properties', 'assumptions'], # experiment elements
        'compound': ['compounds', 'contraindications', 'interactions', 'side_effects', 'treatments_successful', 'treatments_failed'], # drug elements
        'organism': ['genes', 'gene_expressions', 'evolution', 'organs', 'cells', 'nutrients'],
        'condition': ['symptoms', 'conditions', 'diagnosis', 'phases'], # separate diagnosis bc theyre not always accurate so not equivalent to condition
        'context': ['bio_metrics', 'bio_symptoms', 'bio_conditions', 'bio_stressors'], # context elements
        'synthesis': ['instructions', 'parameters', 'optimal_parameter_values', 'required_compounds', 'substitutes', 'equipment_links'],
        'relational': ['components', 'related', 'alternates', 'substitutes', 'sub', 'adjacents', 'stressors', 'dependencies'],
        'conceptual': ['concepts', 'functions', 'causal_stack', 'insights', 'strategies', 'prediction', 'priorities', 'intents', 'systems']
    }
    object_type_keys = {
        'medical': ['experiment', 'compound', 'organism', 'condition', 'context', 'synthesis'],
        'conceptual': ['conceptual', 'relational', 'pattern']
        'structural': ['pos', 'structure']
    }
    '''
    some of these types have mappings like with 
        condition = state
        symptom = function = side_effects
        function = relationship
        synthesis = build process
        structure = pattern
    so generalize when you can
    '''
    for key, val in object_type_keys:
        for ref in val:
            all_vars[key] = [item for item in all_vars['full_params'][ref]]
    all_vars['supported_params'] = []
    for key, val in all_vars['full_params'].items():
        all_vars['supported_params'].extend(val)
    all_vars['passive'] = [" by ", " from ", " of "]
    all_vars['pos_tags'] = get_pos_tags()
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
    all_vars['key_map'] = {
        '-': ['worsen', 'decrease', 'inhibit', 'reduce', 'deactivate', 'disable'],
        '+': ['improve', 'increase', 'induce', 'enhance', 'activate', 'enable'],
        '=': ['equal', 'alternate']
    }
    all_vars['charge'] = {
        '-': aggregate_synonyms_of_type(all_vars, '-'), # antagonist, reduce, inhibit, deactivate, toxic, prevents
        '+': aggregate_synonyms_of_type(all_vars, '+'), # help, assist, enhance, induce, synergetic, sympathetic, leads to
        '=': aggregate_synonyms_of_type(all_vars, '=') # means, signifies, indicates, implies, is, equates to
    }
    ''' to do: use get_charge_of_word in get_clauses '''
    ''' to do: assess which operator combinations neutralize or negate a relationship '''
    all_vars['combined_map'] = {
        '=': ['=-', '-=', '=+', '+=', '=='], #"x = (i - b)" => x and b equal i
        '-': ['-+', '+-'],
        '+': ['--', '++'],
        '#': [
            '# &', # even with x
            '# !', # even without x
            '~ !' # does not increase => 'neutral' or 'independent', 'does not increase' doesnt mean 'decrease'
            #'! noun' # no increase => 'independent'
        ]
    }
    all_vars['clause_map'] = {
        '-' : ["decrease"], # attacks
        '+' : ["increase"], # helps
        '=': ['is', 'like', 'equate', 'equal', 'describe', 'indicate', 'delineate', 'same', 'like', 'similar', 'imply', 'signify', 'mean'],
        '&': ['and', 'with'],
        '|': ['or'],
        '^': ['but', 'yet', 'but yet', 'but rather', 'but actually', 'still', 'without', 'however', 'nevertheless' 'in the absence of', 'lacking'], # except and without
        '%': [
            'because', 'as', 'since', 'if', 'then', 'from', 'due', 'when', 'while', 'during', 'for', 'given',
            'in case', 'in the event that', 'caused by', 'respective of'
        ], # x of y is contextual "x in the context of y"
        '#': ['even', 'still', 'despite', 'otherwise', 'in spite of', 'regardless', 'heedless', 'irrespective'],
        '!': ['not', 'without'],
        '~': ['function']
    }
    all_vars['operator_map'] = {
        '-' : "decrease", # attacks
        '+' : "increase", # helps
        '=' : "equal", # is
        '&' : "union", # with, union
        '|' : "alternate", # or
        '^' : "exception", # without
        '%' : "dependent", # apply
        '#' : "independent" # by standard
        '!' : "not" # negating an noun or verb
    }
    all_vars['clause_delimiters'] = [',', ':', ';']
    for operator, keyword_list in all_vars['clause_map'].items():
        all_vars['clause_delimiters'].extend(keyword_list)

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
    all_vars['pos_patterns'] = [
        'JJ NN',
        '|ADV VB| NN',
        'NN of NN NN',
        'NN of NN',
        '|VB NN| role',
        '|functions works operates interacts acts| as __a__ |VB NN|'
    ]
    all_vars['keywords'] = {
        'treatments': [],
        'compounds': {
            'object': ['ion', 'acid'],
            'modifiers': ['oral', 'liquid', 'topical', 'intravenous', 'iv', 'injection', 'gavage', 'capsule', 'gel', 'powder', 'supplement', 'solution', 'spray', 'tincture', 'mixture'],
        },
        'patient': all_vars['supported_core']['participants']
    }
    # use participant instead of patient bc that has other meanings
    all_vars['pattern_maps'] = {
        'passive_to_active': {
            'x of y': 'y-x'
        }
    }
    all_vars['pattern_index'] = {
        'pos': {
            'noun': [
                'the noun',
                'noun of'
            ],
            'passive': [
                '|VB VBP VBN VBD| |VB VBP VBN VBD|', # is done, was done
                'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', # having been done
                '|VB VBP VBN VBD| |TO IN PP|', # finish by, done by
                '|VBD| VBN VBN |TO IN PP|', # has been done by
                '|noun verb| of |noun verb|' # inhibitor of protein 
            ],
            'modifier': [
                'noun-noun', # the second noun has a verb root, ie "enzyme-inhibitor"
                'noun noun', 
                'noun-verb',
                'noun verb', 
                '[noun adv adj verb] [noun verb]', # detoxified compound
                '[noun verb] [noun adv adj verb]' # compound isolate
                '|NN VB VP VBP VBG VBN VBD VBZ| |NN NNS NNP NNPS JJ JJR|',
                '|NN VB VP VBP VBG VBN VBD VBZ|-|NN NNS NNP NNPS JJ JJR|',
                '|NN NNS NNP NNPS JJ JJR| of |NN NNS NNP NNPS JJ JJR|'
            ]
        },
        'compound' = [
            "administration_method of compound",
            "compound compound"
        ],
        'symptom': [
            'fever that gets worse when x',
            'x reduced y and diminished z even in condition x or condition a'
        ],
         'type': [
            '<adj> <noun>', # Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')
        ],
        'role': [
            '|<adv> <verb> <noun>|', # Ex: 'emulsifying protein' (role = 'emulsifier')
            '<noun> of <noun>', # Ex: 'components of immune system' (role = 'component', system = 'immune system')
            '|<verb> <noun>| role', # Ex: functional role (role => 'function')
            '|functions works operates interacts acts| as (a) |<verb> <noun>|' # Ex: acts as an intermediary (role => 'intermediary')
        ]
    }
    '''
    if there are files with the 'data/objecttype_patterns.txt' name pattern, 
    pull that data and add it to pattern_index dict 
    '''
    for key in all_vars:
        cwd = getcwd()
        pattern_filename = ''.join([cwd, 'data/patterns_', key, '.txt'])
        if os.file.exists(pattern_filename):
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

    all_vars['pos_patterns'] = convert_pos_names_to_nltk_tags(all_vars['pos_patterns'], all_vars)
    all_vars['supported_tags'] = ['noun', 'adj', 'verb', 'adv']
    return all_vars
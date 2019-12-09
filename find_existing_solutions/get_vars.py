from utils import read

def convert_patterns(lang_patterns, all_vars):
    '''
    this function converts esoteric terms like 'NN' into common words like 'noun' 
    in the set of configured patterns
    '''
    patterns = []
    for p in lang_patterns:
        pattern = []
        for alt_phrases in p.split('--'):
            pos_list = alt_phrases.split(' ')
            all_pos = [True for pos_item in pos_list if pos_item in all_vars['language_pos_map'].keys()]
            if len(all_pos) == len(pos_list):
                ''' this is a set of alternative parts of speech '''
                final_list= ['[']
                for item in pos_list:
                    final_list.append(all_vars['language_pos_map'][item].replace('[','').replace(']',''))
                final_list.append(']')
                pattern.append(''.join(final_list))
        for i, w in enumerate(p.split(' ')):
            if w in all_vars['language_pos_map'].values():
                pattern.append(all_vars['language_pos_map'][w])
            else:
                pattern.append(w)
        patterns.append(' '.join(pattern))
    if len(patterns) > 0:
        return patterns
    return False

def get_args(arg_list, all_vars):
    metadata_keys = ''
    generate_source = ''
    generate_target = ''
    args_index = {}
    filters_index = {}
    for i, arg in enumerate(arg_list):
        arg_key = arg.replace('--', '').replace('-', '_')
        print('arg key', arg_key)
        if arg_key in all_vars['supported_params']:
            arg_val = arg_list[i + 1]
            if arg_key == 'metadata':
                if arg_val in all_vars['supported_params'] or arg_val == 'all':
                    metadata_keys = arg_val.split(',')
            elif arg_key == 'filters':
                # --filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
                filters_index = { key: val.split(',') for key, val in arg_val.split(',') } # val will be metricC::metricvalue for metric
            elif arg_key == 'generate':
                generate_list = arg_val.split('::')
                source_list = generate_list[0].split(',')
                generate_source = [s for s in source_list if s in all_vars['supported_params']]
                generate_target = generate_list[1]
            else:
                args_index[arg_key] = arg_val.split(',')
    print('args_index', args_index)
    print('filters', filters_index)
    print('metadata', metadata_keys)
    print('generate', generate_target, generate_source)
    return args_index, filters_index, metadata_keys, generate_target, generate_source

def get_vars():
    verb_contents = read('data/verbs.txt')
    standard_verbs = set('increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable')
    all_vars = {}
    all_vars['standard_verbs'] = set(verb_contents.split('\n')) if verb_contents is not None else standard_verbs
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
    all_vars['medical_sentence_terms'] = ['y', 'ic', 'ia', 'al', 'ment', 'tion'] 
    all_vars['clause_delimiters'] = [',', 'and', 'or', 'because', 'but', 'as', 'if', 'then', 'even', 'without']
    all_vars['operator_map'] = {
        '-' : "decreases",
        '+' : "increases",
        '=' : "equals",
        #'w' : "addition", # with
        #'s' : "subtraction", # without
        #'m' : "multiplication", # apply
        #'d' : "division" # by standard
    }
    all_vars['combined_map'] = {
        'equal': ['=-', '-=', '=+', '+=', '=='], #"x = (i - b)" => x and b equal i
        'negative': ['-+', '+-'],
        'positive': ['--', '++']
    }
    all_vars['numbers'] = '0123456789'
    all_vars['alphanumeric'] = 'abcdefghijklmnopqrstuvwxyz0123456789- '
    all_vars['alphabet'] = 'abcdefghijklmnopqrstuvwxyz'
    all_vars['full_params'] = {
        'request': ['metadata', 'generate', 'filters'], # request params
        'wiki': ['section_list'],
        'pos': ['verbs', 'nouns', 'subjects', 'clauses', 'common_words', 'counts', 'names', 'relationships', 'taken_out', 'phrases', 'title_similarities'], # elements organized by structure
        'experiment': ['hypothesis', 'tests', 'metrics', 'properties'], # experiment elements
        'compound': ['compounds', 'contraindications', 'interactions', 'side_effects', 'treatments_successful', 'treatments_failed'], # drug elements
        'condition': ['symptoms', 'conditions'], # condition elements
        'context': ['bio_metrics', 'bio_symptoms', 'bio_conditions', 'bio_stressors'], # context elements
        'synthesis': ['instructions', 'parameters', 'optimal_parameter_values', 'required_compounds', 'substitutes', 'equipment_links', 'adjacent_compound_synthesis'],
        'interaction': ['components', 'related', 'alternates', 'substitutes', 'adjacent', 'stressors', 'dependencies'], # interaction elements
        'conceptual': ['variables', 'systems', 'functions', 'insights', 'strategies', 'patterns', 'usage_patterns', 'priorities', 'intents', 'types', 'causal_layers'] # conceptual elements
    }
    all_vars['supported_params'] = []
    for key, val in all_vars['full_params'].items():
        all_vars['supported_params'].extend(val)
    all_vars['pattern_categories'] = {
        'types': [
            'adjective noun'
        ],
        'roles': [
            'adverb || verb noun',
            'noun of noun',
            'verb || noun role',
            'functions/works/operates/interacts/acts as (a) verb || noun'
        ],
        'noun': [
            'the noun'
        ]
    }
    ''' () indicates an optional item, --a b c-- indicates a set of alternatives '''
    all_vars['language_patterns'] = [
        'adjective noun',
        '--adverb verb-- noun',
        'noun of noun noun',
        'noun of noun',
        '--verb noun-- role',
        '--functions works operates interacts acts-- as (a) --verb noun--'
    ]
    all_vars['language_pos_map'] = {
        'adjective': '[ADJ]',
        'noun': '[NN||NNP||NNS||JJ||JJR]',
        'adverb': '[ADV]',
        'verb': '[VB||VBP||VBD||VBG||VBN||VBZ]',
        'past_participle': '[VBN]',
    }
    all_vars['patterns'] = convert_patterns(all_vars['language_patterns'], all_vars)
    all_vars['pattern_words'] = ['of', 'acts', 'as']
    all_vars = fill_synonyms('maps', all_vars)
    all_vars['key_map'] = {
        'negative': ['worsen', 'decrease', 'inhibit', 'reduce', 'deactivate', 'disable'],
        'positive': ['improve', 'increase', 'induce', 'enhance', 'activate', 'enable'],
        'equal': ['equal', 'alternate']
    }
    all_vars['charge'] = {
        'negative': aggregate_synonyms_of_type(all_vars, 'negative'), # antagonist, reduce, inhibit, deactivate, toxic, prevents
        'positive': aggregate_synonyms_of_type(all_vars, 'positive'), # help, assist, enhance, induce, synergetic, sympathetic, leads to
        'equal': aggregate_synonyms_of_type(all_vars, 'equal') # means, signifies, indicates, implies, is, equates to
    }
    return all_vars
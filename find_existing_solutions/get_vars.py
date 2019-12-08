from nltk.stem.snowball import SnowballStemmer
from utils import read
stemmer = SnowballStemmer("english")

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
    all_vars = {}
    all_vars['pattern_words'] = ['of', 'acts', 'as']
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
    all_vars['operator_map'] = {
        '-' : "decreases",
        '+' : "increases",
        '=' : "equals",
        'w' : "addition", # with
        's' : "subtraction", # without
        'm' : "multiplication", # apply
        'd' : "division" # by standard
    }
    all_vars['combined_map'] = {
        'equal': ['=-', '-=', '=+', '+=', '=='], #"x = (i - b)" => x and b equal i
        'negative': ['-+', '+-'],
        'positive': ['--', '++']
    }
    all_vars['numbers'] = '0123456789'
    all_vars['alphanumeric'] = 'abcdefghijklmnopqrstuvwxyz0123456789- '
    all_vars['alphabet'] = 'abcdefghijklmnopqrstuvwxyz'
    all_vars['key_map'] = {
        'negative': ['worsen', 'decrease', 'inhibit', 'reduce', 'deactivate', 'disable', 'negative_substrings'],
        'positive': ['improve', 'increase', 'induce', 'enhance', 'activate', 'enable', 'positive_substrings'],
        'equal': ['equal']
    }
    all_vars['full_params'] = {
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
    all_vars['supported_synonyms'] = get_supported_synonyms('synonyms.json', all_vars)
    all_vars['synonym_list'] = {
        'negative': get_synonym_list(all_vars['supported_core'], all_vars['key_map'], 'negative'), # antagonist, reduce, inhibit, deactivate, toxic, prevents
        'positive': get_synonym_list(all_vars['supported_core'], all_vars['key_map'], 'positive'), # help, assist, enhance, induce, synergetic, sympathetic, leads to
        'equal': get_synonym_list(all_vars['supported_core'], all_vars['key_map'], 'equal') # means, signifies, indicates, implies, is, equates to
    }
    return all_vars

def get_supported_synonyms(path, all_vars):
    word_map = read(path)
    if word_map:
        all_vars['supported_core'] = word_map['standard_words'] if 'standard_words' in word_map else {}
        supported_synonyms = set()
        for x in all_vars['supported_core'].keys():
            supported_synonyms.add(x)
            for y in all_vars['supported_core'][x]:
                supported_synonyms.add(y)
        return supported_synonyms
    return False

def get_synonym_list(supported_core, key_map, synonym_type):
    '''
    supported_core = word_map['standard_words'] from synonyms.json
    key_map = {
        'negative': ['decrease', ...],
        'positive': ['increase', ...],
        'equal': ['means', 'equals', ...]
    } 
    '''
    if synonym_type in key_map:
        synonyms = {}
        for key in supported_core:
            if key in key_map[synonym_type]:
                for k in supported_core[key]:
                    synonyms[k] = stemmer.stem(k)
        if synonyms:
            return synonyms 
    return False
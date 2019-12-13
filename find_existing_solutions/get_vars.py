from utils import *
from get_pos import *
from get_synonyms import fill_synonyms
from get_pattern_def import get_pattern_config

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

    all_vars['full_params'] = {
        'request': ['metadata', 'generate', 'filters', 'data'], # request params
        'wiki': ['section_list'],
        'pos': ['pos', 'verbs', 'nouns', 'common_words', 'counts', 'taken_out'],
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
        'medical': ['experiment', 'compound', 'organism', 'condition', 'context', 'synthesis'],
        'conceptual': ['conceptual', 'relational'],
        'structural': ['pos', 'structure']
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
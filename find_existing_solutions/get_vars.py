from utils import read

def get_args(arg_list, all_vars):
    metadata_keys = ''
    generate_source = ''
    generate_target = ''
    args_index = {}
    filters_index = {}
    for i, arg in enumerate(arg_list):
        arg_key = arg.replace('--', '').replace('-', '_')
        if arg_key in all_vars['supported_params']:
            arg_val = arg_list[i + 1]
            if arg_key == 'metadata':
                if arg_val in all_vars['supported_params'] or arg_val == 'all':
                    metadata_keys = arg_val.split(',')
            elif arg_key == 'filters':
                # |filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
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
    print('metadata', metadata_keys, 'generate', generate_target, generate_source)
    return args_index, filters_index, metadata_keys, generate_target, generate_source

def get_vars():
    verb_contents = read('data/verbs.txt')
    standard_verbs = set('increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable')
    all_vars = {}
    all_vars['standard_verbs'] = set(verb_contents.split('\n')) if verb_contents is not None else standard_verbs
    all_vars['numbers'] = '0123456789'
    all_vars['alphanumeric'] = 'abcdefghijklmnopqrstuvwxyz0123456789- '
    all_vars['alphabet'] = 'abcdefghijklmnopqrstuvwxyz'
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
    all_vars['full_params'] = {
        'request': ['metadata', 'generate', 'filters'], # request params
        'wiki': ['section_list'],
        'pos': ['verbs', 'nouns', 'subjects', 'clauses', 'common_words', 'counts', 'names', 'relationships', 'taken_out', 'phrases', 'title_similarities'], # elements organized by structure
        'experiment': ['hypothesis', 'tests', 'metrics', 'properties'], # experiment elements
        'compound': ['compounds', 'contraindications', 'interactions', 'side_effects', 'treatments_successful', 'treatments_failed'], # drug elements
        'condition': ['symptoms', 'conditions'], # condition elements
        'context': ['bio_metrics', 'bio_symptoms', 'bio_conditions', 'bio_stressors'], # context elements
        'synthesis': ['instructions', 'parameters', 'optimal_parameter_values', 'required_compounds', 'substitutes', 'equipment_links'],
        'interaction': ['components', 'related', 'alternates', 'substitutes', 'adjacent', 'stressors', 'dependencies'], # interaction elements
        'pattern': ['line_patterns', 'pattern_stack', 'usage_patterns'],
        'conceptual': ['variables', 'systems', 'functions', 'insights', 'strategies', 'priorities', 'intents', 'types', 'causal_layers'] # conceptual elements
    }
    all_vars['operator_phrases'] = {
        'and': ['with'],
        'or': [],
        'like': ['similar to'],
        'without': ['in the absence of', 'lacking'],
        'when': ['while', 'during', 'for'],
        'but': ['however', 'but yet', 'yet', 'still'],
        'because': ['because of', 'caused by', 'from', 'since', 'respective of', 'due to'], 
        'even': ['despite', 'in spite of', 'regardless of', 'heedless of', 'irrespective of'],
        'if': ['in case', 'in the event that'],
        'before': ['if'],
        'after': ['then'],
        'is': ['equate', 'equal', 'describe', 'indicate', 'delineate', 'same', 'like', 'similar', 'imply', 'signify', 'means']
      },
    all_vars['conceptual_clause_map'] = {
        'union': ['and', 'with'],
        'exception': ['but', 'yet'],
        'dependence': ['because', 'since', 'due', 'caused by'],
        'independence': ['even', 'still', 'despite', 'in spite of', 'regardless', 'irrespective'],
        'conditional': ['when', 'while', 'during', 'for', 'x of y'],
        'alternate': ['or'],
        'equal': ['is']
    }
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
    all_vars['supported_params'] = []
    for key, val in all_vars['full_params'].items():
        all_vars['supported_params'].extend(val)

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

    all_vars['pattern_categories'] = {
        'types': [
            'adjective noun'
        ],
        'roles': [
            '|adverb verb| noun',
            'noun of noun',
            '|verb noun| role',
            '|functions works operates interacts acts| as __a__ |verb noun|'
        ],
        'noun': [
            'the noun'
        ]
    }
    all_vars['language_patterns'] = [
        'JJ NN',
        '|ADV VB| NN',
        'NN of NN NN',
        'NN of NN',
        '|VB NN| role',
        '|functions works operates interacts acts| as __a__ |VB NN|'
    ]
    all_vars['pattern_index'] = {
        'passive': [
            '|VB VBP VBN VBD| |VB VBP VBN VBD|', # is done, was done
            'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', # having been done
            '|VB VBP VBN VBD| |TO IN PP|', # finish by, done by
            '|VBD| VBN VBN |TO IN PP|', # has been done by
            '|noun verb| of |noun verb|' # inhibitor of protein 
        ]
    }
    '''
    VB: Verb, base form - ask is do have build assess evaluate analyze assume avoid begin believe reveal benefit # attention?
        VBP: Verb, non-3rd person singular present - ask is do have
        VBZ: Verb, 3rd person singular present - asks is does has
        VBG: Verb, gerund or present participle - asking, being, doing, having
    VBD: Verb, past tense - asked, was/were, did, had
    VBN: Verb, past participle - asked, used, been, done, had
    '''

    all_vars['language_patterns'] = convert_nltk_tags_to_pos_names(all_vars['language_patterns'], all_vars)
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
    },
    all_vars['supported_tags'] = ['noun', 'adj', 'verb', 'adv']
    all_vars['name_tag_map'] = {
        'noun': 'NN',
        'verb': 'VB',
        'adv': 'ADV',
        'adj': 'JJ'
    }
    all_vars['tag_name_map'] = { item : tag_name for tag_name, tag_list in all_vars['pos_tags'].items() for item in tag_list }
    return all_vars
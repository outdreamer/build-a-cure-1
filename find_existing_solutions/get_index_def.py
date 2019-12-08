def get_empty_index(metadata_keys, full_params):
    '''
    indexes isolates treatments from symptoms, metrics, etc to build indexes of those objects on your local env
        indexes = {
            'counts': set(),
            'clauses': set(),
            'phrases': set(),
            'verbs': set(), # set of relationship verbs in the index set
            'nouns': set(),
            'names': set(),
            'title_similarities': set(),
            'taken_out': set(),
            'relationships': set(),
            'components': set(), # bio objects
            'conditions': set(),
            'symptoms': set(),
            'compounds': set(),
            'metrics': set(), # metric used to measure effectiveness of treatment
            'stressors': set(),
            'bio_conditions': set(),
            'bio_symptoms': set(),
            'bio_metrics': set(),
            'bio_stressors': set(),
            'synthesis_instructions': set(),
            'synthesis_parameters': set(),
            'synthesis_optimal_parameter_values': set(),
            'synthesis_required_compounds': set(),
            'synthesis_substitutes': set(),
            'synthesis_equipment_links': set(),
            'synthesis_adjacent_compounds_synthesis_steps': set(),
            'treatments_successful': set(),
            'treatments_failed': set(),
            'patterns': set(),
            'pattern_stack': set(),
            'functions': set(),
            'insights': set(), # useful sentences in index set that have bio rules in them - for abstracts this will likely just be the treatment success sentence
            'strategies': set(), # insights relevant to methods/mechanisms of action/processes or patterns of problem-solving
            'systems': set(),
            'variables': set(),
            'target_intents': set(),
            'avoid_intents': set(), # in addition to functions you want to target, there are functions you want to avoid as well
            'types': set(),
            'causal_layers': set(),
        }
    rows
        - ensures data remains tied to its original context
        - it has the same elements as index but stores them by each sentence 
          from source data containing a symptom, condition, treatment, etc
    rows = [
        {
            'conditions': ['meningitis'],
            'symptoms': ['temperature'],
            'treatments_successful': ['fluconazole'],
            'insights': ['fluconazole effective 10-week survival'],
            ...
        },
        {
            'conditions': ['diabetes'],
            'symptoms': ['organ failure'],
            'treatments_successful': ['metformin'],
            'insights': ['metformin effective for diabetes'],
            ...
        },
        {
            'metrics': {'naa-cr ratio': 'reduced'}
            'conditions': ['hiv', 'encephalopathy'],
            'components': {
                'organs': ['brain', 'immune system'],
                'microbes': [],
                'cells': [],
                'genes': [],
                'enzymes': [],
                'biosystems': ['immune system', 'nervous system']
            }
            'compounds': ['naa', 'cr'],
            'treatments_successful': [],
            'treatments_failed': [],
            'intents': ['diagnose'],
            'insights': [
                'naa-to-cr ratio is reduced in hiv patients', 
                'naa-to-cr ratio is a marker for hiv brain infection'
            ],
            "strategies": [
                'target bio markers that change with illness for testing',
                'consider other conditions like lack/excess of signals from diagnostic tests & interfering diseases'
            ],
            "symptoms": [
                'encephalopathy': 'no imaging findings',
                'neurological disease': 'other'
            ],
            "patient_conditions": ['HIV-positive'],
            "patient_symptoms": ['neurological disease']
        }
    ]
    '''
    index = {}
    index_keys = []
    for key in full_params.keys():
        if key != 'request':
            for item in full_params[key]:
                index_keys.append(item)
    metadata_keys = index_keys if 'all' in metadata_keys else metadata_keys
    for key in metadata_keys:
        index[key] = set() if key != 'counts' and key in index_keys else {}
    ''' 
    each main medical component deserves its own dictionary, which can be built with rows data
    'synthesis_instructions' = {
        'parameters',
        'optimal_parameter_values',
        'required_compounds',
        'substitutes',
        'equipment_links',
        'adjacent_compounds_and_steps',
    }
    'symptom' = {
        'attributes': [],
        'rules': [],
        'states': [],
        'treatments': []
    }
    'compounds' = {
        'attributes': [],
        'rules': [],
        'states': [],
        'side_effects': [] # this is just a list of symptoms the compound causes, which can be assembled from rows data
    }
    '''
    return index
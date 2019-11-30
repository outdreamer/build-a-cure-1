def get_empty_index(metadata):
    ''' 
    indexes isolates treatments from symptoms, metrics, etc to build indexes of those objects on your local env
        indexes = {
            'verbs': set(), # set of relationship verbs in the index set
            'relationships': set(),
            'components': set(), # bio objects
            'conditions': set(),
            'symptoms': set(),
            'compounds': set(),
            'metrics': set(), # metric used to measure effectiveness of treatment
            'stressors': set(),
            'patient_conditions': set(),
            'patient_symptoms': set(),
            'patient_metrics': set(),
            'patient_stressors': set(),
            'treatments_successful': set(),
            'treatments_failed': set(),
            'patterns': set(),
            'functions': set(),
            'insights': set(), # useful sentences in index set that have bio rules in them - for abstracts this will likely just be the treatment success sentence
            'strategies': set(), # insights relevant to methods/mechanisms of action/processes or patterns of problem-solving
            'systems': set(),
            'variables': set(),
            'intents': set(),
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
    
    index_keys = [
        'verbs', 'relationships', 'components',
        'conditions', 'symptoms', 'compounds', 'metrics', 'stressors',
        'patient_conditions', 'patient_symptoms', 'patient_metrics', 'patient_stressors',
        'treatments_successful', 'treatments_failed', 
        'patterns', 'functions', 'insights', 'strategies', 'systems', 
        'variables', 'intents', 'types', 'causal_layers'
    ]
    if metadata == 'all' or metadata == 'generate-all':
        index = { key : set() for key in index_keys}
    else:
        metadata_keys = metadata.split(',')
        index = { key : set() for key in metadata_keys if key in index_keys}
    ''' 
    each main medical component deserves its own dictionary, which can be built with rows data
    symptom = {
        'attributes': [],
        'rules': [],
        'states': [],
        'treatments': []
    }
    compounds = {
        'attributes': [],
        'rules': [],
        'states': [],
        'side_effects': [] # this is just a list of symptoms the compound causes, which can be assembled from rows data
    }
    '''
    return index
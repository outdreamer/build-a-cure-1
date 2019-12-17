def get_empty_index(all_vars):
    '''
    indexes isolates treatments from symptoms, metrics, etc to build indexes of those objects on your local env
    rows
        - ensures data remains tied to its original context
        - it has the same elements as index but stores them by each sentence 
          from source data containing a symptom, condition, treatment, etc
    rows = [
        {
            'condition': ['meningitis'],
            'symptom': ['temperature'],
            'treatments_successful': ['fluconazole'],
            'insight': ['fluconazole effective 10-week survival'],
            ...
        },
        {
            'condition': ['diabetes'],
            'symptom': ['organ failure'],
            'treatments_successful': ['metformin'],
            'insight': ['metformin effective for diabetes'],
            ...
        },
        {
            'metric': {'naa-cr ratio': 'reduced'}
            'condition': ['hiv', 'encephalopathy'],
            'component': {
                'organ': ['brain', 'immune system'],
                'microbe': [],
                'cell': [],
                'gene': [],
                'enzyme': [],
                'biosystem': ['immune system', 'nervous system']
            }
            'compound': ['naa', 'cr'],
            'treatments_successful': [],
            'treatments_failed': [],
            'intent': ['diagnose'],
            'insight': [
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
    for key in all_vars['full_params'].keys():
        if key != 'request':
            for item in all_vars['full_params'][key]:
                index_keys.append(item)
    dict_keys = ['count', 'pattern', 'pos', 'word_map']
    all_vars['metadata'] = index_keys if 'metadata' not in all_vars or 'all' in all_vars['metadata'] else all_vars['metadata']
    for key in all_vars['metadata']:
        if key in index_keys:
            if key not in dict_keys:
                index[key] = set()
            else:
                index[key] = {}
    index['data'] = [] # not necessary to ensure uniqueness in articles
    return index
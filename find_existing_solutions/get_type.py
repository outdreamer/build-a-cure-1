def get_index_type(word, all_vars, categories):
    ''' look through syns to find out which index element contains this word '''
    index_type = None
    full_keys = [
        'condition_keywords', 'state', 'treatment_keywords', 'elements', 'compounds', 'metrics', 
        'organisms', 'functions', 'causal_layers', 'symptom_keywords', 'side_effects'
    ]
    param_map = {}
    for keyword in full_keys:
        keyword = keyword.replace('_keywords', 's')
        param_map[keyword] = keyword
    for keyword in ['condition_keywords', 'state']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'conditions'
    for keyword in ['treatment_keywords', 'elements', 'compounds']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'compounds' 
            # not every compound will be a treatment
    for keyword in ['metrics']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'metrics'
    for keyword in ['organisms']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'organisms'
    for keyword in ['functions', 'causal_layers']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'functions'
    for keyword in ['symptom_keywords', 'side_effects']:
        for key in all_vars['supported_core'][keyword]:
            param_map[key] = 'symptoms'
            # assume its a symptom until you can associate it with a compound
    if len(categories) > 0:
        for c in categories:
            c_split = c.split(' ')
            for term in c_split:
                if term in param_map:
                    index_type = param_map[term]
        if not index_type:
            index_type = categories[0]
    return index_type

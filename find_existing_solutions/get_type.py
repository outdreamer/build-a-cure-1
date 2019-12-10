def get_index_type(word, all_vars, categories):
    param_map = {
        'conditions': 'state',
        'compounds': 'elements', # not every compound will be a treatment
        'symptoms': 'side_effects',
        'functions': 'causal_layers'
    }
    for object_type, keyword_list in all_vars['supported_core'].items():
        if word in keyword_list or word == object_type:
            return object_type
        alt_type = param_map[object_type]
        if word in all_vars['supported_core'][alt_type] or word == alt_type:
            return object_type
    if len(categories) > 0:
        for c in categories:
            c_split = c.split(' ')
            for term in c_split:
                index_type = None
                for k, v in param_map.items():
                    index_type = k if v == term else v if k == term else None
                    if index_type:
                        return index_type
        return categories[0]
    return False

def get_types(word, all_vars):
    return word

def get_index_type(object_type, all_vars, categories):
    param_map = {
        'conditions': 'state',
        'compounds': 'elements', # not every compound will be a treatment
        'symptoms': 'side_effects',
        'functions': 'causal_layers'
    }
    if object_type in all_vars['supported_synonyms']:
        return all_vars['supported_synonyms'][object_type]
    alt_type = param_map[object_type]
    if alt_type in all_vars['supported_synonyms']:
        return all_vars['supported_synonyms'][alt_type]
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

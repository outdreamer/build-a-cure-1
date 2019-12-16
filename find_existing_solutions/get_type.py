import wikipedia
from wikipedia.exceptions import DisambiguationError

def get_types(word, pos, title, row, all_vars):
    types = {}
    wikipedia.set_lang("en")
    suggested = None
    if pos in all_vars['pos_tags']['ALL_N']:
        ''' make sure this is a noun before querying '''
        if word[0] == word[0].upper() and word[1] != word[1].upper():
            suggested = get_generic_medication(word)
            suggested = wikipedia.suggest(word) if not suggested else suggested
            print('suggested', suggested, word)
            try:
                content = wikipedia.page(suggested).content
                section_list = [s.strip().replace(' ', '_').lower() for s in content.split('==') if '.' not in s and len(s) < 100]
                print('section list', section_list)
                categories = wikipedia.page(suggested).categories
                if len(categories) > 0:
                    row['types'] = row['types'].union(set(categories))
                    print('categories', categories)
                    if len(section_list) > 0:
                        ''' use section list to determine type first '''
                        for key, val in all_vars['section_map'].items():
                            for section in section_list:
                                if key in section:
                                    index_type =  val
                    else:
                        index_type = get_index_type(suggested, all_vars, categories)
                        if index_type:
                            print('found index type', index_type, word)
                            if index_type in row:
                                if index_type != 'dependencies': # to do: exclude other relationship objects here
                                    index = {index_type: word}
                                    matched_objects = find_patterns(word, index_type, all_vars)
                                    if matched_objects:
                                        for pattern_type in matched_objects.items():
                                            if pattern_type not in row:
                                                row[pattern_type] = []
                                            for pattern, matches in matched_objects[pattern_type].items():
                                                row[pattern_type].extend(matches)
            except Exception as e:
                print('wiki summary exception', e)
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

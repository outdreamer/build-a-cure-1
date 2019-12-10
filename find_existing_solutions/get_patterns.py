'''
- types follow patterns:
    1. <adjective> <noun>
        Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')

- roles follow patterns:
    1. |<adverb> <verb> <noun>|
        Ex: 'emulsifying protein' (role = 'emulsifier')

    2. <noun> of <noun>
        Ex: 'components of immune system' (role = 'component', system = 'immune system')

    3. |<verb> <noun>| role
        Ex: functional role (role => 'function')

    4. |functions works operates interacts acts| as (a) |<verb> <noun>|
        Ex: acts as an intermediary (role => 'intermediary')

- roles are intrinsically related to functions, intents, strategies, & mechanisms

- the word with the highest count that is a noun is likely to be a focal object of the article

- add combination pos identification patterns for use in get_pos
    - 'MD + V' => 'could succeed'
    - 'V + RP' => 'give up'
'''

def extract_patterns(objects, object_types, database_path):
    ''' 
        - this function is for meta-analysis, not finding or replacing a pattern in a line
        - after youre done processing a batch of articles, 
            youll have an index containing types of elements ('condition', 'symptom', 'strategy')
            this function is for finding patterns in those index types
            
        - objects must be a dict if populated
        - to do: you should load the database elsewhere & import
    '''
    docs = {}
    if objects:
        if len(objects) > 0:
            for object_type in objects:
                docs[object_type] = objects[object_type]
    object_types = object_types if object_types else []
    elif database_path: #'data' folder
        docs = get_local_database(database_path, object_types)
    if docs:
        patterns = {}
        for object_type in docs:
            for object_index in docs[object_type]:
                for line in object_index.split('\n'):
                    line_patterns = get_pattern_map_in_line(line, all_vars, None)
                    if line_patterns:
                        for k in line_patterns:
                            if k not in patterns:
                                patterns[k] = []
                            patterns[k].extend(line_patterns[k])
        if patterns:
            return patterns
    return False

def is_pattern_in_line(line, pattern):
    ''' line.count(pattern) or False '''
    pos_line = convert_words_to_pos(line)
    if pattern in pos_line:
        return pos_line.count(pattern)
    return False

def replace_pattern_in_line(line, pattern):
    ''' line.replace(pattern, source_words) '''
    found_patterns = get_source_wordsets(line, pattern)
    if found_patterns:
        return ' '.join(found_patterns)
    return False

def get_pattern_map_in_line(line, all_vars, pattern_keys):
    ''' a = {'pattern': 'source_words'} '''
    found_patterns = {}
    pattern_keys if pattern_keys is not None else all_vars['pattern_index'].keys()
    for pattern_key in pattern_keys:
        pattern_list = all_vars['pattern_index'][pattern_key]
        for pattern in pattern_list:
            source_wordsets_for_pattern = get_source_wordsets_for_pattern(line, pattern)
            if source_wordsets_for_pattern:
                if pattern not in found_patterns:
                    found_patterns[pattern] = []
                found_patterns[pattern].extend(source_wordsets_for_pattern)
    if found_patterns:
        return found_patterns
    return False

def get_source_wordsets_for_pattern(line, pattern):
    ''' ['source_words_for_pattern_instance_1', 'source_words_for_pattern_instance_2', ...] '''
    pos_line = convert_words_to_pos(line)
    if pattern in pos_line:
        source_wordsets_for_patterns = get_source_words(line, pos_line.split(pattern))
        if source_wordsets_for_patterns:
            return source_wordsets_for_patterns
    return False

def get_source_words(source_line, exclude_list):
    delimiter = get_delimiter(source_line)
    for word_set in exclude_list.split(' '):
        if word_set in source_line:
            source_line = source_line.replace(word_set, delimiter)
    source_wordsets_for_patterns = source_line.split(delimiter)
    if source_wordsets_for_patterns:
        if len(source_wordsets_for_patterns) > 0:
            return source_wordsets_for_patterns
    return False

def get_source_wordsets(line, pattern): 
    pos_line = convert_words_to_pos(line)
    if pattern in pos_line:
        non_patterns = pos_line.split(pattern)
        source_words_for_patterns = get_source_words(line, non_patterns)
        if source_words_for_patterns:
            subsets = []
            for i, subset in enumerate(source_words_for_patterns):
                subsets.append(subset)
                if i < len(non_patterns):
                    subsets.append(non_patterns[i])
            if len(subsets) > 0:
                return subsets
    return False

def get_pattern_stack(pattern_stack):
    '''
        pattern_stack is the output of get_pattern_stack, 
        which returns a dict with 
            keys pointing to source sentence &
            values pointing to pattern with pos replacement
        out of the pattern_stack, you need a function to derive the abstract patterns:
        - iterate through words 
            - if its an object, replace it with its type 
            - if its a function, replace it with its core function decomposition
            - repeat until all relevant unique patterns are generated
    '''
    return pattern_stack

''' PROCESS PATTERNS '''

def add_sub_patterns(pattern_list, source_length, combination, all_patterns):
    ''' get subsequent patterns since pattern_list[i] was a list '''
    ''' if set is complete according to len(pattern_list), reset trackers & add to all_patterns '''
    combination = [] if not combination else combination
    if len(combination) == source_length or len(combination) == len(pattern_list):
        all_patterns.add(' '.join(combination))
        return combination, all_patterns
    for pattern_piece in pattern_list:
        if ' ' not in pattern_piece:
            combination.append(pattern_piece)
        else:
            ''' this is a set of alts - iterate through it & pick one & combine it with subsequent patterns '''
            combination, all_patterns = add_sub_patterns(pattern_piece.split(' '), source_length, combination, all_patterns)
    return combination, all_patterns

def get_pattern_alts(source_pattern):
    ''' 
    this converts a pattern string: 
        source_pattern = '|option1 option2| VB'
    into a list of pattern combinations, given alt options in the source_pattern 
        all_patterns = ['option1 VB', 'option2 VB']
    - alternatives are indicated by options separated by spaces within pairs of '|':
    - optional string are indicated by: __optionalstring__
    '''
    # source_pattern =  '|NN VB| VB' or 'NN NP'
    delimiter = '|' in '|' in source_pattern else ' '
    pattern_sets = [i for i in source_pattern.split(delimiter)]
    # you could also create a list of lists & iterate with counters
    # pattern_sets should be a list of pos with alts separated by spaces ['NN VB', 'VB'] or ['NN', 'NP']
    combination = []
    all_patterns = set()
    all_patterns_with_alts = set()
    combination, all_patterns = add_sub_patterns(pattern_sets, len(pattern_sets), combination, all_patterns)
    # all_patterns should be a list of combined patterns like ['NN VB', 'VB VB'],
    # which is both combinations possible of the set ['NN VB', 'VB']
    if all_patterns:
        ''' now replace optional strings with an empty string and add that pattern '''
        for pattern in all_patterns:
            if '__' in pattern:
                new_pattern = pattern
                for item in pattern.split('__'):
                    if ' ' not in item:
                        optional_word = ''.join(['__', item, '__'])
                        if optional_word in source_pattern:
                            new_pattern = new_pattern.replace(optional_word, '')
                new_pattern = new_pattern.replace('  ', ' ')
                # add the alternative pattern with optional strings replaced
                all_patterns_with_alts.add(new_pattern) 
            all_patterns_with_alts.add(pattern)
        if len(all_patterns_with_alts) > 0:
            return all_patterns_with_alts
    return False
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

def get_string_patterns(articles):
    ''' this function looks for matches in elements with repeated pos or string patterns like alpha-<compound>-ic acid '''
    string_patterns_found = set()
    return string_patterns_found

def extract_patterns(word, objects, local_database, object_types):
    docs = {}
    object_types = object_types if object_types else 'patterns'
    if type(object_types) == list:
        if len(object_types) > 0:
            object_types = object_types[0]
    if objects:
        if len(objects) > 0:
            docs[object_types] = objects
    elif local_database: #'data' folder
        docs = get_local_database(local_database, object_types)
    if docs:
        patterns = set()
        for object_type in docs:
            for object_data in docs[object_type]:
                for line in object_data.split('\n'):
                    ''' get matches from configured patterns '''
                    line_patterns = get_patterns_in_line(line, all_vars)
                    if len(line_patterns) > 0:
                        patterns = patterns.union(line_patterns)
                    ''' 
                    splitting into words & appending prev_word, word, & next_word 
                    is a backup strategy if no others are found in article 
                    '''
                    words = line.split(' ')
                    for i, w in enumerate(words):
                        if w == word:
                            ''' to do: use get_next_important_word rather than any next word '''
                            prev_word = words[i - 1] if i > 0 else ''
                            next_word = words[i + 1] if i < (len(words) - 1) else ''
                            word_set = ' '.join([prev_word, word, next_word])
                            converted_word_set = convert_words_to_pos(word_set.strip())
                            if converted_word_set:
                                patterns.add(converted_word_set)
        if len(patterns) > 0:
            return patterns
    return False

def get_delimiter(line):
    ''' get a delimiter that isnt in the line '''
    delimiter = '***' if '***' not in line else '###'
    return delimiter

def remove_items_from_list(original_line, exclude_list):
    delimiter = get_delimiter(original_line)
    for word_set in exclude_list.split(' '):
        if word_set in original_line:
            original_line = original_line.replace(word_set, delimiter)
    words_for_patterns = original_line.split(delimiter)
    if words_for_patterns:
        return words_for_patterns
    return False

def find_patterns(line, all_vars):
    line_patterns = {}
    keywords = None
    for pattern in all_vars['patterns']:
        found = find_pattern(line, pattern, keywords)
        if found:
            if len(found) > 0:
                if pattern not in line_patterns:
                    line_patterns[pattern] = set()
                line_patterns[pattern] = line_patterns[pattern].union(found)
    if line_patterns:
        return line_patterns
    return False

def find_pattern(line, pattern, keywords): 
    ''' original = 'cat ate dog after 12pm dog ate rat and then the next day' '''
    ''' pos_line = 'noun verb noun after 12pm noun verb noun' and then the next day'''
    ''' pattern = 'noun verb noun' '''
    pos_line = convert_words_to_pos(line)
    if pattern in pos_line:
        non_patterns = pos_line.split(pattern)
        ''' non_patterns = [' after 12pm ', ' and then the next day'] '''
        words_for_patterns = remove_items_from_list(line, non_patterns)
        ''''words_for_patterns = ['cat ate dog', 'dog ate rat'] '''
        if words_for_patterns:
            new_line = []
            for i, word_set in enumerate(words_for_patterns):
                new_line.append(word_set)
                ''' get the corresponding item in non_patterns '''
                if i < len(non_patterns):
                    new_line.append(non_patterns[i])
            if len(new_line) > 0:
                return new_line
    if keywords:
        keywords_found = [x for x in keywords if x in pos_line]
        if len(keywords_found) > 2:
            return keywords_found
    return False

def get_pattern_stack(pattern_stack):
    '''
        pattern_stack is the output of get_pattern_stack, 
        which returns a dict with 
            keys pointing to original sentence &
            values pointing to pattern with pos replacement
        out of the pattern_stack, you need a function to derive the abstract patterns:
        - iterate through words 
            - if its an object, replace it with its type 
            - if its a function, replace it with its core function decomposition
            - repeat until all relevant unique patterns are generated
    '''
    return pattern_stack

''' FIND PATTERNS '''

''' PROCESS PATTERNS '''

def add_sub_patterns(pattern_list, original_length, combination, all_patterns):
    ''' get subsequent patterns since pattern_list[i] was a list '''
    ''' if set is complete according to len(pattern_list), reset trackers & add to all_patterns '''
    combination = [] if not combination else combination
    if len(combination) == original_length or len(combination) == len(pattern_list):
        all_patterns.add(' '.join(combination))
        return combination, all_patterns
    for pattern_piece in pattern_list:
        if ' ' not in pattern_piece:
            combination.append(pattern_piece)
        else:
            ''' this is a set of alts - iterate through it & pick one & combine it with subsequent patterns '''
            combination, all_patterns = add_sub_patterns(pattern_piece.split(' '), original_length, combination, all_patterns)
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
                new_pattern = new_pattern.replace('  ',' ')
                # add the alternative pattern with optional strings replaced
                all_patterns_with_alts.add(new_pattern) 
            all_patterns_with_alts.add(pattern)
        if len(all_patterns_with_alts) > 0:
            return all_patterns_with_alts
    return False
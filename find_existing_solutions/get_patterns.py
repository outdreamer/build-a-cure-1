def get_pattern_matches_in_line(line, pattern_keys, all_vars):
    ''' a = {'pattern': 'source_words'} '''
    found_patterns = {}
    pattern_keys if pattern_keys is not None else all_vars['pattern_index'].keys()
    for pattern_key in pattern_keys:
        if pattern_key in all_vars['pattern_index']:
            pattern_list = all_vars['pattern_index'][pattern_key]
            for pattern in pattern_list:
                alt_patterns = get_alt_patterns(pattern)
                ''' pattern is included in alt_patterns if there are no alt options in pattern '''
                if alt_patterns:
                    if len(alt_patterns) > 0:
                        for alt_pattern in alt_patterns:
                            source_subsets = get_pattern_source_subsets(line, alt_pattern)
                            if source_subsets:
                                found_patterns[alt_pattern] = set(source_subsets)
    if found_patterns:
        return found_patterns
    return False

def get_pattern_source_words(source_line, exclude_list):
    ''' get source words in same positions as pattern '''
    ''' get_pattern_source_words('a b c', ['b']) == ['a', 'c'] '''
    delimiter = get_delimiter(source_line)
    for word_set in exclude_list.split(' '):
        if word_set in source_line:
            source_line = source_line.replace(word_set, delimiter)
    source_subsets = source_line.split(delimiter)
    if source_subsets:
        if len(source_subsets) > 0:
            return source_subsets
    return False

def get_pattern_source_subsets(line, pattern):
    ''' get only the matching subsets from line with words in the same positions & pos as pattern '''
    ''' ['pattern_instance_1', 'pattern_instance_2''] '''
    pos_line = convert_words_to_pos(line)
    if pattern in pos_line:
        source_subsets = get_pattern_source_words(line, pos_line.split(pattern))
        if source_subsets:
            if len(source_subsets) > 0:
                return source_subsets
    return False

def get_all_source_subsets(line, pattern):
    ''' split a line into subsets so each pattern section is in its own subset '''
    ''' ['pattern_instance_1', 'non-pattern-words', 'pattern_instance_2', 'other non-pattern words'] '''
    pos_line = convert_words_to_pos(line)
    if pattern in pos_line:
        non_patterns = pos_line.split(pattern)
        source_subsets = get_pattern_source_words(line, non_patterns)
        if source_subsets:
            subsets = []
            for i, subset in enumerate(source_subsets):
                subsets.append(subset)
                if i < len(non_patterns):
                    subsets.append(non_patterns[i])
            if len(subsets) > 0:
                return subsets
    return False

def replace_pattern_in_line(line, pattern):
    ''' line.replace(pattern, source_words) '''
    found_patterns = get_all_source_subsets(line, pattern)
    if found_patterns:
        return ' '.join(found_patterns)
    return False

def is_pattern_in_line(line, pattern):
    ''' count of pattern in line or False '''
    pos_line = convert_words_to_pos(line)
    if pattern.lower() in pos_line.lower():
        return pos_line.lower().count(pattern.lower())
    return False

''' PROCESS PATTERNS '''

def add_sub_patterns(pattern_list, source_length, combination, all_patterns):
    ''' get subsequent patterns since pattern_list[i] was a list '''
    ''' if set is complete according to len(pattern_list), reset trackers & add to all_patterns '''
    combination = [] if not combination else combination
    if len(combination) > 0:
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

def get_alt_patterns(source_pattern):
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

def get_type_patterns(source_pattern):
    ''' to do: implement this after get_types '''
    return source_pattern

def replace_pattern(source_pattern, target_pattern, line, all_vars):
    '''
    - to do: add mapping patterns for use in replacement functions
        - 'MD + V' => 'could succeed'
        - 'V + RP' => 'give away'
    '''
    return source_pattern

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

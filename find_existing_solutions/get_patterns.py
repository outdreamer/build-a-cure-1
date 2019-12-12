def get_patterns_between_objects(objects):
    '''
    this function is to determine patterns using each object in the list as input
    to find patterns between list items
    since we're passing in index[keys] to this function,
    we'll be handling lists of objects like strategies
    to find patterns in strategy objects,
    youd abstract the objects in each strategy and check if that abstract version occurs elsewhere

    example:
        with inputs:
            objects = [
                'look before you leap',
                'check yourself before you wreck yourself'
            ]
        this function would identify the pattern these strategies have in common:
            abstract_pattern = "use caution to prevent adverse events"

        this function would return:
            pattern = "apply(context, style, abstract_strategy) => metaphorical_strategy"

        Example of applying the abstract_pattern to produce a strategy:

            apply(context="crossing a gap", style=None, strategy=abstract_pattern) = 'look before you leap'
                - the adverse event possible in the context of "crossing a gap" is "falling in the gap"
                - the method of using caution in the context of "crossing a gap" is "looking"

            apply(context="prepare_for_social_situation", style="slang", strategy=abstract_pattern) = 'check yourself before you wreck yourself'
                - the adverse event possible in the context of "prepare_for_social_situation" is "wrecking yourself"
                - the method of using caution in the context of "prepare_for_social_situation" is "checking yourself"
    '''
    return objects

def index_as_functions(line):
    ''' this is to convert relationships in line into a function object
        example: "x could possibly generate y" outputs the following object:
            function = {
                input="object(x)", 
                attribute="possible", 
                intent="generate", 
                type="causative",
                output="object(y)"
            }

        - functional patterns:
            - are more complicated than pos/string/type patterns, and are returned from get_functions(line)
            - rely heavily on the verb or verb phrases and conditional operators
            - if its a supported type like strategy or insight you dont need to wrap it with object() syntax
            - each argument to function inputs, relation, and outputs should be another function object
            - we use relation as a param to the function to differentiate them 
            - indexing info this way makes storing function pattern_maps & advanced system analysis queries possible

        - syntax: 
            - y.function(x) indicates its a process of some external object acting on x
                "pathway regulation" => regulatory_system.regulating(pathway)
            - a function of x would be indicated similarly:
                "x.function(a)" => pathway.adapt("receptor_A")

        - example:
            original_line = 'Understanding how this pathway is regulated could lead to new strategies to treat both diseases'
                function=(
                    input=(
                        function(input="object(pathway)", attribute="pathway.regulation", output="insight")
                          # ----------------------- Understanding of 'pathway regulation'
                    ),
                    relation=(
                        function(input="relation", attribute="possible", intent="generate", output="function") 
                    ),    # ----------------------- could generate
                    output=(
                        function(
                            input="object([diabetes, cancer], type=medical_condition)", 
                            output="strategy(attribute=[new, multiple], intent=treatment)"
                        ) # ----------------------- strategies to treat both diseases
                    )
                )
            which abstracts to the function pattern:
                function=(
                    input=(function(input="object(x)", attribute="y.function(x)", output="insight")),
                    relation=(function(input="function.name", attribute=function.attribute, intent=function.intent, output=function)),
                    output=(function(input="object(objects), type=objects.type", output="strategy(attribute=strategy.attributes, intent=strategy.intent)"))
                )
    '''
    return line

def find_patterns(source_input, pattern_keys, all_vars):
    '''
    if source_input is a list, get patterns between objects in the list,
    rather than patterns in a string source_input
    '''
    ''' a = {'pattern': 'source_words'} '''
    found_patterns = get_patterns_between_objects(source_input)
    if found_patterns:
        return found_patterns
    found_patterns = {}
    pattern_keys if pattern_keys is not None else all_vars['pattern_index'].keys()
    for pattern_key in pattern_keys:
        combined_key = ''.join(['patterns_', pattern_key])
        found_patterns[combined_key] = {}
        if pattern_key in all_vars['pattern_index']:
            pattern_list = all_vars['pattern_index'][pattern_key]
            for pattern in pattern_list:
                ''' pattern is included in alt_patterns if there are no alt options in pattern '''
                alt_patterns = get_alt_patterns(pattern)
                if alt_patterns:
                    if len(alt_patterns) > 0:
                        for alt_pattern in alt_patterns:
                            source_subsets = get_pattern_source_subsets(line, alt_pattern)
                            if source_subsets:
                                found_patterns[combined_key][alt_pattern] = set(source_subsets)
    if found_patterns:
        return found_patterns
    return False

def apply_pattern_map(line, pattern_map):
    ''' this replaces a pattern with another pattern using variables 
    pattern_map = {
        'nounified_verb of noun' => 'nounified_verb-noun'
    }
    output would be:
        the line with replaced values of the pattern_map, if the pattern keys are found in the line
    when you check for patterns:
        iterate up in size from word => modifier => phrase
        so you dont miss phrases that match a pattern with only variable names:
            'x of y' (will catch 'substrate of a mixture of compound and organism')
        rather than pos:
            'noun of noun' (will only catch 'inhibitor of enzyme')
    '''
    for object_type in ['word', 'modifier', 'phrase']:
        for pattern in pattern_map:
            found_patterns = get_pattern_source_subsets(line, pattern)
            if found_patterns:
                for p in found_patterns:
                    applied = get_new_version(p, pattern, pattern_map[pattern])
                    line.replace(p, applied)
                return line
    return False

def get_new_version(subset, pattern_map):
    ''' subset = "inhibitor of compound"
        pattern_map = {
            'source': "x of y", "NN of NN",
            'target': "y x
        }
        output should be "compound-inhibitor"
    '''
    ''' handle target patterns with more words than source '''
    ''' handle other delimiters than space in case your source pattern has no spaces '''
    delimiter = None
    split, delimiters = split_by_delimiter(subset, all_vars)
    if delimiters:
        if len(delimiters) > 0:
            if ' ' not in delimiters:
                delimiter = delimiters[0]
    if delimiter:
        ''' create a position map for source & target '''
        positions = {'source': {}, 'target': {}}
        designated_variables = [x for x in all_vars['alphabet']]
        source_words = pattern_map['source'].split(delimiter)
        ''' assuming 'I' and 'a' have been removed at this point'''
        for pattern_type in ['source', 'target']:
            for position, w in enumerate(pattern_map[pattern_type].split(delimiter)):
                nltk_pos = get_nltk_pos(word)
                pos = get_pos(word)
                synsets = get_synsets(word, pos, all_vars)
                if w in designated_variables:
                    positions[pattern_type][position] = w
                elif w in all_vars['pos_tags']['all']:
                    positions[pattern_type][position] = w
                elif not pos or not nltk_pos or len(synsets) == 0:
                    '''
                    check output of pos identification for single letters
                    allow variables of a type other than designated
                     '''
                    positions[pattern_type][position] = w
                else:
                    '''
                    not a variable name so add it in this position
                    if this word is not in target_pattern, 
                    include an empty string in target_pattern 
                    '''
                    source_word = source_words[position]
                    if pattern_type == 'target' and source_word not in pattern_map['target']:
                        positions[pattern_type][position] = ''
                    else:
                        positions[pattern_type][position] = w
        '''
        positions = {
            'source': {0: 'x', 1: 'of', 2: 'y'},
            'target': {0: 'y', 1: '', 2: 'x'}
        }
        '''
        position_map = {}
        for source_position, source_word in positions['source'].items():
            if source_word in positions['target'].values():
                for target_position, target_word in positions['target'].items():
                    if source_word == target_word:
                        position_map[source_position] = target_position
            else:
                position_map[source_position] = ''
        '''
        final_map = {
            0: 2,
            1: '',
            2: 0
        }
        '''
        ''' now apply this mapping to the subset '''
        saved_words = subset.split(delimiter)
        new_words = []
        for i, word in enumerate(subset.split(delimiter)):
            if i in position_map:
                target_position = position_map[i]
                new_words.append(saved_words[target_position])
        if len(new_words) > 0:
            new_subset = delimiter.join(new_words)
            return new_subset
    return False

def is_pattern_in_line(line, pattern):
    ''' count of pattern in line or False '''
    pos_line = convert_words_to_pos(line)
    if pattern.lower() in pos_line.lower():
        return pos_line.lower().count(pattern.lower())
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

def get_pattern_source_words(source_line, exclude_list):
    ''' get source words in same positions as pattern '''
    ''' ('a b c', ['b']) == ['a', 'c'] '''
    delimiter = get_delimiter(source_line)
    for word_set in exclude_list.split(' '):
        if word_set in source_line:
            source_line = source_line.replace(word_set, delimiter)
    source_subsets = source_line.split(delimiter)
    if source_subsets:
        if len(source_subsets) > 0:
            return source_subsets
    return False

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

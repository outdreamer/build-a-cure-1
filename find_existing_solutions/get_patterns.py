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
    found_patterns = {}
    if type(source_input) == list:
        found_patterns = get_patterns_between_objects(source_input)
    else:
        pattern_keys if pattern_keys is not None else all_vars['pattern_index'].keys()
        for pattern_key in pattern_keys:
            combined_key = ''.join(['patterns_', pattern_key])
            found_patterns[combined_key] = {}
            if pattern_key in all_vars['pattern_index']:
                for pattern in all_vars['pattern_index'][pattern_key]:
                    source_subsets = get_pattern_source_subsets(source_input, pattern, 'pattern')
                    if source_subsets:
                        found_patterns[combined_key][pattern] = set(source_subsets)
    if found_patterns:
        return found_patterns
    return False

def apply_pattern_map(line, pattern_map):
    ''' 
    this replaces a pattern with its associated pattern found in the line using variables 

    apply_pattern_map(line='dog of cat', pattern_map = {'noun1 of noun2' => 'noun2 noun1'})
        would output: 'cat dog'

    output: the line with replaced values of the pattern_map, if the pattern keys are found in the line
    '''
    # for object_type in ['word', 'modifier', 'phrase']:
    for source_pattern, target_pattern in pattern_map.items():
        found_subsets = get_pattern_source_subsets(line, source_pattern, 'pattern')
        if found_subsets:
            for subset in found_subsets:
                pattern_map = {'source': source_pattern, 'target': target_pattern}
                applied = get_new_version(subset, sub_pattern_map, all_vars)
                line.replace(p, applied)
            return line
    return False

def get_new_version(subset, sub_pattern_map, all_vars):
    ''' subset = "inhibitor of compound"
        sub_pattern_map = {
            'source': "x of y",
            'target': "y x"
        }
        output = "compound-inhibitor"

        to do:
        - handle target patterns with more words than source
        - handle other delimiters than space in case your source pattern has no spaces

        this should be identified as positive matches of the modifier pattern 'JJ NN':
        sub_pattern_map = {'source': "JJ1 NN1 of JJ2 NN2", 'target': "JJ2 NN2 JJ1 NN1"}
        subset = "catalyzing inhibitor of alkalizing enzyme"
    '''
    
    delimiter = find_delimiter(subset, all_vars)
    if delimiter:
        ''' create a position map for source & target '''
        positions = {'source': {}, 'target': {}}
        source_words = subset.split(delimiter)
        for pattern_type in ['source', 'target']:
            for position, w in enumerate(sub_pattern_map[pattern_type].split(delimiter)):
                source_word = source_words[position] if position < len(source_words) else None
                if pattern_type == 'target' and source_word is not None and source_word not in sub_pattern_map['target']:
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
        ''' position_map = {0: 2, 1: '', 2: 0} '''
        ''' now apply this mapping to the subset '''
        saved_words = subset.split(delimiter)
        new_words = []
        for i, word in enumerate(subset.split(delimiter)):
            if i in position_map:
                target_position = position_map[i]
                new_words.append(saved_words[target_position])
        if len(new_words) > 0:
            return delimiter.join(new_words)
    return False

def get_pattern_source_subsets(line, pattern, get_type):
    ''' get only the matching subsets from line with words in the same positions & pos as pattern '''
    ''' ['pattern_instance_1', 'pattern_instance_2''] '''
    '''
        support numerical variables by checking non-numeric pattern for match with pos_line 
        to do: this prevents users from configuring patterns with numbers like 14alpha-deoxy-enzyme
    '''
    pattern_without_numbers = []
    pos_line = convert_words_to_pos(line)
    delimiter = find_delimiter(subset, all_vars)
    if delimiter:
        for word in pattern.split(delimiter):
            nonnumeric_word = ''.join([w for w in word if w not in '0123456789']) 
            if nonnumeric_word in all_vars['pos_tags']['ALL']:
                pattern_without_numbers.append(nonnumeric_word)
            else:
                pattern_without_numbers.append(word)
        nonnumeric_pattern = delimiter.join(pattern_without_numbers) if len(pattern_without_numbers) > 0 else pattern
        if nonnumeric_pattern in pos_line:
            subsets = []
            if get_type == 'pattern':
                subsets = get_pattern_source_words(line, pos_line.split(nonnumeric_pattern))
            else:
                ''' split a line into subsets so each pattern section is in its own subset '''
                ''' ['pattern_instance_1', 'non-pattern-words', 'pattern_instance_2', 'other non-pattern words'] '''
                non_patterns = pos_line.split(pattern)
                sources = get_pattern_source_words(line, non_patterns)
                if sources:
                    for i, subset in enumerate(sources):
                        subsets.append(subset)
                        if i < len(non_patterns):
                            subsets.append(non_patterns[i])
            if subsets:
                if len(subsets) > 0:
                    return subsets 
    return False

def get_pattern_source_words(source_line, exclude_list):
    ''' get source words in same positions as pattern '''
    ''' ('a b c', ['b']) == ['a', 'c'] '''
    delimiter = get_delimiter(source_line)
    for word_set in exclude_list:
        if word_set in source_line:
            source_line = source_line.replace(word_set, delimiter)
    source_subsets = source_line.split(delimiter)
    if source_subsets:
        if len(source_subsets) > 0:
            return source_subsets
    return False

def get_nested_patterns(pattern):
    '''
    support for nested alts in patterns like:
     '__|a an|__' and '|VB NN |VB ADV|| VB'

    basically you want to find any nested patterns 
    and replace them with a variable, 
    and return the new pattern with variables as well as the variable map:
        pattern = '|VB NN x| VB' and variables['x'] = '|VB ADV|'
    '''
    print('get nested alts for pattern', pattern)
    variables = {}
    nested_patterns = []
    split = ['', 'VB NN ', 'VB ADV', '', ' VB']
    delimiter_index = 0
    new_variable_value = []
    for char in pattern.split(''):
        if char == delimiter:
            delimiter_index += 1
            if delimiter_index > 0 and (delimiter_index / 2) == int(delimiter_index / 2):
                ''' this is an even delimiter index, so end this variable '''
                new_key = get_new_key(variables.keys(), all_vars)
                variables[new_key] = ''.join(new_variable_value)
                pattern.replace(new_variable_value, new_key)
                new_variable_value = []
        else:
            new_variable_value.append(char)
    if pattern:
        print('new pattern', pattern, variables)
        ''' pattern is included in alt_patterns if there are no alt options in pattern '''
        alt_patterns = get_alt_patterns(pattern, variables)
        if alt_patterns:
            if len(alt_patterns) > 0:
                return alt_patterns
    return False, False

def get_alt_patterns(source_pattern, nested_variables):
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
    pattern_length = len(pattern_sets)
    if nested_variables:
        '''
        pattern = '|VB NN x| VB' and variables['x'] = 'VB ADV'
        pattern = '|VB NN VB&ADV|' means 'VB or NN or VB & ADV'

        this function needs to support nested patterns, so when iterating, 
        check for any var chars and if found, 
        iterate through variable values & replace with each value
        '''          
        pattern_length += sum([len(v.split(' ')) for k, v in nested_variables.items()])
    combination, all_patterns = add_sub_patterns(pattern_sets, pattern_length, combination, all_patterns, nested_variables)
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

def add_sub_patterns(pattern_list, source_length, combination, all_patterns, nested_variables):
    ''' get subsequent patterns since pattern_list[i] was a list
        if set is complete according to len(pattern_list), reset trackers & add to all_patterns
        you can replace these with a variable just like you replaced nested patterns with variables
    '''
    combination = [] if not combination else combination
    if len(combination) > 0:
        if len(combination) == source_length or len(combination) == len(pattern_list):
            all_patterns.add(' '.join(combination))
            return combination, all_patterns
    for pattern_piece in pattern_list:
        if pattern_piece in nested_variables:
            pattern_piece = nested_variables[pattern_piece]
        if ' ' not in pattern_piece:
            combination.append(pattern_piece)
        else:
            ''' this is a set of alts - iterate through it & pick one & combine it with subsequent patterns '''
            combination, all_patterns = add_sub_patterns(pattern_piece.split(' '), source_length, combination, all_patterns)
    return combination, all_patterns

def get_type_patterns(source_pattern):
    ''' to do: implement this after get_types '''
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

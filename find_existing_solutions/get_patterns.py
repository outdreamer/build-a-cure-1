import itertools
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
import random
from get_pos import get_nltk_pos

def get_patterns_between_objects(objects, object_type, all_vars):
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

def get_partial_pos(pattern, all_vars):
    pattern = convert_words_to_pos(pattern, None, all_vars)
    pattern_words = pattern.split(' ')
    new_pattern_words = []
    for w in pattern_words:
        nonnumeric_var = get_nonnumeric(w, all_vars)
        if nonnumeric_var in all_vars['pos_tags']['ALL']:
            for pos_key in ['V', 'N', 'D', 'P', 'C', 'ADV', 'ADJ']:
                if nonnumeric_var in all_vars['pos_tags'][pos_key] or nonnumeric_var == pos_key:
                    new_pattern_words.append(pos_key)
        else:
            new_pattern_words.append(w)
    if len(new_pattern_words) > 0:
        return ' '.join(new_pattern_words)
    return pattern

def apply_pattern_map(line, pattern_map, all_vars):
    ''' 
    - this replaces a pattern with its associated pattern found in the line using variables 
        apply_pattern_map(line='dog of cat', pattern_map = {'noun1 of noun2' => 'noun2 noun1'}) = 'cat dog'
    to do:
        - add partial patterns to get_nested_patterns
        - make sure youre generating all patterns for both source & target pattern sets
        - make a sub function to apply one pattern at a time & retain a copy of the original line
        - for object_type in ['word', 'modifier', 'phrase'] - these should already be replaced with option sets of each type pattern 
        - modifier1 should be replaced with each modifier pattern + 1 and used to generate a new pattern containing each modifier pattern
        - when the source pattern is 'VBD VBN' and the target is 'VBZ' you need to isolate the 'VBN' which is the more meaningful verb
            currently its getting overridden by the consecutive verb which also matches the 'V' type but need a more robust way
    '''

    original_line = line
    pattern_map = add_repeated_indexes_to_pattern_map(pattern_map, all_vars)
    reverse_keys = reversed(sorted(pattern_map.keys()))
    for source_pattern in reverse_keys:
        pos_line = convert_words_to_pos(line, source_pattern, all_vars)
        target_pattern = pattern_map[source_pattern]
        new_line, variables, generated_patterns = apply_pattern(source_pattern, target_pattern, line, pos_line, all_vars)
        if new_line:
            print('applied pattern to line', new_line)
            print('sp', source_pattern, 'tp', target_pattern, 'vars', variables)
            ''' to do: in order to support iterated replacement, you need to make sure your patterns are ordered in the right way '''
            return new_line #line = new_line
    return line

def generate_patterns_for_pattern(pattern, line, pos_line, all_vars):
    patterns = []
    variables = {}
    nested_patterns, variables = get_nested_patterns(line, pattern, 'pattern', None, all_vars)
    if nested_patterns:
        variables = variables if variables else {}
        for np in nested_patterns:
            alt_patterns = get_alt_patterns(np, variables, all_vars)
            alt_patterns = alt_patterns if alt_patterns else [np]
            patterns.extend(alt_patterns)
    else:
        patterns.extend(nested_patterns)
    if len(patterns) > 0:
        return patterns, variables
    return False, False

def generate_patterns_for_pattern_map(source_pattern, target_pattern, line, pos_line, all_vars):
    variables = {'source': {}, 'target': {}}
    generated_patterns = {'source': [], 'target': []}
    source_patterns, source_variables = generate_patterns_for_pattern(source_pattern, line, pos_line, all_vars)
    if source_patterns:
        generated_patterns['source'].extend(source_patterns)
        variables['source'] = source_variables if source_variables else {}
        for sp in source_patterns:
            ''' only generate target patterns for sp if sp found in line '''
            found_sp_subsets = get_pattern_source_subsets(line, pos_line, sp, 'pattern', all_vars)
            print('found source pattern in subset', found_sp_subsets, sp)
            if found_sp_subsets:
                target_patterns, target_variables = generate_patterns_for_pattern(target_pattern, line, pos_line, all_vars)
                if target_patterns:
                    generated_patterns['target'].extend(target_patterns)
                    variables['target'] = target_variables if target_variables else {}
        return generated_patterns, variables
    return False, False

def apply_pattern(source_pattern, target_pattern, line, pos_line, all_vars):
    variables = {}
    all_patterns = {'source': [], 'target': []}
    generated_patterns, generated_variables = generate_patterns_for_pattern_map(source_pattern, target_pattern, line, pos_line, all_vars)
    print('generated_patterns', 'source', source_pattern, 'target', target_pattern)
    print(generated_patterns)
    if generated_patterns:
        all_patterns['source'] = generated_patterns['source'] if 'source' in generated_patterns else []
        all_patterns['target'] = generated_patterns['target'] if 'target' in generated_patterns else []
        variables = generated_variables if generated_variables else {'source': {}, 'target': {}}
        for sp in all_patterns['source']:
            for tp in all_patterns['target']:
                applied = reposition(line, sp, tp, all_vars)
                if applied:
                    line = applied
        return line, variables, all_patterns
    return False, False, False

def find_patterns(line, pattern_key, all_vars):
    '''
    if line is a sequence, get patterns between objects in the list,
    rather than patterns in a line
    '''
    found_patterns = {}
    if type(line) == list or type(line) == set:
        found_patterns = get_patterns_between_objects(line)
    else:
        if pattern_key in all_vars['pattern_index']:
            combined_key = ''.join([pattern_key, '_patterns'])
            for pattern in all_vars['pattern_index'][pattern_key]:
                ''' only want to generate source patterns here, send a flag to not generate target patterns '''
                generated_patterns, generated_variables = generate_patterns_for_pattern(pattern, line, pos_line, all_vars)
                if generated_patterns:
                    for gsp in generated_patterns['source']:
                        pos_line = convert_words_to_pos(line, gsp, all_vars)
                        found_subsets = get_pattern_source_subsets(line, pos_line, gsp, 'pattern', all_vars)
                        if found_subsets:
                            if combined_key not in found_patterns:
                                found_patterns[combined_key] = {}
                            found_patterns[combined_key][gsp] = found_subsets
    if found_patterns:
        return found_patterns
    return False

def add_repeated_indexes_to_pattern_map(pattern_map, all_vars):
    ''' 
        append position integers to repeated words in source & target patterns 
        if the same count is in the target pattern
        to do:
            - implement count comparison if count of indexed word differs in source/target 
    '''
    new_pattern_map = {}
    for source_pattern, target_pattern in pattern_map.items():
        indexed_source_pattern = add_indexes_to_repeated_words(source_pattern, target_pattern, all_vars)
        indexed_target_pattern = add_indexes_to_repeated_words(target_pattern, source_pattern, all_vars)
        new_pattern_map[indexed_source_pattern] = indexed_target_pattern
    pattern_map = new_pattern_map if new_pattern_map else pattern_map
    return pattern_map

def add_indexes_to_repeated_words(line, comparison, all_vars):
    '''
    line the NN VBD VBN IN the NN IN a RB JJ NN IN CC NN VB CC VBG NN
    comparison the0 N1 VBD VBN IN the1 N2
    '''
    comparison_words = generate_all_var_type_variants(line, comparison, all_vars)
    ''' comparison_words should now be: ['the', 'N', 'V', 'V', 'IN', 'the', 'N2'] '''
    new_words = []
    words = line.split(' ')
    for i, w in enumerate(words):
        ''' w = V, V1, VB, VB1, the, the1 '''
        nonnumeric_w = get_nonnumeric(w, all_vars)
        if w == nonnumeric_w:
            is_supported = is_supported_tag(nonnumeric_w, all_vars)
            if is_supported:
                ''' V, VB '''
                new_words.append(''.join([nonnumeric_w, str(i)]))
            else:
                ''' the '''
                new_words.append(''.join([w, str(i)]))
        elif w != nonnumeric_w:
            ''' V1, the1 '''
            new_words.append(w)
    if len(new_words) > 0:
        return ' '.join(new_words)
    return line

def generate_all_var_type_variants(pattern, comparison, all_vars):
    '''
        - this function is necessary for pattern maps where the source pos type & target pos type 
            are a set:subset relationship (V: VBD, V1: VBD2) rather than equivalent (VBD: VBD, VBD1: VBD2)
            or patterns that have specific source words (the) vs. their target pos type (DT, DT1)

        pattern = 'the0 N1 VBD the1' should produce a list: [
            'the0 N1 VBD the1', # original pattern
            'the N VBD the', # numbers removed
            'the0 N1 V the1', # specific pos_tags converted to general pos_types

            'DT0 N1 VBD DT1', # original pattern with words converted to specific pos_type
            'DT N VBD DT', # numbers removed
            'DT0 N1 V DT1', # specific pos_tags converted to general pos_types & words converted to specific pos_type

            'D0 N1 VBD D1', # original pattern with words converted to general pos_type
            'D N VBD D', # numbers removed
            'D0 N1 V D1', # specific pos_tags converted to general pos_types & words converted to general pos_type
        ]
    '''
    pattern_list = []
    #comparison_words = [get_partial_pos(get_nonnumeric(c, all_vars), all_vars) for c in comparison.split(' ')]
    return pattern_list
    
def reposition(subset, source_pattern, target_pattern, all_vars):
    ''' subset = "inhibitor of compound", source_pattern = "VBZ of NN", target_pattern = "NN VBG"
        output = "compound-inhibitor"
        to do:
        - handle target patterns with more words than source
        - handle other delimiters than space in case your source pattern has no spaces
        - syntax delimiters ('|', '&') should be handled in prior processing in get_alt_patterns
    '''
    print('reposition', subset, source_pattern, target_pattern)
    delimiter = find_delimiter(subset, all_vars)
    if delimiter:
        ''' create a position map for source & target '''
        new_words = {}
        position_map = {}
        positions = {'source': {}, 'target': {}}
        source_words = source_pattern.split(delimiter)
        target_words = target_pattern.split(delimiter)
        for position, w in enumerate(source_words):
            positions['source'][position] = w
            positions['target'][position] = target_words[position] if position < len(target_words) else ''
        ''' positions = { 'source': {0: 'x', 1: 'of', 2: 'y'}, 'target': {0: 'y', 1: '', 2: 'x'} } '''
        for source_position, source_word in positions['source'].items():
            for target_position, target_word in positions['target'].items():
                partial_source_pos = get_partial_pos(source_word, all_vars)
                partial_target_pos = get_partial_pos(target_word, all_vars)
                if (source_word == target_word) or (partial_source_pos == partial_target_pos):
                    ''' to do: exact word match or (supported_tag) '''
                    position_map[source_position] = target_position
                else:
                    if source_word in all_vars['pos_tags']['ALL_V'] and target_word in all_vars['pos_tags']['ALL_V']:
                        position_map[source_position] = target_position
        ''' apply position_map to words in subset: position_map = {0: 2, 1: '', 2: 0} '''
        for source_position, source_word in enumerate(subset.split(delimiter)):
            for sp, tp in position_map.items():
                if sp == source_position:
                    source_var = positions['source'][sp]
                    target_var = positions['target'][tp]
                    nonnumeric_source_var = get_nonnumeric(source_var, all_vars)
                    nonnumeric_target_var = get_nonnumeric(target_var, all_vars)
                    source_is_var = is_supported_tag(nonnumeric_source_var, all_vars)
                    target_is_var = is_supported_tag(nonnumeric_target_var, all_vars)
                    if source_is_var and target_is_var:
                        ''' variable: conjugate if different, add if equal '''
                        if source_var != target_var:
                            conjugated_word = conjugate(source_word, source_var, target_var, all_vars)
                            if conjugated_word:
                                new_words[tp] = conjugated_word
                        else:
                            new_words[tp] = source_word
                    else:
                        ''' not a variable: include index matches ('the': 'the0') but not positional/non-content matches ('x': 'the') '''
                        if source_var == source_word or nonnumeric_source_var == source_word:
                            new_words[tp] = source_word
        if new_words:
            new_items = [new_words[k] for k in sorted(new_words.keys()) if k in new_words]
            if len(new_items) > 0:
                return delimiter.join(new_items)
    return False

def get_pattern_source_subsets(line, pos_line, pattern, get_type, all_vars):
    ''' get only the matching subsets from line with words in the same positions & pos as pattern
        ['pattern_instance_1', 'pattern_instance_2']
        support numerical variables by checking non-numeric pattern for match with pos_line 
        to do: this prevents users from configuring patterns with numbers like 14alpha-deoxy-enzyme
    '''
    print('get pattern subsets for line', line)
    print('pos line', pos_line)
    print('pattern', pattern)
    subsets = []
    delimiter = find_delimiter(line, all_vars)
    pos_pattern = convert_words_to_pos(pattern, None, all_vars)
    print('pos pattern', pos_pattern)
    if delimiter:
        pattern_without_numbers = []
        for word in pos_pattern.split(delimiter):
            nonnumeric_word = get_nonnumeric(word, all_vars)
            is_supported = is_supported_tag(nonnumeric_word, all_vars)
            if is_supported:
                pattern_without_numbers.append(nonnumeric_word)
            else:
                pattern_without_numbers.append(word)
        nonnumeric_pattern = delimiter.join(pattern_without_numbers) if len(pattern_without_numbers) > 0 else pos_pattern
        if nonnumeric_pattern == pos_line:
            return [pattern]
        if nonnumeric_pattern in pos_line:
            if get_type == 'pattern':
                subsets = get_pattern_source_words(line, pos_line.split(nonnumeric_pattern))
            else:
                ''' split a line into subsets so each pattern section is in its own subset '''
                ''' ['pattern_instance_1', 'non-pattern-words', 'pattern_instance_2', 'other non-pattern words'] '''
                non_patterns = pos_line.split(pos_pattern)
                sources = get_pattern_source_words(line, non_patterns)
                if sources:
                    for i, subset in enumerate(sources):
                        ''' to do: convert back to original line subset '''
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

def get_delimiter(line):
    ''' get a delimiter that isnt in the line '''
    delimiter = '***' if '***' not in line else '###'
    return delimiter

def get_original_pattern_length(pattern, delimiter):
    '''
    for a pattern like  '|VB NN x| VB', should return 2
    '''
    delimiter_count = pattern.count(delimiter)
    delimiter_pair_count = delimiter_count / 2
    delimiter_index = 0
    reduced_pattern = []
    for i, char in enumerate(pattern):    
        if char == delimiter:
            delimiter_index += 1
        elif delimiter_index == 0 or (delimiter_index/2 == int(delimiter_index/2)):
            reduced_pattern.append(char)
    reduced_pattern_string = ''.join(reduced_pattern)
    reduced_pattern_string = reduced_pattern_string.replace('  ',' ')
    space_count = reduced_pattern_string.count(' ')
    final_count = delimiter_count + space_count
    if final_count > 0:
        return final_count
    return False

def get_nested_patterns(line, pattern, pattern_type, source_vars, all_vars):
    '''
    support for nested alts in patterns like:
     '__|a an|__' and '|VB NN |VB ADV|| VB'
    pattern = '|VB NN x| VB' and variables['x'] = '|VB ADV|'
    returns nested_patterns = ['VB VB', 'NN VB', 'x VB']
    '''
    '''to do: 
        - add operator support for char other than '|'
        - A&B or VB&VB should be logged as a variable
    '''
    new_patterns = [] 
    new_pattern = []
    variables = {}
    line_delimiter = get_delimiter(line)
    delimiters = ['|']
    space_count = pattern.count(' ') - 2
    for d in delimiters:
        original_pattern_length = get_original_pattern_length(pattern, d)
        for i, subset in enumerate(pattern.split(d)):
            words = subset.strip().split(' ')
            ''' delimiter section is beginning or ending '''
            if len(new_pattern) == (original_pattern_length - space_count):
                new_pattern.extend(words)
                new_patterns.append(' '.join(new_pattern))
                new_pattern = []
            if i > 0 and (i / 2) != int(i / 2):
                ''' make sure only sub-patterns with pos_tags are logged as a variable '''
                is_tag_section = False
                for var in words:
                    nonnumeric_var = get_nonnumeric(var, all_vars)
                    is_supported = is_supported_tag(nonnumeric_var, all_vars)
                    if is_supported:
                        is_tag_section = True
                if is_tag_section:
                    var_value = ' '.join(words)
                    if source_vars:
                        if var_value in source_vars.values():
                            for k, v in source_vars.items():
                                if v == var_value:
                                    variables[k] = v
                                    new_pattern.append(k) # *** var
                        else:
                            new_key = get_new_key(variables.keys(), line, all_vars)
                            variables[new_key] = var_value # *** '-_-'.join(words)
                            new_pattern.append(new_key) # *** var
                    else:
                        new_key = get_new_key(variables.keys(), line, all_vars)
                        variables[new_key] = var_value # *** '-_-'.join(words)
                        new_pattern.append(new_key) # *** var
            else:
                new_pattern.extend(words)
    if len(new_patterns) > 0:
        return new_patterns, variables
    return [pattern], variables

def get_alt_patterns(pattern, nested_variables, all_vars):
    ''' 
    this functions returns ['VB NN D1 D2', 'VB JJ D1 D2'] 
    from pattern = 'VB x D1 D2' and nested_variables['x'] = 'NN JJ'
    - alternatives are indicated by options separated by spaces within pairs of '|'
    - optional string are indicated by: __optionalstring__
    - you could also replace 'VB' with 'V' and do a match on those
    '''
    pattern = pattern.strip()
    all_patterns = []
    delimiter = find_delimiter(pattern, all_vars)
    if delimiter:
        # you could also create a list of lists & iterate with counters
        # pattern_sets should be a list of pos with alts separated by spaces ['NN VB', 'VB'] or ['NN', 'NP']
        '''
        pattern = '|VB NN x| VB' and variables['x'] = 'VB ADV'
        pattern = '|VB NN VB&ADV|' means 'VB or NN or VB & ADV'
        this function needs to support nested patterns, so when iterating, 
        check for any var chars and if found, iterate through variable values & replace with each value
        '''
        new_all_patterns = add_sub_patterns(pattern.split(delimiter), nested_variables)
        if new_all_patterns:
            if len(new_all_patterns) > 0:
                for nap in new_all_patterns:
                    all_patterns.append(nap)
        if len(all_patterns) > 0:
            return all_patterns
    # all_patterns should be a list of combined patterns like ['NN VB', 'VB VB'],
    # which is both combinations possible of the set ['NN VB', 'VB']
    ''' move to add_sub_patterns so vars are supported as well
    if all_patterns:
        #now replace optional strings with an empty string and add that pattern
        for pattern in all_patterns:
            all_patterns_with_alts = []
            if '__' in pattern:
                new_pattern = pattern
                for item in pattern.split('__'):
                    if ' ' not in item:
                        optional_word = ''.join(['__', item, '__'])
                        if optional_word in pattern:
                            new_pattern = new_pattern.replace(optional_word, '')
                new_pattern = new_pattern.replace('  ', ' ')
                # add the alternative pattern with optional strings replaced
                all_patterns_with_alts.append(new_pattern) 
            all_patterns_with_alts.append(pattern)
        if len(all_patterns_with_alts) > 0:
            return all_patterns_with_alts
    '''
    return False

def add_sub_patterns(pattern_list, nested_variables):
    ''' get subsequent patterns since pattern_list[i] was a list
        if set is complete according to len(pattern_list), reset trackers & add to all_patterns
        you can replace these with a variable just like you replaced nested patterns with variables
    '''
    ''' you could generate a dict of lists with initial vars or indexes as keys 
        or create sets of variable replacement values and then iterate through pattern_list, 
        replacing vars with those in order
    '''
    all_sub_patterns = []
    pattern_string = ' '.join(pattern_list)
    new_pattern_words = []
    var_sets = []
    var_set = []
    variable_lists = {}
    '''
    nested_variables = {
        'x': 'NN ADV RR Q',
        'y': 'JJ ADJ B' 
    }
    '''
    #positions of x & y = [0, 2]
    #generate every non-repeating combination of them: [0, 2] and [2, 0]
    # pattern_list = ['x', 'of', 'y']
    value_sets = []
    final_sets = []
    all_list_strings = []
    ordered_var_lists = []
    sorted_keys = sorted(nested_variables.keys())
    for key in sorted_keys:
        val_list = nested_variables[key].split(' ')
        value_sets.extend(val_list)
        ordered_var_lists.append(val_list)
    list_length = len(nested_variables.keys())
    combinations = itertools.combinations(value_sets, list_length)
    for c in combinations:
        for i, key in enumerate(sorted_keys):
            new_list = []
            for j, item in enumerate(c):
                if item in ordered_var_lists[j]:
                    new_list.append(item)
            if len(new_list) == list_length:
                new_list_string = ' '.join(new_list)
                if new_list_string not in all_list_strings:
                    final_sets.append(new_list)
                    all_list_strings.append(new_list_string)
    new_lists = []
    for varset in final_sets:
        new_list = []
        for i, piece in enumerate(pattern_list):
            if piece in nested_variables:
                var_index = sorted_keys.index(piece)
                var_value = varset[var_index]
                new_list.append(var_value)
            else:
                new_list.append(piece)
        if len(new_list) > 0:
            new_list_string = ' '.join(new_list)
            new_lists.append(new_list_string)
    if len(new_lists) > 0:
        return new_lists
    return False

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

def convert_words_to_pos(line, pattern, all_vars):
    ''' 
    when running function to get pos_line, 
    check each word if its an indexed word appearing in nonnumeric source_pattern words
    if so, leave it as-is

    pos line the NN VBD VBN IN the NN IN a RB JJ NN IN CC NN VB CC VBG NN
    pattern the0 N1 VBD VBN IN the1 N2
    pos pattern the0 N1 VBD VBN IN the1 N2

    to do:
        - add support for mapping a source var like V1 to a target var like VB1
        - words like 'bear', 'worm', 'rat' will be logged as a verb even when preceded by determiner
        - add pattern_map word_pos entries to convert words to the correct pos: 
            'DT V1 V2 V3' => 'DT N V1 V2' if V1 can be a noun
    ''' 
    new_line = []
    delimiters = ['|', '__', '&']
    line = add_indexes_to_repeated_words(line, pattern, all_vars)   
    nonnumeric_source_words = []    
    if pattern:
        nonnumeric_source_words = [get_nonnumeric(sw, all_vars) for sw in pattern.split(' ')]
    for word in line.split(' '):
        for d in delimiters:
            word = word.replace(d, '')
        if word in nonnumeric_source_words:
            new_line.append(word)
        else:
            nonnumeric_w = get_nonnumeric(word, all_vars)
            is_supported = is_supported_tag(nonnumeric_w, all_vars)
            if is_supported:
                ''' add tags (N, VB, NN, VBZ, etc) unchanged if found '''
                new_line.append(word)
            else:
                if nonnumeric_w != word:
                    ''' this is an indexed word like 'the1', add as-is '''
                    new_line.append(word)
                else:
                    pos = get_nltk_pos(word, all_vars)
                    is_supported = is_supported_tag(pos, all_vars)
                    if is_supported:
                        new_line.append(pos)
                    else:
                        new_line.append(word)
    line = ' '.join(new_line)
    return line

def is_supported_tag(var, all_vars):
    if var in all_vars['pos_tags']['ALL'] or var in all_vars['pos_tags']:
        return True
    return False

def get_nonnumeric(var, all_vars):
    nonnumeric_var = ''.join([x for x in var if x.lower() in all_vars['alphabet']])
    if len(nonnumeric_var) > 0:
        return nonnumeric_var
    return var

def find_delimiter(line, all_vars):
    delimiters = [c for c in line if c.lower() not in all_vars['alphabet']] 
    if len(delimiters) > 0:
        max_delimiter = max(delimiters)
        if max_delimiter:
            return max_delimiter
    delimiter = ' ' if ' ' in line else ''
    return delimiter

def get_new_key(key_dict, source_line, all_vars):
    new_key = None
    upper_limit = len(all_vars['alphabet']) - 1
    random_index = random.randint(0, upper_limit)
    random_letter = all_vars['alphabet'][random_index]
    if key_dict:
        for k in key_dict:
            new_key = ''.join([k, random_letter])
    else:
        new_key = random_letter
    if new_key:
        if new_key in key_dict or new_key in source_line.split(' '):
            return get_new_key(key_dict, source_line, all_vars)
        else:
            return new_key
    return False 

def conjugate(word, source_pos, target_pos, all_vars):
    ''' convert word from source_pos to target_pos '''
    target_endings = {
        'VB': '',
        'VBP': '',
        'VBZ': 's',
        'VBG': 'ing',
        'VBD': 'ed',
        'VBN': 'ed'
    }
    case_maps = {
        'be': {'VB': 'is', 'VBD': 'was', 'VBG': 'is', 'VBN': 'been', 'VBP': 'is', 'VBZ': 'is'},
        'do': {'VB': 'do', 'VBD': 'did', 'VBG': 'doing', 'VBN': 'done', 'VBP': 'do', 'VBZ': 'does'},
        'have': {'VB': 'have', 'VBD': 'had', 'VBG': 'having', 'VBN': 'had', 'VBP': 'have', 'VBZ': 'has'}
    }
    nonnumeric_s_pos = get_nonnumeric(source_pos)
    nonnumeric_t_pos = get_nonnumeric(target_pos)
    if nonnumeric_s_pos != nonnumeric_t_pos:
        is_source_supported = is_supported_tag(nonnumeric_s_pos, all_vars)
        is_target_supported = is_supported_tag(nonnumeric_t_pos, all_vars)
        if is_source_supported and is_target_supported:
            if (
                (nonnumeric_s_pos == 'V' or nonnumeric_s_pos in all_vars['pos_tags']['V']) and 
                (nonnumeric_t_pos == 'V' or nonnumeric_t_pos in all_vars['pos_tags']['V'])
            ):
                equivalent = ['VB', 'VBP'] # 'VBG', 'VBN', 'VBD', 'VBZ'
                '''
                    VB: Verb, base form - ask is do have 
                        VBP: Verb, non-3rd person singular present - ask is do have
                        VBZ: Verb, 3rd person singular present - asks is does has
                        VBG: Verb, gerund or present participle - asking, being, doing, having
                    VBD: Verb, past tense - asked, was/were, did, had
                    VBN: Verb, past participle - asked, used, been, done, had
                '''
                infinitive = lemmatizer.lemmatize(word, 'v')
                stem = stemmer.stem(infinitive)
                if infinitive in case_maps:
                    return case_maps[infinitive][target_pos]
                if target_pos == 'VB' or target_pos == 'VBZ':
                    return infinitive
                ''' to do: remove trailing e/s if applicable '''            
                new_word = ''.join([stem, target_endings[target_pos]])
                return new_word
    return False
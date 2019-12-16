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

def find_patterns(source_input, pattern_key, all_vars):
    '''
    if source_input is a list, get patterns between objects in the list,
    rather than patterns in a string source_input
    '''
    ''' a = {'pattern': 'source_words'} '''
    found_patterns = {}
    if type(source_input) == list or type(source_input) == set:
        found_patterns = get_patterns_between_objects(source_input)
    else:
        if pattern_key in all_vars['pattern_vars']:
            combined_key = ''.join(['patterns_', pattern_key])
            for pattern in all_vars['pattern_index'][pattern_key]:
                all_patterns = [pattern]
                for variable in all_vars['pattern_vars']:
                    if variable in pattern:
                        generated_patterns = generate_patterns_for_keyword_pattern(pattern, variable, all_vars)
                        if generated_patterns:
                            all_patterns.extend(generated_patterns)
                for ap in all_patterns:
                    found_subsets = get_pattern_source_subsets(source_input, pos_line, ap, 'pattern', all_vars)
                    if found_subsets:
                        if combined_key not in found_patterns:
                            found_patterns[combined_key] = {}
                        found_patterns[combined_key][pattern] = found_subsets
    if found_patterns:
        return found_patterns
    return False

def get_partial_pos(pattern, all_vars):
    pattern = convert_words_to_pos(pattern, all_vars)
    pattern_words = pattern.split(' ')
    new_pattern_words = []
    for pos_key in all_vars['supported_pattern_variables']:
        for w in pattern_words:
            ''' to do: this shouldnt be necessary '''
            #nonnumeric_var = ''.join([x for x in w if x in all_vars['alphabet']])
            #if nonnumeric_var in all_vars['supported_pattern_variables']:                
            #''' JJ found in all_vars['supported_pattern_variables'] '''
            if pos_key in all_vars['supported_pattern_variables']:
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
    pos_line = convert_words_to_pos(line, all_vars)
    pattern_map = add_indexes_to_repeated_words(pattern_map)
    reverse_keys = reversed(sorted(pattern_map.keys())) # to do: this should already be done in get_vars
    for source_pattern in reverse_keys:
        target_pattern = pattern_map[source_pattern]
        new_line, variables, generated_patterns = apply_pattern(pattern_map, source_pattern, target_pattern, line, pos_line, all_vars)
        if new_line:
            print('new line', new_line)
            print('vars', variables)
            print('generated patterns', generated_patterns)
            ''' to do: decide if you want to iterate or return line after first replaced pattern '''
            #line = new_line
            return new_line
    return line

def apply_pattern(pattern_map, source_pattern, target_pattern, line, pos_line, all_vars):
    variables = {}
    generated_patterns = {'source': [], 'target': []}
    nested_source_patterns, source_variables = get_nested_patterns(line, source_pattern, 'pattern', None, all_vars)
    nested_target_patterns, target_variables = get_nested_patterns(line, target_pattern, 'pattern', source_variables, all_vars)
    print('source_variables', source_variables)
    print('target_variables', target_variables)
    ''' get_nested_patterns returns ['VB x D1 D2''] from pattern = 'VB |NN JJ| D1 D2' '''
    if nested_source_patterns and nested_target_patterns:
        variables['source'] = source_variables if source_variables else {}
        variables['target'] = target_variables if target_variables else {}
        ''' 
        get_alt_patterns returns ['VB NN D1 D2', 'VB JJ D1 D2'] 
        from pattern = 'VB x D1 D2' and variables['x'] = 'NN JJ'
        # '|NN VB| of |ADV ADJ|': '|ADV ADJ| |NN VB|'
        '''
        for nsp in nested_source_patterns:
            alt_s_patterns = get_alt_patterns(nsp, variables['source'], all_vars)
            print('nsp', nsp, 'alt_s_patterns', alt_s_patterns)
            if alt_s_patterns:
                alt_s_patterns = alt_s_patterns if len(alt_s_patterns) > 0 else [nsp]
            alt_s_patterns = alt_s_patterns if alt_s_patterns else [nsp]
            if len(alt_s_patterns) > 0:
                generated_patterns['source'].extend(alt_s_patterns)
                for asp in alt_s_patterns:
                    ''' 
                    below logic (get target alt patterns & reposition) 
                    should only be called if get_pattern_source_subsets(asp, line) is True 
                    '''
                    found_asp_subsets = get_pattern_source_subsets(line, pos_line, asp, 'pattern', all_vars)
                    if found_asp_subsets:
                        print('found asp in source', asp, line)
                        for ntp in nested_target_patterns:
                            alt_t_patterns = get_alt_patterns(ntp, variables['target'], all_vars)
                            print('ntp', ntp, 'alt_t_patterns', alt_t_patterns)
                            if alt_t_patterns:
                                alt_t_patterns = alt_t_patterns if len(alt_t_patterns) > 0 else [ntp]
                            alt_t_patterns = alt_t_patterns if alt_t_patterns else [ntp]
                            if len(alt_t_patterns) > 0:
                                generated_patterns['target'].extend(alt_t_patterns)
                                for atp in alt_t_patterns:
                                    sub_pattern_map = {'source': asp, 'target': atp}
                                    applied = reposition(line, sub_pattern_map, all_vars)
                                    if applied:
                                        line = applied
                                        print('line', line, 'asp', asp, 'atp', atp)
        return line, variables, generated_patterns
    return False, False, False

def add_indexes_to_repeated_words(pattern_map):
    ''' 
        append position integers to repeated words in source & target patterns 
        if the same count is in the target pattern 
    '''
    new_pattern_map = {}
    for source_pattern, target_pattern in pattern_map.items():
        source_words = source_pattern.split(' ')
        target_words = target_pattern.split(' ')
        repeated_index = 0
        new_source_words = []
        for i, w in enumerate(source_words):
            source_count = source_words.count(w)
            if source_count > 1 and source_count == target_words.count(w):
                indexed_word = ''.join([w, str(repeated_index)])
                new_source_words.append(indexed_word)
                repeated_index += 1
            else:
                new_source_words.append(w)
        if len(new_source_words) > 0:
            new_source_pattern = ' '.join(new_source_words)
        repeated_index = 0
        new_target_words = []
        for i, w in enumerate(target_words):
            target_count = target_words.count(w)
            if target_count > 1 and target_count == source_words.count(w):
                indexed_word = ''.join([w, str(repeated_index)])
                new_target_words.append(indexed_word)
                repeated_index += 1
            else:
                new_target_words.append(w)
        if len(new_target_words) > 0:
            new_target_pattern = ' '.join(new_target_words)
            new_pattern_map[new_source_pattern] = new_target_pattern
    pattern_map = new_pattern_map if new_pattern_map else pattern_map
    return pattern_map

def reposition(subset, sub_pattern_map, all_vars):
    ''' subset = "inhibitor of compound"
        sub_pattern_map = {
            'source': "x of y",
            'target': "y x"
        }
        sub_pattern_map = {
            'source': "VBZ of NN",
            'target': "NN VBG"
        }
        output = "compound-inhibitor"
        to do:
        - handle target patterns with more words than source
        - handle other delimiters than space in case your source pattern has no spaces

        this should be identified as positive matches of the modifier pattern 'JJ NN':
        sub_pattern_map = {'source': "JJ1 NN1 of JJ2 NN2", 'target': "JJ2 NN2 JJ1 NN1"}
        subset = "catalyzing inhibitor of alkalizing enzyme"

        should we support | char here or embed that query? 
        - it should already be done with get_alt_patterns so no '|' should still be in the pattern string
    '''
    ''' need to identify that JJ1 is a variable without removing its identifier 1 '''
    print('reposition', subset, sub_pattern_map)
    delimiter = find_delimiter(subset, all_vars)
    if delimiter:
        ''' create a position map for source & target '''
        positions = {'source': {}, 'target': {}}
        source_words = sub_pattern_map['source'].split(delimiter)
        target_words = sub_pattern_map['target'].split(delimiter)
        for position, w in enumerate(sub_pattern_map['source'].split(delimiter)):
            positions['source'][position] = w
        for position, w in enumerate(sub_pattern_map['source'].split(delimiter)):
            target_word = target_words[position] if position < len(target_words) else ''
            positions['target'][position] = target_word
        '''
        positions = {
            'source': {0: 'x', 1: 'of', 2: 'y'},
            'target': {0: 'y', 1: '', 2: 'x'}
        }
        '''
        print('positions', positions)
        position_map = {}
        for source_position, source_word in positions['source'].items():
            for target_position, target_word in positions['target'].items():
                ''' to do: need to handle more complex cases with multiple matches '''
                if source_word == target_word:
                    ''' to do: exact word match or (supported_tag) '''
                    position_map[source_position] = target_position
                else:
                    if source_word in all_vars['pos_tags']['ALL_V'] and target_word in all_vars['pos_tags']['ALL_V']:
                        position_map[source_position] = target_position
        ''' position_map = {0: 2, 1: '', 2: 0} '''
        ''' now apply this mapping to the subset '''
        new_position_dict = {}
        for source_position, target_position in position_map.items():
            if source_position in positions['source'] and target_position in positions['target']:
                new_position_dict[target_position] = positions['source'][source_position]
        saved_words = subset.split(delimiter)
        print('saved words', saved_words)
        print('position map', position_map)
        new_words = {}
        for source_position, word in enumerate(saved_words):
            target_position = None
            for sp, tp in position_map.items():
                if sp == source_position:
                    target_position = tp
            if type(target_position) == int:
                source_var = positions['source'][source_position]
                target_var = positions['target'][target_position]
                nonnumeric_source_var = ''.join([x for x in source_var if x.lower() in all_vars['alphabet']])
                nonnumeric_target_var = ''.join([x for x in target_var if x.lower() in all_vars['alphabet']])
                source_is_var = True if nonnumeric_source_var in all_vars['pos_tags']['ALL'] or nonnumeric_source_var in all_vars['pos_tags'] else False
                target_is_var = True if nonnumeric_target_var in all_vars['pos_tags']['ALL'] or nonnumeric_target_var in all_vars['pos_tags'] else False
                print('source word', word, 'source var', source_var, 'target var', target_var, 'source position', source_position, 'target position', target_position)
                if source_is_var and target_is_var:
                    ''' this is a variable '''
                    if source_var != target_var:                           
                        ''' transform the original subset word from pos=source_var to pos=target_var like VBN => VBZ '''
                        conjugated_word = conjugate(word, source_var, target_var, all_vars) # word, source_pos, target_pos
                        if conjugated_word:
                            new_words[target_position] = conjugated_word
                    else:
                        ''' theres no verb variable transformation necessary, so just add the original word for this position '''
                        new_words[target_position] = word
                else:
                    ''' this is a word '''
                    if source_var == word or nonnumeric_source_var == word:
                        ''' 
                            exclude positional but non-content word matches like 'x' => 'the' 
                            but include indexed word matches like 'the' => 'the0' 
                        '''
                        new_words[target_position] = word
        if new_words:
            new_items = []
            for k in sorted(new_words.keys()):
                new_items.append(new_words[k])
            if len(new_items) > 0:
                new_line = delimiter.join(new_items)
                return new_line
    return False

def get_pattern_source_subsets(line, pos_line, pattern, get_type, all_vars):
    ''' get only the matching subsets from line with words in the same positions & pos as pattern
        ['pattern_instance_1', 'pattern_instance_2']
        support numerical variables by checking non-numeric pattern for match with pos_line 
        to do: this prevents users from configuring patterns with numbers like 14alpha-deoxy-enzyme
    '''
    subsets = []
    delimiter = find_delimiter(line, all_vars)
    delimiter = delimiter if len(delimiter) > 0 else ' '
    pos_pattern = convert_words_to_pos(pattern, all_vars)
    if delimiter:
        pattern_without_numbers = []
        for word in pos_pattern.split(delimiter):
            nonnumeric_word = ''.join([w for w in word if w not in '0123456789']) 
            if nonnumeric_word in all_vars['pos_tags']['ALL']:
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
                    if var in all_vars['pos_tags']['ALL'] or var in all_vars['pos_tags']:
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

def convert_words_to_pos(line, all_vars):
    new_line = []
    processing_line = line
    delimiters = ['|', '__', '&']
    for word in processing_line.split(' '):
        for d in delimiters:
            processing_word = word.replace(d, '')
        if word in all_vars['pos_tags']['ALL'] or word in all_vars['pos_tags']:
            ''' add tags (N, VB, NN, VBZ, etc) unchanged if found '''
            new_line.append(word)
        else:
            pos = get_nltk_pos(word, all_vars)
            if pos in all_vars['pos_tags']['ALL']:
                new_line.append(pos)
            else:
                new_line.append(word)
    line = ' '.join(new_line)
    return line

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
    if source_pos in all_vars['pos_tags']['V'] and target_pos in all_vars['pos_tags']['V']:
        equivalent = ['VB', 'VBD'] # 'VBG', 'VBN', 'VBP', 'VBZ'
        '''
            VB: Verb, base form - ask is do have 
                VBP: Verb, non-3rd person singular present - ask is do have
                VBZ: Verb, 3rd person singular present - asks is does has
                VBG: Verb, gerund or present participle - asking, being, doing, having
            VBD: Verb, past tense - asked, was/were, did, had
            VBN: Verb, past participle - asked, used, been, done, had
        '''
        case_maps = {
            'be': {'VB': 'is', 'VBD': 'was', 'VBG': 'is', 'VBN': 'been', 'VBP': 'is', 'VBZ': 'is'},
            'do': {'VB': 'do', 'VBD': 'did', 'VBG': 'doing', 'VBN': 'done', 'VBP': 'do', 'VBZ': 'does'},
            'have': {'VB': 'have', 'VBD': 'had', 'VBG': 'having', 'VBN': 'had', 'VBP': 'have', 'VBZ': 'has'}
        }
        infinitive = lemmatizer.lemmatize(word, 'v')
        stem = stemmer.stem(infinitive)
        if infinitive in case_maps:
            return case_maps[infinitive][target_pos]
        if target_pos == 'VB' or target_pos == 'VBZ':
            return infinitive
        target_endings = {
            'VB': '',
            'VBP': '',
            'VBZ': 's',
            'VBG': 'ing',
            'VBD': 'ed',
            'VBN': 'ed'
        }
        ''' to do: remove trailing e/s if applicable '''
        if source_pos in all_vars['pos_tags']['ALL'] and target_pos in all_vars['pos_tags']['ALL']:
            if source_pos != target_pos:
                new_word = ''.join([stem, target_endings[target_pos]])
                return new_word
    return False
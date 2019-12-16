import itertools
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
from get_pos import get_nltk_pos
from get_vars import get_all_versions, find_delimiter

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

def apply_pattern_map(line, pattern_map, all_vars):
    ''' 
    - this replaces a pattern with its associated pattern found in the line using variables 
        apply_pattern_map(line='dog of cat', pattern_map = {'noun1 of noun2' => 'noun2 noun1'}) = 'cat dog'
    to do:
        - for object_type in ['word', 'modifier', 'phrase'] - these should already be replaced with option sets of each type pattern 
        - modifier1 should be replaced with each modifier pattern + 1 and used to generate a new pattern containing each modifier pattern
        - when the source pattern is 'VBD VBN' and the target is 'VBZ' you need to isolate the 'VBN' which is the more meaningful verb
            currently its getting overridden by the consecutive verb which also matches the 'V' type but need a more robust way
        - in order to support iterated replacement, you need to make sure your patterns are ordered in the right way
    '''
    pos_lines = get_all_versions(line, 'all', all_vars)
    if pos_lines:
        for pos_line in pos_lines:
            for source_pattern, target_pattern in pattern_map.items():
                new_line = apply_pattern(pos_line, source_pattern, target_pattern, all_vars)
                if new_line:
                    print('applied pattern to line', new_line)
                    print('sp', source_pattern, 'tp', target_pattern)
                    line = new_line # return new_line if not iterating through all patterns in map
    return line

def find_patterns(line, pattern_key, all_vars):
    '''
    if line is a sequence, get patterns between objects in the list,
    rather than patterns in a line
    '''
    found_patterns = {}
    if type(line) == list or type(line) == set:
        found_patterns = get_patterns_between_objects(line)
    else:
        pos_lines = add_indexes_to_repeated_words(line, all_vars) 
        if pos_lines:
            if len(pos_lines) > 0:
                for pos_line in pos_lines:
                    if pattern_key in all_vars['pattern_index']:
                        combined_key = ''.join([pattern_key, '_patterns'])
                        for pattern in all_vars['pattern_index'][pattern_key]:
                            '''
                            only want to generate source patterns here, 
                            send a flag to not generate target patterns
                            '''
                            generated_patterns, generated_variables = generate_patterns_for_pattern(pattern, line, pos_line, all_vars)
                            if generated_patterns:
                                for gsp in generated_patterns['source']:
                                    found_subsets = get_pattern_source_subsets(line, pos_line, gsp, 'pattern', all_vars)
                                    if found_subsets:
                                        if combined_key not in found_patterns:
                                            found_patterns[combined_key] = {}
                                        found_patterns[combined_key][gsp] = found_subsets
    if found_patterns:
        return found_patterns
    return False

def apply_pattern(subset, source_pattern, target_pattern, all_vars):
    ''' subset = "inhibitor of compound", source_pattern = "VBZ of NN", target_pattern = "NN VBG"
        output = "compound-inhibitor"
        to do:
        - handle target patterns with more words than source
        - handle other delimiters than space in case your source pattern has no spaces
        - syntax delimiters ('|', '&') should be handled in prior processing in get_alt_patterns
        - return False if source_pattern not in subset
    '''
    print('apply_pattern', subset, source_pattern, target_pattern)
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
                if source_word == target_word:
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
    delimiter = find_delimiter(line, all_vars)
    pos_patterns = add_indexes_to_repeated_words(pattern, all_vars) 
    if pos_patterns and delimiter:
        if len(pos_patterns) > 0:
            subsets = []
            for pos_pattern in pos_patterns:
                if pos_pattern == pos_line:
                    return [pattern]
                if pos_pattern in pos_line:
                    if get_type == 'pattern':
                        subsets = get_pattern_source_words(line, pos_line.split(pos_pattern))
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
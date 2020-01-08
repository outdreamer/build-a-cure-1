from nltk import pos_tag, word_tokenize
from get_vars import get_blob, get_nltk_pos, convert_to_operators

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

def find_relationship(subset, row, av):
    '''
        - now you can generate the relationships based on operator logic stored in our row['clause']['condition'] objects
        - variables should be a dict like: { var_name : var_value, var_name: modifier }  ("x": "original_word")
        - each dict in row['clause']['condition'] indicates an independent clause in a sentence 
        - each clause is separated by subject, so there should only be one subject per row['clause']['condition']
            (can also be a sentence if its independent & contains one clause 
        - for relation [ 'x=y # z-a' ], 
            row['clause']['condition'][0] = {
                'type': 'statement', # 'condition'
                'subject': '',
                'statement': 'x=y',
                'conditional': '# z-a',
                'variables': {'s': 'original words'}
            }
        'x=y # z-a' == 'x is y independently of z is a' == 'x-y relationship is independent of z-a relationship'
        find_relationship(row, av) = ['x=y', 'a does not change x=y']
        - this is a generative function, applying each subject to each verb & each clause 
            to generate the full set of relationships in the sentence
        - this function is to catch all the meaning in clauses like: 
            "x reduced b inhibitor" => "x - i-b"
        - deriving relationships like:
            "x increases b" => "x+b"
            "x reduces inhibitor" => "x-i"
            "inhibitor reduces b" => "i-b"
            "x reduces b-inhibitor" => "x - b-i"
        - this function also applies combined operator impact from the configured map with get_impact() so that:
            "x - i-b" parses to "x+b" since "--" maps to "+"
        1. deconstructs the sentence based on operator logic so its represented by order of operations
            - applies operator logic to clauses to produce alternative relationships:
                - "x was b even with a" means a is irrelevant, so => relationships ["x was b", "a does not impact (x was b)"]
                - "x was a and was b" should produce => clause "x was (a and b)", relationship ["x was a", "x was b"], variable "(a and b)"
                - "x was a and therefore b" => clause "x was a so b", relationship ["a therefore b", "x leads to b"], variable "(a so b)"
                - "N V even with x or y" should produce: ["N V even with x", "N V even with y", "N V even with x or y"]
    '''
    original_row = row
    relationship = []
    clause_relations = []
    if type(row['clause']) == dict:
        for clause in row['clause']['condition']:
            '''
                for each subject, join:
                    - (subject + all combinations of statements + conditionals)
                    - net impact of (subject + all combinations of statements & conditionals)
                and add to relationship set for this row
            '''
            new_clause_relations = []
            subject = clause['subject']
            statement_combinations = get_combinations(clause['statement'], line)
            conditional_combinations = get_combinations(clause['conditional'], line)
            for statement in statement_combinations:
                for conditional in conditional_combinations:
                    subject_statement = ' '.join([subject, statement])
                    subject_statement_conditional = ' '.join([subject, statement, conditional])
                    new_clause_relations.append(subject_statement)
                    new_clause_relations.append(subject_statement_conditional)
                    subject_statement_impact = get_net_impact_relation(subject_statement)
                    if subject_statement_impact:
                       new_clause_relations.append(subject_statement_impact)
                    subject_statement_conditional_impact = get_net_impact_relation(subject_statement_conditional)
                    if subject_statement_conditional_impact:
                        new_clause_relations.append(subject_statement_conditional_impact)
            if len(new_clause_relations) > 0:
                for ncr in new_clause_relations:
                    relationship = convert_to_words(ncr, clause['variables'], av)
                    if relationship:
                        relationship.add(relationship) 
                clause_relations.extend(new_clause_relations)   
        print('\nclause_relations', clause_relations)
        print('\nrelationship', relationship)
        if len(clause_relations) > 0:
            row['clause_relations'] = clause_relations            
        if len(relationship) > 0:
            row['relationship'] = relationship
    if original_row != row:
        print('row', row)
        return row
    return False

def get_net_impact_relation(relation, av):
    '''  
    this function should only be applied to relations with more than one operator
    a relationship that has no spaces indicates an isolated modifier block like 'b-inhibitor'
    you could also wrap it in parenthesis to indicate order of operations

    example:
        example with two-operators (smallest number of operators qualifying for use of this function):
            get_impact('x - i-b') should return the net relationship 'x + b' and the full relationship 'x - i + b'
                initial = x - i,    # first/next
                impact = x + b,     # first/last
                full = x - i + b    # all
        example with more than two operators:
            relation = 'x - i-b - y+a + z-c'
            objects = x i b y a z c 
            combined_operators = 
                -
                - => -- => + 
                -
                + => -+ => - 
                +
                - => +- => -
            full = 'x - i + b - y - a + z - c'
    to do: 
        - right now it only supports "=", "+", "-" - add &, ^, and other operator support
        - this doesnt supported multi-layer nested operators yet
    '''
    # before iterating, replace & combine consecutive operators
    letters = []
    operators = []
    operator_sequence = []
    for w in relation:
        if w in av['clause_map']:
            if len(operator_sequence) > 0:
                operator_sequence.append(w)
            else:
                operator_sequence = [w]
        else:
            if len(operator_sequence) > 0:
                operator_string = ''.join(operator_sequence)
                if len(operator_sequence) > 1:
                    net_operator = get_combined_operator(combined, av)
                    if net_operator:
                        letters.append(net_operator)
                        operators.append(net_operator)
                elif len(operator_sequence) == 1:
                    letters.append(operator_string)
                    operators.append(operator_string)
                operator_sequence = []
            letters.append(w)
    ''' now you should have any consecutive operators like '++' or '+ -' replaced with their combined version '+' or '-' '''
    relation = ''.join(letters)
    ''' if there is only one or zero operators, no application of operator logic necessary '''
    if len(operators) < 2:
        return False
    operators = []
    new_words = []
    sub_relations = []
    full_relation = []
    for word in relation.split(' '):
        if word not in av['clause_map']:
            ''' could be sub-relation 'i-b' or a word like 'x' '''
            sub_operator_in_word = [x for x in word if x in av['clause_map']]
            if len(sub_operator_in_word) > 0:
                if len(sub_operator_in_word) == 1:
                    ''' this is a sub-relation like a modifier 'i-b' with no spaces to indicate a sub-unit '''
                    sub_operator = sub_operator_in_word[0]
                    sub_words = word.split(sub_operator)
                    # dont add sub-words or sub-operators to operators
                    ''' each sub relation should be reduced to three items (a modifier like 'inhibitor - b') at this point '''
                    if len(sub_words) == 3:
                        prev_operator = operators[-1] if len(operators) > 0 else None
                        if prev_operator:
                            combined = ''.join([prev_operator, sub_operator])
                            if len(combined) > 1:
                                net_operator = get_combined_operator(combined, av)
                                if net_operator:
                                    initial_sub_relation = ' '.join([new_words[-1], prev_operator, sub_words[0]]) # x - i
                                    second_sub_relation = ' '.join([new_words[-1], net_operator, sub_words[2]]) # x + b
                                    full_relation.extend([sub_words[0], net_operator, sub_words[2]])
                                    sub_relations.append(initial_sub_relation, second_sub_relation)
                        else:
                            print('no prev operator, this is the first relation')
                            sub_relation = ' '.join(word)
                            all_relations.append(sub_relation)
                    else:
                        print('more than 2 objects per logical unit', word, relation)
                        exit()
                else:
                    print('more than one operator per logical unit', word, relation)
                    exit()
            else:
                pos = get_nltk_pos(word, av)
                if pos:
                    if pos in av['tags']['N']:
                        ''' 
                        only add nouns for impact relationship analysis - 
                        should already be done but just verifying 
                        '''
                        new_words.append(word)
                else:
                    if word in av['alphabet'] or word in variables:
                        print('found var', word)
                    new_words.append(word)
        else:
            ''' this is an operator, log it for use in prev_operator '''
            operators.append(word)
    all_relations = [] 
    if len(sub_relations) > 0:
        all_relations.extend(sub_relations)
    if len(full_relation) > 0:
        all_relations.append(full_relation)
    if len(all_relations) > 0:
        return all_relations
    return False

def get_combinations(object_list, line):
    combinations = object_list
    ''' get impact of each individual item in object_list '''
    impacts = []
    for item in object_list:        
        impact = get_impact(item)
        if impact:
            impacts.append(impact)
    ''' to do: remove combinations that arent in original order in line '''
    combs = itertools.combinations(object_list)
    if combs:
        if len(combs) > 0:
            combinations.extend(combs)
    for c in combinations:
        ''' and get impact of each object combination '''        
        impact = get_impact(c)
        if impact:
            combinations.append(impact)
    if len(combinations) > 0:
        return combinations
    return False

def get_operator(word, av):
    for k, values in av['clause_map'].items():
        if word in values:
            return  k
    return False

def convert_to_words(line, variables, av):
    new_words = []
    for word in line.split(' '):
        if word in variables:
            new_words.append(variables[word])
        else:
            found_operator_or_variable = False
            for k, values in av['clause_map'].items():
                if k in word: # for indexed vars like +1, -1, =1
                    if word in variables:
                        new_words.append(variables[word])
                        found_operator_or_variable = True
                    else:
                        ''' 
                        if no variable assigned for this operator, 
                        choose the first word in clause_map list for this operator 
                        '''
                        new_words.append(values[0])
                        found_operator_or_variable = True
            if not found_operator_or_variable:
                ''' just a word, not an operator or other variable '''
                new_words.append(word)
    if len(new_words) > 0:
        return ' '.join(new_words)
    return False

def find_clause(subset, row, av):
    ''' 
        - clauses are relationships between subject and objects in line separated by delimiters like:
            prepositions, conjunctions, determiners, and punctuation

        - this function: 
            - splits by delimiters (and, or, because, ',', ';')
            - filters out meaningless clauses with filter_clauses()
            - orders clauses based on operator logic for ordered_operators with order_clauses()
            - separates the line by subjects, delimiters, & verbs
            - converts to operators & variables 
            - creates clause dicts: 
                row['clause'] = [
                    {                
                        'type': '',
                        'variables': clause_variables,
                        'subject': '',
                        'conditional': [],
                        'statement': [], # contains verb + rest of predicate
                        'delimiter': []
                    }
                ]
        - once you identify modifiers, identifying clauses is mostly a matter of identifying subjects and operators (and, because, ',')
        - check for verb tenses normally used in passive sentences # had been done = past perfect
        - translate questions into statements of intent: "would there be an effect of x on y?" intent = "evaluate x-y relationship" 
            where clauses include: ['subject verb relationship(s)', 'conditional(s)']
            and relationships include: ['subject verb relationship(s)', 'subject verb relationship(s) conditional(s)']
    '''
    original_row = row
    variables = {}
    row['clause'] = []
    split = split_by_delimiters(subset, av)
    new_split = filter_clauses(split, av)
    if new_split:
        subset = ' '.join(new_split)
    no_punctuation_subset = subset
    for cd in av['clause_punctuation']:
        if cd in no_punctuation_subset:
            no_punctuation_subset = no_punctuation_subset.replace(cd, '***')
    clauses_by_punctuation = no_punctuation_subset.split('***')
    print('clauses_by_punctuation', clauses_by_punctuation)
    operator_clauses = {}
    for oc in clauses_by_punctuation:
        operator_clause, variables = convert_to_operators(oc, av)
        if operator_clause:
            operator_clauses[operator_clause] = variables if variables else {}
    print('operator clauses', operator_clauses)
    new_subset = order_clauses(subset, clauses_by_punctuation, av)
    print('new_subset', new_subset)
    if new_subset:
        subset = new_subset
    print('subset', subset)
    '''
    clauses_by_punctuation ['x acts as agonizing inhibits of y']
    operator clauses {'x acts as agonizing inhibits of y': {}}
    new_subset x acts as agonizing inhibits of y
    subset x acts as agonizing inhibits of y
    '''
    all_subjects = [] # there should only be one subject per clause set
    ''' sentence should be in active voice by now '''
    if operator_clauses:
        print('operator clauses', operator_clauses)
        for operator_clause, clause_variables in operator_clauses.items():
            print('parsing operator clause', operator_clause, 'variables', clause_variables)
            cmap = {                
                'type': '',
                'variables': clause_variables,
                'subject': '',
                'conditional': [],
                'statement': [], # contains verb + rest of predicate
                'delimiter': []
            }
            verb_index = 0
            operator_clause = ' '.join(operator_clause) if type(operator_clause) == list else operator_clause
            original_clause_words = operator_clause.split(' ')
            print('ocw', original_clause_words)
            for i, w in enumerate(original_clause_words):
                if verb_index == 0:
                    if w not in cmap['subject']:
                        pos = get_nltk_pos(w, av)
                        blob = get_blob(w)
                        if w not in av['tags']['ALL']:
                            all_subjects.append(w)
                            cmap['subject'] = w # make sure subjects are not repeated across clause entries
                if w in row['verb']: # found a verb
                    verb_index = i
                    cmap['statement'] = original_clause_words[(i - 1):len(original_clause_words)]
                    operator_statement, variables = convert_to_operators(cmap['statement'], av)
                    if operator_statement:
                        cmap['statement'] = operator_statement
                elif w in av['clause_delimiters']:
                    cmap['delimiter'].append(w)
            cmap['conditional'] = operator_clause.replace(cmap['subject'], '')
            for statement in cmap['statement']:
                cmap['conditional'] = operator_clause.replace(statement, '')
            ''' to do: split conditional by condition keywords '''
            operator_condition, variables = convert_to_operators(cmap['conditional'], av)
            if operator_condition:
                cmap['conditional'] = operator_condition
            ''' determine what type of clause this is '''
            condition_score = 0
            statement_score = 0
            for key in ['statement', 'conditional']:
                if len(cmap[key]) > 0:
                    for item in cmap[key]:
                        verb_count = [v for v in av['verb_operators'] if v in item]
                        condition_count = [w for w in av['causal_operators'] if w in item]
                        ''' found verb in item so probably a statement unless:
                            - the verb is part of a verb phrase like 'even with alkalizing process'
                            - it has definitive condition keywords 
                        '''
                        if len(condition_count) > 0:
                            condition_score += 1
                        elif len(verb_count) > 0:
                            statement_score += 1
            cmap['type'] = 'condition' if condition_score > statement_score else 'statement'
            if cmap:
                print('found cmap', cmap)
                row['clause'].append(cmap)
        print('\nall row clauses', row['clause'])
    '''
        operator clauses {'x acts as agonizing inhibits of y': {}}
        parsing operator clause x acts as agonizing inhibits of y variables {}
        ocw ['x', 'acts', 'as', 'agonizing', 'inhibits', 'of', 'y']
        found cmap {'type': 'statement', 'variables': {}, 'subject': 'acts', 'conditional': 'x acts as agonizing inhibits of ', 'statement': 'agonizing inhibits of y', 'delimiter': []}
        all row clauses [{'type': 'statement', 'variables': {}, 'subject': 'acts', 'conditional': 'x acts as agonizing inhibits of ', 'statement': 'agonizing inhibits of y', 'delimiter': []}]
    '''
    # the process was activated because x was signaling successfully
    # x successful signals activated the process
    # should replace independence operators with 'with' because the next clause is true regardless but retain not ! operator
    if original_row != row:
        return row
    return False

def split_by_delimiters(line, av):
    new_sections = []
    new_section = []
    for word in line.split(' '):
        punctuation_found = False
        for punctuation in av['clause_punctuation']:
            if punctuation in word:
                word = word.replace(punctuation, '')
                new_section.append(word)
                new_sections.append(' '.join(new_section))
                new_sections.append(punctuation)
                punctuation_found = True
        if not punctuation_found:
            delimiter_found = False
            for k, values in av['clause_map'].items():
                if word in values:
                    new_sections.append(' '.join(new_section))
                    new_section = []
                    new_sections.append(word)
            if not delimiter_found:
                new_section.append(word)
    if len(new_section) > 0:
        new_sections.append(' '.join(new_section))
    if len(new_sections) > 0:
        return new_sections
    return False

def order_clauses(line, clauses_by_punctuation, av):
    '''
    - conditional clauses have a delimiter that indicates a condition or dependency:
        'or', 'when', 'even', 'despite', 'because', 
        they are not always indicated by common operators like 'and', 'but', 'yet', 'still'

    - example of equally important clauses:
        line = "the protein should have activated the process, but the process killed the cell anyway"
        clauses = ["protein does not activate the process", "process kills cells"]

    - filter_clauses removes clauses that dont change the output impact of the sentence
        
    - arranges clauses according to operators: line = 'x was y even with a' => 'x = y # a'

    - "in the event of onset, symptoms appear at light speed, even if you take vitamin c at the max dose" =>
        "you take" => "" # it's implied that a patient will be taking the medicine 
            because thats the intent of consuming the information, so it doesnt need to be stated
        "vitamin c at the max dose" => modifier pattern "max dose vitamin c"

    - at this point row['line'] is broken into a condition entry for each clause: 

    - this function should conduct ordering operations:
        - 'non-verb clause, verb_clause' => 
          'verb_clause non-verb clause' => 
          'if x then y' => 
          'y if x'
        - 'subject1 verb clause because subject2 verb clause' => 
          'subject2 verb-to-noun causes subject1 verb-to-noun'
        - 'the process activated x because y inhibits b' => 
          'y b-inhibition causes the process to activate x' => 
          'y b-inhibition enables process to activate x'
    '''
    ''' rearrangement logic '''
    for k in av['ordered_operators']:
        if k == 'because':
            ''' check that each 'because' keyword is not in the first clause, otherwise leave it where it is '''
            for v in av['clause_map']['%']:
                for i, word in enumerate(line.split(' ')):
                    if v == word:
                        if v not in clauses_by_punctuation[0]:
                            ''' to do: assign ratio logic here, 3 is minimum relation length '''
                            line = ' causes '.join(reversed(line.split(v)))
    ''' to do: replace verb + not with antonym & handle 'despite' operator '''
    if line:
        return line
    return False

def filter_clauses(clauses, av):
    ''' removes meaningless clauses '''
    return clauses

def get_combined_operator(combined, av):
    for key, val in av['combined_map'].items():
        if combined in val:
            return key
    return False

def get_meaning_score(phrase, line):
    '''
    this should return 0 for phrases 
    that dont change the meaning of the sentence
    (mostly any phrase without a verb) 
    lines with more variation between words & compared to intent are more meaningful
    '''
    meaning = 0
    if meaning:
        return meaning
    return False

def find_modifier(subset, row, av):
    '''
    - we're isolating modifiers bc theyre the smallest unit of 
        functions (inputs, process, outputs)
        which can be embedded in phrases, clauses, and sentences
    - we wouldnt add noun modifiers which imply an action in the past which wont be repeated:
        "protein isolate"
    - only verb modifiers which imply an action in the present to indicate ongoing relevant functionality:
        "ionizing radiation", "ionizer of radiation"
    - noun modifiers should be indexed as phrases, so get_phrases has to be called before this function
    - use cardinal numbers to get metric modifiers
    - apply pattern_map functionality first if it can replace patterns in modifiers 
    - otherwise continue with below logic
        convert "x subset_keyword y" to "y x"
        subset_keywords = ['of', 'in', 'from']
            "item in list" => "list item"
            "inhibitor of x" => "x-inhibitor"
    - change words to their stem and get the pos of their stem 
        "x has effect of membrane disruption" is a modifier pattern: "x has function of noun noun" 
        "x has function of noun1 noun2": "x noun1 noun2 function"
      but the second noun is a conjugation of a verb "disrupt" so should be converted to "x disrupts membranes"
    - takes out determiners if indicating 'one', 'some', or 'same' quantity 
    '''
    original_row = row
    modifier = None
    tagged_dict = {} 
    blob_dict = {}
    words = subset.split(' ')
    tagged = pos_tag(word_tokenize(subset))
    if tagged:
        for item in tagged:
            tagged_dict[item[0]] = item[1]
        blob = get_blob(subset)
        if blob:
            blob_tokens = blob.parse()
            if blob_tokens:
                for token in blob_tokens:
                    blob_dict[token] = token.split('/')
        if tagged_dict and blob_dict:
            for i, word in enumerate(words):
                pos = row['word_map'][word] if word in row['word_map'] else ''
                if pos:
                    if pos not in av['tags']['exclude']:
                        if word in blob_dict and word in tagged_dict:
                            modifier = word
                            other_word = words[i + 1] if (i + 1) < len(words) else words[i - 1] if i > 0 else None
                            if other_word:
                                other_word_pos = row['word_map'][other_word] if other_word in row['word_map'] else ''
                                if other_word_pos in av['tags']['ALL_N'] or other_word_pos in av['tags']['ALL_V']:
                                    row['modifier'].add(' '.join([ratio, other_word]))
    if original_row != row:
        return row
    return False

def find_phrase(subset, row, av):
    words = subset.split(' ')
    phrases = split_by_subset(words, 'pos', av['tags']['DPC'], av)
    if phrases:
        if len(phrases) > 0:
            return set(phrases)
    return False

def find_verb_phrase(subset, row, av):
    verb_phrases = set()
    if 'phrase' in row:
        for p in row['phrase']:
            for w in p.split(' '):
                pos = row['word_map'][w] if w in row['word_map'] else get_nltk_pos(w, av)
                if pos:
                    if pos in av['tags']['V']:
                        verb_phrases.add(p)
    if len(verb_phrases) > 0:
        return verb_phrases
    return False

def find_noun_phrase(subset, row, av):
    noun_phrases = set()
    if 'phrase' in row:
        for p in row['phrase']:
            for w in p.split(' '):
                pos = row['word_map'][w] if w in row['word_map'] else get_nltk_pos(w, av)
                if pos:
                    if pos in av['tags']['N']:
                        noun_phrases.add(p)
    if len(noun_phrases) > 0:
        return noun_phrases
    return False

def find_attribute(subset, row, av):
    return False

def find_function(subset, row, av):
    return False

def split_by_subset(items, check_var, check_list, av):
    subsets = []
    subset = []
    for w in items:
        check_var = get_nltk_pos(w, av) if check_var == 'pos' else w if check_var == 'word' else None
        if check_var:
            if check_var in check_list:
                subsets.append(' '.join(subset))
                subset = []
            else:
                subset.append(w)
    if len(subset) > 0:
        subsets.append(' '.join(subset))
    if len(subsets) > 0:
        return subsets
    return False
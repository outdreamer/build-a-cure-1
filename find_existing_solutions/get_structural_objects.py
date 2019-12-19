def find_relationship(row, all_vars):
    '''
        now you can generate the relationships based on operator logic stored in our row['clause']['condition'] objects
        
        - variables should be a dict like: { var_name : var_value, var_name: modifier }  ("x": "original_word")
        - each dict in row['clause']['condition'] indicates an independent clause in a sentence 
        - each clause is separated by subject, so there should only be one subject per row['clause']['condition']
            (can also be a sentence if its independent & contains one clause 

        for relation [ 'x=y # z-a' ], 
            row['clause']['condition'][0] = {
                'type': 'statement', # 'condition'
                'subject': '',
                'statement': 'x=y',
                'conditional': '# z-a',
                'variables': {'s': 'original words'}
            }

        'x=y # z-a' == 'x is y independently of z is a' == 'x-y relationship is independent of z-a relationship'

        find_relationship(row, all_vars) = [
            'x=y',
            'a does not change x=y'
        ]

        - this is a generative function, applying each subject to each verb & each clause 
            to generate the full set of relationships in the sentence

        - this function is to catch all the meaning in clauses like: 
            "x reduced b inhibitor" => "x - i-b"

        deriving relationships like:
            "x increases b" => "x+b"
            "x reduces inhibitor" => "x-i"
            "inhibitor reduces b" => "i-b"
            "x reduces b-inhibitor" => "x - b-i"

        this function also applies combined operator impact from the configured map with get_impact() so that:
            "x - i-b" parses to "x+b" since "--" maps to "+"

        1. deconstructs the sentence based on operator logic so its represented by order of operations
            - applies operator logic to clauses to produce alternative relationships:
                - "x was b even with a" means a is irrelevant, so => relationships ["x was b", "a does not impact (x was b)"]
                - "x was a and was b" should produce => clause "x was (a and b)", relationship ["x was a", "x was b"], variable "(a and b)"
                - "x was a and therefore b" => clause "x was a so b", relationship ["a therefore b", "x leads to b"], variable "(a so b)"
                - "N V even with x or y" should produce: ["N V even with x", "N V even with y", "N V even with x or y"]
    '''
    word_relation = []
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
            for ncr in new_clause_relations:
                word_relation = convert_to_words(ncr, clause['variables'], all_vars)
                if word_relation:
                    word_relations.add(word_relation) 
            clause_relations.extend(new_clause_relations)   

        print('\nclause_relations', clause_relations)
        print('\nword_relations', word_relations)
        if len(clause_relations) > 0:
            row['clause_relations'] = clause_relations            
        if len(word_relations) > 0:
            row['word_relations'] = word_relations
    return row

def get_net_impact_relation(relation, all_vars):
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
        - right now it only supports "=", "+", "-": add &, ^, and other operator support
        - this doesnt supported multi-layer nested operators yet
    '''
    # before iterating, replace & combine consecutive operators
    letters = []
    operators = []
    operator_sequence = []
    for w in relation:
        if w in all_vars['clause_map']:
            if len(operator_sequence) > 0:
                operator_sequence.append(w)
            else:
                operator_sequence = [w]
        else:
            if len(operator_sequence) > 0:
                operator_string = ''.join(operator_sequence)
                if len(operator_sequence) > 1:
                    net_operator = get_combined_operator(combined, all_vars)
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
        if word not in all_vars['clause_map']:
            ''' could be sub-relation 'i-b' or a word like 'x' '''
            sub_operator_in_word = [x for x in word if x in all_vars['clause_map']]
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
                                net_operator = get_combined_operator(combined, all_vars)
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
                pos = get_nltk_pos(word, all_vars)
                if pos:
                    if pos in all_vars['pos_tags']['N']:
                        ''' 
                        only add nouns for impact relationship analysis - 
                        should already be done but just verifying 
                        '''
                        new_words.append(word)
                else:
                    if word in all_vars['alphabet'] or word in variables:
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

def get_operator(word, all_vars):
    for k, values in all_vars['clause_map'].items():
        if word in values:
            return  k
    return False

def convert_to_words(line, variables, all_vars):
    new_words = []
    for word in line.split(' '):
        if word in variables:
            new_words.append(variables[word])
        else:
            found_operator_or_variable = False
            for k, values in all_vars['clause_map'].items():
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

def find_clause(pattern, matches, row, all_vars):
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

    line = row['line']
    split_by_delimiters = split_by_delimiters(line)
    new_split = filter_clauses(split_by_delimiters, all_vars)
    if new_split:
        split_by_delimiters = new_split
        line = ' '.join(new_split)
    no_punctuation_line = line
    for cd in all_vars['clause_punctuation']:
        if cd in no_punctuation_line:
            no_punctuation_line = no_punctuation_line.replace(cd, '***')
    clauses_by_punctuation = no_punctuation_line.split('***')
    print('clauses_by_punctuation', clauses_by_punctuation)
    operator_clauses = {}
    for oc in clauses_by_punctuation:
        operator_clause, variables = convert_to_operators(clause, all_vars)
        if operator_clause:
            operator_clauses[operator_clause] = variables if variables else {}
    print('operator clauses', operator_clauses)
    new_line = order_clauses(line, clauses_by_punctuation, all_vars)
    if new_line:
        line = new_line
    all_subjects = []
    row['clause'] = []
    if operator_clauses:
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
            for i, w in enumerate(operator_clause.split(' ')):
                if verb_index == 0:
                    if w not in all_subjects:
                        cmap['subject'].append(w)
                        all_subjects.append(w) # make sure subjects are not repeated across clause entries
                if v in row['verb']: # hit the verb, exit
                    verb_index = i
                    cmap['statement'] = original_clause_words[(i - 1):len(original_clause_words)]
                    operator_statement = convert_to_operators(cmap['statement'], all_vars)
                    if operator_statement:
                        cmap['statement'] = operator_statement
                elif w in all_vars['clause_delimiters']:
                    cmap['delimiter'].append(w)
            cmap['conditional'] = original_clause.replace(cmap['subject'], '')
            cmap['conditional'] = cmap['conditional'].replace(cmap['statement'], '')
            operator_condition = convert_to_operators(cmap['conditional'], all_vars)
            if operator_condition:
                cmap['conditional'] = operator_condition
            ''' determine what type of clause this is '''
            for key in ['statement', 'conditional']:
                if len(cmap[key]) > 0:
                    verb_operator_count = 0
                    for v in all_vars['verb_operators']:
                        if v in cmap[key]:
                            verb_operator_count += 1
                    if verb_operator_count > 0 and len(cmap['subject']) > 0:
                        ''' probably a statement unless:
                            - the verb is part of a verb phrase like 'even with alkalizing process'
                            - it has definitive condition keywords 
                        '''
                        for w in all_vars['causal_operators']:
                            if w in cmap[key]:
                                ''' found a definitive causal keyword '''
                                cmap['type'] = 'condition'
                        if 'type' not in conditional:
                            cmap['type'] = 'statement'
                    else:
                        for w in all_vars['causal_operators']:
                            if w in cmap[key]:
                                ''' found a definitive condition keyword '''
                                cmap['type'] = 'condition'
            if cmap:
                print('found cmap', cmap)
                row['clause'].append(cmap)
        print('\nall row clauses', row['clause'])
    # the process was activated because x was signaling successfully
    # x successful signals activated the process
    # should replace independence operators with 'with' because the next clause is true regardless but retain not ! operator
    print('\nfinal row', row)
    return row

def split_by_delimiters(line, all_vars):
    new_sections = []
    new_section = []
    for word in line.split(' '):
        punctuation_found = False
        for punctuation in all_vars['clause_punctuation']:
            if punctuation in word:
                word = word.replace(punctuation, '')
                new_section.append(word)
                new_sections.append(' '.join(new_section))
                new_sections.append(punctuation)
                punctuation_found = True
        if not punctuation_found:
            delimiter_found = False
            for k, values in all_vars['clause_map'].items():
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

def order_clauses(line, clauses_by_punctuation, all_vars):
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

    lines = []

    ''' rearrangement logic '''
    for k, values in all_vars['ordered_operators']:
        if k == 'because':
            ''' check that each 'because' keyword is not in the first clause, otherwise leave it where it is '''
            for v in all_vars['clause_map']['%']:
                for i, word in enumerate(line.split(' ')):
                    if v == word:
                        if v not in clauses_by_punctuation[0]:
                            ''' to do: assign ratio logic here, 3 is minimum relation length '''
                            line = ' causes '.join(reversed(line.split(v)))
    #elif k == 'not':
    #for line in lines:
    ''' to do: replace verb + not with antonym & handle 'despite' operator '''
    if line:
        return line
    return False

def filter_clauses(clauses, all_vars):
    ''' removes meaningless clauses '''
    return clauses

def get_combined_operator(combined, all_vars):
    for key, val in all_vars['combined_map'].items():
        if combined in val:
            return key
    return False

def find_attribute(pattern, matches, row, all_vars):
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

def find_modifier(pattern, matches, row, all_vars):
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
      but the second noun is a conjugation of a verb "disrupt" so should be converted to 
      "x disrupts membranes"
    '''
    ''' takes out determiners if indicating 'one', 'some', or 'same' quantity '''
    modifier = None
    modified = None   
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
                for token, val in blob_tokens.items():
                    blob_dict[token] = val.split('/')
        if tagged_dict and blob_dict:
            for i, word in enumerate(words):
                pos = row['word_map'][word] if word in row['word_map'] else ''
                if pos:
                    if pos not in all_vars['pos_tags']['exclude']:
                        if word in blob_dict and word in tagged_dict:
                            #if blob_dict[word][0] != tagged_dict[word]:
                            ''' ntlk and blob tags differ: nltk: 'imaging' => 'VBG' blob: 'imaging' => 'NN', 'B-NP', 'I-PNP' '''
                            modifier = word
                            other_word = words[i + 1] if (i + 1) < len(words) else words[i - 1] if i > 0 else None
                            if other_word:
                                other_word_pos = row['word_map'][other_word] if other_word in row['word_map'] else ''
                                if other_word_pos in all_vars['pos_tags']['ALL_N'] or other_word_pos in all_vars['pos_tags']['ALL_V']:
                                    row['modifier'].add(' '.join([ratio, other_word]))
    return row

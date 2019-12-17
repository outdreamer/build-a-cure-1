import random
from utils import *
from get_synonyms import *
from get_vars import get_new_key

def find_relationship(row, all_vars):
    ''' now you can generate the relationships based on operator logic stored in our row['clause']: 
        row['clause'] = {
            '(x = y) # a': [
                'x = y',
                '(x = y) # a', # (x = y) independently of a
                'a !@ (x = y)' # a does not change (x = y)
            ]
        }
        find_relationship(row, all_vars) = [
            'x is y',
            'x is y even with a',
            'a does not change (x is y)'
        ]
        - this is a generative function, applying each subject to each verb & each clause 
            to generate the full set of relationships in the sentence
        - this function is to catch all the meaning in clauses like: 
            "x reduced b inhibitor" => "x - (i - b)"
        - and your current logic will only capture: 
            "x reduced b"
        when in reality youd want to store the full clause so the relationships can be derived:
            "x increases b" => "x + b"
            "x reduces inhibitor" => "x - i"
            "inhibitor reduces b" => "i - b"
        operator_clauses is original clauses with operators instead of verbs & variable names instead of sub-clauses: ["x - a"]
        so it can do substitutions and derive the alternate relationships in get_combined_relationships()

        1. deconstructs the sentence based on operator logic so its represented by order of operations
            - applies operator logic to clauses to produce alternative relationships:
                - "x was b even with a" means a is irrelevant, so => relationships ["x was b", "a does not impact (x was b)"]
                - "x was a and was b" should produce => clause "x was (a and b)", relationship ["x was a", "x was b"], variable "(a and b)"
                - "x was a and therefore b" => clause "x was a so b", relationship ["a therefore b", "x leads to b"], variable "(a so b)"
                - "N V even with x or y" should produce: ["N V even with x", "N V even with y", "N V even with x or y"]

    '''
    variables = {}
    operator_clauses = {}
    ''' variables should be a dict like: { var : modifier relationship }  ("a": "i - b") '''
    variables['subject'] = row['clause']['subject']
    word_relationships = []
    for v, verb_clause in enumerate(row['clause']['verb_relationship']):
        ''' for each verb_relationship r, join it with the subject & each conditional & add the combined version '''
        operator_verb_clause = convert_to_operators(verb_clause, all_vars)
        new_clause = ' '.join([variables['subject'], operator_verb_clause])
        operator_clauses[new_clause] = verb_clause
        word_relationships.append(' '.join([variables['subject'], verb_clause]))
        for c, condition_clause in enumerate(row['clause']['conditional']):
            operator_condition_clause = convert_to_operators(condition_clause, all_vars)
            new_condition_clause = ' '.join([variables['subject'], operator_verb_clause, operator_condition_clause])
            operator_clauses[new_condition_clause] = condition_clause
            word_relationships.append(' '.join([variables['subject'], verb_clause, condition_clause]))
    operator_relationships = set(operator_clauses.keys())
    print('\nvariable', variables)
    print('\nword_relationship', word_relationships)
    print('\noperator_relationship', operator_relationships)
    print('\noperator_clause', operator_clauses.keys())
    placeholder_clauses = []
    for operator_clause in operator_clauses:
        placeholder_clause, variables = replace_with_placeholders(operator_clause, variables, all_vars)   
        placeholder_clauses.append(placeholder_clause)
    print('\nplaceholder', placeholder_clauses)
    if len(placeholder_clauses) > 0:
        relationships = get_combined_relationships(placeholder_clauses, row['clause'], variables, all_vars)
        if relationships:
            return relationships
    return False

def replace_with_placeholders(operator_clause, variables, all_vars):
    ''' what differentiates a variable from a normal word? 
        variables are used to refer to components of sub-logic that include 
        an embedded relationship which must be handled associatively 
        so that x - a+b ends up as two relationships: x-a and x+b

        right now this just supports identifying basic units of sub-logic such as:
        - modifiers, like "enzyme analyzer"
        - conditional clauses

        this is step 2 in the below workflow:
        - in order to preserve order of operations:
            1. first converting "b inhibitor" to:
                { new_key: modifier_relationship } = {"a": "i-b"}
            2. then converting "x - i-b" to "x-a" and storing in placeholder_clauses
            3. then converting "x-a" to permuted relationship set:
                "x-i" and "x+b"
    '''
    placeholder_clause = []
    delimiter = '+' if '+' in operator_clause else '-' if '-' in operator_clause else '='
    for i, word_set in enumerate(operator_clause.split(delimiter)):
        word_set = word_set.strip()
        if word_set not in ['+', '-', '=', 'subject']:
            new_key = get_new_key(variables, all_vars)
            variables[new_key] = word_set
            placeholder_clause.append(new_key)
        else:
            placeholder_clause.append(word_set)
    placeholder_string = delimiter.join(placeholder_clause)
    return placeholder_string, variables

def get_combined_relationships(placeholder_clauses, conditional_items, variables, all_vars):
    '''
    this is step 3 in the below workflow:
    - in order to preserve order of operations:
        1. first converting "b inhibitor" to: { new_key: modifier_relationship } = {"a": "i-b"}
        2. then converting "x - i-b" to "x-a" and storing in placeholder_clauses
        3. then converting "x-a" to permuted relationship set: "x-i" and "x+b"
    '''
    subject = None
    operator = None
    symbol_relationships = set()
    for pc in placeholder_clauses:
        new_relationship = replace_operators_with_words(pc, conditional_items, variables, all_vars)
        if new_relationship:
            symbol_relationships.add(new_relationship)
    if len(symbol_relationships) > 0:
        return symbol_relationships
    return False

def replace_operators_with_words(pc, conditional_items, variables, all_vars):
    relationships = set()
    relationship = set()
    new_pc_words = []
    sub_relationship = []
    reverse_var_keys = reversed(sorted(variables.keys()))
    for k in reverse_var_keys:
        pc = pc.replace(k, variables[k])
        for operator, word in all_vars['operator_map'].items():
            if operator in pc:
                pc = pc.replace(operator, ''.join([' ', word, ' ']))
    if pc:
        return pc
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

def find_clause(pattern, matches, row, all_vars):
    ''' 
        - clauses are relationships between subject and objects in line separated by delimiters like:
            prepositions, conjunctions, determiners, and punctuation

        - this function: 
            - separates the line by subjects, delimiters, & verbs
                - identifies operators
                - formats the line into a set of clauses for each subject, organized by operator logic

        - once you identify modifiers, identifying clauses is mostly a matter of identifying subjects and operators (and, because, ',')
        - check for verb tenses normally used in passive sentences # had been done = past perfect
        - translate questions into statements of intent: "would there be an effect of x on y?" intent = "evaluate x-y relationship" 
            where clauses include: ['subject verb relationship(s)', 'conditional(s)']
            and relationships include: ['subject verb relationship(s)', 'subject verb relationship(s) conditional(s)']
    '''
    no_punctuation_line = row['line']
    for cd in [',', ':', ';', '(', ')']:
        if cd in no_punctuation_line:
            no_punctuation_line = no_punctuation_line.replace(cd, '***')
    clauses_by_punctuation = no_punctuation_line.split('***')
    print('clauses_by_punctuation', clauses_by_punctuation)
    operator_clauses = {}
    for oc in clauses_by_punctuation:
        operator_clause = []
        for w in oc.replace('  ', ' ').split(' '):
            for k, values in all_vars['clause_map'].items():
                if w in values:
                    operator_clause.append(k)
                else:
                    operator_clause.append(w)
        if len(operator_clause) > 0:
            new_clause = ' '.join(operator_clause)
            operator_clauses[new_clause] = oc
    print('operator_clauses', operator_clauses)
    all_subjects = []
    if operator_clauses:
        row['clause'] = operator_clauses
        for operator_clause, original_clause in operator_clauses.items():
            cmap = {
                'conditional': [],
                'subject': [],
                'statement': [], # contains verb + rest of predicate
                'delimiter': [],
                'operator_conditional': [],
                'operator_subject': [],
                'operator_statement': [],
                'operator_delimiter': []
            }
            print('parsing original clause', original_clause)
            operator_clause_words = operator_clause.split(' ')
            original_clause_words = original_clause.split(' ')
            verb_index = 0
            for i, w in enumerate(original_clause_words):
                if verb_index == 0:
                    if w not in all_subjects:
                        cmap['subject'].append(w)
                        all_subjects.append(w) # make sure subjects are not repeated across clause entries
                    cmap['operator_subject'].append(operator_clause_words[i])
                if v in row['verb']: # hit the verb, exit
                    verb_index = i
                    cmap['statement'] = original_clause_words[i:]
                    cmap['operator_statement'] = operator_clause_words[i:]
                elif w in all_vars['clause_delimiters']:
                    cmap['delimiter'].append(w)
                    cmap['operator_delimiter'].append(operator_clause_words[i])
            print('condition map', cmap)
            cmap['conditional'] = original_clause.replace(cmap['subject'], '')
            cmap['conditional'] = cmap['conditional'].replace(cmap['statement'], '')
            cmap['operator_conditional'] = original_clause.replace(cmap['operator_subject'], '')
            cmap['operator_conditional'] = cmap['operator_conditional'].replace(cmap['operator_statement'], '')
            print('conditional', cmap['conditional'])
            print('operator conditional', cmap['operator_conditional'])
            new_condition = []
            for i, w in enumerate(conditional.split(' ')):
                if w in cmap['delimiter']:
                    operator = operator_conditional.split(' ')[i]
                    new_condition.append(operator)
                else:
                    new_condition.append(w)
            new_condition_clause = ' '.join(new_condition)
            print('conditional with operator delimiters', new_condition_clause)
            cmap['conditional'] = new_condition_clause
            row['condition'] = cmap
        print('\nclause', row['clause'])
        print('\ncondition', row['condition'])

    ''' now assign condition type '''
    # the process was activated because x was signaling successfully
    # x successful signals activated the process
    # should replace independence operators with 'with' because the next clause is true regardless but retain not ! operator
    passive_operators = ['%'] # the next clause after the passive operators should precede the previous clause
    general_operators = ['&', '|', '^'] # and, or, but can be conditional delimiters or statement delimiters or part of a phrase
    conditional_operators = ['#'] #['when', 'even', 'despite', 'because']
    verb_operators = ['=', '+', '-', '~', '>', '@', '<']
    clause_types = ['condition', 'statement', 'question']
    ''' first determine what type of clause this is out of clause_types '''
    new_conditions = []
    for conditional in row['condition']:
        for key in ['operator_statement', 'operator_conditional']:
            if len(conditional[key]) > 0:
                verb_operator_count = 0
                for v in verb_operators:
                    if v in conditional[key]:
                        verb_operator_count = 0
                if verb_operator_count > 0 and len(conditional['subject']) > 0:
                    ''' probably a statement unless:
                        - the verb is part of a verb phrase like 'even with alkalizing process'
                        - it has definitive condition keywords 
                    '''
                    for w in conditional_operators:
                        if w in conditional[key]:
                            ''' found a definitive condition keyword '''
                            conditional['type'] = 'condition'
                    if 'type' not in conditional:
                        conditional['type'] = 'statement'
                else:
                    for w in conditional_operators:
                        if w in conditional[key]:
                            ''' found a definitive condition keyword '''
                            conditional['type'] = 'condition'
        new_conditions.append(conditional)
    if len(new_conditions) > 0:
        row['condition'] = new_conditions
    print('\nfinal row', row)
    return row
    
def get_object_by_position(index, sentence_pieces, position, check_list, phrases):
    relevant_piece = sentence_pieces[index - 1] if position == 'prev' else sentence_pieces[index + 1] if index < (len(sentence_pieces) - 1) else ''
    if relevant_piece != '':
        sequenced_words = relevant_piece.split(' ') if position == 'next' else relevant_piece.split(' ').reverse()
        for w in sequenced_words:
            phrase_string = ' '.join(phrases)
            if w in phrase_string:
                for phrase in phrases:
                    for i, phrase_word in enumerate(phrase.split(' ')):
                        if phrase_word == w and i == 0:
                            ''' this is the first word in a phrase so get the whole phrase '''
                            return phrase
            elif w in check_list: # check that its in the check_list passed in before returning it
                return w
    return False

def order_and_convert_clauses(row, line, all_vars):
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
            row['condition'] = [
                {
                    "subject": "x",
                    "statement": "is y",
                    "delimiter": "even when",
                    "conditional": "z",
                    "operator_subject": "x",
                    "operator_statement": "= y",
                    "operator_delimiter": "# &",
                    "operator_conditional": "z"
                }
            ]
        - this function should conduct ordering operations:
            - 'non-verb clause, verb_clause' => 'verb_clause non-verb clause' => 'if x then y' => 'y if x'
            - 'subject1 verb clause because subject2 verb clause' => 'subject2 verb-to-noun causes subject1 verb-to-noun'
            - 'the process activated x because y inhibits b' => 'y b-inhibition causes the process to activate x' => 'y b-inhibition enables process to activate x'
        clause_map = {
            '-': ["decrease"], # attacks
            '+': ["increase"], # helps
            '=': ['is', 'like', 'equate', 'equal', 'describe', 'indicate', 'delineate', 'same', 'like', 'similar', 'implies', 'signifies', 'means'],
            '&': ['and', 'with'], # union
            '|': ['or'], # alternative
            '^': ['but', 'yet', 'but yet', 'but rather', 'but actually', 'still', 'without', 'however', 'nevertheless', 'in the absence of', 'lacking'], # exception
            '%': ['because', 'since', 'if', 'so', 'as', 'then', 'from', 'due', 'when', 'while', 'during', 'for', 'given'], # dependence/contextual/subset
            '#': ['even', 'still', 'despite', 'otherwise', 'in spite of', 'regardless', 'heedless', 'irrespective'] # independence
            '!': ['not'],
            '~': ['functions', 'that'],
            '>': ['creates', 'becomes', 'changes into', 'transforms', 'produces', 'leads to', 'converts into'],
            '@': ['changes', 'impacts', 'influences', 'adjusts', 'modulates', 'modifies', 'alters', 'affects'],
            '<': ['subset'], #'x is a subset of y'
            '!@': ['does not change'] # to do: add all combination operators
        }
    }
    '''
    statement_count = 0
    condition_count = 0
    for clause in row['condition']:
        clause_type = clause['type']
        if clause['type'] == 'statement':
            statement_count += 1
        else:
            condition_count += 1
    ordered_clauses = []
    if condition_count == 0:
        ''' no conditional clauses found, only passive or general operators separating statements '''
        ''' to do: rearrange if separating operator is the dependence operator '''
        for clause in row['condition']:
            if clause['type'] == 'statement':
                for s in clause['statement']:
                    full_statement = ' '.join([clause['subject'], s])
                    ordered_clauses.append(full_statement)
    else:
        ''' make sure statements precede conditions '''
        for clause in row['condition']:
            if clause['type'] == 'statement':
                for s in clause['statement']:
                    full_statement = ' '.join([clause['subject'], s])
                    ordered_clauses.append(full_statement)
        for clause in row['condition']:
            if clause['type'] == 'condition':
                ordered_clauses.extend(clause['conditional'])
    print('ordered clauses', ordered_clauses)
    clauses = filter_clauses(ordered_clauses, all_vars)
    return clauses

def filter_clauses(clauses, all_vars):
    ''' removes meaningless clauses '''
    return clauses

def convert_to_operators(original_clause, all_vars):
    ''' check for synonym first: 'reduced' has polarity 0.0 '''
    operator_clause = []
    for word in original_clause.split(' '):
        operator = get_operator(word, all_vars)
        if operator:
            operator_clause.append(operator)
        elif word in all_vars['supported_synonyms']:
            common_verb = all_vars['supported_synonyms'][word]
            operator = get_operator(common_verb, all_vars)
            if operator:
                operator_clause.append(operator)
        else:
            operator_clause.append(word)
    if len(operator_clause) > 0:
        operator_string = ' '.join(operator_clause)
        return operator_string
    return False

def get_combined_operator(combined):
    for key, val in all_vars['combined_map'].items():
        if combined in val:
            return key
    return False

def operator_count(line, operators):
    line_list = line.split(' ') if type(line) == str else line
    total = 0
    for i in line_list:
         for o in operators:
            total += i.count(o)
    return total

def has_operator(line):
    if '+' in line and '-' in line and '=' in line:
        return True
    return False

def split_by_operators(clause):
    ''' ideally we'd only have one operator per clause at this point & suboperators are stored in variables
    '''
    clause_split = []
    relation = set()
    for c in clause.split(' '):
        if c in ['+', '-', '=']:
            clause_split.append(relation)
            clause_split.append(c)
            relation = set()
        else:
            relation.add(c)
    if len(relation) > 0:
        clause_split.append(relation)
    if len(clause_split) > 0:
        return clause_split
    return False
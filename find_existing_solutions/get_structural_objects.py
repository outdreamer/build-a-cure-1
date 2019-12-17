import random
from utils import *
from get_synonyms import *
from get_vars import get_new_key

def find_relationship(row, all_vars):

    '''
        now you can generate the relationships based on operator logic stored in our row['clauses']: 
            '(x = y) # a': [
            '(x = y) # a',
            '(x = y) # a',
            'a (x = y) # a'
        ]
        get_relationships('(x = y) # a') = [
            'x is y',
            'x is y even with a',
            'a cannot prevent (x is y)'
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
    '''
    operator_clauses = {}
    '''
        operator_clauses is original clauses with operators instead of verbs & variable names instead of sub-clauses: ["x - a"]
        so it can do substitutions and derive the alternate relationships in get_combined_relationships()
    '''
    variables = {}
    ''' variables should be a dict like: { var : modifier relationship }  ("a": "i - b") '''
    citems = get_conditionals(row, all_vars)
    variables['subject'] = citems['subject']
    word_relationships = []
    for v, verb_clause in enumerate(citems['verb_relationship']):
        ''' for each verb_relationship r, join it with the subject & each conditional & add the combined version '''
        operator_verb_clause = convert_to_operators(verb_clause, all_vars)
        new_clause = ' '.join([variables['subject'], operator_verb_clause])
        operator_clauses[new_clause] = verb_clause
        word_relationships.append(' '.join([variables['subject'], verb_clause]))
        for c, condition_clause in enumerate(citems['conditional']):
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
        relationships = get_combined_relationships(placeholder_clauses, citems, variables, all_vars)
        if relationships:
            return relationships
    return False

def replace_with_placeholders(operator_clause, variables, all_vars):
    ''' what differentiates a variable from a normal word? 
        variables are used to refer to components of sub-logic that include 
        an embedded relationship which must be handled associatively 
        so that x - (a - b) ends up as two relationships: x - a and x + b

        right now this just supports identifying basic units of sub-logic such as:
        - modifiers, like "enzyme analyzer"
        - conditional clauses
    '''
    ''' 
    this is step 2 in the below workflow:
    - in order to preserve order of operations:
        1. first converting "b inhibitor" to:
            { new_key: modifier_relationship } = {"a": "(i - b)"}
        2. then converting "x - (i - b)" to "x - a" and storing in placeholder_clauses
        3. then converting "x - a" to permuted relationship set:
            "x - i" and "x + b"
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
        1. first converting "b inhibitor" to:
            { new_key: modifier_relationship } = {"a": "i - b"}
        2. then converting "x - (i - b)" to "x - a" and storing in placeholder_clauses
        3. then converting "x - a" to permuted relationship set: "x - i" and "x + b"
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
    ''' this function should split the line by det and prep
        include splitting by parenthesis & clause delimiters 

        - clauses are relationships between subject and objects in line

        - this function:
            1. separates the line by subjects
                1. identifies operators
                2. formats the line into a set of clauses for each subject, organized by operator logic
                3. deconstructs the sentence based on operator logic so its represented by order of operations
                    - applies operator logic to clauses to produce alternative relationships:
                        - "x was b even with a" means a is irrelevant, so => relationships ["x was b", "a does not impact (x was b)"]
                        - "x was a and was b" should produce => clause "x was (a and b)", relationship ["x was a", "x was b"], variable "(a and b)"
                        - "x was a and therefore b" => clause "x was a so b", relationship ["a therefore b", "x leads to b"], variable "(a so b)"
                        - "N V even with x or y" should produce: ["N V even with x", "N V even with y", "N V even with x or y"]

        - once you identify modifiers, identifying clauses is mostly a matter of identifying subjects and operators (and, because, ',')

        to do:
            - call after order_and_convert_clauses() so position is: 'subject verb relationship conditional' rather than handling multiple subjects
            where clauses include:
                'subject verb relationship(s)'
                'conditional(s)'
            and relationships include:
                'subject verb relationship(s)'
                'subject verb relationship(s) conditional(s)'
    '''
    sentence_pieces = [] # break up sentence by verbs
    sentence_piece = []
    for w in row['line'].split(' '): 
        if len(w) > 0:
            if '(' in w:
                sentence_pieces.append(' '.join(sentence_piece))
                sentence_piece = [w.replace('(', '')]
            elif ')' in w:
                sentence_piece.append(w.replace(')', ''))
                sentence_pieces.append(' '.join(sentence_piece))
                sentence_piece = []
            elif w not in row['verb']:
                sentence_piece.append(w)
            else:
                sentence_pieces.append(' '.join(sentence_piece))
                sentence_pieces.append(w) # add the verb separately
                sentence_piece = []
    for j, s in enumerate(sentence_pieces):
        s_split = s.split(' ') if type(s) == str else s
        for i, word in enumerate(s_split):
            if word in row['verb']:
                prev_object = False if i < 1 else get_object_by_position(i, s_split, 'prev', row['noun'], row['phrase'])
                prev_object = sentence_pieces[j - 1] if prev_object is False and j > 0 else prev_object
                next_object = False if i == (len(sentence_pieces) - 1) else get_object_by_position(i, s_split, 'next', row['noun'], row['phrase'])
                next_object = sentence_pieces[j + 1] if next_object is False and j < (len(sentence_pieces) - 1) else next_object
                if active:
                    if prev_object:
                        row['subject'].add(prev_object)
                        if next_object:
                            row['clause'].add(' '.join([prev_object, word, next_object]))
                else:
                    # to do: handle other cases where infinitive is linguistically awkward bc clauses will be re-used later
                    if next_object:
                        row['subject'].add(next_object)
                        if prev_object:
                            row['clause'].add(' '.join([next_object, word, prev_object]))
    print('\nclause', row['clause'])
    row['conditional'] = []
    row['subject'] = []
    row['verb_relationship'] = []
    row['delimiter'] = []
    all_vars['clause_delimiters'].append('1')
    for i, c in enumerate(row['clause']):
        c_strip = c.strip()
        if i == 0:
            row['subject'] = c_strip
        else:
            words = c_strip.split(' ')
            is_a_condition = is_condition(words, row, all_vars)
            if is_a_condition:
                ''' is_a_condition has the next important word in condition '''
                pos = row['word_map'][is_a_condition] if is_a_condition in row['word_map'] else ''
                if pos:
                    if pos not in all_vars['pos_tags']['ALL_V']:
                        for j, w in enumerate(words):
                            if w in all_vars['clause_delimiters']:
                                row['delimiter'].append(w)
                                remainder = ' '.join([x for x in words if words.index(x) >= j])
                                if w == words[-1]:
                                    ''' the delimiter is the last word in this clause '''
                                    remainder = ' '.join([x for x in words if words.index(x) < j])
                                if remainder not in row['conditional']:
                                    row['conditional'].append(remainder)
                            else:
                                if c_strip not in row['conditional']:
                                    row['conditional'].append(c_strip)
                    else:
                        for w in words:
                            if w in all_vars['clause_delimiters']:
                                row['delimiter'].append(w)
                                words.remove(w)
                        if c_strip not in  row['verb_relationship']:
                            row['verb_relationship'].append(c_strip)
            else:
                if c_strip not in row['conditional']:
                    row['conditional'].append(c_strip)
    ''' at this point row represents a sentence broken into: 
        row = {
            "subject": "x",
            "verb_relationships": "is y",
            "delimiter": "even when",
            "condition": "z"
        }
    '''
    print('\nconditional', row)
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
        isolate clauses having embedded relationships with parenthesis: (if clause contains verb or verb-modifier) => '(x was y) even with a'
        we would store multiple patterns for the independence relationship, 
        because a is an object and would therefore be a subject (acting agent) in some relationships, 
        so we want to index that too, even though it seems like a duplicate
        if a is a treatment, we definitely want the relationship:
            "treatment a cannot prevent symptom x from being symptom y"
            indexed with treatment a as the subject
    '''
    ''' filter_clauses removes clauses that dont change the output impact of the sentence '''

    ''' arranges clauses according to operators
        line = 'x was y even with a' => 
        separate by clause_delimiters: ['x was y', 'even with', 'a']
        replace with clause_map operators: '(x equal y) independent a'
        replace with symbolic operators: '(x = y) # a'

        converts "in the event of onset, symptoms appear at light speed, even if you take vitamin c at the max dose" =>
            "you take" => "" # it's implied that a patient will be taking the medicine so it doesnt need to be stated
            "vitamin c at the max dose" => modifier pattern "max dose vitamin c"
    '''
    clauses = filter_clauses(clauses, all_vars)
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
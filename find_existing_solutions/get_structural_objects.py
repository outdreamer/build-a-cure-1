import random
from utils import *

def get_relationships_from_clauses(clauses, line, nouns, all_vars):
    '''
    this function is to catch all the meaning in clauses like: 
        "x reduced b inhibitor" => "x - (i - b)"
    and your current logic will only capture: 
        "x reduced b"
    when in reality youd want to store the full clause so the relationships can be derived:
        "x increases b" => "x + b"
        "x reduces inhibitor" => "x - i"
        "inhibitor reduces b" => "i - b"
    so use get_modifiers to find the modifying words like inhibitor and apply them to the verb 
    to get the final version of the relationship

    to do: 
     - you need an operator for clause delimiters
     - add more advanced analysis for linguistic patterns of symptoms 
        'fever that gets worse when x', or 'x reduced y and diminished z even in condition x or condition a', 
        which should have condition x added to the previous relationships
     - add this pattern to clause processing "x is y and is b" => x should be related to y and b
            NAA to Cr ratio 
                is reduced in HIV positive patients and
                is a marker for HIV infection of the brain 
                    even in the absence of imaging findings of HIV encephalopathy 
                    or when the patient is symptomatic due to neurological disease of other etiologies.
    '''
    operator_clauses = {}
    '''
        operator_clauses should be the original clauses but with operators instead of verbs
        and with variable names instead of modifier relationships:
        ["x - a"]
        so it can do substitutions and derive the alternate relationships in extract_combined_relationships()
    '''
    variables = {}
    '''
        variables should be a dict like: 
        { var : modifier relationship }:
        "a": "(i - b)"
    '''
    print('line', line)
    citems = get_conditionals(line, nouns, clauses)
    '''
        these two verb-initiated relationships
        'is reduced in HIV positive patients',
        'is a marker for HIV infection of the brain',
        should preface each conditional relationship right after the subject
    '''
    variables['subject'] = citems['subject']
    word_relationships = set()
    operator_relationships = set()
    ''' to do: assume this can be nested, to contain other dicts of embedded relationships '''
    for operand, original_clause in citems['conditional'].items():   
        print('operand', operand) 
        print('original_clause', original_clause)        
        if original_clause in citems['verb_relationships']:
            ''' for each verb_relationship r, join it with the subject & add to subject_full_relationships '''
            operator_clause = convert_to_operators(original_clause, all_vars)
            if operator_clause:
                new_operator_clause = ' '.join(['subject', operator_clause])
                operator_clauses[new_operator_clause] = original_clause
                operator_relationships.add(new_operator_clause)
                word_relationship = ' '.join([variables['subject'], original_clause])
                word_relationships.add(word_relationship)
            for operand, clause in citems['conditional'].items():
                if clause not in citems['verb_relationships']:
                    ''' for each verb_relationship r, join it with each conditional relationship clause & add to operator_relationships '''
                    sub_operator_clause = convert_to_operators(clause, all_vars)
                    if sub_operator_clause:
                        word_relationships.add(clause)
                        operator_relationships.add(sub_operator_clause)
                        operator_clauses[sub_operator_clause] = clause
                        joined_word_relationship = ' '.join([word_relationship, clause])
                        word_relationships.add(joined_word_relationship)
                        joined_operator_clause = ' '.join([new_operator_clause, sub_operator_clause])
                        operator_relationships.add(joined_operator_clause)
                        operator_clauses[joined_operator_clause] = joined_word_relationship

    print('\nword_relationships', word_relationships)
    print('\noperator_relationships', operator_relationships)
    print('\noperator_clauses', operator_clauses.keys())
    placeholder_clauses = []
    for operator_clause in operator_clauses:
        placeholder_clause, variables = replace_with_placeholders(operator_clause, line, variables, all_vars)   
        placeholder_clauses.append(placeholder_clause)
    print('placeholders', placeholder_clauses)
    if len(placeholder_clauses) > 0:
        relationships_with_vars = extract_combined_relationships(placeholder_clauses, citems, variables, all_vars)
        if relationships_with_vars:
            print('relationships_with_vars', relationships_with_vars)
            return relationships_with_vars
    return False

def get_conditionals(line, nouns, clauses):
    ''' 
    this function assumes rearrange_sentence was already called on line used to generate sentence_pieces 
    '''
    ''' to do:
        - you still need to deconstruct the sentence based on these dependencies 
            so its represented accurately according to order of operations
            example: 
                "even x or y" should be all one clause
                "x is a and b" or "x is a and is b" should be two clauses "x is a" and "x is b"
                "x is a or b" should be one clause
        - handle sentences with multiple subjects - actually it should already be organized by subject into separate lines            
    '''
    print('\nclauses', clauses)
    items = {'conditional': [], 'subject': '', 'verb_relationships': [], 'delimiters': []}
    all_vars['clause_delimiters'].append('1')
    for i, c in enumerate(clauses):
        c_strip = c.strip()
        if i == 0:
            items['subject'] = c_strip
        else:
            words = c_strip.split(' ')
            is_a_condition = is_condition(words, all_vars['clause_delimiters'])
            if is_a_condition:
                ''' is_a_condition has the next important word in condition '''
                if get_pos(is_a_condition) != 'verb':
                    for j, w in enumerate(words):
                        if w in all_vars['clause_delimiters']:
                            items['delimiters'].append(w)
                            remainder = ' '.join([x for x in words if words.index(x) > j])
                            if w == words[-1]:
                                ''' the delimiter is the last word in this clause '''
                                remainder = ' '.join([x for x in words if words.index(x) < j])
                            items['conditional'].append(remainder)
                        else:
                            items['conditional'].append(c_strip)
                else:
                    for w in words:
                        if w in all_vars['clause_delimiters']:
                            items['delimiters'].append(w)
                            words.remove(w)
                    items['verb_relationships'].append(c_strip)
            else:
                items['conditional'].append(c_strip) # last item without delimiter
    ''' at this point items represents a sentence broken into: 
        items = {
            "subject": "x",
            "verb_relationships": "is y",
            "delimiter": "even",
            "condition": "when z"
        }
    '''
    print('\nconditionals', items)
    return items

def replace_with_placeholders(operator_clause, line, variables, all_vars):
    ''' what differentiates a variable from a normal word? 
        variables are used to refer to components of sub-logic that include 
        an embedded relationship which must be handled associatively 
        so that x - (a - b) ends up as two relationships: x - a and x + b

        right now this just supports identifying basic units of sub-logic such as:
        - modifiers, like "enzyme extractor"
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
            words = word_set.split(' ')
            new_key = get_new_key(variables, all_vars)
            variables[new_key] = ' '.join(words) if len(words) > 0 else words[0]
            placeholder_clause.append(new_key)
        else:
            placeholder_clause.append(word_set)
    placeholder_string = delimiter.join(placeholder_clause)
    return placeholder_string, variables

def extract_combined_relationships(placeholder_clauses, conditional_items, variables, all_vars):
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
        new_relationship = process_placeholder(pc, conditional_items, variables, all_vars)
        if new_relationship:
            symbol_relationships.add(new_relationship)
    if len(symbol_relationships) > 0:
        return symbol_relationships
    return False

def process_placeholder(pc, conditional_items, variables, all_vars):
    operator_list = ['+', '-', '=']
    relationships = set()
    relationship = set()
    new_pc_words = []
    sub_relationship = []
    reverse_var_keys = reversed(sorted(variables.keys()))
    for k in reverse_var_keys:
        spaced_var = ''.join(['', variables[k], ''])
        pc = pc.replace(k, spaced_var)
        for o in operator_list:
            if o in pc:
                spaced_operator = ''.join([' ', all_vars['operator_map'][o], ' '])
                pc = pc.replace(o, spaced_operator)
    if pc:
        return pc
    return False

def split_by_delimiter(placeholder_string, all_vars):
    word_list = []
    word = []
    delimiters = []
    for char in placeholder_string:
        if char in all_vars['alphabet']:
            word.append(char)
        else:
            delimiters.append(char)
            word_string = ''.join(word)
            word_list.append(word_string)
            word = []
    if len(word) > 0:
        word_string = ''.join(word)
        word_list.append(word_string)
    return word_list, delimiters

def get_new_key(key_dict, all_vars):
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
        if new_key in key_dict:
            return get_new_key(key_dict, all_vars)
        else:
            return new_key
    return False 

def is_condition(asp_words, clause_delimiters):
    first_word = get_first_important_word(asp_words)
    if first_word:
        pos = get_pos(first_word)
        if pos:
            if pos != 'noun':
                return first_word
    for word in asp_words:
        if word in clause_delimiters:
            return word
    return False

def add_items(word_sets, cd, clause_delimiters):
    new_items = []
    for i, word_set in enumerate(word_sets):
        for w in word_set.split(' '):
            if len(w) > 0 and w not in clause_delimiters:
                new_items.append(w)
    return ' '.join(new_items)

def get_next_clause(delimiter, index, all_sentence_pieces):
    next_clause = None
    for i, clause in enumerate(all_sentence_pieces):
        if i == index and clause == delimiter:
            if i < (len(all_sentence_pieces) - 1):
                next_clause = all_sentence_pieces[i + 1]
                if len(next_clause.split(' ')) > 1:
                    return next_clause
                else:
                    new_index = index + 1
                    return get_next_clause(delimiter, new_index, all_sentence_pieces)
    return False

def convert_to_operators(original_clause, all_vars):
    operator_clause = []
    for word in original_clause.split(' '):
        operator = get_operator(word, all_vars)
        if operator:
            operator_clause.append(operator)
        else:
            operator_clause.append(word)
    if len(operator_clause) > 0:
        operator_string = ' '.join(operator_clause)
        operator_string = operator_string.replace('= = +', '+').replace('= = -', '-') # had been done
        operator_string = operator_string.replace('= +', '+').replace('= -', '-') # is reduced
        return operator_string
    return False

def get_combined_operator(combined):
    if combined in all_vars['combined_map']['negative']:
        return '-'
    elif combined in all_vars['combined_map']['positive']:
        return '+'
    elif combined in all_vars['combined_map']['equal']:
        return '='
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
    ''' ideally wed only have one operator per clause at this point 
        & suboperators are stored in variables so 
        split_by_operators shouldnt be necessary
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

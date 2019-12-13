import random
from utils import *
from get_synonyms import *
from get_objects import *

def get_relationships_from_clauses(row, all_vars):
    '''
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
    print('line', row['line'])
    citems = get_conditionals(row, all_vars)
    variables['subject'] = citems['subject']
    word_relationships = []
    for v, verb_clause in enumerate(citems['verb_relationships']):
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
    print('\nvariables', variables)
    print('\nword_relationships', word_relationships)
    print('\noperator_relationships', operator_relationships)
    print('\noperator_clauses', operator_clauses.keys())
    placeholder_clauses = []
    for operator_clause in operator_clauses:
        placeholder_clause, variables = replace_with_placeholders(operator_clause, variables, all_vars)   
        placeholder_clauses.append(placeholder_clause)
    print('\nplaceholders', placeholder_clauses)
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

def add_items(word_sets, cd, clause_delimiters):
    new_items = []
    for i, word_set in enumerate(word_sets):
        for w in word_set.split(' '):
            if len(w) > 0 and w not in clause_delimiters:
                new_items.append(w)
    return ' '.join(new_items)

def get_next_clause(delimiter, index, all_sentence_pieces):
    for i, clause in enumerate(all_sentence_pieces):
        if i == index and clause == delimiter:
            if (i + 1) < len(all_sentence_pieces):
                next_clause = all_sentence_pieces[i + 1]
                if len(next_clause) > 1:
                    return next_clause
                else:
                    new_index = index + 1
                    return get_next_clause(delimiter, new_index, all_sentence_pieces)
    return False

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

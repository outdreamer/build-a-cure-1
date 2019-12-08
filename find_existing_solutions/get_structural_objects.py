import random
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

from get_structure import get_pos 
from utils import *

def get_first_non_stopword(words):
    for word in words:
        pos = get_pos(word)
        if pos == 'verb' or word not in stop:
            return word
    return False

def get_conditionals(line, nouns, clauses):
    ''' 
    this function assumes rearrange_sentence
    was already called on line used to generate sentence_pieces 
    '''

    ''' in the following sentence:
    NAA to Cr ratio 
        is reduced in HIV positive patients and
        is a marker for HIV infection of the brain 
            even in the absence of imaging findings of HIV encephalopathy 
            or when the patient is symptomatic due to neurological disease of other etiologies.
    this function would return the last two items 
    '''

    '''
        to do: you still need to deconstruct the sentence based on these dependencies 
        so its represented accurately according to order of operations
        example: 
        "even x or y" should be all one clause
        "x is a and b" or "x is a and is b" should be two clauses "x is a" and "x is b"
        "x is a or b" should be one clause 
    '''
    ''' to do: implement multi-delimiter logic '''

    print('\nclauses', clauses)
    secondary_delimiters = ['when', 'without']
    clause_delimiters = ['and', 'or', 'because', 'but', 'as', 'if', 'then', 'even', 'without']
    # conditional is a list bc it needs to preserve order
    items = {'conditional': {'first': ''}, 'subject': '', 'verb_relationships': set(), 'delimiters': []}
    ''' to do: handle sentences with duplicate delimiters '''
    for i, c in enumerate(clauses):
        c_strip = c.strip()
        if i == 0:
            items['subject'] = c_strip
        else:
            words = c_strip.split(' ')
            current_delimiter = 'first'
            items['delimiters'].append(current_delimiter)
            is_condition = check_is_condition(words, clause_delimiters)
            if is_condition:
                print('is_condition', is_condition, get_pos(is_condition))
                is_not_verb = True if get_pos(is_condition) != 'verb' else False
                current_delimiter = is_condition if is_not_verb else current_delimiter       
                if is_not_verb and current_delimiter in clause_delimiters:
                    if current_delimiter not in items['conditional']:
                        items['conditional'][current_delimiter] = ''
                    for j, w in enumerate(words):
                        if w in clause_delimiters:
                            current_delimiter = w
                            print('updated current_delimiter', current_delimiter)
                            items['delimiters'].append(current_delimiter)
                            remainder = ' '.join([w for w in words if words.index(w) > j])
                            if is_condition == words[-1]:
                                ''' the delimiter is the last word in this clause '''
                                remainder = ' '.join([w for w in words if words.index(w) < j])
                            items['conditional'][current_delimiter] = remainder
                else:
                    word_string = ' '.join(words)
                    for w in words:
                        if w in clause_delimiters:
                            current_delimiter = w
                            items['delimiters'].append(current_delimiter)
                            words.remove(current_delimiter)
                            word_string = ' '.join(words)
                            print('cd', current_delimiter, 'ws', word_string)
                            if word_string != current_delimiter:
                                items['conditional'][current_delimiter] = word_string
                    if c not in items['conditional'][current_delimiter]:
                        items['conditional'][current_delimiter] = word_string
                    items['verb_relationships'].add(word_string)  
    print('\nconditionals', items)
    ''' at this point items represents a sentence broken into:
    - subject "x"
    - verb_relationships "is y"
    - delimiter "even"
    - condition "when z"
    '''
    return items

def check_is_condition(asp_words, clause_delimiters):
    first_word = get_first_non_stopword(asp_words)
    if first_word:
        pos = get_pos(first_word)
        if pos:
            if pos != 'noun':
                return first_word
    for word in asp_words:
        if word in clause_delimiters:
            return word
    return False

def add_items(phrases, cd, clause_delimiters):
    new_items = []
    for i, phrase in enumerate(phrases):
        for w in phrase.split(' '):
            stripped_item = w.strip()
            if len(stripped_item) > 0 and stripped_item not in clause_delimiters:
                new_items.append(stripped_item)
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

def get_relationships_from_clauses(clauses, line, nouns, all_vars):
    '''
    this function is to catch all the meaning in phrases like: 
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

def extract_combined_relationships(placeholder_clauses, conditional_items, variables, all_vars):
    '''
    this is step 3 in the below workflow:
    - in order to preserve order of operations:
        1. first converting "b inhibitor" to:
            { new_key: modifier_relationship } = {"a": "i - b"}
        2. then converting "x - (i - b)" to "x - a" and storing in placeholder_clauses
        3. then converting "x - a" to permuted relationship set:
            "x - i" and "x + b"
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

def get_combined_operator(combined):
    if combined in all_vars['combined_map']['negative']:
        return '-'
    elif combined in all_vars['combined_map']['positive']:
        return '+'
    elif combined in all_vars['combined_map']['equal']:
        return '='
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
    for i, phrase in enumerate(operator_clause.split(delimiter)):
        phrase = phrase.strip()
        if phrase not in ['+', '-', '=', 'subject']:
            words = phrase.split(' ')
            new_key = get_new_key(variables, all_vars)
            variables[new_key] = ' '.join(words) if len(words) > 0 else words[0]
            print('added var', new_key, variables[new_key])
            placeholder_clause.append(new_key)
            '''
            to do: finish get_modifier logic
            for j, word in enumerate(words):
                prev_word = words[j - 1] if j > 0 else False
                next_word = words[j + 1] if j < (len(words) - 1) else False
                is_modifier = get_modifier(prev_word, word, next_word)
                if is_modifier:
                    modified_word = get_modified_word(line, word)
                    if modified_word:
                        variables[new_key] = [word, 'of', modified_word]
                        placeholder_clause.append(new_key)
                else:
                    variables[new_key] = word
                    placeholder_clause.append(new_key)
            '''
        else:
            placeholder_clause.append(phrase)
    placeholder_string = delimiter.join(placeholder_clause)
    return placeholder_string, variables

def get_modifier(prev_word, word, next_word):
    ''' if this is a modifier, return True 
    - the reason we're isolating modifiers is because theyre embedded relationships 
    so in order to process them correctly, we have to extract them 
    & format them the same as other relationships 
    - then we can do more straightforward calculations with the operator_clause 
    & generate the full set of relationships in the original clause
    - we can easily identify modifiers that are in supported_synonyms 
    but for others we need standard pos patterns

    to do:
        - use prev_word & next_word in get_modifier
    '''
    modifier_score = 0
    modifier_substrings = [
        "or",
        "er",
    ]
    modifier_patterns = [
        'noun-noun', # the second noun has a verb root, ie "enzyme inhibitor"
        'noun noun', 
    ]
    word_pos = get_pos(word)
    stem_pos = get_pos(stemmer.stem(word))
    if stem_pos in ['VBP', 'VBD', 'VBN', 'VBZ', 'VBG'] and modifier_pos in ['NN', 'JJ', 'JJR', 'NNS', 'NNP', 'NNPS', 'RB']:
        modifier_score += 1
    for m in modifier_substrings:
        if m in word:
            index = len(word) - len(m) - 1
            if word[index:] == m:
                modifier_score += 1
    for pattern in modifier_patterns:
        if word_pos:
            found = find_pattern(word, word_pos, pattern)
            if found:
                modifier_score += 1
    if modifier_score > 3:
        return True
    return False

def get_modified_word(operator_clause, nouns, modifier):
    ''' to do: this will fail if you removed the modified word or put it in the next clause '''
    print('get_modified_word: operator_clause', operator_clause, 'modifier', modifier)
    split_clause = operator_clause.strip().split(modifier)
    if len(split_clause) > 1:
        prev_word = split_clause[0].split(' ')[-1]
        next_word = split_clause[1].split(' ')[0]
        print('previous', prev_word, 'next', next_word)
        prev_pos = get_pos(prev_word) if prev_word not in ['+', '-', '='] else ''
        next_pos = get_pos(next_word) if next_word not in ['+', '-', '='] else ''
        if prev_pos == 'noun':
            return prev_word
        elif next_pos == 'noun':
            return next_word
        else:
            ''' apply same logic but get next object & previous object '''
    return False

def get_operator(verb, all_vars):
    ''' this is to map a verb to an operator like +, -, =
    to simplify sentence sentiment analysis 
    right now we're just supporting positive, negative, or equal 
    to do: 
    - implement positive/negative prefix/suffix checking, like 'dis-' is often a negative prefix
    '''
    pos = get_pos(verb)
    if pos == 'verb':
        stem = stemmer.stem(verb)
        polarity = get_polarity(verb)
        # print('get_operator: polarity', polarity, pos, stem, verb)
        if verb in all_vars['synonym_list']['negative'].keys() or stem in all_vars['synonym_list']['negative'].values() or polarity < 0.0:
            return '-'
        elif verb in all_vars['synonym_list']['positive'].keys() or stem in all_vars['synonym_list']['positive'].values() or polarity > 0.0:
            return '+'
        elif verb in all_vars['synonym_list']['equal'].keys() or stem in all_vars['synonym_list']['equal'].values(): # to do: assess equal word polarity 
            return '='
    return False

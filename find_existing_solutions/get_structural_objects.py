import random
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

from get_patterns import *
from get_structure import get_pos 
from utils import *

def get_first_non_stopword(words):
    for word in words:
        pos = get_pos(word)
        if pos == 'verb' or word not in stop:
            return word
    return False

def get_replacement_synonym(word):
    '''
    'as' can mean:    
        'like': 'as is common in that area',
        'because': 'as',
        'when': 'as the sun sets'
    '''
    synonym_sets = {
        'and': ['with'], # conditional
        'when': ['while', 'during'], # conditional
        'or': [], # alternative
        'but': ['however', 'yet'], # exception
        'because': ['since', 'respective', 'respectively', 'due'], # dependency
        'even': ['despite', 'in spite of', 'regardless of', 'heedless of', 'irrespective of'], # independence
        'is': [
            "equate",
            "equal",
            "describe",
            "indicate",
            "delineate",
            "same",
            "like",
            "similar to",
            "similar",
            "imply",
            "signify",
            "means"
        ] # similarity
    }
    for standard, synonyms in synonym_sets.items():
        if word in synonyms:
            return standard
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
    new_clauses = []
    for c in clauses:
        words = c.split(' ')
        new_words = []
        for w in words:
            synonym = get_replacement_synonym(w)
            if synonym:
                new_words.append(synonym)
            else:
                new_words.append(w)
        new_clause = ' '.join(new_words)
        new_clauses.append(new_clause)
    clauses = set(new_clauses)
    clause_delimiters = ['and', 'or', 'because', 'but', 'as', 'if', 'then', 'when', 'even', 'without'] #'is',
    '''
        to do: you still need to deconstruct the sentence based on these dependencies 
        so its represented accurately according to order of operations
        example: 
        "even x or y" should be all one clause
        "x is a and b" or "x is a and is b" should be two clauses "x is a" and "x is b"
        "x is a or b" should be one clause 
    '''
    all_sentence_pieces = []
    conditional_pieces = []
    items = {'conditional': [], 'other': []}
    for c in clauses:
        words = c.split(' ')
        clause_found = False
        for cd in clause_delimiters:
            if cd in words: # should check if cd == words[0] and leave in delimiter
                if not clause_found:
                    clause_found = True
                    if cd == words[0]:
                        conditional_pieces.append(cd)
                    new_items = add_items(c.split(cd), cd, clause_delimiters)
                    conditional_pieces.extend(new_items)
                    if cd != words[0]:
                        conditional_pieces.append(cd)
        if not clause_found:
            is_condition = check_is_condition(words, clause_delimiters)
            if is_condition:
                conditional_pieces.append(c)
            else:
                all_sentence_pieces = [c.strip()]
    for cp in conditional_pieces:
        all_sentence_pieces.append(cp)
    for i, asp in enumerate(all_sentence_pieces):
        if i > 0:
            asp_words = asp.split(' ')
            if len(asp_words) == 1:
                ''' this is a delimiter, get the next phrase '''
                next_clause = get_next_clause(asp, i, all_sentence_pieces)
                if next_clause:
                    items['conditional'].append(' '.join([asp, next_clause]))
                else:
                    items['conditional'].append(asp)
            else:
                is_condition = check_is_condition(asp_words, clause_delimiters)
                if is_condition:
                    items['conditional'].append(asp)
        else:
            items['other'].append(asp)
    print('conditionals', items)
    return items

def check_is_condition(asp_words, clause_delimiters):
    first_word = get_first_non_stopword(asp_words)
    if first_word:
        pos = get_pos(first_word)
        if pos:
            if pos != 'noun' or first_word in clause_delimiters:
                return True
    return False

def add_items(words, cd, clause_delimiters):
    new_items = []
    for i, item in enumerate(words):
        stripped_item = item.strip()
        if len(stripped_item) > 0 and stripped_item not in clause_delimiters:
            new_items.append(stripped_item)
    return new_items

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
    conditional_items = get_conditionals(line, nouns, clauses)
    ''' process non-conditionals first '''
    for item_type in ['other', 'conditional']:
        for original_clause in conditional_items[item_type]:
            operator_clause = []
            for word in original_clause.split(' '):
                if word not in nouns:
                    operator = get_operator(word, all_vars)
                    if operator:
                        operator_clause.append(operator)
                else:
                    operator_clause.append(word)
            operator_clause = ' '.join(operator_clause)
            operator_clauses[operator_clause] = original_clause
        print('operator_clauses', operator_clauses)
    operator_sentence = ' '.join(operator_clauses.keys())
    print('operator sentence', operator_sentence)
    placeholder_clauses = []
    for operator_clause in operator_clauses:
        placeholder_clause, variables = replace_with_placeholders(operator_clause, operator_sentence, line, variables, all_vars)   
        placeholder_clauses.append(placeholder_clause)
    print('placeholders', placeholder_clauses)
    relationships_with_vars = extract_combined_relationships(placeholder_clauses, conditional_items, operator_sentence, variables, all_vars)
    if relationships_with_vars:
        relationships_with_values = replace_with_values(relationships_with_vars, variables, all_vars)
        if relationships_with_values:
            print('relationships_with_values', relationships_with_values)
            return relationships_with_values
    return False

def replace_with_values(relationships_with_vars, variables, all_vars):
    ''' 
    this is step 5 in the below workflow:
    - in order to preserve order of operations:
        1. first converting "b inhibitor" to:
            { new_key: modifier_relationship } = {"a": "(i - b)"}
        2. then converting "x - (i - b)" to "x - a" and storing in placeholder_clauses
        3. then converting "x - a" to permuted relationship set:
            "x - i" and "x + b"
        4. conditionals should be applied last
        5. then the symbolic relationships can be replaced with original values:
            "x reduces inhibitor" and "x increases b"
    '''
    relationships_with_values = set()
    for r in relationships_with_vars:
        new_words = []
        words = r.split(' ')
        for w in words:
            if w in variables:
                new_words.append(variables[w])
            elif w in all_vars['operator_map']:
                new_words.append(all_vars['operator_map'][w])
            else:
                new_words.append(w)
        relationships_with_values.add(' '.join(new_words))
    return relationships_with_values

def extract_combined_relationships(placeholder_clauses, conditional_items, operator_sentence, variables, all_vars):
    '''
    this is step 3 in the below workflow:
    - in order to preserve order of operations:
        1. first converting "b inhibitor" to:
            { new_key: modifier_relationship } = {"a": "i - b"}
        2. then converting "x - (i - b)" to "x - a" and storing in placeholder_clauses
        3. then converting "x - a" to permuted relationship set:
            "x - i" and "x + b"
        4. conditionals should be applied last
        5. then the symbolic relationships can be replaced with original values:
            "x reduces inhibitor" and "x increases b"
    '''
    subject = None
    operator = None
    symbol_relationships = set()
    for pc in placeholder_clauses:
        new_relationships = process_placeholder(pc, conditional_items, variables, all_vars)
        if new_relationships:
            for r in new_relationships:
                symbol_relationships.add(r)
    if len(symbol_relationships) > 0:
        return symbol_relationships
    return False

def process_placeholder(pc, conditional_items, variables, all_vars):
    relationships = []
    if pc not in conditional_items['conditional']:
        words = pc.split(' ')
        print('clause words', words)
        if len(words) > 1:
            subject = words[0]
            operator = words[1]
            words = words[2:]
            last_word = ' '.join(words)
            print('last word', last_word)
            operator_count = sum([last_word.count(o) for o in all_vars['operator_map'].keys() if o in last_word])
            if operator_count > 1:
                new_relationships = process_placeholder(last_word, conditional_items, variables, all_vars)
                if new_relationships:
                    ''' to do: dont just extend it, apply new_relationships to existing relationships '''
                    relationships.extend(new_relationships)
            elif last_word in variables:
                subitem = variables[last_word]
                ''' add the sub-item relationship itself: (i - b) '''
                relationships.append(' '.join(subitem))
                items = subitem.split(' ')
                suboperator = None
                for i in items:
                    if i in all_vars['operator_map'].keys():
                        suboperator = i
                    else:
                        if suboperator is None:
                            ''' add the first object's applied relationship to the original subject: (x - i) '''
                            relationships.append(' '.join([subject, operator, i]))
                        else:
                            ''' add the second object's applied relationship to the original subject: (x + b) '''
                            final_suboperator = ''
                            combined = ''.join([operator, suboperator])
                            if combined in all_vars['combined_map']['negative']:
                                final_suboperator = '-'
                            elif combined in all_vars['combined_map']['positive']:
                                final_suboperator = '+'
                            elif combined in all_vars['combined_map']['equal']:
                                final_suboperator = '='
                            relationships.append(' '.join([subject, final_suboperator, i]))
    if len(relationships) > 0:
        return relationships
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
            new_key = '_'.join([k, random_letter])
    else:
        new_key = random_letter
    if new_key:
        if new_key in key_dict:
            return get_new_key(key_dict, all_vars)
        else:
            return new_key
    return False 

def replace_with_placeholders(operator_clause, operator_sentence, line, variables, all_vars):
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
        4. conditionals should be applied last
        5. then the symbolic relationships can be replaced with original values:
            "x reduces inhibitor" and "x increases b"
    '''
    placeholder_clause = []
    for i, word in enumerate(operator_clause.split(' ')):
        if word not in ['+', '-', '=']:
            prev_word = operator_clause[i - 1] if i > 0 else ''
            next_word = operator_clause[i + 1] if i < (len(operator_clause) - 1) else ''
            is_modifier = get_modifier(prev_word, word, next_word)
            if is_modifier:
                modified_word = get_modified_word(line, word)
                if modified_word:
                    new_key = get_new_key(variables, all_vars)
                    variables[new_key] = [word, 'of', modified_word]
                    placeholder_clause.append(new_key)
            else:
                new_key = get_new_key(variables, all_vars)
                variables[new_key] = word
                placeholder_clause.append(new_key)
        else:
            placeholder_clause.append(word)
    return ' '.join(placeholder_clause), variables

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
        print('get_treatment_potential: polarity', polarity, pos, stem, verb)
        if verb in all_vars['synonym_list']['negative'].keys() or stem in all_vars['synonym_list']['negative'].values() or polarity < 0.0:
            return '-'
        elif verb in all_vars['synonym_list']['positive'].keys() or stem in all_vars['synonym_list']['positive'].values() or polarity > 0.0:
            return '+'
        elif verb in all_vars['synonym_list']['equal'].keys() or stem in all_vars['synonym_list']['equal'].values(): # to do: assess equal word polarity 
            return '='
    return False

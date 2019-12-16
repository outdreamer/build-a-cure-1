from utils import *

def find_metrics(pattern, lines, row, all_vars):
    '''
    find any metrics in this pattern's matches
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information
    '''
    metrics = set()
    split_line = pattern.split(' ') if pattern is not None else []
    for i, word in enumerate(split_line):
        numbers = [w for w in word if w.isnumeric()]
        if len(numbers) > 0:
            if len(numbers) == len(word):
                next_word = split_line[i + 1] if (i + 1) < len(split_line) else ''
                if len(next_word) < 5:
                    # to do: add extra processing rather than assuming its a unit of measurement
                    metrics.add(word)
                    metrics.add(next_word) # '3 mg'
            else:
                metrics.add(word) # '3mg'
    return metrics

def find_modifiers(pattern, lines, row, all_vars):
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
                                    row['modifiers'].add(' '.join([ratio, other_word]))
        return row
    return False

def find_clauses(row, all_vars):
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

        conditional_keys = ['C', 'P', 'ADV', 'ADJ', 'verb_potential']
        pos_tags['conditional'] = []
        for tag in conditional_keys:
            pos_tags['conditional'].extend(pos_tags[tag])

        relation_keys = ['C', 'P']
        pos_tags['relation'] = []
        for tag in relation_keys:
            pos_tags['relation'].extend(pos_tags[tag])

        to do:
            - call after order_and_convert_clauses() so position is: 'subject verb relationship conditionals'
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
            elif w not in row['verbs']:
                sentence_piece.append(w)
            else:
                sentence_pieces.append(' '.join(sentence_piece))
                sentence_pieces.append(w) # add the verb separately
                sentence_piece = []
    for j, s in enumerate(sentence_pieces):
        s_split = s.split(' ') if type(s) == str else s
        for i, word in enumerate(s_split):
            if word in row['verbs']:
                prev_object = False if i < 1 else get_object_by_position(i, s_split, 'prev', row['nouns'], row['phrases'])
                prev_object = sentence_pieces[j - 1] if prev_object is False and j > 0 else prev_object
                next_object = False if i == (len(sentence_pieces) - 1) else get_object_by_position(i, s_split, 'next', row['nouns'], row['phrases'])
                next_object = sentence_pieces[j + 1] if next_object is False and j < (len(sentence_pieces) - 1) else next_object
                if active:
                    if prev_object:
                        row['subjects'].add(prev_object)
                        if next_object:
                            row['clauses'].add(' '.join([prev_object, word, next_object]))
                else:
                    # to do: handle other cases where infinitive is linguistically awkward bc clauses will be re-used later
                    if next_object:
                        row['subjects'].add(next_object)
                        if prev_object:
                            row['clauses'].add(' '.join([next_object, word, prev_object]))
    print('\nclauses', row['clauses'])
    #row['functions'].add(word) # relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
    #row['components'].add(word) # compounds, symptoms, treatments, metrics, conditions, stressors, types, variables
    row['conditionals'] = []
    row['subjects'] = []
    row['verb_relationships'] = []
    row['delimiters'] = []
    all_vars['clause_delimiters'].append('1')
    for i, c in enumerate(row['clauses']):
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
                                row['delimiters'].append(w)
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
                                row['delimiters'].append(w)
                                words.remove(w)
                        if c_strip not in  row['verb_relationships']:
                            row['verb_relationships'].append(c_strip)
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
    print('\nconditionals', row)
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
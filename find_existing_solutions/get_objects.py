from utils import *

def get_modifier(line, all_vars):
    '''
    - we're isolating modifiers bc theyre the smallest unit of 
        functions (inputs, process, outputs)
        which can be embedded in phrases, clauses, and sentences
    - we wouldnt add noun modifiers which imply an action in the past which wont be repeated:
        "protein isolate"
    - only verb modifiers which imply an action in the present to indicate ongoing relevant functionality:
        "ionizing radiation", "ionizer of radiation"
    - noun modifiers should be indexed as phrases, so get_phrases has to be called before this function
    '''
    modifier_sets = []
    patterns = get_pattern_map_in_line(line, all_vars, ['modifier'])
    if patterns:
        for p, subsets in patterns.items():
            for subset in subsets:
                modifier = find_modifier(subset, p, all_vars)
                if modifier:
                    modifier_sets.append(modifier)
    if len(modifier_sets) > 0:
        return modifier_sets
    return False

def find_modifier(subset, pattern, all_vars):
    modifier = None
    modified = None   
    tagged_dict = {} 
    blob_dict = {}
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
        words = subset.split(' ')
        for i, word in enumerate(words):
            word_pos = get_nltk_pos(word)
            if word_pos not in all_vars['pos_tags']['exclude']:
                if word in blob_dict and word in tagged_dict:
                    if blob_dict[word][0] != tagged_dict[word]:
                        ''' ntlk and blob tags differ:
                            nltk: 'imaging' => 'VBG'
                            blob: 'imaging' => 'NN', 'B-NP', 'I-PNP'
                        '''
                        modifier = word
                        next = words[i+1] if (i + 1) < len(words) else None
                        prev = words[i-1] if i > 1 else None
                        next_pos = get_pos(next)
                        prev_pos = get_pos(prev)
                        if next_pos == 'noun' or next_pos == 'verb':
                            return ' '.join([modifier, next])
                        elif prev_pos == 'noun' or prev_pos == 'verb':
                            return ' '.join([modifier, prev])
    return False
    
def get_active(line, all_vars):
    '''
    check for verb tenses normally used in passive sentences 
    # had been done = past perfect

    test cases:
    - "protein that modulates a signaling pathway" => "signaling pathway-changing protein" 
    pattern = "A were subjected to B induced by C of D"
    pattern_with_pos = "A were subjected to B induced by C of D"

    - "Rats were subjected to liver damage induced by intra-peritoneal injection of thioacetamide" => 
        "intra-peritoneal thioacetamide injection induced liver damage in rats"
        noun_phrases for this would be "intra-peritoneal thioacetamide injection", "liver damage" and "rats"
    - "chalcone isolated from Boesenbergia rotunda rhizomes" => "Boesenbergia rotunda rhizomes isolate chalcone"

    keep in mind:
        if you standardize "injection of thioacetamide" to "thioacetamide injection", 
        your other pattern configuration wont work, so either 
        add more patterns, change the pattern, or apply pattern function before this one
    '''
    active_line = None # to do: need a map between passive & active patterns
    passive = 0
    for pattern in all_vars['pattern_index']['passive']:
        found = is_pattern_in_line(line, pattern, all_vars)
        if found:
            passive += found
        passive += len(keywords_found)
    if passive > 3:
        active = apply_pattern_map(line, 'active', all_vars)
    if active_line:
        return active_line
    return False

'''
to do:
    - you still need to deconstruct the sentence based on these dependencies 
        so its represented accurately according to order of operations
        example: 
            "even x or y" should be all one clause
            "x is a and b" or "x is a and is b" should be two clauses "x is a" and "x is b"
            "x is a or b" should be one clause
    - use get_modifiers to find the modifying words like inhibitor & apply them to the verb to get the final relationship
    - add more advanced analysis for linguistic patterns of symptoms 
        'fever that gets worse when x', or 'x reduced y and diminished z even in condition x or condition a', 
        which should have condition x added to the previous relationships
    - clauses are relationships between subject and objects in line
    - retrieved clauses should be a list separated by subjects, 
        containing the acting subject, verb, & object:
        clauses = ['chemical', 'caused', 'reaction'], ['experiment', 'was', 'successful']]
    - active: x  -  did  -  this and then y  -  did  -  z
    - passive: this  -  was done  -  by x and then z  -  was done  -  by y
    - converts a sentence like: 
            "in the event of onset, symptoms appear at light speed, even if you take vitamin c at the max dose"
        to reduced ordered form:
            "symptoms appear quickly even with vitamin c max dose"
    - standardize modifiers & passive language
    - positions your sentence clauses in the same pattern   
    - handle sentences with multiple subjects - actually it should already be organized by subject into separate lines 
    - have conditionals at the end rather than the beginning
'''

def get_conditionals(line, nouns, clauses, all_vars):
    ''' assumes rearrange_sentence was already called on line used to generate clauses '''
    print('\nclauses', clauses)
    items = {'conditional': [], 'subject': '', 'verb_relationships': [], 'delimiters': []}
    all_vars['clause_delimiters'].append('1')
    for i, c in enumerate(clauses):
        c_strip = c.strip()
        if i == 0:
            items['subject'] = c_strip
        else:
            words = c_strip.split(' ')
            is_a_condition = is_condition(words, all_vars)
            if is_a_condition:
                ''' is_a_condition has the next important word in condition '''
                if get_pos(is_a_condition, all_vars) != 'verb':
                    for j, w in enumerate(words):
                        if w in all_vars['clause_delimiters']:
                            items['delimiters'].append(w)
                            remainder = ' '.join([x for x in words if words.index(x) >= j])
                            if w == words[-1]:
                                ''' the delimiter is the last word in this clause '''
                                remainder = ' '.join([x for x in words if words.index(x) < j])
                            if remainder not in items['conditional']:
                                items['conditional'].append(remainder)
                        else:
                            if c_strip not in items['conditional']:
                                items['conditional'].append(c_strip)
                else:
                    for w in words:
                        if w in all_vars['clause_delimiters']:
                            items['delimiters'].append(w)
                            words.remove(w)
                    #if c_strip not in items['conditional']:
                    #    items['conditional'].append(c_strip)
                    if c_strip not in  items['verb_relationships']:
                        items['verb_relationships'].append(c_strip)
            else:
                if c_strip not in items['conditional']:
                    items['conditional'].append(c_strip)
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


def get_clauses(line, row, all_vars):
    line, clauses = rearrange_sentence(line, all_vars)
    active = get_active(line)
    sentence_pieces = [] # break up sentence by verbs
    sentence_piece = []
    for w in line.split(' '): 
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
                    active_s = change_to_infinitive(word)
                    active_s = 'was' if active_s == 'be' else active_s # to do: handle other cases where infinitive is linguistically awkward bc clauses will be re-used later
                    if next_object:
                        row['subjects'].add(next_object)
                        if prev_object:
                            row['clauses'].add(' '.join([next_object, active_s, prev_object]))
    return row 

def rearrange_sentence(line, all_vars):
    split = line.split(',')
    clauses = []
    clauses = [
        "in the event of onset",
        "symptoms appear",
        "at light speed", 
        "even if you take vitamin c",
        "at the max dose"
    ]
    ordered_clauses = order_clauses(clauses)
    meaningful_clauses = filter_clauses(ordered_clauses)
    meaningful_clauses = [
        "symptoms appear",
        "quickly", 
        "even with",
        "vitamin c",
        "max dose"
    ]
    converted_clauses = convert_clauses(meaningful_clauses)
    converted_clauses = [
        "symptoms appear",
        "quickly", 
        "independently of",
        "vitamin c",
        "max dose"
    ]
    line = ' '.join(converted_clauses)
    return clauses, line
    
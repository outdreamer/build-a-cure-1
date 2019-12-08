from nltk import word_tokenize, pos_tag
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

from utils import read
from get_vars import get_vars
from get_patterns import *


def get_pos(word):
    noun_pos = ['NN', 'NNP', 'NNS', 'JJ', 'JJR']
    verb_pos = ['VB', 'VBP', 'VBD', 'VBG', 'VBN', 'VBZ']
    exclude = ['DT', 'WRB', 'TO', 'CC', 'IN']
    noun_string = 'noun'
    verb_string = 'verb'
    if len(word) > 0:
        pos = [item[1] for item in pos_tag(word_tokenize(word)) if item[0].lower() == word]
        if (len(pos) > 0 and pos[0] in noun_pos):
            return noun_string
        elif (len(pos) > 0 and pos[0] in verb_pos):
            return verb_string
        else:
            noun_synsets = Word(word).get_synsets(pos=NOUN)
            if len(noun_synsets) > 0:
                return noun_string
            verb_synsets = Word(word).get_synsets(pos=VERB)
            if len(verb_synsets) > 0:
                return verb_string
            else:
                stem = stemmer.stem(word)
                stem_pos = [item[1] for item in pos_tag(word_tokenize(stem)) if item[0].lower() == stem]
                if len(stem_pos) > 0:
                    if stem_pos[0] in noun_pos:
                        return noun_string
                    elif stem_pos[0] in verb_pos:
                        return verb_string
                noun_stem_synsets = Word(stem).get_synsets(pos=NOUN)
                if len(noun_stem_synsets) > 0:
                    return noun_string
                verb_stem_synsets = Word(stem).get_synsets(pos=VERB)
                if len(verb_stem_synsets) > 0:
                    return verb_string
        if pos not in exclude:
            print('get_pos: unknown word', word, pos)
    return False

def concatenate_species(data):
    data_lines = data.split('.')
    new_lines = []
    next_item = None
    for i, d in enumerate(data_lines):
        d_split = d.split(' ')
        last_item = d_split.pop()
        if len(last_item) == 1:
            if (i + 1) < len(d):
                prev_item = d_split[-1]
                if len(prev_item) > 1:
                    next_item = data_lines[i+1].strip().split(' ')[0]
                    d_next = '-'.join([last_item, next_item]) #C. elegans => C-elegans
                    d_split.append(d_next)
                    new_lines.append(' '.join(d_split))
        else:
            next_item = None
            new_lines.append(' '.join(d_split))
        if next_item is not None:
            next_item_len = len(next_item)
            if next_item == d[0:next_item_len]:
                d = ' '.join(d[next_item_len:].split(' '))
                new_lines.append(d)
    data = '.'.join(new_lines)
    return data

def get_counts(article_words, processed_data, tagged, line, metadata):
    leave_in_pos = ['NNP', 'NNS', 'JJR'] # JJR example: 'broader'
    for item in tagged:
        if len(item) == 2:
            w = item[0].lower()
            if item[1] in leave_in_pos:
                if len(w) > 0 and w not in stop:
                    w_upper = w.upper()
                    w_name = ''.join([w[0].upper(), w[1:]])
                    upper_count = article_words.count(w_upper) # find acronyms, ignoring punctuated acronym
                    count = processed_data.count(w)
                    ## and w not in verbs and w not in nouns and w_name not in ' '.join(names):
                    if item[0] == w_name and w_name != article_words[0] and w_name not in ' '.join(metadata['names']): # exclude first word in sentence
                        if upper_count > 0 and upper_count <= count:
                            if upper_count not in metadata['counts']:
                                metadata['counts'][upper_count] = set()
                            metadata['counts'][upper_count].add(w_upper)
                        else:
                            if count > 0:
                                if count not in metadata['counts']:
                                    metadata['counts'][count] = set()
                                metadata['counts'][count].add(w)
    common_words = get_most_common_words(counts, 3) # get top 3 tiers of common words
    if common_words:
        metadata['common_words'].extend(common_words)
    return metadata

def get_names(article_words, line, phrases, metadata):
    line = line.replace("'",'')
    tagged = pos_tag(word_tokenize(line))
    for p in phrases:
        if len(p) > 0:
            new_name = []
            phrase_words = p.split(' ')
            for name in phrase_words:
                pos = [item[1] for item in tagged if item[0].lower() == name]
                if len(pos) > 0:
                    pos_item = pos[0]
                    if name not in stop:
                        if pos_item == 'NNP':
                            name = ''.join([name[0].upper(), name[1:]]) if '.' not in name and '/' not in name else name.upper()
                            new_name.append(name)  
                        elif pos_item == 'NNS':
                            name = ''.join([name[0].upper(), name[1:]])
                            if name in article_string:
                                new_name.append(name)
            if len(new_name) > 0:                                         
                final_name = ' '.join(new_name)
                if len(new_name) == len(phrase_words) and final_name != article_words[0] and final_name.lower() not in metadata['nouns'] and final_name.lower() not in metadata['verbs']:
                    metadata['names'].add(final_name) # find names and store separately
    return metadata

def get_clauses(line, phrases, metadata):
    '''
    to do: 
    - add logic for other phrase types than 'noun-noun', like verb_phrases
    - clauses are relationships between subject and objects in line
    - the response object should be a list of the acting subject, verb, & object:
        row['clauses'] = ['chemical', 'caused', 'reaction'], ['experiment', 'was', 'successful']]
    # handle sentences like: "x did this and then y did z", which would be broken up like:
    active:
        x 
        did 
        this and then y 
        did 
        z
    passive: "this was done by x and then z was done by y"
        this
        was done 
        by x and then z
        was done
        by y
    '''
    line = rearrange_sentence(line)
    active = get_active(line)
    sentence_pieces = [] # break up sentence by verbs
    sentence_piece = []
    for w in line.split(' '):
        if w not in metadata['verbs']:
            sentence_piece.append(w)
        else:
            sentence_pieces.append(sentence_piece)
            sentence_pieces.append(w) # add the verb separately
            sentence_piece = []
    for i, s in enumerate(sentence_pieces):
        if s in metadata['verbs']:
            prev_object = '' if i < 1 else get_object_by_position(i, sentence_pieces, 'prev', metadata['nouns'], phrases)
            next_object = '' if i == (len(sentence_pieces) - 1) else get_object_by_position(i, sentence_pieces, 'next', metadata['nouns'], phrases)
            if active:
                metadata['subjects'].add(prev_object)
                metadata['clauses'].add(' '.join([prev_object, s, next_object]))
            else:
                active_s = change_to_active(s)
                active_s = 'was' if active_s == 'be' else active_s # to do: handle other cases where infinitive is linguistically awkward bc clauses will be re-used later
                metadata['subjects'].add(next_object)
                metadata['clauses'].add(' '.join([next_object, active_s, prev_object]))
    return metadata 

def get_pos_in_line(line, metadata):
    pattern_format_line = convert_to_pattern_format(line)
    for index, p in enumerate(pattern_format_line.split(' ')):
        if len(p) > 0:
            if p == 'verb':
                metadata['verbs'].add(line[index])
                metadata['functions'].add(item[0])
                # relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
            elif p == 'noun':
                ''' check if the noun stem is a verb, if so add it to verbs
                    # using verb_versions adds a lot of nouns like worm & rat to the verbs list
                    verb_suffixes = ['e', 'd', 'ed'] 
                    verb_versions = [pos_tag(word_tokenize(''.join([p, v]))) for v in verb_suffixes]
                '''
                metadata['nouns'].add(line[index])
                metadata['components'].add(item[0]) 
                # compounds, symptoms, treatments, metrics, conditions, stressors, types, variables
            else:
                metadata['taken_out'].add('_'.join([line[index], pos]))
    return metadataa

def remove_unnecessary_words(line, phrases, clauses):
    ''' this should remove all excessive language where phrases or clauses dont add meaning '''
    return line

def rearrange_sentence(line):
    '''
    this function is to format your sentences in the same way

    this means fulfilling the following expectations:
    - having conditionals at the end rather than the beginning
    - standardized words when synonyms are found
    - simplified language where clearly mappable

    so a sentence like: 
    "in the event of onset, symptoms appear at light speed, even if you take vitamin c at max dose"

    is reduced to:
    "symptoms appear even with vitamin c max dose"
    '''
    return line

def get_charge_of_word(word, all_vars):
    found_synonym = True if word in all_vars['supported_synonyms'] else False
    print('found synonym', found_synonym)
    if found_synonym:
        for synonym_type in all_vars['key_map']:
            if found_synonym in all_vars['key_map'][synonym_type]:
                print('found synonym charge', synonym_type)
                return synonym_type
    return False

def get_similarity_to_title(string, title):
    string_split = string.split(' ')
    title_split = title.split(' ')
    both = set()
    similarity = {}
    for s in string_split:
        if s in title_split:
            both.add(s)
    if len(both) > 0:
        key = (len(both) / len(title))
        similarity[string] = key
        return similarity
    return False

def get_most_common_words(counts, top_index):
    '''
    given counts which is structured like:
    counts = {
        0: ['words', 'that', 'appeared', 'once'],
        1: ['items', 'shown', 'twice']
    }
    '''
    sorted_keys = sorted(counts.keys()).reverse()
    max_key = max(counts.keys())
    retrieved_index = 0
    max_words = []
    for k in sorted_keys:
        max_words.extend(counts[k])
        retrieved_index += 1
        if retrieved_index == top_index:
            return max_words
    if len(max_words) > 0:
        return max_words
    return False

def get_structural_metadata(line, title, article_words, article_string, index, row, metadata_keys):
    line = replace_contractions(line)
    line = remove_standard_punctuation(line)
    # line = line.replace(',','')
    similarity = get_similarity_to_title(line, title)
    if similarity:
        for line, score in similarity.items():
            if line not in row['title_similarities']:
                row['title_similarities'][line] = score
    pattern_stack = get_pattern_stack(line)
    if pattern_stack:
        for key, val in pattern_stack.items():
            if key not in row['pattern_stack']:
                row['pattern_stack'][key] = val
            else:
                row['pattern_stack'][key].extend(val)
    row = get_pos_in_line(line, row)
    phrases = TextBlob(line).noun_phrases
    if len(phrases) > 0:
        metadata['phrases'] = phrases
    row = get_names(article_string, line, metadata['phrases'], row)
    line = remove_names(line, row['names'])
    row = get_clauses(line, metadata['phrases'], row)
    tagged = pos_tag(word_tokenize(line))
    processed_data = remove_standard_punctuation(article_string.lower())
    processed_data = processed_data.replace("'",'').replace(',','')
    row = get_counts(article_words, processed_data, tagged, line, row)
    for key in row:
        if key in index:
            index[key] = index[key].union(row[key])
    return index, row

def remove_names(line, names_list):
    '''
    # to do: remove all irrelevant proper nouns like place, company, university & individual names
    if row:
        if 'names' in row:
            for name in row['names']:
                line = line.replace(name, '') 
    '''
    return line

def merge(temp, metadata):
    for key, val in temp.items():
        if val:
            if type(val) == dict:
                merge_val = '::'.join(['_'.join([k, v]) for k, v in val.items()])
            if key in metadata:
                if type(metadata[key]) == set:
                    if type(val) == str:
                        metadata[key].add(val)
                    elif type(val) == dict:
                        metadata[key].add(merge_val)
                    else:
                        for item in val:
                            metadata[key].add(item)
                elif type(metadata[key]) == str:
                    if type(val) == str:
                        metadata[key] = ','.join([metadata[key], val])
                    elif type(val) == dict:
                        metadata[key] = ','.join([metadata[key], merge_val])
                    else:
                        metadata[key] = ','.join([metadata[key], ','.join(val)])
                elif type(metadata[key]) == dict:
                    for k, v in metadata[key]:
                        if type(val) == str:
                             metadata[key][k] = ','.join([metadata[key][k], val])
                        if type(val) == dict:
                            for a, b in val.items():
                                if a in metadata[key]:
                                    if type(metadata[key][a]) == set:
                                        if a not in metadata[key]:
                                            metadata[key][a] = set()
                                        metadata[key][a].add(b)
                                    elif type(metadata[key][a]) == list:
                                        if a not in metadata[key]:
                                            metadata[key][a] = []
                                        metadata[key][a].append(b)
                                    elif type(metadata[key][a]) == str:
                                        metadata[key][a] = ','.join([metadata[key][a], b])
                        else:
                            if type(metadata[key][k]) == set:
                                metadata[key][k] = metadata[key][k].union(list(val))
                            elif type(metadata[key][k]) == list:
                                metadata[key][k].extend(val)
    return metadata

def get_active(line):
    ''' check for verb tenses normally used in passive sentences 
    VBD: Verb, past tense #thought, did, gave
    VBG: Verb, gerund or present participle #thinking, doing, giving
    VBN: Verb, past participle #had thought, had done, had given
    VBP: Verb, non-3rd person singular present 
    VBZ: Verb, 3rd person singular present
    # had been done = past perfect
    '''
    passive_keywords = [
        ' by '
    ]
    passive_patterns = [
        'was past_participle',
        'had past_participle',
        'has been past_participle'
    ]
    formatted_line = convert_to_pattern_format(line)
    passive = 0
    for p in passive_patterns:
        keywords_found = [True for x in passive_keywords if x in line]
        found = find_pattern(line, formatted_line, p)
        if found:
            passive += 1
        passive += len(keywords_found)
    if passive > 2:
        return False
    return True

def replace_contractions(line):
    contractions = {
        'isnt': 'is not', 
        'dont': 'do not', 
        'wont': 'will not', 
        'mustnt': 'must not', 
        'couldnt': 'could not', 
        'cant': 'can not', 
        'wouldnt': 'would not', 
        'shouldnt': 'should not', 
        'havent': 'have not'
    }
    line = line.replace("'",'')
    new_line = []
    for w in line.split(' '):
        if w in contractions:
            new_line.append(contractions[w])
        else:
            new_line.append(w)
    line = ' '.join(new_line)
    return line

def get_phrase_with_word(word, phrases, line):
    phrase_string = ' '.join(phrases)
    if word in phrase_string:
        for phrase in phrases:
            '''
            p_pos = line.find(phrase)
            word_pos = line.find(word)
            if word_pos >= p_pos:
            '''
            for i, phrase_word in enumerate(phrase.split(' ')):
                if phrase_word == word and i == 0:
                    ''' this is the first word in a phrase so get the whole phrase '''
                    return phrase
    return False

def get_object_by_position(index, sentence_pieces, position, check_list, phrases):
    relevant_piece = sentence_pieces[index - 1] if position == 'prev' else sentence_pieces[index + 1]
    sequenced_words = relevant_piece.split(' ') if position == 'next' else relevant_piece.split(' ').reverse()
    for w in sequenced_words:
        found = get_phrase_with_word(w, phrases, line)
        if found:
            return found
        elif w in check_list: # check that its in the noun list passed in before returning it as an object
            return w
    return False

'''
structural metadata example output:

counts {
     1: {'science', 'beyond'},
     2: {'university'},
     11: {'insulin'},
     5: {'said'}
}
phrases {
     3: {'elegans', 'pi3k/akt', 'likely', 'm.d'},
     1: {'pathways', 'systems', 'broader', 'variants', 'processing', 'synthesis', 'imbalances', 'besides', 'strategies', 'drugs', 'therapies'},
     2: {'ways', 'molecules', 'components', 'worms'},
     7: {'cells'},
     4: {'diseases', 'proteins'}
}
verbs {'responses', 'maintaining', 'fold', 'contributes', 'understanding', 'exists', 'deleting', 'corresponding', 'screen'}
nouns {
    'researcher', 'total', 'sclerosis', 'proper', 'stress', 'parent', 'abnormal', 'phenotype', 'disease', 'human', 'chaperone', 'convenient', 'protein', 'professor', 'pancreatic', 'rat', 'genetic', 'amyotrophic', 
    'percent', 'insulin', 'reticulum', 'biogenesis', 'content', 'new', 'role', 'homeostasis', 'mammalian', 'health', 'contribution', 'Trap-alpha', 'model', 'associate', 'worm', 'pathway', 'research', 'expression', 
    'cancer', 'beta', 'endoplasmic', 'cell', 'response', 'gene', 'insulin-like', 'system', 'cellular', 'oncology', 'nematode', 'lateral', 'growth', 'factor', 'anti-tumor', 'unexpected', 'neurodegenerative', 'reduction', 
    'approach', 'culture', 'primordial', 'common', 'perspective'
}
names {'Caenorhabditis', 'Medical Center', 'Advances', 'Er', 'Vanderbilt', 'Alzheimers', 'PI3K/AKT', 'Michigan', 'M.D', 'Trap-alpha'}
taken_out [
    'therapies_N', 'drugs_N', 'strategies_N', 'pathways_N', 'components_N', 'elegans_N', 'worms_N', 'systems_N', 'variants_N', 'cells_N', 'cells_N', 'molecules_N', 'cells_N', 'proteins_N', 'proteins_N', 
    'were_R', 'likely_B', 'imbalances_N', 'diseases_N', 'molecules_N', 'besides_N', 'broader_J', 'ways_N'
]
pattern stack [
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['understanding of type']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['professor of medicine']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['University of Michigan']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['molecules of insulin']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['expression of chaperone']}
]
'''

'''
stemmer = SnowballStemmer("english")
patterns = convert_patterns(language_patterns)
print('converted patterns', patterns)
metadata = 'all'
all_vars = get_vars()
empty_index = get_empty_def(metadata, all_vars['supported_params'])
row = empty_index
index = empty_index
article_string = read('article.txt')
if article_string:
    article_string = concatenate_species(article_string)
    article_words = article_string.split('\n')
    title = article_words[0]
    for line in article_words:
        if len(line.strip()) > 0:
            metadata = get_structural_metadata(line, title, article_words, article_string, index, row, metadata)
            for key in metadata:
                print(key, metadata[key])
'''
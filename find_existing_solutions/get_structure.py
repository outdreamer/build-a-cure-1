from nltk import word_tokenize, pos_tag

from utils import *
from get_vars import get_vars

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

def get_counts_in_line(words, row):
    ''' to do: nouns with highest counts are likely to be central objects '''
    for w in words:
        count = words.count(w)
        w_upper = w.upper()
        w_name = w.capitalize() if w.capitalize() != words[0] else w
        upper_count = words.count(w_upper) # find acronyms, ignoring punctuated acronym
        if count > 0 or upper_count > 0:
            count_num = upper_count if upper_count <= count else count
            count_val = w_upper if upper_count <= count else w 
            if count_num not in row['counts']:
                row['counts'][count_num] = set()
            row['counts'][count_num].add(count_val)
    if len(row['counts']) > 0:
        common_words = get_most_common_words(row['counts'], 3) # get top 3 tiers of common words
        if common_words:
            row['common_words'] = row['common_words'].union(common_words)
    return row

def get_names(article_words, line, row):
    # to do: identify all irrelevant proper nouns like place, company, university & individual names
    tagged = pos_tag(word_tokenize(line))
    for p in row['phrases']:
        if len(p) > 0:
            new_name = []
            phrase_words = p.split(' ')
            for name in phrase_words:
                pos = [item[1] for item in tagged if item[0].lower() == name]
                if len(pos) > 0:
                    pos_item = pos[0]
                    if pos_item == 'NNP':
                        name = ''.join([name[0].upper(), name[1:]]) if '.' not in name and '/' not in name else name.upper()
                        new_name.append(name)  
                    elif pos_item == 'NNS':
                        name = ''.join([name[0].upper(), name[1:]])
                        if name in '\n'.join(article_words):
                            new_name.append(name)
            if len(new_name) > 0:                                         
                final_name = ' '.join(new_name)
                if len(new_name) == len(phrase_words) and final_name != line[0:len(final_name)] and final_name.lower() not in row['nouns'] and final_name.lower() not in row['verbs']:
                    row['names'].add(final_name) # find names and store separately
    line = ' '.join([w for w in line.split(' ') if w not in row['names']])
    return row, line

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

def get_similar_lines(row, line, title):
    max_line = ''
    if line != title:
        counts = {}
        similarity = get_similarity_to_title(line, title)
        if similarity:
            for line, score in similarity.items():
                if score not in row['title_similarities']:
                    counts[score] = line
                    row['title_similarities'][line] = score
        max_score = max(counts.keys())
        max_line = counts[max_score]
    return max_line, row

def get_structural_metadata(line, row, metadata_keys, all_vars):
    line_patterns = get_patterns_in_line(line, all_vars)
    if line_patterns:
        row['line_patterns'] = line_patterns
    row = get_pos_in_line(line, row)
    phrases = get_phrases(line)
    if phrases:
        row['phrases'] = phrases
    row, line = get_names(article_string, line, row)
    row = get_clauses(line, row, all_vars)
    row = get_counts_in_line(line, row)
    return row

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
    relevant_piece = sentence_pieces[index - 1] if position == 'prev' else sentence_pieces[index + 1] if index < (len(sentence_pieces) - 1) else ''
    if relevant_piece != '':
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
    {'|NN NNP NNS JJ JJR| of |NN NNP NNS JJ JJR|': ['understanding of type']}, 
    {'|NN NNP NNS JJ JJR| of |NN NNP NNS JJ JJR|': ['professor of medicine']}, 
    {'|NN NNP NNS JJ JJR| of |NN NNP NNS JJ JJR|': ['University of Michigan']}, 
    {'|NN NNP NNS JJ JJR| of |NN NNP NNS JJ JJR|': ['molecules of insulin']}, 
    {'|NN NNP NNS JJ JJR| of |NN NNP NNS JJ JJR|': ['expression of chaperone']}
]
'''

'''
all_vars = get_vars()
article_string = read('article.txt')
if article_string:
    article_string = concatenate_species(article_string)
    article_words = article_string.split('\n')
    title = article_words[0]
    for line in article_words:
        if len(line.strip()) > 0:
            empty_index = get_empty_def(metadata, all_vars['supported_params'])
            metadata = get_structural_metadata(line, title, article_words, article_string, empty_index, empty_index, 'all')
            for key in metadata:
                print(key, metadata[key])
'''
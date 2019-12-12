from nltk import word_tokenize, pos_tag

from utils import *
from get_vars import get_vars

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
    ''' get counts, most_common_words, nouns, verbs, noun_phrases, and taken_out words '''
    row = get_pos_in_line(line, row, all_vars)
    ''' get phrases comes before get_names '''
    phrases = get_phrases(line, row, all_vars)
    if phrases:
        row['phrases'] = phrases
    ''' replace non-medical irrelevant names with empty string '''
    row = replace_names(row, all_vars)
    
    ''' these should be isolated & done with get_metadata '''
    ''' get modifier blocks '''
    modifiers = get_modifier(line, row, all_vars)
    if modifiers:
        row['modifiers'] = modifiers
    ''' get clause, functions, component, & relationship blocks '''
    row = get_clauses(line, row, all_vars)
    ''' get any pos patterns found in line '''
    line_patterns = get_patterns_in_line(line, row, all_vars)
    if line_patterns:
        row['line_patterns'] = line_patterns
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
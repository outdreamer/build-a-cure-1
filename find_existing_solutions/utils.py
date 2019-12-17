import json, itertools, csv, os, ssl
import nltk
from nltk import CFG, pos_tag, word_tokenize, ne_chunk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob, Sentence, Word, WordList
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from get_index_def import get_empty_index
from get_vars import read, get_singular, get_stem
from get_patterns import apply_pattern_map
from get_pos import get_nltk_pos

stop = set(stopwords.words('english'))

''' SIMILARITY FUNCTIONS '''

def get_polarity(line):
    ''' to do: use blob.sentiment_assessments 
            Sentiment(
                polarity=-0.008806818181818186, 
                subjectivity=0.32386363636363635, 
                assessments=[
                    (['positive'], 0.22727272727272727, 0.5454545454545454, None), 
                    (['absence'], -0.0125, 0.0, None), 
                    (['due'], -0.125, 0.375, None), 
                    (['other'], -0.125, 0.375, None)
                ]
            )
    '''
    blob = get_blob(line)
    if blob:
        sentiment = blob.sentiment
        if sentiment:
            if sentiment.polarity:
                return roun(sentiment.polarity, 1)
    return 0

def correct_spelling(line):
    blob = Sentence(line)
    if blob:
        return blob.correct()
    return text

def get_subjectivity(line):
    return line

''' GET STRUCTURAL TYPE FUNCTIONS '''

def get_blob(string):
    if type(string) == str:
        return TextBlob(string)
    return False

def replace_names(row, all_vars):
    # to do: identify all irrelevant proper nouns like place, company, university & individual names
    original_words = row['original_line'].split(' ')
    tagged = pos_tag(word_tokenize(row['line']))
    ''' to do: make sure names are grouped into phrases '''
    for p in row['phrase']:
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
                        if name in original_words:
                            new_name.append(name)
            if len(new_name) > 0:                                         
                final_name = ' '.join(new_name)
                if len(new_name) == len(phrase_words):
                    if final_name != row['line'][0:len(final_name)]:
                        if final_name.lower() not in row['noun']:
                            if final_name.lower() not in row['verb']:
                                row['name'].add(final_name) # find names and store separately
    row['line'] = ' '.join([w for w in row['line'].split(' ') if w not in row['name']])
    return row

def get_determiner_ratio(word):
    ratios = {
        'extra': ['extra', 'another', 'more'],
        'same': ['whole', 'both', 'all', 'every', 'each'], # to do: integrate equal keywords like 'basically', 'essentially', 'same', 'equal']
        'high': ['high', 'extremely', 'such', 'especially', 'very', 'much', 'many', 'lot', 'quite'],
        'some': ['a', 'an', 'any', 'whatever', 'which', 'whichever', 'part', 'half', 'some'], # exclude 'either'
        'one': ['the', 'this', 'that', 'those', 'these', 'them', 'particular'],
        'none': ['none', 'nothing', 'nary', 'neither', 'nor', 'no']
    }
    for k, v in ratios.items():
        if word in v or word == k:
            return k
    return False

def get_ngrams_by_position(word_list, word, x, direction):
    ''' 
    get a list of words of length (2x + 1) in word list starting with word 
    and iterating outward in direction x number of times 
    '''
    list_length = len(word_list)
    word_index = word_list.index(word)
    if word_index:
        start = word_index - x if word_index > x else word_index if direction == 'next' else 0
        end = word_index + x if (word_index + x) < list_length else word_index if direction == 'prev' else list_length
        return word_list[start:end]
    return False

def get_most_common_words(counts, top_index):
    '''
    counts = {
        0: ['words', 'that', 'appeared', 'once'],
        1: ['items', 'shown', 'twice']
    }
    '''
    count_keys = counts.keys()
    if len(count_keys) > 1:
        top_index = len(count_keys) - 1 if len(count_keys) < top_index else top_index
        sorted_keys = reversed(sorted(count_keys))
        max_key = max(count_keys)
        retrieved_index = 0
        max_words = set()
        for k in sorted_keys:
            max_words = max_words.union(counts[k])
            retrieved_index += 1
            if retrieved_index == top_index:
                return max_words
        if len(max_words) > 0:
            return max_words
    return False

def is_condition(asp_words, row, all_vars):
    for word in asp_words:
        if word in all_vars['clause_delimiters']:
            return word
        else:
            pos = row['pos'][word] if word in row['pos'] else get_pos(word)
            if pos not in all_vars['pos_tags']['ALL_N'] or word not in stop:
                return word
    return False

def get_sentence_delimiter(text):
    return '\n' if text.count('\n') > text.count('. ') else '. '

def standardize_delimiter(text):
    blob = get_blob(text)
    if blob:
        sentences = blob.sentences
        if len(sentences) > 0:
            return '\n'.join([s.string for s in sentences])
    delimiter = get_sentence_delimiter(text)
    if delimiter:
        return '\n'.join(text.split(delimiter))
    return False

def standardize_punctuation(line):
    # remove apostrophes, replace brackets with parenthesis
    line = line.replace('[', ' ( ').replace(']', ' ) ').replace("'", '') 
    # replace clause punctuation with comma
    line = line.replace(' - ', ' , ')
    '''
    operator_keys = all_vars['operator_map'].keys()
    for k in operator_keys:
        line = line.replace(k, '')
    '''
    # space comma to avoid conflation with words, then replace double spaces
    line = line.replace(',', ' , ').replace('  ', ' ')
    return line

def remove_stopwords(line, word_map):
    custom_removal = [] #['the', 'a', 'an', 'them', 'they']
    words = line.split(' ') if type(line) == str else line
    word_list = []
    for w in words:
        if '/' in w or '|' in w:
            option = select_option(w, word_map)
            if option:
                word_list.append(option)
        else:
            if w[-1] == 's':
                w = get_singular(w)
            if w not in stopwords.words('english') and w not in custom_removal:
                word_list.append(w)
    if len(word_list) > 0:
        return ' '.join(word_list)
    return line

def replace_quotes_with_parenthesis(line):
    quotes = line.count('"')
    if quotes > 0:
        new_line = []
        quote_pairs = quotes / 2
        if quote_pairs == int(quote_pairs):
            found_first = False
            this_quote = []
            for w in line.split(' '):
                if '"' in w:
                    if found_first:
                        ''' already found quote in pair, closing quote '''
                        found_first = False
                        this_quote.append(w.replace('"', ')'))
                        new_line.append(' '.join(this_quote))
                        this_quote = []
                    else:
                        ''' first quote in pair, opening quote '''
                        found_first = True
                        this_quote.append(w.replace('"', '('))
                else:
                    new_line.append(w)
        else:
            print('uneven quotes', quote_pairs, quotes, line)
        # now all quote content should be surrounded by parentheses instead
        line = ' '.join(new_line) if len(new_line) > 0 else line
    return line

def select_option(alt_phrase, word_map):
    ''' 
        this function translates:
        - expression/activity = expression-activity (different pos = phrase)
        - describes/delineates = describes (same pos, if synonym, choose more common one)
    '''
    delimiter = [c for c in '/|' if c in alt_phrase]
    alts = alt_phrase.split(delimiter)
    alt_pos = [word_map[a] for a in alts]
    if len(alt_pos) > 0:
        if alt_pos[0]:
            default_pos = alt_pos[0]
            found_non_default = [True for a in alt_pos if a != default_pos]
            if found_non_default:
                ''' these options are different pos so dont remove them '''
                alt_phrase = alt_phrase.replace(delimiter, '-')
                return alt_phrase
            else:
                ''' these options are all the same pos, check if theyre synonyms '''
                default_alt = alts[0]
                for a in alts:
                    if a != default_alt:
                        similarity = get_similarity(default_alt, a)
                        if similarity:
                            if similarity < 0.7:
                                ''' found a non-synonym, keep all options '''
                                return alt_phrase
                ''' all words were synonyms, return first option if most common not found '''
                most_common_option = get_most_common_word(alts)
                if most_common_option:
                    if len(most_common_option) > 0:
                        return most_common_option[0]
                return default_alt
    return alt_phrase

def get_charge_of_word(word, all_vars):
    if word in all_vars['supported_synonyms']:
        synonym = all_vars['supported_synonyms'][word]
        for synonym_type in all_vars['charge']:
            if synonym in all_vars['charge'][synonym_type]:
                print('get_charge_of_word: found synonym charge', word, synonym, synonym_type)
                return synonym_type
    return False

def get_similarity(base_word, new_word, pos_type, all_vars):
    if pos_type in ['N', 'V', 'ADV', 'ADJ']:
        base_synsets = Word(base_word).get_synsets(pos=pos_type)
        new_synsets = Word(new_word).get_synsets(pos=pos_type)
        if len(new_synsets) > 0 and len(base_synsets) > 0:
            similarity = base_synsets.path_similarity(new_synsets)
            print('\tget similarity', new_synsets, base_synsets, similarity)
            return similarity
    return 0

def get_similarity_to_title(title, row):
    similarity = 0
    if row['line'] != title:
        title_split = title.split(' ')
        both = set()
        for s in row['line'].split(' '):
            if s in title_split:
                both.add(s)
        if len(both) > 0:
            similarity = round(len(both) / len(title_split), 1)
        if similarity:
            row['similarity'] = similarity
    return row

''' STORAGE FUNCTIONS '''

def get_local_database(database_dir, object_types):
    docs = {}
    if not os.path.exists(database_dir) or not os.path.isdir(database_dir):
        cwd = getcwd()
        database_dir = ''.join([cwd, '/', database_dir])
    if os.path.exists(database_dir) and os.path.isdir(database_dir):
        object_types = object_types if object_types else []
        if len(object_types) > 0:
            paths = [''.join([database_dir, '/', ot, '.txt']) for ot in object_types]
            docs = get_local_data(paths, docs)
        else:
            paths = [''.join([database_dir, '/', fp]) for fp in os.listdir(database_dir)]
            docs = get_local_data(paths, docs)
    if docs:
        return docs
    return False

def get_local_data(paths, docs):
    for path in paths:
        object_type = path.split('/')[-1].replace('.txt', '')
        if os.path.isfile(path):
            contents = read(path)
            if contents:
                lines = contents.split('\n')
                if len(lines) > 0:
                    docs[object_type] = set(lines)
    return docs

def save(path, data):
    print('\t\twriting', path)
    path = path.replace('txt', 'json') if type(data) != str else path
    with open(path, 'w') as f:
        if 'json' in path:
            json.dump(data)
        else:
            f.write(data)
        f.close()
    return True

def write_csv(rows, header_list, path):
    if len(rows) > 0:
        with open(path, 'wt') as f:
            csv_writer = csv.DictWriter(f, fieldnames=header_list)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
            f.close()
            return True 
    return False

def downloads(paths):
    for path in paths:
        if not os.path.exists(path):
            ''' this is the first run so download packages '''
            os.mkdir(path)
            try:
                _create_unverified_https_context = ssl._create_unverified_context
            except AttributeError:
                pass
            else:
                ssl._create_default_https_context = _create_unverified_https_context
            # download all the corpuses by running nltk.download() & selecting it manually in the gui that pops up, 
            nltk.download()
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
            nltk.download('maxent_ne_chunker')
    return True
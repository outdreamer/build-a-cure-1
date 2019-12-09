import json, itertools, csv
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset
stemmer = SnowballStemmer("english")  
lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english'))

def get_stem(word):
    stem = stemmer.stem(word)
    if stem:
        return stem 
    return word

def get_polarity(line):
    return TextBlob(line).sentiment.polarity

def change_to_infinitive(verb):
    infinitive = lemmatizer.lemmatize(verb, 'v')
    print('infinitive', infinitive)
    return infinitive

def standard_text_processing(text, all_vars):
    text = remove_standard_punctuation(text)
    text = remove_stopwords(text.strip().lower())
    words = text.strip().split(' ')
    if len(words) > 1:
        formatted_text = ''.join([x for x in text if x in all_vars['alphanumeric']])
        if len(formatted_text) > 0:
            return formatted_text
    return text       

def remove_standard_punctuation(line):
    return line.replace('"', '').replace('(','').replace(')','').replace('[','').replace(']','')

def get_definitions(word):
    defs = Word(base_word).definitions
    print('\tdefinitions', defs)
    return defs

def get_keywords(word):
    ''' add option to use local_database/index (phrases, relationships) or pull from a data source '''
    keywords = []
    defs = Word(word).definitions:
    for d in defs:
        words = d.split(' ')
        for w in words:
            if w not in stop:
                keywords.append(w)
    if len(keywords) > 0:
        return keywords
    return False

def get_local_database(path, objects):
    docs = []
    if not os.path.exists(path) or not os.path.isdir(path):
        cwd = getcwd()
        path = ''.join([cwd, '/', path])
    if os.path.exists(path) and os.path.isdir(path):
        for file_path in os.path.listdir(path):
            full_path = '/'.join([path, file_path])
            if os.path.isfile(full_path):
            if len(objects) > 0:
                if file_path in objects:
                    contents = read(full_path)
                    if contents:
                        docs.append(contents)
            else:
                contents = read(full_path)
                if contents:
                    docs.append(contents)
    if len(docs) > 0:
        return docs
    return False

def get_usage_patterns(word, articles, local_database):
    patterns = set()
    if local_database: #'data' folder
        articles = get_local_database(local_database)
    if len(articles) > 0:
        for a in articles:
            for line in a.split('\n'):
                words = line.split(' ')
                for i, w in enumerate(words):
                    if w == word:
                        prev_word = words[i - 1] if i > 0 else ''
                        next_word = words[i + 1] if i < (len(words) - 1) else ''
                        pattern = ' '.join([prev_word, word, next_word])
                        converted_pattern = convert_to_pattern_format(pattern.strip())
                        if converted_pattern:
                            patterns.add(converted_pattern)
        if len(patterns) > 0:
            return patterns
    return False

def get_similarity(base_word, new_word):
    new_synsets = Word(new_word).get_synsets(pos=VERB)
    base_synsets = Word(base_word).get_synsets(pos=VERB)
    if len(new_synsets) > 0 and len(base_synsets) > 0:
        similarity = base_synsets.path_similarity(new_synsets)
        print('\tget similarity', new_synsets, base_synsets, similarity)
        return similarity
    return 0

def get_partial_match(keyword_list, words, match_type):
    words = [words] if type(words) == str else words
    for word_or_phrase in words:
        for word in word_or_phrase.split(' '):
            for k in keyword_list:
                if '-' in k:
                    position = 'suffix' if '-' == k[0] else 'prefix' if '-' == k[len(k) - 1] else 'other'
                    new_k = k.replace('-', '')
                    suffix = word[(len(word)-len(new_k)):len(word)]
                    prefix = word[0:len(new_k)]
                    if (position == 'suffix' and new_k == suffix) or (position == 'prefix' and new_k == prefix):
                        return True if match_type == 'bool' else k
                else:
                    if len(k) > 4 and len(word) > 4 and k in word or word in k:
                        return True if match_type == 'bool' else k
                    match_count = 0
                    for i in range(0, len(word)):
                        if i < len(k):
                            if k[i] == word[i]:
                                match_count += 1
                    match_ratio = match_count / len(word)
                    if match_ratio > 0.8:
                        return True if match_type == 'bool' else k
                    '''
                    word_root = stemmer.stem(word)
                    print('word root', word_root, word)
                    k_root = stemmer.stem(k)
                    if word_root == k_root:
                        return True if match_type == 'bool' else k
                    '''
    return False

def save(path, data):
    path = path.replace('txt', 'json') if type(data) != str else path
    with open(path, 'w') as f:
        if 'json' in path:
            json.dump(data)
        else:
            f.write(data)
        f.close()
    return True

def read(path):
    index = None
    if os.path.exists(path):
        print('found path', path)
        with open(path, 'r') as f:
            index = json.load(f) if 'json' in path else f.read()
            f.close()
    return index

def write_csv(rows, header_list, path):
    with open(path, 'wt') as f:
        csv_writer = csv.DictWriter(f, fieldnames=header_list)
        csv_writer.writeheader()
        csv_writer.writerows(rows)
        f.close()
        return True 
    return False

def remove_stopwords(line):
    ''' to do: add semantic & keyword equivalence checks '''
    custom_removal = [] #['the', 'a', 'an', 'them', 'they']
    words = line.strip().split(' ') if type(line) == str else line
    word_list = [w for w in words if w not in stopwords.words('english') and w not in custom_removal]
    return ' '.join(word_list)

import os, json, itertools, csv
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset
stemmer = SnowballStemmer("english")  

def get_definitions(word):
    defs = Word(base_word).definitions
    print('\tdefinitions', defs)
    return defs

def get_similarity(base_word, new_word):
    new_synsets = Word(new_word).get_synsets(pos=VERB)
    base_synsets = Word(base_word).get_synsets(pos=VERB)
    if len(new_synsets) > 0 and len(base_synsets) > 0:
        similarity = base_synsets.path_similarity(new_synsets)
        print('\tget similarity', new_synsets, base_synsets, similarity)
        return similarity
    return 0

def get_subword_match(keyword_list, words, match_type):
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

def check_for_supported_synonym(word, index_keys, supported_core):
    common_synonym = ''
    # word_root = stemmer.stem(word)
    for key in supported_core:
        for item in key:
            if item == word:
                common_synonym = key
        matched = get_subword_match(supported_core[key], word, 'word')
        if matched:
            if key in index_keys:
                common_synonym = key
            else:
                common_synonym = matched if '-' not in matched else word
    if len(common_synonym) > 0:
        return common_synonym
    return False

def get_standard_word(row, word, supported_core, supported_synonyms, standard_verbs):
    '''
    this should standardize a word like 'enhance' to a verb like 'increase' 
    actually we can replace that for now with a synonym list, as in get_synonym_list()
    '''
    if word in supported_synonyms or word in standard_verbs:
        return word
    # word_root = stemmer.stem(word)
    standard_word = check_for_supported_synonym(word, row.keys(), supported_core)
    if standard_word:
        return standard_word
    verb_synset = Word(word).get_synsets(pos=VERB)
    noun_synset = Word(word).get_synsets(pos=NOUN)
    synset = verb_synset if len(verb_synset) > 0 else noun_synset if len(noun_synset) > 0 else []
    if len(synset) > 0:
        counts = {}
        for s in synset:
            sname = s.name().split('.')[0]
            if sname in counts:
                counts[sname] += 1
            else:
                counts[sname] = 1
        count_values = [counts[x] for x in counts]
        max_value = max(count_values)
        max_synonyms = [c for c in counts if counts[c] == max_value]
        if len(max_synonyms) > 0:
            for ms in max_synonyms:
                '''
                supported_synonyms has synonyms of common functions like increase, enhance, activate
                standard_verbs has common verbs found in medical abstracts
                '''
                if ms in supported_synonyms or ms in standard_verbs:
                    return ms
            #print('\tnot in supported synonyms or standard relationships', word, ms, max_synonyms[0])
            return max_synonyms[0]
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

def remove_duplicates(line):
    ''' to do: add semantic & keyword equivalence checks '''
    custom_removal = ['the', ',', '.', 'a', 'an', 'them', 'they']
    if type(line) == str:
        line = line.strip()
        line_list = set(w for w in line.split(' ') if w.lower().strip() not in stopwords.words('english') and w.lower().strip() not in custom_removal)
        return ' '.join(line_list)
    else:
        return [w.lower() for w in line if w.strip().lower() not in stopwords.words('english') and w.strip.lower() not in custom_removal]
    return line
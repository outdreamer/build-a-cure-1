import json, itertools, csv
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob

lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

def get_stem(word):
    stem = stemmer.stem(word)
    if stem:
        return stem 
    return word

def get_pos_in_line(line, row):
    for word in line.split(' '):
        if len(word) > 0:
            pos = get_pos(word)
            if pos == 'verb':
                row['verbs'].add(word)
                row['functions'].add(word)
                # relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
            elif pos == 'noun':
                row['nouns'].add(word)
                row['components'].add(word) 
                # compounds, symptoms, treatments, metrics, conditions, stressors, types, variables
            else:
                row['taken_out'].add('_'.join([word, pos]))
    return row

def get_modifier(prev_word, word, next_word):
    ''' if this is a modifier, return True 
    - the reason we're isolating modifiers is because theyre embedded relationships 
    so in order to process them correctly, we have to extract them 
    & format them the same as other relationships 
    - then we can do more straightforward calculations with the operator_clause 
    & generate the full set of relationships in the original clause
    - we can easily identify modifiers that are in syns or modifier index 
    but for others we need standard pos patterns

    to do:
        - use prev_word & next_word in get_modifier
    '''
    modifier_score = 0
    modifier_substrings = [
        "or",
        "er",
        "ed"
    ]
    modifier_patterns = [
        'noun-noun', # the second noun has a verb root, ie "enzyme-inhibitor"
        'noun noun', 
        'noun-verb',
        'noun verb', 
        '[noun adverb adjective verb] [noun verb]', # detoxified compound
        '[noun verb] [noun adverb adjective verb]' # compound isolate
    ]
    word_pos = get_pos(word)
    stem_pos = get_pos(get_stem(word))
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

def get_topic(word):
    '''
      this function will be used in remove_unnecessary_words
      to filter out words that are either non-medical or too specific to be useful (names)

      test cases:
          permeability => ['structure']
          medicine => ['medical']
          plausibility => ['logic']
    '''
    topics = ['structural', 'logical']
    stem = get_stem(word)

def get_first_important_word(words):
    for word in words:
        pos = get_pos(word)
        if pos == 'verb' or word not in stop:
            return word
    return False

def get_blob(string):
    if type(string) == str:
        return TextBlob(string)
    return False

def get_correlation_of_relationship(intent, line):
    blob = get_blob(line)
    print("\tline sentiment", blob.sentiment, "line", line)
    if intent:
        intent_blob = get_blob(intent)
        print("\tintent sentiment", intent_blob.sentiment, "intent", intent)
    return get_polarity(line)

def get_polarity(line):
    blob = get_blob(line)
    if blob:
        return blob.sentiment.polarity
    return 0

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

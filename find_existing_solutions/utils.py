import json, itertools, csv, os
import nltk
from nltk import CFG, pos_tag, word_tokenize, ne_chunk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob, Sentence, Word, WordList

lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

from get_pos import *

''' SIMILARITY FUNCTIONS '''

def get_polarity(line):
    line_blob = get_blob(line)
    sentiment = line_blob.sentiment
    if sentiment:
        if sentiment.polarity:
            return roun(sentiment.polarity, 1)
    return 0

def correct_spelling(line):
    blob = textblob.Sentence(line)
    if blob:
        return blob.correct()
    return text

def get_subjectivity(line):
    return line

def get_definitions(word):
    defs = Word(word).definitions
    if defs:
        print('\tdefinitions', defs)
        return defs
    return False

def get_definition_keywords(word):
    ''' add option to use local_database/index (phrases, relationships) or pull from a data source '''
    defs = get_definitions(word)
    print('defs', word, defs)
    if defs:
        keywords = []
        for d in defs:
            words = d.split(' ')
            for w in words:
                keywords.append(w)
        if len(keywords) > 0:
            return keywords
    return False

''' GET STRUCTURAL TYPE FUNCTIONS '''

def get_trees(line):
    grammar_entries = ['S -> NP VP', 'PP -> P NP', 'NP -> Det N | NP PP', 'VP -> V NP | VP PP']
    tagged = pos_tag(word_tokenize(line))
    '''
    grammar_dict = {}
    for item in tagged:
        pos = item[1]
        value = item[0]
        if pos != value:
            if pos not in grammar_dict:
                grammar_dict[pos] = [value]
            else:
                grammar_dict[pos].append(value)
    for key, val in grammar_dict.items():
        if len(val) > 1 and type(val) == list:
            new_grammar_entry = ''.join([key, ' -> ', ' | '.join(val)])
            grammar_entries.append(new_grammar_entry)
    grammar_definition = '\n'.join(grammar_entries) if len(grammar_entries) > 0 else None
    print('grammar_def', grammar_definition)
    if grammar_definition:
        grammar = CFG.fromstring(grammar_definition)
        parser = nltk.ChartParser(grammar)
        for tree in parser.parse(line):
             print('tree', tree)
    '''
    trees = ne_chunk(tagged)
    # Tree('S', [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), Tree('ORGANIZATION', [('Foo', 'NNP'), ('Bar', 'NNP')]), ('sentence', 'NN'), ('.', '.')])
    print('trees', trees)
    return trees

def get_stem(word):
    stem = stemmer.stem(word)
    if stem:
        return stem 
    return word

def get_first_important_word(words, all_vars):
    for word in words:
        pos = get_pos(word, all_vars)
        if pos == 'verb' or word not in stop:
            return word
    return False

def get_blob(string):
    if type(string) == str:
        return TextBlob(string)
    return False

def get_singular(word):
    wl = WordList((word))
    singular_list = wl.singularize()
    if len(singular_list) > 0:
        for item in singular_list:
            return item
    return False

def change_to_infinitive(verb):
    infinitive = lemmatizer.lemmatize(verb, 'v')
    return infinitive

def get_pos_in_line(line, row, all_vars):
    for word in line.split(' '):
        if len(word) > 0:
            pos = get_pos(word, all_vars)
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
            docs = add_objects(paths, docs)
        else:
            paths = [''.join([database_dir, '/', fp]) for fp in os.path.listdir(path)]
            docs = add_objects(paths, docs)
    if docs:
        return docs
    return False

def add_objects(paths, docs):
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

def read(path):
    index = None
    if 'DS_Store' not in path:
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

def is_condition(asp_words, all_vars):
    first_word = get_first_important_word(asp_words, all_vars)
    if first_word:
        pos = get_pos(first_word, all_vars)
        if pos:
            if pos != 'noun':
                return first_word
    for word in asp_words:
        if word in all_vars['clause_delimiters']:
            return word
    return False

def get_delimiter(line):
    ''' get a delimiter that isnt in the line '''
    delimiter = '***' if '***' not in line else '###'
    return delimiter

def get_sentence_delimiter(text):
    return '\n' if text.count('\n') > text.count('. ') else '. '

def standardize_delimiter(text):
    blob = get_blob(text)
    if blob:
        sentences = blob.sentences
        if len(sentences) > 0:
            return '\n'.join(sentences)
    delimiter = get_sentence_delimiter(text)
    if delimiter:
        return '\n'.join(text.split(delimiter))
    return False

def standard_text_processing(text, all_vars):
    text = space_punctuation(text.strip())
    text = remove_stopwords(text)
    replaced_text = replace_syns(text, 'all', all_vars)
    text = replaced_text if replaced_text else text
    return text

def split_by_delimiter(line, all_vars):
    words = []
    word = []
    delimiters = [] 
    for char in line:
        if char in all_vars['alphabet']:
            word.append(char)
        else:
            delimiters.append(char)
            words.append(''.join(word))
            word = []
    if len(word) > 0:
        words.append(''.join(word))
    return words, delimiters

def space_punctuation(line):
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
    line = line.replace('[', ' ( ').replace(']', ' ) ').replace("'", '') # remove contraction & possession apostrophes
    line = line.replace(':', ' , ').replace(';', ' , ') # replace clause punctuation with comma
    line = line.replace(',', ' , ').replace('  ', ' ')
    return line

def select_option(alt_phrase):
    ''' 
        this function translates:
        - expression/activity = expression-activity (different pos = phrase)
        - describes/delineates = describes (same pos, if synonym, choose more common one)
    '''
    delimiter = [c for c in '/|' if c in alt_phrase]
    alts = alt_phrase.split(delimiter)
    alt_pos = [get_pos(a, all_vars) for a in alts]
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

def get_meaning_score(phrase, line):
    '''
    this should return 0 for phrases 
    that dont change the meaning of the sentence
    (mostly any phrase without a verb) 
    '''
    meaning = 0
    if meaning:
        return meaning
    return False

def remove_stopwords(line):
    ''' this should remove all excessive language where phrases or clauses dont add meaning
    - common nouns ("associate", "multi-resolution", "delicate")
    - also proper noun names: 'M.D.'
    - remove plural form of duplicate objects in sets
    '''

    ''' to do: add semantic & keyword equivalence checks '''
    custom_removal = [] #['the', 'a', 'an', 'them', 'they']
    words = line.split(' ') if type(line) == str else line
    word_list = []
    for w in words:
        if '/' in w or '|' in w:
            option = select_option(w)
            if option:
                word_list.append(option)
        else:
            if w not in stopwords.words('english') and w not in custom_removal:
                word_list.append(w)
    return ' '.join(word_list)

def get_ngrams(word_list, word, x, direction):
    ''' 
    get a list of words in word list starting with word 
    and iterating outward in direction x number of times 
    to do: use blob.ngrams(n=x)
    '''
    list_length = len(word_list)
    word_index = word_list.index(word)
    if word_index:
        start = word_index - x if word_index > x else word_index if direction == 'next' else 0
        end = word_index + x if (word_index + x) < list_length else word_index if direction == 'prev' else list_length
        return word_list[start:end]
    return False

def get_phrases(line, all_vars):
    ''' to do: use all_vars['pos_tags']['phrase'] = ['PP', 'NNP', 'VP'] '''
    phrases = set()
    blob = get_blob(line)
    if blob:
        for p in blob.noun_phrases:
            phrases.add(p)
    if len(phrases) > 0:
        return phrases
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
    return word

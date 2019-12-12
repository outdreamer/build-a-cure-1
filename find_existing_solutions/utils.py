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
    definitions = Word(word).define(NOUN)
    print('define', word, definitions)
    defs = Word(word).definitions
    if defs:
        print('\tdefinitions', word, defs)
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
    trees = ne_chunk(tagged)
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
    ''' get first synset name '''
    infinitive = lemmatizer.lemmatize(verb, 'v')
    return infinitive

def get_new_key(key_dict, all_vars):
    new_key = None
    upper_limit = len(all_vars['alphabet']) - 1
    random_index = random.randint(0, upper_limit)
    random_letter = all_vars['alphabet'][random_index]
    if key_dict:
        for k in key_dict:
            new_key = ''.join([k, random_letter])
    else:
        new_key = random_letter
    if new_key:
        if new_key in key_dict:
            return get_new_key(key_dict, all_vars)
        else:
            return new_key
    return False 

def replace_names(row, all_vars):
    # to do: identify all irrelevant proper nouns like place, company, university & individual names
    original_words = row['original_line'].split(' ')
    tagged = pos_tag(word_tokenize(row['line']))
    ''' to do: make sure names are grouped into phrases '''
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
                        if name in original_words:
                            new_name.append(name)
            if len(new_name) > 0:                                         
                final_name = ' '.join(new_name)
                if len(new_name) == len(phrase_words):
                    if final_name != row['line'][0:len(final_name)]:
                        if final_name.lower() not in row['nouns']:
                            if final_name.lower() not in row['verbs']:
                                row['names'].add(final_name) # find names and store separately
    row['line'] = ' '.join([w for w in row['line'].split(' ') if w not in row['names']])
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

def get_pos_metadata(line, row, all_vars):
    ''' to do: nouns with highest counts are likely to be central objects '''
    ''' takes out determiners if indicating 'one', 'some', or 'same' quantity '''
    keep_ratios = ['extra', 'high', 'none']
    row = row if row else get_empty_index(None, all_vars)
    words = line.split(' ')
    for i, word in enumerate(words):
        if len(word) > 0:
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
            pos = get_pos(word, all_vars)
            if pos == 'verb':
                ''' to do: standardize verbs before adding them - this will make some patterns invalid '''
                # word = change_to_infinitive(word)
                row['verbs'].add(word)
            elif pos == 'noun':
                row['nouns'].add(word)
            else:
                nltk_pos = get_nltk_pos(word)
                if nltk_pos in all_vars['pos_tags']['det']:
                    ratio = get_determiner_ratio(word)
                    if ratio:
                        if ratio in keep_ratios:
                            other_word = words[i + 1] if (i + 1) < len(words) else words[i - 1] if i > 0 else None
                            if other_word:
                                row['modifiers'].add(' '.join([ratio, other_word]))
                row['taken_out'].add('_'.join([word, pos]))
    if len(row['counts']) > 0:
        common_words = get_most_common_words(row['counts'], 3) # get top 3 tiers of common words
        if common_words:
            row['common_words'] = row['common_words'].union(common_words)
    blob = get_blob(line)
    if blob:
        noun_phrases = blob.noun_phrases
        if noun_phrases:
            row['noun_phrases'] = noun_phrases
    return row

def get_most_common_words(counts, top_index):
    '''
    counts = {
        0: ['words', 'that', 'appeared', 'once'],
        1: ['items', 'shown', 'twice']
    }
    '''
    count_keys = counts.keys()
    if len(counts.keys()) > 0:
        sorted_keys = reversed(sorted(count_keys))
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

def standard_text_processing(text, all_vars):
    text = concatenate_species(text.strip())
    text = standardize_delimiter(text)
    text = standardize_punctuation(text)
    text = remove_stopwords(text)
    new_lines = []
    for line in text.split('\n'):
        line = replace_quotes_with_parenthesis(line)
        new_line = convert_to_active(line)
        if new_line:
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    if len(new_lines) > 0:
        text = '\n'.join(new_lines)
    text = replace_with_syns(text, 'all', all_vars)
    return text

def replace_with_syns(text, element, all_vars):
    new_text = []
    for w in text.split(' '):
        word = ''.join([x for x in w if x == '-' or x == ' ' or x in all_vars['alphabet']]) # some synonyms have dashes and spaces
        check_types = ['synonym', 'common', 'standard', 'similarity']
        # dont add stem-similarity replacement bc you still need pos identification
        match, check_type, all_vars = find_matching_synonym(word, check_types, None, all_vars)
        if match and check_type:
            new_text.append(w.replace(word, match))
        else:
            new_text.append(w)
    if len(new_text) > 0:
        return ' '.join(new_text)
    return text, all_vars

def standardize_punctuation(line):
    # remove apostrophes, replace brackets with parenthesis
    line = line.replace('[', ' ( ').replace(']', ' ) ').replace("'", '') 
    # replace clause punctuation with comma
    line = line.replace(' - ', ' , ')
    operator_keys = all_vars['operator_map'].keys()
    for k in operator_keys:
        line = line.replace(k, '')
    # space comma to avoid conflation with words, then replace double spaces
    line = line.replace(',', ' , ').replace('  ', ' ')
    return line

def remove_stopwords(line):
    custom_removal = [] #['the', 'a', 'an', 'them', 'they']
    words = line.split(' ') if type(line) == str else line
    word_list = []
    for w in words:
        if '/' in w or '|' in w:
            option = select_option(w)
            if option:
                word_list.append(option)
        else:
            if w[-1] == 's':
                w = get_singular(w)
            if w not in stopwords.words('english') and w not in custom_removal:
                word_list.append(w)
    return ' '.join(word_list)

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

def get_charge_of_word(word, all_vars):
    if word in all_vars['supported_synonyms']:
        synonym = all_vars['supported_synonyms'][word]
        for synonym_type in all_vars['charge']:
            if synonym in all_vars['charge'][synonym_type]:
                print('get_charge_of_word: found synonym charge', word, synonym, synonym_type)
                return synonym_type
    return False

def get_similarity(base_word, new_word, pos_type, all_vars):
    pos_lib_map = { 'noun': NOUN, 'verb': VERB, 'adv': ADV, 'adj': ADJ }
    if pos_type in pos_lib_map:
        pos_type = pos_lib_map[pos_type]
        base_synsets = Word(base_word).get_synsets(pos=pos_type)
        new_synsets = Word(new_word).get_synsets(pos=pos_type)
        if len(new_synsets) > 0 and len(base_synsets) > 0:
            similarity = base_synsets.path_similarity(new_synsets)
            print('\tget similarity', new_synsets, base_synsets, similarity)
            return similarity
    return 0

def get_similarity_to_title(line, title, row):
    similarity = 0
    if line != title:
        title_split = title.split(' ')
        both = set()
        for s in string.split(' '):
            if s in title_split:
                both.add(s)
        if len(both) > 0:
            similarity = round(len(both) / len(title_split), 1)
        if similarity
            row['similarity'] = similarity
    return row

def get_meaning_score(phrase, line):
    '''
    this should return 0 for phrases 
    that dont change the meaning of the sentence
    (mostly any phrase without a verb) 
    lines with more variation between words & compared to intent are more meaningful
    '''
    meaning = 0
    if meaning:
        return meaning
    return False

def get_phrases(line, row, all_vars):
    ''' to do: use all_vars['pos_tags']['phrase'] = ['PP', 'NNP', 'VP'] '''
    ''' rather than just noun_phrases, we want to identify any phrases '''
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

def convert_to_active(line):
    '''
    active test cases:
    
    - "protein that modulates a signaling pathway" => "signaling pathway-changing protein" 
        pattern = "A were subjected to B induced by C of D"
        pattern_with_pos = "A were subjected to B induced by C of D"

    - "Rats were subjected to liver damage induced by intra-peritoneal injection of thioacetamide" => 
        "intra-peritoneal thioacetamide injection induced liver damage in rats"
        noun_phrases for this would be "intra-peritoneal thioacetamide injection", "liver damage" and "rats"
    
    - "chalcone isolated from Boesenbergia rotunda rhizomes" => "Boesenbergia rotunda rhizomes isolate chalcone"

    keep in mind:
        if you standardize "injection of thioacetamide" to "thioacetamide injection", 
        your other pattern "x of y" configuration wont be necessary, 
        so remove that pattern once youve tested apply_pattern_map

    - check for verb tenses normally used in passive sentences # had been done = past perfect
    - translate questions into statements of intent:
        "would there be an effect of x on y?"
        intent = "evaluate relationship between x and y" 
    - active: x  -  did  -  this and then y  -  did  -  z
    - passive: this  -  was done  -  by x and then z  -  was done  -  by y
    '''
    active_line = apply_pattern_map(line, all_vars['pattern_maps']['passive_to_active'])
    if active_line:
        return active_line
    return line

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
            paths = [''.join([database_dir, '/', fp]) for fp in os.path.listdir(path)]
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
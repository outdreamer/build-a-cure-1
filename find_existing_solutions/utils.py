import json, itertools, csv, os
import nltk
from nltk import pos_tag, word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob

lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

from get_pos import *

''' SIMILARITY FUNCTIONS '''

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

def get_definitions(word):
    defs = Word(base_word).definitions
    if defs:
        print('\tdefinitions', defs)
        return defs
    return False

def get_definition_keywords(word):
    ''' add option to use local_database/index (phrases, relationships) or pull from a data source '''
    defs = get_definitions(word)
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
    print('getting trees for line', line)
    grammar_entries = ['S -> NP VP', 'PP -> P NP', 'NP -> Det N | NP PP', 'VP -> V NP | VP PP']
    tagged = pos_tag(word_tokenize(line)) # [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('Foo', 'NNP'), ('Bar', 'NNP'), ('sentence', 'NN'), ('.', '.')]
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

def get_metrics(line):
    '''
    find any metrics in this line
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information
    '''
    metrics = set()
    split_line = line.split(' ')
    for i, word in enumerate(split_line):
        numbers = [w for w in word if w.isnumeric()]
        if len(numbers) > 0:
            if len(numbers) == len(word):
                next_word = split_line[i + 1] if (i + 1) < len(split_line) else ''
                if len(next_word) < 5:
                    # to do: add extra processing rather than assuming its a unit of measurement
                    metrics.add(word)
                    metrics.add(next_word) # '3 mg'
            else:
                metrics.add(word) # '3mg'
    return metrics

def get_modifier(words, row, all_vars):
    if ' '.join(words) not in row['phrases']:
        modifier = None
        modified = None
        modifier_substrings = ["or", "er", "ed", "ing"]       
        for word in words:
            for m in modifier_substrings:
                split = word.split(m)
                if split[-1] == m:
                    modifier = word
        return modified, modifier
    return False, False
    
def get_modifiers(words, row, all_vars):
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
    for pattern in all_vars['pattern_index']['modifier']:
        subsets = get_source_wordsets_for_pattern(' '.join(words), pattern)
        if subsets:
            for subset in subsets:
                modified, modifier = get_modifier(subset, row, all_vars)
                if modified and modifier:
                    modifier_sets.append(' '.join([modified, modifier]))
    word_range = 3 if len(words) > 5 else 2 if len(words) > 3 else 1
    for i in range(0, word_range):
        subset = get_subset_of_list(words, word, i, 'both')
        modified, modifier = get_modifier(subset, row, all_vars)
        if modified and modifier:
            modifier_sets.append(' '.join([modified, modifier]))
    if len(modifier_sets) > 0:
        return modifier_sets
    return False

def get_delimiter(line):
    ''' get a delimiter that isnt in the line '''
    delimiter = '***' if '***' not in line else '###'
    return delimiter

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
                if object_type not in docs:
                    docs[object_type] = []
                docs[object_type].append(contents)
    return docs

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
    if 'DS_Store' not in path:
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

''' WORD REMOVAL FUNCTIONS '''

def standard_text_processing(text, all_vars):
    text = space_punctuation(text.strip())
    text = remove_stopwords(text)
    replaced_text = replace_syns(text, 'all', all_vars['supported_core'])
    text = replaced_text if replaced_text else test
    return text       

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
            exit()
        # now all quote content should be surrounded by parentheses instead
        line = ' '.join(new_line) if len(new_line) > 0 else line
    line = line.replace('[', ' ( ').replace(']', ' ) ').replace("'", '') # remove contraction & possession apostrophes
    line = line.replace(':', ' , ').replace(';', ' , ') # replace clause punctuation with comma
    line = line.replace(',', ' , ').replace('  ', ' ')
    return line

def rearrange_sentence(line, all_vars):
    '''
    this function is to position your sentence clauses in the same pattern
    this means fulfilling the following expectations:
    - having conditionals at the end rather than the beginning
    so a sentence like: 
        "in the event of onset, symptoms appear at light speed, even if you take vitamin c at the max dose"
    is reduced to:
        "symptoms appear quickly even with vitamin c max dose"
    '''
    split = line.split(',')
    clauses = get_clauses(line)
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

def get_subset_of_list(word_list, word, x, direction):
    ''' 
    get a list of words in word list starting with word 
    and iterating outward in direction x number of times 
    '''
    list_length = len(word_list)
    word_index = word_list.index(word)
    if word_index:
        start = word_index - x if word_index > x else word_index if direction == 'next' else 0
        end = word_index + x if (word_index + x) < list_length else word_index if direction == 'prev' else list_length
        return word_list[start:end]
    return False

def get_phrases(line):
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

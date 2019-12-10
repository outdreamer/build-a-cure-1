import json, itertools, csv
import nltk
from nltk import pos_tag, word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob

lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

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

def change_to_infinitive(verb):
    infinitive = lemmatizer.lemmatize(verb, 'v')
    print('infinitive', infinitive)
    return infinitive

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
    passive = 0
    keywords = []
    for pattern in all_vars['pattern_index']['passive']:
        found = find_pattern(line, pattern, keywords)
        if found:
            if len(found) > 0:
                passive += len(found)
        passive += len(keywords_found)
    if passive > 2:
        return False
    return True

def get_modified_word(operator_clause, nouns, modifier):
    ''' to do: this will fail if you removed the modified word or put it in the next clause '''
    print('get_modified_word: operator_clause', operator_clause, 'modifier', modifier)
    split_clause = operator_clause.strip().split(modifier)
    if len(split_clause) > 1:
        prev_word = split_clause[0].split(' ')[-1]
        next_word = split_clause[1].split(' ')[0]
        prev_pos = get_pos(prev_word) if prev_word not in ['+', '-', '='] else ''
        next_pos = get_pos(next_word) if next_word not in ['+', '-', '='] else ''
        if prev_pos == 'noun':
            return prev_word
        elif next_pos == 'noun':
            return next_word
        else:
            ''' apply same logic but get next object & previous object '''
    return False
    
def get_modifier(prev_word, word, next_word):
    '''
    to do: finish get_modifier logic
    for j, word in enumerate(words):
        prev_word = words[j - 1] if j > 0 else False
        next_word = words[j + 1] if j < (len(words) - 1) else False
        is_modifier = get_modifier(prev_word, word, next_word)
        if is_modifier:
            modified_word = get_modified_word(line, word)
            if modified_word:
                variables[new_key] = [word, 'of', modified_word]
                placeholder_clause.append(new_key)
        else:
            variables[new_key] = word
            placeholder_clause.append(new_key)
    '''
    '''
    if this is a modifier, return True 
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
    stem_pos = get_pos(get_stem(word))
    if stem_pos in ['VBP', 'VBD', 'VBN', 'VBZ', 'VBG'] and modifier_pos in ['NN', 'JJ', 'JJR', 'NNS', 'NNP', 'NNPS', 'RB']:
        modifier_score += 1
    for m in modifier_substrings:
        if m in word:
            index = len(word) - len(m) - 1
            if word[index:] == m:
                modifier_score += 1
    keywords = []
    for pattern in modifier_patterns:
        found = find_pattern(word, pattern, keywords)
        if found:
            modifier_score += 1
    if modifier_score > 3:
        return True
    return False

''' STORAGE FUNCTIONS '''

def get_local_database(path, objects):
    docs = {}
    if not os.path.exists(path) or not os.path.isdir(path):
        cwd = getcwd()
        path = ''.join([cwd, '/', path])
    if os.path.exists(path) and os.path.isdir(path):
        if len(objects) == 0:
            for file_path in os.path.listdir(path):
                full_path = '/'.join([path, file_path])
                object_type = file_path.replace('.txt','')
                if os.path.isfile(full_path):
                    contents = read(full_path)
                    if contents:
                        if object_type not in docs:
                            docs[object_type] = []
                        docs[object_type].append(contents)
        else:
            for object_type in objects:
                full_path = ''.join([path, '/', object_type, '.txt'])
                if os.path.isfile(full_path):
                    contents = read(full_path)
                    if contents:
                        if object_type not in docs:
                            docs[object_type] = []
                        docs[object_type].append(contents)
    if docs:
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


''' WORD REMOVAL FUNCTIONS '''

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

def rearrange_sentence(line):
    '''
    this function is to format your sentences in the same way

    this means fulfilling the following expectations:
    - having conditionals at the end rather than the beginning
    - standardized words
    - simplified language where clearly mappable

    so a sentence like: 
    "in the event of onset, symptoms appear at light speed, even if you take vitamin c at max dose"

    is reduced to:
    "symptoms appear even with vitamin c max dose"
    '''
    return line

def remove_names(line, names_list):
    '''
    # to do: remove all irrelevant proper nouns like place, company, university & individual names
    if row:
        if 'names' in row:
            for name in row['names']:
                line = line.replace(name, '') 
    '''
    return line
    
def remove_unnecessary_words(line, phrases, clauses):
    ''' this should remove all excessive language where phrases or clauses dont add meaning
    - common nouns ("associate", "multi-resolution", "delicate", "order", "disorders", "expression/activity")
    - also proper noun names: ''M.D..''
    - remove plural form of duplicate objects in sets
    - make sure this is the same line in functions: expression/activity
    '''

    return line

def remove_stopwords(line):
    ''' to do: add semantic & keyword equivalence checks '''
    custom_removal = [] #['the', 'a', 'an', 'them', 'they']
    words = line.strip().split(' ') if type(line) == str else line
    word_list = [w for w in words if w not in stopwords.words('english') and w not in custom_removal]
    return ' '.join(word_list)

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

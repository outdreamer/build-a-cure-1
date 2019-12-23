import wikipedia
from wikipedia.exceptions import DisambiguationError
import xml.dom.minidom

from get_pos import *
from get_type import *
from get_vars import *
from get_medical_objects import *
from get_structural_objects import *
from get_conceptual_objects import *

def get_data_store(index, database, operation, args):
    '''
    this assembles an index or retrieves it from local storage,
    filtering by object_types found in the metadata argument
    '''
    downloaded = downloads(['data', 'datasets'])
    if not downloaded:
        return False
    av = get_vars()
    if av:
        data_store = {}
        ''' if index or database not passed in, fetch the local db if it exists '''
        args, filters, metadata, generate_target, generate_source = get_args(args, av)
        av['metadata'] = metadata if metadata else av['supported_params']
        if operation == 'build':
            database = get_local_database('data', None) if not database else database
            data_store, rows = build_indexes(database, args, filters, av)
        elif operation == 'get_database':
            data_store = get_local_database('data', None)
        elif operation == 'get_index':
            data_store = index
        if data_store and metadata:
            new_index = {}
            for key in metadata:
                new_index[key] = data_store[key] if key in data_store else set()
            if new_index:
                return new_index
    return False

def get_data_from_source(source, keyword, av):
    data = {}
    total = 0
    max_count = 10
    for i in range(0, 10):
        start = i * max_count
        if total > start or total == 0:
            url = source['url'].replace('<KEY>', keyword).replace('<START>', str(start)).replace('<MAX>', str(max_count))
            print('url', url)
            response = requests.get(url)
            if response.content:
                articles = {}
                if source['response_format'] == 'xml':
                    xml_string = xml.dom.minidom.parseString(response.content)
                    if xml_string:
                        count_tag = xml_string.documentElement.getElementsByTagName(source['count'])
                        total = int(count_tag[0].childNodes[0].nodeValue)
                        articles = xml_string.documentElement.getElementsByTagName(source['entries'])
                else:
                    articles = json.loads(response.content)
                if len(articles) > 0:
                    data = process_articles(entries, data, source, av)
    if data:                                         
        return data
    return False

def process_articles(articles, data, source, av):
    for article in articles:
        title = get_text_from_nodes(article, source['title_element'])
        article_text = get_text_from_nodes(article, source['summary_element'])
        if title and article_text:
            article_lines, av = standard_text_processing(article_text, av)
            if article_lines:
                data[title] = article_lines # article_lines[line][word] = pos
    return data

def get_text_from_nodes(entry, element_name):
    nodes = [node for node in entry.childNodes if node.nodeName == element_name]
    if len(nodes) > 0:
        text = ''.join([subnode.wholeText for node in nodes for subnode in node.childNodes])
        if len(text) > 0:
            return text
    return False

def add_row(row, index, empty_index, rows):
    if row:
        if row != empty_index:
            for key, val in row.items():
                if type(val) == dict:
                    row[key] = '::'.join(['_'.join([k,v]) for k,v in val.items()])
                elif type(val) == set or type(val) == list:
                    row[key] = str('::'.join(set(val)))
                elif type(val) == bool:
                    row[key] = '1' if val is True else '0'
                index[key] = index[key].add(row[key])
            rows.append(row)
    return index, rows

def build_indexes(database, args, filters, av):
    ''' 
    - this function indexes data from api providing articles
    - if the local database is found, use that as starting index, otherwise build it
    '''
    rows = []
    empty_index = get_empty_index(av)
    index = database if database else empty_index if empty_index else None
    for arg in args:
        for source in av['sources']:
            data = get_data_from_source(source, arg, av)
            if data:
                for title, article_lines in data.items():
                    for line, word_map in article_lines.items():
                        row = get_metadata(line, title, word_map, av)
                        if row:
                            index, rows = add_row(row, index, empty_index, rows)
    if index and rows:
        for key in index:
            if key != 'rows':
                ''' get the patterns in each index we just built & save '''
                for row in rows:
                    objects, patterns = extract_objects_and_patterns_from_index(index, row, key, None, av)
                    #to do: patterns = get_patterns_between_objects(index[key], key, av)
                    # get patterns for index[key] objects with object_type key
                    if patterns:
                        if len(patterns) > 0:
                            object_patterns = [''.join([k, '_', '::'.join(v)]) for k, v in patterns.items()] # 'pattern_match1::match2::match3'
                            object_pattern_name = ''.join(['data/patterns_', key, '.txt']) 
                            index[object_pattern_name] = '\n'.join(object_patterns)
                    save(''.join(['data/pk_', key, '.txt']), '\n'.join(index[key]))
            else:
                write_csv(rows, index.keys(), 'data/rows.csv')
        return index, rows
    return False, False

def get_metadata(line, title, word_map, av):
    ''' 
    this function initializes the row object & populates it with various metadata types:
        - structural_types to get nouns, verbs, phrases, modifiers, clauses, & relationships
        - medical_types to get conditions, symptoms, & treatments in the sentence 
        - conceptual_types to get types, strategies & insights
    '''
    row = get_empty_index(av)                   
    row['line'] = line
    row['word_map'] = word_map
    row['original_line'] = line
    row = replace_names(row, av)
    row = get_similarity_to_title(title, row)  
    print('\ngetting structural metadata for line', line)
    row = get_structural_metadata(row, av)
    print('\nrow with structural metadata', row)
    intent = None # find_intent(row, av)
    hypothesis = None # find_hypothesis(row, av)
    row = find_treatment(row['line'], None, row, av)
    for metadata_type in ['medical_types', 'conceptual_types']:
        for object_type in av[metadata_type]:
            if object_type in av['metadata']:
                for search_pattern_key in av['pattern_index']:
                    # check that this data 'strategy', 'treatment' was requested and is supported in pattern_index
                    objects, patterns = extract_objects_and_patterns_from_index(index, row, object_type, search_pattern_key, av)
                    if objects:
                        row[object_type] = objects
                    if patterns:
                        row['pattern'] = row['pattern'].union(set([p for p in patterns]))
    print('\nmedical objects', row)
    return row

def extract_objects_and_patterns_from_index(index, row, object_type, search_pattern_key, av):
    '''
    - all of your 'find_object' functions need to support params: pattern, matches, row, av

    - this function is for meta-analysis

        1. find any matches from search_pattern_key patterns in index[object_type]/row[object_type] lines
        2. if pattern matches found in lines, 
            find objects in matches with type-specific logic from find_<object_type> function
        3. if no pattern matches found in lines, 
            find objects in lines with type-specific logic from find_<object_type> function

        for an index or row containing types of elements ('condition', 'symptom', 'strategy')
        this function is for finding patterns in those index types in the input (index or row['line'])

    - object_type is the key in object types supported in av['full_params'] to find:
        ['treatment', 'condition', 'strategy']

    - search_pattern_key is the key of av['pattern_index'] keys to search: 
        ['modifier', 'type', 'role']

    - object_type can equal search_pattern_key

    '''
    if index or row:
        lines = [row['line']] if row and 'line' in row else []
        if not index:
            index = row
        if index:
            if object_type in index and object_type in av['metadata']:
                lines = index[object_type]
                if len(index[object_type]) > 0:
                    patterns = {}
                    objects = { object_type: set() }
                    print('index search_pattern_key', search_pattern_key)
                    print('search index lines', index[object_type])
                    for line in lines:
                        found_objects_in_patterns, found_patterns, av = get_patterns_and_objects_in_line(line, search_pattern_key, index, object_type, av)
                        if found_objects_in_patterns:
                            objects[object_type] = found_objects_in_patterns
                        if found_patterns:
                            patterns = found_patterns
                        else:
                            ''' 
                            if there are no matches found for object_type patterns, 
                            do a standard object query independent of patterns to apply type-specific logic 
                            '''
                            found_objects = apply_find_function(object_type, None, [line], index, av)
                            if found_objects:
                                objects[object_type] = found_objects
                    if objects or patterns:
                        print('extracted', objects, patterns)
                        return objects, patterns
    return False, False

def get_patterns_and_objects_in_line(line, search_pattern_key, index, object_type, av):
    ''' the reason we allow search_pattern_key and object_type to differ is to find subset matches 
        example: 
            find 'modifiers' in 'treatment patterns' would have:
            object_type = 'modifier' and search_pattern_key = 'treatment'
        to do:
            - make a list of subset pattern type relationships
    '''
    found_objects = set()
    found_patterns, av = match_patterns(line, search_pattern_key, av)
    if found_patterns and object_type != 'pattern':
        print('found patterns', found_patterns)
        for pattern_type in found_patterns:
            for pattern, matches in found_patterns[pattern_type].items():
                ''' filter pattern matches for this type before adding them, with type-specific logic in find_* functions '''
                ''' note: this is not restricting output to found objects '''
                found_objects = apply_find_function(object_type, pattern, matches, index, av)
                print('found objects', found_objects)
    if len(found_objects) > 0 or found_patterns:
        return found_objects, found_patterns, av
    return False, False, av

def apply_find_function(object_type, pattern, matches, index, av):
    ''' find functions check for objects of object_type in matches list which match pattern 
        - all find object functions need to support params:
            - pattern, matches_lines, row_index, av
              pattern & subsets matching pattern
                - pattern = 'x of y'
                - lines = 'dog of cat', 'cat of dog' 
              no pattern passed in, just lines array
                - pattern = None
                - lines = ['find the objects in this sentence']
    '''
    function_name = ''.join(['find_', object_type])
    if function_name in globals():
        try:
            function = getattr(globals(), function_name)
            print('found function', function)
            if function:
                got_objects = function(pattern, matches, index, av)
                if got_objects:
                    if len(got_objects) > 0:
                        return set([item for item in got_objects])
        except Exception as e:
            # print('e', e)
            return False
    return False

def get_structural_metadata(row, av):
    '''
        1. 'ngram', 'modifier', 'phrase', 'noun_phrase', 'verb_phrase', 'clause', 'subject', 'pattern',
        2. order_and_convert_clauses
        3. 'relationship'

        verb-noun-phrases should be converted into modifiers
        once you have the nouns/modifiers, you can pick a subject from the noun or modifier
    '''
    generated_patterns, av = get_all_versions(row['line'], 'all', av) 
    if generated_patterns:
        row['pattern'][row['line']] = set(generated_patterns)
    print('get_structural_metadata: got patterns for line', row['line'])
    print(row['pattern'])
    keep_ratios = ['extra', 'high', 'none']
    line = row['line'] if 'line' in row and type(row) == dict else row # can be a row index dict or a definition line
    row = row if type(row) == dict else get_empty_index(['all'], av)
    row['line'] = line
    word_pos_line = ''.join([x for x in line if x in av['alphanumeric'] or x in av['clause_analysis_chars']])
    words = word_pos_line.split(' ')
    for i, w in enumerate(words):
        if len(w) > 0:
            count = words.count(w)
            w_upper = w.upper()
            w_name = w.capitalize() if w.capitalize() != words[0] else w
            upper_count = words.count(w_upper) # find acronyms, ignoring punctuated acronym
            if count > 0:
                count_num = upper_count if upper_count >= count else count
                count_val = w_upper if upper_count >= count else w 
                if count_num not in row['count']:
                    row['count'][count_num] = set()
                row['count'][count_num].add(count_val)
            pos = row['word_map'][w] if w in row['word_map'] else False
            if pos:
                ''' favor noun before verb '''
                if pos in av['tags']['VC']:
                    row['clause_marker'].add(w)
                if pos in av['tags']['ALL_N'] or w in av['alphabet']:
                    ''' format nouns like 'inhibitor' as a verb '''
                    stem = get_stem(w)
                    stem_pos = get_nltk_pos(stem, av)
                    if stem_pos:
                        present_verb = conjugate(w, stem_pos, 'VBZ', av)
                        if present_verb:
                            row['verb'].add(present_verb)
                    else:
                        row['noun'].add(w)
                elif pos in av['tags']['ALL_V']:
                    ''' dont conjugate '-ing' to preserve verb-noun modifier phrases '''
                    if pos != 'VBG':
                        present_verb = conjugate(w, pos, 'VBZ', av)
                        if present_verb:
                            row['verb'].add(present_verb)
                        else:
                            row['verb'].add(w)
                    else:
                        row['verb'].add(w)
                elif pos in av['tags']['D']:
                    ratio = get_determiner_ratio(w)
                    if ratio:
                        if ratio in keep_ratios:
                            row['det'].add(str(ratio))
                elif pos in av['tags']['P']:
                    row['prep'].add(w)
                elif pos in av['tags']['C']:
                    row['conj'].add(w)
                elif pos in av['tags']['ADV'] or pos in av['tags']['ADJ']:
                    row['descriptor'].add(w)
                else:
                    row['taken_out'].add('_'.join([w, str(pos)]))
    if len(row['count'].keys()) > 1:
        common_words = get_most_common_words(row['count'], 3) # get top 3 tiers of common words
        if common_words:
            row['common_word'] = common_words
    ngrams = find_ngrams(word_pos_line, av) # 'even with', 'was reduced', 'subject position'
    if ngrams:
        row['ngram'] = ngrams
        ngram_list = [v for k, v in ngrams.items()]
        ngram_list.append(word_pos_line)
        structure_types = ['modifier', 'verb_phrase', 'noun_phrase', 'phrase', 'clause']
        for i, key in enumerate(structure_types):
            objects, patterns = extract_objects_and_patterns_from_index(row, None, key, key, av)
            if objects:
                if key in objects:
                    if key == 'verb_phrase':
                        for item in objects[key]:
                            for w in item.split(' '):
                                pos = get_nltk_pos(w, av)
                                if pos:
                                    present_verb = conjugate(w, pos, 'VBZ', av)
                                    if present_verb:
                                        row[key].add(present_verb)
                                    else:
                                        row[key].add(w)
                    elif key == 'subject':
                        for item in objects[key]:
                            row[key].add(item.split(' ')[0]) # get first word in 'N V' subject pattern
                    else:
                        row[key] = row[key].union(set(objects[key]))
            if patterns:
                row['pattern'] = row['pattern'].union(set(patterns))
    extra_patterns = find_pattern(row['line'], av)
    if extra_patterns:
        row['pattern'] = row['pattern'].union(set(extra_patterns))
    row = find_relationship(row, av)
    objects, patterns = extract_objects_and_patterns_from_index(row, None, 'relationship', 'relationship', av)
    if objects:
        if 'relationship' in objects:
            row['relationship'] = row['relationship'].union(set(objects['relationship']))
        if patterns:
            row['pattern'] = row['pattern'].union(set(patterns))
    for key in row:
        print('key', key, row[key])
    return row

def find_ngrams(line, av):
    phrases = {'N': [], 'V': [], 'ADJ': [], 'ADV': [], 'DPC': []} # take out adj & adv
    phrase_keys = ['N', 'V', 'ADJ', 'ADV']
    tags = av['tags']
    non_dpc_segments = []
    new_segment = []
    for w in line.split(' '):
        pos = get_nltk_pos(w, av)
        if pos:
            if pos in tags['ALL_V'] or pos in tags['ALL_N'] or pos in tags['ADV'] or pos in tags['ADJ']:
                new_segment.append(w)
            else:
                non_dpc_segments.append(' '.join(new_segment))
                new_segment = []
    if len(non_dpc_segments) > 0:
        for non_dpc_segment in non_dpc_segments:
            for key in phrase_keys:
                pos_phrases = get_ngrams_of_type(key, non_dpc_segment, av)
                if pos_phrases:
                    phrases[key] = pos_phrases
    dpc_phrases = get_ngrams_of_type('DPC', line, av)
    if dpc_phrases:
        phrases['DPC'] = dpc_phrases
    if phrases:
        return phrases
    return False

def get_ngrams_of_type(pos_type, line, av):
    all_pos_type = ''.join(['ALL_', pos_type])
    pos_type = all_pos_type if all_pos_type in av['tags'] else pos_type
    if pos_type in av['tags']:
        words = line.split(' ')
        ngrams = get_ngram_combinations(words, 5) # hydrolyzing radioactive catalyzing potential isolates
        phrases = []
        ngrams = ngrams if ngrams else [' '.join(words)]
        for n in ngrams:
            ngram_phrase = []
            for word in n:
                word_pos = get_nltk_pos(word, av)
                if word_pos:
                    if word_pos in av['tags'][pos_type]:
                        ngram_phrase.append(word)
            if len(ngram_phrase) > 1:
                ''' skip ngrams of length 1 '''
                joined_phrase = ' '.join(ngram_phrase)
                if joined_phrase not in phrases:
                    phrases.append(joined_phrase)
        if len(phrases) > 0:
            return phrases
    return False

def get_ngram_combinations(word_list, x):
    if x > 0 and x < len(word_list):
        grams = []
        combinations = itertools.combinations(word_list, x)
        for c in combinations:
            gram = [w for w in c]
            if len(gram) > 0:
                phrase = ' '.join(gram)
                if phrase in ' '.join(word_list):
                    grams.append(gram)
        if len(grams) > 0:
            return grams
    return False

if sys.argv:
    index = get_data_store(None, None, 'build', sys.argv)
    print('get_data_store:index', index)

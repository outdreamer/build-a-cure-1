import sys, json, os, re, urllib, csv, ssl, random
import wikipedia
from wikipedia.exceptions import DisambiguationError
import xml.dom.minidom
import requests

from utils import *
from get_index_def import get_empty_index
from get_vars import get_vars, get_args
from get_patterns import find_patterns
#from get_objects import *
from get_structural_objects import *
from get_conceptual_objects import *
from get_medical_objects import *
from get_type import *


def get_data_store(index, database, operation, args):
    '''
    this assembles an index or retrieves it from local storage,
    filtering by object_types found in the metadata argument
    '''
    downloaded = downloads(['data', 'datasets'])
    if not downloaded:
        return False
    all_vars = get_vars()
    if all_vars:
        data_store = {}
        ''' if index or database not passed in, fetch the local db if it exists '''
        args, filters, metadata, generate_target, generate_source = get_args(args, all_vars)
        if operation == 'build':
            database = get_local_database('data', None) if not database else database
            data_store, rows = build_indexes(database, metadata, args, filters, all_vars)
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

def get_data_from_source(source, keyword, all_vars):
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
                    data = process_articles(entries, data, source, all_vars)
    if data:                                         
        return data
    return False

def process_articles(articles, data, source, all_vars):
    for article in articles:
        title = get_text_from_nodes(article, source['title_element'])
        article_text = get_text_from_nodes(article, source['summary_element'])
        if title and article_text:
            article_lines = standard_text_processing(article_text, all_vars)
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

def build_indexes(database, metadata, args, filters, all_vars):
    ''' 
    - this function indexes data from api providing articles
    - if the local database is found, use that as starting index, otherwise build it
    '''
    rows = []
    empty_index = get_empty_index(metadata, all_vars)
    index = database if database else empty_index if empty_index else None
    for arg in args:
        for source in all_vars['sources']:
            data = get_data_from_source(source, arg, all_vars)
            if data:
                for title, article_lines in data.items():
                    for line, word_map in article_lines.items():
                        row = get_metadata(metadata, line, title, word_map, all_vars)
                        if row:
                            index, rows = add_row(row, index, empty_index, rows)
    if index:
        write_csv(rows, index.keys(), 'data/rows.csv')
        for key in index:
            if key != 'rows':
                ''' get the patterns in each index we just built & save '''
                objects, patterns = extract_objects_and_patterns_from_index(index, key, None, all_vars)
                #to do: patterns = get_patterns_between_objects(index[key], key, all_vars) # get patterns for index[key] objects with object_type key
                if patterns:
                    if len(patterns) > 0:
                        object_patterns = [''.join([k, '_', '::'.join(v)]) for k, v in patterns.items()] # 'pattern_match1::match2::match3'
                        object_pattern_name = ''.join(['data/patterns_', key, '.txt']) 
                        index[object_pattern_name] = '\n'.join(object_patterns)
                save(''.join(['data/', key, '.txt']), '\n'.join(index[key]))
        return index, rows
    return False, False

def get_metadata(metadata, line, title, word_map, all_vars):
    ''' 
    this function initializes the row object & populates it with various metadata types:
        - structural_types to get nouns, verbs, phrases, modifiers, clauses, & relationships
        - medical_types to get conditions, symptoms, & treatments in the sentence 
        - conceptual_types to get types, strategies & insights
    '''
    row = get_empty_index(metadata, all_vars)                   
    row['line'] = line
    row['word_map'] = word_map
    row['original_line'] = line
    row = replace_names(row, all_vars)
    row = get_similarity_to_title(title, row)  
    row = get_pos_metadata(row, all_vars)
    intent = None # find_intents()
    hypothesis = None # find_hypothesis()
    row = find_treatments(None, row['line'], row, all_vars)
    for metadata_type in ['structural_types', 'medical_types', 'conceptual_types']:
        for meta_type in all_vars[metadata_type]:
            if meta_type in metadata and meta_type in all_vars['pattern_index']:
                search_pattern_key = meta_type
                # check that this data 'strategies', 'treatments' was requested and is supported in pattern_index
                #modifiers, verb_phrases, roles, types, etc
                objects, patterns = extract_objects_and_patterns_from_index(row, meta_type, search_pattern_key, all_vars)
                if objects:
                    row[meta_type] = objects
                if patterns:
                    row['patterns'] = row['patterns'].union(set([p for p in patterns]))
    print('medical objects', row)
    return row

def extract_objects_and_patterns_from_index(index, object_type, search_pattern_key, all_vars):
    '''
    - all of your 'find_object' functions need to support params: pattern, matches, row, all_vars

    - this function is for meta-analysis
        for an index or row containing types of elements ('condition', 'symptom', 'strategy')
        this function is for finding patterns in those index types in the input (index or row['line'])

    - object_type is the key in object types supported in all_vars['full_params'] to find:
        ['treatments', 'conditions', 'strategies']

    - search_pattern_key is the key of all_vars['pattern_index'] keys to search: 
        ['modifiers', 'types', 'roles']

    - index can be the master index used to track all objects identified across an article set,
        or the row index to track objects found in each line
    '''
    if index:
        patterns = {}
        objects = { object_type: set() }
        lines = [index['line']] if 'line' in index else index[object_type] if object_type in index else []
        for line in lines:
            found_objects_in_patterns, found_patterns = get_patterns_and_objects_in_line(line, search_pattern_key, index, object_type, all_vars)
            if found_objects_in_patterns:
                objects[object_type] = found_objects_in_patterns
                if found_patterns:
                    patterns = found_patterns
            else:
                ''' 
                if there are no matches found for object_type patterns, 
                do a standard object query independent of pattern matches 
                '''
                found_objects = apply_find_function(object_type, None, [line], index, all_vars)
                if found_objects:
                    objects[object_type] = found_objects
        if objects or patterns:
            print('extract_objects_and_patterns_from_index response', objects, patterns)
            return objects, patterns
    return False, False

def get_patterns_and_objects_in_line(line, search_pattern_key, index, object_type, all_vars):
    found_objects = set()
    found_patterns = find_patterns(line, search_pattern_key, all_vars)
    if found_patterns and object_type != 'patterns':
        for pattern, matches in found_patterns.items():
            ''' filter pattern matches for this type before adding them, with type-specific logic in find_* functions '''
            found_objects = apply_find_function(object_type, pattern, matches, index, all_vars)
    if len(found_objects) > 0 or found_patterns:
        return found_objects, found_patterns
    return False, False

def apply_find_function(object_type, pattern, matches, index, all_vars):
    ''' find functions check for objects of object_type in matches list which match pattern '''
    function_name = ''.join(['find_', object_type])
    if function_name in globals():
        try:
            function = getattr(globals(), function_name)
            got_objects = function(pattern, matches, index, all_vars)
            if got_objects:
                if len(got_objects) > 0:
                    return set([item for item in got_objects])
        except Exception as e:
            # print('e', e)
            return False
    return False

if sys.argv:
    index = get_data_store(None, None, 'build', sys.argv)
    print('get_data_store:index', index)

import sys, json, os, re, urllib, csv, ssl, random
import wikipedia
from wikipedia.exceptions import DisambiguationError
import xml.dom.minidom
import requests

from utils import *
from get_index_def import get_empty_index
from get_structure import get_pos, get_structural_metadata
from get_vars import get_vars, get_args
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
        args_index, filters, metadata, generate_target, generate_source = get_args(args, all_vars)
        if operation == 'build':
            database = get_local_database('data', None)
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

def get_data_From_source(source, keyword, index, all_vars):
    total = 0
    max_count = 10
    for i in range(0, 10):
        start = i * max_count
        if total > start or total == 0:
            url = source['url'].replace('<KEY>', keyword).replace('<START>', str(start)).replace('<MAX>', str(max_count))
            print('url', url)
            response = requests.get(url)
            if response.content:
                xml_string = xml.dom.minidom.parseString(response.content)
                if xml_string:
                    count_tag = xml_string.documentElement.getElementsByTagName(source['count'])
                    total = int(count_tag[0].childNodes[0].nodeValue)
                    entries = xml_string.documentElement.getElementsByTagName(source['entries'])
                else:
                    entries = json.loads(response.content)
                if len(entries) > 0:
                    for entry in entries:
                        for node in entry.childNodes:
                            article = []
                            if node.nodeName in ['title', 'summary']:
                                for subnode in node.childNodes:
                                    text = subnode.wholeText
                                    if len(text) > 0:
                                        text = standard_text_processing(text, all_vars)
                                        text_list = [text] if node.nodeName == 'title' else text.split('\n')
                                        article.extend(text_list)                    
                            if len(article) > 0:
                                index['articles'].append('\n'.join(article))
    return index

def add_row(row, index, empty_index, rows):
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
    empty_index = get_empty_index(metadata, all_vars)
    index = database if database else empty_index
    rows = []
    for arg in args:
        for keyword in args[arg]:
            for source in all_vars['sources']:
                index = get_data_From_source(source, keyword, index, all_vars)
    if len(index['data']) > 0:
        for a in index['data']:
            article_words = a.split(' ')
            lines = a.split('\n')
            title = lines[0]
            for line in lines:
                row = empty_index                   
                row['line'] = line
                row['original_line'] = line
                row = get_structural_metadata(row, metadata, all_vars)
                row = get_metadata(row, metadata, all_vars)
                index, rows = add_row(row, index, empty_index, rows)
                print('row', row)
            most_similar_lines, row = get_similar_lines(lines)
            if most_similar_lines:
                index['most_similar_lines'] = most_similar_lines
    ''' save rows '''
    if len(rows) > 0:
        write_csv(rows, index.keys(), 'data/rows.csv')
    ''' save indexes '''
    for key in index:
        ''' get the patterns in the indexes we just built and save '''
        index_text = '\n '.join(index[key])
        patterns = get_pattern_matches_in_line(index_text, key, all_vars) # get patterns for index[key] objects with object_type key
        if patterns:
            object_patterns = [''.join([k, '_', '::'.join(v)]) for k, v in patterns.items()]
            object_pattern_name = ''.join(['data/patterns_', key, '.txt']) 
            object_pattern_data = '\n'.join(object_patterns)
            index[object_pattern_name] = object_pattern_data
        save(''.join(['data/', key, '.txt']), '\n'.join(index[key]))
    return index, rows

def get_metadata(row, metadata, all_vars):
    ''' 
    this function should be called from get_relationships_from_clauses so 
    types, concepts, strategies & insights are identified & indexed right away 
    while this function fetches conceptual metadata like types, strategies & insights
    to do: 
        - add filtering to skip irrelevant sentences to topic ('medical')
        - add filtering of insights to apply directly to the target condition or mechanisms
        - add mechanisms of action keywords & patterns to get strategies
        - this function determines conditions, symptoms, & treatments in the sentence 
          which fetches conceptual metadata like insights & strategies
    '''
    intent = None
    hypothesis = None
    row = get_treatments(intent, hypothesis, row, metadata, all_vars)
    for metadata_type in ['medical', 'conceptual']:
        for key in metadata:
            if key in all_vars['supported_params']:
                found_objects = get_objects_of_type(None, key, row['line'], all_vars)
                if found_objects:
                    row[key] = found_objects
    print('medical objects', row)
    return row

def get_objects_of_type(index, index_type, line, all_vars):
    print('get_objects_of_type', index_type, line)
    index = {index_type: line} if line else index
    if index:
        matched_objects = extract_objects_matching_patterns(index, [index_type], all_vars)
        if matched_objects:
            return matched_objects
    return False

def extract_objects_matching_patterns(index, search_pattern_keys, all_vars):
    ''' 
    - this function is for meta-analysis, not finding or replacing a pattern in a line
    - after youre done processing a batch of articles, 
        youll have an index containing types of elements ('condition', 'symptom', 'strategy')
        this function is for finding patterns in those index types
    - objects & local_database are both dicts of sets, just like index & row in get_metadata
    '''
    ''' all of your 'find_object' functions need to support params: pattern, matches, all_vars '''
    if index:
        objects = {}
        for object_type in index:
            if object_type not in objects:
                objects[object_type] = set()
            for line in index[object_type]:
                pattern_matches = get_pattern_matches_in_line(line, search_pattern_keys, all_vars)
                if pattern_matches:
                    for pattern, matches in pattern_matches.items():
                        objects['patterns'].add(pattern)
                        if object_type != 'patterns':
                            ''' filter matches before adding them, with type-specific logic '''
                            function_name = ''.join(['find_', object_type])
                            function = getattr(globals(), function_name)
                            got_objects = function(pattern, matches, all_vars)
                            if got_objects:
                                if len(got_objects) > 0:
                                    for item in got_objects:
                                        objects[object_type].add(item)
        if objects:
            return objects
    return False

if sys.argv:
    index = get_data_store(None, None, 'build', sys.argv)
    print('get_data_store:index', index

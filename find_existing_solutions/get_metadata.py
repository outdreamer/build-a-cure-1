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

def pull_summary_data(sources, metadata, generate_source, generate_target, args, filters, all_vars):
    ''' 
    - this function indexes data from api providing articles
    - if the local database is found, use that as starting index, otherwise build it
    '''
    empty_index = get_empty_index(metadata, all_vars['full_params'])
    local_database = get_local_database('data', None) # '' object param means get all objects
    index = local_database if local_database else empty_index
    index['articles'] = []
    rows = []
    for arg in args:
        for keyword in args[arg]:
            for source in sources:
                index = get_articles(source, keyword, index, all_vars)
    if len(index['articles']) > 0:
        for a in index['articles']:
            for line in a.split('\n'):
                row = empty_index
                if line != lines[0]:
                    most_similar_line, row = get_similar_lines(row, line, lines[0])
                    if most_similar_line:
                        row['most_similar_line'] = most_similar_line
                index, row = get_structural_metadata(line, row, metadata, all_vars)
                index, row = get_medical_metadata(lines, line, index, row, metadata, all_vars)
                index, row = get_conceptual_metadata(lines line, index, row, metadata, all_vars) #custom analysis
                index, row = update_index(row, index, empty_index, rows)
                print('row', row)

    if len(rows) > 0:
        write_csv(rows, index.keys(), 'data/rows.csv')
        generate_keys = index.keys() if generate_source == 'all' else generate_source.split(',')
        datasets = generate_datasets(generate_keys, generate_target, index, rows)
    ''' save items in index '''
    for key in index:
        ''' get the patterns in the indexes we just built and save '''
        patterns = extract(index[key], local_database, all_vars, 'patterns') # get patterns for index[key] objects with object_type key
        if patterns:
            pos_patterns = patterns.keys()
            word_patterns = [item for val_list in patterns.values() for item in val_list]
            index['usage_patterns'] = '\n'.join(pos_patterns.extend(word_patterns))
        save(''.join(['data/', key, '.txt']), '\n'.join(index[key]))
    return articles, index, rows

def update_index(row, index, empty_index, rows):
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

def get_articles(source, keyword, index, all_vars):
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
                                        text = standardize_delimiter(text)
                                        text = standard_text_processing(text, all_vars)
                                        text_list = [text] if node.nodeName == 'title' else sentences
                                        article.extend(text_list)                    
                            if len(article) > 0:
                                index['articles'].append('\n'.join(article))
    return index

def get_medical_metadata(lines, line, index, row, metadata, all_vars):
    '''
    - this function determines conditions, symptoms, & treatments in the sentence 
    - this function is a supplement to get_metadata, 
      which fetches conceptual metadata like insights & strategies
    to do: 
        - add treatment keyword check & add treatment keywords
        - add metadata check to make sure they requested this data
    '''
    intent = None
    hypothesis = None
    title = lines[0]
    row = get_treatments(intent, hypothesis, line, title, row, metadata, all_vars)
    return index, row

def get_conceptual_metadata(lines, line, index, row, metadata, all_vars):
    ''' 
    this function is a supplement to get_medical_objects, 
    which fetches condition, symptom, & treatment metadata,
    while this function fetches conceptual metadata like types, strategies & insights

    to do: 
        - add filtering to skip sentences without any symptoms or bio metrics, like:
        - add filtering of insights to apply directly to the condition or mechanisms involved
        - add standardization of acronyms using search with keywords so you get n-acetylaspartic acid from naa and creatine from cr
        - find the primary condition being studied to differentiate from other conditions or complications mentioned 
        - add mechanisms of action keywords & patterns to get strategies
    '''

    '''
    output = wikipedia.search(suggested, results=1)
    images_urls = wikipedia.page(suggested).images
    summary = wikipedia.summary(suggested)
    print('summary', summary) 
    '''
    title = lines[0]
    wikipedia.set_lang("en")
    suggested = None
    index_type = None
    for r in row['relationships']:
        for word in r.split(' '):
            pos = get_pos(word, all_vars)
            if pos == 'noun':
                ''' make sure this is a noun before querying '''
                if word[0] == word[0].upper() and word[1] != word[1].upper():
                    suggested = get_generic_medication(word)
                suggested = wikipedia.suggest(word) if not suggested else suggested
                print('suggested', suggested, word)
                try:
                    content = wikipedia.page(suggested).content
                    section_list = [s.strip().replace(' ', '_').lower() for s in content.split('==') if '.' not in s and len(s) < 100]
                    index['section_list'] = index['section_list'].union(section_list)
                    print('section list', section_list)
                    categories = wikipedia.page(suggested).categories
                    if len(categories) > 0:
                        row['types'] = row['types'].union(set(categories))
                        print('categories', categories)
                        if len(section_list) > 0:
                            ''' use section list to determine type first '''
                            for key, val in all_vars['section_map'].items():
                                for section in section_list:
                                    if key in section:
                                        index_type =  val
                        else:
                            index_type = get_index_type(suggested, all_vars, categories)
                            if index_type:
                                print('found index type', index_type, word)
                                if index_type in row:
                                    if index_type != 'dependencies':
                                        output = get_index_objects(index_type, r)
                                        if output != r:
                                            for k in output:
                                                row[k] = output[k]
                except Exception as e:
                    print('wiki summary exception', e)
    row['dependencies'] = get_dependencies('all', None, row['relationships'], 3)
    return index, row

all_vars = get_vars()
if all_vars:
    done = downloads(['data', 'datasets'])
    if done:
        args_index, filters_index, metadata, generate_target, generate_source = get_args(sys.argv, all_vars)
        if len(args_index.keys()) == 1:
            if 'sources' in all_vars:
                articles, index, rows = pull_summary_data(all_vars['sources'], metadata, generate_source, generate_target, args_index, filters_index, all_vars)
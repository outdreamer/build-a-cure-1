import sys
import networkx as nx
import networkx.generators.small as gs
import matplotlib.pyplot as plt

from get_pos import *
from get_vars import *
from get_structural_objects import *
from get_metadata import get_metadata, get_structural_metadata, get_data_from_source

keyword = None
graph_data = 'relationships.txt'
relationship_data = []
graph_object = None

if sys.argv:
    print('args', sys.argv)
    args = sys.argv
    for i, arg in enumerate(args):
        if 'keyword' in arg and (i + 1) < len(args):
            keyword = sys.argv[i + 1]
print('keyword', keyword)
if keyword:
    av = get_vars()
    if av:
        G = nx.Graph()
        #if os.path.exists(graph_data):
            # graph_object = nx.read_gml(graph_data)
        if not graph_object:
            if os.path.exists(graph_data):
                with open(graph_data, 'r') as f:
                    relationships = f.readlines()
                    if len(relationships) > 0:
                        print('relationships', len(relationships))
                    f.close()
            content, sections, categories = get_content_from_wiki(keyword, av)
            if content:
                print('retrieved content from wiki', content)
                print('sections', sections, 'categories', categories)
                content = content.replace('(', '').replace(')', '').replace('=', '').replace('-', ' ').replace('\n', '')
                lines = content.split('.')
                relationships = []
                edges = []
                nodes = {}
                for line in lines:
                    line = line.strip().replace(',','')
                    if len(line) > 5 and len(relationships) < 20:
                        blob = get_blob(line)
                        print('line', line)
                        if blob:
                            relationship = {'source': [], 'verb': None, 'target': []}
                            for word in blob.split(' '):
                                pos = get_nltk_pos(word, av)
                                if pos:
                                    if pos in av['tags']['V']:
                                        relationship['verb'] = word
                                    elif pos in av['tags']['ALL_N']:
                                        if relationship['verb'] is not None:
                                            relationship['target'].append(word)
                                        else:
                                            relationship['source'].append(word)
                            relationship['source'] = ' '.join(relationship['source'])
                            relationship['target'] = ' '.join(relationship['target'])
                            relationships.append(relationship)
                            if relationship['verb'] is not None:
                                source = str(len(relationships) * 2)
                                nodes[source] = relationship['source']
                                #G.add_node(source, nodelabel=relationship['source'])
                                G.add_node(relationship['source'])
                                target = str(int(source) + 1)
                                nodes[target] = relationship['target']
                                edges.append('-'.join([source, relationship['verb'], target]))
                                #G.add_node(target, nodelabel=relationship['target'])
                                G.add_node(relationship['target'])
                                G.add_edge(relationship['source'], relationship['target']) # add label relationship['verb']
                                G[relationship['source']][relationship['target']]['color'] = 'blue'
            nx.write_gml(G, graph_data)
            print('relationships', len(relationships))
            print(relationships)
            with open(graph_data, 'w') as f:
                f.write('\n'.join(edges))
                f.close()
            nx.draw(G, with_labels=True)
            plt.savefig('article.svg')
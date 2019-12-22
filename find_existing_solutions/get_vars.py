import random, json, itertools, csv, os, ssl, sys, re, urllib, itertools, requests
import nltk
from nltk.stem import SnowballStemmer
from nltk import CFG, pos_tag, word_tokenize, ne_chunk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob, Sentence, Word, WordList
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from get_pos import *

stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english'))

def get_pattern_config(av):
    av['passive'] = [" by ", " from ", " of "]
    ''' to do: assess which operator combinations neutralize or negate a relationship '''
    av['combined_map'] = {
        '=': ['=-', '-=', '=+', '+=', '=='], #"x = (i - b)" => x and b equal i
        '-': ['-+', '+-', '=-', '-=', '==-', '=-=', '-==', '-=-', '---'],
        '+': ['--', '++', '+=', '=+', '==+', '=+=', '+==', '+=+', '+++'],
        '#': [
            '#&', # despite x
            '#!', # despite no x
            '!-', # not decrease
            '!+', # not increase ('neutral' or 'independent', 'does not increase' doesnt mean 'decrease')
            '!>', # not change
            '~!', # does not increase =>
            '!@' # 'does not change' # to do: add all combination operators
        ],

    }
    av['combined_operators'] = []
    for key, values in av['combined_map'].items():
        av['combined_operators'].extend(values)
    av['impact_operator_map'] = {
        '!@': 'does not change'
    }
    av['replacement_patterns'] = {
        'fails': 'does not V' # antonym
    }
    av['key_map'] = {
        '-': ['worsen', 'decrease', 'inhibit', 'reduce', 'deactivate', 'disable'],
        '+': ['improve', 'increase', 'induce', 'enhance', 'activate', 'enable'],
        '=': ['equal', 'alternate'],
        '>': ['create'],
        '@': ['change'],
        '~': ['function']
    }
    av['charge'] = {
        '-': aggregate_synonyms_of_type(av, '-'), # antagonist, reduce, inhibit, deactivate, toxic, prevents
        '+': aggregate_synonyms_of_type(av, '+'), # help, assist, enhance, induce, synergetic, sympathetic, leads to
        '=': aggregate_synonyms_of_type(av, '=') # means, signifies, indicates, implies, is, equates to
    }
    ''' this maps operators to lists of operator keyword to use as clause delimiters '''
    av['clause_map'] = {
        '-': ["decrease"], # attacks
        '+': ["increase"], # helps
        '=': ['is', 'like', 'equate', 'equal', 'describe', 'indicate', 'delineate', 'same', 'like', 'similar', 'implies', 'signifies', 'means'],
        '&': ['and', 'with'], # can be conditional delimiters or statement delimiters or part of a noun phrase
        '|': ['or'], # can be conditional delimiters or statement delimiters or part of a noun phrase
        '^': ['but', 'yet', 'but yet', 'but rather', 'but actually', 'still', 'without', 'however', 'nevertheless', 'in the absence of', 'lacking'], # 'as', except and without
        '%': [
            'because', 'since', 'if', 'then', 'from', 'due', 'when', 'while', 'during', 'for', 'given',
            'in case', 'in the event that', 'caused by', 'respective of', 'later', 'after', 'before', 'pre-', 'post-'
        ], # x of y is contextual "x in the context of y"
        '#': ['despite', 'even', 'still', 'otherwise', 'in spite of', 'regardless', 'heedless', 'irrespective'],
        '!': ['not'],
        '~': ['functions', 'that'],
        '>': ['creates', 'becomes', 'changes into', 'transforms', 'produces', 'leads to', 'converts into'],
        '@': ['changes', 'impacts', 'influences', 'adjusts', 'modulates', 'modifies', 'alters', 'affects'],
        '<': ['is a subset of', 'is in', 'is part of', 'is a section of', 'is a segment of', 'is a piece of', 'is a component of'] #'x is a subset of y'
    }
    ''' to do: need functional operator for 'causes' '''
    av['clause_punctuation'] = [',', ':', ';', '(', ')']
    av['ordered_operators'] = ['because'] #, 'despite', 'not']
    av['passive_operators'] = ['%'] # the next clause after the passive operators should precede the previous clause
    av['general_operators'] = ['&', '|', '^'] # and, or, but can be conditional delimiters or statement delimiters or part of a phrase
    av['causal_operators'] = ['#'] #['when', 'even', 'despite', 'because']
    av['verb_operators'] = ['=', '+', '-', '~', '>', '@', '<']
    av['clause_types'] = ['condition', 'statement', 'question']
    ''' this maps operators to standard words to replace them with '''
    av['operator_map'] = {
        '-' : "decrease", # attacks
        '+' : "increase", # helps
        '=' : "equal", # is
        '&' : "union", # with, union
        '|' : "alternate", # or
        '^' : "exception", # without
        '%' : "dependent", # apply
        '#' : "independent", # by standard
        '!' : "not", # negating an noun or verb
        '~' : 'function',
        '>' : 'create', # should add changes as well as creates
        '@' : 'change',
        '<' : 'is subset of'
    }
    ''' sort clause delimiters so the longer strings are matched first '''
    for key in av['clause_map']:
        av['clause_map'][key] = reverse_sort(av['clause_map'][key])
    av['clause_delimiters'] = []
    for k, v in av['clause_map'].items():
        av['clause_delimiters'].extend(v)
    av['clause_delimiters'].extend([',', ':', ';', '(', ')'])
    abstract_verbs = ['find', 'derive', 'build', 'test', 'apply']
    med_objects = ['treatment', 'compound', 'test', 'metric', 'mechanism']
    study_objects = ['relationship', 'limit', 'type', 'method']
    conceptual_objects = ['relationship', 'problem', 'strategy', 'process', 'insight', 'function', 'variable', 'system', 'theory', 'opinion', 'conclusion', 'observation']
    av['info_types'] = ['excuse', 'opinion', 'fact', 'lie', 'belief', 'joke', 'insight', 'reason', 'intent', 'strategy']

    ''' to do: some of these types have type mappings so generalize when you can
        condition = state
        symptom = function = side_effects
        function = relationship
        synthesis = build process
        structure = pattern
    '''
    ''' conceptual relationships:
        priority = direction
        observation = insight = function = result = relationship
        conclusion = ordered_list(observations) + guess = coefficients + bias
        strategy = ordered_list(insights)
        strategy = insight + context
        problem = (combination of intents having different priorities) or (an resource distribution imbalance)
        intent = strategy + priority
        solution = (combination of strategies operating on variables with insight functions that reduce dimensions of problem (function-combination) or (resource-imbalance))
        type = combination(attributes)
        intents = function outputs, including unintended/emergent/unforeseen side effects
        roles = functions
        relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
        components = compounds, symptoms, treatments, metrics, conditions, stressors, types, variables

        'insight': set(), # useful sentences in index set that have bio rules in them - for abstracts this will likely just be the treatment success sentence
        'strategy': set(), # insights relevant to methods/mechanisms of action/processes or patterns of problem-solving
        'target_intent': set(),
        'avoid_intent': set(), # in addition to functions you want to target, there are functions you want to avoid as well
    '''
    av['study_intents'] = {
        'test': 'to confirm a relationship (between x=success)', 
        'find': 'to find a relationship (between x=y)', 
        'verify': 'to confirm an object (study, method, result)',
        'compare': 'to compare objects (study=study, method=method, result=protocol)', 
        # compare => check that all studies confirm each other, or check that a method-implementation or result-derivation followed protocol
        'build': 'to build object (compound, symptom, treatment, condition, state)' 
        # to get 'health', follow build protocol 'x', to get 'compound', follow build protocol 'y'
    }
    av['intent_map'] = {
        'route': {
            'attention': 'distract',
            'assumption': 'project',
        },
        'find': {
            'interaction': 'relevance',
            'alternative': {},
            'limit': {},
            'relationship': {
                'condition': {
                    'treat': ['compound', 'method'],
                    'diagnose': ['method']
                },
                'symptom': {
                    'check': 'condition'
                },
                'compound': {
                    'synthesize': ['method']
                }
            }
        },
        'change': {
            'subject': 'deflect',
            'negative': {
                'statement': 'contradict',
                'accusation': 'deny'
            },
            'assumption': 'counter-argue',
            'add': {
                'doubt': 'question', # cast doubt on
                'noise': 'obfuscate',
                'contradiction': 'confuse',
                'nonsense': 'entertain' # not real
            },
            'align': {
                'incentive': 'provoke' # argument/emotion/reaction
            },
            'remove': {
                'doubt': 'imply', # remove doubt
                'ambiguity': 'clarify', # remove ambiguity
                'credibility': 'criticize',
                'alignment': 'conflict'
            },
        },
        'reveal': {
            'priority': 'persuade',
            'benefit': 'persuade', # defend,
            'cost': 'persuade' # attack
        },
        'organize': {
            'example': '',
            'introduce': '',
            'exception': '',
            'list': {
                'property': 'compare'
            },  
            'categorize': '', 
            'summarize': '',
            'compare': {
                'review': ['meta', 'peer', 'alternative']
            },
            'verify': ['retract', 'replicate']
        },
        'fit': {
            'structure': {
                'model': 'test', # explore, experiment
                'network': {
                    'system': 'understand',
                    'system_path': 'educate'
                },
                'path': {
                    'perspective': 'interpret',
                    'understanding': 'explain',
                    'protocol': 'evaluate',
                    'logic': 'conclude',
                    'logic': 'argume',
                    'logic': 'function', # derive
                    'logic': 'justify',
                    'intent': 'justify'
                }
            }
        },
        'frame': {  # cast one info type (opinion) as another (fact) 
            'question': 'implication',
            'opinion': 'fact',
            'lie': 'fact',
            'opinion': 'joke',
            'lie': 'joke',
            'opinion': 'insight',
            'lie': 'insight',
            'excuse': 'reason',
            'lie': 'reason',
            'lie': 'excuse',
            'intent': 'excuse',
            'info_asymmetry': 'excuse'
        }
    }
    av['default_props'] = {
        'input': {},
        'output': {},
        'optimal_parameter': {},
        'attribute': {},
        'function': [],
        'type': [],
        'topic': [],
        'state': [] # versions
    }
    av['instruction_props'] = {
        'substitute': {},
        'equipment':{},
    }
    av['symptom_props'] = {
        'treatment': []
    }
    av['compound_props'] = {
        'side_effect': [] # this is just a list of symptoms the compound causes, which can be assembled from rows data
    }
    av['keywords'] = {
        'equipment': {
            'type': [],
            'object': {},
            'modifier': [],
            'property': {},
            'component': {}
        },
        'metric': {
            'type': [],
            'object': {},
            'modifier': ['quantitative'],
            'property': ['level', 'quantity'],
            'component': {}
        },
        'test': {
            'type': [],
            'object': {},
            'modifier': ['machine', 'sample'],
            'property': {},
            'component': {}
        },
        'experiment': {
            'type': [],
            'object': {},
            'modifier': [],
            'property': ['parameter', 'linearity', 'sensitivity', 'precision', 'repeatability', 'recovery'],
            'component': {}
        },
        'state': {
            'type': [],
            'object': {},
            'modifier': ['-tion'],
            'property': ['active', 'order'],
            'component': {}
        },
        'function': {
            'type': ['function', 'intent', 'strategy', 'mechanism', 'relationship', 'process', 'modifier', 'logic'],
            'object': [
                'effect', 'activation', 'activity', 'reaction', 'process', 'role', '-osis', '-isis', '-ysis', '-ism', '-tion',
                'anti-', 'pro-', '-ist', '-ive', '-ing', '-yst', '-ior', '-or', '-er',
                'attenuate', 'down/up/regulate', 'stimulate', 'absorb', 'catalyze', 'alleviate', 'suppress','moderate', 'adjust', 'change'
            ],
            'modifier': [],
            'property': {},
            'component': {}
        },
        'patient': {
            'type': [],
            'object': av['supported_core']['participants'],
            'modifier': [],
            'property': {},
            'component': {}
        },
        'symptom': {
            'type': [],
            'object': {},
            'modifier': [],
            'property': {},
            'component': {}
        },
        'treatment': {
            'type': [],
            'object': {},
            'modifier': [],
            'property': {},
            'component': {}
        },
        'condition': {
            'type': [],
            'object': {},
            'modifier': [],
            'property': {},
            'component': {}
        },
        'compound': {
            'type': ['bio', 'chemical'],
            'object': [
                'polymer', 'molecule', 'macromolecule', 'peptide', 'fat', 'protein', 'carbohydrate', 'sugar', 'lipid', 'fatty acid', 
                'acid', 'base', 'enzyme', 'plasma', 'fluid', 'tissue', 'blood', 'receptor', '-ion', 'acid', 'base'
            ],
            'modifier': [
                'oral', 'liquid', 'frozen', 'heated', 'refrigerated', 'topical', 'intravenous', 'iv', 'concentration',
                'injection', 'gavage', 'capsule', 'gel', 'powder', 'supplement', 'solution', 'spray', 'tincture', 'mixture'
            ],
            'property': {'charge': '', 'electron_count': ''},
            'component': {'bond': [], 'element': [], 'atom': [], 'molecule': [], 'ion': []}
        },
        'gene': {
            'type': [],
            'object': [],
            'modifier': [],
            'property': {},
            'component': {}
        },
        'cell': {
            'type': [],
            'object': [],
            'modifier': [],
            'property': {},
            'component': {
                'mitochondria': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                },
                'nucleus': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                }, 
                'dna': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': []
                }, 
                'membrane': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                }
            }
        },
        'tissue': {
            'type': [
                'muscle', 
                'mucus_membrane', 
                'bone', 
                'collagen',
                'organ'
            ],
            'object': [],
            'modifier': [],
            'property': {},
            'component': ['cell']
        },
        'micro-organism': {
            'type': [],
            'object': ['bacteria', 'fungi', 'virus', 'pathogen', 'cell'],
            'modifier': [],
            'property': {},
            'component': {}
        },
        'bio_system': {
            'type': [],
            'object': {
                'organ': {
                    'type': [],
                    'object': ['liver', 'kidney', 'bladder', 'ovary', 'uterus', 'lung', 'intestine', 'gall bladder', 'bladder', 'skin', 'appendix'],
                    'modifier': [],
                    'property': {},
                    'component': {}
                },
                'nervous': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                },  
                'lymphatic': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                },  
                'immune': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                },   
                'circulatory': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                },    
                'digestive': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                },  
                'timer': {
                    'type': [],
                    'object': [],
                    'modifier': [],
                    'property': {},
                    'component': {}
                }
            },
            'modifier': [],
            'property': ['fragility', 'toxicity', '-ty', 'synthetic'],
            'component': {}
        }
    }

    '''
        VBZ: Verb, 3rd person singular present - asks is does has
        VBG: Verb, gerund or present participle - asking, being, doing, having
        VBD: Verb, past tense - asked, was/were, did, had
    '''

    ''' *** IMPORTANT PATTERN CONFIG INFO ***
        - for pattern configurations, always put the extended pattern first
            - if you put '<noun>' before "<noun> <noun>',
                you'll miss phrases like 'compound acid' returning matches like:
                     ['compound acid']
                and will instead get matches for the '<noun>' pattern:
                    ['compound', 'acid']
                so make sure thats what you want before ignoring this rule
        - pattern_syntax: 
            __a__ : an optional item
            |a b c| : a set of alternatives
        - note that we are also supporting pos names in the patterns, in case you want to include all tags from that pos type
        - if you include 'noun' in your pattern, it'll replace it with all the noun pos tags, like |NN NNS NNP NNPS| etc
    '''

    av['pattern_maps'] = {
        'passive_to_active': {
            'x of y': 'y x', # to do: add support for new characters in target_pattern like 'y-x'
            'x was VBD by y': 'y VBZ x', # alkalization of x => x alkalizer => alkalizes x
            'x that has y': 'x with y',
            'the N1 VBD VBN IN the N2': 'the N2 VBZ the N1', # x was bitten by y => y bit x
            'x VBD VBD IN y': 'y VBN x',
            'x VBD VBN by y': 'y VBN x',
            'x VBZ VBN by y': 'y VBN x',
            'x that y z': 'z y x', # "protein that modulates a (signaling pathway)" => "(signaling pathway)-changing protein" 
            'x that does VBG': 'x VBZ', # x that does inhibiting => x inhibits
            'x that does VBG': 'x VBZ', # x that does inhibiting => x inhibits 
            'x with y functionality': 'x y', 
            'x has ability to do y': 'x y',
            'JJ1 NN1 of JJ2 NN2': 'JJ2 NN2 JJ1 NN1',
            'x is an item in list b': 'x is in list b'
        },
        'verb_phrase': {
            'could not have been done': 'was impossible',
            'could not have': 'cannot',
            'could have been done': 'was possible',
            'could have': 'can',
            'should not have been done': 'was inadvisable',
            'should not have': 'does',
            'should have': 'does not',
            'has not been done': 'did not',
            'had been done': 'did'
        }
    }
    av['pattern_vars'] = ['N', 'ALL_N', 'V', 'ALL_V', 'ADJ', 'ADV', 'DPC', 'C', 'D', 'P']
    av['type_pattern_index'] = {
        'passive': [
            'noun_phrase1 of noun_phrase2' # enzyme inhibitor of protein synthesis
        ],
        'modifier': [],
        'noun_phrase': [],
        'verb_phrase': [],
        'phrase': [
            'modifier1 DPC modifier2'
        ],
        'clause': [
            'clause1 DPC clause2'
        ],
        'relationship': [
            'clause',
            'phrase1 phrase2 V clause',
            'clause1 DPC clause2'
        ],
        'rule': [],
        'context': [],
        'compound': [
            "rule of compound",
            "compound1 compound2"
        ],
        'condition': [],
        'symptom': [
            'N that gets worse when context1',
            'x - y & - z even in condition1 or condition2'
        ]
    }
    av['pattern_index'] = {
        'passive': [
            '|VB VBP VBN VBD| |VB VBP VBN VBD|', # is done, was done
            'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', # having been done
            '|VB VBP VBN VBD| |TO IN PP|', # finish by, done by
            '|VBD| VBN VBN |TO IN PP|', # has been done by
        ],
        'subject': [
            'ALL_N ALL_V',
        ],
        'modifier': [
            #'(?)', # add support for an any character 
            '|N V| |N ADV ADJ V|', # compound isolate
            'NNP ALL_N', # Diabetes mellitus
            'N N', # the second noun may have a verb root, ie "enzyme-inhibitor"
            'N V',
            'JJ NN'
        ],
        'phrase': [
            'ALL_N DPC |ADJ ADV VB VBG VBD| ALL_N', # converter of ionic/ionized/ionizing radiation, necrotizing spondylosis
            'ALL_N DPC ALL_N |VBG VBD|', # metabolite of radiation poisoning
            'ALL_N DPC ALL_N', # metabolite/metabolizer/inhibitor/alkalization of radiation, 
        ],
        'clause': [
            '|suppose thought assumed| that', 
            'DPC NP VP NP',
            'DPC NP DPC NP',
            'DPC VP NP',
            'DPC VP',
            'DPC NP',
        ],
        'noun_phrase': [
            'ALL_N ALL_N',
            'ALL_N ALL_N ALL_N', # HIV-positive patients => NNP JJ NNS
        ],
        'verb_phrase': [
            'ADV ALL_V',
            'ADJ ALL_V',
            'ALL_V ALL_V', #'associating alkalizing with compound x'
            'ALL_V ALL_V',
            'plays a |VB NN| role',
            '|functions works operates interacts acts| as __a__ |VB NN|'
        ],
        'type': [
            'ADJ N', # Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')
        ],
        'role': [
            'ADV |V N|', # Ex: 'emulsifying protein' (role = 'emulsifier')
        ]
    }

    for key in av['type_pattern_index']:
        av['pattern_vars'].append(key)
    for key in av['pattern_index']:
        av['pattern_vars'].append(key)
    av['pattern_vars'] = set(av['pattern_vars'])
    av['all_pattern_version_types'] = ['correct', 'indexed', 'nested', 'alt', 'pos', 'type', 'synonym', 'operator', 'function']
    ''' 
    now that pattern lists are generated, 
    populate pattern types from type_pattern_index[key[
    with all variants from the corresponding list in pattern_index[key]
    '''
    for key, type_pattern_index in av['type_pattern_index'].items():
        new_type_pattern_index = []
        for type_pattern in type_pattern_index:
            for sub_pattern_type, sub_pattern_list in av['pattern_index'].items():
                nonnumeric_index_type = get_nonnumeric(sub_pattern_type, av)
                nonnumeric_type_pattern = get_nonnumeric(type_pattern, av)
                ''' if 'modifier' in ['modifier', 'DPC', 'modifier'] '''
                if nonnumeric_index_type in nonnumeric_type_pattern.split(' '):
                    ''' iterate through modifiers pattern_index, replacing nonnumeric_index_type with index pattern '''
                    for sub_pattern in sub_pattern_list:
                        new_type_pattern = nonnumeric_type_pattern.replace(nonnumeric_index_type, sub_pattern)
                        new_type_pattern_index.append(''.join(new_type_pattern))
        if len(new_type_pattern_index) > 0:
            if key in av['pattern_index']:
                av['pattern_index'][key].extend(new_type_pattern_index)
    '''
    if there are files with the 'data/objecttype_patterns.txt' name pattern, 
    pull that data and add it to pattern_index dict 
    '''
    av = update_patterns(av)
    return av

def update_patterns(av):
    indexed_patterns = []
    av['all_patterns'] = []
    cwd = os.getcwd()
    all_pattern_filename = ''.join([cwd, '/data/all_patterns.txt'])
    if os.path.exists(all_pattern_filename):
        pattern_contents = read(all_pattern_filename)
        if pattern_contents:
            for line in pattern_contents.split('\n'):
                pattern_split = line.split('::')
                pattern_index = pattern_split[0]
                pattern_key = pattern_split[1]
                pattern = pattern_split[2]
                if pattern_key in av[pattern_index]:
                    av['all_patterns'].append(pattern)
                    av[pattern_index][pattern_key].append(pattern)
    if len(av['all_patterns']) > 0:
        indexed_patterns = av['all_patterns']
    elif len(av['all_patterns']) == 0:
        new_pattern_lines = []
        for pattern_index in ['pattern_index', 'type_pattern_index']:
            for pattern_key, patterns in av[pattern_index].items():
                for original_pattern in patterns:
                    if original_pattern not in indexed_patterns:
                        indexed_patterns.append(original_pattern)
                        generated_patterns, av = get_all_versions(original_pattern, 'all', av) 
                        if generated_patterns:
                            for pattern in generated_patterns:
                                new_pattern_lines.append('::'.join([pattern_index, pattern_key, pattern]))
                            av[pattern_index][pattern_key] = reversed(sorted(generated_patterns))
        if len(new_pattern_lines) > 0:
            av['all_patterns'] = reversed(sorted(new_pattern_lines))
            save(all_pattern_filename, new_pattern_lines)
    for pattern_map_key, pattern_map in av['pattern_maps'].items():
        new_pattern_map = {}
        for sp, tp in pattern_map.items():
            if sp not in indexed_patterns:
                indexed_patterns.append(sp)
                sp_patterns, av = get_all_versions(sp, 'all', av) 
                if sp_patterns:
                    for sp_pattern in sp_patterns:
                        if tp not in indexed_patterns:
                            indexed_patterns.append(tp)
                            tp_patterns, av = get_all_versions(tp, 'all', av) 
                            if tp_patterns:
                                for tp_pattern in tp_patterns:
                                    new_pattern_map[sp_pattern] = tp_pattern
        if new_pattern_map:
            av['pattern_maps'][pattern_map_key] = new_pattern_map
    return av

def reverse_sort(map_list):
    '''
    - before parsing patterns, sort the patterns by number of spaces 
        so the longest patterns get parsed first as a safeguard
    - also sort clause delimiters by length before applying them so you apply 
        "but actually" as a delimiter before applying "but"
    '''
    sorted_val_list = []
    length_index = {}
    for key in map_list:
        length_index[key] = len(key)
    if length_index:
        for length in reversed(sorted(length_index.values())):
            for k, v in length_index.items():
                if v == length:
                    sorted_val_list.append(k)
    if len(sorted_val_list) > 0:
        return sorted_val_list
    return False

def get_args(arg_list, av):
    metadata_keys = ''
    generate_source = ''
    generate_target = ''
    args_index = {}
    filters_index = {}
    for i, arg in enumerate(arg_list):
        arg_key = arg.replace('--', '').replace('-', '_')
        if arg_key in av['supported_params']:
            arg_val = arg_list[i + 1] if (i + 1) < len(arg_list) else ''
            if arg_key == 'metadata':
                if arg_val in av['supported_params'] or arg_val == 'all':
                    metadata_keys = arg_val.split(',')
            elif arg_key == 'filters':
                # |filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
                filters_index = { key: val.split(',') for key, val in arg_val.split(',') } # val will be metricC::metricvalue for metric
            elif arg_key == 'generate':
                generate_list = arg_val.split('::')
                generate_source = [s for s in generate_list[0].split(',') if s in av['supported_params']]
                generate_target = generate_list[1]
            else:
                args_index[arg_key] = arg_val.split(',')
    print('args_index', args_index)
    print('filters', filters_index)
    print('metadata', metadata_keys, 'generate', generate_target, generate_source)
    metadata_keys = 'all' if metadata_keys == '' else metadata_keys
    return args_index, filters_index, metadata_keys, generate_target, generate_source

def get_vars():
    verb_contents = read('data/verbs.txt')
    standard_verbs = set(['increase', 'decrease', 'inhibit', 'induce', 'activate', 'deactivate', 'enable', 'disable'])
    av = {}
    av['standard_verbs'] = set(verb_contents.split('\n')) if verb_contents is not None else standard_verbs
    av['numbers'] = '0123456789'
    av['alphanumeric'] = 'abcdefghijklmnopqrstuvwxyz0123456789- '
    av['alphabet'] = 'abcdefghijklmnopqrstuvwxyz'    
    av['clause_analysis_chars'] = [' ', '-', ':', ';', '(', ')']
    av['full_params'] = {
        'request': ['metadata', 'generate', 'filters', 'data'], # request params
        'wiki': ['section_list'],
        'pos': ['pos', 'verb', 'noun', 'common_word', 'count', 'taken_out', 'clause_marker', 'line', 'prep', 'conj', 'det', 'descriptor', 'original_line', 'word_map'],
        'structure': ['type', 'name', 'ngram', 'modifier', 'phrase', 'clause', 'subject', 'relationship', 'pattern', 'similar_line'], # structural
        'experiment': ['hypothesis', 'test', 'metric', 'property', 'assumption'], # experiment elements
        'compound': ['compound', 'contraindication', 'interaction', 'side_effect', 'treatment_successful', 'treatment_failed'], # drug elements
        'organism': ['gene', 'expression', 'evolution', 'organ', 'cell', 'nutrient'],
        'condition': ['symptom', 'condition', 'diagnosis', 'phase'], # separate diagnosis bc theyre not always accurate so not equivalent to condition
        'context': ['bio_metric', 'bio_symptom', 'bio_condition', 'bio_stressor'], # context elements
        'synthesis': ['instruction', 'parameter', 'optimal_parameter', 'substitute', 'equipment'],
        'relational': ['component', 'related', 'alternate', 'substitute', 'sub', 'adjacent', 'stressor', 'dependency'],
        'conceptual': ['concept', 'variable', 'function', 'causal_stack', 'insight', 'strategy', 'prediction', 'priority', 'intent', 'system']
    }
    object_type_keys = {
        'medical_types': ['experiment', 'compound', 'organism', 'condition', 'context', 'synthesis'],
        'conceptual_types': ['conceptual', 'relational'],
        'structural_types': ['pos', 'structure']
    }
    for key, val in object_type_keys.items():
        for ref in val:
            av[key] = [item for item in av['full_params'][ref]]
    av['supported_params'] = []
    for key, val in av['full_params'].items():
        av['supported_params'].extend(val)
    av['tags'] = get_tags()
    ''' retrieve synonyms from maps/*.json '''
    av = fill_synonyms('maps', av)
    av['section_map'] = {
        'signs_and_symptoms': 'condition',
        'medical_uses': 'treatment',
        'chemical_and_physical_properties': 'compound', # this refers to a compound that is not a known treatment or is a sub component of a treatment
        'applications': 'compound',
        'growth': 'organism',
        'adverse_effects': 'treatment',
        'side_effects': 'treatment',
        'contraindications': 'treatment',
        'interactions': 'treatment',
        'pharmacology': 'treatment',
        'common_names': 'organism',
        'cause': 'symptom',
        'pathophysiology': 'symptom',
        'diagnostic_approach': 'symptom',
        'management': 'symptom',
        'epidemiology': 'symptom',
        'uses': 'organism', # https://en.wikipedia.org/wiki/Boesenbergia_rotunda
    }
    av = get_pattern_config(av)
    return av

def aggregate_synonyms_of_type(av, synonym_type):
    type_synonyms = set()
    if synonym_type in av['key_map']:
        for keyword in av['key_map'][synonym_type]:
            if keyword in av['supported_core']:
                if type(av['supported_core'][keyword]) == dict:
                    for k, v in av['supported_core'][keyword]:
                        type_synonyms.add(k)
                        type_synonyms.add(v)
                elif type(av['supported_core'][keyword]) == list:
                    for x in av['supported_core'][keyword]:
                        type_synonyms.add(x)
    return type_synonyms

def fill_synonyms(path, av):
    ''' get maps in path & assemble into synonym lists '''
    cwd = os.getcwd()
    av['supported_core'] = {}
    av['supported_synonyms'] = {}
    av['supported_stems'] = {}
    if not os.path.exists(path) or not os.path.isdir(path):
        path = '/'.join([cwd, path])
    if os.path.exists(path) and os.path.isdir(path):
        for filename in os.listdir(path):
            full_path = '/'.join([path, filename]) 
            if os.path.exists(full_path) and os.path.isfile(full_path):
                word_map = read(full_path)
                if word_map:
                    if 'sources' not in filename:
                        for top_element in word_map:
                            av['supported_core'][top_element] = word_map[top_element]
                            av['supported_stems'][top_element] = set()
                            if type(word_map[top_element]) == list:
                                for y in word_map[top_element]:
                                    av = process_synonym_element(y, top_element, av)
                            elif type(word_map[top_element]) == dict:
                                for k, y in word_map[top_element].items():
                                    av['supported_stems'][top_element].add(get_stem(k))
                                    av = process_synonym_element(y, top_element, av)
                                    av = process_synonym_element(y, k, av)     
                    else:
                        print('word map', word_map)
                        av['sources'] = word_map
    return av

def process_synonym_element(y, keyword, av):
    if type(y) == list:
        for x in y:
            av['supported_stems'][keyword].add(get_stem(x))
            av['supported_synonyms'][x] = keyword
    elif type(y) == dict:
        for k, v in y.items():
            av['supported_stems'][keyword].add(get_stem(k))
            av['supported_stems'][k].add(get_stem(v))
            av['supported_synonyms'][k] = keyword
            av['supported_synonyms'][v] = k
    elif type(y) == str:
        av['supported_stems'][keyword].add(get_stem(y))
        av['supported_synonyms'][y] = keyword
    return av                                    

def get_general_pos(pattern, av):
    ''' convert 'NN' => 'N' '''
    new_subsets = []
    for subset in pattern.split('|'):
        new_words = []
        for word in subset.split(' '):
            nn = get_nonnumeric(word, av)
            if 'ALL_' in nn:
                new_words.append(nn.replace('ALL_',''))
            elif nn in av['tags']['ALL']:
                pos_tag = sorted([key for key in av['tags'] if nn in av['tags'][key] and len(key) == 1])
                if len(pos_tag) > 0:
                    new_words.append(pos_tag[0])
            else:
                new_words.append(word)
        if len(new_words) > 0:
            new_subsets.append(' '.join(new_words))
    if len(new_subsets) > 0:
        return '|'.join(new_subsets)
    return False

def get_specific_pos(pattern, av):
    ''' convert 'ALL_N' => |NN JJ JJR NNS NNP NNPS RB] '''
    new_subsets = []
    for subset in pattern.split('|'):
        new_words = []
        for word in subset.split(' '):
            nn = get_nonnumeric(word, av)
            tag_list = [x for k, v in av['tags'] for x in v] if nn == 'ALL' else av['tags'][nn] if nn in av['tags'] else None
            if tag_list:
                new_words.append(''.join(['|', ' '.join(tag_list), '|']))
            else:
                new_words.append(word)
        if len(new_words) > 0:
            new_subsets.append(' '.join(new_words))
    if len(new_subsets) > 0:
        return '|'.join(new_subsets)
    return False

def get_all_pos(pattern, av):
    ''' convert 'ALL_N' => |NN JJ JJR NNS NNP NNPS RB], 'dog' => 'NN' '''
    new_subsets = []
    for subset in pattern.split('|'):
        new_words = []
        for word in subset.split(' '):
            nn = get_nonnumeric(word, av)
            tag_list = [x for k, v in av['tags'] for x in v] if nn == 'ALL' else av['tags'][nn] if nn in av['tags'] else None
            if tag_list:
                new_words.append(''.join(['|', ' '.join(tag_list), '|']))
            elif nn in av['tags']['ALL']:
                new_words.append(word)
            else:
                pos = get_nltk_pos(word, av)
                if pos:
                    new_words.append(pos)
                else:
                    new_words.append(word)
        if len(new_words) > 0:
            new_subsets.append(' '.join(new_words))
    if len(new_subsets) > 0:
        return '|'.join(new_subsets)
    return False

def is_isolated_alt(subset, av):
    alt_subset = subset.replace('|', '')
    if alt_subset == subset.strip():
        no_letters_spaces = [x for x in alt_subset if x.lower() not in av['alphanumeric'] and x != ' ' and x != '_']
        if len(no_letters_spaces) == 0:
            return alt_subset
    return False

def get_alts(pattern, av):
    all_alts = get_alt_sets(pattern, [], av)
    index_lists = []
    if all_alts:
        if len(all_alts) > 0:
            for sub_list in all_alts:
                index_lists = append_list(index_lists, sub_list)
            index_lists = set([il.replace('  ',' ') for il in index_lists])
            if len(index_lists) > 0:
                return index_lists
    return False

def get_alt_sets(pattern, all_alts, av):
    subsets, variables = get_pattern_subsets(pattern, av)
    all_alts = all_alts if all_alts else []
    if subsets:
        for item in subsets:
            if item != '':
                if item in variables:
                    unwrapped = variables[item][1:-1]
                    delimiter_count = unwrapped.count('|')
                    if delimiter_count == 2:
                        all_options = []
                        for option_set in unwrapped.split('|'):
                            joined = ''.join(['|', option_set.strip(), '|'])
                            if joined in pattern and joined != '||':
                                subset_string = unwrapped.replace(joined, '')
                                for o in option_set.split(' '):
                                    all_options.append(unwrapped.replace(joined, o))
                        if len(all_options) > 0:
                            all_alts.append(all_options)
                    elif delimiter_count > 2:
                        new_all_sets = get_alt_sets(variables[item], all_alts, av)
                        if len(new_all_sets) > 0:
                            all_alts = new_all_sets
                    elif delimiter_count == 0:
                        all_alts.append(unwrapped.split(' '))
                else:
                    all_alts.append(item)
    if len(all_alts) > 0:
        new_alts = []
        for sub_list in all_alts:
            if type(sub_list) == list:
                total_set = list(set([word for sub_list_item in sub_list for word in sub_list_item.split(' ')]))
                new_alts.append(total_set)
            else:
                new_alts.append(sub_list)
        if len(new_alts) > 0:
            return new_alts
    return False

def append_list(index_lists, sub_list):
    new_index_list = []
    if type(sub_list) == list:
        for i, item in enumerate(sub_list):
            if len(index_lists) > 0:
                for index_list in index_lists:
                    new_index_list.append(' '.join([index_list, item]).strip())
            else:
                new_index_list.append(item)
    else:
        if len(index_lists) > 0:
            for index_list in index_lists:
                new_index_list.append(' '.join([index_list, sub_list]).strip())
        else:
            new_index_list.append(sub_list)
    if len(new_index_list) > 0:
        return new_index_list
    return False

def generate_alt_patterns(pattern, av):
    ''' 
    this functions returns ['VB NN D1 D2', 'VB JJ D1 D2'] from pattern = 'VB |NN JJ| D1 D2' 
    - alternatives are indicated by options separated by spaces within pairs of '|'
    - optional strings are indicated by: __option__    
    - pattern = '|VB NN VB&ADV|' means 'VB or NN or VB & ADV'
    '''
    new_pattern = pattern.strip().replace('__', '')
    delimiter = find_delimiter(new_pattern, av)
    if delimiter:
        alts = get_alts(new_pattern, av)
        if alts:
            if len(alts) > 0:
                ''' now replace optional strings and add that pattern as well '''
                if '__' in pattern:
                    all_patterns = []
                    for alt in alts:
                        alt = alt.strip().replace('&', ' & ')
                        nap_with_options = []
                        nap_without_options = []
                        alt_words = alt.split(' ')
                        for word in alt_words:
                            joined = ''.join(['__', word, '__'])
                            if joined in pattern:
                                nap_with_options.append(word)
                            else:
                                nap_with_options.append(word)
                                nap_without_options.append(word)
                        all_patterns.append(' '.join(nap_with_options))
                        all_patterns.append(' '.join(nap_without_options))
                    if len(all_patterns) > 0:
                        return all_patterns
                else:
                    new_alts = []
                    for alt in alts:
                        new_alts.append(alt.strip().replace('&', ' & '))
                    if len(new_alts) > 0:
                        return new_alts
    return False

def generate_indexed_patterns(pattern, av):
    ''' this function adds an integer index to any repeated items '''
    new_words = []
    words = pattern.split(' ')
    for i, w in enumerate(words):
        if w not in ['__', '|']: # exclude delimiters from indexing
            nonnumeric_w = get_nonnumeric(w, av)
            if w == nonnumeric_w:
                if words.count(w) > 1:
                    new_words.append(''.join([w, str(i)]))
                else:
                    new_words.append(w)
            else:
                new_words.append(w)
        else:
            new_words.append(w)
    if len(new_words) > 0:
        return ' '.join(new_words)
    return False
    
def generate_correct_patterns(pattern, av):
    '''
        - words like 'bear', 'worm', 'rat' will be logged as a verb even when preceded by determiner
        - add pattern_map word_pos entries to convert words to the correct pos: 
            'DT V1 V2 V3' => 'DT N V1 V2' if V1 can be a noun
        - this function corrects patterns with incorrect mappings like:
            'the VB VB VB IN the NN' to 'the NN VB VB IN the NN'
        - remove incorrect pattern syntax:
            - make sure '&' is not surrounded by spaces 
            - make sure '__' is not wrapping a string wrapped by spaces 
            - if there is an odd number of '|' delimiters, 
                remove the delimiter remaining from bubbling outward from innermost embedded pattern
                if there are no embedded patterns, remove any consecutive delimiters '||'
            - make sure there are no repeats within an alt_set: '|VB VB NN|' should be '|VB NN|'
    '''
    return False

def generate_type_patterns(pattern, av):
    ''' 
    to do: implement after get_types 
        Cytotoxicity in cancer cells => <component object>-toxicity, anti-tumor => anti-<component object of illness>
        suppress/interfere/inhibit activity of carcinog/canc/tumz => suppress/interfere/inhibit activity of drug/medication/enzyme
    '''
    return False

def generate_synonym_patterns(pattern, av):
    ''' first check that words are not in supported keywords, then get the synonym '''
    new_pattern = []
    for word in pattern.split(' '):
        nonnumeric = get_nonnumeric(word, av)
        if nonnumeric not in av['tags']['ALL'] and nonnumeric not in av['tags'] and av['type_pattern_index'] and nonnumeric not in av['pattern_index']:
            ''' this is a word, check for synonyms '''
            synonym, av = replace_with_syns(word, None, ['synonym'], av)
            if not synonym:
                synonym, av = replace_with_syns(word, None, ['common', 'standard', 'similarity'], av)
            if synonym:
                new_pattern.append(synonym)
            else:
                new_pattern.append(word)
        else:
            new_pattern.append(word)
    if len(new_pattern) > 0:
        return ' '.join(new_pattern), av
    return False, av

def generate_operator_patterns(pattern, av):
    new_pattern, variables = convert_to_operators(pattern, av)
    if new_pattern:
        return new_pattern
    return False

def generate_function_patterns(pattern, av):
    ''' find functions in pattern & replace with their core function decomposition '''
    functions = find_function(pattern)
    if functions:
        for f in functions:
            core_functions = find_core_function(f)
            if core_functions:
                ''' replace f with core_functions in pattern '''
                for cf in core_functions:
                    pattern = pattern.replace(function, cf)
    return [pattern]

def get_all_versions(pattern, version_types, av):
    ''' 
    this is to generate patterns with standardized synonyms, operators, & types in configured patterns
    execute indexed patterns after you run nested & alt patterns 
    - version_types = av['all_pattern_version_types'] if version_types == 'all' or len(version_types) == 0 else version_types
    - corrected_pattern = generate_correct_patterns(pattern, av)
    '''
    #pattern = '|functions works operates interacts acts| as __a__ |VB NN|'
    pattern = 'ALL_N DPC |ADJ ADV VB |VBG VBD|| ALL_N |JJ NN|'
    # to_iterate = set([x for x in [get_specific_pos(pattern, av), get_general_pos(pattern, av), get_all_pos(pattern, av)] if type(x) != bool])
    word_count = [x for x in pattern.replace('|','').replace('__','').replace('&',' ').split(' ') if x not in av['tags']['ALL'] and x not in av['tags']]
    print('\n\tget_all_versions: pattern', pattern)
    all_to_iterate = []
    alt_patterns = generate_alt_patterns(pattern, av)
    if alt_patterns:
        print('alt_patterns', alt_patterns)
        for ap in alt_patterns:
            ''' now replace general with specific and call generate_alt_patterns again '''
            '''
            specific_ap = get_specific_pos(pattern, av)
            specific_alt_patterns = generate_alt_patterns(specific_ap, av)
            if specific_alt_patterns:
                for sap in specific_alt_patterns:
                    all_to_iterate.append(generate_indexed_patterns(sap, av))
            else:
            '''
            all_to_iterate.append(generate_indexed_patterns(ap, av))
    else:
        all_to_iterate.append(generate_indexed_patterns(pattern, av))
    all_patterns = set([x for x in all_to_iterate if type(x) != bool])
    print('\n\tall patterns', len(all_patterns), all_patterns)
    final_patterns = set()
    for ap in all_patterns:
        if len(word_count) > 0:
            synonym_pattern, av = generate_synonym_patterns(ap, av)
            if synonym_pattern:
                final_patterns.add(synonym_pattern)
                final_patterns.add(generate_operator_patterns(synonym_pattern, av))
        final_patterns.add(generate_operator_patterns(ap, av))
    final_patterns = set([x for x in final_patterns if type(x) != bool])
    if len(final_patterns) > 0:
        print('final', len(final_patterns))
        exit()
        return final_patterns, av
    return False, av

def get_pattern_subsets(pattern, av):
    '''        0           1       23       4     5
    'ALL_N DPC |ADJ ADV VB |VBG VBD|| ALL_N |JJ NN|'
    {
      x: |VBG VBD|,
      y: |ADJ ADV VB x|,
      z: |JJ NN|
    }
    0 1 -> cant be embedded because ip[0] == 0
    1 2 -> is 1 2 an inner pair: yes
      is 0 3 an outer pair? yes
    2 3 -> is 2 3 an inner pair? no
      is 1 4 an outer pair? no
    3 4 -> is 3 4 an inner pair? no
      is 2 5 an outer pair? yes
    4 5 -> cant be embedded because ip[1] == (delimiter_count - 1)
    one legit embedded pair (1, 2)
    but both pairs (1, 2) and (4, 5) should be logged as vars
    'ALL_N DPC y ALL_N z'
    '''
    variables = {}
    index_pairs = []
    delimiter_indexes = {}
    strings = []
    tracking_pattern = pattern
    delimiter_count = pattern.count('|')
    if delimiter_count == 0:
        return pattern.count(' ') + 1
    for i, char in enumerate(pattern):
        if char == '|':
            delimiter_index = len(delimiter_indexes.keys())
            delimiter_indexes[delimiter_index] = i
    first_index = delimiter_indexes[0]
    last_index = delimiter_indexes[max(delimiter_indexes.keys())]
    new_subsets = []
    if first_index > 0:
        initial = pattern[0: first_index]
        new_subsets.append(initial)
    for count, char_pos in delimiter_indexes.items():
        if (count + 1) < len(delimiter_indexes.keys()):
            index_pairs.append([count, count + 1])
    if len(index_pairs) > 0:
        for i, ip in enumerate(index_pairs):
            new_key = get_new_key(variables, pattern, av)
            substring = pattern[delimiter_indexes[ip[0]]:delimiter_indexes[ip[1]] + 1]
            if '|' in substring:
                subset = substring.replace('|', '').strip()
                delimiter_joined = ''.join(['|', subset, '|'])
                if delimiter_joined != '||' and delimiter_joined in substring:
                    ''' inner_pair is an alt set, possible embedded pair '''
                    value_for_embedded_pair = get_var_for_embedded(delimiter_joined, delimiter_indexes, index_pairs, i, 1, variables, pattern, av)
                    if value_for_embedded_pair:
                        variables[new_key] = value_for_embedded_pair
                        value_without_embedded_pair = value_for_embedded_pair.replace(delimiter_joined, '').replace('|','')
                        if value_without_embedded_pair.strip() == new_subsets[-1].strip():
                            new_subsets.pop()
                    else:
                        variables[new_key] = delimiter_joined
                    new_subsets.append(new_key)
                else:
                    new_subsets.append(subset)
            else:
                new_subsets.append(substring)
    if last_index < (len(pattern) - 1):
        final = pattern[last_index:]
        new_subsets.append(final)
    if len(new_subsets) > 0:
        return new_subsets, variables
    return False, False

def get_var_for_embedded(delimiter_joined, delimiter_indexes, index_pairs, i, offset, variables, pattern, av):
    delimiter_count = max(delimiter_indexes.keys())
    if (i - offset) >= 0 and (i + offset) < delimiter_count:
        prev_index = index_pairs[i - offset][0]
        next_index = index_pairs[i + offset][1]
        ''' if the pair is the first or last pair it cant be embedded '''
        outer_substring = pattern[delimiter_indexes[prev_index]:delimiter_indexes[next_index] + 1]
        if delimiter_joined in outer_substring:
            ''' outer pair is an alt set as well, check next outer pair '''
            next_outer_delimiter_joined = get_var_for_embedded(outer_substring, delimiter_indexes, index_pairs, i, offset + 1, variables, pattern, av)
            if next_outer_delimiter_joined:
                new_key = get_new_key(variables, pattern, av)
                return next_outer_delimiter_joined
            return outer_substring
    return False

def convert_to_pos_type(word, nonnumeric_w, pos_type, av):
    is_supported = is_supported_tag(nonnumeric_w, av)
    if is_supported:
        ''' pos type '''
        if pos_type == 'specific':
            return nonnumeric_w
        else:
            for pos_key, values in av['tags'].items():
                if nonnumeric_w in values:
                    return pos_key
    else:
        ''' word '''
        pos = get_nltk_pos(nonnumeric_w, av)
        if pos:
            if pos_type == 'specific':
                return pos
            else:
                for pos_key, values in av['tags'].items():
                    if pos in values:
                        return pos_key
    return False

def is_supported_tag(var, av):
    if var in av['tags']['ALL'] or var in av['tags']:
        return True
    return False

def get_nonnumeric(var, av):
    if var:
        nonnumeric_var = ''.join([x for x in var if x.lower() in av['alphabet'] or x == '_' or x == ' '])
        if len(nonnumeric_var) > 0:
            return nonnumeric_var
    return var

def get_new_key(key_dict, source_line, av):
    new_key = None
    upper_limit = len(av['alphabet']) - 1
    random_index = random.randint(0, upper_limit)
    random_letter = av['alphabet'][random_index]
    if key_dict:
        for k in key_dict:
            new_key = ''.join([k, random_letter])
    else:
        new_key = random_letter
    if new_key:
        if new_key in key_dict or new_key in source_line.split(' '):
            return get_new_key(key_dict, source_line, av)
        else:
            return new_key
    return False 

def read(path):
    index = None
    if 'DS_Store' not in path:
        if os.path.exists(path):
            with open(path, 'r') as f:
                index = json.load(f) if 'json' in path else f.read()
                f.close()
    return index

def get_singular(word):
    wl = WordList((word))
    singular_list = wl.singularize()
    if len(singular_list) > 0:
        for item in singular_list:
            return item
    return False

def get_stem(word):
    stem = stemmer.stem(word)
    if stem:
        return stem 
    return word

def find_delimiter(line, av):
    delimiters = [c for c in line if c.lower() not in av['alphabet']] 
    if len(delimiters) > 0:
        max_delimiter = max(delimiters)
        if max_delimiter:
            return max_delimiter
    delimiter = ' ' if ' ' in line else ''
    return delimiter

def get_delimiter(line):
    ''' get a delimiter that isnt in the line '''
    delimiter = '***' if '***' not in line else '###'
    return delimiter

''' SIMILARITY FUNCTIONS '''

def get_polarity(line):
    ''' to do: use blob.sentiment_assessments 
            Sentiment(
                polarity=-0.008806818181818186, 
                subjectivity=0.32386363636363635, 
                assessments=[
                    (['positive'], 0.22727272727272727, 0.5454545454545454, None), 
                    (['absence'], -0.0125, 0.0, None), 
                    (['due'], -0.125, 0.375, None), 
                    (['other'], -0.125, 0.375, None)
                ]
            )
    '''
    blob = get_blob(line)
    if blob:
        sentiment = blob.sentiment
        if sentiment:
            if sentiment.polarity:
                return roun(sentiment.polarity, 1)
    return 0

def correct_spelling(line):
    blob = Sentence(line)
    if blob:
        return blob.correct()
    return text

def get_subjectivity(line):
    return line

''' GET STRUCTURAL TYPE FUNCTIONS '''

def get_blob(string):
    if type(string) == str:
        return TextBlob(string)
    return False

def replace_names(row, av):
    # to do: identify all irrelevant proper nouns like place, company, university & individual names
    original_words = row['original_line'].split(' ')
    tagged = pos_tag(word_tokenize(row['line']))
    ''' to do: make sure names are grouped into phrases '''
    for p in row['phrase']:
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
                        if final_name.lower() not in row['noun']:
                            if final_name.lower() not in row['verb']:
                                row['name'].add(final_name) # find names and store separately
    row['line'] = ' '.join([w for w in row['line'].split(' ') if w not in row['name']])
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

def get_ngrams_by_position(word_list, word, x, direction):
    ''' 
    get a list of words of length (2x + 1) in word list starting with word 
    and iterating outward in direction x number of times 
    '''
    list_length = len(word_list)
    word_index = word_list.index(word)
    if word_index:
        start = word_index - x if word_index > x else word_index if direction == 'next' else 0
        end = word_index + x if (word_index + x) < list_length else word_index if direction == 'prev' else list_length
        return word_list[start:end]
    return False

def get_most_common_words(counts, top_index):
    '''
    counts = {
        0: ['words', 'that', 'appeared', 'once'],
        1: ['items', 'shown', 'twice']
    }
    '''
    count_keys = counts.keys()
    if len(count_keys) > 1:
        top_index = len(count_keys) - 1 if len(count_keys) < top_index else top_index
        sorted_keys = reversed(sorted(count_keys))
        max_key = max(count_keys)
        retrieved_index = 0
        max_words = set()
        for k in sorted_keys:
            max_words = max_words.union(counts[k])
            retrieved_index += 1
            if retrieved_index == top_index:
                return max_words
        if len(max_words) > 0:
            return max_words
    return False

def is_condition(asp_words, row, av):
    for word in asp_words:
        if word in av['clause_delimiters']:
            return word
        else:
            pos = row['pos'][word] if word in row['pos'] else get_pos(word)
            if pos not in av['tags']['ALL_N'] or word not in stop:
                return word
    return False

def get_sentence_delimiter(text):
    return '\n' if text.count('\n') > text.count('. ') else '. '

def standardize_delimiter(text):
    blob = get_blob(text)
    if blob:
        sentences = blob.sentences
        if len(sentences) > 0:
            return '\n'.join([s.string for s in sentences])
    delimiter = get_sentence_delimiter(text)
    if delimiter:
        return '\n'.join(text.split(delimiter))
    return False

def standardize_punctuation(line):
    # remove apostrophes, replace brackets with parenthesis
    line = line.replace('[', ' ( ').replace(']', ' ) ').replace("'", '') 
    # replace clause punctuation with comma
    line = line.replace(' - ', ' , ')
    '''
    operator_keys = av['operator_map'].keys()
    for k in operator_keys:
        line = line.replace(k, '')
    '''
    # space comma to avoid conflation with words, then replace double spaces
    line = line.replace(',', ' , ').replace('  ', ' ')
    return line

def remove_stopwords(line, word_map):
    custom_removal = [] #['the', 'a', 'an', 'them', 'they']
    words = line.split(' ') if type(line) == str else line
    word_list = []
    for w in words:
        if '/' in w or '|' in w:
            option = select_option(w, word_map)
            if option:
                word_list.append(option)
        else:
            if w[-1] == 's':
                w = get_singular(w)
            if w not in stopwords.words('english') and w not in custom_removal:
                word_list.append(w)
    if len(word_list) > 0:
        return ' '.join(word_list)
    return line

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

def select_option(alt_phrase, word_map):
    ''' 
        this function translates:
        - expression/activity = expression-activity (different pos = phrase)
        - describes/delineates = describes (same pos, if synonym, choose more common one)
    '''
    delimiter = [c for c in '/|' if c in alt_phrase]
    alts = alt_phrase.split(delimiter)
    alt_pos = [word_map[a] for a in alts]
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
                        if similarity:
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

def get_charge_of_word(word, av):
    if word in av['supported_synonyms']:
        synonym = av['supported_synonyms'][word]
        for synonym_type in av['charge']:
            if synonym in av['charge'][synonym_type]:
                print('get_charge_of_word: found synonym charge', word, synonym, synonym_type)
                return synonym_type
    return False

def get_similarity(base_word, new_word, pos_type, av):
    if pos_type in ['N', 'V', 'ADV', 'ADJ']:
        base_synsets = Word(base_word).get_synsets(pos=pos_type)
        new_synsets = Word(new_word).get_synsets(pos=pos_type)
        if len(new_synsets) > 0 and len(base_synsets) > 0:
            similarity = base_synsets.path_similarity(new_synsets)
            print('\tget similarity', new_synsets, base_synsets, similarity)
            return similarity
    return 0

def get_similarity_to_title(title, row):
    similarity = 0
    if row['line'] != title:
        title_split = title.split(' ')
        both = set()
        for s in row['line'].split(' '):
            if s in title_split:
                both.add(s)
        if len(both) > 0:
            similarity = round(len(both) / len(title_split), 1)
        if similarity:
            row['similarity'] = similarity
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
            docs = get_local_data(paths, docs)
        else:
            paths = [''.join([database_dir, '/', fp]) for fp in os.listdir(database_dir)]
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
    path = path.replace('txt', 'json') if '.json' in path else path
    with open(path, 'w') as f:
        if 'json' in path:
            json.dump(data, f)
        else:
            f.write('\n'.join(data))
        f.close()
    return True

def write_csv(rows, header_list, path):
    if len(rows) > 0:
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

def replace_with_syns(line, word_map, check_types, av):
    new_text = []
    check_types = ['synonym', 'common', 'standard', 'similarity'] if not check_types else check_types
    # dont add stem-similarity replacement bc you still need pos identification
    for w in line.split(' '):
        word = ''.join([x for x in w if x == '-' or x == ' ' or x == '_' or x in av['alphabet']]) # some synonyms have dashes and spaces
        pos = word_map[w] if word_map and w in word_map else get_nltk_pos(w, av)
        if pos:
            if pos not in av['tags']['exclude'] and pos not in av['tags']['DPC']:
                match, check_type = find_matching_synonym(word, pos, check_types, None, av)
                if match:
                    if w not in av['supported_synonyms']:
                        av['supported_synonyms'][w] = match
                    new_text.append(w.replace(word, match))
                    ''' add synonym mapping to avoid checking all check_types for this word in future bc 'synonym' check_type should return it now '''
                else:
                    new_text.append(w)
    if len(new_text) > 0:
        return ' '.join(new_text), av
    return line, av


def get_definitions(word):
    defs = Word(word).definitions
    if defs:
        print('defs', word, defs)
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

def get_syn_from_definition(word, word_pos):
    candidates = set()
    definitions = get_definitions(word)
    if definitions:
        for d in definitions:
            for w in d:
                dpos = get_nltk_pos(w, av)
                if dpos == word_pos:
                    candidates.add(w)
    if len(candidates) > 0:
        '''
        to do: if found other words with same pos in definitions, 
        filter by meaning & similarity to word
        '''
        return candidates
    return False

def standard_text_processing(text, av):
    text = concatenate_species(text.strip())
    text = standardize_delimiter(text)
    text = standardize_punctuation(text)
    article_lines = {}
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = replace_quotes_with_parenthesis(line)
        active_line, av = apply_pattern_map(line, av['pattern_maps']['passive_to_active'], av)
        line = active_line if active_line else line
        if line not in article_lines:
            article_lines[line] = {}
        for word in line.split(' '):
            pos = get_nltk_pos(word, av)
            if pos:
                article_lines[line][word] = pos
            else:
                article_lines[line][word] = ''
        #line = remove_stopwords(line, article_lines[line])
        syn_line, av = replace_with_syns(line, article_lines[line], None, av)
        if syn_line:
            article_lines[syn_ine] = article_lines[line]
    if article_lines:
        return article_lines, av
    return False, av
    
def get_operator(verb, av):
    ''' this maps a verb ('reduce' or 'inhibit') to an operator like +, -, = '''
    for charge, values in av['charge'].items():
        if verb == charge or verb in values:
            return charge
        #polarity = get_polarity(verb)
        #operator = '-' if polarity < 0.0 else '+' if polarity > 0.0 else '='
        #return operator
    return False

''' these functions can be used in get_common_synonym(word) or get_common_score(word) '''

def get_synsets(word, pos, av):
    synsets = {}
    if pos:
        pos_lower = str(pos).lower()
        synsets = get_synsets_of_type(word, pos_lower, av)
        if synsets:
            synsets[pos_lower] = synsets
            synsets['count'] = {k : len(v) for k, v in synsets.items()}
    else:
        synsets = {
            'N': get_synsets_of_type(word, 'N', av),
            'V': get_synsets_of_type(word, 'V', av),
            'ADV': get_synsets_of_type(word, 'ADV', av),
            'ADJ': get_synsets_of_type(word, 'ADJ', av)
        }
        synsets['count'] = {k : len(v) for k, v in synsets.items()}
    return synsets

def get_synsets_of_type(word, pos_type, av):
    pos_lib_map = { 'N': NOUN, 'V': VERB, 'ADV': ADV, 'ADJ': ADJ }
    if pos_type in pos_lib_map:
        pos_type = pos_lib_map[pos_type]
        if len(word) > 0 and len(pos_type) > 0:
            synsets = Word(word).get_synsets(pos=pos_type)
            if len(synsets) > 0:
                return [s.name().split('.')[0].lower() for s in synsets]
    return False

def get_common_word(word, pos, av):
    '''
    this should standardize a word like 'enhance' to a verb like 'increase' 
    actually we can replace that for now with a synonym list, as in aggregate_synonyms_of_type()
    '''
    if word in av['supported_synonyms']:
        return av['supported_synonyms'][word]
    if pos:
        if pos in av['tags']['SYNSET']:
            synsets = get_synsets(word, pos, av)
            if synsets:
                for supported_tag, synset_list in synsets.items():
                     if len(synset_list) > 0:
                        counts = {}
                        for item in synset_list:
                            if item not in counts:
                                counts[item] = 0
                            counts[item] += 1
                        max_value = max(counts.values())
                        max_synonyms = [c for c in counts if counts[c] == max_value]
                        if len(max_synonyms) > 0:
                            for syn in max_synonyms:
                                similar_score = get_similarity(word, syn, pos_type, av) 
                                if similar_score > 0.5:
                                    return syn
                            return max_synonyms[0]
    return word

def find_matching_synonym(word, pos, check_types, exclude_types, av):
    items = {}
    default_check_types = [
        'standard', 'stem', 'substring', 'type', 'pos', 'partial',
        'synonym', 'common', 'ratio', 'charge', 'similarity'
    ]
    if len(word) > 0:
        if check_types != 'definition':
            if not check_types:
                check_types = default_check_types
            if exclude_types:
                for exclude_type in exclude_types:
                    check_types = check_types.remove(exclude_type)
            match, check_type = iterate_through_synonyms(av, check_types, word, pos)
            if match and check_type:
                return match, check_type
            #print('no matches found', word, pos, check_types)
            return word, check_types[0]
        ''' if no matches found, check for syns of words in definition '''
        if pos in av['tags']['SYNSET']:
            definitions = get_definitions(word)
            if definitions:
                for d in definitions:
                    d_row = get_structural_metadata(d, av)
                    if d_row:
                        if 'verb' in d_row:
                            for v in d_row['verb']:
                                ''' for each verb in the definition, do same synonym check '''
                                match, check_type = iterate_through_synonyms(av, check_types, v, pos)
                                if match and check_type:
                                    print('found matches', word, check_type, match)
                                    return match, check_type
    ''' as a backup, you can query pattern, function, & relationship data to derive standard verb '''
    return False, False

def iterate_through_synonyms(av, check_types, word, pos):
    for key, val in av['supported_synonyms'].items():
        for check_type in check_types:
            if len(word) > 0:
                keyword_match, check_type = matches(word, pos, key, check_type, 'word', av)
                if keyword_match and check_type:
                    return keyword_match, check_type
    return False, False

def matches(word, word_pos, k, check_type, word_type, av):
    ''' word_type can be line, phrase, or word '''
    ''' add synsets option '''
    words = [word] if word_type != 'line' else word.split(' ')
    for w in words:
        if k and w:
            pos_k = get_nltk_pos(k, av)
            if check_type == 'standard':
                w = conjugate(w, word_pos, 'VB', av) # standardize tense to infinitive
                k = conjugate(k, pos_k, 'VB', av)
            elif check_type == 'stem':
                if w in av['supported_stems'] and k in av['supported_stems']:
                    w = av['supported_stems'][w]
                    k = av['supported_stems'][k]
                else:
                    w = stemmer.stem(w)
                    k = stemmer.stem(k)
            elif check_type == 'substring':
                if w in k or k in w:
                    return k, check_type
            elif check_type == 'type':
                w = find_type(w, word_pos, None, None, av)
                k = find_type(k, pos_k, None, None, av)
            elif check_type == 'pos':
                w = word_pos
                k = pos_k
            elif check_type == 'partial':
                w = get_partial_match(av, w, 'synonym')
                k = get_partial_match(av, k, 'synonym')
            elif check_type == 'synonym':
                w = av['supported_synonyms'][w] if w in av['supported_synonyms'] else None
                k = av['supported_synonyms'][k] if k in av['supported_synonyms'] else None
            elif check_type == 'common':
                w = get_common_word(w, word_pos, av)
                k = get_common_word(k, pos_k, av)
            elif check_type == 'ratio':
                ratio = get_match_ratio(w, k)
                if ratio:
                    if ratio > 0.9:
                        return k, check_type
            elif check_type == 'charge':
                w = get_charge_of_word(w, av)
                k = get_charge_of_word(k, av)
            elif check_type == 'similarity':
                similarity = get_similarity(w, k, word_pos, av)
                if similarity > 0.9:
                    return k, check_type
            if w and k:
                if w == k:
                    return k, check_type
    return False, False

def get_partial_match(av, word, match_type):
    ''' to do: add lemmatize + suffix check to get_partial_match function '''
    ''' match_type = ['synonym', 'bool', 'keyword'] '''
    for k, v in av['supported_synonyms'].items():
        if k[0] == '-' or k[-1] == '-':
            new_k = k.replace('-', '')
            word_split = word.split(new_k)
            if len(word_split) == 2:
                if (k[0] == '-' and word_split[-1] == '') or (k[-1] == '-' and word_split[0] == ''):
                    return True if match_type == 'bool' else v if match_type == 'synonym' else new_k
        else:
            ''' to do: integrate similarity & pos matching '''
            ratio = get_match_ratio(word, k)
            threshold = 0.7 # should be at threshold just under 8/13 to capture rational => rationalizing
            if ratio > threshold:
                return True if match_type == 'bool' else v if match_type == 'synonym' else k
        if len(k) > 5 and len(word) > 5 and k in word or word in k and (len(k) - len(word)) <= 5:
            return True if match_type == 'bool' else v if match_type == 'synonym' else k
    return False

def get_match_ratio(word, keyword):
    last_index = len(keyword) - 1
    reversed_indexes = reversed(range(0, last_index))
    for length in reversed_indexes:
        remainder = keyword[length:]
        if remainder in word:
            return round(len(remainder) / len(word), 1)
    for length in reversed_indexes:
        for offset in reversed_indexes:
            if length < len(keyword):
                if offset < length:
                    subset = keyword[offset:length]
                    if subset in word:
                        return round(len(subset) / len(word), 1)
    return False

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
                    next_item = data_lines[i+1].strip().split(' ')[0] if (i + 1) < len(data_lines) else ''
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

def conjugate(word, source_pos, target_pos, av):
    ''' convert word from source_pos to target_pos '''
    target_endings = {
        'VB': '',
        'VBP': '',
        'VBZ': 's',
        'VBG': 'ing',
        'VBD': 'ed',
        'VBN': 'ed'
    }
    case_maps = {
        'be': {'VB': 'is', 'VBD': 'was', 'VBG': 'is', 'VBN': 'been', 'VBP': 'is', 'VBZ': 'is'},
        'do': {'VB': 'do', 'VBD': 'did', 'VBG': 'doing', 'VBN': 'done', 'VBP': 'do', 'VBZ': 'does'},
        'have': {'VB': 'have', 'VBD': 'had', 'VBG': 'having', 'VBN': 'had', 'VBP': 'have', 'VBZ': 'has'}
    }
    nonnumeric_s_pos = get_nonnumeric(source_pos, av)
    nonnumeric_t_pos = get_nonnumeric(target_pos, av)
    if nonnumeric_s_pos != nonnumeric_t_pos:
        is_source_supported = is_supported_tag(nonnumeric_s_pos, av)
        is_target_supported = is_supported_tag(nonnumeric_t_pos, av)
        if is_source_supported and is_target_supported:
            if (
                (nonnumeric_s_pos == 'V' or nonnumeric_s_pos in av['tags']['V']) and 
                (nonnumeric_t_pos == 'V' or nonnumeric_t_pos in av['tags']['V'])
            ):
                equivalent = ['VB', 'VBG', 'VBP'] # 'VBG', 'VBN', 'VBD', 'VBZ'
                infinitive = lemmatizer.lemmatize(word, 'v')
                stem = stemmer.stem(infinitive)
                new_word = ''.join([stem, target_endings[target_pos]])
                if infinitive in case_maps:
                    return case_maps[infinitive][target_pos]
                if target_pos == 'VB':
                    return infinitive
                ''' remove trailing e/s if applicable '''  
                if penultimate_char not in 'aeiou' and last_char == 's':
                    word = word[0:-1]
                elif 'ies' == word[-3]:
                    word = ''.join([word[0:-3], 'y'])
                elif penultimate_char in 'aeiou' and last_char == 's':
                    word = word[0:-2]
                return new_word
    return False

def get_patterns_between_objects(objects, object_type, av):
    '''
    this function is to determine patterns using each object in the list as input
    to find patterns between list items
    since we're passing in index[keys] to this function,
    we'll be handling lists of objects like strategies
    to find patterns in strategy objects,
    youd abstract the objects in each strategy and check if that abstract version occurs elsewhere

    example:
        with inputs:
            objects = [
                'look before you leap',
                'check yourself before you wreck yourself'
            ]
        this function would identify the pattern these strategies have in common:
            abstract_pattern = "use caution to prevent adverse events"

        this function would return:
            pattern = "apply(context, style, abstract_strategy) => metaphorical_strategy"

        Example of applying the abstract_pattern to produce a strategy:

            apply(context="crossing a gap", style=None, strategy=abstract_pattern) = 'look before you leap'
                - the adverse event possible in the context of "crossing a gap" is "falling in the gap"
                - the method of using caution in the context of "crossing a gap" is "looking"

            apply(context="prepare_for_social_situation", style="slang", strategy=abstract_pattern) = 'check yourself before you wreck yourself'
                - the adverse event possible in the context of "prepare_for_social_situation" is "wrecking yourself"
                - the method of using caution in the context of "prepare_for_social_situation" is "checking yourself"
    '''
    return objects

def index_as_functions(line):
    ''' this is to convert relationships in line into a function object
        example: "x could possibly generate y" outputs the following object:
            function = {
                input="object(x)", 
                attribute="possible", 
                intent="generate", 
                type="causative",
                output="object(y)"
            }

        - functional patterns:
            - are more complicated than pos/string/type patterns, and are returned from get_functions(line)
            - rely heavily on the verb or verb phrases and conditional operators
            - if its a supported type like strategy or insight you dont need to wrap it with object() syntax
            - each argument to function inputs, relation, and outputs should be another function object
            - we use relation as a param to the function to differentiate them 
            - indexing info this way makes storing function pattern_maps & advanced system analysis queries possible

        - syntax: 
            - y.function(x) indicates its a process of some external object acting on x
                "pathway regulation" => regulatory_system.regulating(pathway)
            - a function of x would be indicated similarly:
                "x.function(a)" => pathway.adapt("receptor_A")

        - example:
            original_line = 'Understanding how this pathway is regulated could lead to new strategies to treat both diseases'
                function=(
                    input=(
                        function(input="object(pathway)", attribute="pathway.regulation", output="insight")
                          # ----------------------- Understanding of 'pathway regulation'
                    ),
                    relation=(
                        function(input="relation", attribute="possible", intent="generate", output="function") 
                    ),    # ----------------------- could generate
                    output=(
                        function(
                            input="object([diabetes, cancer], type=medical_condition)", 
                            output="strategy(attribute=[new, multiple], intent=treatment)"
                        ) # ----------------------- strategies to treat both diseases
                    )
                )
            which abstracts to the function pattern:
                function=(
                    input=(function(input="object(x)", attribute="y.function(x)", output="insight")),
                    relation=(function(input="function.name", attribute=function.attribute, intent=function.intent, output=function)),
                    output=(function(input="object(objects), type=objects.type", output="strategy(attribute=strategy.attributes, intent=strategy.intent)"))
                )
    '''
    return line

def apply_pattern_map(line, pattern_map, av):
    ''' 
    - this replaces a pattern with its associated pattern found in the line using variables 
        apply_pattern_map(line='dog of cat', pattern_map = {'noun1 of noun2' => 'noun2 noun1'}) = 'cat dog'
    to do:
        - for object_type in ['word', 'modifier', 'phrase'] - these should already be replaced with option sets of each type pattern 
        - modifier1 should be replaced with each modifier pattern + 1 and used to generate a new pattern containing each modifier pattern
        - when the source pattern is 'VBD VBN' and the target is 'VBZ' you need to isolate the 'VBN' which is the more meaningful verb
            currently its getting overridden by the consecutive verb which also matches the 'V' type but need a more robust way
        - in order to support iterated replacement, you need to make sure your patterns are ordered in the right way
    '''
    print('apm')
    exit()
    pos_lines, av = get_all_versions(line, 'all', av)
    if pos_lines:
        for pos_line in pos_lines:
            for source_pattern, target_pattern in pattern_map.items():
                new_line = apply_pattern(pos_line, source_pattern, target_pattern, av)
                if new_line:
                    print('applied pattern to line', new_line)
                    print('sp', source_pattern, 'tp', target_pattern)
                    line = new_line # return new_line if not iterating through all patterns in map
    return line, av

def find_pattern(line, av):
    ''' to do: this is to cluster repeated patterns in a lines list '''
    return False

def match_patterns(line, pattern_key, av):
    '''
    if line is a sequence, get patterns between objects in the list,
    rather than patterns in a line
    '''
    print('mp')
    exit()
    found_patterns = {}
    if type(line) == list or type(line) == set:
        found_patterns = get_patterns_between_objects(line)
    else:
        pos_lines, av = get_all_versions(line, av) 
        if pos_lines:
            if len(pos_lines) > 0:
                for pos_line in pos_lines:
                    if pattern_key in av['pattern_index']:
                        combined_key = ''.join([pattern_key, '_pattern'])
                        for pattern in av['pattern_index'][pattern_key]:
                            '''
                            only want to generate source patterns here, 
                            send a flag to not generate target patterns
                            '''
                            found_subsets, av = get_pattern_source_subsets(line, pos_line, pattern, 'pattern', av)
                            if found_subsets:
                                if combined_key not in found_patterns:
                                    found_patterns[combined_key] = {}
                                found_patterns[combined_key][pattern] = found_subsets
    if found_patterns:
        return found_patterns, av
    return False, av

def apply_pattern(subset, source_pattern, target_pattern, av):
    ''' subset = "inhibitor of compound", source_pattern = "VBZ of NN", target_pattern = "NN VBG"
        output = "compound-inhibitor"
        to do:
        - handle target patterns with more words than source
        - handle other delimiters than space in case your source pattern has no spaces
        - syntax delimiters ('|', '&') should be handled in prior processing in generate_alt_patterns
        - return False if source_pattern not in subset
    '''
    print('apply_pattern', subset, source_pattern, target_pattern)
    delimiter = find_delimiter(subset, av)
    if delimiter:
        ''' create a position map for source & target '''
        new_words = {}
        position_map = {}
        positions = {'source': {}, 'target': {}}
        source_words = source_pattern.split(delimiter)
        target_words = target_pattern.split(delimiter)
        for position, w in enumerate(source_words):
            positions['source'][position] = w
            positions['target'][position] = target_words[position] if position < len(target_words) else ''
        ''' positions = { 'source': {0: 'x', 1: 'of', 2: 'y'}, 'target': {0: 'y', 1: '', 2: 'x'} } '''
        for source_position, source_word in positions['source'].items():
            for target_position, target_word in positions['target'].items():
                if source_word == target_word:
                    ''' to do: exact word match or (supported_tag) '''
                    position_map[source_position] = target_position
                else:
                    if source_word in av['tags']['ALL_V'] and target_word in av['tags']['ALL_V']:
                        position_map[source_position] = target_position
        ''' apply position_map to words in subset: position_map = {0: 2, 1: '', 2: 0} '''
        for source_position, source_word in enumerate(subset.split(delimiter)):
            for sp, tp in position_map.items():
                if sp == source_position:
                    source_var = positions['source'][sp]
                    target_var = positions['target'][tp]
                    nonnumeric_source_var = get_nonnumeric(source_var, av)
                    nonnumeric_target_var = get_nonnumeric(target_var, av)
                    source_is_var = is_supported_tag(nonnumeric_source_var, av)
                    target_is_var = is_supported_tag(nonnumeric_target_var, av)
                    if source_is_var and target_is_var:
                        ''' variable: conjugate if different, add if equal '''
                        if source_var != target_var:
                            conjugated_word = conjugate(source_word, source_var, target_var, av)
                            if conjugated_word:
                                new_words[tp] = conjugated_word
                        else:
                            new_words[tp] = source_word
                    else:
                        ''' not a variable: include index matches ('the': 'the0') but not positional/non-content matches ('x': 'the') '''
                        if source_var == source_word or nonnumeric_source_var == source_word:
                            new_words[tp] = source_word
        if new_words:
            new_items = [new_words[k] for k in sorted(new_words.keys()) if k in new_words]
            if len(new_items) > 0:
                return delimiter.join(new_items)
    return False

def get_pattern_source_subsets(line, pos_line, pattern, get_type, av):
    ''' get only the matching subsets from line with words in the same positions & pos as pattern
        ['pattern_instance_1', 'pattern_instance_2']
        support numerical variables by checking non-numeric pattern for match with pos_line 
        to do: this prevents users from configuring patterns with numbers like 14alpha-deoxy-enzyme
    '''
    print('gpss')
    exit()
    delimiter = find_delimiter(line, av)
    pos_patterns, av = get_all_versions(pattern, av) 
    if pos_patterns and delimiter:
        if len(pos_patterns) > 0:
            subsets = []
            for pos_pattern in pos_patterns:
                if pos_pattern == pos_line:
                    return [pattern]
                if pos_pattern in pos_line:
                    if get_type == 'pattern':
                        subsets = get_pattern_source_words(line, pos_line.split(pos_pattern))
                    else:
                        ''' split a line into subsets so each pattern section is in its own subset '''
                        ''' ['pattern_instance_1', 'non-pattern-words', 'pattern_instance_2', 'other non-pattern words'] '''
                        non_patterns = pos_line.split(pos_pattern)
                        sources = get_pattern_source_words(line, non_patterns)
                        if sources:
                            for i, subset in enumerate(sources):
                                ''' to do: convert back to original line subset '''
                                subsets.append(subset)
                                if i < len(non_patterns):
                                    subsets.append(non_patterns[i])
            if subsets:
                if len(subsets) > 0:
                    return subsets, av
    return False, av

def get_pattern_source_words(source_line, exclude_list):
    ''' get source words in same positions as pattern '''
    ''' ('a b c', ['b']) == ['a', 'c'] '''
    delimiter = get_delimiter(source_line)
    for word_set in exclude_list:
        if word_set in source_line:
            source_line = source_line.replace(word_set, delimiter)
    source_subsets = source_line.split(delimiter)
    if source_subsets:
        if len(source_subsets) > 0:
            return source_subsets
    return False

def convert_to_operators(line, av):
    # check for synonym first: 'reduced' has polarity 0.0
    variables = {}
    new_words = []
    words = line.split(' ')
    for i, word in enumerate(words):
        found_operator = get_operator(word, av)
        if found_operator:
            if variables:
                operator_count = 0
                for k in variables:
                    if found_operator in k:
                        operator_count += 1
                if operator_count > 0:
                    operator_count += 1
                indexed_operator = ''.join([found_operator, str(operator_count)])
                variables[indexed_operator] = word # {variables['+1'] = 'enables'}
                new_words.append(indexed_operator)
            else:
                variables[found_operator] = word
                new_words.append(found_operator)
        else:
            if word in av['supported_synonyms']:
                common_verb = av['supported_synonyms'][word]
                operator = get_operator(common_verb, av)
                if operator:
                    new_words.append(operator)
                else:
                    new_words.append(common_verb)
            else:
                new_words.append(word)
    if len(new_words) > 0:
        return ' '.join(new_words), variables
    return False, False

def get_nltk_pos(word, av):
    if '_' in word or word in [a for a in av['alphabet']]:
        ''' this is a variable, dont modify '''
        return False
    tags = TextBlob(word).parse()
    tags_split = tags.split('/')
    blob_pos = tags_split[1] if len(tags_split) > 1 else None
    tagged = pos_tag(word_tokenize(word))
    if len(tagged) > 0:
        for item in tagged:
            if len(item) > 0:
                if blob_pos != item[1]:
                    ''' blob identifies 'explains' as a verb when pos_tag doesnt '''
                    if blob_pos in av['tags']['ALL_V']:
                        return blob_pos
                return item[1]
    return False
import wikipedia
from wikipedia.exceptions import DisambiguationError
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

from get_medical_objects import find_generic_medication
from get_pos import *

wikipedia.set_lang("en")
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english'))

def get_pattern_config(av):
    av['verb_meanings'] = ['action']
    av['negative_meanings'] = ['down']
    av['positive_meanings'] = ['up']
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
    for k, v in av['charge'].items():
        if k == '=':
            av['charge'][k] = av['charge'][k].union({'is'})
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
    av['clause_delimiters'] = reversed(sorted(av['clause_delimiters']))
    abstract_verbs = ['find', 'derive', 'build', 'test', 'apply']
    med_objects = ['treatment', 'compound', 'test', 'metric', 'mechanism']
    study_objects = ['relationship', 'limit', 'type', 'method']
    conceptual_objects = ['relationship', 'problem', 'strategy', 'process', 'insight', 'function', 'variable', 'system', 'theory', 'opinion', 'conclusion', 'observation']
    av['info_types'] = ['excuse', 'opinion', 'fact', 'lie', 'belief', 'joke', 'insight', 'reason', 'intent', 'strategy']
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
    ''' *** IMPORTANT PATTERN CONFIG INFO ***

        - for pattern configurations, always put the extended pattern first
            - if you put '<noun>' before "<noun> <noun>',
                you'll miss phrases like 'compound acid' returning matches like:
                     ['compound acid']
                and will instead get matches for the '<noun>' pattern:
                    ['compound', 'acid']
                so make sure thats what you want before ignoring this rule

        - pattern_syntax: 
            - __a__ : an optional item
            - |a b c| : a set of alternatives, each of which will be selected one at a time in the output patterns
            - if you include 'N' in your pattern, it'll replace it with all the noun pos tags, like |NN NNS NNP NNPS| etc
    '''
    av['computed_pattern_maps'] = {}
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
        }
    }
    av['convert_map'] = {
        'could not have been done': 'was impossible',
        'could not have': 'cannot',
        'could have been done': 'was possible',
        'could have': 'can',
        'should not have been done': 'was inadvisable',
        'should not have': 'does',
        'should have': 'does not',
        'has not been done': 'did not',
        'had been done': 'did',
        'into': 'to'
    }
    av['pattern_vars'] = [item for item in av['tags'].keys()]

    ''' the type_index is to store combinations of other type variables like noun_phrase & general variables like x '''
    av['computed_type_index'] = {}
    av['computed_pattern_index'] = {}
    av['type_index'] = {
        'passive_identifier': [
            'noun_phrase1 of noun_phrase2' # enzyme inhibitor of protein synthesis - to do: there are some examples where this structure adds clarity rather than just adding words, like where modifier relationships arent clear
        ],
        'modifier_identifier': [],
        'noun_phrase': [],
        'verb_phrase': []
    }
    '''
        'clause_identifier': [],
        'phrase_identifier': [
            'modifier_identifier DPC modifier_identifier'
        ],
        'relationship_identifier': [
            'phrase_identifier phrase_identifier V clause_identifier',
        ],
        'rule_identifier': [
            'if x then y',
        ],
        'condition_identifier': [],
        'compound_identifier': [
            "rule_identifier of compound_identifier",
            "compound_identifier compound_identifier"
        ],
        'context_identifier': [
            'given',
            'when x',
            'if x',
            'even x',
            'while x',
            'with x',
            'without x'
        ],
        'symptom_identifier': [
            'N that gets worse when context_identifier',
            'x - y & - z even in condition_identifier or condition_identifier'
        ]
    '''
    av['pattern_index'] = {
        'passive_identifier': [
            '|VB VBP VBN VBD| |VB VBP VBN VBD|', # is done, was done
            'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', # having been done
            '|VB VBP VBN VBD| |TO IN PP|', # finish by, done by
            '|VBD| VBN VBN |TO IN PP|', # has been done by
        ],
        'subject_identifier': [
            'ALL_N ALL_V',
        ],
        'modifier_identifier': [
            #'(?)', # add support for an any character 
            '|ALL_N ALL_V| |ALL_N ADV ADJ ALL_V|', # compound isolate
            'NNP ALL_N', # Diabetes mellitus
            'ALL_N ALL_N', # the second noun may have a verb root, ie "enzyme-inhibitor"
            'ALL_N ALL_V',
            'JJ NN'
        ],
        'phrase_identifier': [
            'ALL_N DPC |ADJ ADV VB VBG VBD| ALL_N', # converter of ionic/ionized/ionizing radiation, necrotizing spondylosis
            'ALL_N DPC ALL_N |VBG VBD|', # metabolite of radiation poisoning
            'ALL_N DPC ALL_N', # metabolite/metabolizer/inhibitor/alkalization of radiation, 
        ],
        'clause_identifier': [
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
        'type_identifier': [
            'ADJ ALL_N', # Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')
        ],
        'role_position': [
            'ADV |ALL_V ALL_N|', # Ex: 'emulsifying protein' (role = 'emulsifier')
        ]
    }
    for key in av['type_index']:
        av['pattern_vars'].append(key)
    for key in av['pattern_index']:
        av['pattern_vars'].append(key)
    av['pattern_vars'] = set(av['pattern_vars'])
    av['all_pattern_version_types'] = ['correct', 'indexed', 'nested', 'alt', 'pos', 'type', 'synonym', 'operator', 'function', 'maps']
    ''' 
    now that pattern lists are generated, 
    populate pattern types from type_index[key[
    with all variants from the corresponding list in pattern_index[key]
    '''
    for key, type_index in av['type_index'].items():
        new_type_index = []
        for type_pattern in type_index:
            for sub_pattern_type, sub_pattern_list in av['pattern_index'].items():
                nonnumeric_index_type = get_nonnumeric(sub_pattern_type, av)
                nonnumeric_type_pattern = get_nonnumeric(type_pattern, av)
                ''' if 'modifier' in ['modifier', 'DPC', 'modifier'] '''
                if nonnumeric_index_type in nonnumeric_type_pattern.split(' '):
                    ''' iterate through modifiers pattern_index, replacing nonnumeric_index_type with index pattern '''
                    for sub_pattern in sub_pattern_list:
                        new_type_pattern = nonnumeric_type_pattern.replace(nonnumeric_index_type, sub_pattern)
                        new_type_index.append(''.join(new_type_pattern))
        if len(new_type_index) > 0:
            if key in av['pattern_index']:
                av['pattern_index'][key].extend(new_type_index)
    ''' if there are files with the 'data/objecttype_patterns.txt' name pattern, pull that data and add it to pattern_index dict  '''
    av = update_patterns(av)
    return av

def update_patterns(av):
    '''
    if 'data/all_patterns.txt' found, 
        read patterns & sort into pattern_index/type_index lists
    otherwise 
        generate patterns for pattern_index & type_index patterns
        & generate patterns for source/target patters in pattern maps 
        and save all generated patterns in 'data/all_patterns.txt'
    '''
    print('function::update_patterns')
    all_pattern_filename = ''.join([os.getcwd(), '/data/all_patterns.txt'])
    if os.path.exists(all_pattern_filename):
        pattern_contents = read(all_pattern_filename)
        if pattern_contents:
            for line in pattern_contents.split('\n'):
                pattern_split = line.split('::')
                if len(pattern_split) > 0:
                    pattern_index = pattern_split[0]
                    pattern_key = pattern_split[1]
                    pattern = pattern_split[2]
                    if pattern_key not in av[pattern_index]:
                        av[pattern_index][pattern_key] = []
                    if pattern_index == 'pattern_maps':
                        pattern_map = pattern.split(':')
                        av[pattern_index][pattern_key][pattern_map[0]] = pattern_map[1]
                    else:
                        av[pattern_index][pattern_key].append(pattern)
    else:
        new_pattern_lines = []
        for pattern_index in ['pattern_index', 'type_index']:
            pattern_index_name = ''.join(['computed_', pattern_index])
            for pattern_key, patterns in av[pattern_index].items():
                for original_pattern in patterns:
                    print('function::update_patterns - get_all_versions in original_pattern', original_pattern)
                    generated_patterns, av = get_all_versions(original_pattern, 'all', av) 
                    if generated_patterns:
                        all_patterns = [pattern for pattern_type, patterns in generated_patterns.items() for pattern in patterns]
                        for pattern in all_patterns:
                            new_pattern_lines.append('::'.join([pattern_index, pattern_key, pattern]))
                        for pattern_type, patterns in generated_patterns.items():
                            if pattern_type not in av[pattern_index_name]:
                                av[pattern_index_name][pattern_type] = []
                            av[pattern_index_name][pattern_type].extend(patterns)
                    else:
                        new_pattern_lines.append('::'.join([pattern_index, pattern_key, original_pattern]))
        version_types = [x for x in av['all_pattern_version_types'] if x != 'maps']
        for pattern_map_key, pattern_map in av['pattern_maps'].items():
            if pattern_map_key not in av['computed_pattern_maps']:
                av['computed_pattern_maps'][pattern_map_key] = {}
            for sp, tp in pattern_map.items():
                print('function::update_patterns - get_all_versions in sp', sp, 'tp', tp)
                sp_pattern_index, av = get_all_versions(sp, version_types, av) 
                tp_pattern_index, av = get_all_versions(tp, version_types, av) 
                if sp_pattern_index and tp_pattern_index:
                    if 'standard' in sp_pattern_index and 'standard' in tp_pattern_index:
                        sp_pattern_index['standard'] = list(sp_pattern_index['standard'])
                        tp_pattern_index['standard'] = list(tp_pattern_index['standard'])
                        for pattern_type, sp_patterns in sp_pattern_index.items():
                            if pattern_type not in av['computed_pattern_index']:
                                av['computed_pattern_index'][pattern_type] = []
                            av['computed_pattern_index'][pattern_type].extend(sp_patterns)
                        for pattern_type, tp_patterns in tp_pattern_index.items():
                            if pattern_type not in av['computed_pattern_index']:
                                av['computed_pattern_index'][pattern_type] = []
                            av['computed_pattern_index'][pattern_type].extend(tp_patterns)
                        for i, sp_item in enumerate(sp_pattern_index['standard']):
                            if i < len(tp_pattern_index['standard']):
                                tp_item = tp_pattern_index['standard'][i]
                                new_pattern_lines.append('::'.join(['pattern_maps', pattern_map_key, ':'.join([sp_item, tp_item])]))
                                av['computed_pattern_maps'][pattern_map_key][sp_item] = tp_item
        if len(new_pattern_lines) > 0:
            av['all_patterns'] = list(set(reversed(sorted(new_pattern_lines))))
            save(all_pattern_filename, av['all_patterns'])
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
        'wiki': ['section_list'],
        'request': ['metadata', 'generate', 'filters', 'data'], # request params
        'pos': ['pos', 'verb', 'noun', 'common_word', 'count', 'taken_out', 'clause_marker', 'line', 'prep', 'conj', 'det', 'descriptor', 'original_line', 'word_map'],
        'structure': ['type', 'name', 'ngram', 'modifier', 'phrase', 'noun_phrase', 'verb_phrase', 'clause', 'subject', 'relationship', 'pattern', 'similar_line'], # structural
        'experiment': ['hypothesis', 'test', 'metric', 'property', 'assumption'], # experiment elements
        'compound': ['compound', 'contraindication', 'interaction', 'side_effect', 'treatment', 'treatment_successful', 'treatment_failed'], # drug elements
        'organism': ['gene', 'expression', 'evolution', 'organ', 'cell', 'nutrient'],
        'condition': ['symptom', 'condition', 'diagnosis', 'phase'], # separate diagnosis bc theyre not always accurate so not equivalent to condition
        'context': ['bio_metric', 'bio_symptom', 'bio_condition', 'bio_stressor'], # context elements
        'synthesis': ['instruction', 'parameter', 'optimal_parameter', 'substitute', 'equipment'],
        'relational': ['component', 'related', 'alternate', 'substitute', 'sub', 'adjacent', 'stressor', 'dependency'],
        'conceptual': ['concept', 'variable', 'function', 'causal_stack', 'insight', 'strategy', 'prediction', 'priority', 'intent', 'system']
    }
    av['default_objects'] = [
        'structure', 'type', 'pattern', 'metric', 'property', 'assumption', 'parameter', 
        'optimal_parameter', 'stressor', 'dependency', 'concept', 'variable', 'function', 
        'causal_stack', 'insight', 'strategy', 'prediction', 'priority', 'intent', 'system'
    ]
    av['related_metadata'] = {
        'component': ['related', 'alternate', 'substitute', 'sub', 'adjacent'],
        'experiment': ['hypothesis', 'threshold', 'metric', 'test', 'conclusion'],
        'test': ['metric', 'equipment', 'measurement', 'accuracy'],
        'contraindication': ['compound', 'treatment', 'symptom', 'condition'],
        'interaction': ['compound', 'treatment', 'symptom', 'condition'],
        'side_effect': ['symptom', 'treatment', 'compound'],
        'compound': ['formula', 'chemical_properties', 'synthesis', 'treatment', 'condition', 'symptom', 'side_effect', 'interaction', 'contraindication'],
        'treatment': ['compound', 'contraindication', 'interaction', 'side_effect', 'treatment_successful', 'treatment_failed'],
        'organism': ['gene', 'organ', 'cell', 'nutrient'],
        'gene': ['expression'],
        'evolution': ['gene', 'nutrient'],
        'organ': ['gene', 'cell', 'nutrient'],
        'cell': ['organelle', 'gene', 'nutrient'],
        'symptom': ['condition', 'treatment', 'diagnosis'],
        'condition': ['symptom', 'treatment', 'diagnosis'],
        'diagnosis': ['test', 'metric', 'symptom', 'condition', 'phase', 'context'],
        'phase': ['condition', 'context', 'symptom'],
        'context': ['bio_metric', 'bio_symptom', 'bio_condition', 'bio_stressor'],
        'synthesis': ['instruction', 'equipment']
    }
    av['definitions'] = {
    
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
                synonym_map = read(full_path)
                if synonym_map:
                    if 'sources' not in filename:
                        for top_element in synonym_map:
                            av['supported_core'][top_element] = synonym_map[top_element]
                            av['supported_stems'][top_element] = set()
                            if type(synonym_map[top_element]) == list:
                                for y in synonym_map[top_element]:
                                    av = process_synonym_element(y, top_element, av)
                            elif type(synonym_map[top_element]) == dict:
                                for k, y in synonym_map[top_element].items():
                                    av['supported_stems'][top_element].add(get_stem(k))
                                    av = process_synonym_element(y, top_element, av)
                                    av = process_synonym_element(y, k, av)     
                    else:
                        av['sources'] = synonym_map
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
    ''' 
    this function is only for translating all_v into list of v tags, not translating words into pos
    convert 'ALL_N' => |NN JJ JJR NNS NNP NNPS RB] 
    '''
    new_subsets = []
    for subset in pattern.split('|'):
        new_words = []
        for word in subset.split(' '):
            nn = get_nonnumeric(word, av)
            if nn:
                tag_list = [x for k, v in av['tags'] for x in v] if nn == 'ALL' else av['tags'][nn] if nn in av['tags'] else None
                if tag_list:
                    new_words.append(''.join(['|', ' '.join(tag_list), '|']))
                elif nn in av['tags']['ALL']:
                    new_words.append(word)
                else:
                    pos = get_nltk_pos(nn, av)
                    if pos:
                        new_words.append(pos)
                    else:
                        new_words.append(word)
            else:
                new_words.append(word)
        if len(new_words) > 0:
            new_subsets.append(' '.join(new_words))
    if len(new_subsets) > 0:
        return '|'.join(new_subsets)
    return False

def get_all_pos(pattern, av):
    ''' convert 'ALL_N' => |N JJ JJR NNS NNP NNPS RB], 'dog' => 'N' '''
    new_subsets = []
    for subset in pattern.split('|'):
        new_words = []
        for word in subset.split(' '):
            nn = get_nonnumeric(word, av)
            if nn:
                tag_list = [x for k, v in av['tags'] for x in v] if nn == 'ALL' else av['tags'][nn] if nn in av['tags'] else None
                if tag_list:
                    new_words.append(''.join(['|', ' '.join(tag_list), '|']))
                elif nn in av['tags']['ALL']:
                    new_words.append(word)
                else:
                    pos = get_nltk_pos(nn, av)
                    if pos:
                        new_words.append(pos)
                    else:
                        new_words.append(word)
            else:
                new_words.append(word)
        if len(new_words) > 0:
            final_words = []
            for word in new_words:
                all_type = ''.join(['ALL_', word])
                if all_type in av['tags']:
                    final_words.append(word)
                else:
                    for tag in av['tags']:
                        tag_type = tag.replace('ALL_','')
                        if word in av['tags'][tag] and tag_type == tag_type.upper() and tag_type != 'SYNSET':
                            final_words.append(tag_type)
                            break
            new_subsets.append(' '.join(final_words))
    if len(new_subsets) > 0:
        return '|'.join(new_subsets)
    return False

def append_list(starting_list, add_list):
    all_lists = []
    if len(starting_list) > 0:
        for sub_list in starting_list:
            for add_item in add_list:
                sub_list_copy = [item for item in sub_list]
                sub_list_copy.append(add_item)
                all_lists.append(sub_list_copy)
    else:
        for sub_item in add_list:
            if type(sub_item) == list:
                all_lists.append(sub_item)
            else:
                all_lists.append([sub_item])
    if len(all_lists) > 0:
        return all_lists
    return False

def generate_indexed_patterns(pattern, av):
    ''' this function adds an integer index to any repeated items '''
    new_words = []
    words = pattern.split(' ')
    for i, w in enumerate(words):
        if w != '':
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

def correct(line):
    blob = get_blob(line)
    if blob:
        #corrected_string = blob.correct().string
        start = line.count('(')
        end = line.count(')')
        if start > end:
            line = ''.join([line, ')'])
        elif start < end:
            line = ''.join(['(', line])
        return line.replace('..', '.').replace(',.', '.').replace('.,', '.').replace(';.', ';').replace('.;', ';').replace(':.', ':').replace('.:', ':')
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
    pattern = correct(pattern)
    if pattern:
        return pattern
    return False

def get_content_from_wiki(keyword, av):
    ''' to do: add support for embedded disambiguation queries returning multiple results '''
    content = None
    suggested = wikipedia.suggest(keyword) if not keyword else keyword
    try:
        content = wikipedia.page(suggested).content
    except Exception as e:
        print('wiki summary exception', e)
    if content:
        sections = {s.strip().replace(' ', '_').lower() for s in content.split('==') if '.' not in s and len(s) < 100}
        print('sections', sections)
        categories = wikipedia.page(suggested).categories
        if len(categories) > 0:
            print('categories', categories)
        return content, sections, categories
    return False, False, False

def find_type(word, pos, title, row, av):
    if pos in av['tags']['ALL_N']:
        ''' make sure this is a noun before querying '''
        if len(word) > 1:
            if word[0] == word[0].upper() and word[1] != word[1].upper():
                suggested = find_generic_medication(word, {}, av)
                print('suggested', suggested, word)
                if suggested:
                    content, sections, categories = get_content_from_wiki(suggested, av)
                    if content and sections and categories:
                        row['type'] = row['type'].union(set(categories))
                        index_type = [val for key, val in av['section_map'].items() for section in sections if key in section]
                        if len(index_type) == 0:
                            index_type = get_index_type(suggested, av, categories)
                        print('found index type', index_type, word)
                        if index_type in row:
                            if index_type != 'dependency': # to do: exclude other relationship objects here
                                found_subsets, av = get_matching_subsets(word, index_type, av)
                                if found_subsets:
                                    for pattern_type in found_subsets.items():
                                        if pattern_type not in row:
                                            row[pattern_type] = set()
                                        for pattern, matches in found_subsets[pattern_type].items():
                                            if pattern not in row[pattern_type]:
                                                row[pattern_type][pattern] = set()
                                            row[pattern_type][pattern] = row[pattern_type][pattern].union(matches)
                                    row['type'].add(index_type)
    return row

def generate_type_patterns(line, av):
    ''' 
        Cytotoxicity in cancer cells => <component object>-toxicity, 
            anti-tumor => anti-<component object of illness>
        suppress/interfere/inhibit activity of carcinog/canc/tumz => 
            suppress/interfere/inhibit activity of drug/medication/enzyme
    '''
    new_pattern = []
    for w in line.split(' '):
        pos = get_nltk_pos(w, av)
        if pos:
            row = find_type(w, pos, None, None, av)
            if row:
                if 'type' in row:
                    if len(row['type']) > 0:
                        new_pattern.append(', '.join(row['type']))
            else:
                new_pattern.append(w)
        else:
            new_pattern.append(w)
    if len(new_pattern) > 0:
        return [' '.join(new_pattern)]
    return False

'''
def generate_pattern_type_patterns(line, generated_patterns, av):
    #transform modifiers/clauses in a line to type names like 'modifier', 'clause', etc 
    #to do: 
    # - identify common alts & consolidate to one pattern with alts wherever possible
    for pattern_index in ['pattern_index', 'type_index']:
        for pattern_key in av[pattern_index]:
            if generated_patterns:
                patterns, av = get_matching_subsets(line, pattern_key, av)
                if patterns:
                    for pattern_type in patterns:
                        for pattern, matches in pattern_type.items():
                            # replace m with pattern_key
                            for m in matches:
                                line = line.replace(m, pattern_key)
    if line:
        return line
    return False
'''

def consolidate_patterns(all_patterns, av):
    ''' this function identifies possible alt_patterns in a set '''
    if len(all_patterns) > 0:
        ''' note: pattern retrieved from match_pattern may have delimiter '''
        candidates = {}
        possible_alt_patterns = []
        for pattern_words in all_patterns:
            for ap_words in all_patterns:
                words_in_common = get_words_in_common(pattern_words, ap_words)
                if words_in_common:
                    if (len(words_in_common) / len(pattern_words)) > 0.7:
                        pattern = ' '.join(pattern_words)
                        if pattern not in candidates:
                            candidates[pattern].append(ap_words)
        for pattern, alt_word_sets in candidates.items():
            alt_pattern = []
            pattern_words = pattern.split(' ')
            for i, s in enumerate(pattern_words):
                for ap_words in alt_word_sets:
                    if i < len(ap_words):
                        ''' to do: handle optional words found in one pattern but not the other '''
                        if s == ap_words[i]:
                            alt_pattern.append(s)
                        else:
                            if i < len(alt_pattern):
                                if type(alt_pattern[i]) == list:
                                    alt_pattern[i].append(ap_words[i])
                            else:
                                alt_pattern[i] = [s, ap_words[i]]
            if len(alt_pattern) > 0:
                new_alt_pattern = []
                for ap in alt_pattern:
                    if type(ap) == list:
                        new_alt_pattern.append(''.join(['|', ' '.join(ap), '|']))
                    else:
                        new_alt_pattern.append(ap)
                if len(new_alt_pattern) > 0:
                    possible_alt_patterns.add(' '.join(new_alt_pattern))   
        if len(possible_alt_patterns) > 0:
            return possible_alt_patterns
    return False 

def get_words_in_common(source_words, target_words):
    words_in_common = []
    for s in source_words:
        if s in target_words:
            words_in_common.append(s)
    if len(words_in_common) > 0:
        return words_in_common
    return False

def generate_synonym_patterns(pattern, av):
    ''' first check that words are not in supported keywords, then get the synonym '''
    new_words = []
    words = pattern.split(' ')
    for word in words:
        nonnumeric = get_nonnumeric(word, av)
        if nonnumeric not in av['tags']['ALL'] and nonnumeric not in av['tags'] and nonnumeric not in av['type_index'] and nonnumeric not in av['pattern_index']:
            ''' this is a word, check for synonyms '''
            synonym, av = replace_with_syns(nonnumeric, None, ['synonym'], av)
            if not synonym:
                synonym, av = replace_with_syns(nonnumeric, None, ['common', 'standard', 'similarity'], av)
            if synonym:
                new_words.append(synonym)
            else:
                new_words.append(word)
        else:
            new_words.append(word)
    if len(new_words) > 0:
        return ' '.join(new_words), av
    return False, av

def generate_operator_patterns(pattern, av):
    new_pattern, variables = convert_to_operators(pattern, av)
    if new_pattern:
        return new_pattern
    return False

def get_polarity_pattern(pattern, av):
    new_words = []
    for word in pattern.split(' '):
        if word not in av['operator_map']:
            blob = get_blob(word)
            if blob:
                new_words.append(str(round(blob.sentiment_assessments.polarity, 2)))
            else:
                new_words.append(word)
        else:
            new_words.append(word)
    if len(new_words) > 0:
        return ' '.join(new_words)
    return False   

def get_subjectivity_pattern(pattern, av):
    new_words = []
    for word in pattern.split(' '):
        if word not in av['operator_map']:
            blob = get_blob(word)
            if blob:
                new_words.append(str(round(blob.sentiment_assessments.subjectivity, 2)))
            else:
                new_words.append(word)
        else:
            new_words.append(word)
    if len(new_words) > 0:
        return ' '.join(new_words)
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

def generate_alt_patterns(pattern, av):
    ''' 
    this functions returns ['VB NN D1 D2', 'VB JJ D1 D2'] from pattern = 'VB |NN JJ| D1 D2' 
    - alternatives are indicated by options separated by spaces within pairs of '|'
    - optional strings are indicated by: __option__    
    - pattern = '|VB NN VB&ADV|' means 'VB or NN or VB & ADV'
    '''
    print('generate_alt_patterns::pattern', pattern)
    all_alts = []
    pattern = '\n'.join([p for p in pattern]) if type(pattern) != str else pattern
    pattern = pattern.strip().replace('__', '')
    ''' treat vars like 'noun_phrase' similarly to wrapped lists with '|' '''
    for var_name in av['pattern_vars']:
        if var_name in pattern and var_name in av['pattern_index']:
            for var_pattern_item in av['pattern_index'][var_name]:
                var_pattern_item_words = var_pattern_item.split(' ')
                new_words = []
                for word in var_pattern_item_words:
                    if word in av['tags']:
                        sub_list = ''.join(['|', ' '.join(av['tags'][word]), '|'])
                        new_words.append(sub_list)
                    else:
                        new_words.append(word)
                if len(new_words) > 0:
                    var_pattern_item = ''.join(['|', ' '.join(new_words), '|'])
                var_name_pattern = ''.join(['|', var_pattern_item, '|'])
                pattern_with_var_name = pattern.replace(var_name, var_name_pattern)
                var_all_alts = get_alt_sets(pattern_with_var_name, [], av)
                if var_all_alts:
                    all_alts.extend(var_all_alts)
    if len(all_alts) == 0:
        var_all_alts = get_alt_sets(pattern, [], av)
        if var_all_alts:
            all_alts.extend(var_all_alts)
    if len(all_alts) > 0:
        ''' now replace optional strings and add that pattern as well '''
        if '__' in pattern:
            all_patterns = []
            for alt in all_alts:
                 alt_words = alt.strip().replace('&', ' & ').split(' ')
                 all_patterns.append(' '.join(alt_words))
                 all_patterns.append(' '.join([word for word in alt_words if ''.join(['__', word, '__']) not in pattern]))
            if len(all_patterns) > 0:
                return set(all_patterns)
        return set([alt.strip().replace('&', ' & ') for alt in all_alts])
    return False

def get_all_combinations(alt_lists):
    '''
    alt_lists = a list of lists [['a', 'b'], ['c', 'd'], 'e'] 
    build list of all possible options for a combination and select count of output 
    '''
    all_lists = []
    for i, sub_list in enumerate(alt_lists):
        if type(sub_list) == list:
            new_all_lists = append_list(all_lists, sub_list)
        else:
            new_all_lists = append_list(all_lists, [sub_list])
        all_lists = new_all_lists if new_all_lists else all_lists
    if len(all_lists) > 0:
        return all_lists
    return False

def get_alt_sets(pattern, all_alts, av):
    ''' to do: collapse ||JJ JJR JJS| |WRB RB RBR RBS|| to one alt set '''
    #pattern = 'ALL_N |DPC word ALL_N| and |ADJ ADV ALL_N| DPC but |ADV ALL_V|'
    #pattern = '|suppose thought assumed| and |ALL_N DPC| but ALL_N'
    print('get alt sets pattern', pattern, 'all_alts', all_alts)
    delimiter = '|'
    pattern_words = [tag for tag in pattern.split(' ') if tag.replace(delimiter, '') in av['tags']]
    if len(pattern_words) > 0:
        new_words = []
        for word in pattern.split(' '):
            word_tag = word.replace(delimiter, '')
            if word_tag in av['tags']:
                sub_list = ''.join([delimiter, ' '.join(av['tags'][word_tag]), delimiter])
                new_word = word.replace(word_tag, sub_list)
                new_words.append(new_word)
            else:
                new_words.append(word)
        if len(new_words) > 0:
            pattern = ''.join([delimiter, ' '.join(new_words), delimiter])
    print('pattern 1', pattern)
    subsets = get_pattern_subsets(pattern, av)
    if subsets:
        return subsets
    return False

def get_pattern_subsets(pattern, av):
    ''' to do: look for embedded sets such as the unit ||a b| |c d|| and flatten them to |a b c d| '''
    delimiter = '|'
    delimiter_pair = '||'
    interim_pair = '| |'
    wrapped_pairs = ['|| ', ' ||']
    wrapped_pair_len = len('|| ')
    unit_pair_count = 2
    interim_count = unit_pair_count * 2
    wrapped_alts_count = ((unit_pair_count * 2) + unit_pair_count) # 6
    consecutive_subsets_or_preceding_subsequent_wrapped_count = (unit_pair_count * 2) + 1 # 5
    consecutive_subsets_preceding_subsequent_wrapped_count = (unit_pair_count * 2) + 1 + 2 # 7
    indexes = {}
    new_subsets = []
    index_pairs = []
    adjacent_pairs = []
    for i, char in enumerate(pattern):
        if char == delimiter:
            indexes[len(indexes.keys())] = i
    index_keys = indexes.keys()
    for count, char_pos in indexes.items():
        if (count + 1) < len(index_keys):
            index_pairs.append([count, count + 1])
    ending_string = None
    isolated_subsets = False # if its a list of isolated sets or strings with no embedded alts like |a b c| |d e f| and |g h i|
    unwrapped_pattern = pattern[1:-1] if pattern[0] == delimiter and pattern[-1] == delimiter else pattern
    if delimiter_pair not in unwrapped_pattern:
        isolated_subsets = True
    else:
        index_len = len(index_keys)
        first_delimiter = indexes[1] if index_len > 2 else 0
        last_delimiter = indexes[index_len - 2] + 1 if index_len > 2 else 0
        if first_delimiter > 0:
            starting_string = pattern[0:first_delimiter].replace('|', '')
            if len(starting_string) > 0:
                new_subsets.append(starting_string.split(' '))
                new_pattern = pattern[len(starting_string):]
                pattern = new_pattern if len(new_pattern) > 0 else pattern
            ending_string = pattern[last_delimiter:].replace('|', '')
            new_pattern = pattern[0:-len(ending_string)]
            pattern = new_pattern if len(new_pattern) > 0 else pattern
        indexes = {}
        for i, char in enumerate(pattern):
            if char == delimiter:
                indexes[len(indexes.keys())] = i
        index_keys = indexes.keys()
        for count, char_pos in indexes.items():
            if (count + 1) < len(index_keys):
                index_pairs.append([count, count + 1])
        for i, index in indexes.items():
            if i > 0:
                if (index - 1) == indexes[i - 1]:
                    adjacent_pairs.append([index - 1, index])
    if len(adjacent_pairs) > 0:
        if delimiter_pair in pattern:
            first_subset = pattern.split(delimiter_pair)[0]
            if len(first_subset) > 0:
                for item in first_subset.split(' |'):
                    if delimiter in item:
                        for sub_item in item.split(delimiter):
                            new_subsets.append(sub_item)
                    else:
                        new_subsets.append(item)
    if len(adjacent_pairs) > 1:
        for i, pair in enumerate(adjacent_pairs):
            if i == len(adjacent_pairs) - 1:
                adjacent_subset = pattern[pair[0]:pair[1]]
            if i > 0:
                previous_pair = adjacent_pairs[i - 1]
                adjacent_subset = pattern[previous_pair[0]:pair[1] + 1]
                print('adjacent_subset', adjacent_subset)
                if len(adjacent_subset) > 0:
                    delimiter_count = adjacent_subset.count(delimiter)
                    subset_with_interim = adjacent_subset.replace(delimiter_pair, '')
                    if len(subset_with_interim.replace('|','').strip()) > 0:
                        subset_with_interim = subset_with_interim[1:] if subset_with_interim[0] == delimiter else subset_with_interim
                        subset_with_interim = subset_with_interim[0:-1] if subset_with_interim[-1] == delimiter else subset_with_interim
                        interim_delimiter = ' |' if ' |' in subset_with_interim else '| ' if '| ' in subset_with_interim else ''
                        if interim_delimiter != '':
                            if subset_with_interim.replace(interim_delimiter, '').count(delimiter) == 0:
                                interim_split = subset_with_interim.split(interim_delimiter)
                                words_found = []
                                subsets_found = []
                                for sub_list in interim_split:
                                    new_subsets.append(sub_list.split(' '))
                                for item in interim_split:
                                    adjacent_subset = adjacent_subset.replace(item, '')
                        new_subset = adjacent_subset.replace(delimiter, '').strip()
                        if len(adjacent_subset) > 0:
                            if delimiter_count % unit_pair_count == 0:
                                if adjacent_subset[-3:] in wrapped_pairs and adjacent_subset[0:3] in wrapped_pairs:
                                    consecutive_subsets = adjacent_subset[3:-3].split(interim_pair)
                                    for cs in consecutive_subsets:
                                        for c in cs.split(delimiter):
                                            new_subsets.append(c.split(' '))
                                else: 
                                    new_subsets.append(list(set(new_subset.split(' '))))
                            else:
                                if adjacent_subset.count(delimiter) == consecutive_subsets_or_preceding_subsequent_wrapped_count:
                                    if adjacent_subset[-3:] in wrapped_pairs or adjacent_subset[0:3] in wrapped_pairs:
                                        new_subsets.append(new_subset.split(' '))
                                    else:
                                        print('\t\tadjacent_subset 3b', adjacent_subset)
                                        exit()
                                elif delimiter_count == consecutive_subsets_preceding_subsequent_wrapped_count:
                                    adjacent_subset = adjacent_subset[0:-3] if adjacent_subset[-3:] in wrapped_pairs else adjacent_subset
                                    adjacent_subset = adjacent_subset[3:] if adjacent_subset[0:3] in wrapped_pairs else adjacent_subset
                                    adjacent_subset = adjacent_subset[1:] if adjacent_subset[0:2] == delimiter_pair else adjacent_subset
                                    adjacent_subset = adjacent_subset[0:-1] if adjacent_subset[-2:] == delimiter_pair else adjacent_subset
                                    if interim_pair in adjacent_subset and adjacent_subset.count(delimiter) == interim_count:
                                        adjacent_subset = adjacent_subset[1:] if adjacent_subset[0] == delimiter else adjacent_subset
                                        adjacent_subset = adjacent_subset[0:-1] if adjacent_subset[-1] == delimiter else adjacent_subset
                                        consecutive_subsets = adjacent_subset.split(interim_pair)
                                        for cs in consecutive_subsets:
                                            new_subsets.append(cs.split(' '))
                                    else:
                                        ''' interim words '''
                                        new_subsets.extend([subset.strip() for subset in adjacent_subset.split('|') if len(subset.strip()) > 0])
                                else:
                                    if adjacent_subset[0:2] == delimiter_pair and adjacent_subset[-2:] == delimiter_pair:
                                        adjacent_subset = adjacent_subset[2:-2]
                                        consecutive_subsets = adjacent_subset.split(interim_pair)
                                        for cs in consecutive_subsets:
                                            new_subsets.append(cs.split(' '))
            else:
                adjacent_subset = pattern[pair[0]:pair[1] + 1]
                if adjacent_subset != delimiter_pair:
                    print('xx', adjacent_subset)
                    exit()
    else:
        if len(pattern) > 0:
            pattern = pattern[1:-1] if pattern[0] == delimiter and pattern[-1] == delimiter else pattern
            ''' safe to assume we can just split pairs since there are no adjacent subsets like ||a b c| |d e f||'''
            for subset in pattern.split(delimiter):
                if len(subset) > 0:
                    if subset[0] == ' ' and subset[-1] == ' ':
                        ''' word sequence or word '''
                        new_subsets.append(subset.strip())
                    else:
                        subset = subset.replace(delimiter, '').strip()
                        if len(subset) > 0:
                            new_subsets.append(subset.split(' '))
    if len(adjacent_pairs) > 0:
        if delimiter_pair in pattern:
            last_subset = pattern.split(delimiter_pair)[-1]
            if len(last_subset) > 0:
                for item in last_subset.split(' |'):
                    if delimiter in item:
                        for sub_item in item.split(delimiter):
                            new_subsets.append(sub_item)
                    else:
                        new_subsets.append(item)
    if ending_string:
        if len(ending_string) > 0:
            new_subsets.append(ending_string.split(' '))
    new_lists = []
    for ns in new_subsets:
        if type(ns) == str:
            ns = ns.strip()
            if ns != '':
                new_lists.append(ns.split(' '))
        else:
            ns = [item for item in ns if item != '']
            if len(ns) > 0:
                new_lists.append(ns)
    new_subsets = new_lists if len(new_lists) > 0 else new_subsets
    print('new subsets', new_subsets)
    if len(new_subsets) > 0:
        final_combinations = get_all_combinations(new_subsets)
        if final_combinations:
            final_subsets = []
            for fc in final_combinations:
                final_subsets.append(' '.join(fc))
            if len(final_subsets) > 0:
                print('final_subsets', final_subsets)
                return final_subsets
        return new_subsets
    return False

def get_all_versions(pattern, version_types, av):
    ''' 
    this is to generate patterns with standardized synonyms, operators, & types in configured patterns
    execute indexed patterns after you run nested & alt patterns

    - collapses embedded alt sets into the same level of alt as the host set
        '||JJ JJR JJS| |WRB RB RBR RBS| VB |VBG VBD||' => '|JJ JJR JJS WRB RB RBR RBS VB VBG VBD|'

    - some pattern generation function expect tags and some expect words - 
        separate those with word_count in case pattern is a line of words or a pattern of words & tags

    to do:
        - fix | showing up in synonyms output from indexed patterns
    '''
    #corrected_pattern = generate_correct_patterns(pattern, av)
    pattern_index = {
        'standard': set(), 'type': set(), 'operator': set(), 'polarity': set(), 'subjectivity': set(), 
        'synonym': set(), 'pos': set(), 'combination': set(), 'pattern_type': set()
    }
    #pattern = '|functions works operates interacts acts| as __a__ |VB NN|'
    #pattern = '|suppose thought assumed| that'
    #version_types = av['all_pattern_version_types'] if version_types == 'all' or len(version_types) == 0 else version_types
    #pattern = 'modifier_identifier DPC modifier_identifier'
    #pattern = 'first ALL_N DPC |ADJ ADV| and ALL_N |ADJ ADV| but'
    #pattern = '|VBD| VBN VBN |TO IN PP|' to do: fix consecutive strings in between
    print('function::get_all_versions for pattern', pattern)
    alt_patterns = generate_alt_patterns(pattern, av)
    print('generated alt_patterns', alt_patterns)
    ''' for each generated pattern of alternative permutations from a pattern including | alts, 
        calculate versions of each generated pattern like semantic/operator/synonym 
    '''
    if alt_patterns:
        if len(alt_patterns) < (10 * 10 * 10):
            for ap in alt_patterns:
                word_count = [word for word in ap.split(' ') if word not in av['tags']['ALL'] and get_nltk_pos(word, av) not in av['tags']['DPC']]
                if len(word_count) > 0:
                    '''
                    type_patterns = generate_type_patterns(ap, av)
                    if type_patterns:
                        print('type_patterns', type_patterns)
                        for tp in type_patterns:
                            type_pattern = standardize_words(tp, 'type', av)
                            print('type_pattern', type_pattern)
                            if type_pattern:
                                indexed_tp = generate_indexed_patterns(type_pattern, av)
                                if indexed_tp:
                                    pattern_index['type'].add(indexed_tp)
                    '''
                    synonym_pattern = standardize_words(ap, 'synonym', av)
                    if synonym_pattern:
                        ip = generate_indexed_patterns(synonym_pattern, av)
                        if ip:
                            #pattern_index['synonym'].add(ip)
                            if ip.count(' ') == ap.count(' '):
                                op = generate_operator_patterns(ip, av)
                                if op:
                                    pattern_index['operator'].add(op)
                                    pp = get_polarity_pattern(ip, av)
                                    if pp:
                                        pattern_index['polarity'].add(pp)
                                    sp = get_subjectivity_pattern(ip, av)
                                    if sp:
                                        pattern_index['subjectivity'].add(sp)
                                pos = get_specific_pos(ip, av)
                                if pos:
                                    pattern_index['pos'].add(pos)
                                cp = get_all_pos(ip, av)
                                if cp:
                                    pattern_index['combination'].add(cp)
                                pattern_index['standard'].add(ip)
                else:
                    ip = generate_indexed_patterns(ap, av)
                    if ip:
                        if ip.count(' ') == ap.count(' '):
                            pos = get_specific_pos(ip, av)
                            if pos:
                                pattern_index['pos'].add(pos)
                            cp = get_all_pos(ip, av)
                            if cp:
                                pattern_index['combination'].add(cp)
                            pattern_index['standard'].add(ip)
            if len(pattern_index.values()) > 0:
                print('got_all_versions', pattern, pattern_index)
                return pattern_index, av
        else:
            pattern_index['standard'] = set(pattern)
            return pattern_index, av
    return False, av

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

def read(path):
    index = None
    if 'DS_Store' not in path:
        if os.path.exists(path):
            with open(path, 'r') as f:
                index = json.load(f) if 'json' in path else f.read()
                f.close()
    return index

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
    blob = get_blob(line)
    if blob:
        sentiment = blob.sentiment
        if sentiment:
            if sentiment.polarity:
                return roun(sentiment.polarity, 1)
    return 0

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
            w = singularize_word(w, av)
            if w not in stopwords.words('english') and w not in custom_removal:
                word_list.append(w)
    if len(word_list) > 0:
        return ' '.join(word_list)
    return line

def replace_quotes_with_parenthesis(line):
    new_line = []
    quotes = line.count('"')
    if quotes > 0:
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
        ''' now all quote content should be surrounded by parentheses instead '''
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
    alt_pos = []
    if len(alts) > 0:
        for a in alts:
            if a in word_map:
                alt_pos.append(word_map[a])
        if len(alt_pos) > 0:
            alt_pos = alt_pos[0]
        if alt_pos:
            found_non_default = [True for a in alt_pos if a != alt_pos]
            if found_non_default:
                ''' these options are different pos so dont remove them '''
                alt_phrase = alt_phrase.replace(delimiter, '-')
                return alt_phrase
            else:
                ''' these options are all the same pos, check if theyre synonyms '''
                default_alt = alts[0]
                for a in alts:
                    if a != default_alt:
                        similarity = get_similarity(default_alt, a, av)
                        if similarity:
                            if similarity < 0.7:
                                ''' found a non-synonym, keep all options '''
                                return alt_phrase
                ''' all words were synonyms, return first option if most common not found '''
                max_words, counts = get_common_words(alts, 3, av)
                if max_words:
                    if len(max_words) > 0:
                        return max_words[0]
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

def get_similarity(base_word, new_word, av):
    base_pos = get_nltk_pos(base_word, av)
    new_pos = get_nltk_pos(new_word, av)
    pos_lib_map = { 'N': NOUN, 'V': VERB, 'ADV': ADV, 'ADJ': ADJ }
    if new_pos and base_pos:
        for tag, tag_values in av['tags'].items():
            if base_pos in tag_values and tag in pos_lib_map:
                base_pos = tag
            if new_pos in tag_values and tag in pos_lib_map:
                new_pos = tag    
        if base_pos in pos_lib_map and new_pos in pos_lib_map:
            base_synsets = Word(base_word).get_synsets(pos=pos_lib_map[base_pos])
            new_synsets = Word(new_word).get_synsets(pos=pos_lib_map[new_pos])
            if len(new_synsets) > 0 and len(base_synsets) > 0:
                for bs in base_synsets:
                    for ns in new_synsets:
                        similarity = bs.path_similarity(ns)
                        print('\tget similarity', base_word, new_word, new_synsets, base_synsets, similarity)
                        return similarity
    return False

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

def replace_with_syns(words, word_map, check_types, av):
    new_text = []
    check_types = ['definition', 'synonym', 'common', 'standard', 'similarity'] if not check_types else check_types
    # dont add stem-similarity replacement bc you still need pos identification
    for w in words:
        word = ''.join([x for x in w if x == '-' or x == ' ' or x == '_' or x in av['alphabet']]) # some synonyms have dashes and spaces
        pos = word_map[w] if word_map and w in word_map else get_nltk_pos(w, av)
        if pos:
            if pos not in av['tags']['exclude'] and pos not in av['tags']['DPC']:
                match, check_type = find_matching_synonym(word, pos, check_types, None, av)
                if match:
                    if match != w:
                        if w not in av['supported_synonyms']:
                            av['supported_synonyms'][w] = match
                        new_text.append(w.replace(word, match))
                    else:
                        new_text.append(w)
                    ''' add synonym mapping to avoid checking all check_types for this word in future bc 'synonym' check_type should return it now '''
                else:
                    new_text.append(w)
        else:
            new_text.append(w)
    if len(new_text) > 0:
        return ' '.join(new_text), av
    return ' '.join(words), av

def get_names(line):
    names = []
    words = line.split(' ')
    for w in words:
        w_upper = w.upper()
        w_name = w.capitalize()
        if words.count(w_upper) > 0 and w_upper != words[0]:
            names.append(w_upper)
        elif words.count(w_name) > 0 and w_name != words[0]:
            names.append(w_name)
    if len(names) > 0:
        return names
    return False

def get_common_words(line, distance, av):
    blob = get_blob(line)
    if blob:
        word_counts = blob.word_counts
        counts = {}
        for word, wc in word_counts.items():
            pos = get_nltk_pos(word, av)
            if pos:
                if pos not in av['tags']['DPC']:
                    if word not in counts:
                        counts[word] = 0
                    counts[word] += wc
        max_words = []
        max_count = max(counts.values())
        for word, count in counts.items():
            if count > 1:
                if (max_count - count) < distance:
                    max_words.append(word)
        if len(max_words) > 0 and counts:
            return max_words, counts
    return False, False

def get_definitions(define_word, av):
    pos_word = get_nltk_pos(define_word, av)
    if len(define_word) > 4 and define_word not in av['supported_synonyms'] and define_word not in av['supported_synonyms'].values():
        meanings = []
        defs = Word(define_word).definitions
        if defs:
            print('defs', define_word, defs)
            line = ' '.join(defs)
            blob = get_blob(line)
            if blob:
                words_pos = {}
                for word in line.replace(';', '').replace(',', '').split(' '):
                    pos = get_nltk_pos(word, av)
                    if pos:
                        words_pos[word] = pos
                sentiment_assessments = blob.sentiment_assessments
                if sentiment_assessments:
                    for a in sentiment_assessments.assessments:
                        meanings.extend(a[0])
                    if len(meanings) > 0:
                        for meaning in meanings:
                            if pos_word in av['tags']['ALL_V']:
                                if meaning in av['verb_meanings']:
                                    for n in av['negative_meanings']:
                                        if n in meanings:
                                            return define_word
                                    for p in av['positive_meanings']:
                                        if p in meanings:
                                            return define_word
                max_words, counts = get_common_words(line, 3, av)
                if max_words:
                    if len(max_words) > 0:
                        if len(max_words) == 1:
                            if max_words[0] in words_pos:
                                if words_pos[max_words[0]] == pos_word:
                                    ''' if the most common word is also the same pos as original word, return most common word '''
                                    return max_words[0]
                        else:
                            for mw in max_words:
                                if mw in words_pos:
                                    if words_pos[mw] == pos_word:
                                        ''' if this most common word is also the same pos as original word, return this most common word '''
                                        return mw
                    else:
                        ''' if none of the max_words match the original word's pos, revert to any common words '''
                        for word, count in counts.items():
                            if word in words_pos:
                                if words_pos[word] == pos_word:
                                    return word
                ''' if none of the common words match the original word's pos, revert to any words matching pos '''
                matching_pos_words = []
                for word, pos in words_pos.items():
                    if pos == pos_word:
                        matching_pos_words.append(word)
                if len(matching_pos_words) > 0:
                    ''' to do: apply sort '''
                    return matching_pos_words[0]
            ''' if no matching words found, sort defs to find best match '''
            if pos_word not in av['tags']['ALL_V']:
                shortest_def = get_shortest_definition(defs)
                if shortest_def:
                    return shortest_def
                return defs[0]
    else:
        if define_word in av['supported_synonyms']:
            return av['supported_synonyms'][define_word]
        if define_word in av['supported_synonyms'].values():
            return define_word
        return define_word
    if pos_word in av['tags']['ALL_V']:
        return define_word
    return False

def get_definition_keywords(word):
    ''' add option to use local_database/index (phrases, relationships) or pull from a data source '''
    definition = get_definitions(word, av)
    if definition:
        keywords = definition.split(' ')
        if len(keywords) > 0:
            return keywords
    return False

def get_syn_from_definition(word, word_pos):
    candidates = set()
    definition = get_definitions(word, av)
    if definition:
        for w in definition.split(' '):
            dpos = get_nltk_pos(w, av)
            if dpos == word_pos:
                candidates.add(w)
    if len(candidates) > 0:
        ''' to do: if found other words with same pos in definitions, filter by meaning & similarity to word '''
        return candidates
    return False

def standard_text_processing(text, av):
    text_words = text.strip().replace('\n', '').replace(';', '').replace(',', '').split(' ')
    for letter in av['alphabet']:
        if letter in text_words and letter != 'a' and letter != 'i' and letter != 'x' and letter != 'y':
            text = concatenate_species(text)
    text = standardize_delimiter(text)
    text = standardize_punctuation(text)
    article_lines = {}
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.strip() != '':
            print('line', line)
            replaced_line = replace_quotes_with_parenthesis(line)
            line = replaced_line if replaced_line else line
            corrected_line = correct(line)
            line = corrected_line if corrected_line else line
            print('corrected line', line)
            new_line = standardize_words(line, 'synonym', av)
            line = new_line if new_line else line
            new_words = []
            for word in line.split(' '):
                singular_word = singularize_word(word, av)
                if singular_word:
                    new_words.append(singular_word)
                else:
                    new_words.append(word)
            line = ' '.join(new_words) if len(new_words) > 0 else line
            ''' to do: fix mapping '''
            ''' remove call to apply_pattern_map & nested calls to get_all_versions
            active_line, av = apply_pattern_map(line, 'passive_to_active', av)
            print('active line', active_line)
            line = active_line if active_line else line
            '''
            word_map = {}
            for word in line.split(' '):
                pos = get_nltk_pos(word, av)
                word_map[word] = pos if pos else ''
            #line = remove_stopwords(line, article_lines[line])
            '''
            to do: fix word replacement 'find' => 'test'
            syn_line, av = replace_with_syns(line.split(' '), word_map, None, av)
            if syn_line:
                if syn_line not in article_lines:
                    article_lines[syn_line] = {}
                for word in syn_line.split(' '):
                    pos = get_nltk_pos(word, av)
                    article_lines[syn_line][word] = pos if pos else ''
            else:
            '''
            if line not in article_lines:
                article_lines[line] = word_map
    if article_lines:
        print('article', article_lines)
        return article_lines, av
    return False, av
    
def get_operator(verb, av):
    ''' this maps a verb ('reduce' or 'inhibit') to an operator like +, -, = '''
    for charge, values in av['charge'].items():
        if verb == charge or verb in values:
            return charge
    blob = get_blob(verb)
    if blob:
        sentiment_assessments = blob.sentiment_assessments
        if sentiment_assessments:
            meanings = []
            for a in sentiment_assessments.assessments:
                meanings.extend(a[0])
            for meaning in meanings:
                if meaning in av['verb_meanings']:
                    for n in av['negative_meanings']:
                        if n in meanings:
                            return '-'
                    for p in av['positive_meanings']:
                        if p in meanings:
                            return '+'
                    return '='
                    ''' to do: add other operators '''
        '''
        polarity = blob.polarity
        operator = '-' if polarity < 0.0 else '+' if polarity > 0.0 else '='
        return operator
        '''
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
    definition = get_definitions(word, av)
    if definition:
        return definition
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
                                similar_score = get_similarity(word, syn, av) 
                                if similar_score > 0.7:
                                    return syn
                            return max_synonyms[0]
    return word

def standardize_words(line, get_type, av):
    ''' standardizes words in ngrams to synonyms '''
    ''' to do: retain original indexes for variable mapping with new word indexes ''' 
    space_count = line.count(' ')
    for gc in range(space_count, 0):
        blob = get_blob(line)
        if blob:
            ngrams = blob.ngrams(gc)
            for ngram in ngrams:
                gram = ' '.join(ngram)
                nn_gram = get_nonnumeric(gram, av)
                tag_count = [x for x in nn_gram.split(' ') if x in av['tags']['ALL'] or x in av['tags']]
                if tag_count == 0:
                    synonym = None
                    if get_type == 'synonym':
                        synonym = get_synonym_word(nn_gram, av)
                    else:
                        row = find_type(nn_gram, None, None, None, av)
                        if row:
                            if 'type' in row:
                                if len(row['type']) > 0:
                                    synonym = row['type'][0]
                    if synonym:
                        line = line.replace(gram, synonym)                        
    return line

def get_synonym_word(word, av):
    if word in av['convert_map']:
        return av['convert_map'][word]
    elif word in av['supported_synonyms']:
        return av['supported_synonyms'][word]
    return False

def get_shortest_definition(defs):
    if len(defs) > 0:
        shortest_def = None
        for d in defs:
            if shortest_def:
                if len(d) < len(shortest_def):
                    shortest_def = d
            else:
                shortest_def = d
        if shortest_def:
            return shortest_def
    return False

def find_matching_synonym(word, pos, check_types, exclude_types, av):
    ''' examples:   biofilm :: membrane,   sympathetic :: synergistic,   irritate :: damage
    '''
    items = {}
    default_check_types = [
        'standard', 'stem', 'synonym', 'common', 'similarity', 'partial'
    ]
    all_check_types = [
        'standard', 'stem', 'substring', 'type', 'pos', 'partial',
        'synonym', 'common', 'ratio', 'charge', 'similarity'
    ]
    if len(word) > 0:
        ''' favor definitions over synonym calculations '''
        definition = get_definitions(word, av)
        if definition:   
            return definition, 'definition'
        if not check_types:
            check_types = default_check_types
        if exclude_types:
            for exclude_type in exclude_types:
                check_types = check_types.remove(exclude_type)
        match, check_type = iterate_through_synonyms(av, check_types, word, pos)
        if match and check_type:
            return match, check_type
        if pos in av['tags']['SYNSET']:
            ''' if no matches found, check for syns of words in definition '''
            if definition:
                d_row = get_structural_metadata(definition, av)
                if d_row:
                    if 'verb' in d_row:
                        for v in d_row['verb']:
                            ''' for each verb in the definition, do same synonym check '''
                            match, check_type = iterate_through_synonyms(av, check_types, v, pos)
                            if match and check_type:
                                print('found matches', word, check_type, match)
                                return match, check_type
                        if pos == 'V' or pos in av['tags']['V']:
                            return v, check_types[0]
        return word, check_types[0]
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
            similarity = get_similarity(w, k, av)
            pos_k = get_nltk_pos(k, av)
            if check_type == 'standard':
                w = conjugate(w, 'VB', av) # standardize tense to infinitive
                k = conjugate(k, 'VB', av)
            elif check_type == 'stem':
                if w in av['supported_stems'] and k in av['supported_stems']:
                    w = av['supported_stems'][w]
                    k = av['supported_stems'][k]
                else:
                    w = stemmer.stem(w)
                    k = stemmer.stem(k)
            elif check_type == 'substring':
                if w in k or k in w and (len(w) - len(k)) < 6:
                    return k, check_type
            elif check_type == 'type':
                w_row = find_type(w, word_pos, None, None, av)
                if w_row:
                    if 'type' in w_row:
                        if len(w_row['type']) > 0:
                            w = ', '.join(w_row['type'])
                k_row = find_type(k, pos_k, None, None, av)
                if k_row:
                    if 'type' in k_row:
                        if len(k_row['type']) > 0:
                            k = ', '.join(k_row['type'])
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
                if similarity:
                    if similarity > 0.9:
                        return k, check_type
            elif check_type == 'definition':
                w = get_definitions(w, av)
                k = get_definitions(k, av)
                definition_similarity = get_similarity(w, k, av)
                if w and k:
                    missing_words = [0 for dw_word in w.split(' ') if dw_word not in k.split(' ')]
                    if len(missing_words) < 3 or definition_similarity > 0.9:
                        return k, check_type
            if w and k:
                if w == k:
                    return k, check_type
                if similarity:
                    if similarity > 0.9:
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
    print('data_lines', data_lines)
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

def conjugate(word, target_pos, av):
    ''' convert word from source_pos to target_pos '''
    endings = {
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
    equivalent = ['VB', 'VBG', 'VBP'] # 'VBG', 'VBN', 'VBD', 'VBZ'  
    infinitive = lemmatizer.lemmatize(word, 'v')
    stem = stemmer.stem(infinitive)
    if infinitive in case_maps:
        return case_maps[infinitive][target_pos]
    if target_pos == 'VB':
        return infinitive
    if len(word) > 2:
        ''' to do: apply all cases from singularize_word to this assignment '''
        word_stem = ''.join([stem, endings[target_pos]]) if stem != infinitive and stem[-1] != 's' else stem
        singular_word = singularize_word(word_stem, av)
        if singular_word:
            return singular_word
        return word_stem
    return False

def singularize_word(word, av):
    pos = get_nltk_pos(word, av)
    if pos:
        #lemmatizer_type = 'v' if pos in av['tags']['ALL_V'] else 'n'
        #infinitive = lemmatizer.lemmatize(word, lemmatizer_type)
        #stem = stemmer.stem(infinitive)
        ''' to do: dont reduce words ending in 'tion' that dont have a root verb or are a verb, like ration '''
        if len(word) > 4:
            #word = ''.join([word[0:-2], 's']) if word[-2:] == 'or' or word[-2:] == 'er' and word[-3:] != 'ter' else word
            #word = ''.join([word[0:-4], 'te']) if len(word) > 8 and word[-4:] == 'tion' else word # creation => creat, ration, function, inhibition -> inhibit
            penultimate_char = word[-2]
            last_char = word[-1]
            if word[-3] == 'ies':
                return ''.join([word[0:-3], 'y'])
            if word[-3] == 'ses':
                return ''.join([word[0:-3], 'sis']) # parentheses => parenthesis, analyses => analysis
            if penultimate_char == 's' and last_char == 's':
                return word # regress
            if penultimate_char not in 'aeiou' and last_char == 's':
                return word[0:-1] # catalysts => catalyst
            if penultimate_char == 'e' and last_char == 's':
                if pos in av['tags']['ALL_V']:
                    # dont remove 'es' for conjugated verbs or special nouns like diabetes
                    return word
                else:
                    return word
                    #return word[0:-1]
            if penultimate_char in 'aiou' and last_char == 's':
                return word # analogous
    return word

def get_pos_line(line, av):
    new_words = []
    for word in line.split(' '):
        pos = get_nltk_pos(word, av)
        new_word = pos if pos else word 
        new_words.append(new_word)
    if len(new_words) > 0:
        pos_line = ' '.join(new_words)
        return pos_line
    return False

def apply_pattern_map(line, pattern_map, av):
    ''' 
    - this replaces a pattern with its associated pattern found in the line using variables 
        (line='dog of cat', pattern_map = {'noun1 of noun2' => 'noun2 noun1'}) = 'cat dog'
    to do:
        - for object_type in ['word', 'modifier', 'phrase'] - these should already be replaced with option sets of each type pattern 
        - modifier1 should be replaced with each modifier pattern + 1 and used to generate a new pattern containing each modifier pattern
        - when the source pattern is 'VBD VBN' and the target is 'VBZ' you need to isolate the 'VBN' which is the more meaningful verb
            currently its getting overridden by the consecutive verb which also matches the 'V' type but need a more robust way
        - in order to support iterated replacement, you need to make sure your patterns are ordered in the right way
    '''
    # x of y => 'y x'
    print('function::apply pattern map for line', line)
    if pattern_map in av['pattern_maps']:
        for source_pattern, target_pattern in av['pattern_maps'][pattern_map].items():
            ''' recalculate line versions in case line was changed with previous pattern match '''
            print('function::apply pattern map - get_all_versions for line', line)
            line_version_index, av = get_all_versions(line, 'all', av)
            print('line_version_index', line_version_index)
            if line_version_index:
                for line_version_type, versions in line_version_index.items():
                    for line_version in versions:
                        print('applying patterns from pattern_map to line version', pattern_map, 'source_pattern', source_pattern, 'line', line_version)
                        variables, line_with_vars = get_variables_for_pattern(line_version, source_pattern, av)
                        line_with_vars = line_with_vars if line_with_vars else line_version
                        found_subsets, av = get_pattern_source_subsets(line_with_vars, source_pattern, 'pattern', av)
                        if found_subsets:
                            print('applying pattern map to line', line_version, 'sp', source_pattern, 'tp', target_pattern)
                            new_line = apply_pattern(line_with_vars, source_pattern, target_pattern, av)
                            if new_line:
                                print('applied pattern to line', new_line, 'sp', source_pattern, 'tp', target_pattern)
                                if variables:
                                    ''' replace variables with original values '''
                                    line_words = line_with_vars.split(' ')
                                    new_line_words = []
                                    for word in line_words:
                                        if word in variables:
                                            new_line_words.append(variables[word])
                                        else:
                                            new_line_words.append(word)
                                    if len(new_line_words) > 0:
                                        new_line = ' '.join(new_line_words)
                                        print('new line after replacing vars', new_line)
                                line = new_line # return new_line if not iterating through all patterns in map
    return line, av

def get_variables_for_pattern(line, pattern, av):
    ''' for a line like 'cat-mouse of dog is a key', and pattern 'x of y', 
        assign variables x = "cat-mouse" and y = "dog is a key" and return line with variables replaced

        to do: 
            - support multi-word variables
            - fix pattern mapping of variables to assign position based on positions of non-var sections of pattern, rather than word position 
    '''
    #line = 'x is ionizs inhibits of y', pattern = 'x of y'
    variables = {}
    vars_in_pattern = [letter for letter in pattern.split(' ') if letter in av['alphabet']]
    words = line.split(' ')
    pattern_words = pattern.split(' ')
    non_var_words = [word for word in pattern_words if word not in av['alphabet']]
    new_words = []
    final_line_words = []
    if len(non_var_words) > 0:
        if non_var_words[0] == words[0]:
            ''' if the first word is not a variable, add it & remove from non_var_words '''
            final_line_words.append(non_var_words[0])
            non_var_words = non_var_words[1:]
        for w in words:
            if w in non_var_words:
                new_words.append('***')
            else:
                new_words.append(w)
        if len(new_words) > 0:
            line_variables = ' '.join(new_words).split('***')
            for i, v in enumerate(line_variables):
                ''' match up var names with vars from pattern '''
                if i < len(vars_in_pattern):
                    var_name = vars_in_pattern[i]
                    if len(final_line_words) > 0:
                        if final_line_words[-1] == v.split(' ')[0]:
                            v = ' '.join(v.split(' ')[1:])
                        elif final_line_words[-1] in v:
                            v = v.replace(final_line_words[-1], '')
                    variables[var_name] = v
                    final_line_words.append(var_name)
                    if i < len(non_var_words):
                        final_line_words.append(non_var_words[i])
        if len(non_var_words) > 0:
            if non_var_words[-1] == words[-1]:
                ''' if the last word is not a variable, add it '''
                final_line_words.append(non_var_words[-1])
    if variables:
        return variables, ' '.join(final_line_words)
    return False, False


def derive_and_store_patterns(object_type, index, av):
    ''' this is to identify common patterns in a set of articles pulled from a source list 

    the source list should be items that are likely or guaranteed to contain objects of type 'object_type',
    because this function is not trying to guess if an object type is in a document, 
    it's trying to identify patterns of objects of 'object_type' using documents known to contains objects of that type
    
    identify in each line:
    - pos patterns: 'N V |JJ VB|'
    - operator patterns: 'V = V N'
    - common synonym patterns: 'function changes function'
    - type patterns: 'structure compound and rule test'
    - combination patterns: 'N V and V ADJ'
    - pattern_index type patterns: 'modifier clause'

    and add to index, then aggregate by max counts & store most common patterns in data set

    this function is to determine patterns using each object in the list as input, to find patterns between list items
    since we're passing in index[keys] to this function, we'll be handling lists of objects like strategies
    to find patterns in strategy objects, youd abstract the objects in each strategy and check if that abstract version occurs elsewhere

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
    to do:
      - use definitions as a data source for relationships if none are found 
    '''

    print('function::derive_and_store_patterns')
    all_patterns = set()
    pattern_counts = {'standard': {}, 'type': {}, 'operator': {}, 'polarity': {}, 'subjectivity': {}, 'synonym': {}, 'pos': {}, 'combination': {}, 'pattern_type': {}}
    if object_type in index:
        source_names = filter_source_list(object_type)
        if source_names:
            articles = []
            for source_name in source_names:
                for source in av['sources']:
                    if source_name == source['name']:
                        keyword = ''
                        data = get_data_from_source(source, keyword, av)
                        if data:
                            for title, article_lines in data.items():
                                article = [title]
                                for line, word_map in article_lines.items():
                                    article.append(line)
                                    print('function::derive_and_store_patterns - get_all_versions for line', line)
                                    generated_patterns, av = get_all_versions(line, 'all', av)
                                    if generated_patterns:
                                        for pattern_type, patterns in generated_patterns.items():
                                            all_patterns = all_patterns.union(patterns)
                                            if pattern_type not in pattern_counts:
                                                pattern_counts[pattern_type] = {}
                                            for p in patterns:
                                                if p not in pattern_counts[pattern_type]:
                                                    pattern_counts[pattern_type][p] = 0
                                                pattern_counts[pattern_type][p] += 1
                                if len(article) > 0:
                                    articles.append('\n'.join(article))                
            if len(articles) > 0:
                filename = ''.join(['article_store_', object_type, '.txt'])
                save(filename, '\n\n'.join(articles))
            if pattern_counts:
                object_pattern_name = ''.join(['data/patterns_', object_type, '.txt'])
                ''' dont need to extract patterns in pattern_list bc that just identifies matching patterns and we want to derive patterns '''
                ''' store patterns for this type of data source '''
                for pattern_type, pattern_map in pattern_counts.items():
                    pattern_list = pattern_map.keys()
                    new_counts = {}
                    possible_alt_patterns = consolidate_patterns(pattern_list, av)
                    if possible_alt_patterns:
                        for p in possible_alt_patterns:
                            if p not in new_counts:
                                if p in pattern_map:
                                    new_counts[p] = pattern_map[p]
                                else:
                                    new_counts[p] = 1
                            else:
                                new_counts[p] += 1
                    if new_counts:
                        pattern_map = new_counts
                    new_pattern_type = []
                    threshold = 1
                    max_pattern_count = max(pattern_map.values())
                    if max_pattern_count > threshold:
                        for pattern, pattern_count in pattern_map.items():
                            if pattern_count > threshold:
                                new_pattern_type.append('::'.join([pattern, pattern_count]))
                        if len(new_pattern_type) > 0:
                            filename = ''.join(['derived_patterns_', object_type, '_', pattern_type, '.txt'])
                            save(filename, '\n'.join(new_pattern_type))
                            ''' to do: update av pattern index with newly derived patterns '''
    return all_patterns, articles, av

def get_matching_subsets(line, pattern_key, av):
    '''
    find subsets in a line, matching stored patterns in av[pattern_index][pattern_key]
    '''
    print('function::get_matching_patterns - get_all_versions in line', line)
    found_patterns = {}
    line_versions, av = get_all_versions(line, 'all', av)
    if line_versions:
        for line_version in line_versions:            
            for pattern_index in ['computed_type_index', 'computed_pattern_index']:
                for pattern_type, patterns in av[pattern_index].items():
                    if pattern_type == pattern_key or pattern_key == 'all' or pattern_key is None:
                        for pattern in patterns:
                            found_subsets, av = get_pattern_source_subsets(line_version, pattern, 'pattern', av)
                            if found_subsets:
                                combined_key = ''.join([pattern_type, '_pattern'])
                                if combined_key not in found_patterns:
                                    found_patterns[combined_key] = {}
                                if pattern not in found_patterns[combined_key]:
                                    found_patterns[combined_key][pattern] = []
                                found_patterns[combined_key][pattern].extend(found_subsets)
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
    print('apply_pattern', subset, 'sp', source_pattern, 'tp', target_pattern)
    delimiter = find_delimiter(subset, av)
    print('delimiter', delimiter)
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
        print('positions', positions)
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
        print('position_map', position_map)
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
                            conjugated_word = conjugate(source_word, target_var, av)
                            if conjugated_word:
                                new_words[tp] = conjugated_word
                        else:
                            new_words[tp] = source_word
                    else:
                        ''' not a variable: include index matches ('the': 'the0') but not positional/non-content matches ('x': 'the') '''
                        if source_var == source_word or nonnumeric_source_var == source_word:
                            new_words[tp] = source_word
        if new_words:
            print('new_words', new_words)
            new_items = [new_words[k] for k in sorted(new_words.keys()) if k in new_words]
            if len(new_items) > 0:
                return delimiter.join(new_items)
    return False

def get_pattern_source_subsets(line, pattern, get_type, av):
    ''' get only the matching subsets from line with words in the same positions & pos as pattern
        ['pattern_instance_1', 'pattern_instance_2']
        support numerical variables by checking non-numeric pattern for match with pos_line 
        to do: 
            - this prevents users from configuring patterns with numbers like 14alpha-deoxy-enzyme
            - add support for other pattern types than pos type
    '''
    if pattern == line:
        return [pattern], av
    if pattern in line:
        subsets = []
        non_pattern_subsets = line.split(pattern)
        if get_type == 'pattern':
            subsets = get_pattern_source_words(line, non_pattern_subsets)
        else:
            ''' split a line into subsets so each pattern section is in its own subset '''
            ''' ['pattern_instance_1', 'non-pattern-words', 'pattern_instance_2', 'other non-pattern words'] '''
            sources = get_pattern_source_words(line, non_pattern_subsets)
            if sources:
                for i, subset in enumerate(sources):
                    ''' to do: convert back to original line subset '''
                    subsets.append(subset)
                    if i < len(non_pattern_subsets):
                        subsets.append(non_pattern_subsets[i])
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
    words = line.split(' ') if type(line) == str else line
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
            operator = get_operator(word, av)
            if operator:
                new_words.append(operator)
            else:
                new_words.append(word)
    if len(new_words) > 0:
        return ' '.join(new_words), variables
    return False, False

def get_nltk_pos(word, av):
    if word:
        if '_' in word or word in [a for a in av['alphabet']]:
            ''' this is a variable, dont modify '''
            return False
        tagged = pos_tag(word_tokenize(word))
        tags = TextBlob(word).parse().split('/')
        if len(tags) > 1:
            blob_pos = tags[1]
            if len(tags) > 2:
                if tags[2] == 'B-NP':
                    return blob_pos
            if len(tagged) > 0:
                for item in tagged:
                    if len(item) > 0:
                        if blob_pos != item[1]:
                            ''' blob identifies 'explains' as a verb when pos_tag doesnt '''
                            if blob_pos in av['tags']['ALL_V']:
                                return blob_pos
                        return item[1]
    return False

def find_ngrams(line, av):
    phrases = {'phrase': [], 'N': [], 'V': [], 'ADJ': [], 'ADV': [], 'DPC': []} # take out adj & adv
    key_map = {'N': 'noun', 'V': 'verb', 'ADJ': 'adj', 'ADV': 'adv', 'DPC': 'dpc'}
    non_dpc_segments = []
    new_segment = []
    for w in line.split(' '):
        if len(w) > 0:
            pos = get_nltk_pos(w, av)
            if pos:
                if pos not in av['tags']['DPC']:
                    new_segment.append(w)
                else:
                    new_section = ' '.join(new_segment)
                    if len(new_section) > 0:
                        non_dpc_segments.append(new_section)
                    else:
                        non_dpc_segments.append('***')
                    new_segment = []
            else:
                new_segment.append(w)
        else:
            new_segment.append('***')
    if len(new_segment) > 0:
        non_dpc_segments.append(' '.join(new_segment))
    if len(non_dpc_segments) > 0:
        non_dpc_segments = ' '.join(non_dpc_segments).split('***')
        phrases['phrase'] = non_dpc_segments
    for key in ['N', 'V', 'ADJ', 'ADV', 'DPC']:
        pos_phrases = get_ngrams_of_type(key, line, av)
        if pos_phrases:
            for p in pos_phrases:
                if p in line:
                    map_key = key_map[key]
                    phrases[key].append(p)
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

def get_index_type(object_type, av, categories):
    param_map = {
        'condition': 'state',
        'compound': 'element', # not every compound will be a treatment
        'symptom': 'side_effect',
        'function': 'causal_layer'
    }
    if object_type in av['supported_synonyms']:
        return av['supported_synonyms'][object_type]
    alt_type = param_map[object_type]
    if alt_type in av['supported_synonyms']:
        return av['supported_synonyms'][alt_type]
    if len(categories) > 0:
        for c in categories:
            for term in c.split(' '):
                index_type = None
                for k, v in param_map.items():
                    index_type = k if v == term else v if k == term else None
                    if index_type:
                        return index_type
        return categories[0]
    return False

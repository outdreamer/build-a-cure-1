import os
from get_pos import convert_pos_names_to_nltk_tags
from get_synonyms import aggregate_synonyms_of_type

def get_pattern_config(all_vars):
    all_vars['passive'] = [" by ", " from ", " of "]
    ''' to do: assess which operator combinations neutralize or negate a relationship '''
    all_vars['combined_map'] = {
        '=': ['=-', '-=', '=+', '+=', '=='], #"x = (i - b)" => x and b equal i
        '-': ['-+', '+-', '=-', '-=', '==-', '=-=', '-==', '-=-', '---'],
        '+': ['--', '++', '+=', '=+', '==+', '=+=', '+==', '+=+', '+++'],
        '#': [
            '# &', # even with x
            '# !', # even without x
            '! -', # not decrease
            '! +', # not increase ('neutral' or 'independent', 'does not increase' doesnt mean 'decrease')
            '! >', # not change
            '~ !' # does not increase =>
        ]
    }
    all_vars['key_map'] = {
        '-': ['worsen', 'decrease', 'inhibit', 'reduce', 'deactivate', 'disable'],
        '+': ['improve', 'increase', 'induce', 'enhance', 'activate', 'enable'],
        '=': ['equal', 'alternate'],
        '>': ['creates'],
        '@': ['changes'],
        '~': ['functions']
    }
    all_vars['charge'] = {
        '-': aggregate_synonyms_of_type(all_vars, '-'), # antagonist, reduce, inhibit, deactivate, toxic, prevents
        '+': aggregate_synonyms_of_type(all_vars, '+'), # help, assist, enhance, induce, synergetic, sympathetic, leads to
        '=': aggregate_synonyms_of_type(all_vars, '=') # means, signifies, indicates, implies, is, equates to
    }
    ''' this maps operators to lists of operator keyword to use as clause delimiters '''
    all_vars['clause_map'] = {
        '-' : ["decrease"], # attacks
        '+' : ["increase"], # helps
        '=': ['is', 'like', 'equate', 'equal', 'describe', 'indicate', 'delineate', 'same', 'like', 'similar', 'implies', 'signifies', 'means'],
        '&': ['and', 'with'],
        '|': ['or'],
        '^': ['but', 'yet', 'but yet', 'but rather', 'but actually', 'still', 'without', 'however', 'nevertheless' 'in the absence of', 'lacking'], # except and without
        '%': [
            'because', 'as', 'since', 'if', 'then', 'from', 'due', 'when', 'while', 'during', 'for', 'given',
            'in case', 'in the event that', 'caused by', 'respective of', 'during', 'later', 'after', 'before', 'pre-', 'post-'
        ], # x of y is contextual "x in the context of y"
        '#': ['even', 'still', 'despite', 'otherwise', 'in spite of', 'regardless', 'heedless', 'irrespective'],
        '!': ['not', 'without'],
        '~': ['functions', 'that'],
        '>': ['creates', 'becomes', 'changes into', 'transforms', 'produces', 'leads to', 'converts into'],
        '@': ['changes', 'impacts', 'influences', 'adjusts', 'modulates', 'modifies', 'alters', 'affects'],
        '<': ['subset'] #'x is a subset of y'
    }
    ''' this maps operators to standard words to replace them with '''
    all_vars['operator_map'] = {
        '-' : "decrease", # attacks
        '+' : "increase", # helps
        '=' : "equal", # is
        '&' : "union", # with, union
        '|' : "alternate", # or
        '^' : "exception", # without
        '%' : "dependent", # apply
        '#' : "independent", # by standard
        '!' : "not", # negating an noun or verb
        '~' : 'functions',
        '>' : 'creates', # should add changes as well as creates
        '@' : 'changes',
        '<' : 'is subset of'
    }

    ''' sort clause delimiters so the longer strings are matched first '''
    all_vars['clause_delimiters'] = [',', ':', ';']
    for k, v in all_vars['clause_map'].items():
        all_vars['clause_delimiters'].extend(v)
    all_vars['clause_delimiters'] = reverse_sort(all_vars['clause_delimiters'])

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

    all_vars['keywords'] = {
        'treatments': [],
        'compounds': {
            'object': ['ion', 'acid'],
            'modifiers': ['oral', 'liquid', 'topical', 'intravenous', 'iv', 'injection', 'gavage', 'capsule', 'gel', 'powder', 'supplement', 'solution', 'spray', 'tincture', 'mixture'],
        },
        'patient': all_vars['supported_core']['participants']
    }
    # use participant instead of patient bc that has other meanings
    '''
        VBZ: Verb, 3rd person singular present - asks is does has
        VBG: Verb, gerund or present participle - asking, being, doing, having
        VBD: Verb, past tense - asked, was/were, did, had
    '''
    all_vars['pattern_maps'] = {
        'passive_to_active': {
            'x of y': 'y x', # to do: add support for new characters in target_pattern like 'y-x'
            'x was inhibited by y': 'y inhibits x',
            'x that has y': 'x with y',
            'x was VBD by y': 'y VBZ x',
            'x that y z': 'z y x', # "protein that modulates a (signaling pathway)" => "(signaling pathway)-changing protein" 
            'x that does VBG': 'x VBZ', # x that does inhibition => x inhibits
            'x that does VBG': 'x VBZ', # x that does inhibition => x inhibits 
            'x with y functionality': 'x y', 
            'x has ability to do y': 'x y',
            'JJ1 NN1 of JJ2 NN2': 'JJ2 NN2 JJ1 NN1'
        }
    }
    all_vars['supported_pattern_variables'] = ['N', 'V', 'ADJ', 'ADV', 'DPC', 'C', 'D', 'P']
    all_vars['pattern_index'] = {
        'passive': [
            '|VB VBP VBN VBD| |VB VBP VBN VBD|', # is done, was done
            'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', # having been done
            '|VB VBP VBN VBD| |TO IN PP|', # finish by, done by
            '|VBD| VBN VBN |TO IN PP|', # has been done by
            '|word phrase| of |word phrase|' # enzyme inhibitor of protein synthesis
        ],
        'modifier': [
            #'(?)', # add support for an any character 
            '|N V| |N ADV ADJ V|', # compound isolate
            'ALL_N IN |ADJ ADV VB VBG VBD| ALL_N', # converter of ionic/ionized/ionizing radiation, necrotizing spondylosis
            'ALL_N IN ALL_N |VBG VBD|', # metabolite of radiation poisoning
            'ALL_N IN ALL_N', # metabolite of radiation 
            'NNP ALL_N', # Diabetes mellitus
            'N N', # the second noun may have a verb root, ie "enzyme-inhibitor"
            'N V',
            'JJ NN',
            'or IN ALL_N',
            'er IN ALL_N',
            'tion IN ALL_N' # alkalization of compound => compound alkalizer => alkalizes compound
        ],
        'noun_phrases': [
            'ALL_N ALL_N',
            'ALL_N ALL_N ALL_N', # HIV-positive patients => NNP JJ NNS
        ],
        'verb_phrases': [
            'ADV ALL_V',
            'ADJ ALL_V',
            'ALL_V ALL_V', #'associating alkalizing with compound x'
            'ALL_V ALL_V',
            'plays a |VB NN| role',
            '|functions works operates interacts acts| as __a__ |VB NN|'
        ],
        'compound': [
            "administration_method of compound",
            "compound compound"
        ],
        'symptom': [
            'fever that gets worse when x',
            'x reduced y and diminished z even in condition x or condition a'
        ],
         'type': [
            'ADJ N', # Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')
        ],
        'role': [
            '|ADV V N|', # Ex: 'emulsifying protein' (role = 'emulsifier')
            'N of N', # Ex: 'components of immune system' (role = 'component', system = 'immune system')
            '|V N| role', # Ex: functional role (role => 'function')
            '|functions works operates interacts acts| as (a) |V N|' # Ex: acts as an intermediary (role => 'intermediary')
        ]
    }

    ''' sort pattern_map and pattern_index so the longer patterns are checked first '''
    all_vars['pattern_maps'] = reverse_sort(all_vars['pattern_maps'])
    all_vars['pattern_index'] = reverse_sort(all_vars['pattern_index'])

    '''
    if there are files with the 'data/objecttype_patterns.txt' name pattern, 
    pull that data and add it to pattern_index dict 
    '''
    for key in all_vars:
        cwd = os.getcwd()
        pattern_filename = ''.join([cwd, 'data/patterns_', key, '.txt'])
        if os.path.exists(pattern_filename):
            pattern_contents = read(pattern_filename)
            if pattern_contents:
                pattern_lines = pattern_contents.split('\n')
                if len(pattern_lines) > 0:
                    if key not in all_vars['pattern_index']:
                        all_vars['pattern_index'][key] = []
                    for line in pattern_lines:
                        pattern = line.split('_')[0] 
                        # just fetching the pattern, not the matches stored after the '_'         
                        all_vars['pattern_index'][key].append(pattern)
    converted_all_vars = convert_pos_names_to_nltk_tags(all_vars)
    if converted_all_vars:
        return converted_all_vars
    return all_vars

def reverse_sort(map_dict):
    '''
        - before parsing patterns, sort the patterns by number of spaces 
            so the longest patterns get parsed first as a safeguard

        - also sort clause delimiters by length before applying them so you apply 
            "but actually" as a delimiter before applying "but"
    '''
    length_index = {}
    for operator, val_list in map_dict.items():
        for item in val_list:
            length_index[item] = len(item)
    sorted_val_list = []
    for length in reversed(sorted(length_index.values())):
        sorted_val_list.append(''.join([k for k, v in length_index.items() if v == length]))
    if len(sorted_val_list) > 0:
        map_dict = sorted_val_list
    return map_dict

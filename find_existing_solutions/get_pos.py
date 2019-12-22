'''
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
    nltk.help.upenn_tagset()
'''

def get_tags():
    pos_tags = {}
    ''' I. SUBSETS '''

    '''
    pos_tags['list'] = ['LS']
        LS: List item marker - 1) A A. SP-44001 * a first one 
    pos_tags['phrase'] = ['PP', 'NNP', 'VP']
        PP: Preposition Phrase
        NNP: Proper noun, singular Phrase
        VP: Verb Phrase
    pos_tags['clause'] = ['S', 'SBAR']
        S: Simple declarative clause
        SBAR: Clause introduced by a (possibly empty) subordinating conjunction
    pos_tags['question'] = ['SBARQ', 'SQ']
        SBARQ: Direct question introduced by a wh-word or a wh-phrase.
        SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
    pos_tags['passive'] = ['SINV', 'SQ']
        SINV: Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.
        SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
    '''

    ''' II. WORDS '''
    pos_tags['N'] = ['NN', 'NNP', 'NNS', 'JJ', 'JJR'] # JJ and JJR often capture nouns rather than adjectives
    '''
        NN: Noun, singular or mass - common-carrier knuckle-duster casino thermostat investment humour falloff wind hyena override subhumanity machinist
        NNP; Proper noun, singular (Names) - Africa Michigan Hyugen NYC
        NNS: Noun, plural
        NNPS: Proper noun, plural - 'Associations'
    '''
    pos_tags['V'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] # 'VP'
    '''
        VB: Verb, base form - ask is do have build assess evaluate analyze assume avoid begin believe reveal benefit # attention?
            VBP: Verb, non-3rd person singular present - ask is do have
            VBZ: Verb, 3rd person singular present - asks is does has
            VBG: Verb, gerund or present participle - asking, being, doing, having
        VBD: Verb, past tense - asked, was/were, did, had
        VBN: Verb, past participle - asked, used, been, done, had
        VP: Verb Phrase
    '''
    pos_tags['VC'] = ['MD', 'RP']
    '''
        MD: Modal - 'could', 'will'
        RP: Particle - aboard about across along apart around aside at away back before by ever for from go i.e. in into just later more off on open out over per that through under up whole with
    '''
    pos_tags['ADV'] = ['WRB', 'RB', 'RBR', 'RBS']
    '''
        RB: Adverb - very occasionally basically practically prominently technologically predominately swiftly fiscally
        RBR: Adverb, comparative - 'better'
        RBS: Adverb, superlative - 'best'
        WRB: Wh-adverb - how however whence whenever where whereby whereever wherein whereof why
    '''
    pos_tags['ADJ'] = ['JJ', 'JJR', 'JJS']
    '''
        JJ: Adjective - big, third pre-war separable ectoplasmic battery-powered participatory multi-disciplinary
        JJR: Adjective, comparative - bigger
        JJS: Adjective, superlative - biggest
    '''
    pos_tags['SYM'] = ['CD', 'SYN']
    '''
        CD: Cardinal number - ten, 1.0, IX, '60s', DM2, mid-1890, 1,000, dozen
        SYM: Symbol 
    '''
    pos_tags['D'] = ['DT', 'PDT', 'WDT']
    '''
        DT: Determiner - all an another any both each either every half many much nary neither no some such that the them these this those
        PDT: Pre determiner - all both half many quite such sure this
        WDT: Wh-determiner - that what whatever which whichever
    '''
    pos_tags['P'] = ['TO', 'PP']
    '''
        TO: "to" as preposition or infinitive marker
        PP: Preposition Phrase
    '''
    pos_tags['C'] = ['CC', 'IN']
    '''
        CC: Coordinating conjunction - 'n and both but either et for less minus neither nor or plus so therefore times v. versus vs. whether yet
        IN: Preposition or subordinating conjunction - among upon whether out pro despite on by below within for near behind atop around if until below next into if beside
    '''
    pos_tags['DPC'] = ['DT', 'PDT', 'WDT', 'TO', 'PP', 'CC', 'IN']
    pos_tags['ALL_N'] = ['NN', 'JJ', 'JJR', 'NNS', 'NNP', 'NNPS', 'RB']
    pos_tags['ALL_V'] = ['RP', 'MD', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    pos_tags['SYNSET'] = set()
    for key in ['N', 'V', 'ADJ', 'ADV']:
        for item in pos_tags[key]:
            pos_tags['SYNSET'].add(item)
    pos_tags['SYNSET'] = list(pos_tags['SYNSET'])
    pos_tags['ALL'] = set()
    for key in pos_tags:
        for item in pos_tags[key]:
            pos_tags['ALL'].add(item)
    pos_tags['ALL'] = list(pos_tags['ALL'])
    ''' 'RB' points to 'even', 'WRB' points to when, 'JJ' describes 'due' '''
    conditional_keys = ['C', 'P', 'ADV', 'ADJ', 'VC']
    pos_tags['conditional'] = []
    for tag in conditional_keys:
        pos_tags['conditional'].extend(pos_tags[tag])
    relation_keys = ['C', 'P']
    pos_tags['relation'] = []
    for tag in relation_keys:
        pos_tags['relation'].extend(pos_tags[tag])

    ''' III. REMOVE '''

    # safe to remove pronouns unless theres ambiguity - converted sentence should be less ambiguous
    # replace_with_syns() takes out symbols, punctuation, and determiners if indicating 'some'
    # to do: once you establish coordinating relationships or ratios, remove determiners & prepositions 

    pos_tags['exclude'] = ['UN', 'EX', 'FW', 'TO', 'PRP', 'PRP$', 'WP', 'WP$', 'POS']
    ''' 
        UH: interjection - goodbye hey amen huh uh shucks heck anyways
        EX: Existential there - 'there' (in 'there exists')
        FW: Foreign word
        PRP: Personal pronoun - hers herself him himself hisself it itself me myself one oneself ours ourselves ownself self she thee theirs them themselves they thou thy us
        WP: Wh-pronoun - that what whatever whatsoever which who whom whosoever
        WP$ Possessive wh-pronoun - 
        POS: Possessive ending - ' 's in words to indicating someone's property (my parents' house, womens' issues, people's problems)
        PRP$: Possessive pronoun - her his mine my our ours their thy your
    '''

    return pos_tags

def get_empty_index(av):
    '''
    indexes isolates treatments from symptoms, metrics, etc to build indexes of those objects on your local env
    rows
        - ensures data remains tied to its original context
        - it has the same elements as index but stores them by each sentence 
          from source data containing a symptom, condition, treatment, etc
    rows = [
        {
            'condition': ['meningitis'],
            'symptom': ['temperature'],
            'treatments_successful': ['fluconazole'],
            'insight': ['fluconazole effective 10-week survival'],
            ...
        },
        {
            'condition': ['diabetes'],
            'symptom': ['organ failure'],
            'treatments_successful': ['metformin'],
            'insight': ['metformin effective for diabetes'],
            ...
        },
        {
            'metric': {'naa-cr ratio': 'reduced'}
            'condition': ['hiv', 'encephalopathy'],
            'component': {
                'organ': ['brain', 'immune system'],
                'microbe': [],
                'cell': [],
                'gene': [],
                'enzyme': [],
                'biosystem': ['immune system', 'nervous system']
            }
            'compound': ['naa', 'cr'],
            'treatments_successful': [],
            'treatments_failed': [],
            'intent': ['diagnose'],
            'insight': [
                'naa-to-cr ratio is reduced in hiv patients', 
                'naa-to-cr ratio is a marker for hiv brain infection'
            ],
            "strategies": [
                'target bio markers that change with illness for testing',
                'consider other conditions like lack/excess of signals from diagnostic tests & interfering diseases'
            ],
            "symptoms": [
                'encephalopathy': 'no imaging findings',
                'neurological disease': 'other'
            ],
            "patient_conditions": ['HIV-positive'],
            "patient_symptoms": ['neurological disease']
        }
    ]
    '''
    index = {}
    index_keys = []
    for key in av['full_params'].keys():
        if key != 'request':
            for item in av['full_params'][key]:
                index_keys.append(item)
    dict_keys = ['count', 'pattern', 'pos', 'word_map']
    av['metadata'] = index_keys if 'metadata' not in av or 'all' in av['metadata'] else av['metadata']
    for key in av['metadata']:
        if key in index_keys:
            if key not in dict_keys:
                index[key] = set()
            else:
                index[key] = {}
    index['data'] = [] # not necessary to ensure uniqueness in articles
    return index
from nltk import pos_tag, word_tokenize 

'''
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
    nltk.help.upenn_tagset()
'''

def unconjugate(verb, pos, pos_tags):
    ''' the basic form of a verb is VB, so if this is a verb, 
        convert all other verb forms to that verb form
    '''
    tag = get_nltk_pos(verb)
    if tag != 'VB':
        if tag in pos_tags['verbs']:
            base_verb = change_to_infinitive(verb)
            if base_verb:
                return base_verb
    return verb

def convert_words_to_pos(line, all_vars):
    new_line = []
    for word in line.split(' '):
        pos = get_pos(word, all_vars)
        val = pos if pos else word
        new_line.append(val)
    line = ' '.join(new_line)
    return line

def get_nltk_objects(tag_key, line, all_vars):
    items = []
    if tag_key in all_vars['pos_tags']:
        tagged = pos_tag(word_tokenize(line))
        if tagged:
            for item in tagged:
                if item[1] in all_vars['pos_tags'][tag_key]:
                    items.append(item[0])
    if len(items) > 0:
        return items
    return False

def convert_nltk_tags_to_pos_names(source_list, all_vars):
    ''' this function converts 'NN' => 'noun'  '''
    new_list = []
    for p in source_list:
        for pos in p.split(' '):
            # pos should be '__VP' or 'VB' or '|NN' or 'NNP|'
            isolated_pos = pos.replace('__', '').replace('|', '')
            for tag, tags in all_vars['pos_tags'].items():
                if isolated_pos in tags:
                    pos_tag = pos.replace(isolated_pos, tag)
                    p = p.replace(pos, pos_tag)
        new_list.append(p)
    if len(new_list) > 0:
        return new_list
    return False

def get_nltk_pos(word):
    tagged = pos_tag(word_tokenize(word))
    if len(tagged) > 0:
        for item in tagged:
            if len(item) > 0:
                return item[1]
    return False

def get_pos(word, all_vars):
    ''' get 'noun' from 'voter' rather than 'NN' '''
    if len(word) > 0:
        pos = get_nltk_pos(word)
        pos_key = pos
        if pos not in all_vars['pos_tags']['exclude']:
            for key, val in all_vars['pos_tags'].items():
                if pos in val and key in all_vars['supported_tags']:
                    return key
    return False

def get_pos_tags():
    pos_tags = {}
    ''' I. SUBSETS '''

    pos_tags['list'] = ['LS']
    ''' 
        LS: List item marker - 1) A A. SP-44001 * a first one 
    '''
    pos_tags['phrase'] = ['PP', 'NNP', 'VP']
    '''
        PP: Preposition Phrase
        NNP: Proper noun, singular Phrase
        VP: Verb Phrase
    '''
    pos_tags['clause'] = ['S', 'SBAR']
    '''
        S: Simple declarative clause
        SBAR: Clause introduced by a (possibly empty) subordinating conjunction
    '''
    pos_tags['conditional'] = ['CC', 'IN', 'RB', 'WRB', 'JJ'] # 'RB' points to 'even', 'WRB' points to when, 'JJ' describes 'due'

    pos_tags['question'] = ['SBARQ', 'SQ']
    '''
        SBARQ: Direct question introduced by a wh-word or a wh-phrase.
        SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
    '''
    pos_tags['passive'] = ['SINV', 'SQ']
    '''
        SINV: Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.
        SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
    '''

    ''' II. WORDS '''
    pos_tags['noun'] = ['NN', 'NNP', 'NNS', 'JJ', 'JJR'] # JJ and JJR often capture nouns rather than adjectives
    '''
        NN: Noun, singular or mass - common-carrier knuckle-duster casino thermostat investment humour falloff wind hyena override subhumanity machinist
        NNP; Proper noun, singular (Names) - Africa Michigan Hyugen NYC
        NNS: Noun, plural
        NNPS: Proper noun, plural - 'Associations'
    '''
    pos_tags['verb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'VP']
    '''
        VB: Verb, base form - ask is do have build assess evaluate analyze assume avoid begin believe reveal benefit # attention?
            VBP: Verb, non-3rd person singular present - ask is do have
            VBZ: Verb, 3rd person singular present - asks is does has
            VBG: Verb, gerund or present participle - asking, being, doing, having
        VBD: Verb, past tense - asked, was/were, did, had
        VBN: Verb, past participle - asked, used, been, done, had
        VP: Verb Phrase
    '''
    pos_tags['verb_keywords'] = ['RP', 'MD']
    '''
        RP: Particle - aboard about across along apart around aside at away back before by ever for from go i.e. in into just later more off on open out over per that through under up whole with
        MD: Modal - 'could', 'will'
    '''
    pos_tags['adv'] = ['WRB', 'RB', 'RBR', 'RBS']
    '''
        RB: Adverb - very occasionally basically practically prominently technologically predominately swiftly fiscally
        RBR: Adverb, comparative - 'better'
        RBS: Adverb, superlative - 'best'
        WRB: Wh-adverb - how however whence whenever where whereby whereever wherein whereof why
    '''
    pos_tags['adj'] = ['JJ', 'JJR', 'JJS']
    '''
        JJ: Adjective - big, third pre-war separable ectoplasmic battery-powered participatory multi-disciplinary
        JJR: Adjective, comparative - bigger
        JJS: Adjective, superlative - biggest
    '''
    pos_tags['sym'] = ['CD', 'SYN']
    '''
        CD: Cardinal number - ten, 1.0, IX, '60s', DM2, mid-1890, 1,000, dozen
        SYM: Symbol # took out symbols in replace_syns()   
    '''
    # once you establish coordinating relationships or ratios, remove determiners & prepositions 
    pos_tags['det'] = ['DT', 'PDT', 'WDT']
    '''
        DT: Determiner - all an another any both each either every half many much nary neither no some such that the them these this those
        PDT: Pre determiner - all both half many quite such sure this
        WDT: Wh-determiner - that what whatever which whichever
    '''
    pos_tags['prep'] = ['TO', 'PP']
    '''
        TO: "to" as preposition or infinitive marker
        PP: Preposition Phrase
    '''
    pos_tags['conj'] = ['CC', 'IN']
    '''
        CC: Coordinating conjunction - 'n and both but either et for less minus neither nor or plus so therefore times v. versus vs. whether yet
        IN: Preposition or subordinating conjunction - among upon whether out pro despite on by below within for near behind atop around if until below next into if beside
    '''
    pos_tags['all_nouns'] = ['NN', 'JJ', 'JJR', 'NNS', 'NNP', 'NNPS', 'RB']

    ''' III. REMOVE '''
    # safe to remove pronouns unless theres ambiguity - converted sentence should be less ambiguous
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

def get_determiner_ratio(word, number_of_items):
    '''
    word = 'giraffes'
    number_of_items = number of giraffes
    '''
    extra = str(number_of_items + 1)
    same = str(number_of_items)
    high = str(number_of_items - 1)
    some = str(int(round(number_of_items / 2)))
    ratios = {
        extra: ['extra', 'another', 'more'],
        same: ['whole', 'both', 'all', 'every', 'each'], # to do: integrate equal keywords like 'basically', 'essentially', 'same', 'equal']
        high: ['high', 'extremely', 'such', 'especially', 'very', 'much', 'many', 'quite'],
        some: ['a', 'an', 'lot', 'any', 'whatever', 'which', 'whichever', 'part', 'either', 'half', 'some'],
        '1': ['the', 'this', 'that', 'those', 'these', 'them', 'particular'],
        '0': ['none', 'nothing', 'nary', 'neither', 'nor', 'no']
    }
    for k, v in ratios.items():
        if word in v:
            ratio = round((int(k) / number_of_items), 1)
            return ratio
    return 0
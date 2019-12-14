from nltk import pos_tag, word_tokenize 
from textblob import TextBlob

'''
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
    nltk.help.upenn_tagset()
'''

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

def convert_pos_names_to_nltk_tags(all_vars):
    '''
    - convert noun => |NN JJ JJR NNS NNP NNPS RB] 
        which is every nltk pos in all_vars['pos_tags']['ALL_N'] 
        and same for verbs since nouns & verbs are often identified as other tags, 
        which are listed in ALL_N and ALL_V

    - for every pattern found in all_vars['pattern_index'], replace keywords with nltk tags:

        all_vars['pos_tags']['D'] = ['DT', 'PDT', 'WDT']
        all_vars['pos_tags']['P'] = ['TO', 'PP']
        all_vars['pos_tags']['C'] = ['CC', 'IN']
        all_vars['pos_tags']['DPC'] = ['DT', 'PDT', 'WDT', 'TO', 'PP', 'CC', 'IN']

        all_vars['pos_tags']['ADV'] = ['WRB', 'RB', 'RBR', 'RBS']
        all_vars['pos_tags']['ADJ'] = ['JJ', 'JJR', 'JJS']

        all_vars['pos_tags']['N'] = ['NN', 'NNP', 'NNS', 'JJ', 'JJR']
        all_vars['pos_tags']['V'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        all_vars['pos_tags']['ALL_N'] = ['NN', 'JJ', 'JJR', 'NNS', 'NNP', 'NNPS', 'RB']
        all_vars['pos_tags']['ALL_V'] = ['RP', 'MD', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

    '''
    for pattern_type, pattern_list in all_vars['pattern_index'].items():
        new_list = []
        for p in pattern_list:
            new_words = []
            for word in p.split(' '):
                if word in all_vars['supported_pattern_variables']:
                    nltk_pos = ''.join(['|', ' '.join(all_vars['pos_tags'][word]), '|'])
                    # pos should now be '__VP' or 'VB' or '|NN NNP|'
                    new_words.append(nltk_pos)
            if len(new_words) > 0:
                new_list.append(' '.join(new_words))
        if len(new_list) > 0:
            all_vars['pattern_index'][pattern_type] = new_list
    return all_vars

def get_nltk_pos(word, all_vars):
    if word in [a for a in all_vars['alphabet']]:
        return False
    tags = TextBlob(word).parse()
    tags_split = tags.split('/')
    blob_pos = tags_split[1] if len(tags_split) > 1 else None
    tagged = pos_tag(word_tokenize(word))
    if len(tagged) > 0:
        for item in tagged:
            if len(item) > 0:
                if blob_pos != item[1]:
                    ''' blob identifies 'explains' as a verb when nltk doesnt '''
                    if blob_pos in all_vars['pos_tags']['ALL_V']:
                        return blob_pos
                return item[1]
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
    pos_tags['verb_keywords'] = ['RP'] 
    '''
        RP: Particle - aboard about across along apart around aside at away back before by ever for from go i.e. in into just later more off on open out over per that through under up whole with
    '''
    pos_tags['verb_potential'] = ['MD']
    '''
        MD: Modal - 'could', 'will'
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
    '''
    replace_with_syns() takes out symbols, punctuation, and determiners if indicating 'some'
    '''
    # once you establish coordinating relationships or ratios, remove determiners & prepositions 
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
    '''
    'RB' points to 'even', 'WRB' points to when, 'JJ' describes 'due'
    '''
    conditional_keys = ['C', 'P', 'ADV', 'ADJ', 'verb_potential']
    pos_tags['conditional'] = []
    for tag in conditional_keys:
        pos_tags['conditional'].extend(pos_tags[tag])

    relation_keys = ['C', 'P']
    pos_tags['relation'] = []
    for tag in relation_keys:
        pos_tags['relation'].extend(pos_tags[tag])

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
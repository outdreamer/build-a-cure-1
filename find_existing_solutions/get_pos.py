def convert_words_to_pos(line):
    new_line = []
    for word in line.split(' '):
        pos = get_pos(word)
        val = pos if pos else word
        new_line.append(val)
    line = ' '.join(new_line)
    return line

def convert_nltk_tags_to_pos_names(source_list, all_vars):
    ''' this function converts 'NN' => 'noun'  '''
    new_list = []
    for p in source_list:
        for pos in p.split(' '):
            # pos should be '__VP' or 'VB' or '|NN' or 'NNP|'
            isolated_pos = pos.replace('__','').replace('|','')
            for tag, tags in all_vars['pos_tags'].items():
                if isolated_pos in tags:
                    pos_tag = pos.replace(isolated_pos, tag)
                    p = p.replace(pos, pos_tag)
        new_list.append(p)
    if len(new_list) > 0:
        return new_list
    return False

def get_pos_name(word, all_vars):
    ''' get 'noun' from 'voter' rather than 'NN' '''
    if len(word) > 0:
        stem = get_stem(word)
        words = [word, stem] if stem else [word]
        # get pos of word first, then stem if no results found for word
        for word in words:
            pos = get_nltk_pos_of_word(word)
            for tag_type in all_vars['supported_tags']:
                if tag_type in all_vars['pos_tags']:
                    if pos in all_vars['pos_tags'][tag_type]:
                        return all_vars['tag_name_map'][pos]

            ''' check original synsets before any stem processing, including stem synsets'''
            synsets = get_synsets(word)
            max_synset_count = max(synsets.keys())
            max_synsets = synsets[max_synset_count]
            # max_synsets = ['verb', 'noun'] means its likelist & equally likely to be a verb or noun
            if len(max_synsets) > 0:
                first_max = max_synsets[0]
                for ms in max_synsets:
                    if ms == pos:
                        return ms
                return first_max
        if len(pos) > 0:
            if pos[0] not in exclude:
                print('get_pos: unknown word type', word, pos)
    return False

def get_nltk_pos_of_word(word):
    tagged = pos_tag(word_tokenize(word))
    if len(tagged) > 0:
        for item in tagged:
            if item[0].lower() == word.lower():
                return item[1]
    return False

def get_synsets(word):
    synsets = {
        'noun': get_synsets_of_type(word, NOUN),
        'verb': get_synsets_of_type(word, VERB),
        'adverb': get_synsets_of_type(word, ADV),
        'adjective': get_synsets_of_type(word, ADJ)
    }
    synsets['counts'] = {}
    for k, v in synsets.items():
        v_count = len(v) if v else 0
        if v_count not in synsets['counts']:
            synsets['counts'][v_count] = [k]
        else:
            synsets['counts'][v_count].append(k)
    return synsets

def get_synsets_of_type(word, pos_type):
    if pos_type in [NOUN, VERB, ADV, ADJ]:
        if len(word) > 0 and pos_type > 0 and pos_type in all_vars['supported_tags']:
            synsets = Word(word).get_synsets(pos=pos_type)
            if len(synsets) > 0:
                return [s.name().split('.')[0].lower() for s in synsets]
    return False

def get_pos_tag(word, all_vars):
    tagged = pos_tag(word_tokenize(word))
    for item in tagged:
        tag = item[1]
        confirmed_tag = confirm_tag_with_preference_rules(tag, word, pos_tags)
        if confirmed_tag:
            return confirmed_tag
    return False

def confirm_tag_with_preference_rules(nltk_tag_name, word, all_vars):
    ''' to do: you could just implement ordered preferences
     by iterating through pos_tags with a list of keys '''

    ''' nltk_tag_name is the tag selected by nltk
    sometimes youll have to choose which tag to assign based 
    on your analysis between alternate/overlapping categories
    '''
    confirmed_tag = nltk_tag_name
    if nltk_tag_name in all_vars['tag_name_map']:
        nltk_tag_name = all_vars['tag_name_map'][nltk_tag_name] # returns noun for NN, NP, etc
        custom_tag = get_custom_tag(word, all_vars)
    return confirmed_tag

def get_custom_tag(word, all_vars):

def unconjugate(verb, pos, pos_tags):
    ''' the basic form of a verb is VB, so if this is a verb, 
        convert all other verb forms to that verb form
    '''
    if pos == 'verb':
        tag = get_pos_tag(verb)
        if tag != 'VB':
            if tag in pos_tags['verbs']:
                #base_verb = convert(verb)
                if base_verb:
                    return base_verb
    return verb

def get_pos_tags():

    article_tags = ['question', 'passive', 'list', 'phrase', 'clause']

    ''' to do: where theres overlap between categories, you need a ranking to select the correct type '''
    pos_tags = {}

    ''' I. SENTENCE TYPES '''
    pos_tags['question'] = ['SBARQ', 'SQ']
    '''
    SBARQ: Direct question introduced by a wh-word or a wh-phrase.
    SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
    '''
    pos_tags['passive'] = [
    '''
    SINV: Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.
    SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
    '''

    ''' II. PHRASES & CLAUSES '''
    pos_tags['list'] = ['LS']
    '''
    LS: List item marker - 1) A A. SP-44001 * a first one
    '''
    ''' use these to find phrases '''
    pos_tags['conjunction'] = ['CC', 'IN']
    '''
    CC: Coordinating conjunction - 'n and both but either et for less minus neither nor or plus so therefore times v. versus vs. whether yet
    IN: Preposition or subordinating conjunction 
    astride among uppon whether out inside pro despite on by throughout below within for towards near behind atop around if like until below next into if beside
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

    ''' III. REMOVE '''
    # safe to remove pronouns unless theres ambiguity - converted sentence should be less ambiguous
    pos_tags['pronoun'] = ['PRP', 'PRP$']
    '''
    PRP: Personal pronoun - hers herself him himself hisself it itself me myself one oneself ours ourselves ownself self she thee theirs them themselves they thou thy us
    PRP$: Possessive pronoun - her his mine my our ours their thy your
    WP: Wh-pronoun - that what whatever whatsoever which who whom whosoever
    WP$ Possessive wh-pronoun - 
    '''
    pos_tags['possessive'] = ['POS', 'PRP$', 'WP$']
    '''
    POS: Possessive ending - ' 's in words to indicating someone's property (my parents' house, womens' issues, people's problems)
    PRP$: Possessive pronoun - her his mine my our ours their thy your
    WP$ Possessive wh-pronoun - 
    '''
    # also safe to remove determiners & prepositions once you establish coordinating relationships
    pos_tags['determiner'] = ['DT', 'PDT', 'WDT']
    '''
    DT: Determiner - all an another any both del each either every half many much nary neither no some such that the them these this those
    PDT: Pre determiner - all both half many quite such sure this
    WDT: Wh-determiner - that what whatever which whichever
    '''
    pos_tags['preposition'] = ['TO', 'PP']
    '''
    TO: "to" as preposition or infinitive marker
    PP: Preposition Phrase
    '''

    ''' IV. BASIC POS '''
    pos_tags['noun'] = ['NN', 'NNP', 'NNS', 'JJ', 'JJR'] 
    # JJ and JJR often capture nouns rather than adjectives
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
    pos_tags['interjection'] = ['UN']
    '''
    UH: interjection - goodbye hey amen huh uh shucks heck anyways
    '''
    pos_tags['adverb'] = ['WRB', 'RB', 'RBR', 'RBS']
    '''
    RB: Adverb - very occasionally basically practically prominently technologically predominately swiftly fiscally
    RBR: Adverb, comparative - 'better'
    RBS: Adverb, superlative - 'best'
    WRB: Wh-adverb - how however whence whenever where whereby whereever wherein whereof why
    '''
    pos_tags['adjective'] = ['JJ', 'JJR', 'JJS']
    '''
    JJ: Adjective - big, third pre-war separable ectoplasmic battery-powered participatory multi-disciplinary
    JJR: Adjective, comparative - bigger
    JJS: Adjective, superlative - biggest
    '''
    pos_tags['exclude'] = ['DT', 'WRB', 'TO', 'CC', 'IN', 'FW', 'EX']
    '''
    EX: Existential there - 'there' (in 'there exists')
    FW: Foreign word
    '''
    pos_tags['symbolic'] = ['CD', 'SYN']
    '''
    CD: Cardinal number - ten, 1.0, IX, '60s', DM2, mid-1890, 1,000, dozen
    SYM: Symbol # took out symbols in replace_syns()   
    '''
    return pos_tags

'''
    https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk

    nltk.help.upenn_tagset()

    CC: Coordinating conjunction
    CD: Cardinal number
    DT: Determiner
    EX: Existential there
    FW: Foreign word
    IN: Preposition or subordinating conjunction
    JJ: Adjective
    JJR: Adjective, comparative
    JJS: Adjective, superlative
    LS: List item marker
    MD: Modal
    NN: Noun, singular or mass
    NNS: Noun, plural
    PP: Preposition Phrase
    NNP: Proper noun, singular Phrase
    NNPS: Proper noun, plural
    PDT: Pre determiner
    POS: Possessive ending
    PRP: Personal pronoun Phrase
    PRP: Possessive pronoun Phrase
    RB: Adverb
    RBR: Adverb, comparative
    RBS: Adverb, superlative
    RP: Particle
    S: Simple declarative clause
    SBAR: Clause introduced by a (possibly empty) subordinating conjunction
    SBARQ: Direct question introduced by a wh-word or a wh-phrase.
    SINV: Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.
    SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.
    SYM: Symbol
    VP: Verb Phrase
    VBD: Verb, past tense
    VBG: Verb, gerund or present participle
    VBN: Verb, past participle
    VBP: Verb, non-3rd person singular present
    VBZ: Verb, 3rd person singular present
    WDT: Wh-determiner
    WP: Wh-pronoun
    WP: Possessive wh-pronoun
    WRB: Wh-adverb
'''
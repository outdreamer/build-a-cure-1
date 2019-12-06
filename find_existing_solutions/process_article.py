from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob, Word

stemmer = SnowballStemmer("english")  
stop = set(stopwords.words('english'))

data = None
with open('article.txt', 'r') as f:
    data = f.read()
    f.close()
if data:
    counts = {}
    phrases = {}
    taken_out = []
    names = set()
    verbs = set()
    common_nouns = set()
    for line in data.split('. '):
        data_words = data.strip().split(' ')
        processed_data = data.lower().replace('"', '').replace("'",'').replace(',','').replace('(','').replace(')','').replace('[','').replace(']','')
        name_line = line.replace('"', '').replace("'",'').replace('(','').replace(')','').replace('[','').replace(']','')
        name_tagged = pos_tag(word_tokenize(name_line))
        line = line.replace('"', '').replace("'",'').replace(',','').replace('(','').replace(')','').replace('[','').replace(']','')
        tagged = pos_tag(word_tokenize(line))
        leave_in_pos = ['NNP', 'NNS', 'JJR'] # JJR example: 'broader'
        common_noun_pos = ['JJ', 'NN']
        verb_pos = ['VB', 'VBP', 'VBD', 'VBG', 'VBN', 'VBZ']
        blob = TextBlob(name_line)
        new_line = line # replace names in new line if any are found so theyre not included in tagged after name loop
        print('tagged', tagged)
        for p in blob.noun_phrases:
            if len(p) > 0:
                new_name = []
                phrase_words = p.split(' ')
                for name in phrase_words:
                    pos = set(item[1] for item in tagged if item[0].lower() == name)
                    for item in pos:
                        print('item', item, name)
                        if item in verb_pos and name not in stop:
                            verbs.add(name)
                        elif item in common_noun_pos:
                            ''' check if the noun stem is a verb, if so add it to verbs '''
                            stem = stemmer.stem(name)
                            verb_suffixes = ['e', 'd', 'ed'] # this adds a lot of nouns like worm & rat to the verbs list
                            verb_versions = [pos_tag(word_tokenize(''.join([name, v]))) for v in verb_suffixes] # append verb affixes and check if its a verb
                            tags = pos_tag(word_tokenize(stem))
                            if tags[0][1] in verb_pos: # or verb_versions[0][0][1] in verb_pos or verb_versions[1][0][1] in verb_pos or verb_versions[2][0][1] in verb_pos:
                                verbs.add(name)
                            else:
                                if name not in stop:
                                    common_nouns.add(name)
                        elif item == 'NNP':
                            name = ''.join([name[0].upper(), name[1:]]) if '.' not in name and '/' not in name else name.upper()
                            new_name.append(name)  
                        else:
                            taken_out.append('_'.join([name, item[1]]))                                          
                final_name = ' '.join(new_name)
                if len(new_name) == len(phrase_words) and final_name != data_words[0] and final_name.lower() not in common_nouns and final_name.lower() not in verbs:
                    names.add(final_name) # find names and store separately
                    new_line = line.replace(final_name, '')
        print('names', names)
        '''
        to do: exclude places 'Michigan' & common nouns 'Medical Center'
        names {'Hu', 'Patrick Hu', 'Advances', 'PI3K/AKT', 'Insulin', 'Michigan', 'Ming Liu', 'M.D', 'Peter Arvan', 'Caenorhabditis', 'Er', 'Vanderbilt', 'Medical Center', 'Alzheimers', 'Trap-alpha'}
        '''
        blob = TextBlob(new_line)
        tagged = pos_tag(word_tokenize(new_line))
        print('tagged', tagged)
        for item in tagged:
            if len(item) == 2:
                w = item[0].lower()
                if item[1] in leave_in_pos:
                    if len(w) > 0 and w not in stop:
                        w_upper = w.upper()
                        w_name = ''.join([w[0].upper(), w[1:]])
                        upper_count = data_words.count(w_upper) # find acronyms, ignoring punctuated acronym
                        count = processed_data.count(w)
                        ## and w not in verbs and w not in common_nouns and w_name not in ' '.join(names):
                        if item[0] == w_name and w_name != data_words[0] and w_name not in ' '.join(names): # exclude first word in sentence
                            if upper_count > 0 and upper_count <= count:
                                if upper_count not in counts:
                                    counts[upper_count] = set()
                                counts[upper_count].add(w_upper)
                            else:
                                if count > 0:
                                    if count not in counts:
                                        counts[count] = set()
                                    counts[count].add(w)
        for p in blob.noun_phrases:
            if len(p) > 0:
                for n in p.split(' '):
                    new_p = set()
                    p_name = ''.join([n[0].upper(), n[1:]])
                    for name in names:
                        if name not in p_name:
                            new_p.add(n)
                    p = ' '.join(new_p)
                    if len(p.strip()) > 0:
                        proceed = True
                        if len(phrase_words) == 1:
                            pos = set(item[1] for item in tagged if item[0].lower() == phrase_words[0])
                            for item in pos:
                                if item in verb_pos:
                                    proceed = False
                        if proceed:
                            p_upper = p.upper()
                            upper_count = data_words.count(p_upper) # find acronyms
                            phrase_count = processed_data.count(p)
                            if p not in verbs and p not in common_nouns and p_name not in ' '.join(names) and p not in stop:
                                if upper_count > 0 and len(p_upper) > 0 and upper_count < phrase_count:
                                    if upper_count not in phrases:
                                        phrases[upper_count] = set()
                                    phrases[upper_count].add(p_upper)
                                else:
                                    if phrase_count not in phrases:
                                        phrases[phrase_count] = set()
                                    phrases[phrase_count].add(p)

    print('counts', counts)
    print('phrases', phrases)
    print('verbs', verbs)
    print('nouns', common_nouns)
    print('names', names)
    print('taken_out', taken_out)

patterns = []

'''
- types follow patterns:
    1. <adjective> <noun>
    Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')

- roles follow patterns:
    1. <adverb> || <verb> <noun>
    Ex: 'emulsifying protein' (role = 'emulsifier')

    2. <noun> of <noun>
    Ex: 'components of immune system' (role = 'component', system = 'immune system')

    3. <verb> || <noun> role
    Ex: functional role (role => 'function')

    4. functions/works/operates/interacts/acts as (a) <verb> || <noun>
    Ex: acts as an intermediary (role => 'intermediary')

- roles are intrinsically related to functions, intents, strategies, & mechanisms

# the word with the highest count that is a noun is likely to be a focal object of the article

counts {
	 1: {'science', 'beyond'},
	 2: {'university'},
	 11: {'insulin'},
	 5: {'said'}
}
phrases {
	 3: {'elegans', 'pi3k/akt', 'likely', 'm.d'},
	 1: {'pathways', 'systems', 'broader', 'variants', 'processing', 'synthesis', 'imbalances', 'besides', 'strategies', 'drugs', 'therapies'},
	 2: {'ways', 'molecules', 'components', 'worms'},
	 7: {'cells'},
	 4: {'diseases', 'proteins'}
}
verbs {'responses', 'maintaining', 'fold', 'contributes', 'understanding', 'exists', 'deleting', 'corresponding', 'screen'}
nouns {
	'researcher', 'total', 'sclerosis', 'proper', 'stress', 'parent', 'abnormal', 'phenotype', 'disease', 'human', 'chaperone', 'convenient', 'protein', 'professor', 'pancreatic', 'rat', 'genetic', 'amyotrophic', 
	'percent', 'insulin', 'reticulum', 'biogenesis', 'content', 'new', 'role', 'homeostasis', 'mammalian', 'health', 'contribution', 'Trap-alpha', 'model', 'associate', 'worm', 'pathway', 'research', 'expression', 
	'cancer', 'beta', 'endoplasmic', 'cell', 'response', 'gene', 'insulin-like', 'system', 'cellular', 'oncology', 'nematode', 'lateral', 'growth', 'factor', 'anti-tumor', 'unexpected', 'neurodegenerative', 'reduction', 
	'approach', 'culture', 'primordial', 'common', 'perspective'
}
names {'Caenorhabditis', 'Medical Center', 'Advances', 'Er', 'Hu', 'Peter Arvan', 'Vanderbilt', 'Alzheimers', 'PI3K/AKT', 'Michigan', 'M.D', 'Patrick Hu', 'Trap-alpha', 'Ming Liu'}
taken_out [
	'therapies_N', 'drugs_N', 'strategies_N', 'pathways_N', 'components_N', 'elegans_N', 'worms_N', 'systems_N', 'variants_N', 'cells_N', 'cells_N', 'molecules_N', 'cells_N', 'proteins_N', 'proteins_N', 
	'were_R', 'likely_B', 'imbalances_N', 'diseases_N', 'molecules_N', 'besides_N', 'broader_J', 'ways_N'
]

 '''

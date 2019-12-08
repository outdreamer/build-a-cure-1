''' important note for pattern definitions in get_vars:
    - always put the extended pattern first
    - if you put '<noun>' before "<noun> <noun>',
        you'll miss phrases like 'compound acid' returning matches like:
             ['compound acid']
        and will instead get matches for the '<noun>' pattern:
            ['compound', 'acid']
        so make sure thats what you want before ignoring this rule
        
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
'''

def convert_patterns(lang_patterns):
    patterns = []
    for p in lang_patterns:
        pattern = []
        for alt_phrases in p.split('--'):
            pos_list = alt_phrases.split(' ')
            all_pos = [True for pos_item in pos_list if pos_item in all_vars['language_pos_map'].keys()]
            if len(all_pos) == len(pos_list):
                ''' this is a set of alternative parts of speech '''
                final_list= ['[']
                for item in pos_list:
                    final_list.append(all_vars['language_pos_map'][item].replace('[','').replace(']',''))
                final_list.append(']')
                pattern.append(''.join(final_list))
        for i, w in enumerate(p.split(' ')):
            if w in all_vars['language_pos_map'].values():
                pattern.append(all_vars['language_pos_map'][w])
            else:
                pattern.append(w)
        patterns.append(' '.join(pattern))
    if len(patterns) > 0:
        return patterns
    return False

def convert_to_pattern_format(line):
    new_line = []
    for word in line.split(' '):
        pos = get_pos(word)
        val = pos if pos else word # to do: restrict by pattern_words
        new_line.append(val)
    line = ' '.join(new_line)
    return line

def find_pattern(original, line, pattern):
    found_phrases = []
    original_split = original.split(' ')
    if pattern in line:
        ''' replace pattern with pos so each pos in pattern is only taking up one item in line.split(' ') '''
        line_split = line.split(pattern)
        for i, phrase in enumerate(line_split):
            words = phrase.split(' ')
            if i < (len(line_split) - 1):
                new_pattern = []
                for j in range(0, len(pattern.split(' '))):
                    pattern_index = len(words) + j - 1
                    if pattern_index < len(original_split):
                        new_pattern.append(original_split[pattern_index])
                found_phrases.append(' '.join(new_pattern))            
    if len(found_phrases) > 0:
        return found_phrases, pattern
    return False, False

def get_pattern_stack(line):
    line = line.replace('\n','').replace('.', '')
    original = line
    pattern_stack = {}
    pos_line = convert_to_pattern_format(line)
    for pattern in patterns:
        found, adjusted_pattern = find_pattern(original, pos_line, pattern)
        if found:
            if adjusted_pattern not in pattern_stack:
                pattern_stack[adjusted_pattern] = found
            else:
                pattern_stack[adjusted_pattern].extend(found)
    return pattern_stack
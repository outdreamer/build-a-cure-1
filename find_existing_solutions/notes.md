
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
        intents = function outputs, including unintended/emergent/unforeseen side effects (target/avoid)
        roles = functions
        relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
        components = compounds, symptoms, treatments, metrics, conditions, stressors, types, variables
    '''
    '''
        'passive_identifier': [
            'noun_phrase1 of noun_phrase2' # enzyme inhibitor of protein synthesis - 
            # to do: there are some examples where this structure adds clarity rather than just adding words, like where modifier relationships arent clear
        ],
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
        'context_identifier': [],
        'condition_identifier': [],
        'compound_identifier': [
            "rule_identifier of compound_identifier",
            "compound_identifier compound_identifier"
        ],
        'symptom_identifier': [
            'N that gets worse when context_identifier',
            'x - y & - z even in condition_identifier or condition_identifier'
        ]
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
            - __a__ : an optional item
            - |a b c| : a set of alternatives, each of which will be selected one at a time in the output patterns
            - if you include 'N' in your pattern, it'll replace it with all the noun pos tags, like |NN NNS NNP NNPS| etc
    '''
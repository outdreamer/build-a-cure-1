from get_structural_objects import get_relationships_from_clauses

''' 
    each main medical object deserves its own dictionary, which can be built with rows data
    'synthesis_instructions' = {
        'parameters',
        'optimal_parameter_values',
        'required_compounds',
        'substitutes',
        'equipment_links',
        'adjacent_compounds_and_steps',
    }
    'symptom' = {
        'attributes': [],
        'rules': [],
        'states': [],
        'treatments': []
    }
    'compounds' = {
        'attributes': [],
        'rules': [],
        'states': [],
        'side_effects': [] # this is just a list of symptoms the compound causes, which can be assembled from rows data
    }

Treatments:
    treatment_administration_modifiers = ['oral','liquid','topical','intravenous', 'iv']
    treatment_administration_methods = ['injection','gavage','capsule', 'gel', 'powder','supplement', 'solution', 'spray', 'tincture', 'mixture']
    
Compounds:
    compound_modifiers = ['isolate', 'ion', 'acid']
    compound_patterns = [
        "administration_method of compound",
        "compound compound"
    ]

Patients:
    # treatments mention response in patients/subjects
    patient_keywords = supported_core['participant'] # use participant instead of patient bc that has other meanings

Side effect keywords to use to test relationships derived with nlp tools:
  - nouns: effect, activation, activity, reaction, process, role
  - adjectives:
  - objects: 
    - functions: attenuate, enhance, reduce, down/up/regulate, stimulate, de/activate, dis/enable, absorb, catalyze, alleviate, suppress, decline, increase, enrich, moderate, adjust, change
    - experiment:
      - properties: parameters, linearity, sensitivity, precision, repeatability, recovery
    - role:
      - inhibitor, antagonist, catalyst, receptor
      - synergy, cooperative, coordinating, enhancing, activating
      - neutralizing, counteracting, disabling, deactivating, anti
    - process:
      - apoptosis
      - glucolysis
      - transcription
    - states:
      - active, inactive
      - inflammation
    - bio properties:
      - fragility
      - toxicity
    - chemical compounds:
      - molecules
      - bonds
      - elements
      - charge
      - electrons
      - ions
    - bio compounds 
      - proteins
      - enzymes
      - lipids
      - genes: expression, active
      - blood
    - cell components:
      - mitochondria
      - nucleus
      - dna
      - membrane
    - microorganisms:
      - bacteria
      - fungi
      - virus
    - tissue:
      - muscle
      - mucus membrane
      - collagen
    - organs: 
      - liver: synoyms (hepatic), components (hepatocytes)
      - kidney
      - bladder
    - systems:
      - lymph
      - nervous
      - immune
      - circulatory
      - digestive
    - treatments
    - conditions: anything ending in -a is usually a condition
    - tests: pcr
    - metric: levels, quantitative, concentration
'''

verification_dict = {}
output_dict = {}

def test_similarity(verification_dict, output_dict):
  '''
  1. check for coverage of verification_dict 
  2. check for errors (missing components, words that are too different to be correct)
  '''

def get_sub_components(condition_keyword):
  ''' when searching for research on a compound or condition, also check for its sub-components, 
      and the compounds its sub-components can be used to make '''

def get_generic_medication(brand_name):
    import wikipedia
    from wikipedia.exceptions import DisambiguationError
    keyword = None
    original_content = None
    generic_content = None
    try:
        original_content = wikipedia.page(brand_name).content
    except Exception as e:
        print(e)
        for item in e:
            if brand_name.lower() not in item.lower() and 'medica' in item.lower():
                keyword = item
    try:
        generic_page = wikipedia.page(item)
        generic_title = generic_page.title
        generic_content = generic_page.content
        for i, s in enumerate(content.split('\n')):
            if '==' in s and '.' not in s:
                sname = s.replace('=','').strip().replace(' ','_').lower()
                if sname in all_vars['section_map']:
                    return generic_title
        if 'a medication' in generic_content:
            return generic_title
    except Exception as e:
        print('keyword e', keyword, e)
    return False

def get_synthesis_instructions(article):
    '''
    - also add an 'instructions' & 'equipment' item to reduce a study:
      https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4507162/

      to the set of instructions to synthesize the compound:
        - A: mix (((cop_oil & amb) dissolved in dmac) + (C dissolved in ethanol)) for 30 minutes & evaporate for 6 hours in a rotary evaporator 
        - B: dissolve D in double distilled water
        - add A to B one drop at a time while stirring
        - homogenize using a microfluidizer

      and the set of equipment necessary:
        - beakers
        - dropper
        - --heater rotary-evaporator--
        - --homogenizer micro-fluidizer--

      any compounds necessary:
        - cop_oil, amb, dmac, ethanol, double distilled water, TPGS, soya lecithin

      any optional substitutes:
        C: (co-surfactants): soya lecithin (PC), span 80, propylene glycol     
        D: (surfactants): tween 80, labrasol, d-α-tocopheryl polyethylene glycol 1000 succinate (TPGS), pluronic F-68, pluronic F-127

      any parameters & parameter values:
        - isotropic mixture (1:1) of TPGS and PC
        - Cop, drug to Cop ratio 1:20
        - homogenization parameters 15 cycles at 50 MPa of microfluidizer
    '''
    return article

def get_adjacent_compounds(compound):
    return compound

def get_primary_condition(article, index):
    '''
    get the primary condition being studied
    which should be the keyword passed to get_summary_data
    if it was a condition
    or the subject of the study
    '''
    return article 

def get_metrics(line):
    '''
    find any metrics in this line
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information
    '''
    metrics = set()
    split_line = line.split(' ')
    for i, word in enumerate(split_line):
        numbers = [w for w in word if w.isnumeric()]
        if len(numbers) > 0:
            if len(numbers) == len(word):
                next_word = split_line[i + 1]
                if len(next_word) < 5:
                    # to do: add extra processing rather than assuming its a unit of measurement
                    metrics.add(word)
                    metrics.add(next_word) # '3 mg'
            else:
                metrics.add(word) # '3mg'
    return metrics

def get_side_effects(line):
    '''
    this should pull from data in standard sites like wiki, drugs, webmd, & rxlist 
    as well as forum data to find rare symptoms & interactions not listed elsewhere
    '''
    return line

def get_compounds(line):
    ''' - add regex for numerically indexed prefixes like 14alpha-'''
    return line

def get_symptoms(line):
    return line

def get_mechanisms(line):
    ''' get specific process explaining how this compound works '''
    return line

def get_tests(line):
    return line

def get_related_components(component):
    '''
    this should return all primary sub-components & outputs known for the component,
    such as important adjacent compounds which this one frequently turns into
    or other variations of the compound which have very different functionality
    '''
    return component

def get_treatments(intent, hypothesis, line, title, row, metadata, all_vars):
    '''
    hypothesis & intent can be Null for now 

    this function will process a relationship like:

    intent='check_correlation', line="this protein activates this gene known to cause this condition"

    the line must have these conditions met before it should be analyzed as a treatment:
        - check if it has words similar to the title to indicate relevance to study intent 
        - then check that the objects are in the names or medical objects indexes
        - the condition being studied or a marker of it is mentioned as well

    then it analyzes the positivity of the relationship between objects in the line,
     & tests if this is a positive association for the condition, so it can be used as a treatment:

        - returns "positive" for line above to indicate a potential treatment
        - returns "positive" for "this compound had a synergistic effect with a drug to treat the condition"
        - returns "negative" for "this compound reduced disease inhibition"

    - "intents" are similar to "effects" or "outputs", but assumed to be the purpose of an operation once known
    
    when you have intent & hypothesis functions done, you can do logic like:
    if the intent is check_correlation:
        if the hypothesis is "drug reduced blood pressure":
            if the sentence is:
                "drug did not reduce blood pressure" => negative correlation (failure) or a negative intent (reduce)
            if the sentence is:
                "drug did reduce blood pressure" => positive correlation (success) or a negative intent (reduce)
    '''

    blob = get_blob(line)
    sentiment = blob.sentiment if blob else None
    print("\tline sentiment", sentiment, "line", line)
    if hypothesis:
        hypothesis_blob = get_blob(hypothesis)
        hypothesis_sentiment = hypothesis_blob.sentiment if hypothesis_blob else None
        print("\thypothesis sentiment", hypothesis_sentiment, "hypothesis", hypothesis)
    if intent:
        intent_blob = get_blob(intent)
        intent_sentiment = intent_blob.sentiment if intent_blob else None
        print("\tintent sentiment", intent_sentiment, "intent", intent)

    ''' to do: do study & sentence intent matching '''
    derived_relationships = get_relationships_from_clauses(row['clauses'], line, row['nouns'], all_vars)
    if derived_relationships:
        for r in derived_relationships:
            ''' row['variables'] = get_dependencies('inputs', line, row['relationships'], 1)) '''
            intent = None
            correlation = get_correlation_of_relationship(intent, r)
            print('\tget_treatments: correlation', correlation, r)
            if correlation > 0.3:
                row['treatments_successful'].add(r)
            else:
                row['treatments_failed'].add(r)
    return row
from get_structural_objects import *

''' 
  each main medical object has its own property set, which can be built with rows data:
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

Side effect keywords to use to test relationships derived with nlp tools:
  - nouns: effect, activation, activity, reaction, process, role
  - roles: intrinsically related to functions, intents, strategies, & mechanisms
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

def get_object_similarity(verification_dict, output_dict):
  '''
  1. check for coverage of verification_dict 
  2. check for errors (missing components, words that are too different to be correct)
  '''

def get_generic_medication(brand_name):
    '''
      to do:
        - add standardization of acronyms using search with keywords 
          so you get n-acetylaspartic acid from naa and creatine from cr
    '''
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
                sname = s.replace('=', '').strip().replace(' ', '_').lower()
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

def get_primary_condition(article, index):
    '''
      to do:
        - find the primary condition being studied to differentiate 
          from other conditions or complications mentioned 
          which should be the keyword passed to get_summary_data if it was a condition query 
          or one of the subjects of the study
    '''
    return article 

def get_side_effects(line):
    '''
    this should pull from data in standard sites like wiki, drugs, webmd, & rxlist 
    as well as forum data to find rare symptoms & interactions not listed elsewhere
    side_effects = unintended symptoms caused by a drug
    '''
    return line

def get_compounds(line):
    ''' - add regex for numerically indexed prefixes like 14alpha-'''
    return line

def get_symptoms(line):
    ''' pulls from sources specific to symptoms: rxlist, drugs, wiki, forums '''
    ''' symptom examples: fever red urine skin rash paralysis headache bleeding '''
    return line

def get_mechanisms(line):
    '''
    get specific process explaining how this compound works
    uses descriptive language, detailing the process, so present tense verbs like 'works'
    if its a new discovery in an experiment it might be 'x was observed to work'
    '''
    return line

def get_tests(line):
    return line

def get_adjacents(compound):
    ''' 
    get similar compounds with similar functionality 
    that can be synthesized with accessible methods 
    '''
    return compound

def get_sub_components(condition_keyword):
  ''' when searching for research on a compound or condition, also check for its sub-components, 
      and the compounds its sub-components can be used to make '''

def get_related_components(component, data_store, all_vars):
    '''
    this should return all primary sub-components & outputs known for the component,
    such as important adjacent compounds which this one frequently turns into
    or other variations of the compound which have very different functionality
    & pull components of a compound & primary metabolites

    this should only pull the dependencies that are components 
      components meaning interaction objects rather than functions or attributes
    '''
    related_components = set()
    ''' 
    to do: add logic to pull functions
    if not already in index or local_database & get related components from functions
    '''
    definitions = get_definitions(word)
    if definitions:
        for d in definitions:
            d_row = get_pos_metadata(d, None, all_vars)
            if d_row:
                if 'nouns' in d_row:
                    for n in d_row['nouns']:
                        related_components.add(n)
    return related_components

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
            correlation = get_similarity(intent, r)
            print('\tget_treatments: correlation', correlation, r)
            if correlation > 0.3:
                row['treatments_successful'].add(r)
            else:
                row['treatments_failed'].add(r)
    return row

def filter_source_list(object_type, sources):
  ''' 
    filter sources by target object bc some sources are irrelevant to some intents
    apply other filters based on query intent:
      - if they want treatments or synthesis instructions,
        add 'store' sources so you can return links to purchase products
      - if they want a prediction, query code sources for ML functions
      - if the treatment involves an organism (like a type of bacteria), 
          synthesis instructions may involve:
          - collecting samples in the wild
          - predicting phase structure
      - if they want condition data, you need to return phases & timeline
        - if they submit symptoms with a condition query, tell them what phase theyre at
      - if the results are not sufficient, offer option to generate a predictor & estimate cost
      - if a known treatment doesnt exist, your generator needs to return results like:
        - how to modify the problem to be more solvable
          - how to modify treatments to apply to the problem (mutation strategies)
          - how to trigger genes to switch off a process
          - how to make an organism evolve a particular function
  '''
  all_sources = ['rxlist', 'drugs', 'wiki', 'forums', 'pubchem', 'code', 'store', 'generator']
  source_filters = {
    'symptoms': ['rxlist', 'drugs', 'wiki', 'forums', 'pubchem', 'generator'],
    'treatments': ['pubchem', 'wiki', 'rxlist', 'drugs','store', 'generator'],
    'compounds': ['rxlist', 'drugs', 'wiki', 'pubchem', 'store', 'generator'],
    'synthesis_instructions': ['rxlist', 'drugs', 'wiki', 'pubchem', 'store', 'generator'],
    'components': ['rxlist', 'drugs', 'wiki', 'pubchem', 'generator'],
    'conditions': ['wiki', 'pubchem', 'rxlist', 'drugs', 'generator'],
    'organisms': ['wiki', 'pubchem', 'rxlist', 'drugs', 'store', 'generator']
  }
  return sources
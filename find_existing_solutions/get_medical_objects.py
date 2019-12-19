from get_structural_objects import *

def find_object_similarity(verification_dict, output_dict):
  '''
  1. check for coverage of verification_dict 
  2. check for errors (missing components, words that are too different to be correct)
  '''
  return False

def find_metric(pattern, matches, row, all_vars):
    '''
    find any metrics in this pattern's matches
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information
    '''
    metrics = set()
    split_line = pattern.split(' ') if pattern is not None else []
    for i, word in enumerate(split_line):
        numbers = [w for w in word if w.isnumeric()]
        if len(numbers) > 0:
            if len(numbers) == len(word):
                next_word = split_line[i + 1] if (i + 1) < len(split_line) else ''
                if len(next_word) < 5:
                    # to do: add extra processing rather than assuming its a unit of measurement
                    metrics.add(word)
                    metrics.add(next_word) # '3 mg'
            else:
                metrics.add(word) # '3mg'
    return row

def get_common_property(objects, patterns, metadata):
    ''' 
      for requested metadata="treatment", 
      get properties related to successful treatments 
      & do extra searches for those properties as well

      property types:
        - general properties like 'symmetric'
        - topic-related properties like 'hepatoprotective'
        - object-related properties like 'has chemical sub-structure= "hydrogen group" or "benzene cycle"'

      so when youre identifying objects, once you have some objects indexed, 
      go through their properties and do extra searches on the common properties to find 'potential matches'
      in addition to 'known matches'

    '''
    return False

def find_generic_medication(pattern, matches, row, all_vars):
    '''
      to do:
        - add standardization of acronyms using search with keywords 
          so you get n-acetylaspartic acid from naa and creatine from cr
        - also add reverse function to get all possible names of a substance or species to maximize results
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

def find_synthesis(pattern, matches, row, all_vars):
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
    return row

def find_stressor(pattern, matches, row, all_vars):
    '''
    - example of stressor response:
    - when drug handles a function, bio system component shrinks:
      - Researchers measured the volume of the hypothalamus in each scan. 
      This cone-shaped part of the brain has a number of jobs including controlling the release of hormones and regulating reproductive functions.
    - find example of the opposite relationship
    '''
    return row

def find_primary_condition(pattern, matches, row, all_vars):
    '''
      to do:
        - find the primary condition being studied to differentiate 
          from other conditions or complications mentioned 
          which should be the keyword passed to get_summary_data if it was a condition query 
          or one of the subjects of the study
    '''
    return row 

def find_side_effect(pattern, matches, row, all_vars):
    '''
    this should pull from data in standard sites like wiki, drugs, webmd, & rxlist 
    as well as forum data to find rare symptoms & interactions not listed elsewhere
    side_effects = unintended symptoms caused by a drug
    '''
    return row

def find_compound(pattern, matches, row, all_vars):
    ''' - add regex for numerically indexed prefixes like 14alpha-'''
    return row

def find_symptom(pattern, matches, row, all_vars):
    ''' pulls from sources specific to symptoms: rxlist, drugs, wiki, forums '''
    ''' symptom examples: fever red urine skin rash paralysis headache bleeding '''
    return row

def find_mechanism(pattern, matches, row, all_vars):
    '''
    get specific process explaining how this compound works
    uses descriptive language, detailing the process, so present tense verbs like 'works'
    if its a new discovery in an experiment it might be 'x was observed to work'
    '''
    return row

def find_test(pattern, matches, row, all_vars):
    return row

def find_adjacent(pattern, matches, row, all_vars):
    ''' 
    get similar compounds with similar functionality 
    that can be synthesized with accessible methods 
    '''
    return row

def find_sub_component(pattern, matches, row, all_vars):
    ''' when searching for research on a compound or condition, also check for its sub-components, 
      and the compounds its sub-components can be used to make '''
    return row

def find_related_component(pattern, matches, row, all_vars):
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
    to do: add logic to pull functions, relationships, clauses, phrases, & modifiers
    if not already in index or local_database & get related components from functions
    '''
    definitions = get_definitions(word)
    if definitions:
        for d in definitions:
            d_row = get_structural_metadata(d, all_vars)
            if d_row:
                if 'noun' in d_row:
                    for n in d_row['noun']:
                        related_components.add(n)
    return row

def find_treatment(pattern, matches, row, all_vars):
    '''
    hypothesis & intent can be Null for now 

    this function will process a relationship like:

    intent='check_correlation', row="this protein activates this gene known to cause this condition"

    the row must have these conditions met before it should be analyzed as a treatment:
        - check if it has words similar to the title to indicate relevance to study intent 
        - then check that the objects are in the names or medical objects indexes
        - the condition being studied or a marker of it is mentioned as well

    then it analyzes the positivity of the relationship between objects in the row,
     & tests if this is a positive association for the condition, so it can be used as a treatment:

        - returns "positive" for row above to indicate a potential treatment
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

    blob = get_blob(row['line'])
    sentiment = blob.sentiment if blob else None
    print("\trow sentiment", sentiment, "row", row['line'])
    '''
    if hypothesis:
        hypothesis_blob = get_blob(hypothesis)
        hypothesis_sentiment = hypothesis_blob.sentiment if hypothesis_blob else None
        print("\thypothesis sentiment", hypothesis_sentiment, "hypothesis", hypothesis)
    if intent:
        intent_blob = get_blob(intent)
        intent_sentiment = intent_blob.sentiment if intent_blob else None
        print("\tintent sentiment", intent_sentiment, "intent", intent)
    '''
    ''' to do: do study & sentence intent matching '''
    if 'relationships' in row:
        for r in row['relationships']:
            ''' row['variables'] = get_dependencies('inputs', row['line'], row['relationships'], 1)) '''
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
      - if they want condition data, you need to return phases & timerow
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
    'symptom': ['rxlist', 'drugs', 'wiki', 'forums', 'pubchem', 'generator'],
    'treatment': ['pubchem', 'wiki', 'rxlist', 'drugs','store', 'generator'],
    'compound': ['rxlist', 'drugs', 'wiki', 'pubchem', 'store', 'generator'],
    'synthesis': ['rxlist', 'drugs', 'wiki', 'pubchem', 'store', 'generator'],
    'component': ['rxlist', 'drugs', 'wiki', 'pubchem', 'generator'],
    'condition': ['wiki', 'pubchem', 'rxlist', 'drugs', 'generator'],
    'organism': ['wiki', 'pubchem', 'rxlist', 'drugs', 'store', 'generator']
  }
  return sources
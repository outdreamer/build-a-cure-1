import wikipedia
from wikipedia.exceptions import DisambiguationError
from get_vars import *

def find_object_similarity(verification_dict, output_dict):
  '''
  1. check for coverage of verification_dict 
  2. check for errors (missing components, words that are too different to be correct)
  '''
  return False

def find_dose(subset, row, av):
  '''
  - examples:
    "Start small with three to four drops a day and gradually increasing it as your body adjusts to the right treatment dosage."
    "If you are taking oil of oregano in capsules, you should not consume more than 500 to 600 mg per day"
  '''

def find_metric(subset, row, av):
    '''
    find any metrics in this pattern's matches
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information

    examples:
    - minimum inhibitory concentration MIC
    - naa-to-cr ratio

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

def find_generic_medication(subset, row, av):
    '''
      to do:
        - add standardization of acronyms using search with keywords 
          so you get n-acetylaspartic acid from naa and creatine from cr
        - also add reverse function to get all possible names of a substance or species to maximize results
    '''
    keyword = None
    original_content = None
    generic_content = None
    '''
    try:
        original_content = wikipedia.page(subset).content
    except Exception as e:
        if e:
            print(e)
            #if subset.lower() not in e.strerror() and 'medica' in e.strerror():
            #    keyword = e.strerror
    try:
        generic_page = wikipedia.page(item)
        generic_title = generic_page.title
        generic_content = generic_page.content
        for i, s in enumerate(content.split('\n')):
            if '==' in s and '.' not in s:
                sname = s.replace('=', '').strip().replace(' ', '_').lower()
                if sname in av['section_map']:
                    return generic_title
        if 'a medication' in generic_content:
            return generic_title
    except Exception as e:
        print('keyword e', keyword, e)
    '''
    return False

def find_synthesis(subset, row, av):
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

def find_stressor(subset, row, av):
    '''
    - example of stressor response:
    - when drug handles a function, bio system component shrinks:
      - Researchers measured the volume of the hypothalamus in each scan. 
      This cone-shaped part of the brain has a number of jobs including controlling the release of hormones and regulating reproductive functions.
    - find example of the opposite relationship

    Sample patterns:
      Sesquiterpenes work as a liver and gland stimulant and contain caryophyllene and valencene. 
      Research from the universities of Berlin and Vienna show increased oxygenation around the pineal and pituitary glands.
      While offering a variety of healing properties, the most important ability of the monoterpenes is that they can reprogram miswritten information in the cellular memory (DNA)
      Terpene Alcohols stimulate the immune system, work as a diuretic and a general tonic.
      Sesquiterpene Alcohols are ulcer-protective (preventative).
      Phenols clean receptor sites of cells so sesquiterpenes can delete faulty information from the cell. They contain high levels of oxygenating molecules and have anioxidant properties.
      Camphor, borneol, and eucalyptol are monoterpene ketones that the available body of evidence suggests may be toxic to the nervous system depending on dosage, while jasmine, fenchone, and isomenthone are considered nontoxic. Ketones aid the removal of mucous, stimulate cell and tissue regeneration, promote the removal of scar tissue, aid digestion, normalize inflammation, relieve pain, reduce fever, may inhibit coagulation of blood, and encourage relaxation.
      https://www.homasy.com/blogs/tutorials/what-are-the-major-compounds-of-essential-oils
      Furthermore, histidine can protect the body from radiation damage. It does this by binding to the damaging molecules, therefore eliminating them.

    '''
    return row

def find_primary_condition(subset, row, av):
    '''
      to do:
        - find the primary condition being studied to differentiate 
          from other conditions or complications mentioned 
          which should be the keyword passed to get_summary_data if it was a condition query 
          or one of the subjects of the study
    '''
    return row 

def find_side_effect(subset, row, av):
    '''
    this should pull from data in standard sites like wiki, drugs, webmd, & rxlist 
    as well as forum data to find rare symptoms & interactions not listed elsewhere
    side_effects = unintended symptoms caused by a drug
    '''
    return row

def find_compound(subset, row, av):
    ''' - add regex for numerically indexed prefixes like 14alpha-'''
    return row

def find_symptom(subset, row, av):
    ''' pulls from sources specific to symptoms: rxlist, drugs, wiki, forums '''
    ''' symptom examples: fever red urine skin rash paralysis headache bleeding '''
    return row

def find_mechanism(subset, row, av):
    '''
    get specific process explaining how this compound works
    uses descriptive language, detailing the process, so present tense verbs like 'works'
    if its a new discovery in an experiment it might be 'x was observed to work'

    - best description of mechanism of action was on a category page: https://en.wikipedia.org/wiki/Fungistatics

    '''
    return row

def find_test(subset, row, av):
    return row

def find_adjacent(subset, row, av):
    ''' 
    get similar compounds with similar functionality 
    that can be synthesized with accessible methods 
    '''
    return row

def find_sub_component(subset, row, av):
    ''' 
      - when searching for research on a compound or condition, also check for its sub-components, 
        and the compounds its sub-components can be used to make 
      - queries for a bio-system component should also produce what symptoms 
        can occur if its missing or in excess & what conditions are related
    '''
    return row

def find_related_component(subset, row, av):
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
    definition = get_definitions(word)
    if definition:
        d_row = get_structural_metadata(definition, av)
        if d_row:
            if 'noun' in d_row:
                for n in d_row['noun']:
                    related_components.add(n)
    return row

def find_drug(subset, row, av):
    '''
    - new drugs are at: https://adisinsight.springer.com/drugs/800042427
    '''
    return row

def find_treatment(subset, row, av):
    '''

    - organization of analysis:

      1. condition
        - symptoms

      2. condition metric extreme value 
        - symptoms

      3. strategy:
        - impact on metrics of condition

      4. strategy:
        - impact on symptoms

      5. strategy:
        - impact on condition

    - you can use combinations to create trajectories
        - combine 1 (condition:symptom relationship) & 4 (strategy:symptom relationship) to programatically create trajectory between strategy & impact on condition

    - you can also automate identifying intersections, vertexes, layers, & phase shifts to avoid combinations that will damage the system

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

    - https://en.wikipedia.org/wiki/Hyperlipidemia has the word 'estrogens' as a cause, which could mean a side effect of birth control or phytoestrogens or substances that mimic estrogens
    '''

    ''' to do:
      - add query to other compounds on wiki category templates
      - add query to nih
      - add query to identify mechanisms & search for other compounds with those mechanism
      - add query to identify structure & search for other compounds with similar structure
      - add query to fetch complications & treatments for those, similar to side effects query
    '''

    polarity = get_polarity(row['line'])
    print("\tline polarity", polarity, "row", row['line'])
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
            relation_polarity = get_polarity(row['line'])
            print("\trelation sentiment", relation_polarity, "row", row['line'])
            correlation = get_similarity(intent, r, av)
            print('\tget_treatments: correlation', correlation, r)
            if correlation > 0.3:
                row['treatments_successful'].add(r)
            else:
                row['treatments_failed'].add(r)
    return row

def add_related_metadata(object_type, av):
    if object_type in av['related_metadata']:
        object_list = av['related_metadata'][object_type]
        object_list.extend(av['default_objects'])
        return object_list
    return False

def filter_source_list(object_type):
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
  all_sources = ['rxlist', 'drugs', 'wiki', 'forums', 'pubchem' ] # 'code', 'store', 'generator'
  source_filters = {
    'symptom': ['rxlist', 'drugs', 'wiki', 'forums', 'pubchem'],
    'treatment': ['pubchem', 'wiki', 'rxlist', 'drugs'],
    'compound': ['rxlist', 'drugs', 'wiki', 'pubchem'],
    'synthesis': ['rxlist', 'drugs', 'wiki', 'pubchem'],
    'component': ['rxlist', 'drugs', 'wiki', 'pubchem'],
    'condition': ['wiki', 'pubchem', 'rxlist', 'drugs'],
    'organism': ['wiki', 'pubchem', 'rxlist', 'drugs']
  }
  if object_type in source_filters:
    return source_filters[object_type]
  return sources
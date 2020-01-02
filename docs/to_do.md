# Summary

- now youve built some powerful functions, some of which need completion, debugging & generalization
    - the important next step is hooking up clause/relationship identification to those functions
    - since those are the foundation for the other more important semantic functions in get_medical_objects and get_conceptual_objects
    - key requirements to complete next:
      - find_type
      - consolidate get_all_versions output
      - consolidate pattern identification functions
      - test & update find_clause/relation logic
      - test & update derive patterns logic to build a full pattern index to implement with clause/relation logic

- the relationships between object type layers (structural, conceptual, medical) means that you can re-use logic across layers:
    - example:
      - stressor identification logic can overlap with change/variance/variable identification logic
    - other type mappings to generalize:
      condition = state, symptom = function = side_effects, function = relationship, synthesis = build process, structure = pattern
    - at some point you need to identify this system of relationships between object types & layers 
      so that generation of additional layer interfaces is possible (physics system, math system, chemical system, in addition to medical/bio system)

# Sources

  - check chembl search if you can search for a condition & return molecules known to treat it
  - chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
  - index articles you pull from sources so youre not repeating the query & store it across requests
  - resolve local_database, get_data_store, derive_pattern, get_data_from_source logic & calls
  - add wiki & drugs & nih api calls to sources & adjust api support for those data sources in get_data_source/build_indexes

# Data 
  - pull these properties for compounds on wiki
  - find source of bio keywords & synonyms

# Structural Objects

  - adjust metadata with map to related objects for requested metadata
  - do full synonym check vs definition check at beginning with get_all_versions - generate_synonym_patterns

  find functions:
  - finish find_type
  - add if original_row != row: to all find_* functions
  - find functions should have logic to rule out other types & type-specific logic since they're used as a backup to pattern-matching
  - in find_clause, for question sentence_types, standardize verb-subject to subject-verb: 'V DET noun_phrase ... ?' => 'DET noun_phrase V ...'
  - finish function to combine functions by intent get_net_impact(functions) & combined operators

  pattern alts:
  - in list b***in list b, = ADV V |V N| in output patterns
  - repeated options shouldnt happen within an alt set: |NNS NNS VBZ2 VBZ3 NNS| 
  - randomly assigned indexes: |suppose thought1 assumed| that3 DPC |suppose thought6 assumed| that8 ALL_N9 ALL_N10 ALL_N11
  - consolidate output of index_type patterns like 'modifier clause'

  - examine iterations (lists/if conditions) that determine processing order: 
    (supported_pattern_variables, pos_tags, all_pattern_version_types, reversed keys, etc)
    - add ordered pos-tagging pattern_map to apply preference order to correct incorrectly identified word pos - isolate which tags would be identified as other objects first

  - add ordering logic in find_clause for special clause keywords:
    - 'as' can mean 'like', 'while', or 'because'
    - 'by' can indicate a process/mechanism "it works by doing x", "as"

  - support conversion between pos types like 'verb-to-noun':
    - 'subject1 verb clause because subject2 verb clause' => 'subject2 verb-to-noun causes subject1 verb-to-noun'
    - 'the process activated x because y inhibits b' => 'y b-inhibition causes the process to activate x' => 'y b-inhibition enables process to activate x'

  - fix rows csv format & read/save delimiter handling for get_objects - we are storing patterns with 'pattern_match1::match2::match3' syntax for example
  - write function to get semantic props of compounds (bio-availability, activation in the host species, etc) & get_common_property between objects
  - integrate conditions/symptoms and treatments/compounds schemas (this would be a nice way to test get_attribute function to find differentiating props)
  - remove len(0) checks for lists when possible & consolidate excessive chained response checks
  - make sure youre not assigning scores or other calculated numbers as dict keys or other identifiers anywhere 

# Functions

  - add variable accretion patterns (how an object becomes influenced by a new variable)
  - add get_common_properties function to do extra property-based searches after identifying objects with extract
  - write function to identify contradictory information (retracted studies, false information, conspiracy theory (anti-vax), opinion) & selecting least likely to be false
    - this will be useful when youre pulling non-research study data, like when youre looking up a metric or compound if you dont find anything on wiki
  - write function to identify authoritative sources (wiki is more trustworthy than a holistic or commercialized blog based on editing metadata)
  - in order to implement this without ml, you need functions to identify conceptual metadata of a compound or organism, so at least these to get started:
    - add identification functions:
        - types (['structure', 'life form', 'organic molecule'] from 'protein')
        - get_topic
        - objects (nouns like 'protein')
        - components (topical nouns that are found in another topical component, like organelles of a cell)
        - attributes (attribute metric/feature nouns like 'toxicity')
        - functions (verbs like 'ionizing', 'activate', inputs/outputs like subject/predicate nouns)
        - variables (function inputs like subject/modifier nouns)
        - test on bio systems:
          - "adjacency as a definition of relevance can be used as a way to derive paths" + "path optimization can be used to get a drug to a location in the system"
          - "isolate a pathogen cell before destroying it so it cant communicate info about what destroyed it to other pathogens to help them evolve resistance"
    - functions to determine:
      - position/role in a system 
      - function type associated with its core functions (change rules, boundary rules)
      - emergent effects in edge cases, rule change states, & interacting with other system layers
      - solution via conceptual route
  - write a function to derive core component functions for any system - then you can write functions to:
      - determine equivalent functions or more optimal version of a function
      - determine function intent
      - alter core functions used to alter function intent
      - when generating solutions, change core functions to vary to describe any function set that builds any other function set in a system
        - set of binding/interaction/priority functions for element atoms
  - add function to test chemical reactions: https://cheminfo.github.io/openchemlib-js/docs/classes/reaction.html
  - add keyword processing to apply_find_function 
  - fill in keywords & patterns for objects (strategies/mechanisms used by an organism/on a compound)
  - function to predict a compound for a pathogen/condition requires data:
    - compound & pathogen attributes (compound metadata like metabolism/dose/interactions/effects)
    - variable/state impact (gene expression)
    - interaction rules with expected object types (in the bloodstream if taken orally, in the lungs if inhaled)
    - sub-components that could be altered through interaction to neutralize its functionality
    - dependency scope (volume of layers of relevance)

# Conceptual
  - function to identify & remove common article intents with high probability of falsehood to reduce it to just facts
  - add intent matching so you can compare treatment relationships with article intents to see if its actually a sentence with a treatment in it
    - finish treatment failure condition - make sure it adds nothing if theres no treatment in the article - this is related to intent function
  - use distortion patterns of entities like atlases, templates, solution progressions to form a compressed version of the host system
    https://techxplore.com/news/2019-11-medical-image-analysis.html
  - add stressor language patterns
  - for queries of functions like "disable a gene", you can include intent & function metadata to point to sets of compounds that could do the required edits:
    - find compound (protein, enzyme, etc) that unfolds DNA
    - find compound that modifies (edits, activates, removes) the gene once unfolded as specifically as possible 
      (can be a compound with a cutting subcomponent at the right length to target the dna if you can bind it to the first or last gene with another compound)
    - find compound with function = "refolds DNA"
    https://medicalxpress.com/news/2019-12-common-insulin-pathway-cancer-diabetes.html

# Questions
  - are pathogen receptors/membranes unique enough that you could design a substance to artificially bind with them to deactivate or puncture the membrane without impacting other structures?

# ML
  - the full data set should have numerical categories indicating condition(s) treated in the output label so it can be separated into sub-sets by condition treated
  - incorporate stacked autoencoders to leverage unsupervised learning to get initial weights
  - incorporate cosine loss rather than categorical cross entropy
  - add recurrent nn example code that can be copied & plugged in without modification

# Generating Data Set from Smile Formula

  - you could also check the reaction with chemlib's reaction product tool another way you could encode it is by using the # of electrons in the first atom in each pair as the x value, and # of electrons in the second atom as the y value (optionally including the bond type as z value by strength" & graphing it, then deriving the function for each cluster of points using standard math do chemical compounds with similar formulas calculated in this way share properties? this implies the side of each bond has embedded meaning since youre grouping them: 'all the right-side values are x', 'all the left-side values are y'should you repeat the values to erase this bias? like h2o would be represented as pairs: [ho], [oh] rather than [ho] and [h, Null]

  - the meaning is the relationship between bonded elements, as well as the sequence between groups of bonded elements so I think its legit how do you preserve sequence order in that situation? do you assign an ordinal variable to each pair, so your data set is: 1,h,o,bondtype, 2,h,o,bondtype and you have 4 dimensions to graph instead of 3? once you have the function, each chemical can be represented by its coefficients

  - if you have a function to calculate/predict bond strength between two atoms given their identity & electron count, that could be useful data as well, beyond the bond order

# Generating Data Sets from Combinining Data for Component Names

  - analyze which components these disease & evolved genes/traits have in common & which system attributes are influenced
    and try to predict diseases & evolved genes/traits from new component sets & newly enabled interactions with existing components
    & find an optimal set for health (extra processing organs, more diverse microbiome, etc)
    https://medicalxpress.com/news/2019-11-humans-co-evolved-immune-related-diseasesand.html

  - generate multiple datasets:
    - smile + each medical component (side effects, functions, symptoms) to get a predictor formula for that component from the smile formula
    - really you should iterate through all combinations of components and generate a dataset for each one to check for relationships
    - data set of just props in case there is a relationship between successful treatment & one of the properties available (need a chemical with property x value y)

  - now that you have a smile formula generator, you have the raw structure data, 
    assuming you can usually generate the right formula from a sequence of electron counts, which may not be realistic but youll at least have sets of elements to look in
  - so its time to focus on metadata - aggregate a property set available from apis, find the most comprehensive one, & use that api to fill in structural metadata
  - then you can finish the conceptual metadata functions to pull treatments, symptoms, conditions, sub_components(atoms, ions, circles), related_components (genes, proteins), mechanisms of action (rules/functions)
    (plus abstract metadata like intents, priorities, strategies, & insights)
  - figure out how to represent conceptual metadata as numbers in case you want to train on it, you may have to rely on mappings & encoding but some have clear value functions
    if there are a thousand strategies, id rather store encoded first node, encoded function, encoded last node, 
    which will involve less if there are 10 of each (30 features as opposed to 1000)
    but if strategies have more than 2 nodes (if you cant reduce them further), then itll get big quickly & you wont be able to store all the metadata in one dataset

  - then you can create a script to generate & deploy a bunch of models as web services
    you can write a cost estimator function to generate a cost as part of the output for the patient

  - should build a UI at some point but csv's should be fine for now, since its reducing the data a lot,
   and most people will just use it for fetching known treatments that have been tried or a likely condition for their symptoms

  - once youre done with that, you can move on to more complex compounds like organisms & integrate some more interesting analysis

# Diagrams

- make diagram for variable accretion patterns
- finish diagrams for specific concepts, core functions, and concept operations
- finish informal fallacy diagrams: https://en.wikipedia.org/wiki/List_of_fallacies
- consider using dimensionality reduction as a way to identify abstract patterns & functions to explain common deviations from patterns
    https://miro.medium.com/max/1659/1*nQrZmfQE3zmMnCJLb_MNpQ.png
    https://towardsdatascience.com/step-by-step-signal-processing-with-machine-learning-pca-ica-nmf-8de2f375c422
- use this or similar as example when describing current state of problem solving: 
    https://miro.medium.com/max/462/1*X7dQgs1gsJ0Sktz3t7J21Q.png
    https://towardsdatascience.com/feature-extraction-techniques-d619b56e31be

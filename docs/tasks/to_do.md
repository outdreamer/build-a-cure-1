# Summary

- now youve built some powerful functions, some of which need completion, debugging & generalization
    - the important next step is hooking up clause/relationship identification to those functions
    - since those are the foundation for the other more important semantic functions in get_medical_objects and get_conceptual_objects
    - key requirements to complete next:
      - find_type
      - find_definition - can pull from dataset for a type to build definition
      - consolidate pattern identification functions
      - test & update find_clause/relation logic
      - test & update derive_patterns logic to build a full pattern index to implement with clause/relation logic

- the relationships between object type layers (structural, conceptual, medical) means that you can re-use logic across layers:
    - example:
      - stressor identification logic can overlap with change/variance/variable identification logic
    - other type mappings to generalize:
      condition = state, symptom = function = side_effects, function = relationship, synthesis = build process, structure = pattern
    - at some point you need to identify this system of relationships between object types & layers 
      so that generation of additional layer interfaces is possible (physics system, math system, chemical system, in addition to medical/bio system)

- you can work on other tasks for a while before completing relationship/clause/pattern fitting:
  - insight identifier
  - dose prediction for a patient
  - fetch contraindications for a drug (find nth-degree side effects, outputs, high dose impact if not metabolized, conditions, interacting/synergistic/neutralizing drugs)
  - find most common adjacent compound (to make it likeliest that the person can find the common compound and synthesize the version they need)
  - fetch synthesis instructions for a drug from most common adjacent compound
  - treatment component identification function
  - drug reaction predictor & compound search from smile formula
  - function/directory organization
    - first list & organize functions
    - ideally functionality would be organized by intent folders so permissions could be granted according to intent assessment


# Sources

  - check chembl search if you can search for a condition & return molecules known to treat it
  - chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
  - resolve local_database, get_data_store, derive_pattern, get_data_from_source logic & calls
  - pull these properties for compounds on wiki
  - find source of bio keywords & synonyms


# Pattern Functions

  - fix indexing 'NNP NN NNS1 of JJ JJ JJ2' or postpone to pattern evaluation time
  - fix missing alts
      pattern_index::verb_phrase::plays a |VB NN| role::a NN role
  - fix one-letter alts: pattern_index::phrase_identifier::ALL_N DPC ALL_N |VBG VBD|::N D N V
  - generalize alt logic to use embedded pair finding
  - fix supported stem assignment (endings like 'is': {'functions a', 'acts a', 'plays a', 'operates a', 'works a'})
  - fix charge function ('edit' is assigned positive score)
  - add core clause patterns 
  - fix pattern matching functions
  - finish pos, clause, modifiers code from find implementation
  - get a language map for implementing other tools
  - add conversion of pattern matching options to regex
  - add precomputing if a sub-pattern was already computed: 'ALL_N ALL_N of ALL_N ALL_N' in 'ALL_N ALL_N ALL_N of ALL_N ALL_N ALL_N'
  - add formatting to allow multiple items as keys in json and maintain order for interface network paths
  

# Structural Objects

  - add complications object when querying treatments
  - resolve \n separator when not used as a new line separator
  - store definitions
  - fix conjugation
  - fix return from type_patterns

  - when evaluating interactions, check for other compounds that interfere with metabolism & de/activation (cytochromes it targets, liver enzymes it assists), 
    which can increase or decrease blood ratio of a drug
  - look for processes/intake of nutrients that could combine to form other compounds (berberine) given the output health factors (stable blood sugar)
  - fix order of assembled combinations:
      get_alts: all_alts [['suppose', 'assumed', 'thought'], ['DT', 'PDT', 'WDT', 'TO', 'PP', 'CC', 'IN'], ' that ', ['suppose', 'assumed', 'thought'], ' that']
  - remove plural tags once you finish singularize function
  - make sure apply_pattern_map explores all versions of line, but returns one new line
  - add common patterns that have more than one index type to all index type lists - 'x of y', 'phrase of phrase', etc
  - identify lists in sentence and surround with parenthesis if embedded or insert as examples of an object ('such as', 'like', 'as in'), 'found in', 'including', 'having'
  - find functions should have definition logic & logic to rule out other types & type-specific logic since they're used as a backup to pattern-matching
    the order of find_* function application can take the place of this, if patterns are comprehensive enough
  - add pattern to standardize verb-subject to subject-verb: 'V DET noun_phrase ... ?' => 'DET noun_phrase V ...'
  - finish function to combine functions by intent get_net_impact(functions) & combined operators
  - verify that if not response false check is same as youve been using

  pattern alts:
  - repeated options shouldnt happen within an alt set: |NNS NNS VBZ2 VBZ3 NNS| 
  - implement pattern-mix matching to mix & match patterns of various types to find key patterns with mixed types not generated by current logic

  processing order:
  - examine iterations (lists/keys()/items()/config/if conditions) that determine processing order: (supported_pattern_variables, pos_tags, all_pattern_version_types, reversed keys, etc)
    - when identifying all objects, order can be from low to high
    - when classifying specific objects, order should be from high to low - return first match, or adjust line being analyzed with replacement for each match, starting with longest matches first
    - add ordered pos-tagging pattern_map to apply preference order to correct incorrectly identified word pos - isolate which tags would be identified as other objects first

  clause identification: 
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
  - add keyword processing to apply_find_function 


# Functions

  - function to predict a compound for a pathogen/condition requires data:
      - compound & pathogen attributes (compound metadata like metabolism/dose/interactions/effects)
      - variable/state impact (gene expression)
      - interaction rules with expected object types (in the bloodstream if taken orally, in the lungs if inhaled)
      - sub-components that could be altered through interaction to neutralize its functionality
      - dependency scope (volume of layers of relevance)
  - add get_common_properties function to do extra property-based searches after identifying objects with extract
  - add function to test chemical reactions: https://cheminfo.github.io/openchemlib-js/docs/classes/reaction.html
  - fill in keywords & patterns for objects (strategies/mechanisms used by an organism/on a compound)
  - find situations where systems dont act like objects in a system (despite similarities in object/system behavior like variance/definition gaps)
  - merge finder & builder notes
  - use distortion patterns of entities (like atlases, templates, solution progressions) to form a compressed version of the host system - https://techxplore.com/news/2019-11-medical-image-analysis.html
  - add stressor language patterns
  - for queries of functions like "disable a gene", you can include intent & function metadata to point to sets of compounds that could do the required edits:
    - find compound (protein, enzyme, etc) that unfolds DNA
    - find compound that modifies (edits, activates, removes) the gene once unfolded as specifically as possible 
      (can be a compound with a cutting subcomponent at the right length to target the dna if you can bind it to the first or last gene with another compound)
    - find compound with function = "refolds DNA"
    https://medicalxpress.com/news/2019-12-common-insulin-pathway-cancer-diabetes.html
  - program to identify optimal use cases 
  - program to delegate optimized use cases to tools optimized for them (languages better at one task than another)

# ML
  - the full data set should have numerical categories indicating condition(s) treated in the output label so it can be separated into sub-sets by condition treated
  - incorporate stacked autoencoders to leverage unsupervised learning to get initial weights
  - incorporate cosine loss rather than categorical cross entropy
  - add recurrent nn example code that can be copied & plugged in without modification
  - from a data set, it should be possible to compute which questions can be answered by the data set, with what confidence & specificity - if it matches user intent, you can proceed with the analysis
  - accretion of data set variables into types using info filters is one relationship that occurs on the interface network


# Questions
  - are pathogen receptors/membranes unique enough that you could design a substance to artificially bind with them to deactivate or puncture the membrane without impacting other structures?


# Planned features

  - smart contracts for browser, to grant permissions to various web events/user actions for a particular session
    When you log in, you create a mini contract saying what you intend to do, and if behavior deviates outside of what the contract supports, the session is terminated

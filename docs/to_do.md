# Sources:

- check chembl search if you can search for a condition & return molecules known to treat it
- chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
- index articles you pull from sources so youre not repeating the query & store it across requests
- make sources query specific - symptom queries should pull from drugs/rxlist/forums/wiki

## Data 
  - pull these properties for compounds on wiki:
        Bioavailability 63–89%[4]:73
        Protein binding 10–25%[5]
        Metabolism  Predominantly in the liver[3]
        Metabolites APAP gluc, APAP sulfate, APAP GSH, APAP cys, NAPQI[6]
        Onset of action Pain relief onset by route:
          By mouth – 37 minutes[7]
          Buccal – 15 minutes[7]
          Intravenous – 8 minutes[7]
        Elimination half-life 1–4 hours[3]
        Excretion Urine (85–90%)[3]
  - find source of bio keywords & synonyms

## Structural Objects

  - finish generate_pattern_type_patterns and generate_type_patterns
  - add if original_row != row: to all find_* functions
  - do full synonym check vs definition check at beginning with get_all_versions - generate_synonym_patterns
  - find functions should have logic to rule out other types & type-specific logic since they're used as a backup to pattern-matching

  - in find_clause, for question sentence_types, standardize verb-subject to subject-verb: 'V DET noun_phrase ... ?' => 'DET noun_phrase V ...'
  - finish function to combine functions by intent get_net_impact(functions) & combined operators
  - in list b***in list b, = ADV V |V N|
  - repeated options shouldnt happen within an alt set: |NNS NNS VBZ2 VBZ3 NNS| 
  - randomly assigned indexes: |suppose thought1 assumed| that3 DPC |suppose thought6 assumed| that8 ALL_N9 ALL_N10 ALL_N11

  - pattern processing order: examine iterations (lists/if conditions) that determine processing order: 
    (supported_pattern_variables, pos_tags, all_pattern_version_types, reversed keys, etc)
    - add ordered pos-tagging pattern_map to apply preference order to correct incorrectly identified word pos - isolate which tags would be identified as other objects first

  - add ordering logic in find_clause for special clause keywords:
    - 'as' can mean 'like', 'while', or 'because'
    - 'by' can indicate a process/mechanism "it works by doing x", "as"

  - support conversion between pos types like 'verb-to-noun':
    - 'subject1 verb clause because subject2 verb clause' => 'subject2 verb-to-noun causes subject1 verb-to-noun'
    - 'the process activated x because y inhibits b' => 'y b-inhibition causes the process to activate x' => 'y b-inhibition enables process to activate x'
  - fix rows csv format & read/save delimiter handling for get_objects - we are storing patterns with 'pattern_match1::match2::match3' syntax for example
  - use definitions as a data source for relationships if none are found 
  - write function to get semantic props of compounds (bio-availability, activation in the host species, etc) & get_common_property between objects
  - integrate conditions/symptoms and treatments/compounds schemas (this would be a nice way to test get_attribute function to find differentiating props)

  - remove len(0) checks for lists when possible & consolidate excessive chained response checks
  - make sure youre not assigning scores or other calculated numbers as dict keys or other identifiers anywhere 
  - some of these types have type mappings so generalize when you can: condition = state, symptom = function = side_effects, function = relationship, synthesis = build process, structure = pattern


## Functions
  - add variable accretion patterns (how an object becomes influenced by a new variable)
  - add get_common_properties function to do extra property-based searches after identifying objects with extract
  - add wiki & drugs & nih api calls to sources & api support for those data sources in get_data_source/build_indexes
  - build math logic/plain language translation function - example: https://adventuresinmachinelearning.com/improve-neural-networks-part-1/
  - write function to identify contradictory information (retracted studies, false information, conspiracy theory (anti-vax), opinion) & selecting least likely to be false
    - this will be useful when youre pulling non-research study data, like when youre looking up a metric or compound if you dont find anything on wiki
  - write function to identify authoritative sources (wiki is more trustworthy than a holistic or commercialized blog)
  - in order to implement this without ml, you need functions to identify conceptual metadata of a compound or organism, so at least these to get started:
    - add identification functions:
        - types (['structure', 'life form', 'organic molecule'] from 'protein') - add generate_type_patterns() after get_type
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
  - implementation of idea: "code selection algorithm to select function combinations according to data structure & priority at function stack run time"
    - example:
    - select code that is optimized for fewest lines of code/quickest execution time/data storage usage/state storage/memory usage based on input data structure & variance
      - "if input has variance k, allow for conditions checking for parameters of variance"
        - "if input has types [a, b, c], select conditions checking for corresponding types [a1, b1, c1]"
                  if word_type in a1_type_list:
                    type_a.add(word)
                  elif word_type in b1_type_list:
                    type_b.add(word)
                  elif word_type in c1_type_list:
                    type_c.add(word)
                  else:
                    no_type.add(word)
        - "if input has types [a], organize code so that assignment is done at end of condition set"
                  word_type = None
                  if original_type in type_list:
                    other_type = logic_operation(word, original_type)
                    if other_type:
                      word_type = other_type
                    else:
                      word_type = original_type
                  if word_type:
                    type_a.add(word_type)

Conceptual:
  - function to identify & remove common article intents with high probability of falsehood to reduce it to just facts
  - add intent matching so you can compare treatment relationships with article intents to see if its actually a sentence with a treatment in it
    - finish treatment failure condition - make sure it adds nothing if theres no treatment in the article - this is related to intent function
  - use distortion patterns of entities like atlases, templates, solution progressions to form a compressed version of the host system
    https://techxplore.com/news/2019-11-medical-image-analysis.html
  - add stressor language patterns:
      Sesquiterpenes work as a liver and gland stimulant and contain caryophyllene and valencene. 
      Research from the universities of Berlin and Vienna show increased oxygenation around the pineal and pituitary glands.
      While offering a variety of healing properties, the most important ability of the monoterpenes is that they can reprogram miswritten information in the cellular memory (DNA)
      Terpene Alcohols stimulate the immune system, work as a diuretic and a general tonic.
      Sesquiterpene Alcohols are ulcer-protective (preventative).
      Phenols clean receptor sites of cells so sesquiterpenes can delete faulty information from the cell. They contain high levels of oxygenating molecules and have anioxidant properties.
      Camphor, borneol, and eucalyptol are monoterpene ketones that the available body of evidence suggests may be toxic to the nervous system depending on dosage, while jasmine, fenchone, and isomenthone are considered nontoxic. Ketones aid the removal of mucous, stimulate cell and tissue regeneration, promote the removal of scar tissue, aid digestion, normalize inflammation, relieve pain, reduce fever, may inhibit coagulation of blood, and encourage relaxation.
      https://www.homasy.com/blogs/tutorials/what-are-the-major-compounds-of-essential-oils
      Furthermore, histidine can protect the body from radiation damage. It does this by binding to the damaging molecules, therefore eliminating them.
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
  - consider using dimensionality reduction as a way to identify abstract patterns & functions to explain common deviations from patterns
    https://miro.medium.com/max/1659/1*nQrZmfQE3zmMnCJLb_MNpQ.png
    https://towardsdatascience.com/step-by-step-signal-processing-with-machine-learning-pca-ica-nmf-8de2f375c422
  - use this or similar as example when describing current state of problem solving: 
    https://miro.medium.com/max/462/1*X7dQgs1gsJ0Sktz3t7J21Q.png
    https://towardsdatascience.com/feature-extraction-techniques-d619b56e31be

# Examples:

- synonyms examples:
  biofilm :: membrane
  sympathetic :: synergistic
  irritate :: damage

- metrics function should identify:
  - minimum inhibitory concentration MIC
  - naa-to-cr ratio

- new drugs are at: https://adisinsight.springer.com/drugs/800042427

- best description of mechanism of action was on a category page:
  https://en.wikipedia.org/wiki/Fungistatics

- doses examples:
  "Start small with three to four drops a day and gradually increasing it as your body adjusts to the right treatment dosage."
  "If you are taking oil of oregano in capsules, you should not consume more than 500 to 600 mg per day"

- assumption counterexamples:

  1. "smile formulas are generally under 100 char"
    - wiki for smiles doc has 240-char compound formula: https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system

  2. "structure is a good mechanism for deriving function"
    - bakuchiol has example of structural difference with similar function:
    https://en.wikipedia.org/wiki/Bakuchiol

  3. "wiki articles of related compounds will mention each other"
    - sertraline wiki doesnt mention interaction with fluconazole 
      - youd have to derive by noting that it increased blood level/metabolism of substrates some CYP 450 enzymes inhibited by fluconazole
      - or that it is metabolized by some of the same enzymes
      - https://en.wikipedia.org/wiki/Sertraline#Overdose


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
  - then you can generate combination datasets of:
    supervised data:
      [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, property] # to predict a certain property that a structure has, like activating a particular gene or binding to something
      [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, genes] # to predict which genes will interact with a compound
      [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, mechanism] # to predict which processes will activate/neutralize/bind with a compound
      [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, metabolism] # to predict how a compound will be metabolized
      [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, dose] # to predict a non-toxic dose of a compound
      [structure, structural_metadata, mechanism_of_action_metadata, symptom] # to predict a symptom caused by a structure
      [symptoms, successful_treatment_structure_label] # to predict successful treatment structures for a set of symptoms
      [symptoms, structure, structural_metadata, mechanism_of_action_metadata, success_for_treating_condition_C] # to predict successful treatment structures for a condition given the symptoms indicating the phase
    sequential data:
      [past_conditions, future_conditions] # to predict the conditions a patient will likely develop

  - then you can create a script to generate & deploy a bunch of models as web services
    you can write a cost estimator function to generate a cost as part of the output for the patient

  - should build a UI at some point but csv's should be fine for now, since its reducing the data a lot,
   and most people will just use it for fetching known treatments that have been tried or a likely condition for their symptoms

  - once youre done with that, you can move on to more complex compounds like organisms & integrate some more interesting analysis


# Diagrams

- finish diagrams for specific concepts, core functions, and concept operations
- finish informal fallacy diagrams: https://en.wikipedia.org/wiki/List_of_fallacies
    Argument to moderation (false compromise, middle ground, fallacy of the mean, argumentum ad temperantiam) – assuming that the compromise between two positions is always correct.[16]
    Continuum fallacy (fallacy of the beard, line-drawing fallacy, sorites fallacy, fallacy of the heap, bald man fallacy) – improperly rejecting a claim for being imprecise.[17]
    Suppressed correlative – a correlative is redefined so that one alternative is made impossible.[18]
    Definist fallacy – involves the confusion between two notions by defining one in terms of the other.[19]
    Divine fallacy (argument from incredulity) – arguing that, because something is so incredible or amazing, it must be the result of superior, divine, alien or paranormal agency.[20]
    Double counting – counting events or occurrences more than once in probabilistic reasoning, which leads to the sum of the probabilities of all cases exceeding unity.
    Equivocation – the misleading use of a term with more than one meaning (by glossing over which meaning is intended at a particular time).[21]
        Ambiguous middle term – a common ambiguity in syllogisms in which the middle term is equivocated.[22]
        Definitional retreat – changing the meaning of a word to deal with an objection raised against the original wording.[1]
        Motte-and-bailey fallacy – the arguer conflates two positions with similar properties, one modest and easy to defend (the "motte") and one much more controversial (the "bailey"). The arguer advances the controversial position, but when challenged, they insist that they are only advancing the more modest position.[23][24][25]
        Fallacy of accent – a specific type of ambiguity that arises when the meaning of a sentence is changed by placing an unusual prosodic stress, or when, in a written passage, it is left unclear which word the emphasis was supposed to fall on.
        Persuasive definition – a form of stipulative definition which purports to describe the "true" or "commonly accepted" meaning of a term, while in reality stipulating an uncommon or altered use. (See also the if-by-whiskey fallacy, below)
    Ecological fallacy – inferences about the nature of specific individuals are based solely upon aggregate statistics collected for the group to which those individuals belong.[26]
    Etymological fallacy – reasoning that the original or historical meaning of a word or phrase is necessarily similar to its actual present-day usage.[27]
    Fallacy of composition – assuming that something true of part of a whole must also be true of the whole.[28]
    Fallacy of division – assuming that something true of a thing must also be true of all or some of its parts.[29]
    False attribution – an advocate appeals to an irrelevant, unqualified, unidentified, biased or fabricated source in support of an argument.
    Fallacy of quoting out of context (contextotomy, contextomy; quotation mining) – refers to the selective excerpting of words from their original context in a way that distorts the source's intended meaning.[30]
    False authority (single authority) – using an expert of dubious credentials or using only one opinion to sell a product or idea. Related to the appeal to authority (not always fallacious).
    False dilemma (false dichotomy, fallacy of bifurcation, black-or-white fallacy) – two alternative statements are held to be the only possible options when in reality there are more.[31]
    False equivalence – describing a situation of logical and apparent equivalence, when in fact there is none.
    Feedback fallacy - in the context of performance appraisal, the belief in the accuracy of feedback, despite evidence that feedback is subject to large systematic errors due to the idiosyncratic rater effect.[32]
    Historian's fallacy – the assumption that decision makers of the past viewed events from the same perspective and had the same information as those subsequently analyzing the decision.[33]
    Historical fallacy – a set of considerations is thought to hold good only because a completed process is read into the content of the process which conditions this completed result.[34]
    Homunculus fallacy – a "middle-man" is used for explanation; this sometimes leads to regressive middle-men. Explains without actually explaining the real nature of a function or a process. Instead, it explains the concept in terms of the concept itself, without first defining or explaining the original concept.
    Inflation of conflict – arguing that if experts of a field of knowledge disagree on a certain point, the experts must know nothing, and therefore no conclusion can be reached, or that the legitimacy of their entire field is put to question.[37]
    If-by-whiskey – an argument that supports both sides of an issue by using terms that are selectively emotionally sensitive.
    Incomplete comparison – insufficient information is provided to make a complete comparison.
    Inconsistent comparison – different methods of comparison are used, leaving a false impression of the whole comparison.
    Intentionality fallacy – the insistence that the ultimate meaning of an expression must be consistent with the intention of the person from whom the communication originated (e.g. a work of fiction that is widely received as a blatant allegory must necessarily not be regarded as such if the author intended it not to be so.)[38]
    Ludic fallacy – the belief that the outcomes of non-regulated random occurrences can be encapsulated by a statistic; a failure to take into account that unknown unknowns in determining the probability of events taking place.[39]  - spin, system
    McNamara fallacy (quantitative fallacy) – making a decision based only on quantitative observations, discounting all other considerations.
    Mind projection fallacy – subjective judgments are "projected" to be inherent properties of an object, rather than being related to personal perceptions of that object.
    Moving the goalposts (raising the bar) – argument in which evidence presented in response to a specific claim is dismissed and some other (often greater) evidence is demanded.
    Nirvana fallacy (perfect-solution fallacy) – solutions to problems are rejected because they are not perfect.
    Prosecutor's fallacy – a low probability of false matches does not mean a low probability of some false match being found.
    Proving too much – using a form of argument that, if it were valid, could be used to reach an additional, invalid conclusion.
    Psychologist's fallacy – an observer presupposes the objectivity of their own perspective when analyzing a behavioral event.
    Referential fallacy[40] – assuming all words refer to existing things and that the meaning of words reside within the things they refer to, as opposed to words possibly referring to no real object or that the meaning of words often comes from how they are used.
    Reification (concretism, hypostatization, or the fallacy of misplaced concreteness) – a fallacy of ambiguity, when an abstraction (abstract belief or hypothetical construct) is treated as if it were a concrete, real event or physical entity. 
    Retrospective determinism – the argument that because an event has occurred under some circumstance, the circumstance must have made its occurrence inevitable.
    Special pleading – a proponent of a position attempts to cite something as an exemption to a generally accepted rule or principle without justifying the exemption.

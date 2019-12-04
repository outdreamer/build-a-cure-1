to do:

- finish get object functions for pulling existing research studies 
  - symptom examples:
  - fever red urine skin rash paralysis headache bleeding

- fix plural form of duplicate objects in sets

- remove nouns, verbs, adverbs & adjectives from objects:
  - components
  - compounds
  - remove common nouns analysis, basis, dis/order, diagnosis from conditions

- same line in functions: expressionactivity
- do a check for full keyword matching before adding a partial match
  compounds: 'disease'
  causal_layers: 'cr,ratio' 
  metrics: 'administration'

- check chembl search if you can search for a condition & return molecules known to treat it

- finish is_valid function 

- integrate conditions/symptoms and treatments/compounds schemas

- finish treatment failure condition - make sure it adds nothing if theres no treatment in the article - this is related to intent function

- make a list of common intent synonyms & store - ie, diagnose - use source of bio synonyms

- check output of synonym replacements to make sure its not changing meaning

- add get_related_components function to pull components of a compound & primary metabolites

- get word roots & word distortions of synonyms using lemmatization lib

- finish get_metadata (strategies, insights)

  - insight in a article doc is likely to:
    - have more topic-related keywords
    - have a causation verb (induces, associated)
    - relate to intents important to agents (health, avoid illness)
    "saturated fat intake induces a cellular reprogramming that is associated with prostate cancer progression and lethality"
    https://medicalxpress.com/news/2019-11-high-fat-diet-proven-fuel-prostate.html

  - get strategies used by an organism or used on a compound like: 
    https://medicalxpress.com/news/2019-11-high-resolution-images-malaria-parasites-evade.html

    - the most important metadata attribute to write a function for is the reason for success/failure indicating the mechanism of action or strategy used
      The strategy behind the successful or failed attack should ideally be included
        - "this structure on the compound tears the cell barrier"
        - "induces apoptosis by depriving it of contrary signals"
      in as structured a format as possible (numerical mappings could work for an initial version)

    - drugs need a way to handle common mutation strategies of pathogens
      - up regulating CDR genes
      - reduced sensitivity of the target enzyme to inhibition by the agent
      - mutations in the ERG11 gene, which codes for 14α-demethylase. These mutations prevent the azole drug from binding, while still allowing binding of the enzyme's natural substrate, lanosterol

- next task will be: predict a phage for a pathogen, vs. predict a compound for a pathogen/condition
- in order to accurately predict a compound for a pathogen/condition, you need to know:
  - attributes (compound metadata youre already working on)
  - gene expression impact
  - interaction rules with common cell types it's expected to be exposed to (in the bloodstream if taken orally, in the lungs if inhaled)
  - the sub-components of the compound that could be altered through interaction to neutralize its functionality
  - the specificity of the compound's effects
  - how it's metabolized, to know whether it could be taken at an effective dose
  - if the conditio involves a pathogen, you need to know the pathogen's structure & metadata

- are pathogen receptors/membranes unique enough that you could design a substance to artificially bind with them to deactivate or puncture the membrane without impacting other structures?

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

- finish specific concepts, core functions, and concept operation diagrams

objectives:

- analyze which components these disease & evolved genes/traits have in common & which system attributes are influenced
  and try to predict diseases & evolved genes/traits from new component sets & newly enabled interactions with existing components
  & find an optimal set for health (extra processing organs, more diverse microbiome, etc)
  https://medicalxpress.com/news/2019-11-humans-co-evolved-immune-related-diseasesand.html

- generate multiple datasets:
  - smile + each medical component (side effects, functions, symptoms) to get a predictor formula for that component from the smile formula
  - really you should iterate through all combinations of components and generate a dataset for each one to check for relationships
  medical_components = [
    metrics: {'naa-cr ratio': 'reduced'}
            conditions: 'hiv', 'encephalopathy'
            organs: ['brain', 'immune system']
            compounds: ['naa', 'cr']
            insights: [
                'naa-to-cr ratio is reduced in hiv patients', 
                'naa-to-cr ratio is a marker for hiv brain infection'
            ]
            strategies: [
                'target bio markers that change with illness for testing',
                'consider other conditions like lack/excess of signals from diagnostic tests & interfering diseases'
            ]
            symptoms: [
                'encephalopathy': 'no imaging findings'
                'neurological disease': 'other'
            ]
            patient: ['HIV-positive', 'symptoms of neurological disease']
  ]
  - chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
  - data set of just props in case there is a relationship between successful treatment & one of the properties available (need a chemical with property x value y)

-  make table of useful patterns as you pull data, replacing common objects with abstract type keywords:
  Example:
    Cytotoxicity in cancer cells
    anti-tumor
    suppress/interfere/inhibit activity of carcinog/canc/tumz

  Patterns:
    <component object>-toxicity
    anti-<component object of illness>
    suppress/interfere/inhibit activity of drug/medication/enzyme

- once you have standard object analysis with some object model insights, you can apply them to bio systems
  - "adjacency as a definition of relevance can be used as a way to derive paths" + "path optimization can be used to get a drug to a location in the system"

- the full data set should have numerical categories indicating condition(s) treated in the output label so it can be separated into sub-sets by condition treated

- incorporate stacked autoencoders to leverage unsupervised learning to get initial weights

- incorporate cosine loss rather than categorical cross entropy

- add recurrent nn example code that can be copied & plugged in without modification

- write function to get semantic bio metadata of compounds (bio-availability, activation in the host species, etc)

- write function to pull symptom lists for a condition from forums/drugs/rxlist

- build math logic/plain language translation function first - example: https://adventuresinmachinelearning.com/improve-neural-networks-part-1/

- in order to implement this without ml, you need functions to identify conceptual metadata of a compound or organism, so at least these to get started:
  - function-identifying function 
  - attribute-identifying function 
  - type-identifying function

- later you can do more advanced analysis, like:
  - determining position/role in a system 
  - determining set of patterns for its functions 
  - determining rules associated with its core functions (change rules, boundary rules)
  - determining side effects in edge cases, interacting with other bio-system layers
  - determining solution via conceptual route

- when generating solutions, change core functions to vary to describe any function set that builds any other function set in a system
  - set of binding functions for element atoms
  - set of molecular interaction physics for compound molecules
  - set of interaction functions for microorganisms
  - set of priority functions for microorganisms

- write a function to derive these core component functions for any system

- consider using dimensionality reduction as a way to identify abstract patterns & functions to explain common deviations from patterns
  https://miro.medium.com/max/1659/1*nQrZmfQE3zmMnCJLb_MNpQ.png
  https://towardsdatascience.com/step-by-step-signal-processing-with-machine-learning-pca-ica-nmf-8de2f375c422

- use this or similar as example when describing current state of problem solving: 
  https://miro.medium.com/max/462/1*X7dQgs1gsJ0Sktz3t7J21Q.png
  https://towardsdatascience.com/feature-extraction-techniques-d619b56e31be

Assumption counterexamples:

- Assumption: smile formulas are generally under 100 char
  - wiki for smiles doc has 240-char compound formula: https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system

- Assumption: structure is a good mechanism for deriving function
  - bakuchiol has example of structural difference with similar function:
  https://en.wikipedia.org/wiki/Bakuchiol

- Assumption: wiki articles of related compounds will mention each other
  - sertraline wiki doesnt mention interaction with fluconazole 
    - youd have to derive by noting that it increased blood level/metabolism of substrates some CYP 450 enzymes inhibited by fluconazole
    - or that it is metabolized by some of the same enzymes
    - https://en.wikipedia.org/wiki/Sertraline#Overdose

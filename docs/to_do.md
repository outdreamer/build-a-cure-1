to do:

- finish get object functions

- fix plural form of duplicate objects in sets

- finish syllogistic fallacy diagrams:
  Fallacy of four terms (quaternio terminorum) – a categorical syllogism that has four terms.[13]
  Illicit major – a categorical syllogism that is invalid because its major term is not distributed in the major premise but distributed in the conclusion.[12]
  Illicit minor – a categorical syllogism that is invalid because its minor term is not distributed in the minor premise but distributed in the conclusion.[12]
  Fallacy of the undistributed middle – the middle term in a categorical syllogism is not distributed.[14]

  https://en.wikipedia.org/wiki/List_of_fallacies

- finish red herring fallacy diagrams:
  - texas sharpshooter

- finish informal fallacy diagrams

- remove nouns, verbs, adverbs & adjectives from objects:
  - components
  - compounds
  - remove common nouns analysis, basis, dis/order, diagnosis from conditions

- same line in functions: expressionactivity
- do a check for full keyword matching before adding a partial match
  compounds: 'disease'
  causal_layers: 'cr,ratio' 
  metrics: 'administration'

- finish specific concepts, core functions, and concept operation diagrams

- insight in a article doc is likely to:
  - have more topic-related keywords
  - have a causation verb (induces, associated)
  - relate to intents important to agents (health, avoid illness)
  "saturated fat intake induces a cellular reprogramming that is associated with prostate cancer progression and lethality"
  https://medicalxpress.com/news/2019-11-high-fat-diet-proven-fuel-prostate.html

- symptom examples:
  - fever red urine skin rash paralysis headache bleeding

- integrate chembl search if you can search for a condition & return molecules known to treat it

- add function output to verbs index

- finish is_valid function using pubchem search api & error message

- integrate conditions/symptoms
- integrate treatments/compounds

- finish treatment failure condition
  - make sure it adds nothing if theres no treatment in the article - this is related to intent function

- make a list of common intent synonyms & store - ie, diagnose

- check output of synonym replacements to make sure its not changing meaning

- finish get_metadata

- use source of bio synonyms

- add get_related_components function to pull components of a compound & primary metabolites

- get word roots & word distortions of synonyms using lemmatization lib

- add function to convert smile formula - find way to represent it without assigning numbers to chars, or use the image
  You can drastically speed up your analysis to filter generated compounds by validity if there is an api to check if a compound string is valid, bc generating smile formulas is quicker than manipulating coordinates
  - pubchem has a validator in their search for invalid structure submitted to api: "Exception during execution: Unable to standardize the given structure"

  - you need a way to store position of two numbers (left & right element number of protons) in one number as well as the bond type, unless you put the bond type in the next column or if the bond type is derivable
  - you could use a ratio if you store the original values for each row, but that leaves out identity information - the ratio might not be relevant but the identities
  - what about a decimal pair like left_number.right_number - is there room for tuples per cell?

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

to do:
- finish is_valid function using pubchem search api & error message

- finish get_correlation_of_relationship

- make sure you remove punctuation

- check output of synonym replacements to make sure its not changing meaning

- finish tuning output of treatments to list actual treatments from articles

- finish get_metadata

- find source of bio synonyms

- add get_related_components function to pull components of a compound & primary metabolites

- get word roots & word distortions of synonyms using lemmatization lib

- pull strategies used by an organism or used on a compound like: 
  https://medicalxpress.com/news/2019-11-high-resolution-images-malaria-parasites-evade.html

- add function to convert smile formula - find way to represent it without assigning numbers to chars, or use the image
  You can drastically speed up your analysis to filter generated compounds by validity if there is an api to check if a compound string is valid, bc generating smile formulas is quicker than manipulating coordinates
  - pubchem has a validator in their search for invalid structure submitted to api: "Exception during execution: Unable to standardize the given structure"

- the most important metadata attribute to write a function for is the reason for success/failure indicating the mechanism of action or strategy used
  The strategy behind the successful or failed attack should ideally be included
    - "this structure on the compound tears the cell barrier"
    - "induces apoptosis by depriving it of contrary signals"
  in as structured a format as possible (numerical mappings could work for an initial version)

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
  - "adjacency as a definition of relevance can be used as a way to derive the path to get a drug to a location in the system"

- drugs need a way to handle common mutation strategies of pathogens
  - up regulating CDR genes
  - reduced sensitivity of the target enzyme to inhibition by the agent
  - mutations in the ERG11 gene, which codes for 14α-demethylase. These mutations prevent the azole drug from binding, while still allowing binding of the enzyme's natural substrate, lanosterol

- sertraline wiki doesnt mean interaction with fluconazole 
  - youd have to derive by noting that it increased blood level/metabolism of substrates some CYP 450 enzymes inhibited by fluconazole
  - or that it is metabolized by some of the same enzymes
  - https://en.wikipedia.org/wiki/Sertraline#Overdose

- wiki for smiles doc has 240-char compound formula: https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system

- So you'll be generating multiple datasets:
  - smile + side effects to get a side-effect predictor from formula
  - smile + function to get a function predictor from formula
  - smile + props to get a property predictor from formula
  - chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
  - data set of just props in case there is a relationship between successful treatment & one of the properties available (need a chemical with property x value y)

- small changes in structure can invalidate functionality - find a list of those change types

- when you describe the attributes & functions of an object, make sure to list key attributes of each function in a keywords attribute for quick searching for relevant interactions

- the full data set should have numerical categories indicating condition(s) treated in the output label so it can be separated into sub-sets by condition treated

- incorporate stacked autoencoders to leverage unsupervised learning to get initial weights

- incorporate cosine loss rather than categorical cross entropy

- add recurrent nn example code that can be copied & plugged in without modification

- write function to get semantic bio metadata of compounds (bio-availability, activation in the host species, etc)

- write function to pull concepts from a research article 

- write function to pull relationships from a research article

- write function to pull symptom lists for a condition from forums/drugs/rxlist

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
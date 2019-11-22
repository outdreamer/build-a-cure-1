done:
- process chemical structure data json & write to csv

to do:
- finish is_valid function using pubchem search api & error message
- the most important metadata attribute to write a function for is the reason for success/failure
- The mechanism behind or reason for the successful or failed attack should ideally be included ("this structure on the compound tears the cell barrier" or "induces apoptosis by depriving it of contrary signals", etc) in as structured a format as possible (numerical mappings could work for an initial version)

- You can drastically speed up your analysis to filter generated compounds by validity if there is an api to check if a compound string is valid, bc generating smile formulas is quicker than manipulating coordinates
  - pubchem has a validator in their search for invalid structure submitted to api: "Exception during execution: Unable to standardize the given structure"

So you'll be generating multiple datasets:
  - smile + side effects to get a side-effect predictor from formula
  - smile + function to get a function predictor from formula
  - smile + props to get a property predictor from formula
  - chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
  but small changes can invalidate functionality - find a list of those change types
  
- when you describe the attributes & functions of an object, make sure to list key attributes of each function in a keywords attribute for quick searching for relevant interactions
- use bio assay data to predict how a compound will interact with an environment in the absence of human testing
- side effect keywords to use to test relationships derived with nlp tools:
  - nouns: effect, activation, transcription, activity, catalyst, reaction, process
  - verbs: enhance, reduce, down/upregulate, stimulate, de/activate, dis/enable, catalyze, alleviate, decline, increase, enrich, moderate, adjust, change
  - adjectives: active, synergistic, neutralizing, anti-
  - objects: 
    - process:
      - apoptosis
      - glucolysis
    - properties:
      - fragility
    - chemical compounds: molecules
    - bio compounds 
      - proteins
      - enzymes
      - lipids
      - genes: expression, active, 
      - blood
    - cell components:
      - mitochondria
    - microorganisms:
      - bacteria
      - fungi
      - virus
    - tissue:
      - muscle
    - organs: 
      - liver
      - kidney
      - bladder
    - systems:
      - lymph
      - nervous
      - immune
      - circulatory
      - digestive
      - 
    - treatments
    - conditions: anything ending in -a is usually a condition
    - tests: pcr
    - metric: levels, quantitative, glucose


- add function to convert smile formula into fixed number of numerical columns by assigning numbers to chars & scaling
- decide if you need one hot encoding to reprsent categories
- write smile generator function
- the master data set should have numerical categories indicating condition(s) treated in the output label so it can be separated into sub-sets by condition treated
- incorporate stacked autoencoders to leverage unsupervised learning to get initial weights
- incorporate cosine loss rather than categorical cross entropy
- add more nn example code that can be copied & plugged in without modification
- write function to get semantic bio metadata of compounds (bio-availability, activation in the host species, etc)
- write function to pull concepts from a research article 
- write function to pull relationship from a research article
- write function to pull symptom lists for a condition from forums
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

- also create data set of just properties in case there is a relationship between successful treatment & one of the properties available (need a chemical with property x value y)
- look for ways to break up tumors:
  - promote circulation in the organ (like caffeoquinone acid in the liver)
  - inject something the immune system needs
  - push them to a place with greater blood flow or cell communication
  - make many small incisions to activate helpful cell division
  - you need a way to detect tumors before theyre so big they need to be surgically removed, 
    which means either a scan that doesnt use radiation or an army of nanobots, unless theres a metric available with less invasive tests you can use
  - if you can isolate tumors with a compound that they will interpret as the boundary of the host so they dont replicate further, 
    you can probably extract most tumors in pieces using suction devices
  - ideally the solution would use the extra cell division potential to make useful cells
  - or there would be a set of stressors to prevent it from developing
  - make a list of all the potentially helpful substances & organisms & the list of stressors that deactivate/activate them (example, MUC1 - bacteria exposed to a split tail activates it)
  - make a list of anti-inflammatories & fit them to the stressor model
  - determine which organisms can borrow genes & look for link to cancer
  - determine the ratio of stress that optimizes learning without killing the host
  - communication, stressor distribution, & boundaries are important concepts to cancer
  - make a list of the common types of error the immune system makes (h pylori, cancer) 
    and figure out if adjusting immune system function is the best layer to attack from

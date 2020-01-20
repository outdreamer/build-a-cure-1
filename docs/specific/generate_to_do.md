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

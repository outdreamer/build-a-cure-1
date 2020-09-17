'''

  - definition: 
    - uses patterns in network structures & insight paths to predict: 
      - probable missing pieces of networks 
      - insight path of a route type (optimal/realistic) 
      - insight path trajectory for a particular assumption set 
  
  - attributes: 
    - reusability (insights can have a limited opportunity of applicability, and may have scope beyond their host system) 
  
  - functions:
    - apply/derive an insight path, shown in FIG 20 (Insight path application)
    - link insights
    - identify insight

  - objects:

    - rule structure (combination of rules, sequence of rules, position of rules) 

    - units of insight paths include core functions to produce insights, such as:
        - change/split/merge type
        - change attribute value/set
        - apply limit/intent/priority/function/pattern from one part of system to another part of system
        - insert interim/sub-system
        - insert variance
        - insert conflict
        - derive common attributes/rules
        - combine objects that haven't been combined yet
        - check similar objects for common cause or symmetry
        - remove/add assumption/requirement/dependency/connection

  - structures: 

    - insight path: a reusable cross-system pattern, usually built out of core functions from a general interface filter (type, intent, function, structure), that allows generation of insights. 
        It can be as simple as a function like differentiate, a standardizing attribute like relevance, or involve a standard object like a simplifying question. 
        It does not refer to specific strategies unless those strategies can be used to generate insights. 
        Insight paths usually consist of abstract or structural rules like 'match structure' or 'identify type'.


  - concepts: 
    - predictive power (an insight is true & may be powerful in predicting across systems) 

  - examples:
    - a unit example is 'trial and error' or 'statistical regression' or 'break up the problem into smaller problems & solve them separately, then aggregate solution output' - these are standard abstract rule sets/sequences to apply when discovering new insights in a system, which can be used across systems. You can call these specific strategies, but they can also be considered insight-generators or solution-filters, as they can reduce the solution space when narrowing down possible insights describing a link to the correct linking rule. These examples are not always ideal/efficient so they're not top priority methods, but they're a good example of what position an insight path occupies in a system. 
    - an actual useful insight path would solve a common, abstract difficult problem, like 'generating the idea of regression', which would be something like:
      - query for concept adjacent to balance/equivalence in the context of a data set output (average)
      - apply the concept of average to indicate a general average distance within output range specified by input format (point subsets) in an input (data set)
      - find a definition of 'average between output ranges of point subsets' that matches the change type you're aiming for (ie, least squares)
      - find a definition of the format 'point subsets' that matches your average definition (adjacent points with euclidean distance definition, in subsets of the data set with a particular change rate)
      - format the input (calculate the data set subsets) using the 'point subsets' definition
      - apply the definition for 'average between output ranges of point subsets' to the formatted input (calculated data set subsets)
    - As shown in the top section of Fig. 19 in the section titled 'Averaging/Standardizing Function' depicts example implementation of the function, involving sub-functions to connect input A and output B are depicted, with varying number of steps, usage of core functions, direction, probability & complexity.
    - Applying an insight path like 'functions requiring more distortions are less likely' may automate the assignment of levels of probability to prediction functions, given the 'Averaging/Standardizing function' implementation structures depicted.
    - The section of Fig. 19 titled 'Interface Object Insight Path' depicts an example of an insight path that is a trajectory of objects on the interface network, which has some objects in common as the system path because of the cross-over in definitions of a system and an interface. These objects may be object/attributes/rules of an interface (or combinations/other core functions applied to them), maps between interfaces, or filters used to generate an interface.
    - The section of Fig. 19 titled 'Structural Insight Path: Function Pattern' depicts an example structure to frame common distortion patterns as alternate routes from function input to function output, which are a very useful subset of insight paths to generate insights across fields.

  - answers questions like:
    - what rules are useful across systems?
    - what rules are derivable given a set of structures that commonly appear in systems?
    - what are common rules used for previous insights, and how can they be optimized (shortening an insight path with a set of simplifying/standardizing questions)

  - dependencies
    - this function relies on the apply_structure function and the find_format_for_metric.py function 
    
  - visuals
    FIG. 19. 'Insight path application' illustrates insight path examples and an example of applying an insight path. 

'''
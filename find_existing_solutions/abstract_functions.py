'''
  - function to identify alternative routes to an object (create & retrieve info from definition_routes.json)
      
    - this function should find/describe those routes - other functions can rank them & select the best one for a particular intent 

  - definition_routes.json can be generated from the paths in interface_networks.json, which just describes the links in networks of concepts/intents & other interface networks
  
  - function to map object to a function shape
    - this is particularly useful for graphing concepts like 'power' or 'dependence', so these concepts can have structure applied for computation
      - this requires:
        - descriptions of shape metadata
        - concept metadata from interface_networks.json and concepts.json

  - function to map function type/set/chain to a function shape for linking nodes

    - a n-function chain can be framed as a set of functions with linked inputs & outputs, but what does 2-d direction indicate? difference from standard function forming the straight one-function link between the nodes? does 3-d direction add a priority dimension?

      - reverse can be framed as a function chain:
        - determine key metric (direction or starting/ending object)
        - determine direction (first/last item in the sequence)
        - make copy of object or empty object of the same type
        - permute starting point to reverse direction (last/first switch)
        - fill copy of object from new starting point

      - the short version of 'reverse' would be less abtract:
        - list sequence, starting from end

      - what are the intents/priorities of each function, in each method to form 'reverse' function?
        - 'list sequence' has the intents 'describing a sequence' and 'iterate'
        - 'determine key metric' has intents 'determine identifier of reversed object', 'abstract'
        - 'make copy' has intents 'backup', 'adjust with minor changes', 'compare', 'apply process for comparison with original'
        
      - when youre graphing the network of nodes such as object states, like original sequence and reversed sequence, the connecting function between state nodes could vary by these intents, and the 2-d version could indicate:
        - difference of function chain from standard efficient function link
        - abstraction
        - intent alignment (no variance injection points)

      - so the function could look different if graphed on different interfaces

      - the aggregate version of the function might be able to collapse some of the corresponding/aligning differences, bc the aggregate version might not vary on all interfaces (type or causation changes might line up with intent changes, so both arent necessary)

  - function to identify interface trajectory (most efficient path, and destination in same position on other interface) between conceptual/structural interfaces

    - info => clarify => structure
    - info => remove uncertainty => resolve conflicts/alternatives in variable values => isolate => achieve constant state => structure

    - info is a hub between several objects as structure is a hub for the corresponding objects, occupying both the same position type (hub) and the same position on corresponding interface networks

  - attribute identification function

    - identify an object's attributes by:

      - attribute metadata

        - which attributes are:
          - isolatable/unique
          - descriptive/generative/differentiating

        - which attributes have: 
          - change that doesnt align with other changes on the same interaction layer
          - a position separate from other positions in a network
          - type stacks different from other stacks
          - ability to differentiate/identify an object of similar attributes or within the same type
          - causation (caused by something as an output, or an input cause of something else)
          - potential for change
          - alignment with concepts (relevance aligning with similarity/equivalence)

      - information left over that is not captured by other attributes or describable by randomness

  - add a function to get all codebase functions & store them in a dict with their name, params, class, context/usage, and intents, just like functions are stored in the problem_metadata.json example for workflow 1

      - add function to map conceptual object to structural object

        - mapping 'info' to 'structure' can be done with a conceptual route:
          - info => clarify => structure
            concept intent     structure

        - or a layer-traversing route, adding structure with each additional transform:
          - info => remove uncertainty => resolve conflicts/alternatives in variable values =>  isolate =>                    achieve constant state => structure
            concept sub-concept           potential                                             limit/measure                 match function/object     structure
            info    data set              remove duplicate/correlated vars                      remove non-explanatory vars   fit function              fit structure (find semantic map this information fits on as an object/attribute/rule)

      - add function to map conceptual function to structural step:

        - in addition to mapping objects like 'info' to supported objects like 'structure' using the schema or definition derivation, 
          we also want to map concept functions like 'balance' to structural terms like 'evenly distribute',
          and map modifiers like 'evenly' to calculation operations like 'check distribution equal' so that 'evenly distribute' is translated to several options:
            - 'change distribution until equal for all positions'
            - 'remove all' (specific case which is a shortcut implementation of the 'change distribution until equal' operation

          - then 'check equal distribute' would be converted to 'check equal distribution'
          - then reversed to 'check distribution equal' since the 'equal' attribute applies to the 'distribution' object
          - the dependency for 'check' would be found to be 'change' if theres no other process changing it
          - this would create two steps to achieve the 'equal distribution' intent state derived from the step:
            - check if distribution is equal
            - if not, change it

          - then it would be derived that 'iteration' intent applies here since one change may not achieve the 'equal distribution' intent state, either by querying for insights about changes producing a state, or by checking if the goal is reached after one iteration, and then applying any available functions again (the same ones or a combination of other functions available, which is more computationally expensive and may not be allowed by the definition of 'improve') if not

          - the original options for 'evenly distribute' would be used as testing metrics, checking that either all objects were removed or that the remaining objects were distributed evenly

          - in order to build this concept-to-structure function, we need:
            - stored standard language maps & definitions
            - a function (or a dictionary) to standardize language to this system's terms (so distribute is converted to 'change position of objects in group until objects are not in the same position')
            - a function to convert non-supported functions into combinations of supported functions (standardize 'enhance' to 'improve' or 'increase')

              - you can create a 'definition' function and then apply it to test its impact to see if it matches

              - or you can also map intent to create a network for each stored definition, then see if you can optimize/standardize the network, and map it to a supported function network
                - enhance function:
                  - 'apply some process to improve or increase some attribute or process'
                  - intents: change, move in the direction of increasing a metric/object/process or minimizing distance to goal 
                - improve function:
                  - 'apply an optimization process to fulfill a metric' 
                  - intents: minimizing distance to goal, minimizing distance to metric, increase likelihood of minimizing distance to goal (optimize)
                - increase function:
                  - 'apply the add process until the quantity of an object is higher'

                - it also has similarity to 'compound' (which adds extra meaning of applying similar objects/functions to other objects/functions and synergy),
                  but 'improve' and 'increase' are supported core functions and we're trying to standardize the word to a combination or set of these
                - its clear that enhance has some relationship to both of the other functions, which would be even clearer with a network version of each definition

                - given the example input context 'enhance process A to produce a byproduct', we can derive that this is about achieving a goal that doesnt specifically or exclusively have 'increase' connotations, leaving 'improve' as the likely core function to map 'enhance' to, for this context

                - you can test the 'improve' definition on the input objects 'process A' and if it moves in the direction of the other object 'byproduct', it's a better candidate for the standardized function
                  - does 'improving' the objects in the original context have the same output as 'enhancing them'? which types of improvement produce an enhancing effect? 
                  - is there a way to improve some attribute of the objects in a way that doesnt improve the object enhanced in the original context?

                - you can do extra testing on the intent interface:
                  - does 'improve' fulfill 'enhance' intents or just a subset of them, and is that subset the more valid subset in a set of alternatives, or are the other subsets required for the definition?
                  - do 'improve' intents apply to the objects in the original context or do some of them not fit?

      - the concept-to-structure mapping functions can be used in other problem-solving automation workflows


      - then add functions to derive metadata 
        - need dicts for this, including:
          - function chain intent relationships (in addition to function dependency relationships stored in function_order.json)
          - type hierarchies/network structures

'''
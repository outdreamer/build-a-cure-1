  - add formatting to allow multiple items as keys in json and maintain order for interface network paths

  - abstract functions

      - function to find if a concept definition matches a structure:

        - get list of structure objects
        - check if any structure objects match definition relationship objects
        - if so, get relationship between those structure objects
        - check if that structure relationship matches concept definition relationship

        - example:
          - trust: [
            'depend on limited/specific inputs',
            'check at intervals'
          ]

          - structure: 'test applied daily'
            - structure objects: 'test'
            - relationship: 'apply test daily'

          - matching objects: 
            'test', 'check'
            'daily', 'interval'

          - matching relationship:
            'check at intervals' matches 'apply test daily'

          - this structure 'apply test daily' is a potential source of trust in a system (the only time info about the object being tested is not trusted is during the test)

      - network framing function to describe a system as a network & position each object, identifying connecting functions
      - attribute/object/function identification functions
      - interface identification function
      - function to map function type/set/chain to a function shape when linking nodes in a network
      - function to map object/function to a shape
      - representation of a function/attribute changes in isolation with respect to position or time (snapshot or section)

      - function to identify interface trajectory between conceptual/structural interfaces
        - may involve navigating sub-networks within an interface, not just mapping between interfaces
        - trajectories such as: most efficient path, and destination in same position on other interface)
        - uses interface_networks.json if it exists and if not, interface identification, network mapping, and similarity testing
        - function to identify alternative routes to an object (create & retrieve info from definition_routes.json if its already in interface_networks.json)
          - a system applicable to this function would be a process or object like a particular pathogen - complex enough to qualify as a system
        - definition_routes.json can be generated from the paths in interface_networks.json, which just describes the links in networks of concepts/intents & other interface networks
        
        - then add function to map:
          - conceptual object to structural object
          - conceptual function to structural step
      
      - system analysis function (identify boundaries, gaps, limits, layers, & other system objects)

  - give example of each type of problem-solving workflows

    - workflow 1:
      - finish function to determine relevance filter ('functions', 'required') from a problem_step ('find incentives') for a problem definition, to modify problem_steps with extra functions/attributes ('change_position') to be more specific to the problem definition ('find_incentives_to_change_position') for problem_steps involving 'incentives', so you know to use the function_name to modify the problem step if it's between the type 'functions' and the object searched for 'incentives'

      - finish function to get all codebase functions & store them in a dict with their type, context/usage, and intents, just like functions are stored in the problem_metadata.json example for workflow 1
      - finish common sense check
      - finish defining objects in object_schema.json
      - finish organizing functions.json by type, with mapping between general intent functions like 'find' to specific info-relevant terms like 'get'
      - add common phrase check & filter problem steps by repeated combinations with common phrase check
      - finish get_type function to map info to structure using the new functions.json organization
      - finish apply_solution to problem_definition using problem_steps
        - involves building a function to evenly distribute objects (like information/types), given problem positions/agents/objects
      
  - types should be represented as directions (going farther from origin goes further up type stack, where similar types are adjacent)
  - finish system analysis for VDJ recombination 
  - find other relevant immune processes to analyze

  - need to fill in content:
    - finish intent/change type calculation for a system intent
    - selecting optimal combination interfaces to start from when solving problems 
      (how many degrees away from core functions, specific layers or sub-systems, what position on causal structures)
    - key questions to filter attention/info-gathering/solution
    - key functions to solve common problem types
    - development of key decision metrics (bias towards more measurable/different metrics rather than the right metric)
    - trajectory between core & important objects
        - example of choosing inefficiencies/exploit combinations in a system
    - research implementing your solution type (constructing structures (made of boundary/filter/resource sets) to produce substances like antibodies, using bio system stressors)
    - emergent combinations of core functions (include derivation of invalidating contexts for core functions)

  - change phases for causal analysis (interim, changing, diverging, standard, efficient state, constant, interacting, converging, on the verge of obsolescence, outlier, etc)
    - superficial cause, alternate cause in the case of a function, addressing input/output causes
  - framing on interfaces, decomposing causation, then identifying parameters of problem on layer & matching solution
  - independence (closed trade loops) as time storage
  - vertex as a pivot point for an interface

  - function to create graph from article
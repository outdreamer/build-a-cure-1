  
  - add formatting to allow multiple items as keys in json and maintain order for interface network paths

  - make tutorial for interface analysis or at least reading list of posts & docs

  - add concept maps & system maps

  - abstract functions

      - derive combinations & make sure you have full function coverage of all important combinations

        operations = ['find', 'get', 'update', 'apply', 'build', 'combine', 'connect', 'convert', 'balance', 'map', 'match', 'fit', 'filter', 'derive']
        objects = ['strategies', 'questions', 'incentives', 'efficiencies', 'metadata', 'definitions']
        structures = ['paths', 'limits', 'boundaries', 'bonds', 'gaps', 'layers']
        system_objects = ['attributes', 'objects', 'systems', 'sub_systems', 'types', 'functions']

        - check codebase function index for combinations
        - check that you have sample data in json for each combination

      - to map a function/object/system to a structure, you need:
        - the definition
        - system analysis of the definition
        - objects from system analysis like implication
        - structures/functions mapped to the objects (like copy implication is that position of the duplicate object must be different from the original object)
        
        - these objects can be framed in many structural ways:
          - as a set of filters (generating the object/function/system)
          - as a set of vectors (indicating the key attributes or functions generating/determining the object/function/system)
          - as a set of shape structures (indicating how the object's logic works internally (how attributes are related to functions, as in a shape)
          - as a set of embedded dimensions (where an embedded graph indicates internal or subset processing/objects)
          - as a set of related graphs (where each graph depicts structure of some attribute set of the original object/function/system)

      - to map attributes (identifying/differentiating measurable properties of an object like relevance or connectivity), you need:
        - a base object structure 
        - a dimension to frame values & their differences added by the attribute
        - the attribute can be in an embedded dimension set (to indicate differences in value on multiple parameters of the attribute, like when the differences offered by an attribute vary by change type & change rate), but the base object should be included in the structural representation if possible

      - to map a system, you need:
        - nodes with boundaries, indicating objects & components of objects
        - functions linking nodes:
          - vectors with direction, indicating causal direction, input/output flow, intent direction, and other direction-structurable attributes
          - functions whose shape indicates relationship type 
        - system boundaries/layers/gaps/potential and other system structures if they exist

      - to map a type, you need:
        - subset shapes to indicate attribute sets, and structures linked to each attribute to indicate attribute value, range, type & other metadata
        - nodes indicating types 
        - links indicating any causal directions between types

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
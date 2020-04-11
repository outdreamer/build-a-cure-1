
  - fix indexing 'NNP NN NNS1 of JJ JJ JJ2' or postpone to pattern evaluation time
  - fix incomplete alts noun_phrase::N, f, 'works a NN', 'interacts as NN', 'a NN role'
  - add formatting to allow multiple items as keys in json and maintain order for interface network paths

  - fix supported stem assignment (endings like 'is': {'functions a', 'acts a', 'plays a', 'operates a', 'works a'})
  - fix charge function ('edit' is assigned positive score)

  - add core clause patterns 
  - fix pattern matching functions
  - finish pos, clause, modifiers code from find implementation
  - finish network creation function
  - strategy/insight graph

  - map core concepts to structures for use when building other concepts/objects

    - equivalence: 

      - core structural factors:
        - position of determining points (for a line this is either endpoint)
        - distance/length/scalar
        - unit object/attributes/functions (what is the standard form, what core operations does it support)
        - potential field (what positions can it occupy with adjacent transforms)
        - angle of change
        - space/dimension set

      - core definitions

        - equal
          - all attributes/state/values match, irrelevant to the path to the object
  
        - similar

      - equivalence types
        - structural
          - origin/destination (given a particular definition of change & a value for that change type, how does motion create the object or emerge from the object) 
          - shape
          - path (same pattern between origin/destination)
          - set (same set of generative/output/determining objects or interface objects)
          - intersecting (y = f(x))
          - adjacent (one transform away in the form of a shift operation)
          - dimension (variable set, space definitions/conditions)
        - subset equivalence
          - approximate
          - functional
          - alternative
          - interchangeable
        - processed equivalence
          - duplicate
          - version
          - iteration
          - combination
          - standardized equivalence
        - conditional equivalence
          - equal with conditions/context
        - type equivalence
        - matching
          - opposite matching structures, opposite being an adjacent object to the original, and matching object being a fit of an object, indicating an opposite transform
        - symmetric
          - transformable/reversible transforms

      - equivalence attributes
        - degree of equivalence
        - conditions/filters
        - definitions

      - related object definitions
        - change
        - value
        - distance
        - position
        - scale
        - unit
        - angle
        - degree
        - space

      - the different definitions of 'equivalence' types should be mappable with this attribute set
        - system:
          - equal on an attribute set
            - differences
            - emergent output
            - required inputs
            - types
            - output probability distribution
          - equal in system position (occupies same resource set in system or same role)
          - equal in system context (emergent output will be the same)
        - change:
          - equal in change type/rate/pattern/definition
        - intent:
          - equal in granular intent fulfilled/neutralized
          - equal in output priority direction
        - function:
          - equal in function/function metadata
        - potential:
          - equal in range of potential

      - visualizing equivalence across definitions & types:
        - if you can standard objects to attribute sets, you can visualize as a graph of attribute sets where shapes map to attribute sets and visible or highlighted shape attributes are equivalent
        - you need to incorporate objects like conditions & definitions as system/space attributes

  - after identification functions

    - import rules for selecting interfaces to solve a problem on

      Function helped find unused functions
      Intent helped predict system priorities & find exploit opportunities
      System helped find efficiencies
      Pattern helped find insight paths/similarities

    - once you build function/attribute identification function
      - import insight history data to identify insight paths 
        - info insight paths like 'lie => joke => distortion => insight'
        - system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub'

    - make tutorial for interface analysis or at least reading list of posts & docs


  - extra tasks

    - add precomputing if a sub-pattern was already computed:
               'ALL_N ALL_N of ALL_N ALL_N'
         'ALL_N ALL_N ALL_N of ALL_N ALL_N ALL_N'


  - abstract functions

      - derive combinations & make sure you have full function coverage of all important combinations

          operations = ['find', 'get', 'update', 'apply', 'build', 'combine', 'connect', 'convert', 'balance', 'map', 'match', 'fit', 'filter', 'derive']
          objects = ['strategies', 'questions', 'incentives', 'efficiencies', 'metadata', 'definitions']
          structures = ['paths', 'limits', 'boundaries', 'bonds', 'gaps', 'layers']
          system_objects = ['attributes', 'objects', 'systems', 'sub_systems', 'types', 'functions']

        - check codebase function index for combinations
        - check that you have sample data in json for each combination

      - attribute/object/function match functions
      - specific interface identification function
      - standardization network-framing function to describe a system as a network (the standard structure) & position each object, identifying connecting functions
      - system analysis function (identify boundaries, gaps, limits, layers, incentives/intents/questions, & other system objects)
      - isolation function, representating function/attribute changes independent of system context with respect to position or time (snapshot/state or subset)
      - function to define (isolate an object/concept/function for identification, identify definition routes)


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
      
  - types can be represented as directions (going farther from origin goes further up type stack, where similar types are adjacent)

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



- notes

    - if something can generate a change predictably/consistently, it's a change supply - otherwise it's a change request, so output as well as causal position relative to the output is important when determining category
      - time may be a variance gap (a space where change is possible) to resolve a question/problem set - so not resolving it can preserve time, unless resolving it will allow for more potential or moving on to other variance gaps

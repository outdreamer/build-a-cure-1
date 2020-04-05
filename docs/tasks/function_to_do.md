  - added var_names to pattern alts functionality

  - make sure patterns without pos are complete

    ./data/all_patterns.txt:pattern_index::clause_identifier::suppose  that
    ./data/all_patterns.txt:pattern_index::clause_identifier::thought 1 that2 DPC 4 suppose 6 that7
    ./data/all_patterns.txt:pattern_index::clause_identifier::suppose 1 that2 DPC 4 assumed 6 that7
    ./data/all_patterns.txt:pattern_index::clause_identifier::assumed 1 that2 DPC 4 suppose 6 that7
    ./data/all_patterns.txt:pattern_index::clause_identifier::suppose0 1 that2 DPC 4 suppose5 6 that7
    ./data/all_patterns.txt:pattern_index::clause_identifier::suppose 1 that2 DPC 4 thought 6 that7
    ./data/all_patterns.txt:pattern_index::verb_phrase::operates 1 as 3 NN
    ./data/all_patterns.txt:pattern_index::verb_phrase::operates 1 as a 4 VB
    ./data/all_patterns.txt:pattern_index::verb_phrase::operates 1 as a 4 NN
    ./data/all_patterns.txt:pattern_index::verb_phrase::operates 1 as 3 VB


  - make sure nested variables are re-iterated until there are no alt sets left

  - add formatting to allow multiple items as keys in json and maintain order for interface network paths

  - make tutorial for interface analysis or at least reading list of posts & docs

  - fix supported stem assignment (endings like 'is': {'functions a', 'acts a', 'plays a', 'operates a', 'works a'})
  - fix charge function ('edit' is assigned positive score)
  - fix type_index split adding chars
  - fix assignment of pattern_maps to computed patterns
      key pattern_maps {'passive_to_active': 
      {
        'x of y': 'y', 
        'x was VBD by y': 'B', 
        'x that has y': 'x', 'the N1 VBD VBN IN the N2': 'the N2 VBZ the N1', 'x VBD VBD IN y': 'N', 'x VBD VBN by y': 'B', 'x VBZ VBN by y': 'x', 'x that y z': 'z', 'x that does VBG': 'Z', 'x with y functionality': 'y', 'x has ability to do y': '0.0 0.0', 

  - store alternate patterns from pattern_index separately once alts are computed
  
      key pattern_index {'passive_identifier': ['|VB VBP VBN VBD| |VB VBP VBN VBD|', 'VBG |VB VBP VBN VBD| |VB VBP VBN VBD|', '|VB VBP VBN VBD| |TO IN PP|', '|VBD| VBN VBN |TO IN PP|', 'ALL_N ALL_N of ALL_N ALL_N', 'ALL_N ALL_N ALL_N of ALL_N ALL_N ALL_N', 'JJR RB NNS2 IN NNS4 NNP5 NNP6', 'NNPS0 RB NNPS2 of NN NNS JJ', 'JJR0 JJR1 IN NNP JJ', 'RB0 NNP1 JJ of JJR RB5 NNP6', 'NNS0 RB NNS2 of NNS4 NNP NNPS', 'NNPS NN NNS of NNP4 NNP5 JJ',

  - add core clause patterns 
  - fix pattern matching functions
  - finish pos, clause, modifiers code from find implementation
  - finish network creation function
  - then go back to identification functions

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


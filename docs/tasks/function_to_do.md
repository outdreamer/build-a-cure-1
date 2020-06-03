  - fix indexing 'NNP NN NNS1 of JJ JJ JJ2' or postpone to pattern evaluation time
  - fix missing alts
      pattern_index::verb_phrase::plays a |VB NN| role::a NN role
  - fix one-letter alts: pattern_index::phrase_identifier::ALL_N DPC ALL_N |VBG VBD|::N D N V
  - generalize alt logic to use embedded pair finding
  - fix supported stem assignment (endings like 'is': {'functions a', 'acts a', 'plays a', 'operates a', 'works a'})
  - fix charge function ('edit' is assigned positive score)
  - add core clause patterns 
  - fix pattern matching functions
  - finish pos, clause, modifiers code from find implementation

  - make function/query list for workflows, starting with information formats

  - identify attribute: attributes can be reduced to 'position', implemented as a:

      - relationship type (relative difference)
      - structure type (shape)
      - change type (generators of difference)

    - the structural network can frame these position differences to capture all attributes
    - add function to derive structures of an object given its attributes/functions (related attribute sets indicating a type or sub-system, etc)

  - identify function: a function can be reduced to a 'change unit'

  - identify object: an object has attributes/functions and is not itself either of those (for standard definition of object, even though both attributes/functions can be framed as objects)

  - after identification functions

    - import rules for selecting interfaces to solve a problem on

      - determine minimum information
      - query for rules making inferences from available information sets
      - Function interface helps find unused functions
      - Intent interface helps predict system priorities & find exploit opportunities
      - System interface helps find efficiencies
      - Pattern interface helps find insight paths/similarities

    - import insight history data to identify insight paths 
      - info insight paths like 'lie => joke => distortion => insight'
      - system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub'

    - mapping function, to map problems to structures & other problem types

      - find structure

        - find combination (build)
          - of filters
          - of functions
          - of sets
          - of limits

        - find sequence (route)
          - of network nodes representing
            - steps
            - positions
            - sets
            - intents

      - correct imbalance (align)
      
        - in direction
        - in resources
        - in functionality
        - in intent

      - ways to map this:
        - attributes that differentiate problems that are shared with solutions
        - mapping intent to direction and assessing progress by movement in that direction
        - trajectories across dimension sets representing steps
        - networks with clusters & other structures representing decisions
        - system layer graph representing possible steps
        - function sets mapped to sequences given a metric like progression toward goal
        - mapping related/approximate problem or problem higher up causal stack, having lower dimension, like a generative problem
        - mapping change types to dimensions and graphing/calculating dimensions where change types change (a deciding dimension where change type is uncertain but influenced)
        - using a layered graph to visualize change of different types/metrics built on a symmetry (vertical axis if horizontal sections are split)
        - mapping language to structure directly ('find' maps to a set of vectors leading from a node indicating possible start positions, with option to use core function vectors to reach target node)

    - solution decomposition function

    - solution aggregation function

    - make doc to store insight paths, counterintuitive functions, counterexamples, phase shift triggers

    - function to detect patterns in queries & outputs to optimize queries & find insight paths to improve response time

      - example: 3-step jumps with direction change, navigating across a certain pathway in standard structures across interfaces, starting with system then cause & intent, etc
      - this has to identify & remove unnecessary steps that dont change the output
      - identify & replace with faster ways to get to the output without changing the output
      - test cases to determine if output would be changed by removing a step and/or replacing it with another step

  - abstract functions

      - derive combinations & make sure you have full function coverage of all important combinations

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

  - extra tasks

    - add precomputing if a sub-pattern was already computed:
               'ALL_N ALL_N of ALL_N ALL_N'
         'ALL_N ALL_N ALL_N of ALL_N ALL_N ALL_N'
    - add formatting to allow multiple items as keys in json and maintain order for interface network paths

  - alternate utility function implementations have variation potential in the exact operations used to achieve the function intents, but there are requirements in which definitions these functions use because they are inherent to the system. For example, the embodiment may use a specific definition of an attribute (standardized to a set of filters) in order to build the attribute-identification function using a set of filters - but the general attribute definition is still partially determined in its initial version by requirements specified in the documentation, such as a set of core attribute types (input, output, function parameter, abstract, descriptive, identifying, differentiating, variable, constant), the definition of a function, and the definition of conversion functions between standard formats.


  - given that a set of genes produces a range & methods with which change can occur, is there necessarily a determinable difference between which changes can be expected to disrupt the system and which changes its change methods can handle
    - are there necessarily some changes that cant be handled given the ways it can change
    - is there definitely a set of genes that produces a system supporting a set of possible change types that dont allow the system to be destroyed by external pathogens, or does this protected system have the potential to exist genetically, but not coordinate in a way that would be able to function in the real world
    - there is no default mechanism determining the gaps in change rules allowing variance injections in a system generated by genes (which kinds of gene edits are prohibited absolutely, which kinds are contextually possible, etc - these rules are not analyzed for gaps in coverage of change rules by default)
    - these gaps may allow changes to bubble up or cascade system-wide depending on the specificity
      - a rule that allows removal and a rule that allows copying could be used to change the change rules, possibly invalidating themselves or the system
    - how do you find these gaps in enforcement that can be hijacked to disrupt the change rules - with intent structures like chains, networks, & trees

      - whats the intent of deploying a gene edit producing a randomizing function on change locations to every cell? if theres a cell that will become hostile once random changes are made, that could be the intent


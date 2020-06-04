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

      - problem types

        - find structure

          - find combination (build)
            - of filters
            - of functions
            - of objects
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

          - example: find combination of terms to build a prediction function for a data set

            - of filters
              - which filters should be applied to reduce solution space, find relevant objects, or find steps to produce or build the solution

            - of functions
              - which functions are possible solutions to a prediction function problem
                - 'take an average metric of the set of functions predicting x% of the data with fewer than y terms'

            - of objects
                - 'average', 'function set', 'term count', 'accurate prediction ratio'

            - of sets
              - which objects should be grouped (function set, term set)

            - of limits
              - which assumptions are required and which are flexible

            - of matches
              - which objects need to match, to what degree (function terms and data)
              - which set of reductions works the best with a given set of expansions

            - of imbalances/asymmetries (questions)
              - which metric sets are the best filters for a given problem

            - you could graph the problem/solution with any of those objects, if they supply all the info needed to frame the problem
            - navigating on the filter or mismatch section of the network may be faster given the commonness of those objects

          - example: find resources to fulfill a lack of a resource

            - cause of problem: missing resource or its alternatives, or missing resources to generate it or its alternatives, or dependence on resource or its alternative

            1. create missing resource

            - navigate up causal stack: find combinations of functions & objects that generated it
            - navigate sideways: find alternatives or find alternative combinations to generate it

            2. invalidate dependence
            - navigate up causal stack until dependence cause is found: find combinations of functions & objects that generated dependence
            - navigate sideways: find functions to invalidate dependence (generate resource) or correct problem (imbalance, lack, mismatch) causing dependence

            - solution intents 1 & 2 have a 'generate resource' intent in common, which fulfills both solution intents - so if the intent changes between them, the solution involving generating the resource may cover the next problem iteration too, or the intent that invalidates the problem may prevent future iterations


      - ways to map this:

        - attributes that differentiate problems that are shared with possible solutions
        - mapping intent to direction and assessing progress by movement in that direction
        - networks with clusters & other structures representing decisions
        - system layer graph representing possible steps
        - function sets mapped to sequences given a metric like progression toward goal
        - mapping related/approximate problem or problem higher up causal stack, having lower dimension, like a generative problem
        - mapping change types to dimensions and graphing/calculating dimensions where change types change (an aggregate, interface, or deciding dimension where change type is uncertain but not random)
        - using a layered graph to visualize change of different types/metrics built on a symmetry (vertical axis if horizontal sections are split)
        - mapping language to structure directly ('find' maps to a set of vectors leading from a node indicating possible start positions, with option to use core function vectors to reach target node)
        - a trajectory between low-dimensional problem graphs where each graph is a decision step, and attribute sets & problem of similar type occupy a similar position on an axis depicting all the graphs traversed
        - a metric like size of variable interaction space mapped to length/area/volume to indicate how much of the problem is left, and a metric like number of variables mapped to number of sides of the shape to graph the problem according to structural metrics


      - limits in visualization

        - if you reduce a shape of a subset of problem dimensions, those variables (side length if defined as a cube, or variable set like identities of sides, number of corners/sides, angle of corner, shape identity), cant be used later in the solution, so even though some reductions may seem obviously right, more than one solution should be tried

        - mapping problem types to functions has side effects without limits & standardization applied to the format:
          - removing a problem variable can only be mapped to lowering the number of variables (whether limits, multipliers, or other objects) creating a shape once the problem variables are formatted with the same term set


      - parameters to graph problems

        - number of problem-causing variables/solution metrics fulfilled
        - complexity: 
          - number of core function steps required
          - number of variables
          - number of counterintuitive steps (requiring non-standard solutions)
          - number of contrary processes (requiring scoped/nuanced solutions)
        - abstraction (does it solve the same problem when framed on an abstraction layer above)
        - number of steps required, once work is standardized, & adjacence of steps required
        - how much work is required to convert to a particular problem format (route, combination, composition)
        - type/intent ranges/direction (of individual objects or composite stack)
        - similarity (how similar to a standard problem type, or how near to limits within a type dimension)
        - ratio of positive to negative outputs


    - solution decomposition function

    - solution aggregation function

    - make doc to store insight paths, counterintuitive functions, hidden costs, counterexamples, phase shift triggers

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


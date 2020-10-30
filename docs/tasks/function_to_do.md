# to do

  - de-duplicate logic
    - integrate problem_solving_matching.md & analysis_examples.md
    - integrate changes from solution_automation_analysis.py claims to repo
    - integrate example.py & workflow logic
    - integrate rules from diagrams to relevant documents

  - organize interface analysis definitions
  - add functions from workflows & analysis (to do list, questions answered, problems solved, interface definition & functions) as files in functions/ folder
    - resolve duplicate functions
    - organize into primary core functions & list sample parameters (like objects to identify for the identify function)
  - function to translate interface query logic into interface language (combination of core functions (find/build) & other core components)
  
## examples to make

  - finish dilemma example formats
  - query examples for use cases like:
    - lack of information stored (match problem of type 'information lack' with interface query 'check pattern interface for similar patterns')
    - query problem breakdown & integration diagram
    - calculating various different problem breakdown strategies first before executing normal query-building logic for each
  - give interface math examples, like standardization of all distinct components into their own interfaces, rather than within a system context
      - rather than framing the behavior of objects in a system, you can:
        - remove the assumption of the system limits forcing interactions
        - frame each object on its own interface (containing all its possible forms, variables, attributes, generators, cooperative contexts, etc)
        - compute the interactions of those interfaces
  - give example of generating problem types by applying structure
    - for instance, a common problem type is a mismatch/imbalance
      - by applying the 'mismatch' to the cost/benefit relationship, you get an 'inefficiency' problem type, which can be defined as a mismatch/imbalance between the cost & benefit, favoring the cost side (the negative object out of (cost, benefit), associated with problems)
  - add examples of system/object/rule/type change patterns
  - include example workflows with example problems
    - include example of how to generate other workflows (different starting/ending points & trajectories)
  - function test concepts: 
    - usage: application, expectation/intention convergence, permission, error, interaction
    - change: difference/similarity types (difference in value, similarity in position), update, initialization, association/relation, removal, move
    - state, storage (database, distributed sync, cache, data structure), data
    - organization (index, business logic)
    - priority/intent/requirement
    - variable (parameter, attribute, input/output, type)
    - logic (function, fit, completeness, validity, match, gap, connection)
    - assumption: legitimate assumption (context) or false assumption (logic gap)
    - cause, responsibility, dependency
    - scope/relevance, system/context, meaning/integration (system context fit), understanding (state of application relative to intended/optimal state, given problem/intent/tech understanding)
    - interface analysis answers 'how do these concepts interact in a typical implementation', and 'what is the graph of their optimal interactions', with output like:
      - sub-intent of lines of code should match intents of code blocks, functions, & other larger units & structures of code
      - cause, intent, & meaning of code should align (the cause of a function call should match the intents supported by the function and the meaning of the function fit in the system context)
      - workflows & other larger structures of code usage shouldnt produce contradictory cause/intent/meaning/related objects (calling two functions in isolation shouldnt contradict the meaning of calling those functions in a sequence, all other things being equal - otherwise its a potential vuln)

## diagram

    - diagram for workflow 1: 
      - function to determine relevance filter ('functions', 'required') from a problem_step ('find incentives') for a problem definition, to modify problem_steps with extra functions/attributes ('change_position') to be more specific to the problem definition ('find_incentives_to_change_position') for problem_steps involving 'incentives', so you know to use the function_name to modify the problem step if it's between the type 'functions' and the object searched for 'incentives'
    - add conceptual math interface query diagram
      - use lattice multiplication as standard example, other than core operations (add/multiply mapped to language, concepts like irreversibility/asymmetry mapped to math)
    - interface conversion, matching, starting point selection (applying structure, checking if relevant information is found)
    - diagram to document sub-functions of core functions with distortions
    - make diagram for dimension links higher than 3d that are depictable in the same network space
      - should show variables that impact other variables, the change rates of these relationships
      - overall impact should be calculatable from these relationships
      - should show similar movements for correlated variables
      - should show skippable/derivable variables (variables that can be resolved later than they normally are)
      - should show meta forces for overall trends in change rules (direction of combined variable forces)
      - should show limits of measurability & threshold metrics
    - structurize (apply structure to) definitions of objects specific to interfaces
      - example: info asymmetry is associated with an info loss in a particular direction between info types/formats, rather than just an info imbalance or mismatch
      - diagrams for specific concepts, core functions, concept operations (combine, collide, connect, merge, apply), ethical shapes
        - variable accretion patterns (how an object becomes influenced by a new variable, complex system interaction patterns, etc)
        - make diagram of potential matrix to display the concept
          - map parameter sets to potential matrix shapes 
        - finish diagrams for intent (more examples of matching structure with intent), cause (shapes & ambiguity), concept (evolution of concepts, networks, distortion functions)
        - diagram for argument
      - make a system layer diagram for each interface to allow specification of core interfaces & other interface layers (interface interface)
        - make a system layer diagram for structures to include layers of structures 
          (beyond core structures like curves, to include n-degree structures like a wave, as well as semantic output structures like a key, crossing the layer that generates info structures like an insight, a probability, etc)

# content/config

    - import insight history data to identify insight paths (info insight paths like 'lie => joke => distortion => insight', system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub')
    - define default & core objects necessary for system to function (out of the box, rather than minimal config necessary to derive other system components & assemble)
      - add default functions to solve common problem types
      - alternate utility function implementations have variation potential in the exact operations used to achieve the function intents, but there are requirements in which definitions these functions use because they are inherent to the system. For example, the embodiment may use a specific definition of an attribute (standardized to a set of filters) in order to build the attribute-identification function using a set of filters - but the general attribute definition is still partially determined in its initial version by requirements specified in the documentation, such as a set of core attribute types (input, output, function parameter, abstract, descriptive, identifying, differentiating, variable, constant), the definition of a function, and the definition of conversion functions between standard formats.
    - document time structures (concave time explaining compounding similarities up to a point of maximum concavity, a structure that can separate from the other space-times)
    - systematize your definitions of info objects, to include analysis that produces relationships of core objects like opposites to their relevant forms (anti-symmetry) in addition to permuted object states (asymmetry), such as an anti-strategy, anti-information, anti-pattern
      - organize certainty (info) vs. uncertainty objects (potential, risk, probability)
      - make doc to store insight paths, counterintuitive functions, hidden costs, counterexamples, phase shift triggers
      - add technicality, synchronization, bias, counterintuition, & certainty objects leading to inevitable collisions
        - the collision of compounding forces producing a phase shift
        - lack of attention in one driver and false panic in a second driver leading to a car crash given the bases where their processes originate
      - define alignment on interfaces (compounding, coordinating, parallel, similar, etc)
      - start with these info object transforms that filter the most info: opposite, invalidating, symmetric, core, aligning, boundary-breaking, phase shift activating, structure stabilizing, constant changing, converging
      - add core info objects (core strategies, core assumptions) so you can make a network of graphs for a system
    - concept analysis:
      - how new concepts (gaps in network rules) evolve once structure is applied to prior concepts 
    - interface analysis:
      - limitations of interfaces & how to derive them
      - how rules develop on stability & how foundations are connected & destroyed
      - explainability as a space limited by derivable attributes from data set & cross-system similarity
      - vertex definition & give examples (as an intersection/combination of interface variables, such as determining/description(compressing)/generative/causative/derivation variables), around which change develops
    - change analysis:
      - generated object change types
        - constant to variable
        - variable to removal of assumption in variable type/data type
    
    - research implementing your solution type (constructing structures (made of boundary/filter/resource sets) to produce substances like antibodies, using bio system stressors)
    
    - merge definitions into docs/tasks/implementation/constants/definitions.json

    - clarify/resolve terms that can be conflated: 
      - shape/structure
      - rule/test/metric/limit/threshold/boundary/state change/phase shift
      - intent/priority/motivation/incentive
      - method/function/rule/pattern (pattern is a sequence of specific objects)
      - path/route/trajectory/traversal/order/list/sequence
      - object/entity/item/component
      - type/class/category/group/subset
      - closed/isolated/independence/unique/orthogonal
      - model/perspective/filter
      - standard/interface/index/symmetry
      - dimension/variable/axis
      - space/system/context
      - perspective/filter/standard/index & relationship to variables/operations on the interface
      - filter vs. rule is a similar question to attribute vs. rule - sometimes one format is better based on the info you have, sometimes its worth it to transform the format
    
    - update links

'''


  - visuals
    FIG. 9. 'Problem formats, with matching solution formats of problem formats' illustrates an example of various problem formats & solution formats that match them. 
    FIG. 10. 'Problem-solution structure-matching: apply a solution function to a structure containing the problem to find specific solution structures for that problem' illustrates an example of matching a problem with a solution. 
    FIG. 11. 'Finding alternate solution formats that fulfill different metrics' illustrates an example of selecting a solution format that fulfills a solution metric. 
    FIG. 13. 'Causal structure-matching' illustrates a method of matching causal structures to a variable set.  
    FIG. 14. 'Design Interface Query' illustrates a method of assembling input information into structural meaning relevant to the input intent, using a structure containing information formats. 
    FIG. 15. 'Concept definition network' illustrates a network of related concepts. 
    FIG. 16. 'Alternate definition routes' illustrates a set of definition routes for a concept. 
    FIG. 17. 'Match structure for a definition of a concept' illustrates matching a structure to a concept. 
    FIG. 18. 'Intent-matching' illustrates matching intent to structure & vice versa.


  - this function can generate objects like problem-solving automation workflows, found in problem_solving_matching.md and /solution_workflows/*


  - functions to match & select a input-output format connecting format structure, like a format sequence or directed network 

          - An example problem-solving automation workflow for a problem like 'find an optimal implementation of an intersection' (shown in application 16887411 Figs. 1F - 1I), using the system/structure/concept interfaces. 
          1. Problem definition: determine possible match between the problem system intersection object and the system conflict object. 
          2. Standardize the problem to the system interface 
            - Apply the context of the default interaction defined for the intersection (agents crossing the intersection) 
            - Apply structures of possible matching objects in the system interface to the problem object, by applying the structure interface: 
            - components capable of interacting (they have a nonzero interaction space) can be formatted as a network 
            - the position overlap is an example of a tradeoff, so the 'subset' structure is applied) - this can be applied iteratively to check for structures that can be organized/optimized 
            - the antagonistic agent & diverging direction components are merged with the agent component, where the diverging direction structure is applied directly and the antagonistic agent component is implied by their mutual approach of the intersection 
            - the ambiguity system object is inferred by the match of the ambiguity 'unenforced rule' definition route, which matches the 'agent traversal sequence' intersection interaction attribute. 
            - Now the intersection's default interaction (agents looking to cross) is formatted as a network, and system objects like conflict (and its sub-components, patterns, objects, etc) have been matched & applied to the intersection interaction network. 
            - This is a structure of a problem type - 'find traversal sequence conflict resolution rule' - and given that it matches a known problem type 'resolve resource competition', it's likelier to be possible. 
            - The traversal sequence rule can be found by applying other agent & intersection attributes, looking for system & other interface objects like: 
            - irreversible changes (in case one agent will change the intersection in a way that prevents other people from traversing it, like burning a bridge) 
            - intents that are higher priority 
            - intent alignments (both agents have an incentive to apply social norms to maintain rule of law or trust, so their intents can be aligned to follow social rules to determine who traverses first, rather than building new rules to determine this). 
          3. This step identifies whether the output of the previous step creates information that is easily transformed into the solution metric, given the relevant objects/attributes/functions of the solution metric. Is it clear which agent goes first, or whether the intersection can be changed in a way that determines which agent goes first? 
            - If the solution metric 1 is fulfilled, the agents have no antagonistic agent attribute & there is no trade-off because no variance from a decision is allowed at the intersection. 
            - If the solution metric 2 is fulfilled, the intersection loses its position overlap attribute & the diverging direction attribute doesn't matter anymore, but it does have a decision function at the intersection. 
            - If the intersection object with the system interface is applied can be easily transformed into having one of the solution metrics fulfilled, that transformation can be considered a possible solution. 
    
  - this function matches a format with a target object, like a solution structure or intent
  - this function may identify a format structure, such as a sequence of formats, that connect the original input & target output formats
  - this function includes metrics like structure

      - problem-solution formats (shown in FIG. 9 (Problem formats, with matching solution formats) & FIG. 10 (Problem-solution structure matching)) 
        - a vector set is good for converting between problem-solution structures, like converting an inefficiency to an efficiency in a system 
        - problem shape-reducing vector set (where problem variables form the shape) is good for finding a function that reduces shape dimensions & size (like to form a summary), or a vector set to combine solution components in a way that fills the shape structure, if the solution format is a method to fill the problem structure rather than reducing the problem shape 
        - a route optimization problem has the solution format of a vector set between network functions/nodes (where nodes are states/problems/objects, etc) that is optimal in some way (hits a node/path, moves in a direction, minimizes cost of traversal, etc) 
          - with a network of states, the route can be a route between states with additional routes traversed within each state to convert to the next one (set of market states & trades to achieve a market intent) 
        - structure-matching can be a good format for finding an example, finding a reason, or finding a causal structure of variables for a prediction function 
        - an misalignment or mismatch (like an inefficiency, a conflict, or an information imbalance), where the solution format is the set of structures (which can be steps/vectors or applying a pattern or finding a structure in a network) necessary to correct the mismatch (minimize cost, align priorities, balance the information) 
        - abstract format of a query (break problem into information problem types and then the solution is a query of solutions for each of those solved problems) 
    

      - example structures that apply a concept are depicted in FIG. 17 (Match structure for a definition of a concept), which depicts structures of the 'distribution' and 'power' concepts. 
        - In the example 'distribution' function on the left of Fig. 17, a distribution function (that implements conceptual attributes like balance) is depicted, which may produce the Balanced Info Distribution example output from the Standard Info Distribution input.
        - In the example concept structures, such as the 'power' concept structures, on the right of Fig. 17:
            - a 'delegation' power structure is depicted, which indicates that information is sent to other entities for processing work.
            - a 'derivation' power structure is depicted, which indicates that no information is shared except derivation tools.
            - a 'delegation of derivation' power structure is depicted, which indicates that all entities delegate to entity with no caching/data retention power, only processing power.
    

       - example of possible definition routes for the concept of 'equality' are given in FIG. 16. Alternate definition routes 
        - FIG. 16 depicts an example of alternate structural definition routes for 'equality'.
            - For a concept like 'equality', the structural definition routes (standardized language map trajectories) may include:
                - interchangeable (similar enough to be usable for the same trajectories (functions/intents))
                - minimally distant (adjacent enough to be usable for the same trajectories)
                - efficiently convertable (convertible with sufficiently minimal work as to be usable for the same trajectories)
            - For another example, the definition routes for the 'power' concept may include:
                - structural definitions: alternatives, connection hub, input
                - concept-structure definitions: potential, change potential, change activation, truth source, truth access point/path (power being formattable as information)
                - concept definitions: freedom, independence
                - info definitions: energy
            - The alternate definition routes for the 'truth' concept may include:
                - ratio of information you need to ignore to make something seem true (low number of required conditions being an indicator of truth)
                - ratio of successful usages (repeated usability, or robustness)
                - ratio of fitting contexts (fit with other truths)

        - mapping intent to structure & vice versa is shown in FIG. 18 (Intent-matching) 
          - Fig. 18 depicts examples of matching operations between intent & structure.
          - In the 'Mapping Structure to Intent' section on the top left of Fig. 18, mapping intent to direction is depicted in a system as allowing the identification of different intents, given the general intent of the direction.
          - In the 'Identifying side effects of Intents' section on the top right of Fig. 18, an example of deriving intents in a system - intents that have side effects - is depicted.
              - The system limits may force someone prioritizing a priority to move in certain directions that they ordinarily would not if left to make their own decisions in a vacuum. 
              - They start from a selfish priority, moving in the direction of being uncriticizable and building functions to enable that intent, and by the system they're operating in, they're forced to move in other directions (making a gesture of charity, copying agent with priority of improving functionality of other nodes), while still having the same intent.
              - The agent prioritizing that priorit will have pivot/angle/rotation functions/concepts, and their decisions will be buildable with those functions. The agent prioritizing improving other nodes' functionality will have cooperation, sharing, problem-solving functions and their decisions will be buildable with those functions.
              - This is an example of how different intents can not only have the same output (arriving at the same end node), but a similar/overlapping trajectory at various points, while still leaving traces of different intents in their side effects (traces such as functionality developed to serve different intents, at different stages of development).
          - In the 'Intents mapped to structure' section on the bottom half of Fig. 18, examples of structural input intents are depicted on the left, which can adjacently support example structural output intents on the right.
          - For example:
              - Intent 1A (Unenforced equal growth) and intent 1B (Enforced equal growth) may support intents like intent 1C (See which entity gets to the corner first) and intent 1D (Create the emergent entities).
              - Intent 2A (Inject variance in growth inputs) and intent 2B (Inject variance in growth inputs) may support intents like intent 2C (Create field of potential for emergent entities to grow, either within an existing or new boundary) and intent 2D (Create interaction space on emergent entity layer).
              - Intent 3A (Inject variance in state (position after a process)) and intent 3B (Incentive to move toward corners decreases, leading eventually to corner erosion) may support intents like intent 3C (Create temporary interaction layer as needed to resolve question of which entities emerge or create their functions, then dissolve it by switching their positions).
              - Intent 4A (Create evenly distributed growth incentives once corner objects & functions develop) and intent 4B (Remove square boundary & let all functions & objects develop new interaction patterns in outer circle) may support intents like intent 4C (Developing new layer functionality) and 4D (Apply a standardizing, transforming, or reducing filter (square boundary) to a system).
    
        - FIG. 8 contains examples of problem types & associated example structures.
          - On the left of FIG. 8, structures for core problem types standardized to various formats are depicted.
          - An example Info Asymmetry problem structure is depicted in FIG. 8, which is an imbalance in information (when depicted in an information format) or position (when depicted in a system format).
          - An example Intersection problem structure is depicted in FIG. 8, which indicates a problematic intersection, like vectors that shouldn't interact.
          - An example Conflict problem structure is depicted in FIG. 8, which indicates a conflict structure, such as the problem of selecting between alternatives, or the problem of conflicting vector like intents
          - An example Independence problem structure is depicted in FIG. 8, which indicates an independence structure, such as orthogonal directions of change.
          - An example Dependence problem structure is depicted in FIG. 8, which indicates an example dependence structure, such as where one attribute is determined by another which is used as a standard.
          - An example Inequality problem structure is depicted in FIG. 8, which indicates an example inequality/mismatch structure between a solution (like a square shape) and a solution format (like a circle format).
          - An example Information Inequality problem structure is depicted in FIG. 8, which indicates an example structure of an inequality of information, when formatted on the structural-information interface, rather than being formatted on a structural interface one layer of abstraction above it.
          - An example Extra Dimension problem structure is depicted in FIG. 8, which indicates the structure of extra dimension added by integrating a circle across a vertical dimension.
          - An example False Limit problem structure is depicted in FIG. 8, which indicates an example structure of a limit, such as a corner organizing change in a direction.
          - On the right of FIG. 8, structures of problem types that may be generated with (operations like 'combine') are depicted.
          - An example Organization problem structure is depicted in FIG. 8, which indicates an example organization structure, such as finding the right interaction layer to frame an interaction on, or resolving a mismatch/misalignment/imbalance is an organization problem space, where there are clear optimal structures for a certain interaction.
          - An example Inefficiency problem structure is depicted in FIG. 8, which indicates an example inefficiency structure, such as navigating up an abstraction layer when there's no reason to do so.
          - An example False Assumption problem structure is depicted in FIG. 8, which indicates an example false assumption structure, such as starting from the wrong starting point, or assuming there is a required starting point, or using over/under-restrictive limits.
          - An example False Similarity problem structure is depicted in FIG. 8, which indicates an example false similarity structure, such as similar shapes that can develop with independent causes & contextual impact (for example, the appearance & behavior of a square between circles vs. an actual square).

      - on the problem index, problems are mapped to structure, once problems have been converted to an information problem, which has a clear mapping to the structural interface 
        - problems can be framed as info problems (missing info, conflicting info, unconnected info, mismatches, imbalances, asymmetries) 
        - different problem types have different default problem shapes 
            - example problem type shapes: 
                - finding a prediction function can be framed as an optimal path in a network of variable nodes 
                - conflicts can be vectors with different direction or which overlap 
                - a misalignment problem has at least two vectors differing in direction, where the optimal alignment is calculatable or at least the alignment is clearly improvable 
                - a variance injection problem has a opening in a closed system 
                - an asymmetry has an uneven resource distribution 
              - if a problem has a misalignment problem and a variance injection problem, the problem shape can have both shapes in isolated analysis, or they can be merged, applied, added, mixed, intersecting, or combined in another way 
            - example solution shape for problem shape: 
              - for a misalignment problem, the solution shape would be: 
                - a vector aligning them 
                - another adjustment to the system that makes the existing misalignment a correct alignment 
                - a combination of the two 
              - for a variance injection problem, the solution shape would be: 
                - an object (resource, function, constant) to close the opening in the system 
                - an object to prevent further variance injections 
              - for an asymmetry, the solution shape would be: 
                - an optimal transport operation set to distribute the resource optimally according to the metric of symmetry 
        - this analysis involves: 
          - identifying the given problem & solution target structures in the problem space & the related problem network, so the problem & solution can be visualized 
          - identifying & anticipating problems in a system, which optionally includes identifying problem structures (inefficiencies, conflicts, etc) that exist or could emerge 
            - example: in the bio system, DNA regulation functions don't prevent pathogens from injecting DNA or mutations from occurring, so if the program derives the concept of a pathogen or mutation without already having that definition available (using core system analysis), the program could predict that the current DNA regulation functions wouldn't be able to offset the changes exacted by those concepts & the program could predict problems of DNA disregulation in the bio system before they occur 

        - each format is better for different information, problem types/formats (with varying structure in the problem definition) & solution intents, but if the user has a particular required solution format, they may need to translate a sub-optimal problem format into one associated with that solution format 
        - each format involves a standard form like a set of vectors (which may represent a set of database/interface queries or insight paths, info objects like questions/insights/related problems, decisions/actions, causes/explanations, steps like removal/addition of variables, directed structures like distortions/intents, etc) which may be applicable in the interface network to retrieve/connect information, or in the problem space to reduce a problem shape, move around problem components to change the problem, or traverse a route in the problem network system (not necessarily the network of related problems, but the problem framed as requiring a solution route within a network) 


        - function to match structures with coordinating formats, as shown in FIG. 9 with an example of matching problem formats with solution formats.
          - FIG. 9 depicts an example of formatting a problem (like finding a prediction function for a data set) in a different format.
              - Problem format 1 depicts an example problem format such as: find core generators (triangle parameters of connective functions) of prediction function (dotted line) in system that can also generate other functions.
              - Solution format 1 depicts an example solution format that coordinates with problem format 1, such as: core generative vectors.
              - Problem format 2 depicts an example problem format such as: find system to generate prediction function.
              - Solution format 2 depicts an example solution format that coordinates with problem format 2, such as: directed system network generating prediction function.
              - Problem format 3 depicts an example problem format such as: find prediction function (dotted line) in system.
              - Solution format 3 depicts an example solution format that coordinates with problem format 3, such as: base function network trajectory.
              - Problem format 4 depicts an example problem format such as: find causal directions in variable network.
              - Solution format 4 depicts an example solution format that coordinates with problem format 4, such as: directed causal variable network.
              - Problem format 5 depicts an example problem format such as: find sub-functions or alternate routes for a function.
              - Solution format 5 depicts an example solution format that coordinates with problem format 5, such as: vector sequence (to convert into another problem, reduce problem shape, fit a problem structure, fill problem shape,
     generate the function, etc).
              - Problem format 6 depicts an example problem format such as: find sub-intents linking a start & end node.
              - Solution format 6 depicts an example solution format that coordinates with problem format 6, such as: intent network trajectory.
              - Problem format 7 depicts an example problem format such as: format a function as a filter sequence.
              - Solution format 7 depicts an example solution format that coordinates with problem format 7, such as: filter network trajectory.
              - Problem format 8 depicts an example problem format such as: find problem types of a function.
              - Solution format 8 depicts an example solution format that coordinates with problem format 8, such as: problem type network trajectory.
              - Problem format 9 depicts an example problem format such as: find-patterns generating or generating an alternate to a function.
              - Solution format 9 depicts an example solution format that coordinates with problem format 9, such as: pattern network trajectory.
              - Problem format 10 depicts an example problem format such as: find distortion functions & bases generating a function.
              - Solution format 10 depicts an example solution format that coordinates with problem format 10, such as: find distortion functions & bases generating a function.
          

          - example logic of function to find alternate solution formats in FIG. 11 (Finding alternate solution formats that fulfill different metrics) 
            - As shown in FIG. 11, different solution formats fulfill different attributes of the solution.
            - For example, these solutions fulfill the route cost minimization aspect of the solution, but it doesn't enhance rewards of the route, if that's a solution metric determining whether a route is optimized, which can be determined with attribute-assessment functions like determining whether a structure matches a particular concept like 'distribution' or 'equality' or 'organization', which may be conceptual solutioin attributes. This type of function does structure-matching logic like that in FIG 18.
            - Solution format 1 depicts an example specific solution implementing an 'application' of the general solution of 'cost reduction' in an example solution format, like applying a 'system structure change' format (meaning structure).
            - Solution format 2 depicts an example specific solution implementing an 'addition' of the general solution of 'cost reduction' in an example solution format, like adding a 'system-wide cost reduction function' format.
            - Solution format 3 depicts an example specific solution implementing a 'find' of the general solution of 'cost allocation' in an example solution format, like finding an 'optimal cost/benefit allocation, given a particular required path' format.
            - Solution format 4 depicts an example specific solution implementing an 'application' of the general solution of 'cost reduction' in an example solution format, like applying a 'system function distribution (removing incentivized directions or changes)' format.
            - Solution format 5 depicts an example specific solution implementing an 'application' of the general solution of 'cost reduction' in an example solution format, like applying a 'resource position change' format.
            - Solution format 6 depicts an example specific solution implementing an 'application' of the general solution of 'cost reduction' in an example solution format, like applying a 'path shortening' format.
            - Solution format 7 depicts an example specific solution implementing an 'application' of the general solution of 'cost reduction' in an example solution format, like applying a 'resource re-use' format.
            - other example logic to find alternate solution formats includes:
                - how to identify alternative solutions that would be interchangeable with a solution in various contexts (like for different solution metrics): 
                - in other words, how to translate 'find optimal route fulfilling a metric' to an alternative interchangeable solution that makes the initial problem trivial to solve 'find system-wide cost-reduction function that makes system routes equally costly', at which point the original problem's solution is 'any route'. 
                - we are looking for ways to invalidate the problem (generate an adjacent object to act as a proxy or replacement for the solution, generate the solution automatically, change the system structure so solving the problem isn't necessary, etc) rather than generate a specific solution (like how 'trial & error navigation of all possible routes' is a specific solution) 
                - inference sequence using definitions & problem definition: 
                  - check definition: 'route' is defined as 'a path between nodes in a network' 
                  - standardize definition: 'optimal' can be removed because it means the same as 'fulfilling a metric' but adding 'fulfilling a metric the most' to translate it to the standardized form 
                  - find definition (of metric) 
                  - apply logic specific to metric definition, or general information-generating logic like a transform that doesn't change meaning in a context 
                  - if the metric is the general 'minimize cost' metric of an optimization, apply a transform ('abstract' or 'expand/apply/distribute' or 'change specificity attribute value to its extreme value') that doesn't change the meaning, to produce:  
                    - 'minimize system costs' (which doesn't prevent minimize the original cost so it doesn't change the meaning in an invalidating way) 
                  - inject new version into original problem definition: 
                    - 'find route that minimizes system costs' 
                  - check if definitions match logically: a 'route' wouldn't necessarily produce a system cost-minimizing effect 
                  - if they don't match, apply transforms until they match: 
                  - abstract 'route' to get 'function': 'find system cost-minimizing function' 
                  - check problem definition for extra information:  
                  - the intent of the original problem was to minimize cost of a particular route, a problem that would be invalidated if all routes were equally costly; if we found a 'system cost-minimizing function' that minimized system costs, they might become equally costly, thereby invalidating the problem (invalidating it being one way of solving it), producing: 
                    - 'find a system cost-minimizing function that makes system costs equally likely' 
                - different structures fulfill different structural solution metrics 
                  - if 'cost' is the metric, measured by total distance traveled, that is clearly different across the various solution formats of FIG. 11 (Finding alternate solution formats that fulfill different metrics). 
'''
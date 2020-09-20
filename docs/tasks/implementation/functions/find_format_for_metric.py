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


      - a workflow to automate problem-solving is an interface traversal that can be applied to any problem

      - the workflow inherent to this tool (to match a problem with a solution) uses the problem information as the default interface. The overall workflow of this tool can be built with an interface query:

        - find problem type & format the problem as a combination of information problem types (information (problem, assumption) interface, type interface), as well as any related problems (information (problem) interface, pattern interface, and the change interface to generate related problems if none are logged)
        - find solution requirements (structure interface where requirements are limits/thresholds)
        - apply a directed graph (structure interface) of various information formats (interface interface, information interface), positioned in the sequence likeliest to find the missing information to solve (structure interface, similarity concept interface)
          (if its missing cause information, standardize to the causal interface or generate information about likely causes from other interfaces like the pattern interface or generate adjacent or proxy information to cause information like a set of tests to filter out non-cause information or generate interaction pattern information to predict which objects will interact, generating causes)
        - if the information formats applied dont reveal enough info, apply combinations of the formats (structure interface, core interface)
        - if no solution space can be identified or reduced, return the queries and the problem & problem space metadata

      - these are very abstract insight paths (a cross-system, insight-generating sequence) that can generate solutions automatically

      - workflow variables include:

        - starting point of the analysis (which interface the query starts from)
        - structures relevant (which structures or type of graphing method to use)
        - intent (create a prediction function, reduce solution space, compare solutions, or match problem with solution)
        - core abstract function represented (is it a find method, an apply method, a combination)
        - formats & structures used (object model, interface query)

      - if the problem is 'finding a structure that matches conceptual priorities like strength', that can clearly begin on the concept-structure traversal if information required for that traversal already exists in the problem definition or derived metadata

        - concept-structure interface traversal (a multi-interface traversal linking the concept & structure interfaces, so a target concept combination/set/path or target structural attribute can be achieved with structures like filters/limits/functions that adjust the origin structure until it matches the target structural attributes or concepts)

        - or you can standardize to the intent interface which is particularly effective at linking other interfaces (find intents & intent structures that fulfill the 'strength' attribute, and structures matching those intents)

      - other workflows can be derived given alternate traversals that can generate information (like how causation, information formats, functions, and intent can generate structure information), given existing information

        - problem-solution interface traversal: sometimes a sufficient solution may be already stored in the solution table (solution being an information object) and the way to solve the problem is formatting it correctly or identifying its type correctly so that solutions for that format or type can be queried & applied as-is, the most basic traversal type

      - these workflows can be generated with new interface combinations or interfaces, if each interface in the sequence can add information required to solve the problem

      - occasionally an interface will be sufficient on its own, if the problem is already pre-structured

        - for example, the function interface may be enough to find the right sequence of functions, if the function metadata includes input/outputs and there are no ambiguities to resolve, meaning this solution is a simple query to match inputs/outputs, where the final output is the intended goal of the query

      - problem-solving automation workflows

        - these workflows apply various interfaces & analysis types, and can be applied to any problem

          I. Filter problem definition until it matches solution structure (using definition & standardization, applying increasing limits/filters/transforms until problem & solution match)
            - this applies structures such as limits to fulfill solution intents iteratively
            - for example, when deriving the structural implementation of the concept of cryptocurrency, applying a 'group' structure to the 'transaction' object creates the 'transaction ledger' object, which fulfills sub-intents of the solution ('access related information' and 'connect related information') and reduces a problem sub-component (the 'information imbalance' problem type between receiver & sender), a problem type which has related solution functions (like 'distribute information evenly')

          II. Solve problem with structure fitting (adapt probable solution structures to match problem definition)
            - this starts with core, probable, or difference-maximizing structures and applies additional structures until one is found that fulfills solution metrics
            - for example, to find a prediction function for a data set, 
              - the core functions would be common base/distortion (patterns of change), component (core patterns of prediction functions), approximation (generalizing functions), & adjacent functions (functions within a range of accuracy) of prediction functions
              - the probable functions would be functions in between the most accurate and the most generalized function versions
              - the difference-maximizing functions would be the most different possible functions (a circle function to explain a high-randomness data set, multiple step-functions to explain a continuous function, a linear function, etc) to start by examining the most different possibilities and eliminate them with additional filters

          III. Transforming problem into query of solved problems (using most adjacent solution formats)
            - converting the problem into a structure (set, sequence, network) of solved problems (like distributing power, resolving imbalances, etc), and then traversing that structure if multiple alternatives are found
            - this method can take the form of a simple database query ('fetch & apply solutions, including insight paths, for this problem type' or 'find the fewest question jumps that can solve the problem') in its most basic form, if the problem is an existing solved problem
            - for example, finding a prediction function is a set of problems like 'decide on metrics & threshold values', 'decide on complexity', 'choose between opposing sides of tradeoffs', 'generalize', 'identify outliers', 'identify noise', 'account for error types like corrupt/incorrect/unrecoverable/incentivized or improperly formatted/standardized data', 'account for alternate explanations', 'account for correlation between independent variables', 'account for incorrect data types', 'account for missing information', etc

          IV. Solve problem with solution function generation & selection (optionally with pattern/intent-matching)
            - this uses the function interface to identify useful metrics to select functions to begin with when searching for a function to solve a problem (like 'calculate x') which can involve function metadata like identifying hub functions, functions that move in a direction, etc
            - this analysis involves identifying/deriving decision rules to identify alternate/interchangeable solution functions & select between solution functions
            - an example would be deciding when to select a solution function you have indexed in the solution table and when to look for a new function, or update the existing function

          V. Solve problem with conceptual query (iterate through conceptual paths & match with structural path)
            - start with required concepts (but not their optimal relationships in a concept combination) such as 'trust', 'distribution', 'power', and find a structure that arranges those concepts in an optimal way that fits the solution requirements

          VI. Derive conceptual query & match with structural path
            - start by finding the concept combination required ('trust generated from equal distribution of power'), then find matching structures of that specific combination
          
          VII. Vectorize problem/solution space & match intents
            - this involves framing a problem as a structure like a directed network to convert it to a route optimization problem, where the assumptions are inputs, the intents are outputs, & the interim structures can be a mix of interface objects like concepts
            - if you have a general problem definition like 'find a function that calculates x', you would arrange input information on one side, the function on the other side as the goal, and identify related concepts, patterns, & other objects to that intent to connect them, given the definition routes of those terms
            - this can also involve formatting the problem as a set of questions (sub-problems of an information asymmetry problem type) to answer that map from starting information to target information

          VIII. Mapping variance objects in problem space systems as starting solution space
            - framing a problem in terms of variance (on the potential interface) makes it clear which objects are important, given variance/potential structures like interaction spaces, inevitable interactions, variance gaps, etc
            - the high-variance objects in the 'find a prediction function' problem are the error types, assumptions, change types, data set concepts (like how the concept of 'survival skills' is relevant & inferrable in the titanic survival data set), and variation across data sets, so a good solution would integrate functions to identify & handle those objects

          IX. System snapshot (interface/symmetry/vertex) derivation
            - finding the specific interfaces & related objects in a problem system to frame a problem efficiently
            - in the bio system, this would mean automatically identifying the genetic configuration, protein structure, immune memory, and brain interfaces as important determinants of the system
            - in a function set like a code base, this would mean automatically identifying the function type interface (to identify function types like boundary/change rules for efficient function indexing) and the intent interface as important for indexing functions
            - in the 'find a prediction function' problem, this would identify the concept of 'average' as an important symmetry balancing various tradeoffs, identify independent variable probability distributions as an important vertex in predicting the behavior of dependent variables, and identify the cause interface as an important interface for understanding, which is a proxy for a prediction function, the potential interface as a tool for understanding variable dynamics (how sources of variance gather into variables), and the system interface as a way to derive the range of possible prediction functions (how variables gather in complex systems, and how the range of prediction functions is whichever prediction functions are possible between those variables as system components, given system structure, so you should start with the vertices of that range - meaning a set of difference-maximizing functions in that range)

          X. System derivation
            - this is a more comprehensive format that allows quick application & identification of system objects (alternates, efficiencies, incentives)
            - for example, identifying known system objects for the 'find a prediction function' problem would mean identifying incentives in data collection (collect small sample, collect representative sample), efficiencies in calculating prediction functions (some sections should be treated as potential fields, where a network is embedded in place of a function section, to indicate decision logic or alternate functions accessible with additional information, if a predicted value is requested from that section of the function), false similarities (like the apparent similarity between two variables being correlation rather than a direct relationship), opposites (like neutralizing variables), and other core system objects

        - other problem-solving automation workflows would start with different interface traversals & use different origin & target structures (such as:
          - designing interface trajectories
          - generating new info object layers to use as interfaces or systems (combine perspective & potential to generate a potential-perspective field, combine problems & markets to create a market for problems, combine platforms with platforms to create a platform to sell platforms, combine variables and networks to create variable networks, combine variables & risk to identify variable development sequences))
          - finding structures (like insights such as 'break a problem into sub-problems & aggregate solutions' or 'apply filters until the problem space is a solution space, then repeat until the solution space is a solution') that when applied to a problem, create a clear format/structure sequence linking the problem with a solution
            - a specific example is 'problem vectorization' as mentioned above in VII: finding specific interim formats linking a problem & solution format (such as the structure of concepts/interfaces that would link variables with a prediction function) & applying structures to create that format sequence (like a directed network)


  - functions to match & select a input-output format connecting format structure, like a format sequence or directed network 

    - example: find structure for an object/function (similar variance, difference from related objects, intents/priorities, causes, potential ranges, etc)

        - An example problem-solving automation workflow for a problem like 'find an optimal implementation of an intersection' (shown in application 16887411 Figs. 1F - 1I and Fig. 14), using the system/structure/concept interfaces. 
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


    - example of finding a structure
        
        - for input intent task 'correct inequality (imbalance/mismatch) in a structural attribute (value, definition, direction, function, intent)', find structures that:
          - align objects (resolve conflicting objects like conflicting intents)
          - match objects (equate unequal objects like incentives/requirements, or expectations/intents, or opportunity/ability)

        - correct imbalance (direction, resources, functionality, intent)
        - find combination (build) of structures (filters, functions, objects, sets, concepts, intents)
              - example: find combination of structures to build a prediction function for a data set
                  - combination of filters: which filters should be applied to reduce solution space, find relevant objects, or find steps to produce or build the solution
                  - combination of functions: which functions are possible solutions to a prediction function problem ('take an average metric of the function set predicting x% of the data with less than y terms')
                  - combination of objects: 'average', 'function set', 'term count', 'accurate prediction ratio'
                  - combination of sets: which objects should be grouped (function set, term set)
                  - combination of limits: which assumptions are required and which are flexible
                  - combination of matches: which objects need to match, to what degree (function terms and data), and which set of reductions works the best with a given set of expansions
                  - combination of imbalances/asymmetries (questions): which metric sets are the best filters for a given problem
                - you could graph the problem/solution with any of those objects, if they supply all the info needed to frame the problem - navigating on the filter or mismatch section of the network may be faster given the commonness of those objects
              - example: find resource combination to resolve a lack of another resource
                - problem cause: missing resource or its alternatives, or missing resources to generate it or its alternatives, or dependence on resource or its alternative
                - solution 1: create missing resource
                  - navigate up causal stack: find combinations of functions & objects that generated it
                  - navigate sideways: find alternatives or find alternative combinations to generate it
                - solution 2: invalidate dependence
                  - navigate up causal stack until dependence cause is found: find combinations of functions & objects that generated dependence
                  - navigate sideways: find functions to invalidate dependence (generate resource) or correct problem (imbalance, lack, mismatch) causing dependence
                - solution intents 1 & 2 have a 'generate resource' intent in common, which fulfills both solution intents - so if the intent changes between them, the solution involving generating the resource may cover the next problem iteration too, or the intent that invalidates the problem may prevent future iterations
        - find sequence (route) of network nodes representing (steps, positions/states, sets, intents, etc)
              - find sequence of questions to solve a problem
                - example: what is the probability of event x happening
                    - what are the shapes & patterns of errors in assumptions, causes, & selection/generation of methods? (what ratio of incorrect are people with each additional assumption, given the level of certainty per assumption & complexity of problem)
                    - what are the consequences of not correcting those errors? (how wrong can the predictions be)
                    - what is the usual correct assumption pattern once false assumptions are corrected, and whats the insight path to transform the incorrect to the correct version?
                    - whats the rate of discovery of new sub-systems, objects, or variables in related systems like physics
                    - whats the likelihood we created certainty out of what ratio of our assumptions (over-relying on assumptions to make them conditionally true)
                    - whats the possible causative impact of measurements & application of specific knowledge on other systems
                    - whats the possibility that every rule we take as certain is a false similarity, false correlation, or other false object

    - example of finding structures in information formatted as a system

        - find objects, sub-interfaces & concepts in a system
          
          - example: for a password system, relevant basic objects & concepts include:
            - 'memory access patterns' as retrieving a memory has patterns just like retrieving a password from browser storage has patterns or typing someone else's password has patterns
            - 'memory limits' meaning that a memory has more limits on memorable passwords than browser stored passwords or an experienced hacker
            - 'augmentation' meaning password salts
            - 'validation' meaning hash check patterns
            - 'generation' meaning the rules used to generate different types of password (like how passcodes typically have repeated patterns) & the enforced rules to limit passwords (requiring special char types that are usually positioned together if manually generated)
            - 'reverse computation requirements', meaning the cost of rainbow tables and other tools to reduce computation time
            - these objects can be generated with standard system objects/functions/attributes (limits, patterns, core operations like reverse and high-level operations like generate/validate) applied to password system objects/functions/attributes (password rules, char limits)
            - identifying interface objects in a security problem space system:
              - identify contexts (default permissions, information-event-function sets) likelier to incentivize exploits
                - identify adjacent preceding contexts or objects of exploits to prevent exploit contexts from developing
              - identify structures of systems enabling exploits to apply more security or analysis to similar structures
                - identify intersections (edge conditions) or sets (anomaly chains) likely to be exploit opportunities or allow them to develop
                - identify malicious intents that look like positive intents (false similarities)
                - identify function sequences that have gaps in enforcement/injection points, or can be called for malicious purposes because the entire chain is abstract or the pieces being tested are abstract/neutral
                  - identify functions that can be called outside of intended justified contexts
              - identify distortion functions & approved ranges of distortion structures (like combined distortions, distortion sequences, etc)
              - identify positions in a system where movement toward malicious or neutral intent positions is possible/incentivized
              - identify system objects & concepts (expectations vs. intents, side effects, errors, potential, rule enforcement, assumptions, access, randomness, request patterns/sets, false/accidental similarities/differences, pre-approved workflows & request sets) relevant for finding exploit opportunities
              - identify specific objects relevant to exploit opportunities for a system
    
  - this function may identify a format structure, such as a sequence of formats, that connect the original input & target output formats
  - this function includes metrics like structure
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


  - this function includes metrics like structure

      - problem-solution formats (shown in FIG. 9 (Problem formats, with matching solution formats) & FIG. 10 (Problem-solution structure matching)) 
        - a vector set is good for converting between problem-solution structures, like converting an inefficiency to an efficiency in a system 
        - problem shape-reducing vector set (where problem variables form the shape) is good for finding a function that reduces shape dimensions & size (like to form a summary), or a vector set to combine solution components in a way that fills the shape structure, if the solution format is a method to fill the problem structure rather than reducing the problem shape 
        - a route optimization problem has the solution format of a vector set between network functions/nodes (where nodes are states/problems/objects, etc) that is optimal in some way (hits a node/path, moves in a direction, minimizes cost of traversal, etc) 
          - with a network of states, the route can be a route between states with additional routes traversed within each state to convert to the next one (set of market states & trades to achieve a market intent) 
        - structure-matching can be a good format for finding an example, finding a reason, or finding a causal structure of variables for a prediction function 
        - an misalignment or mismatch (like an inefficiency, a conflict, or an information imbalance), where the solution format is the set of structures (which can be steps/vectors or applying a pattern or finding a structure in a network) necessary to correct the mismatch (minimize cost, align priorities, balance the information) 
        - abstract format of a query (break problem into information problem types and then the solution is a query of solutions for each of those solved problems) 
    
        - ways to format a problem:
          - attributes that differentiate problems that are shared with possible solutions
          - mapping intent to direction and assessing progress by movement in that direction
          - networks with clusters & other structures representing decisions
          - system layer graph representing possible steps
          - function sets mapped to sequences given a metric like progression toward goal
          - mapping change types to dimensions and graphing/calculating dimensions where change types change (an aggregate, interface, or deciding dimension where change type is uncertain but not random)
          - using a layered graph to visualize change of different types/metrics built on a symmetry (vertical axis if horizontal sections are split)
          - mapping language to structure directly ('find' maps to a set of vectors leading from a node indicating possible start positions, with option to use core function vectors to reach target node)
          - a trajectory between low-dimensional problem graphs where each graph is a decision step, and attribute sets & problem of similar type occupy a similar position on an axis depicting all the graphs traversed
          - a metric like size of variable interaction space mapped to length/area/volume to indicate how much of the problem is left, and a metric like number of variables mapped to number of sides of the shape to graph the problem according to structural metrics


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
              
'''
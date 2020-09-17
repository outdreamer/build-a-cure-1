'''
    - definition:
      - on this index, problems are mapped to structure, once problems have been converted to an information problem, which has a clear mapping to the structural interface
      - problems can always be framed as info problems (missing info, conflicting info, unconnected info, mismatches, imbalances, asymmetries)
        - finding a prediction function can be framed as an optimal path in a network of variable nodes
      - once you frame a problem as an info problem, you can map info to structure:
        - conflicts can be vectors with different direction or which overlap
      - this involves 
        - identifying the given problem & solution target structures in the problem space & the related problem network, so the problem & solution can be visualized
        - identifying & anticipating problems in a system, which includes identifying problem structures (inefficiencies, conflicts, etc) that exist or could emerge
          - for example, in the bio system, DNA regulation functions don't prevent pathogens from injecting DNA or mutations from occurring, so if you derive the concept of a pathogen or mutation without already having that definition available (using core system analysis), you could predict that the current DNA regulation functions wouldn't be able to offset the changes exacted by those concepts & you could predict problems of DNA disregulation in the bio system before they occur
      - all problem-solving automation methods have a variance assignment, allowing for variation to be explored in a certain location 
        - you can either map problems to fit that structure or design new automation methods based on the variance gap necessary to solve a problem

    - objects (problem, solution, problem/solution space/network) 

    - structures:
      - problem-solution formats (shown in FIG 9 (Problem formats, with matching solution formats) & FIG 10 (Problem-solution structure matching))
        - a vector set is good for converting between problem-solution structures, like converting an inefficiency to an efficiency in a system
          - problem shape-reducing vector set (where problem variables form the shape) is good for finding a function that reduces shape dimensions & size (like to form a summary), or a vector set to combine solution components in a way that fills the shape structure, if the solution format is a method to fill the problem structure rather than reducing the problem shape
          - a route optimization problem has the solution format of a vector set between network functions/nodes (where nodes are states/problems/objects, etc) that is optimal in some way (hits a node/path, moves in a direction, minimizes cost of traversal, etc)
            - with a network of states, the route can be a route between states with additional routes traversed within each state to convert to the next one (set of market states & trades to achieve a market intent)
        - structure-matching can be a good format for finding an example, finding a reason, or finding a causal structure of variables for a prediction function
          - an misalignment or mismatch (like an inefficiency, a conflict, or an information imbalance), where the solution format is the set of structures (which can be steps/vectors or applying a pattern or finding a structure in a network) necessary to correct the mismatch (minimize cost, align priorities, balance the information)
        - abstract format of a query (break problem into information problem types and then the solution is a query of solutions for each of those solved problems)

    - concepts (anomaly, outlier, conflict, inefficiency, mismatch, inequality) 

    - attributes: 
      - number of problem-causing variables/solution metrics fulfilled 
      - complexity: (number of core function steps required, variables, differences/inefficiencies, counterintuitive steps (requiring non-standard solutions), contrary processes (requiring scoped/nuanced solutions)) 
      - abstraction (does it solve the same problem when framed on an abstraction layer above) 
      - number of steps required to create problem from stable system base state, once work is standardized, & adjacence of steps required 
      - how much work is required to convert to a particular problem format (route, combination, composition) 
      - structure of problem types causing or forming the problem (number/position of information asymmetries, resource limits) 
      - structure of information objects in the problem (decision points, variance sources, unanswerable questions of the problem, the structure of causes generating the problem if known) 
      - type/intent ranges/direction (of individual objects or composite stack) 
      - similarity (how similar to a standard problem type, or how near to limits within a type dimension) 
      - ratio of positive to negative outputs (problems solved vs. caused) 
      - inevitability vs. agency of problem cause 
      - agency involved in the problem 
      - problem types (examples shown in FIG 17. Problem Types)
        - dependency/fragility 
        - mismatches 
        - conflicts 
          - intersection/collision 
          - comparison 
          - coordination 
          - competition 
          - conflicting direction/misalignment 
          - incentives/intents 
          - expectations/potential 
          - requirements/enforcement 
          - intent mismatch, like an unintended use (involves integrated third party tech not under review), like unintended side effects: whether it's a closed system or leaks variance (example: pre-computation, memory access, or process re-start event) 
          - misidentification  
            - incorrect structure (metric, information position, or organization/format) 
        - imbalances/inequalities (misdistribution of resources) 
        - inefficiencies (unmaximized benefit/cost ratio, such as unnecessary complexity/work) 
        - gaps 
          - missing information 
          - ambiguity (example: ambiguous alternatives) 
          - gap in rule enforcement 
          - gap in boundary (example: leaks (variance, resource/info), and injection points (assumptions/variance/control/randomness)) 
        - limits, such as enforced rules, or limited resources/functions 
        - specific problem types:
            - malicious alternative route to get same output
            - legitimate/alternative route to get malicious output

    - related objects: 

      - solution types:
        - problem-metadata solution: evaluating problem metadata to evaluate metrics like problem-solving postponement
        - generative solution: solution that generates solutions
        - solution framework: provides starting point & structures for solutions to be built in/with
        - problem decomposer: solution that reduces a problem's root causative (as opposed to just varying) parameters
        - interim solution: clearly suboptimal solution while optimal alternative is built
        - solution query constructor: solution that builds new solutions out of known solution types (existing structural solutions or core functions)
        - structure-finding/fitting solution: solution that assigns a structure to information or matches the gaps/limits in a problem structure to neutralize them

      - questions 
          - what are the problems (inefficiencies, conflicts, mismatches) in this system 
          - what solutions are associated with this problem type 
          - what problems are related to this problem 
          - what problems will develop in this problem space system 
          - what is the probable cost of solving this problem 
          - what is the adjacent format of this problem 


    - examples:

      - examples of problem types on different interfaces:
        - system problems: inefficiency, conflict, mismatch
        - information problems: excessive information, conflicting information, information asymmetry
        - structural problems: unnecessary components, contradictory function requirements, mismatch in shapes
        - intent problems: adding specificity where unnecessary, intents that neutralize each other given position, sub-intents that dont match function intent
        - concept problems: excessive definition routes, overlap in definition routes across concepts, definition route that more adjacently matches another concept
        - logic problems: excessive assumptions, contradictory conclusion & assumption, using specific logic to make absolute inferences

      - problem prediction example with market organization 
        - anticipating problems across many agents with n steps, and calculating which problems will develop and which solutions can be constructed in advance
        - unit example: predict when a dev will need a tool based on usage/purchase/request data (alternatives with different priorities/perspective built-in)
          - which problems will develop from which tool sets used at scale (migration tools between comparable alternatives)
          - which problemss will be prioritized & have solutions constructed
          - how to optimize by constructing other calculated solutions to prevent high-risk problems

    - dependencies
      - this interface relies on the find_format_for_metric.py function 

    - functions
      - this interface implements a function that calls find_format_for_metric.py with intent to find structures that neutralize other structures (rather than a basic match)
      - convert a problem statement (and problem space context if provided) into the problem object metadata 
      - mapping function, to map problems to structures, problem functions, & other problem types (as graphing a problem is depicted in FIG 7 (Problem space visualization))
        
        - program functions
          
          - validate user-provided GUI input information (for example, if the problem statement doesn't match problem type specified), entered in a form as shown in FIG 1 (User Interface Module)
          
          - optimizing functions to analyze prior queries, optimize & maintain the program, such as: 
            - removing duplicates 
            - calculating & compare query & solution statistics 
            - optimizing a performance metric like interface traversal once found 
            - pre-computing & storing frequently requested traversals 
            - optimizing data storage & logic given how other users are using the program
        
        - a set of graphing functions 
         
          - graph the problem space, problem, related problem network (as shown in FIG 7), solution space, solution, embedded graphs, interfaces, and other relevant objects
            
            - function to derive the problem space metadata (which is returned & displayed to the user is shown in FIG 3 Problem Space Metadata), optionally including the solution metadata in FIG 4 (Solution Metadata) & additional solution metadata in alternate formats as shown in FIG 5 (Additional Solution Metadata), if a solution is found or if solution space information is found.
            
            - function to derive, analyze & compare solution metadata, for solution selection purposes
                - input filters 
                - risk contributed by input filters 
                - risk contributed by traversals (using a pattern instead of an insight contributes risk) 
                - solution(s) and/or solution space 
                - solution implementation steps  & components 
                - visualization of solution impact on problem space 
                - set of queries used to generate/find/derive solutions 
                - methods to generate optimizations of those queries which the system will store for any future users with a similar problem 
                - other solution information, like solution statistics, success probability, ratio of patterns to insights used in the solution, etc. 
                - any non-fatal errors encountered, such as missing optional information or components, or patterns/predictions made in the absence of clarity 
                - any problem space information derived during the traversal, such as identified possible/probable insights, questions, strategies, patterns, causes, etc.
            
            - function to graph the problem on a network of related problems (on the same interaction layer, in the same problem space, etc) such as how the problem of building a technology is related to the problem of managing usage of & access to it
              
              - map related/approximate problems/problems (by a metric like cause or similarity) into a related problem network (like a generative vs. identification problem)
              - defining the problem space as a contextual system where the problem is active
                - this includes other problem spaces where it is or could be active
                  - for example, how the 'tech distribution' problem (where most tech is inherently neutral & can be used for good or malicious intents so what matters most is how it's distributed) acts differently in different problem spaces where distribution tools & government ethics & policies differ
            
            - function to graph a problem as a set of structures indicating boundaries (filters, conditions), limits (assumptions, resource limits), or vectors (priorities, forces), creating the problem space (like limited tech creates a problem space) , where the space inside the shape indicates potential for change
              
              - the problem object can be represented differently according to the type & the solution generation method by applying interface filters to the problem space visualization, for example: 
                  - if your problem object is represented as a 3-d shape like a cube (indicating it has three main variables expanding each other from an origin corner & forced to create a closed system to maintain state, or limits intersecting with each other), the solution would need to be in a vector format to remove dimensions of the shape or reduce the size of the problem shape 
                  - for example, if you're representing your problem on the information interface, you may want to represent it as an information problem type within a system context, like how: 
                    - a conflict between system incentives & agent intents could be represented as two vectors with the same origin or two vectors going in different directions 
                    - an information imbalance would look like extra information in different positions 
                    - an information asymmetry would look like information in a position where it's not needed & can be exploited
                    - an information market would have some trust structures embedded, so information can be bought instead of derived for convenience
              
            - function to compare & select between comparable solutions, optionally including selecting solutions based on input preferences selected (preferences like 'avoid using ML in solution', 'use a particular interface', 'use pre-computed solutions from database', etc) 
            
            - functions to select/add/remove problem dimensions  
            
            - functions to identify/reduce solution space 

            - function to graph the problem space, which includes the solution space for the origin problem (and for all related problems on the network that the solution space applies to) - the solution space being a reduced version of the problem shape or structure, or all changes possible in a problem space, or the set of all possible solutions, whichever is the most specific definition that can be identified
            
            - function to derive trajectory between problem graphs where each graph represents a decision/state, and attribute sets & problem of similar type occupy a similar position on an axis depicting all the graphs traversed
            
            - function to graph solutions to the origin problem, which can be represented with formats like:
              - a structure within a system containing the problem (an optimal route with a required attribute like efficiency or a route answering a question, or a combination of objects reducing variance in a rule gap, or a filter sequence that creates a function optimally while storing minimal code)
              - a structure (other than reductions) to aim for when transforming the problem and the available resources implied in its definition (a solution defined as an optimal version of the problem structure, like the optimal structure to represent a concept or build a function) 
              - a reducing transform of the problem shape (solution vectors removing problem dimensions until it's a point) 
              - a problem-solving effect may be measured based on whether a solution contains or comprises a vector that: 
                - neutralizes a problem vector , applying force in opposing direction to a problem vector (reduce an incentive)
                - reduces the problem shape size  or dimension (resolve an ambiguity)
                - fills the problem shape with relevant structures (build a function, find a route)
                - or does any combination of the above for the origin problem & related problems, potentially neutralizing the problem space itself or converting it to another problem space. 
            
            - function to apply the solution to the problem space , as shown in FIG 5 (Additional Solution Metadata)
              - applying a problem-reducing solution vector to a problem space should reduce the origin problem, and possibly other problems or the problem space itself
              - applying a 'route optimization' solution may take the form of adjusting the system structure to invalidate the route, may attach a function to nodes, or inject an efficiency structure to the system, which may also reduce the problem dimensions in the problem space visualization in addition to changing the system structure in the associated visualized system-structure interface format of the problem.
            
            - function to select the right format for the problem & solution
              - each format is better for different information, problem types/formats (with varying structure in the problem definition) & solution intents, but if you have a particular required solution format, you may need to translate a sub-optimal problem format into one associated with that solution format
              - each format involves a standard form like a set of vectors (which may represent a set of database/interface queries or insight paths, info objects like questions/insights/related problems, decisions/actions, causes/explanations, steps like removal/addition of variables, directed structures like distortions/intents, etc) which may be applicable in the interface network to retrieve/connect information, or in the problem space to reduce a problem shape, move around problem components to change the problem, or traverse a route in the problem network system (not necessarily the network of related problems, but the problem framed as requiring a solution route within a network
              - example logic of function to find alternate solution formats in FIG 11 (Finding alternate solution formats that fulfill different metrics)
                - how to identify alternative solutions that would be interchangeable with this solution in various contexts (like for different solution metrics):
                  - in other words, how to translate 'find optimal route fulfilling a metric' to an alternative interchangeable solution that makes the initial problem trivial to solve 'find system-wide cost-reduction function that makes system routes equally costly', at which point the original problem's solution is 'any route'.
                  - we are looking for ways to invalidate the problem (generate an adjacent object to act as a proxy or replacement for the solution, generate the solution automatically, change the system structure so solving the problem isnt necessary, etc) rather than generate a specific solution (like how 'trial & error navigation of all possible routes' is a specific solution)
            
'''
- function to find interfaces 
        - find the pattern interface in the cause interface (used when validating that an interface is completely defined) 
        - identifying all interfaces with variance that cant be captured in other interfaces 
        - filter interfaces  
          - filtering the pattern interface by the intent interface with would produce a set of intents found in patterns 
        - identifying specific interfaces (filters) for a problem/space 

- function to select interfaces by usefulness for problem-solving intents
    - cause is a good interface to host constructive discussions about decisions, that avoids information used to allocate fault
    - intent is a good interface to frame lies
    - pattern is a good interface to frame change types, after already standardizing to the change interface

- function to apply interface query config (default config or config input by user) 
          - interface queries can be configured by parameters like: 
            - priority 
            - logic allowed in interface query (like exit/return statements or conditions) 
            - error log level 
            - optimizations 
            - preferred interfaces/structures/formats/methods, like: 
              - query organization methods 
              - prefer the function interface over the pattern interface, for specificity 
              - prefer sequential interface queries, for state tracking 
              - prefer core functions (prefer finding existing information as opposed to deriving information or generating new information) 


- function to design an (internal) interface traversal: 
        - this function allocates interface structures (like priorities/dependencies/conditions) to form a structure (like a network or sequence) containing operations applying: 
            - specific interface components (like navigation functions) for that interface 
            - core/common components (like distortion functions) of that interface 
            - related components of the interface 
            - other interfaces/interface operations 
          - in order to form an (internal) interface traversal query, similar to the function that designs an (external) cross-interface query structure (like a sequence or network) containing interfaces to apply with connecting logic 
        - determining position/trajectory on interface 
          - starting from a particular object layer on an interface (like how info attributes like measurability are on one layer, and info objects like questions are on another layer) 


- function to select a structure (like a network or sequence) to organize an interface query, containing interfaces to traverse 
            - if not a sequential query, another format like a network interface query may contain conditions to assess after each traversal, such as: 
              - whether to apply/inject an interface if a minimum of information retrieved is not reached 
              - whether to exit processing and return output to the user if information fulfilling a certain metric like 'explanatory potential' is found 
            - the interface query may apply interface operations to determine interface application structure like sequence or network 
        
- function to design an interface query (sequence of traversing interfaces), as shown in FIG. 21 (Interface & traversal diagram)
            - As shown in the 'Interface Query diagram' section of Fig. 21, an interface query (or the corresponding objects inside an interface, such as an interface traversal indicating a preferred navigation like starting with core/common/generative components) has conditional logic dictating which interfaces to apply with what structures (in which conditions and in what sequence), such as:
                - start from system interface
                - check for components fitting the object, attribute, & function interfaces (as well as structural interfaces & objects frequently found in systems like symmetries and equivalences), 
                - apply the insight interface where there is uncertainty and the pattern interface where the insight interface cannot reduce uncertainty.
            - For example, an actual interface traversal does matching logic such as:
                - once you have formatted a problem as a system, iterate through objects, attributes, & functions in the problem system
                - check for anything in the problem system that looks like a system object, such as a false similarity, an incentive, or an efficiency, with a particular focus on system objects that are associated with the problem type (if there are any insights relating that problem type with system objects such as imbalances relating to the info asymmetry problem type). 
            - As shown in the 'Interface' section of Fig. 21, example structures found in an interface are depicted, including injected interfaces, core interface structures, interface-specific analysis functions, etc.
          - this function assembles a structure (like sequence or network) of interfaces or interface structures (like a combination) that can fulfill a user intent (the user optionally being a program requesting an interface traversal or query) 
          - core functions (filter, find, apply, derive, build, change) mapped to user intents (identify cause, predict a variable, build a function) can generate & design a query on the interface network 

- function to find an interface, interface structure, or interface traversal to fulfill an intent 
          - this function finds a structure of information formats/standards that would be useful for a given input intent, and selects the interfaces that could produce that structure of formats 
          - this function identifies when a particular specific interface will reduce solution set across any possible host system 
          - examples: 
              - the filter interface is more clearly usable as a method to generate the others bc most problems can be reduced to a structure that can be filled in different ways for different reasons 
                - it can even generate the change interface, by framing each process as a filter between i/o 
              - framing a conflict of type 'competition' as opposing direction/intent or equivalent direction/intent is a calculation that can be automated using any of these kinds of analysis, but the logic & intent interfaces are best at this, and selecting those type of analysis is an important tool to build 
              - which interface to standardize to in what structure (sequence/combination) depends on which use you intend to use the information for 
                - if you need to implement it immediately, an interface like intent that is semantically adjacent to the structural & logical interfaces will be more useful 
                - if you need to identify new types, standardizing to the type interface will be more useful 
            - example interface queries for problem statements: 
                https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/specific_methods/problem_solving_matching.md 
              - problem: find a prediction function to predict variables causing an output, like predicting stock price or a diagnosis from symptoms/causative conditions 
                - interface traversal 
                - find information (describing variable types, redundancies, missing info, etc) 
                - fit system (fitting the variables to a system format) 
                - map cause (finding root/direct causes & causal structures) 
                - match concept (whether the problem is valid given a definition of price) 
                - identify change (how the function can change) 
                - if thats not enough to fulfill solution metrics or reduce the problem (identify a range of possible prediction functions), traversals with interface operations can be done 
                - causal * change * pattern - to examine whether causal change patterns can reduce the problem or identify a solution 
                - concept * change * causes - to identify if a concept change looks imminent 
              - problem: find & build an optimal invention design to fulfill intents like 'building a function with minimal bugs' 
                - interface traversal 
                - find information (describing function intents, limits, and assumptions like parameters) 
                - fit system (fitting the function to a system, formatted to optionally include possible variance injection points, identify efficiencies like logic that can be merged, etc) 
                - identify structure (identifying structures that can be applied to the function system, like filters (conditions), direction changes (control flow statements), relationships (assignments), and mismatches (errors) 
                - identify potential (identifying unenforced rules, rule-intent imbalances, false similarities, & other objects of potential allowing exploit opportunities that are not already identified) 
                - change cause, intent, concept (test function impact on other causes, concepts, & intents, which are high-level objects a function can alter) 
                - match pattern (does this function comply with patterns for functions with similar solution metrics) 
                - if the function implementation doesn't fulfill solution metrics, other interface traversals can be done 
                - a system-object or function-concept interface like the 'efficiency interface' or 'ambiguity interface' (does this function have a more efficient or less ambiguous route between input & output that might fulfill a solution metric, given that maximizing efficiency & reducing ambiguity are standard system & function metrics) 
              - problem: find an optimal route (or alternatively, find a distribution of functionality/efficiencies/costs to make all routes or a particular route less/equivalently costly) between start & end points, like the 'minimal trades to get equal problem/opportunity distribution' 
                - interface traversal 
                - identify information (identify differentiating attributes/functions/sub-systems of agents/positions/routes within the network) 
                - fit system (identify relevant structures like abstraction layer to traverse at, identify important objects required to solve the problem, like trading problems/markets/skills/information/risk/bets vs. trading currency, or framing currency as a position attribute, rather than a standardizing interface) 
                - identify structure (identify trade & other market structures that are important for understanding why resources don't get distributed fairly, like closed trade loops & independence machines) 
                - identify potential (identify alternative perspectives that could also explain the variation in optimized routes, like alternate value definitions) 
                - identify cause (identify causes like marketing, collusion, and regulations that prevent or interfere with equilibrium market events) 
                - identify concept (identify concepts relevant to markets like balance, demand/supply matching, and how the concept of information can disrupt any other market bc it enables automation) 
                - if queries of those interfaces are insufficient to solve the problem, interface operations can be used 
                - the information-system-structure interface operation (can be used to determine information like the next layer of information objects that are relevant if enough automation is distributed) 
              - problem: design set-sorting or value-finding function: 
                  - analyze a set object from these interfaces - then when you find a pattern match on an interface set, you can restrict the search to those 
                  - core interface: what core functions determine set generation/selection/aggregation/interaction/organization 
                  - causal interface: what functions were used to generate the set 
                  - intent interface: what is this set for 
                  - structure interface: randomness, endpoints, subsets/split 
                  - potential interface: what are the limits on this set, what is the set of possible outcomes 
                  - change interface: where is the change concentrated/distributed in the set from a standard set 
                  - pattern interface: what patterns do sets in this position (determined by attributes or sample subset) normally follow 
                  - function interface: what functions are adjacent to the set if it has a sequence or clear function map 
                  - concept interface:  
                    - what specific tradeoffs/mismatches/alignments/symmetries/combinations/interactions are inherent to the problem/problem space? (specific concept filter)  
                    - where is the power distributed in the set? (abstract concept filter) 
                    - identified concepts: 'similarity' in navigation, 'equality' in split => optimal for target value near initial split points or similar positions to the split points 
                  - system interface: what variance injection points are in the set generation/selection/aggregation/interaction/organization 
                  - key concepts of this problem (like the "tradeoff of search start point/split function/organization vs. performance", "subset gains", "pattern matching", and "potential worst/best case scenario of solution") should be found quickly from various interfaces: 
                  - structure interface:  
                    - position (sequence in the set problem space) is a determinant of adjacence/distance 
                    - adjacence between start search position and final found value position is a key metric 
                    - start-found adjacence can be maximized by changing input (number of start points) 
                    - limits on number of processes involve ability to read a value at a given position at a time 
                    - maximizing start-found adjacence requires more work (higher search processes) to produce a possible metric "lower search time" 
                    - "search time" and "start point count" have a tradeoff structure 
                  - potential interface: 
                    - the set of possible outcomes (possible positions of value) is equal to the set's positions (indexes) 
                    - how do you reduce the set of possible outcomes if the possible outcomes are an integer sequence equal to the set length 
                    - subsets are a potential interim unit (based on the value count attribute) between the outcome data type (one value index) and the input data type (set) 
                    - the potential of subsets of equivalent length to contain the value could be equally likely (adding randomness to search) 
                    - potential injection point for pattern interface: skipping equivalent valued subsets could reduce solve time (if subsets with a certain split follow patterns as determined at search time) 
                    - best case scenario in standard search (random or endpoint) is the first value in the set is the target value 
                    - does subset search offer gains to random search? 
                    - best case scenario of unit solution type (iterate check of value)in subset search is first value after first subset split (split in half) is the target value 
                    - next best case scenario type (if the unit solution type best case scenario doesn't occur iteratively) is pattern found & used to reduce solution/search space 
                    - splitting requires multiple processes 
                    - pattern logging/searching requires multiple processes 
                    - depending on set, either can reduce solution space with extra work 
                    - there is a trade-off between work invested in pattern-checking, subset-splitting & solution space reduction potential 

          - interface query logic example, as shown in Fig. 14 Design Interface Query
            - FIG. 14 depicts an example of assembling Structural Meaning relevant to an Input Intent, using a structure containing Information Formats.
            - For example, to fulfill an intent like 'determine if type variables are a predictor for this data set' (where type variables arent included in the data set), this function would organize the relevant interfaces by core operations: 
              - example of an output interface query in abstracted form (this can be used as a structure to fill with logic, rather than starting from format structure): 
                - check that: 
                  - variables[independent] / (standardized by) 
                    - [type interface].function.(patterns || insights) or [attribute interface].function[aggregation](patterns || insights) 
                      - as an input to [potential interface].[prediction interface].functions (including regression) 
                        - outputs [input information].variable[dependent] 
              1. As shown in the process depicted in the top half of FIG. 14 for this example, the logic may convert initial intent to organized requirements, given dependencies 
                  - intent: 'determine if type variables predict dependent variable from data set' 
                    - sub-intent 'predict dependent variable in data set from type variables' 
                      - sub-intent 'find type variables' 
                  - input: data set variables 
              2. As shown in the process depicted in the top half of FIG. 14 for this example, the logic may determine required formats given a set of specific format requirements, out of the full list:
                      - input requirements: 
                        - type variable format:  
                          - variable set 
                          - type attribute 
                        - prediction format:  
                          - function structures: functions formatted as a set of limits/vectors/filters/networks/sequences/sets 
                          - function format types 
                            - function development functions (and their formats) 
                            - generative/descriptive/causative/determining functions (and their formats) 
                            - mixed-certainty function (with points or subsets where non-uniqueness of outputs is introduced to represent a possibility structure like a possible output range) 
                      - output requirement:  
                        - dependent variable predictor: function 
              3. As shown in the process depicted in the top half of FIG. 14 for this example, the logic may generate an interface query: 
                - use core operations (check/find/apply) & interface rules (regarding input/output, structure/formatting, connection logic)  
                  to connect input format (variable set & generative functions) & output format (predictor of dependent variable), 
                  applying the above organized intent requirement format: 
                    - containing intent: 'check if identified type variable sets can predict the original dependent variable' 
                      - prediction intent: predict dependent variable from type variables 
                        - sub-intent: identify type variables 
                          - sub-intent: apply type format to variables ('attribute set') 
                            - sub-intent: generate variable combinations 
                        - sub-intent: check if each variable combination matches predictor definitions 
                          - sub-intent: apply prediction format ('generative function') to each variable combination 
                            - sub-intent: store generative function for prediction intent 
                      - prediction intent: check if generative function for variable combinations can generate the original function when combined with other generative functions  
                    - containing intent: 'check that dependent variable is predicted with sub-intent prediction output (identified type variables)' 
              4. The process in the top half of FIG. 14 may also involve determining function requirements, given intent format, with sub-queries to generate/find/derive these functions as needed, before running the above interface query 
                    - function: combine variables into sets creating generative functions 
                    - function: iterate through variable sets 
                    - function: identify variable sets indicating types 
                      (variable sets that could create a generative function that would be combined with other functions to build the original function, like how combining y = 2 and y = 4 can generate y = 3) 
                     - function: identify predictive variables 
                    - function: identify dependent variable relationship to function components or alternate functions 
              5. The process in the top half of FIG. 14 may also include iterating through other input format combinations, applying format combinations to organize & connect the available input & output formats 
            - As shown in the bottom half of Fig. 14 in the Interface Query Structure example, the organized intent structure of the logical process above can be visualized with embedded shapes. The intent outputs (starting from the most granular layers) which are then integrated by layer using core operations like combine/filter/apply.

            - example: here's an example of why different interfaces are more useful in different situations, given a standard problem like 'build a function automatically for a given function intent'. 
              https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/core_analysis/system_analysis.md 
              https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/core_analysis/interface_analysis.md 
              https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/core_analysis/derivation_methods.md 
              https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/specific_methods/problem_solving_matching.md 
              1. Intent interface 
              - If you want to build a function automatically, and you have code indexed by intent, then you don't need to write code, you need to write the intent & sub-intent sequence or other structure. I would call that 'standardizing to the intent interface' or 'applying intent structures' to the overall function intent, which is the problem definition ('build a function with this overall intent'). If you already have code indexed by intent, framing a function as a set of intents is trivial. If you don't already have code indexed by intent, the process you use to decompose an overall function intent into a structure of sub-intents is a tool that can be re-used to index existing functions by intent. 
              2. Information interface 
              - If the problem can be framed as an information problem, you can query information problem type rules & patterns to solve it automatically. Building a function automatically given an overall intent would mean: 
                - solving a series of information problems like: 
                  - 'information mismatch' (object1 doesn't match object2 and it should, so assign object2 to object1) 
                  - 'conflicting information' (object1 doesn't match object2 so merge their conflicts)  
                  - 'required information' (object1 is required to have this attribute value so assign it) 
                  - 'missing information' (object1 is missing this attribute so return False or query for that information or generate it). 
              3. Cause interface 
              - If the problem can be framed as a cause problem, then you are querying for causes. Building a function automatically given an overall intent would mean:  
                - finding the causes of bugs 
                - finding the causes of different types of logic & structures (like sequences) applied to different types of logic (inherent rules governing logic given the point/definition of logical operations, like 'an if condition usually precedes a non-if condition' because the point of an if condition is to test for a case to apply logic, where the logic applied is not another condition) 
                - finding the causes of functions & function-related objects like side effects, memory usage, optimizations done on other functions, etc 
                - then you'd compose these causes in a structure that would allow automatic generation of functions from a given intent (first apply logic-related causes to generate a function causing the given function intent, then check for optimization-causes in the generated function & apply optimizations if those causes are found in your generated function structure, then apply tests for bug causes, etc). 
              4. Structure interface 
              - If the problem can be framed as a structure problem, then you are querying for structures. Building a function automatically given an overall intent would mean: 
                  - finding structures to standardize functions to (limits, filters, networks of relationships, directed networks of operations) 
                  - finding structures to standardize intents to (directions as priorities or more structural goals, possible usage ranges as intents, abstraction as an indicator of intent (neutral/mathematical functions can be used for anything), using intent as a proxy structure for the concept of permission by organizing information access by intent) 
                  - matching intent & function structures that fulfill the given overall function intent without causing invalidating side effect intents 
              5. Pattern interface 
              - If the problem can be framed as a problem of resolving which patterns to combine in what structures (where patterns optionally include abstract/generalized structures (such as variables, variable patterns, input-output path patterns, or type patterns) that resolve to specific logic when converted into information, meaning they're assigned constants), building a function automatically given an overall intent would mean: 
                - finding which patterns or alternative pattern sets (a variable type relationship pattern, an input-output type trajectory pattern, a logic sequence pattern, an optimization pattern) can generate the required logic when constants (specific information-filled versions of the abstract pattern structure) are applied 
                  - the output of that may be as diverse as an input-output table to handle a variety of use cases observed, a prediction function trained on input-output data, a logical sequence, a code query, an intent sequence, a directed logic network, etc - depending on the patterns used 
              6. System interface 
              - If the problem can be framed as a problem of fitting the function to a system, building a function automatically given an overall intent would mean: 
                - identifying starting & ending position to map intent to structure in the system (get from input start node to output end node) 
                - identify default & alternative (higher cost, lower step count, etc) paths between start & end node 
                - identifying system objects like efficiencies, incentives, etc, especially those structures clearly relevant to the default & alternative paths between start & end nodes identified 
                - applying definitions of those system objects to select the logical step sequence (avoid conflicts, target rewards without side effects, minimize costs, apply symmetries for standardization purposes) 
                - checking which routes fulfill given function intent 
              7. Concept interface 
              - If the problem can be framed as a set of concepts required for the solution (framing the intent in terms of concepts like 'distribute power evenly'), or if you have conceptual information indexed for code, building a function automatically given an overall intent would mean: 
                - using conceptual math operations to determine which structure of concepts is most useful for the given intent (if combining 'power' and 'efficiency' in a 'sequence' or 'balanced' structure would produce the optimal function for an intent like 'distribute power evenly', that is calculatable if you have other functions indexed by conceptual structures, or if you have conceptual math operations accessible to determine what structure of concepts would generate the required concept set, or if you have intent indexed by conceptual structures, or if you can standardize intent & concept to another interface where you have conceptual structures indexed, etc) 
                  - for example if you have functions indexed with conceptual structures like the individual concepts required (power, efficiency, distribution), what operations can be applied to these concepts to create the optimal concept combination ('distribute power evenly') - meaning conceptual operations like 'inject power to distribution structure', 'limit distribution structure with power injected by efficiency', etc. 
                  - these conceptual operations involve finding matching structures across the concept definitions: 
                  - 'injecting' power into a structure manifesting the 'distribution' concept is possible if the distribution-manifesting structure has an input opportunity of some structure, and power can be translated into a structure that can be used by the structure having that input opportunity (a distribution structure such as a function having an input opportunity in the form of a parameter, where power can be translated into a usable structure like information assigned to that parameter), given the definition of the 'inject' operation as 'input the injectable to the receiver' 
                  - you can avoid doing structural operations by storing the structures for each concept and then storing patterns/outputs of their operations 
                  - if combining power & efficiency produces a structure set, that can be derived by querying the structures of power & efficiency and combining those structures in a way that doesn't invalidate either definition 
                  - you can also apply logic to the concept operation ('inject power to distribution, limited by efficiency') to create the output concept of that conceptual operation ('efficient distribution of power'), and then do a structure query of that output concept 
                  - once you have function structures matching the output (having found function logic matching 'efficient distribution of power' once translated to the structural version 'minimized cost of allocating inputs' if inputs are the structure found in the function system matching the power definition, where 'minimized cost of allocating inputs' can mean 'diversifying calls for this intent across various alternative functions' or 're-using existing functions where possible to minimize the cost of building a function on-demand or at compile time' or 'a function set that minimizes the memory/space requirements of allocating inputs'), you check if those structures optimally fulfill this function's intent, 'distribute power evenly', and then execute the final steps to resolve those structures into function logic (with input-output requirement chains, intent-matching, etc) 
              8. Problem interface 
              - If the problem can be framed as a problem in a problem network of related problems, and/or a problem space, you can calculate attributes like whether the problem is about to be invalidated by other functions built for other problems, whether the profit opportunity of solving the problem is worth the probable cost, whether the whole problem space is about to fundamentally change, etc. Building a function automatically given an overall intent would mean: 
                - determining whether the problem of organizing logic is a solved problem if framed differently (can AI generate code with enough accuracy to invalidate further investment) 
                - determining whether solving an adjacent or proxy problem invalidates solving this specific problem (can concept or intent identification tools or even existing code bases invalidate the need for a tool to build functions automatically, or can code bases be re-written in a way that invalidates automatic code generation, by simplifying code-writing to a task of intent-writing or code query-writing or another process simple enough to invalidate complex code and the need to generate it) 
                  - determining if a solution like logic automation can replace code generation (a tool that automatically applies the definition of logic, optionally including all related objects like logical fallacies, to prevent logically 'jumping to conclusions' or 'ignoring assumptions' or 'over-applying bias vs. updating bias', then indexing code as these logical objects so logical rules can be applied to optimize/generate code) 
                  - this would involve writing high-level logic language like 'find information, avoid misidentifying object1 as object2, combine common attributes of these objects with versioning in case of conflicting values, avoid this conclusion & this fallacy error type', which would allow logical object definitions (of what a fallacy is, what a legitimate conclusion/assumption/implication is, etc) to be applied automatically, rather than the existing method of applying conditional/contextual/specific low-level logic developer-defined definitions to be applied manually, which involves writing low-level logic like 'select * from table, check if object1.attribute.value == object2.attribute.value, etc'. 
                - determining whether the problem can be formatted as a set of solved problems (applying organization to information, applying definitions, finding matching structures, generating tests) or in a format that is solved (route optimization) 
              - given the information you have, one interface may be more useful to standardize to than another. If you already have intent or cause information indexed or otherwise adjacently calculatable, or if those interfaces contain the required solution information (as in, the problem is 'finding the cause of some measurement', so the solution is going to be findable on the causal interface), you'd be better off standardizing to those interfaces first, without other information. 

- function to determine whether to skip adjacent interfaces in interface trajectory 
            - sometimes you'll be able to skip interim variables/interfaces 
              - example: depict the spine variable & the finger position variable to demonstrate/identify chirality, skipping the connecting functions, because there are multiple connecting functions (endpoint/side selection, extremity development) and they dont determine change in either variable, as the key important relationship is the spine symmetry and the orientation transformed about the finger position interface being reversed according to the spine symmetry 
                - the spine isnt symmetric from the side, which implies a bias toward the front, which is a platform where features are concentrated, so the development of limbs (using derivable intents like duplicate, backups, protective, flexible, movement, alternative, balance intents) & their focus toward the front is derivable from the spine features, so we can skip to the finger order interface to identify the concept of chirality or an example of it/its patterns in the system 
              - the interim interfaces & variables may not add change to this relationship so they dont need to be depicted or stored in this context 
              - this is useful for determining where change can be stored/routed in a system 
                - if there is demand for change (stressors demanding new functionality) but all components but one are maximizing their change handlers, then you know theres one potential variable where change will gather/be routed, if its possible to route change from the variance injection point to that variable's causal stack at some layer/point 
              - its also useful for determining interface trajectories/adjacent interfaces 
'''
'''
      - function to traverse an interface (apply an interface to a problem, looking for matching objects)

          - examples:
          
            - system interface traversal 
              - general: fit system objects like symmetries, sub-systems, sub-interfaces, false assumptions, correlations, and conflicts to problem/solution/space definition 
              - specific: find the lowest-cost path in a system (maximizing the number of efficiencies used) using incentivized paths 
            
            - information interface traversal 
              - general: use logic such as mapping the problem as a combination/set/path containing information problem types like an information mismatch or inequality or minimum or overflow or lack 
              - specific: frame a 'find a particular record in a data set' problem as a combination problem of a missing information problem type (composed of a filter-selection problem, an indexing problem, and a sorting problem) or a route optimization problem type (starting point in data set, search/split/sort method selection, and cost-minimization problem for worst-case destination given starting point) 
            
            - insight path application  
              - general: use insight paths from other fields to optimize insight generation/ identification/derivation, where insight paths can contain questions, strategies, insights, & other information objects that are usable across systems to generate/ identify/derive insights in a semi-unknown system 
              - specific: use insight paths from gene editing to automate inventing by mapping gene editing functions (switch, remove, alter) to inventing problem space functions (switch components, remove assumption, alter variable) 
            
            - intent interface application 
              - general: convert inputs/outputs/functions, objects, & attributes to intent to check progress toward solution intent or avoid side effect intents, where adjacent reasons to call the operation & operation outputs are assumed to be included in the intent stack of an operation 
              - specific: convert inputs/outputs/functions, objects, & attributes to intent, to check progress toward target solution metric or avoid side effects 
            
            - structural interface application - general: find a standard structure & format the problem using that structure 
              - specific: convert functions to standard structures like paths, networks, filters, or attributes to check if a function fulfills a solution metric 
            
            - core interface traversal 
              - general: use combinations of core functions (find, build, apply, derive), objects (layer, filter, gap, limit), and attributes (equal, similar) to create a core interaction space & system layer diagram and find target objects quickly using structural definitions of concepts like optimal or applying system filters, or predict missing objects on other layers 
              - specific: use the core functions of the 'combine' or 'organize' intent to predict the next generation of products invented 
            
            - problem interface traversal, specifically a problem vectorization framing the solution as a path in the problem space (mapping the problem definition to a one-directional tree with inputs on one side, interim inferred important problem concepts in between, and target priorities or attributes on the other, linked by available functions) 
              - general: infer important interim concepts of a problem system (like the 'duplicate line' concept for building a 'merge files' function) and use intent- mapping to connect stated problem objects & target outputs using available functions 
              - specific: infer the relevant 'duplicate line', 'similar line', 'similar', & 'equal' concepts of a 'build a function to merge files' problem system and use intent- mapping to connect stated problem objects (line, file, string) & target outputs (one file without duplicate lines) using available functions (iterate, check, is_similar, is_equal) 
            
            - problem space analysis (analyzing a system composed of resources, agent intents, & problems) 
              - general: analyze whether the problem space changes in a way that invalidates the original or other problems once a particular solution is applied, anticipating cascading, self-sustaining & self-solving problems, and selecting between solutions 
              - specific: organize a set of resources into a problem space system with dimensions indicating primary factors of change that are also interfaces (as a foundation where changes can develop and be described in other embedded graphs) or cross-system attributes (like relevance), for standardized comparison of solution impact on all problems in the problem space system 

            - a pattern interface traversal (where patterns replace missing required data, such as patterns between variables of specific types or system positions to infer their probable relationship) 
              - general: select patterns related to stated objects and traversal for patterns or pattern generators linking them to generate an origin solution space to begin compressions at 
              - specific: select patterns related to variable relationships & probability distributions to predict the likeliest ways a function will change 
            
            - a causal interface traversal 
              - general: match problem structures to causal structures (like tree/network/loop/ layer) to infer probable causation metadata like directness of cause, degree of cause, inevitability, ambiguity, uniqueness of cause, causal shape 
              - specific: - find the set of causal objects, functions, and attributes describing a relationship to create a prediction function or reduce input features - apply causal structure relationships to determine if the data is missing information 
            
        - logic:

          1. convert to interface based on definition 
          2. apply an interface to input information 
          3. apply interface components to distort information to generate additional information to match 
              - specific interface components (like navigation functions) for that interface 
              - core/common components (like distortion functions) of that interface 
              - related components of the interface 
              - other interfaces/interface operations 
          4. find matching objects 
          5. convert to original system format) 
        - this function implements traversal by applying interface components (like functions/attributes/objects) of a certain type (like core/common) in a structure (like a sequence) such as: 
          - applying core/common/generative/cross-system components (like functions) first 
          - applying insight/intent interface first 
            - examplee: applying cause-related insight paths to input information once converted to the cause interface 
          - applying interface checks first 
            - example: checking for new interface objects (like change types), if the interface changes frequently (like the change interface) 
          - applying related objects of the interface: 
            - example: applying interface info objects like related questions/insights 
        - the function to traverse an interface is referenced here: 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/specific_methods/math_semantic_map.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/specific_methods/problem_solving_matching.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/tasks/function_to_do.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/tasks/to_do.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/docs/tasks/ideas.md 
          https://github.com/outdreamer/build-a-cure/blob/52c3461fdd3ff38284b63f8c2e71542f415d88d9/README.md 


        7.A. applying default components or prioritized structures to format or otherwise alter the information to identify its structural relevance to that interface with interface conversion function

        7.B. identifying matching components between information & interface components (components like systems, objects, functions, attributes, & types) 
            A. then the input information objects (converted to the interface) would be compared to interface components, to find matching structures 
            B. after this initial match check, the function interface is applied, using interface-specific functions, which are either: 
                - functions of that interface (function types like core/common/interactive/relevant/change/causative/generative/other prioritized distortion function types) 
                - functions of other interfaces 
                    - patterns & functions across interfaces (apply the pattern interface) 
                    - insights & insight paths (apply the insight interface, a sub-interface of the information interface) 
                    - functions to achieve core/common/current interface intents, like core/common formats like 'minimized', attributes like a 'change-handling' priority, or other outputs like core/common/generative functions (apply the intent interface) 
                    - functions of cause/change/potential (apply change/cause/potential interfaces, to ensure youre checking versions of the structure that are probably relevant by commonness or other core priorities like causative change types, causal adjacence, or probability) 
                    - functions of concepts (apply concept interface, to identify concept structures) 
                    - functions of systems (apply the system interface & its components, like the 'optimize' function) 
            C.A. once these functions are applied, iterate through distortion sets producing different states of the input information: 
                - verify that the distortions are still relevant to the interface 
                - repeat the matching process, looking for matching structures between the newly distorted input information structures & the interface components 
                    - for example, once youve applied an insight like 'comparison is quicker if you only compare different attributes', which involves reducing the attributes of the input information to the different attributes, do you find any new matches with interface objects, like a match with a function that could produce those differences, from either point in a compared pair as the input & the other point in the compared pair as the output? 
                        - if so, this is a function that you might not have found as quickly if you were matching the object having those attributes on a different interaction layer, like how comparing two shapes would benefit from different functions than comparing two generative functions of the two shapes 
            C.B. optionally, distortion functions can be applied with intent to identify new components on the interface (apply an intent distortion function on the cause interface) 
            C.C. optionally, distortion functions can be applied to other interface objects, to identify new components on other interfaces (such as applying a causal distortion function to an insight path to check if a new insight path applies, while traversing the cause interface), using the new input information and/or the cause interface objects for comparison 
        
        7.C. convert matching interface components back to input information with interface conversion function 

    '''
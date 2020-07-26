# Analysis definitions
  
  1. Workflows
    
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


  2. Analysis types

    - problem space analysis: visualizing problem metadata & related problem network, and changes to the problem space that invalidate the original or other problems once a particular solution is applied
    - core analysis: automatically finding core objects/functions/attributes/states possible to determine/describe a system, defining core operations like find/apply/build/derive
    - system analysis: automatically fitting system objects like symmetries, sub-systems, sub-interfaces, false assumptions, correlations, efficiencies, incentives, and conflicts to problem definition to determine optimal organization/format/routes/metrics/positions
    - structure analysis: automatically finding structures, like a route between information formats to solve a problem
    - information analysis
      - insight analysis: insight path application (using insight paths from other fields to optimize insight generation)
      - problem analysis: formatting to convert problems to a format with more solution methods, such as problem vectorization (mapping the problem definition to a directed network with inputs on one side, interim inferred important problem concepts in between, and target priorities or attributes on the other, linked by available functions)
      - question analysis: where a question is framed as a source position and a target position on a network, and the answer is the most robust path or the path that moves the nearest to the target position or the path that moves in the priority direction on the network
    - change analysis: automatically identifying change metadata like change types necessary to explain a solution or solve a problem
      - potential analysis: automatically finding structures of variance like gaps/cascades/reducers, possibility fields, and determining/limiting vertices
    - logical analysis
      - function analysis: automatically identifying function metadata like variables, input/output trajectory, the function in a filter format, intent, complexity, efficiency, & exploits
      - intent analysis: automatically finding possible reasons to use a function to automate logic
      - causal analysis: automatically matching the problem to causal structures to infer relevant variables & causation metadata (like directness of cause, degree of cause, inevitability, uniqueness of cause, causal tree/network/loop/layer shape)
      - pattern analysis: automatically finding patterns with relevant similarities to infer the relevance of pattern metadata, where patterns replace missing required data (such as using patterns between variables of specific types or system positions to infer probable variable relationships)
    - concept analysis: automatically identifying concepts associated with a structure & vice versa, identifying positions of default abstract concepts in the network
    - interface analysis: identifying a problem-solving automation workflow to derive/apply, mapping a query across combination or embedded interfaces given problem requirements, or identifying a specific or new interface to define/query


## Standardized analysis

  - definition: this describes the common components of other analysis types

  - objects:
    - interface objects like patterns & concepts

  - structures:
    - core structures (intersections, hubs, vertices, maps, limits, symmetries, & alignments)

  - concepts:
    - abstract concepts (similarity, power)

  - attributes:
    - interface attributes:
      - intent/priority
      - potential/certainty
      - perspective
      - causality
      - abstraction
      - interface queries that can produce this object 
    - commonness
    - contexts (coordinating/opposing, use cases, extreme cases, examples)
    - coordinatability: integration potential
    - interaction layer: which objects it interacts with, on what layers of a system like abstraction/scope layer
    - injectability: can it be used as an input, in many operations
    - emergence: is it generatable from other objects
    - neutrality: the range of operations/contexts it can be used for
    - scope
    - optimization
    - completeness
    - randomness
    - reusability
    - complexity
    - dependence
    - automation/optimization potential (resource investment, rule stabilization) 
    - applicable definitions (like for equivalence) 
    - minimum object identification information (required identity attributes) 
    - relationships 
      - adjacent/related objects of same/different type 
      - problems with adjacent objects & how those problems are generated by adjacent object metadata 

  - functions:  
    - structural functions: combine, merge, apply, embed, mix, filter, chain, define, create, derive, identify, change, version


## Object Analysis

  - definition:

  	- this is a standard information format commonly used in programming, including object/attribute/function information

    - the unique implementation of this used in this tool includes attribute type information, function metadata, and object derivation logic, as well as operations to merge objects & other common operations on these components

    - attribute definition:
      - attributes of an object contain information about other structures/functions of the object
        - 'is an object strong' translates to the question 'does the object have functions that enable it to execute tasks at high performance'
        - the 'strong' attribute refers to a net effect of the set of structures (its functions) that fulfills a metric (like high performance) relating to a state that the host object can occupy consistently, making it an identifying quality (attribute), while not required to remain in that state (can be a variable attribute, with multiple potential values)
        - if a system works well or is efficient, it may fulfill the attribute 'strong', which means that any structures of efficiency/high-functioning (like aligned benefits/costs or aligned intents/incentives or reused functions) may be assignable to the concept of 'strong', given that those can be components/inputs of strength

      - attribute types like input/output, descriptive/identifying/differentiating, abstract, causal, constant/variable/parameter, dependency/requirement, type attributes, etc
      - structurally, attribute can be represented as information flows like inputs/outputs, as emergent characteristics like additional ways to change (adding color or sound to a structure or additional embedded structures like a field/scaffold/layer)

    - object definition:
      - objects can be represented as a set of structures (like limits isolating change or vectors of change) that identify unique or isolatable objects, which act as a cohesive set of components (attributes/functions/sub-objects), or represented by context, given its position on a structure like a network, depicting its relative position to other objects
      - objects have boundaries differentiating them from other objects, containing their functions/attributes/sub-objects if present
        
    - function definition:
      - metadata like input/output parameters

    - definitions are identified by definition routes, which are alternate paths in a standardized language map (with language formatted to use interface terms) to define a object/attribute/function
      - the more abstract a concept, the more definition routes it may have
      - definition routes may reveal a particular structure of a concept, like how power is associated with delegation structures and can be optionally defined as 'ability to delegate'

  - attributes:
  - objects:
  - structures:
  - concepts:
  - functions:

  	- identify data sources (code bases defining schema/class definitions, network maps) automatically with a search to identify tabular data in web resources
    - import (to import objects/attributes/functions)
    - object functions: define, create, derive, identify, change, version
      - definition (definition route) functions
  	- structural functions: combine, merge, apply, embed, mix, filter, chain
      - example: 
        - combining a function and an attribute can mean:
          - changing any structures/metadata of the function that are capable of fulfilling/displaying/hosting the attribute
          - applying the function to the attribute to change its definition
        - which operation is used depends on which type of combine operation is used (merge, embed, intersect, union, version, merge with a particular conflict resolution definition, etc)

  - answers questions like:
    - what attributes do these objects have in common
    - what are the differentiating attributes of this object set
    - what is the relative position of this object on a network of objects
    - what attributes emerge from this object set
    - which objects change in what ways
    - what is the net functionality of the object set
    - how do/will these objects interact


## System Analysis

  - definition:
	  - this is a format accessible once information is standardized to object model
    - this involves framing information as a connected network with a boundary defining the system, that has core system operations, structures, & objects
  
  - structures:

  - objects:
    - information objects
    - variance objects like variance injection points (gaps in rule enforcement) & variance sources (gaps in system boundary allowing variance from other systems to leak in)
    - system objects like system failures/versions/boundaries/maintenance
    - games: system with resources (functions), incentives (benefits/costs), problems to solve with some metric (point maximization, route finding) and some general intent (explore, find, finish path)

      - alternate definition route: a set of intents/alternatives/limits/incentives/exploits/rules/risk & a definition of distance from intent fulfillment (position), usually resulting in the resolution of a clearly optimal route.
        - a game is a type of system & a mixed set, which can exist as a component of a system 
        - games can have many different structures like: 
        - a directed graph with a vector set representing possible agent intents/ functions/resources 
        - a system of nodes & links where agents need function input resources to traverse 
        - a decision tree where certain tree info becomes accessible only at certain nodes (adding uncertainty/risk) 
        - a set of trade options between nodes with different info change/update rules in a system to optimize a resource/trade/market metric 

    - tradeoffs: options with mutually exclusive contradictory benefits (if you take one option, you have to sacrifice the other), often a false trade-off or dichotomy applied when both are simultaneous options rather than contradictory
    - incentives: a reason to take an action (a benefit or cost) - usually interpreted as default in a system
    - inefficiency: defined as not using a cost-reduction or benefit-increasing method (using extra unnecessary resources, not using a requirement-reduction method, not reusing solutions, etc)
    - opportunity: potential move with a potential benefit, with a limited time component
    - exploit opportunities: opportunity with temporary local (selfish) benefits that allocates cost disproportionately to the system (destroying a system-maintenance concept like 'trust' or 'rule of law') or other objects in the system, with negative emergent side effects (hoarding resource incentives, requirement for monitoring & rule enforcement investment, misallocation of justice)

  - functions:
    - optimize, traverse, open/close, etc
    - apply system filters
    - reduce dependencies   
    - close variance injection points   
    - enforce rule
    - identify system objects given their definition, such as a variance gap (a gap in rule enforcement) 
    - map a system layer graph representing combinations
    - identify/derive system context   
    - find interactions of interaction spaces (which interactions are common across agents, likely given other interactions, etc)

  - attributes:
    - cohesiveness
    - isolatability

  - concepts:

  - answers questions like:
    - where are the inefficiencies in this system
    - how can this system be optimized
    - are too many assumptions hard-coded in this system
    - is this system capable of a particular function
    - does this system coordinate with other systems in a stable way
    - is this system adjacently exploitable
    - does this system contain more potential (options) than it needs
    - what input/output paths are available that can achieve a particular intent
    - where would this system generate coincidentally similar structures (a query to identify false similarities)
    - what system structures (or buildable system structures) fit in this unknown information-generating sub-system
    - system-problem interface: what problem types does this system have


## Concept Analysis

  - definition:

    - a concept is an object in a system that:
      - extends the core components of the system in a new way
      - acts as an interface (for change, randomness, etc)
      - has attributes/functionality beyond its definition in that space (can have one function in one system context & another emerging function in a particular state & environment)
      - example: power is the object left when objects implementing it: resources => energy => input => potential) have their context removed, navigating up the abstraction stack from: 
          - the info layer (resources & energy), removing their contextual attributes/rules 
          - to the abstract structural layer (input) 
          - to the abstract layer (potential, which is a related concept of power) 
          - so that the final object is defined in terms of other abstract objects on the top layer 

    - the abstract network is a set of related concept objects remaining after removing context, concepts that are applicable across systems, often have multiple definition routes because they take a variety of forms given the context, and are fundamental to describing a system. A subset of the abstract network is depicted in FIG 15. Concept definition network, which shows concepts related to 'relevance'.

      - example: power is the object left when objects implementing it (resources => energy => input => potential) have their context removed, navigating up the abstraction stack from:
          - the info layer (resources & energy), removing their contextual attributes/rules
          - to the abstract structural layer (input)
          - to the abstract layer (potential, which is a related concept of power)
        - so that the final object is defined in terms of other abstract objects on the top layer
      
    - a non-abstract concept is an abstract concept with structure applied (in a particular system), like how a particular definition of similarity in a system can evolve from the abstract concept of equivalence

  - objects:

  - structures:

  - concepts:

  - attributes:
    - abstraction
    - uniqueness
    - isolability

  - functions:

    - a function to identify concepts given their definition

    - conceptual math: 

      - an example is applying the concept of 'meta' to the concept of 'game' and getting output of the operation like 'a game where games can be created by agents inside the game' or 'a game to design games', given similarities between attributes/functions of objects in the definition & relevant spaces

      - apply one concept to another (apply 'power' to 'market' or 'evaluate market by power' involves standardizing the market concept in terms of power, using power as an interface)

      - apply concept to a structure, as a priority

  - answers questions like:
    - what concepts cannot be reduced/abstracted further
    - what concepts have which associated structures

    - structures that apply a concept are depicted in FIG 9 (Find structure for a definition of a concept0, which depicts structures of the 'distribution' and 'power' concepts, and FIG 2 (Structual definition routes for 'conflict' concept).

    - what definition routes identify a particular concept

      - possible definition routes for the concept of 'equality' are given in FIG 16. Alternate definition routes

    - concept-system interface:
      - what concepts are likely to evolve in a system
      - what concepts are common to most systems (would help identify concepts like an efficiency)

  - examples:

    - create a program that checks if a system is robust automatically, regardless of which system
    - what would a concept like 'robust' mean for a system?
      - given the definition route to 'robust' as 'strong enough to withstand various circumstances'
        - you can infer that if a system is robust, it can retain its structure despite application of various change types
        - so query for change types in that system
        - then check which change types break the system & the ratio of (change types handled/total change types)
        - assign a ratio to 'strong' adjective
        - check if the change type handled ratio is above or below the strong ratio
        - if above, the system is 'robust'


## Function Analysis

  - this interface extends the core function definition of the object format, which refers to any logical rule, and applies a comprehensive definition that can standardize & describe the function potential of other objects

  - definition: a function can be any of the following general types:
    - rule: a static function
    - function: rule tree, composed of:
      - conditions (if/for/while/validation/organization)
      - assignments/relationships (equate an attribute with a value)
      - processes (an altering process like format, a routing process like return, etc)
    - intent: purpose for a function (at granular layers or in strict environments, purpose can be tightly aligned with the function logic, with no side effects)
    - role: function & a position in a system
    - pattern: sequence or other relationship structure of specific/identified objects (like a sequence of rules, filters, or values)
    - connection: causal relationship (some type of interaction occurs)
    - insight: important/relevant/new/unique/abstract/cross-system relationship
    - strategy: insight & a plan intent on how to implement it, usually to achieve a specific goal intent

  - attributes:
    - state
    - context
    - complexity
    - environment
    - optimization potential
    - alternative potential
    - function type (core/boundary/abstract/change/potential)

  - functions:
  
    - info functions:
      - alternate
      - limit
      - enable
      - format
      - organize
      - generalize/specify
      - validate
      - track
      - decide
      - enforce
      - conflict/resolve
      - learn/optimize/correct/update
      - neutralize
      - store/restore
      - equate/differentiate (key points of difference)
      - interface functions (change, intent, type, pattern, concept, problem, strategy, insight, game, perspective)
        - uncertainty/risk/potential/prediction functions
        - solution functions (variance/stressor/error detection, tracing, identification & handler)
      - change
        - update
        - distort (gap creation, divergence)
        - standardize
        - maintain/regulate
        - potential 
          - conversion (adjacence, or what can it be transformed into using available functions)

    - core functions
      - foundation functions: enable other functionality to develop on foundation structures
      - granular functions (reverse, shift, add)
      - general functions:
        - convert (change)
        - apply (format, filter, function, etc)
        - find (find important objects/rules/variables/layers/systems)
        - identify
        - generate (using limits, filters, logic objects, structures, interfaces, symmetries, variables)
        - derive (a combination of deconstruct, match structure, assemble/isolate structure, fill structure)
        - define

    - structure functions
      - compress, expand, limit, position, convert, route, mark, distribute
      - format
      - match
      - fill (gap closing, convergence)
      - fit (path/structure derivation, path evolution in isolation & with other factors)
      - filter (reduce)
      - map (using various versions of structure/fit/format/convert functions like position/combine, and various identification functions like calculate/approximate/measure)
      - interact (combine, isolate, chain, connect, interact, contain, compete, share, coordinate, equate, group, overlap, overload, merge, trade, mix, union, intersection, inject, embed)
      
    - automation
      - function operations: resolve function definition, find functionality, index function metadata, chain functions, function-modifying/generating functions
      - interim functions: provide resources used as inputs to activate other functions (a set of molecules that when detached can activate other processes) 
      - metadata functions: find definition/attribute/object/function
        
    - dependency
      - assume
      - expect
      - contextualize

    - attribute
      - state functions
      - update attribute
      - scope (use case, relevance, lifecycle, self-destruct triggers, context, range)

  - objects:
    - errors
    - assumptions
    - input/output parameters & parameter types
    - definitions of concepts like equivalence, specific to that function

  - structures:
    - formats: core functions, filters, sequences, limits, network/tree representation, probabilities, attributes

  - concepts:

  - answers questions like:
    - is this function applicable to itself
    - is this function optimized
    - is this function usable for a range of intents or specific intents
    - what is the best format for this function
    - should this function have multiple formats or structures which are called in different contexts
    - should this function be stored as an abstract structure or code query and generated/retrieved at run-time or stored as a specific implementation
    - function-system interface question: is this function necessary for the system
    - what functions are adjacent to this function (similar to the function, or efficiently buildable with the same core functions or associated/available distortion functions)


## Intent Analysis

  - definition:
    - intent can be defined as possible reasons to use a function (or use an object as a function):
      - possible outputs (including the explicit intended output, resource access/usage like memory retrieval, object lock, routing information to a function while it's being looked for elsewhere, or processing usage, and side effects)
      - explicit intents ('calculate x')
      - implied intents (the implication of an intent like 'calculate x' is to 'use the output of that calculation to make another decision')
      - embedded intents (implementing a function optimally has an embedded intent of 'optimize this function')
      - injectable intents (intents that can be injected into a range of functions, like the 'use processing power' intent can be injected into any function)

  - attributes:
    - implication
    - directness
    - alignment

  - functions:
    - allow combination of intents to find malicious intent structures (like a sequence of neutral-intent functions that has an emergent malicious intent when used in that sequence)
    - operate on intents (intent-modification intent)
    - derive intent as a dependency of the intent interface conversion function 
    - map intent to direction & assess solution progress by movement in that direction

    - mapping intent to structure & vice versa is shown in FIG 13 (Intent-matching)

  - structures:
    - intent matrix is the interaction space of a set of intents, where its emergent intents can be traced across the interaction space
    - intent stack is the set of adjacent intents of a function, from granular/neutral/abstract to specific/explicit, across various interfaces like logic, abstraction, & structure

  - answers questions like:

    - which intents should follow or be combined with which intents
    - which intents are missing, given an overall function intent
    - which intents do the optimized/simplest/reusable function versions fulfill
    - intent-logic interface question: which intents align with logical objects (assumptions, conclusions)
    - intent-system interface question: which intents are common to all functions in the system
    - intent-function interface questions:
      - which functions are most exploitable for malicious/neutral intents
      - which functions' explicit intents dont match their implicit intents (or emergent intents when combined with other functions), which is like analyzing the structural difference between developer expectation vs. user intention
    - do variable, type, logical, & output intents match overall given function intent
    - what is the logical sequence that best fulfills this intent (useful for automating code generation)
      - what is the function linking these variables, given the variable intents a, b, c and the combination intent matrix ab, bc, ca, and the possible output intents of that matrix, and similarity to output intent of y

  - objects:
    - priorities: abstract directions that intents may fulfill or move agents toward, whereas intents are more granular

  - concepts:


## Pattern Analysis

  - definition:
    - a pattern can include a function (the pattern being a sequence of logical steps) but it is different from a function in that it is more abstract & can include other structures, and the point of the pattern is not to get a particular object like the function output, but to identify common trends across systems so the pattern can be used for inference or value generation
    - a pattern is a relationship between objects, the point of storing which is to identify repeated relationships
    - the relationship between objects is not the only part of the pattern that matters - the actual object identities may be an integral part of the pattern
    - for instance the pattern '1 1 2 3 5' may have a relationship like 'a subset of the fibonacci sequence' but it also may be important that the sequence starts at 1 (the initial object identity) because it may be used for calculation
    - so the trajectory mapped by the pattern may not be all that matters - the starting/ending points or values of the pattern may also be relevant
    - this is different from a function which would have abstract starting/ending points in addition to the sequence of logical steps, to govern where the function can be used
    - patterns that are common across systems imply a level of increased probability of that pattern occurring in other systems, so patterns can be used to infer attributes like probability

  - functions:
    - generator: generates a pattern given parameters
    - compress (reduce the pattern to a generator function)
    - expand (generate a sequence using a generator function)
    - implement (apply a generator or sequence to a structure in a context)

  - attributes:
    - abstraction: a pattern can be a pattern of specific values (1, 2, 3, 4), the metadata of those values (type: int int int int, divisor attribute: odd even odd even, exclusive divisor attribute: prime prime prime not-prime), or an abstract version of the values (number, pair/number of points required for a line, sides of a triangle, number of players required for a game), or a mix of these
    - structure: a pattern can include any structured information, including a set of logical steps, a set of attribute values, a list of events, a query on a graph, a trajectory in a tree, a list of numbers representing feature values, etc

  - objects:
    - components: any type of structured information is allowed in patterns (values like integers, words, other patterns, references to objects, etc)

  - structures:
    - sequence: sequential pattern
    - network: a pattern of relationships

  - concepts:

  - answers questions like:
    - what would the path between inputs/output probably be, given patterns of other paths
    - what is the function linking these variables, given common function patterns between variables of these types/topics/ranges/other metadata?


## Logic Analysis

	- definition:
    - this analysis can include related interfaces of logic (patterns, functions, intent, cause, change)
    - this analysis is used at its most basic level for identifying valid rules ('x, so y' or 'x, so not z')
    - relevant logical objects with defined rules include assumptions, requirements, implications, conclusions, fallacies, inferences, etc, and logical structures like sequences, connections, alternatives which follow the rules of logic (some rules have to follow other rules, logically, so their appropriate structure is a sequence - whereas some rules cannot be implemented simultaneously like mutually exclusive rules, so their appropriate structure is a tree branch)
    - using these logical object definitions & associated logical structures, you can derive what is logical in any given rule set
    - this means you can derive emergent structures of possible error contexts/rules, like: 
      - when there is a difference between the implication of a rule and the implementation of handlers for that rule, there is an opportunity for misuse of that rule
        - if you have logic to handle the 'dog chases cat' rule but you dont have logic to connect & handle the causes of that including 'the cat did something', then the 'dog chases cat' scenario could cause variance in the system, such as being used out of context (even when the cat did not do something), or not being prevented in the system (by handling what the cat did to prevent the chase event)
      - when an assumption may seem to fit in a system where its applied (assume that people are biased), but the implications of that assumption dont fit the system (the system user/designer/implementer may also be biased), the assumption shouldnt be used or should be adjusted to fit the system (all agents are potentially biased at any point because bias is part of the learning process)
	  - enables automation of the selection, structurization (limiting, connecting, scoping, positioning), optimization (reducing number of rules or high-cost rules or distributing/reducing costs better), & implementation of logical rules

	- examples:

      - variable1 is not checked for False (theres a gap in enforcement between the None & False definitions) so the operation could fail
  			if variable1 is None:
  				return False
  			return operation(variable1)

      - theres a potential gap in enforcement of data type, where variable1 might not be an integer even if its positive
  			if variable1 <= 0:
  				return False
  			return int(variable1)

       - there's an unnecessary condition which is invalidated by prior code (if variable1 is not defined, it would never get to the third line, so the third line is unnecesary)
  			if not variable1:
  				return False
  			if variable1:

	- functions:
		- function to identify logical problem types
			- gaps in logic enforcement (variance gaps, fallacies, incorrect contexts, assumptions)
			- overlapping/repeated logic checks (extraneous validation)
			- side effects that don't match function logic objects, like implication

		- logic correction functions
			- identify isolated logic operations
			- identify scope required of each operation
			- identify required position of each isolated logic operation

  - attributes:
    - cohesion: measure of system fit (like fit to a 'common sense' or 'pattern' system)
    - validity

  - objects:
    - logical fallacy: mismatch of logic structures/functions/objects/attributes (scope, relevance, fit, position)
    - assumption: depending on information, like the relevance of a particular rule or insight, as if it is true (or an adjacent/alternative definition of truth, like relevance or fit)
    - implication: context implied by a logical structure:
      - 'dog chases cat' implies context of a prior event like the:
        - 'cat did something' (implies a system where there is a reason of responsibility for every decision or fairness in allocating costs)
          - 'the dog wants something the cat stole' (specific implication)
        - 'the dog is bored' (implies a system where there is lack of work allocation and attention/work are not maximized/optimized)
          - 'the dog doesnt have toys' (specific implication)
        - 'the dog wasnt trained' (implies a system where default behaviors like instincts can be relearned)

      - a headline like 'politician takes a bribe' has implications of relevant context of prior events, like: 
        - 'this is newsworthy since it doesnt happen all the time' (infer a system that doesnt often produce crimes of corruption)
        - 'this is one of the politicians who were caught taking a bribe' (infer a system that is bad at catching criminals)
        - 'this is one of the politicians who the newspaper doesnt like' (infer a system where bias is present in information sources)
        - 'the politician agreed to take the hit for someone else' (infer a system where favors are traded, sometimes to give impressions of false information to protect social assets like reputation)
        - 'the politician was tricked into taking a bribe unknowingly' (infer a system where tricks & liars are common)
        - 'the politician was sacrificed as a scapegoat' (infer a system where criminals' costs are allocated to innocent people)
        - 'this coverage is to pretend the police were making progress against corruption, even though other politicians were also known to take a bribe without the news coverage' (infer a system where information sources enable authorities to hide information about their own decisions that is negative to keep power)

      with varying levels of probability (the more work it takes to generate the justification for an implication, the less likely it is to be true)
    - justification
      - alignment of logical objects (conclusions/assumptions) & related decision objects (patterns, intents) with distortion functions producing the decisions
    - explanation
      - description of logical objects & structures that connect a starting & end rule
        - an explanation of 'how' is a structural route, an explanation of 'why' is a causal route
    - conclusion
      - a logical rule converted into an assumption
    - contradiction
      - a mismatch between rules
      - specific case is a paradox, which is a false contradiction (often from different definitions or scopes of common objects between the rules)
    - inference/deduction
      - matching logical structures
        - if the dog wont stop chasing the cat, someone can infer inferences like that it doesnt want to or that it cannot regulate itself or that it doesnt have other options in another way, like lack of information about negative consequences
      - inferences are potential logical connections, whereas implications are probable logical connections
  - structures:
    - logical sequence (logic that has a position attribute, where it has to follow or be followed by other logic)
    - logic tree (logic with contradictory alternatives that cannot occur simultaneously, to handle different conditions)
    - logical connection (logic that enables other logic, because their inputs, outputs, & objects like implications match rather than contradict each other)
    - logical circle (a logic structure that depends on its output)

  - concepts:

  - answers questions like:
    - is this rule logical or does it have logical errors like contradictions
    - do these rules contradict each other
    - does this rule fit the system it's used in
    - is this assumption valid
    - are these rules fit to the right logical structure 
    - does this rule prohibit another rule
    - should this rule follow this other rule
    - what is the implication of this rule


## Structural Analysis

	- definition:
    - indexing objects by structure allows clear matching of useful structures to objects/attributes/types/rules
    - this allows objects to be graphed in a standard way, which means translating objects like problems into a computable interface
  
  - examples:
    - market structure analysis
      - the market interface is a standard interface where resources (goods, labor, time, risk, information, expectations, theories, & stored prior labor (currency)) are traded
      - a useful new way to use this is to frame non-resource objects as resources (systems, structures, positions, paths, directions, risk chains, trade loops, markets)
      - then you can apply traditional market analysis (optimal transport) to find, for example, the optimal set of trades to change an industry's position

    - for a problem of type 'conflict', like vectors aiming at a corner of a closed shape (where the shape is formed by the intersections of limiting attributes), the structural way to solve that problem is:

      - reducing the angle of the corner 
        which reduces the difference between corners (and the incentive to aim for a corner) & adds extra alternatives
        - the solution is an example of 'false limit' - the limit of there being a finite supply of corners or the limit of one route occupying a position at a given time can be surmounted with extra resources
      - reducing incentive to aim at corners
        - if the shape has fewer corners, there will be less incentive for internal vectors to aim there
      - reducing motion
        - if the shape has a stable state, the motion of the internal vectors can be reduced or staggered at intervals for resource-distribution
      - adding motion
        - use types of motion to distribute the vectors so they aim at different corners

    - you could apply these methods of solving the structural problem to the original problem 
      (a conflict like competition or overflow or false limit or false alignment if the vectors dont need to aim for the same corner)

    - the way to assign 'conflict' problem type to the closed shape structure with internal vectors is by aligning attributes 
      (incentives that organize motion to create an oversupply of resources (motion vectors) that cant be supported by a resource (position))
   
  - functions:
    - find important structures (combinations/layers)
    - find matching structures
    - find differences
    - find sub-components
    - map structures (function sets) to target structures (sequences), given a metric like progression toward goal
      - identify sub-components
      - a function to convert an object between formats (function => attribute sequence, function => filter sequence, etc) by mapping attributes & functions & other metadata of the objects & removing attributes that don't fit in the target format definition (for example, if you're converting to a type, the output should be in an attribute set format) 
      - a function to identify structure matching a pattern (like identify a structure embodying a mismatch, which is a problem type, given a system network definition, where the system could represent an object, function, or attribute) 

  - structures: 
    - dimension
    - layer: parameter determining variance accretion interfaces where interactions develop
    - space: dimension set
    - scale, range, spectrum
    - group: set, potentially across dimensions (cluster of data points)
    - position
    - line: position link
    - sequence
    - center: possible in a shape with symmetries
    - vector: line with restricted metadata (direction & magnitude)
    - circuit: series of lines moving at angles that allow returning to origin point
    - network: linked points
    - tree: network with direction
    - stack: layers representing variables or variants within a type with values (trajectory between points in layers)
    - topology, manifold: permutation set with symmetric properties
    - distance: variance in a similarity measure
    - origin: starting point
    - point: value set of dimensions
    - angle: comparative measure of divergence between paths with same starting point
    - direction: output attribute from input origin given a space-traversal object (line)
    - boundary/edge/limit: extremes of resource combination generative potential
    - inflection: metric change limit (maxima/minima of rate of change)
    - intersection: conflict/overlap
    - tangent: line of least nonzero interactions with another line
    - ratio
    - symmetry
    - scalar
    - path
    - expansion
    - progression
    - distribution

  - attributes:
    - order 
    - balance
    - equivalence/similarity
    - accuracy/fit
    - position

  - objects:
    - comparison
    - combination
    - permutation
    - approximation
    - metric
    - activator
    - trade/cost/benefit
    - change
    - filter

  - concepts:
    - equivalent, alternate, substitute, opposite, inverse

  - answers questions like:
    - how to identify components with structural attributes like chainability (cause, risk, variance, errors, gaps, limits) or variability
    - how to identify a shape fitting information: chain/stack/network/mix/layer, adjacent shapes, or emergent info shapes like alignments/gaps/conflicts
        - will a type stack (which type values on different type layers) or a network/tree (type hierarchy) be a more useful structure to capture a type relationship
    - identify compression/conversion functions of a shape


## Potential Analysis

  - definition:
    - variance is semantically the opposite index (gap/unenforcement/missing information/randomness) to the filter index (limit/structure/information/organization)
      - delegation of variance into systems/types/functions/variables/constantso
        
  - functions:
    - identify high-risk variables
    - identify imminent variable changes

  - attributes:
    - structure (potential being lack of information, and information being structure)

  - objects:

  - structures:
    - certainty structures (patterns, rules, constants, assumptions, limits, metrics, information, similarities/matches/alignments (intents/incentives, demand/supply, limit/variation), definitions)
    - uncertainty structures
      - variance structures (gap, leak, cascades/catalysts, accretions/injections, compounding variance, variance building a new interface, variance distribution/alignment, unenforced rules, measurement limits, open systems)
      - potential structures (unused paths/energy/combinations, adjacent states accessible with existing/available resources)
      - change structures (variables, dependencies, updates, replacements, distortions)
    - interaction layer (layer on which objects are likely to interact)
    - interaction space (set of possible interactions)
    - potential field (range of potential states or positions)

  - concepts:
    - randomness
    - risk/probability
    - opportunity
    - certainty
    - variance
    - enforcement/validation

  - answers questions like:
    - what is the conversion potential of this object given its functions
    - what is the interaction space of this object
    - predict which system filters will be useful based on a system priority
    - this is the problem of adding/fitting/reducing structure from a gap in structure, which can be used to solve problems like:
      - prediction
        - which variables are explanatory, given what we can measure
      - causation
        - how alternatives can converge to the same level of variance or change patterns
    - reducing gaps in rule enforcement to shapes/paths has its own set of rules
    - this interface can also be used for specific attribute analysis, of properties that descend from concepts & take form in a specific problem space:
      - the power concept interface (has structures that look like trust, info, etc)
      - the balance concept interface (has structures that look like symmetry, justice, etc)
    - what type of variable is it? (object-differentiating/identifying attribute, emergent specific/abstract property, direct function input/output)
      - how does the variable relate to other variables? (decisive metric, substitutable alternative, collinear)
      - at what point does a variable become relevant to another variable interaction layer?
      - how do constants accrete between rules, like caps to keep variance from flowing in to corners or creating boundary-invalidating openings in a system/component boundary?
      - what causes variables to cascade across layers, creating fractal variables?
      - what is the path definitely not, based on various maximized measures of similarity?
      - what attributes & attribute sets & attribute dependency trees differ
      - what is transformation cost/potential between objects
      - what is divergence distance between generative paths for each object
      - what is the probable function linking these variables, given that it is an adjacent transform of a square (related function type), & a distant transform of a manifold (unrelated function type)?
    - how does a system become overwhelmed with variance (in various forms, including randomness), does it have outlets like interfaces with other systems to delegate variance


## Change Analysis

  - definition:

    - change analysis relates to information interfaces (question, problem), logical interfaces (function, intent, pattern) and potential interfaces (variance, risk, certainty)
    - change analysis analyzes relationships between objects/attributes/functions
    - change analysis is important for identifying:
      - how relationship structures (distortions, origins, combinations, sequences) relate
      - when change is imminent to assess the value of identifying future states (gather more data for a prediction function, implement versioning, build interfaces for change into the function by parameterizing/abstracting it)
      - what is the best way to frame a change (on what base, with what variables that describe the change, in what spaces/systems, as a combination of what functions, as a change of what uniqueness)

	- examples:

		- when finding a method to approximate area of a square with an arc on one side, rather than deriving an integration method for the non-linear side, it may be more efficient to arrange questions to solve the problem based on change:

      - question sequence based on change:

        - 'what is the non-linear object definition' (arc) 
          - 'how does area change with angle of arc' (in proportion to degree of distortion from line)
            - 'what distortion functions generate the arc from the distortion degree'
              - 'what distortion is present in the observed object'

        - this is a specific case of answering the general question:

          - 'how does this parameter (area) change with respect to distortion from default object (line)' - a question that can be broken into the questions:
            - 'what degree of distortion is the different object (arc) at' (how many distorting n iterations build the arc from the line, which is similar to calculating the log base line of the arc, given the available distortion operation to connect them)
              - 'what is the impact of each distortion on the parameter (area)' (what is the impact of each distorting n iteration on area)
              
        - it's also like calculating: (number of distortions between line & arc) ^ (impact of each distortion on area) = difference in area between line & arc
          using a pattern of change (impact of distortions on area) instead of calculating a way to approximate the area parameter with integration (aggregating subsets that are easier to calculate)

  - functions:
    - derive change
    - derive change base
    - differentiate
    - convert: change a component into another (useful for identifying alternate paths)
    - deconstruct: change an object into its components (useful for identifying origins & common components)
    - distort: apply a distortion function to acquire a difference object (a value difference, an extreme, a magnification, a limit, etc)
    - map change types to dimensions
    - identifying dimensions where change types change (an aggregate, interface, or deciding dimension where change type is uncertain but not random), with embedded parameters & bases for framing changes of a certain type      

  - attributes:
    - uniqueness (is the change composable with core distortion functions or is it formed with different functions than other changes, implying its origin is external to the system)
    - inevitability (is the change pre-determined by the system, in which case its just a continuation of a state progression rather than a fundamental change or source of variance)
    - directness (adjacent change)
    - explicit/implicit (certain/uncertain change)
    - degree (how much was changed, to what level of distortion)
    - change types (create, cause, force, guarantee, convert, enable, depend, connect, structure)

  - objects:
    - equality (alternate, interchangeable)
    - difference (extreme, opposite, contradictory)
    - change source

  - structures:
    - base: varying change bases (what a change's differentiating output is defined in terms of/in relation to) allows various difference types to be measured (removing common parameters/attributes or standardizing by a base), such as change defined as:
      - network position change
      - work to create the change (inevitability)
      - different ways to create the change (if there are many ways to create it, each individual way is insignificant)
      - attribute value change
      - context/system change
      - difference from different origins (randomness, core, default, etc)
      - change in change structures (change stack, circuit, sequence) or functions (derive change, derive change base, convert, differentiate)
      - state change (requiring a new position on a state network)
      - variable change (requiring more/less/new variables or fundamentally altered versions of existing variables)
      - adjacent similarities ('if you remove attribute x, are they equal?')
      - interface change (what interfaces are adjacent/determining/generative/differentiating across the change)
      - interface objects (what concepts/intents differ, does potential increase, are other change types enabled across the change)
      - change based on system vertices (imminent to/distant from a phase shift, at an intersection, changing interaction layers)

  - concepts:
    - base
  
  - answers questions like:
    - as change increases:
      - how do interface objects (functionality/intent/potential) or change objects (structures/functions/variables/embedded parameters/spaces) change
      - which standards/interfaces/change types are adjacent (change framed based on deviation from a standard, like deviating from the correct order or probability distribution, measured by degree of stacked distortions)
      - which difference definition applies (changes framed based on difference type, including difference from value, symmetry, limit, origin, number type, pattern)
      - what probabilities/possibilities become possible/adjacent (adjacent meaning findable/generatable in structural dimensions/on the structural interface)
    - as a concept having structure (like power: degree of independence) changes, does the change definition erode (previously distant points become more equal to adjacent points, so the meaning of information about position/dependency erodes, as power to move between them increases)
    - where can change be stored/routed in a system: if there is demand for change (stressors demanding new functionality) but all components but one are maximizing their change handlers, then you know theres one potential variable where change will gather/be routed, if its possible to route change from the variance injection point to that variable's causal stack at some layer/point


## Causal Analysis

  - definition:
    - cause is defined as dependency

  - functions:
    - resolve: identify cause in a set of possible alternate causes
    - isolate: identify contribution of a particular cause to an output
    - inject/extract dependency
    - identify causal structure, as shown in FIG 14 (Causal structure-matching)

  - attributes:
    - directness (x indirectly causes y, x immediately precedes y on a causal chain)
    - explicit/implicit (x is defined to cause y or x implies y)
    - abstraction (x specifically causes y)
    - isolatability (x is guaranteed to cause y and nothing else does)
    - interchangeability/ambiguity (number of alternative causes that cannot be resolved or eliminated or invalidated)
    - degree (x is n degrees of cause away from y)
    - requirement/probability of cause (if x this hadnt caused y, something else in the system probably would have caused y anyway, given all the similar structures in the system that interact with y, so x is not a required cause of y)
    - inevitability (x must cause y regardless of most possible system contexts)
    - dominance (x is almost always causative if allowed to interact with any object - example 'a source of power')
    - direction (x is always an output so it couldnt have caused y)
    - proxy (x is a proxy for z, so x & z are not both required to explain y)
    - function (x is descriptive rather than generative so it cannot be a cause)
    - difference from randomness
    - difference between actual/possible functions (if an agent doesnt solve a problem, but they could have efficiently solved it, is the problem caused by them or its origin)
    - hierarchical

  - objects:
    - dependencies

  - structures:
    - tree: directed causal network with an origin
    - network: network with functions having a direction attribute
    - direction: causes that fulfill directions representing priorities
    - stack: set of adjacent (or other definition of relevant) causes
    - chain/sequence: connected causes in a direction
    - loop (a function that generates information may end up using that information or its side effects like decisions as an input)

  - concepts:
    - interface: interfaces are causative in that they enable change to develop
    - causative structures: some structures like limits are particularly causative

  - answers questions like:
    - given the position between these causal factors, which causal patterns are likeliest?
    - given that a species occupies an interim position between evolution, efficiency, time, and environment, what is the likeliest causal shape linking a species with its environment?
      - for more evolved organisms, this is a network causal shape, though species with less developed cognitive ability may have simple or uni-directional shapes with environment
    - what is the function linking these variables, given these functions linking other adjacent generating variables/functions further up/down the causal shape


## Insight Analysis

  - definition: an insight path is a reusable cross-system pattern, usually built out of core functions from a general interface filter (type, intent, function, structure), that allows generation of insights. It can be as simple as a function like differentiate, a standardizing attribute like relevance, or involve a standard object like a simplifying question. It does not refer to specific strategies unless those strategies can be used to generate insights. Insight paths usually consist of abstract or structural rules like 'match structure' or 'identify type'.

  - attributes:

  - functions:
    - apply/derive an insight path, shown in FIG 12 (Insight path application)
    - link insights
    - identify insight

  - objects:

  - concepts:

  - examples:

    - a unit example is 'trial and error' or 'statistical regression' or 'break up the problem into smaller problems & solve them separately, then aggregate solution output' - these are standard abstract rule sets/sequences to apply when discovering new insights in a system, which can be used across systems. You can call these specific strategies, but they can also be considered insight-generators or solution-filters, as they can reduce the solution space when narrowing down possible insights describing a link to the correct linking rule. These examples are not always ideal/efficient so they're not top priority methods, but they're a good example of what position an insight path occupies in a system. 

    - an actual useful insight path would solve a common, abstract difficult problem, like 'generating the idea of regression', which would be something like:
      - query for concept adjacent to balance/equivalence in the context of a data set output (average)
      - apply the concept of average to indicate a general average distance within output range specified by input format (point subsets) in an input (data set)
      - find a definition of 'average between output ranges of point subsets' that matches the change type you're aiming for (ie, least squares)
      - find a definition of the format 'point subsets' that matches your average definition (adjacent points with euclidean distance definition, in subsets of the data set with a particular change rate)
      - format the input (calculate the data set subsets) using the 'point subsets' definition
      - apply the definition for 'average between output ranges of point subsets' to the formatted input (calculated data set subsets)

  - answers questions like:
    - what rules are useful across systems?
    - what rules are derivable given a set of structures that commonly appear in systems?
    - what are common rules used for previous insights, and how can they be optimized (shortening an insight path with a set of simplifying/standardizing questions)


## Info Analysis

  - definition:
    - information analysis involves: 
      - standardizing information formats, like standardizing to the object/attribute/function model (including related objects like state & type) so that information structures are clear & can be mapped to information problem types
      - information formatting (mapping the problem as a structure composed of information problem types, like an information mismatch/inequality/minimum/overflow/gap)
      - automatically finding definitions, examples, minimum information to solve, problem-solution matching, insight paths like question-identification functions, finding math structures to re-use math patterns to solve other problems, etc

  - attributes:
    - structure
    - format
    - organization
    - certainty (potential information, future information, measurable information)

  - functions:
    - match
    - fit
    - apply
    - build
    - derive
    - define

  - objects:

    - info objects relate to agents & their communication (perspective, strategy, decision, intent, priority, game, problem)
    
    - these objects can be defined as combinations of general interface objects (object/attribute/type) and core structures/functions/attributes

    - problems: sub-optimal state with identifiable problem structures (inequality, inefficiencies, conflicts, mismatches), where the sub-optimal state can be framed as a source-target node in a network, where the solution is the optimal route between them, a vector set to move source-target nodes to change the problem, a vector set to change the format of the problem or convert it to solved problems, a vector set to change the system the problem occupies to remove the problem structure (such as making the route or all routes lower cost, so finding a route is not a problem anymore), a shape that is fillable or reducible with a solution structure (component set or vector set), or a matching solution structure that otherwise invalidates the problem (a recharge/derivation/information function at each node to make each node equally useful)
    - questions: source & target node, implying a missing structure of the route connecting them ('how to get from a to b', 'why travel from a to b')
    - insights: newly identified rule between objects
    - strategies: insights with an associated context like related intents ('use this rule to achieve intent x'); efficient paths between points
    - patterns: a structure applied to information, where the pattern can refer to the structure or the information filling it
    - perspectives: a filter/priority/rule set, optionally having structures like object positions & default rules, produceable with a chain of distortions from a default perspective
    - examples: structure applied to a rule in a system, so the rule directly references system objects
    - conclusions: resulting output rules or emergent rules from a logical sequence
    - assumptions: structures like conditions or constants taken to be true for a particular context, like a particular intent (for the 'understanding' intent, assume the condition that the 'constant is zero')
    - implications: implications are structures implied but not specified by a definition (like how the existence of a floor is implied by the sentence 'the dog chased the cat'); used for deriving the context of an object - the structures nearby like related intents, the system context an object occupies, etc. Assumptions can be a subset of the implications of an object that are assumed to be true. Both assumptions and implications are pseudo-information that is not definitely true but is potentially true, and treated like true information for a given context like a period of time, during a discussion to learn something, or in the context of executing a function.
    - paradox: false illusion of a contradiction that is legitimate, valid, & logical
    - argument: position of objects or path between points with supporting connective functions
    - game: incentivized motion within a system having limits to prevent motion; a system with conflicting/overlapping intents between agents, usually with low-stakes intents
    - joke: difference between expected & actual position
    - error: difference between expected & actual outcome

  - structures:
    - asymmetry, imbalance, mismatch, excess, conflict, misalignment, lack, gap
    - formats (object format, system format, core format, compressed format)

      - these formats can be used to format a function
        - filter: barrier creating a difference between input & output (like a filter that allows only a particular data structure through, optionally altering that data structure as it passes through)
        - function: sequence of logical steps
        - limit: barrier reducing the potential motion of an object (like range of possible values of a variable, or set of variables collected into a type variable), which can be combined with other limits (corner of a shape, sides of a shape)
        - set: group of objects (like function components)
        - path: sequence of steps, which may be logical or produce logic
        - system: a bounded network (the structure of which may produce a function or allow it to develop)

  - concepts:
    - organization (format)

  - answers questions like:
    - is there a version of this function on the system, and in what format (a compressed/encrypted/generative format)
    - what is the sequence of questions that solves this problem this quickest
    - what is the network of problem types that this problem can be broken into (optimal transport, creating efficiencies/alignments, distributing costs to points where the costs are inputs, finding a prediction function, etc)
    - what is the set of patterns/filters/attributes that can describe this function
    - what is an example of this pattern (what form does the pattern take in a given system)
    - what would the optimal path be, given a certain intent, object identity, & host system?
    - what is the function linking these variables that is most efficient/involves fewest variables/involves known constants?
    - identify structures (layer/format) & objects needed to solve a problem
    - given a type stack progression, what is the likeliest position or extension of that stack?
    - given that these species evolved this way, what level of variance is the missing link between them likely to have?


## Problem Analysis

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

  - functions:

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
        - graph system as format 
        - graph the problem space, problem, related problem network (as shown in FIG 7), solution space, solution, embedded graphs, interfaces, and other relevant objects
          - the problem space metadata returned & displayed to the user is shown in FIG 3 (Problem Space Metadata), optionally including the solution metadata in FIG 4 (Solution Metadata) & additional solution metadata in alternate formats as shown in FIG 5 (Additional Solution Metadata), if a solution is found or if solution space information is found.
          - solution metadata function: deriving, evaluating & comparing solution metadata for solution selection
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
          - graph the problem on a network of related problems (on the same interaction layer, in the same problem space, etc) such as how the problem of building a technology is related to the problem of managing usage of & access to it
            - defining the problem space as a contextual system where the problem is active
              - this includes other problem spaces where it is or could be active
                - for example, how the 'tech distribution' problem (where most tech is inherently neutral & can be used for good or malicious intents so what matters most is how it's distributed) acts differently in different problem spaces where distribution tools & government ethics & policies differ
          - select the right format for the problem & solution is an important function in this analysis; each of those formats is better for different information, problem types/formats (with varying structure in the problem definition) & solution intents, but if you have a particular required solution format, you may need to translate a sub-optimal problem format into one associated with that solution format
            - each of those formats involves a set of vectors (which may represent a set of database/interface queries or insight paths, info objects like questions/insights/related problems, decisions/actions, causes/explanations, steps like removal/addition of variables, directed structures like distortions/intents, etc) which may be applicable in the interface network to retrieve/connect information, or in the problem space to reduce a problem shape, move around problem components to change the problem, or traverse a route in the problem network system (not necessarily the network of related problems, but the problem framed as requiring a solution route within a network)
        - select/add/remove problem dimensions 
        - identify/reduce solution space   
        - apply the solution to the problem space 
        - check if a structure (like a solution) fits/matches another structure (like input assumptions & limits or a solution metric)
          - checking if a solution matches a metric structure is shown in FIG 11 (Finding alternate solution formats that fulfill different metrics)
          - matching a problem format to a solution format is shown in FIG 9 (Problem formats, with matching solution formats of problem formats) and FIG 10 (Problem-solution structure matching: apply a solution function to a structure containing the problem to find specific solution structures for that problem)
        - compare & select between comparable solutions, including selecting solutions based on input preferences selected 
          (preferences like 'avoid using ML in solution', 'use a particular interface', 'use pre-computed solutions from database', etc)
        - decompose/aggregate problems/solutions (as shown in FIG 12)
          - break the problem space into sub-problems that can execute their own interface traversal & solution-matching process to find sub-solutions 
          - aggregate sub-solutions once solutions to sub-problems are found
        - format problem objects (like decisions) as structures (networks with clusters, sequences, & other structures)      
        - deriving trajectory between problem graphs where each graph represents a decision/state, and attribute sets & problem of similar type occupy a similar position on an axis depicting all the graphs traversed
        - representing a solution as a set of vector trajectories across interfaces
        - map related/approximate problems/problems by cause into a related problem network (like a generative vs. identification problem)
        - function to depict a problem space as:
          - the origin problem, defined as a set of structures indicating boundaries (filters, conditions), limits (assumptions, resource limits), or vectors (priorities, forces), creating the problem space (like limited tech creates a problem space) , where the space inside the shape indicates potential for change
            - the problem object can be represented differently according to the type & the solution generation method by applying interface filters to the problem space visualization, for example: 
              - if your problem object is represented as a 3-d shape like a cube (indicating it has three main variables expanding each other from an origin corner & forced to create a closed system to maintain state, or limits intersecting with each other), the solution would need to be in a vector format to remove dimensions of the shape or reduce the size of the problem shape 
              - for example, if you're representing your problem on the information interface, you may want to represent it as an information problem type within a system context, like how: 
                - a conflict between system incentives & agent intents could be represented as two vectors with the same origin or two vectors going in different directions 
                - an information imbalance would look like extra information in different positions 
                - an information asymmetry would look like information in a position where it's not needed & can be exploited
                - an information market would have some trust structures embedded, so information can be bought instead of derived for convenience
          - where the problem space dimensions maximize variance between related problems 
          - including a network of related problems in the problem space & their state, the origin problem occupying a position on the problem network 
          - the solution space for the origin problem (and for all related problems on the network that the solution space applies to) - the solution space being a reduced version of the problem shape or structure, or all changes possible in a problem space, or the set of all possible solutions, whichever is the most specific definition that can be identified
          - solutions to the origin problem, represented as solution formats like:
            - a structure within a system containing the problem (an optimal route with a required attribute like efficiency or a route answering a question, or a combination of objects reducing variance in a rule gap, or a filter sequence that creates a function optimally while storing minimal code)
            - a structure (other than reductions) to aim for when transforming the problem and the available resources implied in its definition (a solution defined as an optimal version of the problem structure, like the optimal structure to represent a concept or build a function) 
            - a reducing transform of the problem shape (solution vectors removing problem dimensions until it's a point) 
            - a problem-solving effect may be measured based on whether a solution contains or comprises a vector that: 
              - neutralizes a problem vector , applying force in opposing direction to a problem vector (reduce an incentive)
              - reduces the problem shape size  or dimension (resolve an ambiguity)
              - fills the problem shape with relevant structures (build a function, find a route)
              - or does any combination of the above for the origin problem & related problems, potentially neutralizing the problem space itself or converting it to another problem space. 

    - ezample logic of function to break a problem into sub-problems

      1. decompose a problem into sub-problems, using core functions like alternate/meta/find applied to problem objects (like how measurement is a core object of a solution, and the prediction function is the default solution object, and a variable is a sub-component object of the prediction function, and so on)
        - an example is breaking a problem into a problem of finding core components & arranging them in a way that passes filters formed by its solution requirements
          - a requirement of a function that follows another is a possible match of input/output, if the functions are dependent, rather than relatively independent functions (occupying different function sequences), thereby translating a requirement to a filter that can be used to reduce the solution space to only function sequences that have matching inputs/outputs.

      2. After sub-problems have individual solutions, you need a way to integrate the sub-solutions so they can solve the original problem

        - for example, once you have the problem broken into a set of filter structures to reduce the solution space, you need a way to arrange those filters so their output generates the solution (so that the input/output of the filters match, & the sequence of filters makes progress toward reducing the solution space).

        - the positions of each sub-problem set can be derived using logical positioning. A generative set should be followed by a measurement set because the output of the generative set (prediction function generated) matches the input of the measurement set (prediction function to measure); this involves a basic input-output chaining operation as mentioned before. A causal set may identify missing information in a variable set to establish cause between variables - that type of structure (missing information) should be followed either by generating the missing information, and if not generatable, should be integrated into the accuracy/confidence/error metrics, as not being able to find the information required to solve the problem (creating an accurate, robust prediction function).

    - example logic of function to find alternate solution formats in FIG 11 (Finding alternate solution formats that fulfill different metrics)

      - how to identify alternative solutions that would be interchangeable with this solution in various contexts (like for different solution metrics):

        - in other words, how to translate 'find optimal route fulfilling a metric' to an alternative interchangeable solution that makes the initial problem trivial to solve 'find system-wide cost-reduction function that makes system routes equally costly', at which point the original problem's solution is 'any route'.

        - we are looking for ways to invalidate the problem (generate an adjacent object to act as a proxy or replacement for the solution, generate the solution automatically, change the system structure so solving the problem isnt necessary, etc) rather than generate a specific solution (like how 'trial & error navigation of all possible routes' is a specific solution)

        - inference sequence using definitions & problem definition:
          - check definition:
            - 'route' is defined as 'a path between nodes in a network'
          - standardize definition:
            - 'optimal' can be removed because it means the same as 'fulfilling a metric' but adding 'fulfilling a metric the most' to translate it to the standardized form
          - find definition (of metric)
          - apply logic specific to metric definition, or general information-generating logic like a transform that doesnt change meaning in a context
            - if the metric is the general 'minimize cost' metric of an optimization, apply a transform ('abstract' or 'expand/apply/distribute' or 'change specificity attribute value to its extreme value') that doesn't change the meaning, to produce: 
              - 'minimize system costs' (which doesnt prevent minimize the original cost so it doesnt change the meaning in an invalidating way)
          - inject new version into original problem definition:
              - 'find route that minimizes system costs'
          - check if definitions match logically: 
            - a 'route' wouldnt necessarily produce a system cost-minimizing effect
          - if they don't match, apply transforms until they match:
            - abstract 'route' to get 'function':
              - 'find system cost-minimizing function'
          - check problem definition for extra information: 
            - the intent of the original problem was to minimize cost of a particular route, a problem that would be invalidated if all routes were equally costly; if we found a 'system cost-minimizing function' that minimized system costs, they might become equally costly, thereby invalidating the problem (invalidating it being one way of solving it), producing:
              - 'find a system cost-minimizing function that makes system costs equally likely'

        - different structures fulfill different structural solution metrics
          - if 'cost' is the metric, measured by total distance traveled, that is clearly different across the various solution formats of FIG 10.

      - FIG 6. Example of a problem-solving automation workflow, with a diagram.

          1. Problem definition: determine possible match between the problem system intersection object and the system conflict object.

          2. standardize the problem to the system interface

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
            - intent alignments (both agents have an incentive to
            apply social norms to maintain rule of law or trust, so their intents can be aligned to follow social rules to determine who traverses first, rather than building new rules to determine this).

          3. This step identifies whether the output of the previous step creates information that is easily transformed into the solution metric, given the relevant objects/attributes/functions of the solution metric. Is it clear which agent goes first, or whether the intersection can be changed in a way that determines which agent goes first?

          - If the solution metric 1 is fulfilled, the agents have no antagonistic agent attribute & there is no trade-off because no variance from a decision is allowed at the intersection.

          - If the solution metric 2 is fulfilled, the intersection loses its position overlap attribute & the diverging direction attribute doesn't matter anymore, but it does have a decision function at the intersection.

          - If the intersection object with the system interface is applied can be easily transformed into having one of the solution metrics fulfilled, that transformation can be considered a possible solution.


  - objects:

  - structures:

    - problem-solution formats (shown in FIG 9 (Problem formats, with matching solution formats) & FIG 10 (Problem-solution structure matching))

      - a vector set is good for converting between problem-solution structures, like converting an inefficiency to an efficiency in a system
        - problem shape-reducing vector set (where problem variables form the shape) is good for finding a function that reduces shape dimensions & size (like to form a summary), or a vector set to combine solution components in a way that fills the shape structure, if the solution format is a method to fill the problem structure rather than reducing the problem shape
        - a route optimization problem has the solution format of a vector set between network functions/nodes (where nodes are states/problems/objects, etc) that is optimal in some way (hits a node/path, moves in a direction, minimizes cost of traversal, etc)
          - with a network of states, the route can be a route between states with additional routes traversed within each state to convert to the next one (set of market states & trades to achieve a market intent)

      - structure-matching can be a good format for finding an example, finding a reason, or finding a causal structure of variables for a prediction function
        - an misalignment or mismatch (like an inefficiency, a conflict, or an information imbalance), where the solution format is the set of structures (which can be steps/vectors or applying a pattern or finding a structure in a network) necessary to correct the mismatch (minimize cost, align priorities, balance the information)
          
      - abstract format of a query (break problem into information problem types and then the solution is a query of solutions for each of those solved problems)

  - concepts:
      - anomaly/outlier
      - counterexample/contradiction
      - conflict
      - inefficiency
      - mismatch

  - attributes:

    - number of problem-causing variables/solution metrics fulfilled
    - complexity: 
          - number of core function steps required
          - number of variables
          - number of differences/inefficiencies
          - number of counterintuitive steps (requiring non-standard solutions)
          - number of contrary processes (requiring scoped/nuanced solutions)
    - abstraction (does it solve the same problem when framed on an abstraction layer above)
    - number of steps required to create problem from stable system state, once work is standardized, & adjacence of steps required
    - how much work is required to convert to a particular problem format (route, combination, composition)
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
            - intent mismatch
              - unintended use (involves integrated third party tech not under review)
                - unintended side effects: whether it's a closed system or leaks variance
                  - function side effect example:
                    - before execution: pre-computing
                    - during: memory access/overflow
                    - after: process re-starting

          - misidentification 
            - incorrect structure 
              - incorrect metric
              - incorrect information position (info leak)
              - incorrect organization

        - imbalances/inequalities
          - misdistribution of resources

        - inefficiencies
          - unmaximized benefit/cost ratio 
            - complexity
            - unnecessary work

        - gaps
          - missing information
            - ambiguity
              - ambiguous alternatives
          - gap in rule enforcement
            - gap in boundary
              - leaks (variance, resource/info)
              - injection point (assumptions/variance/control/randomness)

        - limits
          - limited resources/functions

      - specific problems:
        
        - malicious alternative route to get same output
        - legitimate/alternative route to get malicious output

    - solution types:
      - problem-metadata solution: evaluating problem metadata to evaluate metrics like problem-solving postponement
      - generative solution: solution that generates solutions
      - solution framework: provides starting point & structures for solutions to be built in/with
      - problem decomposer: solution that reduces a problem's root causative (as opposed to just varying) parameters
      - interim solution: clearly suboptimal solution while optimal alternative is built
      - solution query constructor: solution that builds new solutions out of known solution types (existing structural solutions or core functions)
      - structure-finding/fitting solution: solution that assigns a structure to information or matches the gaps/limits in a problem structure to neutralize them

  - examples:

      - examples of problem types on different interfaces:
        - system problems: inefficiency, conflict, mismatch
        - information problems: excessive information, conflicting information, information asymmetry
        - structural problems: unnecessary components, contradictory function requirements, mismatch in shapes
        - intent problems: adding specificity where unnecessary, intents that neutralize each other given position, sub-intents that dont match function intent
        - concept problems: excessive definition routes, overlap in definition routes across concepts, definition route that more adjacently matches another concept
        - logic problems: excessive assumptions, contradictory conclusion & assumption, using specific logic to make absolute inferences

    - example solutions

      - correct inequality (imbalance/mismatch) in a structural attribute (value, definition, direction, function, intent)
        - align objects (resolve conflicting objects like conflicting intents)
        - match objects (equate unequal objects like incentives/requirements, or expectations/intents, or opportunity/ability)
      
      - find structure
        
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

        - find objects, sub-interfaces & concepts in a problem system
          
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

    - answers questions like:
      - what are the problems (inefficiencies, conflicts, mismatches) in this system
      - what solutions are associated with this problem type
      - what problems are related to this problem
      - what problems will develop in this problem space system
      - what is the probable cost of solving this problem
      - what is the adjacent format of this problem


## Interface Analysis

  - objects:
    - interface
    - interface operation (combine interfaces, etc)
    - interface traversal (apply an interface to a problem)
    - interface query (cross multiple interfaces in a sequence)
    - workflow (apply a problem-solving automation workflow with a particular origin interface or interface query)
      - an example of a workflow is shown in FIG 6 (Problem-solving automation workflow)
      - the general workflow of this program is shown in FIG 2 (Solution Automation Module 140)

    - workflow operation (select a problem-solving automation workflow)

  - structures:

  - concepts:

  - definition: 

    - the interface network is the set of networks that act as useful filters/standards for applying structure to organize information, involving analysis like:

      - selecting those optimal interfaces to solve a problem: framing a conflict of type 'competition' as opposing direction/intent or equivalent direction/intent is a calculation that can be automated using any of these kinds of analysis, but the logic & intent interfaces are best at this
      - finding explanatory variables on multiple interfaces (a trajectory on the interface network) & translating them to a shared interface where possible
      - determining position/trajectory within an interface
      - selecting interface as the best standard for comparison (identifying when a particular specific interface will reduce solution set across any possible host system)
      - generating specific interfaces (filters) for a problem/space
      - generating full set of general interfaces (intent, concept, structure)
        - these can be generated by identifying the key differentiating factors across systems, which can be generated as system structures (like combinations of objects - type is an attribute set, intent is a function effect set, concept is a network of networks describing a structural concept (balance, power), structure is an information & rule set)
      - identifying all interfaces with variance that cant be captured in other interfaces
      - calculating when to skip interim variables/interfaces
      - determining adjacent interfaces

    - interface analysis also covers building or selecting a problem-solving automation workflow (whether to start with a particular workflow, which is a layer of abstraction above the question of whether to start with a particular interface, which assumes a workflow has already been selected)

    - the abstract interface network includes layers of network filters (intent, perspective, function (can include patterns, logic, strategies, core functions, and any other set of operations/objects that has order), structure, concept, information (organization, formats, types, info objects like problems/questions/insights/assumptions), potential, change, cause system)

  	- each interface network in the set of interfaces (core function interface network, general interface network, specific interface network) can be used to generate the others
  		- intent interface can be used to generate the type interface
  		- dependency interface can be used to generate the side effect interface
  		- interface network can be used to generate the core function interface

  - attributes:

    - generatability/common derivable core functions with other interfaces
    - information loss
    - variance focus (what variance is exaggerated for comparison by this interface)
    - position of interface on default interface network (what distortions produce this filter/perspective from unfiltered origin)

  - functions:

    - interface operation functions:

      - interface conversion function as shown in FIG 10 (Interface conversion & matching)
        - example: 
          - converting objects to the type interface involves identifying attribute sets that are unique, and then identifying types that can describe multiple unique objects as variations of an attribute in the attribute set
          - converting to the cause interface involves focusing on dependence objects (inputs/outputs)

      - function to design an interface query (sequence of traversing interfaces), as shown in FIG 11 (Interface traversal flow diagram)

        - which interface to standardize to in what structure (sequence/combination) depends on which use you intend to use the information for
          - if you need to implement it immediately, an interface like intent that is semantically adjacent to the structural & logical interfaces will be more useful
          - if you need to identify new types, standardizing to the type interface will be more useful
        - core functions (filter, find, apply, derive, build, change) mapped to user intents (identify cause, predict a variable, build a function) can generate & design a query on the interface network

        - example interface queries for problem statements:

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
                    - fit system (fitting the function to a system, formatted to include possible variance injection points, identify efficiencies like logic that can be merged, etc)
                    - identify structure (identifying structures that can be applied to the function system, like filters (conditions), direction changes (control flow statements), relationships (assignments), and mismatches (errors)
                    - identify potential (identifying unenforced rules, rule-intent imbalances, false similarities, & other objects of potential allowing exploit opportunities that are not already identified)
                    - change cause, intent, concept (test function impact on other causes, concepts, & intents, which are high-level objects a function can alter)
                    - match pattern (does this function comply with patterns for functions with similar solution metrics)

                  - if the function implementation doesnt fulfill solution metrics, other interface traversals can be done
                    - a system-object or function-concept interface like the 'efficiency interface' or 'ambiguity interface' (does this function have a more efficient or less ambiguous route between input & output that might fulfill a solution metric, given that maximizing efficiency & reducing ambiguity are standard system & function metrics)

              - problem: find an optimal route (or alternatively, find a distribution of functionality/efficiencies/costs to make all routes or a particular route less/equivalently costly) between start & end points, like the 'minimal trades to get equal problem/opportunity distribution'
                  
                  - interface traversal
                    - identify information (identify differentiating attributes/functions/sub-systems of agents/positions/routes within the network)
                    - fit system (identify relevant structures like abstraction layer to traverse at, identify important objects required to solve the problem, like trading problems/markets/skills/information/risk/bets vs. trading currency, or framing currency as a position attribute, rather than a standardizing interface)
                    - identify structure (identify trade & other market structures that are important for understanding why resources dont get distributed fairly, like closed trade loops & independence machines)
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
                          - next best case scenario type (if the unit solution type best case scenario doesnt occur iteratively) is pattern found & used to reduce solution/search space
                          - splitting requires multiple processes
                          - pattern logging/searching requires multiple processes
                          - depending on set, either can reduce solution space with extra work
                          - there is a trade-off between work invested in pattern-checking, subset-splitting & solution space reduction potential

      - function to select starting interface

        - Here's an example of why different interfaces are more useful in different situations, given a standard problem like 'build a function automatically for a given function intent'.

        Intent interface

          If you want to build a function automatically, and you have code indexed by intent, then you don't need to write code, you need to write the intent & sub-intent sequence or other structure. I would call that 'standardizing to the intent interface' or 'applying intent structures' to the overall function intent, which is the problem definition ('build a function with this overall intent'). If you already have code indexed by intent, framing a function as a set of intents is trivial. If you don't already have code indexed by intent, the process you use to decompose an overall function intent into a structure of sub-intents is a tool that can be re-used to index existing functions by intent.

        Information interface

          If the problem can be framed as an information problem, you can query information problem type rules & patterns to solve it automatically. Building a function automatically given an overall intent would mean:
                
            - solving a series of information problems like:
              - 'information mismatch' (object1 doesnt match object2 and it should, so assign object2 to object1)
              - 'conflicting information' (object1 doesnt match object2 so merge their conflicts) 
              - 'required information' (object1 is required to have this attribute value so assign it)
              - 'missing information' (object1 is missing this attribute so return False or query for that information or generate it).

        Cause interface

          If the problem can be framed as a cause problem, then you are querying for causes. Building a function automatically given an overall intent would mean: 

            - finding the causes of bugs
            - finding the causes of different types of logic & structures (like sequences) applied to different types of logic (inherent rules governing logic given the point/definition of logical operations, like 'an if condition usually precedes a non-if condition' because the point of an if condition is to test for a case to apply logic, where the logic applied is not another condition)
            - finding the causes of functions & function-related objects like side effects, memory usage, optimizations done on other functions, etc
            - then you'd compose these causes in a structure that would allow automatic generation of functions from a given intent (first apply logic-related causes to generate a function causing the given function intent, then check for optimization-causes in the generated function & apply optimizations if those causes are found in your generated function structure, then apply tests for bug causes, etc).

        Structure interface

          If the problem can be framed as a structure problem, then you are querying for structures. Building a function automatically given an overall intent would mean:

                - finding structures to standardize functions to (limits, filters, networks of relationships, directed networks of operations)
                - finding structures to standardize intents to (directions as priorities or more structural goals, possible usage ranges as intents, abstraction as an indicator of intent (neutral/mathematical functions can be used for anything), using intent as a proxy structure for the concept of permission by organizing information access by intent)
                - matching intent & function structures that fulfill the given overall function intent without causing invalidating side effect intents

        Pattern interface

          If the problem can be framed as a problem of resolving which patterns to combine in what structures (where patterns include abstract/generalized structures (such as variables, variable patterns, input-output path patterns, or type patterns) that resolve to specific logic when converted into information, meaning theyre assigned constants), building a function automatically given an overall intent would mean:
                
            - finding which patterns or alternative pattern sets (a variable type relationship pattern, an input-output type trajectory pattern, a logic sequence pattern, an optimization pattern) can generate the required logic when constants (specific information-filled versions of the abstract pattern structure) are applied
              - the output of that may be as diverse as an input-output table to handle a variety of use cases observed, a prediction function trained on input-output data, a logical sequence, a code query, an intent sequence, a directed logic network, etc - depending on the patterns used

        System interface

          If the problem can be framed as a problem of fitting the function to a system, building a function automatically given an overall intent would mean:
            - identifying starting & ending position to map intent to structure in the system (get from input start node to output end node)
            - identify default & alternative (higher cost, lower step count, etc) paths between start & end node
            - identifying system objects like efficiencies, incentives, etc, especially those structures clearly relevant to the default & alternative paths between start & end nodes identified
            - applying definitions of those system objects to select the logical step sequence (avoid conflicts, target rewards without side effects, minimize costs, apply symmetries for standardization purposes)
            - checking which routes fulfill given function intent

        Concept interface

          If the problem can be framed as a set of concepts required for the solution (framing the intent in terms of concepts like 'distribute power evenly'), or if you have conceptual information indexed for code, building a function automatically given an overall intent would mean:

            - using conceptual math operations to determine which structure of concepts is most useful for the given intent (if combining 'power' and 'efficiency' in a 'sequence' or 'balanced' structure would produce the optimal function for an intent like 'distribute power evenly', that is calculatable if you have other functions indexed by conceptual structures, or if you have conceptual math operations accessible to determine what structure of concepts would generate the required concept set, or if you have intent indexed by conceptual structures, or if you can standardize intent & concept to another interface where you have conceptual structures indexed, etc)
              - for example if you have functions indexed with conceptual structures like the individual concepts required (power, efficiency, distribution), what operations can be applied to these concepts to create the optimal concept combination ('distribute power evenly') - meaning conceptual operations like 'inject power to distribution structure', 'limit distribution structure with power injected by efficiency', etc.
              - these conceptual operations involve finding matching structures across the concept definitions:
                - 'injecting' power into a structure manifesting the 'distribution' concept is possible if the distribution-manifesting structure has an input opportunity of some structure, and power can be translated into a structure that can be used by the structure having that input opportunity (a distribution structure such as a function having an input opportunity in the form of a parameter, where power can be translated into a usable structure like information assigned to that parameter), given the definition of the 'inject' operation as 'input the injectable to the receiver'
              - you can avoid doing structural operations by storing the structures for each concept and then storing patterns/outputs of their operations
                - if combining power & efficiency produces a structure set, that can be derived by querying the structures of power & efficiency and combining those structures in a way that doesnt invalidate either definition
              - you can also apply logic to the concept operation ('inject power to distribution, limited by efficiency') to create the output concept of that conceptual operation ('efficient distribution of power'), and then do a structure query of that output concept
              - once you have function structures matching the output (having found function logic matching 'efficient distribution of power' once translated to the structural version 'minimized cost of allocating inputs' if inputs are the structure found in the function system matching the power definition, where 'minimized cost of allocating inputs' can mean 'diversifying calls for this intent across various alternative functions' or 're-using existing functions where possible to minimize the cost of building a function on-demand or at compile time' or 'a function set that minimizes the memory/space requirements of allocating inputs'), you check if those structures optimally fulfill this function's intent, 'distribute power evenly', and then execute the final steps to resolve those structures into function logic (with input-output requirement chains, intent-matching, etc)

        Problem interface

          If the problem can be framed as a problem in a problem network of related problems, and/or a problem space, you can calculate attributes like whether the problem is about to be invalidated by other functions built for other problems, whether the profit opportunity of solving the problem is worth the probable cost, whether the whole problem space is about to fundamentally change, etc. Building a function automatically given an overall intent would mean:

            - determining whether the problem of organizing logic is a solved problem if framed differently (can AI generate code with enough accuracy to invalidate further investment)
            - determining whether solving an adjacent or proxy problem invalidates solving this specific problem (can concept or intent identification tools or even existing code bases invalidate the need for a tool to build functions automatically, or can code bases be re-written in a way that invalidates automatic code generation, by simplifying code-writing to a task of intent-writing or code query-writing or another process simple enough to invalidate complex code and the need to generate it)
              - determining if a solution like logic automation can replace code generation (a tool that automatically applies the definition of logic, including all related objects like logical fallacies, to prevent logically 'jumping to conclusions' or 'ignoring assumptions' or 'over-applying bias vs. updating bias', then indexing code as these logical objects so logical rules can be applied to optimize/generate code)
                - this would involve writing high-level logic language like 'find information, avoid misidentifying object1 as object2, combine common attributes of these objects with versioning in case of conflicting values, avoid this conclusion & this fallacy error type', which would allow logical object definitions (of what a fallacy is, what a legitimate conclusion/assumption/implication is, etc) to be applied automatically, rather than the existing method of applying conditional/contextual/specific low-level logic developer-defined definitions to be applied manually, which involves writing low-level logic like 'select * from table, check if object1.attribute.value == object2.attribute.value, etc'.
            - determining whether the problem can be formatted as a set of solved problems (applying organization to information, applying definitions, finding matching structures, generating tests) or in a format that is solved (route optimization)

        - given the information you have, one interface may be more useful to standardize to than another. If you already have intent or cause information indexed or otherwise adjacently calculatable, or if those interfaces contain the required solution information (as in, the problem is 'finding the cause of some measurement', so the solution is going to be findable on the causal interface), you'd be better off standardizing to those interfaces first, without other information.

      - function to traverse an interface (apply an interface to a problem, looking for matching objects)

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
        
      - apply an interface as a standard to another interface:
          - intent / structure interface: assess intent interface by a standard of structure interface (which structures can simplify the intent interface)
      
          - concept-structure traversal (a multi-interface traversal linking the concept & structure interfaces, so a target concept combination/set/path or target structural attribute can be achieved with a combination of filters & limits or functions applied to adjust the structure until it matches the target structural attributes or concepts) 
            - general: - find a structure for a certain intent that matches a conceptual priority (like relevance, organization, robustness, equivalence, or trust) - modify a structure with a certain intent so it matches a conceptual priority (like power or a conceptual structure like power distribution) 
            - specific: - find a structure in the finance space that minimizes trust in transactions - modify a multiplication method to find a method minimizing larger calculations 
          
          - structure-math interface mapping 
            - general: use a multi-interface traversal to map problem structures to math objects to apply math insights to problem structures 
            - specific: if the problem is 'predict the shape of the boundary of an even distribution of change across directions from the same origin' (for problems like 'finding a container needed for an experiment growing microorganisms given the requirement of the same origin and non-overlapping paths', or 'predicting the threshold marker needed for comparing speed metrics'), apply the 'circle' definition route using the 'evenly distributed outward motion' route to infer that the boundary could be circular, with variable advantages depending on problem metadata 
          
          - a question-answer interface traversal 
            - general: frame a question as missing information structured as a source position and a target position on a network, and the answer as the most robust path, the most relevant path for a particular intent & objects related to it, the path that moves the nearest to the target position, or the quickest path that moves in the prioritized direction on the network 
            - specific: - frame a question like 'how to build a filter' as an optimal path-finding problem on the network between some undefined starting component set & the destination filter object - frame a question like 'why would you build a filter' as a adjacent object- finding problem to find objects that can be produced if the filter is the starting point (input) or to find intent directions moved in when you follows paths to build the filter (reasons to build it) or subsequent paths using the filter (other applications of the filter) 
  
      - merge interfaces:
          - function + pattern interface: merge networks of functions & patterns into one standard interface definition (input/output/logic + metadata of both objects)
      
      - expand an interface by another interface:

          - function * pattern interface: 
            function patterns (what patterns are there in functions), pattern functions (what functions generate patterns)
            function pattern functions (what functions generate function patterns), pattern function patterns (what patterns are there in functions that generate patterns)
          - cause * type interface: 
            causal type interface (what types of cause are there), type cause interface (what causes types)
            causal type cause (what causes causal types), type cause type (what types of type causes are there)


    - answers questions like:
        - patterns in ratios between uncertainty generated by a function combination vs. uncertainty-reduction function patterns & potential (how does it hide information vs. how can information be derived)
        - the relationship between the transformation function converting one space into another, and the transformation function converting a space's objects (like insights) to another space's objects
        - valid/invalid operations in a space
        - set of all possible spaces (fulfilling concept combinations) & link to the objects best described in that space whose differences are relevant to those concepts
        - within a description system, there will be rules linking objects (like a shape & another shape type) that align with inherent system attributes like symmetry: "given any line, an equilateral triangle can be constructed with the line as its base"
        - core operations done on one attribute (length) vs. another attribute (angle)
        - how core operations & objects accrete in a space (multiple, shift, embed) on every interface layer
        - spaces as the intersection of spectrum variables
        - derive object types with attributes useful for a particular operation ("quaternions for 3-d rotation")
        - value accretion into units (integers)
        - what patterns turn into objects that attract/hold (or provide a platform or conduit for) the most variance
        - attributes accrete into aggregate/type/emergent attributes ("equipollent when they are parallel, of the same length, and similarly oriented")

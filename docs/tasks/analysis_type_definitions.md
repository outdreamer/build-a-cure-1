# Analysis definitions

- reduce these to definitions of each type sufficient to understand & implement each type of analysis, optionally including implementation & target function lists
  
  - workflows
    
    - a workflow to automate problem-solving is an interface traversal that can be applied to any problem

    - if the problem is 'finding a structure that matches conceptual priorities like strength', that can clearly begin on the concept-structure traversal if information required for that traversal already exists in the problem definition or derived metadata

      - concept-structure interface traversal (a multi-interface traversal linking the concept & structure interfaces, so a target concept combination/set/path or target structural attribute can be achieved with structures like filters/limits/functions that adjust the origin structure until it matches the target structural attributes or concepts)

      - or you can standardize to the intent interface which is particularly effective at linking other interfaces (find intents & intent structures that fulfill the 'strength' attribute, and structures matching those intents)

    - other workflows can be derived given alternate traversals that can generate information (like how causation, information formats, functions, and intent can generate structure information), given existing information

      - problem-solution interface traversal: sometimes a sufficient solution may be already stored in the solution table (solution being an information object) and the way to solve the problem is formatting it correctly or identifying its type correctly so that solutions for that format or type can be queried & applied as-is, the most basic traversal type

    - these workflows can be generated with new interface combinations or interfaces, if each interface in the sequence can add information required to solve the problem

    - occasionally an interface will be sufficient on its own, if the problem is already pre-structured

      - the function interface may be enough to find the right sequence of functions, if the function metadata includes input/outputs and there are no ambiguities to resolve, meaning this solution is a simple query to match inputs/outputs, where the final output is the intended goal of the query

    - problem-solving automation workflows

      - these workflows apply various interfaces & analysis types, and can be applied to any problem

        I. Filter problem definition until it matches solution structure (using definition & standardization, applying increasing limits/filters/transforms until problem & solution match)
          - this applies structures such as limits to fulfill solution intents iteratively

        II. Solve problem with structure fitting (adapt probable solution structures to match problem definition)
          - this starts with core, probable, or difference-maximizing structures and applies additional structures until one is found that fulfills solution metrics

        III. Transforming problem into query of solved problems (using most adjacent solution formats)
          - converting the problem into a structure (set, sequence, network) of solved problems (like distributing power, resolving imbalances, etc), and then traversing that structure if multiple alternatives are found
          - this method can take the form of a simple database query ('fetch solutions for this problem type') in its most basic form

        IV. Solve problem with solution function generation & selection (optionally with pattern/intent-matching)
          - this uses the function interface to identify useful metrics to select functions to begin with when searching for a function to solve a problem (like 'calculate x') which can involve function metadata like identifying hub functions, functions that move in a direction, etc

        V. Solve problem with conceptual query (iterate through conceptual paths & match with structural path)
          - start with required concepts (but not their optimal relationships in a concept combination) such as 'trust', 'distribution', 'power', and find a structure that arranges those concepts in an optimal way that fits the requirements

        VI. Derive conceptual query & match with structural path
          - start by finding the concept combination required ('trust generated from equal distribution of power'), then find matching structures of that specific combination
        
        VII. Vectorize problem/solution space & match intents
          - this involves framing a problem as a structure like a directed network to convert it to a route optimization problem, where the assumptions are inputs, the intents are outputs, & the interim structures can be a mix of interface objects like concepts

        VIII. Mapping variance objects in problem space systems as starting solution space
          - framing a problem in terms of variance makes it clear which objects are important, given variance/potential structures like interaction spaces, inevitable interactions, variance gaps, etc

        IX. System snapshot (interface/symmetry/vertex) derivation
          - finding the specific interfaces & related objects in a problem system to frame a problem efficiently
          - in the bio system, this would mean automatically identifying the genetic interface
          - in a function set like a code base, this would mean automatically identifying the function type interface (to identify function types like boundary/change rules for efficient function indexing)

        X. System derivation
          - this is a more comprehensive format that allows quick application & identification of system objects (alternates, efficiencies, incentives)

      - other problem-solving automation workflows would start with different interface traversals & use different origin & target structures (designing interface trajectories, identifying the fewest questions that can solve a problem, applying insight paths)


    - specific interface traversal examples

      - problem: find a prediction function to predict variables causing an output, like predicting stock price or a diagnosis from symptoms/causative conditions
          
          - interface traversal
            - information (describing variable types, redundancies, missing info, etc)
            - system (fitting the variables to a system format)
            - causal (finding root/direct causes & causal structures)
            - concept (whether the problem is valid given a definition of price)
            - change (how the function can change)
          
          - if thats not enough to fulfill solution metrics or reduce the problem (identify a range of possible prediction functions), traversals with interface operations can be done
            - causal * change * pattern - to examine whether causal change patterns can reduce the problem or identify a solution
            - concept * change * causes - to identify if a concept change looks imminent

      - problem: find & build an optimal invention design to fulfill intents like 'building a function with minimal bugs'

          - interface traversal
            - information (describing function intents, limits, and assumptions like parameters)
            - system (fitting the function to a system, formatted to include possible variance injection points, identify efficiencies like logic that can be merged, etc)
            - structure (identifying structures that can be applied to the function system, like filters (conditions), direction changes (control flow statements), relationships (assignments), and mismatches (errors)
            - potential (identifying unenforced rules, rule-intent imbalances, false similarities, & other objects of potential allowing exploit opportunities that are not already identified)
            - causal, intent, concept (test function impact on other causes, concepts, & intents, which are high-level objects a function can alter)
          
          - if the function implementation doesnt fulfill solution metrics, other interface traversals can be done
            - pattern interface (does this function comply with patterns for functions with similar solution metrics)
            - a system-object or function-concept interface like the 'efficiency interface' or 'ambiguity interface' (does this function have a more efficient or less ambiguous route between input & output that might fulfill a solution metric, given that maximizing efficiency & reducing ambiguity are standard system & function metrics)

      - problem: find an optimal route between start & end points, like the 'minimal trades to get equal problem/opportunity distribution'
          
          - interface traversal
            - information (identify differentiating attributes/functions/sub-systems of agents/positions/routes within the network)
            - system (identify relevant structures like abstraction layer to traverse at, identify important objects required to solve the problem, like trading problems/markets/skills/information/risk/bets vs. trading currency, or framing currency as a position attribute, rather than a standardizing interface)
            - structure (identify trade & other market structures that are important for understanding why resources dont get distributed fairly, like closed trade loops & independence machines)
            - potential (identify alternative perspectives that could also explain the variation in optimized routes, like alternate value definitions)
            - causal (identify causes like marketing, collusion, and regulations that prevent or interfere with equilibrium market events)
            - concept (identify concepts relevant to markets like balance, demand/supply matching, and how the concept of information can disrupt any other market bc it enables automation)
          
          - if queries of those interfaces are insufficient to solve the problem, interface operations can be used
            - the information-system-structure interface operation (can be used to determine information like the next layer of information objects that are relevant if enough automation is distributed)

  - analysis types

    - problem space analysis (visualizing problem metadata, and changes to the problem space that invalidate the original or other problems once a particular solution is applied)
    
    - core analysis
      - automatically finding core objects/functions/attributes/states possible to determine/describe a system, defining core operations like find/apply/build/derive
    
    - system analysis
      - automatically fitting system objects like symmetries, sub-systems, sub-interfaces, false assumptions, correlations, efficiencies, incentives, and conflicts to problem definition to determine optimal organization/format/routes/metrics/positions
    
    - structure analysis
      - automatically finding structures, like a route between information formats to solve a problem
    
    - information analysis
      - information problem type formatting (mapping the problem as a structure composed of information problem types, like an information mismatch/inequality/minimum/overflow/gap)
      - automatically finding definitions, examples, minimum information to solve, problem-solution matching, insight paths like question-identification functions, finding math structures to re-use math patterns to solve other problems, etc

      - insight analysis
        - insight path application (using insight paths from other fields to optimize insight generation)
      - problem analysis
        - formatting to convert problems to a format with more solution methods, such as problem vectorization (mapping the problem definition to a directed network with inputs on one side, interim inferred important problem concepts in between, and target priorities or attributes on the other, linked by available functions)
      - question analysis (where a question is framed as a source position and a target position on a network, and the answer is the most robust path or the path that moves the nearest to the target position or the path that moves in the priority direction on the network)
    
    - change analysis
      - automatically identifying change metadata like change types necessary to explain a solution or solve a problem
      - potential analysis
        - automatically finding structures of variance like gaps/cascades/reducers, possibility fields, and determining/limiting vertices
    
    - logical analysis
      - functional analysis
        - automatically identifying function metadata like variables, input/output trajectory, the function in a filter format, intent, complexity, efficiency, & exploits)
      - intent analysis
        - automatically finding possible reasons to use a function to automate logic
      - causal analysis
        - automatically matching the problem to causal structures to infer relevant variables & causation metadata (like directness of cause, degree of cause, inevitability, uniqueness of cause, causal tree/network/loop/layer shape)
      - pattern analysis
        - automatically finding patterns with relevant similarities to infer the relevance of pattern metadata, where patterns replace missing required data (such as using patterns between variables of specific types or system positions to infer probable variable relationships)
    
    - concept analysis
      - automatically identifying concepts associated with a structure & vice versa, identifying positions of default abstract concepts in the network

    - interface analysis
      - mapping a query across combination or embedded interfaces given problem requirements, or identifying a specific or new interface to define/query


## standardized analysis

  - objects:
    - interface objects like patterns & concepts

  - structures:
    - core structures (intersections, hubs, vertices, maps, limits, symmetries, & alignments)

  - concepts:
    - abstract concepts (similarity, power)

  - attributes:
    - interface attributes:
        - intent, priority
        - potential/certainty
        - perspective
        - causality
        - abstraction
    - commonness
    - contexts (coordinating/opposing)
    - coordinatability (with similar objects)
    - interaction layer (which objects does it interact with, on what layers of a system or other layers like abstraction/scope layer)
    - injectability (can it be used in many operations)
    - emergence (is it generatable from other objects)
    - neutrality (the range of operations/contexts it can be used for)
    - scope

  - functions:  
    - structural functions: combine, merge, apply, embed, mix, filter, chain, define, create, derive, identify, change, version


## Object Format

  - definition:

  	- this is a standard information format commonly used in programming, including object/attribute/function information

    - the unique implementation of this used in this tool includes attribute type information, function metadata, and object derivation logic, as well as operations to merge objects & other common operations on these components

    - attribute definition:
      - attributes of an object contain information about other structures/functions of the object
        - 'is an object strong' translates to the question 'does the object have functions that enable it to execute tasks at high performance'
        - the 'strong' attribute refers to a net effect of the set of structures (its functions) that fulfills a metric (like high performance) relating to a state that the host object can occupy consistently, making it an identifying quality (attribute), while not required to remain in that state (can be a variable attribute, with multiple potential values)
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
    - information objects like alternatives, efficiencies, & incentives
    - variance objects like variance injection points (gaps in rule enforcement) & variance sources (gaps in system boundary allowing variance from other systems to leak in)
    - system failures
    - exploit opportunities
    - variance gaps

  - functions:
    - optimize, traverse, open/close, etc

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
    - an abstract concept cannot be abstracted further & is found across all systems
    - a non-abstract concept is an abstract concept with structure applied (in a particular system), like how a particular definition of equivalence in a system can evolve from the abstract concept of similarity

  - objects:

  - structures:

  - concepts:

  - attributes:
    - abstraction
    - uniqueness
    - isolability

  - functions:

  - answers questions like:
    - what concepts cannot be reduced/abstracted further
    - what concepts have which associated structures
    - what definition routes identify a particular concept
    - concept-system interface:
      - what concepts are likely to evolve in a system
      - what concepts are common to most systems (would help identify concepts like an efficiency)

  - examples:

    - design sorting function:
        - similarity in navigation, equality in split => optimal for target value near initial split points or similar positions to the split points
        - assumed difference embedded in pre-computation of attributes => optimal for target value with different pre-computed attribute value, or target values in similar position to values with different pre-computed attribute values or adjacent values


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
    - pattern: sequence of specific/identified objects (like a sequence of rules, filters, or values)
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
    - general functions: find, apply, build, derive, change, define, identify
    - core functions: reverse, shift, add
    - info functions: standardize, differentiate, organize, check, monitor, measure, prevent, enable, regulate, store, restore, decide, track, conflict, learn, optimize
    - structure functions: connect, chain, limit, position, change, match, convert, format, route, fill, bound, bind, mark, fit, combine (interact, compete, share, coordinate, equate, group, merge, mix, union, intersection, embed), distribute, filter
    - interim functions: provide resources used as inputs to activate other functions (a set of molecules that when detached can activate other processes)      
    - foundation functions: enable other functionality to develop on foundation structures
    - function operations (resolve function definition, find functionality, index function metadata, chain functions)

  - objects:
    - errors
    - assumptions
    - input/output parameters & parameter types
    - definitions of concepts like equivalence specific to that function

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

  - functions:
    - allow combination of intents to find malicious intent structures (like a sequence of neutral-intent functions that has an emergent malicious intent when used in that sequence)
    - operate on intents (intent-modification intent)

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
    - do variable, type, logical, & output intents align with overall given function intent
    - what is the logical sequence that best fulfills this intent (useful for automating code generation)
      - what is the function linking these variables, given the variable intents a, b, c and the combination intent matrix ab, bc, ca, and the possible output intents of that matrix, and similarity to output intent of y

  - objects:
  - concepts:


## Pattern Analysis

  - functions:
  - attributes:
  - objects:
  - structures:
  - concepts:
  - answers questions like:
    - what would the path between inputs/output be, given patterns of other paths
    - what is the function linking these variables, given common function patterns between variables of these types/topics/ranges/other metadata?


## Logic Analysis

	- definition:
    - this analysis can include related objects of logic (patterns, functions, intent, cause, and change)
	  - automates the selection, structurization (positioning), optimization, & implementation of logical rules

	- examples:

		- if the following code appears in this order:

			if variable1 is None:
				return False
			return operation(variable1)

			- variable1 is not checked for False (theres a gap in enforcement between the None & False definitions) so the operation could fail

			if variable1 <= 0:
				return False
			return int(variable1)

			- theres a potential gap in enforcement of data type, where variable1 might not be an integer even if its positive

			if not variable1:
				return False
			if variable1:
			
			- there's an unnecessary condition which is invalidated by prior code (if variable1 is not defined, it would never get to the third line, so the third line is unnecesary)

	- functions:

		- function to identify logical problem types
			- gaps in logic enforcement (variance gaps, assumptions)
			- overlapping/repeated logic checks (extraneous validation)
			- side effects that don't match function intent

		- corrective functions
			- identify isolated logic operations
			- identify scope required of each operation
			- identify required position of each isolated logic operation

  - attributes:
  - objects:
  - structures:
  - concepts:
  - answers questions like:


## Structural Analysis

	- definition:
    - indexing objects by structure allows clear matching of useful structures to objects/attributes/types/rules
    - this allows objects to be graphed in a standard way, which means translating objects like problems into a computable interface
  
  - examples:
    - market structure analysis
      - the market interface is a standard interface where resources (goods, labor, time, risk, information, expectations, theories, & stored prior labor (currency)) are traded
      - a useful new way to use this is to frame non-resource objects as resources (systems, structures, positions, paths, directions, risk chains, trade loops, markets)
      - then you can apply traditional market analysis (optimal transport) to find, for example, the optimal set of trades to change an industry's position

  - functions:

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
    - trade
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

  - answers questions like:
    - what is the conversion potential of this object given its functions
    - what is the interaction space of this object

	- variance is semantically the opposite index (gap/unenforcement/missing information/randomness) to the filter index (limit/structure/information/organization)
    - includes certainty objects (known variance, metrics, change patterns), uncertainty (potential/risk/opportunity) objects, and variance structures like cascades, injection points, accretion points
    - delegation of variance into systems/types/functions/variables/constants

    - example of variance type analysis (difference):

      - what type of variable is it? (object-differentiating/identifying attribute, emergent specific/abstract property, direct function input/output)
      - how does the variable relate to other variables? (decisive metric, substitutable alternative, collinear)
   	  - at what point does a variable become relevant to another variable interaction layer?
      - how do constants accrete between rules, like caps to keep variance from flowing in to corners or creating boundary-invalidating openings in a system/component boundary?
      - what causes variables to cascade across layers, creating fractal variables?
      - what is the path definitely not, based on various maximized measures of similarity?
      - what attributes & attribute sets & attribute dependency trees differ
      - what is transformation cost/potential between objects
      - what is divergence distance between generative paths for each object
      - example: "what is the probable function linking these variables, given that it is an adjacent transform of a square (related function type), & a distant transform of a manifold (unrelated function type)?"
      
	- use case:

		- this is the problem of adding/fitting/reducing structure from a gap in structure, which can be used to solve problems like:

			- prediction
				- which variables are explanatory, given what we can measure

			- causation
				- how alternatives can converge to the same level of variance or change patterns

		- reducing gaps in rule enforcement to shapes or paths has its own set of rules

		- this interface can also be used for specific attribute analysis, of properties that descend from concepts & take form in a specific problem space:
			- the power concept interface (has implementations that look like trust, info, etc)
			- the balance concept interface (has implementations that look like symmetry, justice, etc)

  - functions:
  - attributes:
  - objects:
  - structures:
  - concepts:


## Change Analysis

	- this regards the potential to break down & format a problem into many different combinations of solved problems (optimal transport, linear algebra, finding prediction function, etc) or known interfaces (type, intent)
	- some sets are more adjacent than more optimal sets & may be a better investment for short-term gains

	- example:
		- when approximating area of an object that is similar to a square but has a convex arc instead of a side (like an opened envelope), it may be more efficient to:
			- calculate the integral of the arc-ed shape and add it to the square area
			- alternatively, if those functions arent available or if the arc is a very low angle and similar enough to a straight line:
				- the arc can be broken into sub-lines & the area of those shapes calculated & then added to the square area

    - example of interface-based change:

      - as change increases, which interfaces are more/less adjacent, where interfaces are represented as a set of filters, each additional filter being a unit of change on the x-axis, and each subsequent filter being one distortion away from the previous filter, where the origin is the most standard filter

    - example of context-based change:

      - as change increases, how does context change (where unit of context are additional conditions)

    - example of structure-based change:

      - example of time-based change:

        - as time increases, what changes:
          - position
          - value (position on a dimension)
          - distance (position from a base point)

        - changing position based on embedded time

      - example of structure-based change:

        - as change increases, what structures change (which structures are stable even in certain change rates)

      - other standard structural bases as alternatives to time, where change is on a y-axis, and these parameters are on the x-axis

        - order: changes are framed based on order - to examine change patterns with respect to order (where unit order is original/standard and highest order is most different order possible)
        - position: changes are framed based on difference from previous position, starting from the standard unit position (default) - for examining change patterns with respect to position distortion
        - distance: changes are framed based on distance type (distance from value, distance from number type, distance from pattern) - for examining change patterns with respect to distance type
        - value: changes are framed based on value type (exponential, constant, pattern value, symmetric value, origin value) - for examining change patterns with respect to value
        - set: changes are framed based on set membership (number type (prime), pattern (progression), distance (adjacent groups)) - for examining change patterns with respect to sets
        - space: changes are framed based on spaces where that change can be framed (topologies, dimensions, vector spaces) - where spaces are formed by adding dimension units

      - example of object-based change:
        - as change increases, what objects (type/variable/inputs/cause) are more/less adjacent 

    - example of concept-based change:

      - as change increases, how does concept (similarity) change

      - example of power-based change:

          - as power (degree of dependency) changes, what else changes:

            - previously distant points become equal to adjacent points as power increases
            - value reverts a concept & the information of the value loses its meaning
            - dimension space can be determined by the degree of dependency
            - does a change increase or reduce power?

          - this can be framed based on potential (bc power can change with respect to options), variance (because power can change with respect to change), and time (bc power can change over time)

      - example of potential-based change:
      
          - as change increases, how does potential (possible change) increase:

            - what probabilities/possibilities become possible (findable/generatable in structural dimensions/on the structural interface)
            - what possibilities become adjacent/distant
            - does a change increase or reduce potential options?

          - as potential changes, how do potential objects/types vary based on the unit of potential (possibility distance, distance between required limits & optional steps)
          - this can be framed on a base of time, because time is a related object to potential (if there is no potential, there is no time)

      - example of variance-based change:

          - changing stabilization based on randomness
          - changing interface development based on randomness
          - changing systematization based on randomness
          - changing object change based on a changeable interface (change stack, like changing orientation of an object within a system that is changing)
          - changing change types (variance leak, variance cascades/activation, variance injection, compounding variance, variance approaching an interface, variance distribution)

          - does a change increase or reduce change sources?

          - as change increases, what change objects (types/rules/rates/direction) alter position/connection/distance/existence?
            - what else changes
            - what aspects of change are altered
            - what core change functions develop or change
            - where does change go if there isnt enough time to contain it
            - what change rates change
            - what stabilizes
            - what patterns emerge
            - what change cascades are triggered
            - what changes develop into randomness
            - what change combinations produce change rate/type/interface changes
          
          - this is a removal of the time parameter, by assigning distance to change types/rates/other metadata, so that any change is framed in terms of a base unit of change (how much change it produces, by making other objects nearer, creating other objects, and connecting with other objects)

          - this can be framed on a base of potential, because potential is a related object to change (if there is no potential, there is no change)
          - this can be framed on a base of time, because time is a related object to change (if there is no time, there is no change)

    - example of function (relationship)-based change:

      - change with respect to function/intent:
        - as change increases, does functionality/intent change and in what direction?

      - example of cause-based change:

        - change with respect to cause

        - the classic parabola of a ball's motion when thrown from the ground has two primary cause-values:
          - origin force until the peak x-value change rate, and gravity force after the peak x-value change rate
          - if the y-value starts changing more from gravity than from origin force, the gravity force becomes determining

        - additional cause values travel farther up the causal stack:
          - forces causing the emergence of gravity & origin forces are other causes

  - functions:
  - attributes:
  - objects:
  - structures:
  - concepts:
  - answers questions like:


## Causal Analysis

    - given the position between these causal factors, which causal patterns are likeliest?
    - "given that a species occupies an interim position between evolution, efficiency, time, and environment, what is the likeliest causal shape linking a species with its environment?"
      - for more evolved organisms, this is a network causal shape, though species with less developed cognitive ability may have simple or uni-directional shapes with environment
    - "what is the function linking these variables, given these functions linking other adjacent generating variables/functions further up/down the causal shape"

  - functions:
  - attributes:
  - objects:
  - structures:
  - concepts:
  - answers questions like:


## Info Analysis

    - information analysis involves standardizing information formats, like standardizing to the object/attribute/function model (including related objects like state & type) so that information structures are clear & can be mapped to information problem types

    - organization analysis

	    - optimal path/distribution/states
	    - what would the optimal path be, given a certain intent, object identity, & host system?
	    - "what is the function linking these variables that is most efficient/involves fewest variables/involves known constants?"
	    - identify layer to solve a problem at
	    - identify key objects needed to solve a problem
	    - identify structures for information

    - type analysis
      - given a known type stack progression, what is the likeliest position or extension of that stack?
      - "given that these species evolved this way, what level of variance is the missing link between them likely to have?"
      - "what is the function linking these variables, given the type stacks of the function objects (dimensions, adjacent functions, identifiable shapes, etc)"

	- information objects are related to agents & their communication (perspective, strategy, decisions, intent, game, motivation, problems)

	- these objects can be defined as combinations of general interface objects:
	    - perspective: a filter produced by chains of distortions; priority set with object positions & default paths
	    - strategy: efficient path between points
	    - joke: difference between expected & actual position
	    - error: difference between expected & actual decision
	    - argument: position of objects or path between points with supporting connective functions
	    - game: incentivized motion within a system having limits to prevent motion; a system with conflicting/overlapping intents between agents, usually with low-stakes intents
	    - filter: barrier creating a difference between input & output
      - problem: conflict or inequality

  - objects:
  - structures:
  - concepts:
  - answers questions like:


## Problem Analysis

  - definition:
    - on this index, problems are mapped to structure, once problems have been converted to an information problem, which has a clear mapping to the structural interface
    - problems can always be framed as info problems (missing info, conflicting info, unconnected info, mismatches, imbalances, asymmetries)
      - finding a prediction function can be framed as an optimal path in a network of variable nodes
    - once you frame a problem as an info problem, you can map info to structure:
      - conflicts can be vectors with different direction or which overlap

  - functions: 
    - *** add diagrams
    - mapping function, to map problems to structures, problem functions, & other problem types
        - graph attributes that differentiate problems that are impacted by possible solutions
        - map intent to direction & assess progress by movement in that direction
        - networks with clusters, sequences, & other structures representing decisions
        - system layer graph representing combinations
        - interactions of interaction spaces (which interactions are common across agents, likely given other interactions, etc)
        - map function sets to sequences, given a metric like progression toward goal
        - map related/approximate problems/problems elsewhere on the causal stack to a related problem network, having different dimensions (like a generative vs. identification problem)
        - map change types to dimensions and graphing/calculating dimensions where change types change (an aggregate, interface, or deciding dimension where change type is uncertain but not random)
        - using a layered graph to visualize change of different types/metrics built on a symmetry
        - mapping language to structure directly (verbs like 'find' mapped to a set of vectors leading from a node indicating possible start positions, with option to use core function vectors to reach target node)
        - a trajectory between problem graphs where each graph represents a decision/state, and attribute sets & problem of similar type occupy a similar position on an axis depicting all the graphs traversed
        - a metric like size of variable interaction space mapped to length/area/volume to indicate how much of the problem is left, and a metric like number of variables mapped to number of dimensions/sides/layers of the shape to graph the problem according to structural metrics
        - selecting a space (dimension set), with embedded parameters & bases for framing changes of a certain type
        - representing changes produced by a solution as a set of vector trajectories across interfaces

  - objects:
  - structures:
  - concepts:
      - anomaly/counterexample/outlier/conflict

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

  - examples:

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
                1. create missing resource
                  - navigate up causal stack: find combinations of functions & objects that generated it
                  - navigate sideways: find alternatives or find alternative combinations to generate it
                2. invalidate dependence
                  - navigate up causal stack until dependence cause is found: find combinations of functions & objects that generated dependence
                  - navigate sideways: find functions to invalidate dependence (generate resource) or correct problem (imbalance, lack, mismatch) causing dependence
                - solution intents 1 & 2 have a 'generate resource' intent in common, which fulfills both solution intents - so if the intent changes between them, the solution involving generating the resource may cover the next problem iteration too, or the intent that invalidates the problem may prevent future iterations

        - find sequence (route) of network nodes representing (steps, positions/states, sets, intents, etc)

              - find sequence of questions to solve a problem
            	  - example: what is the probability the sun will rise tomorrow
            	    - this can be done with an insight path composed of interface analysis questions:
            	      - what are the shapes & patterns of errors in assumptions & selection/generation of methods? (what ratio of incorrect are people with each additional assumption, given the level of certainty per assumption & complexity of problem)
            	      - what are the consequences of not correcting those errors? (how wrong will the predictions be)
            	      - what are the shapes of cause in generating/selecting assumptions & methods
            	      - what is the usual correct assumption pattern once false assumptions are corrected, and whats the insight path to transform the incorrect to the correct version?
            	      - whats the rate of discovery of new sub-systems, objects, or variables in related systems like physics
            	      - whats the likelihood we created certainty out of what ratio of our assumptions (over-relying on assumptions to make them conditionally true)
            	      - whats the possible causative impact of measurements & application of science knowledge on other knowledge
            	      - whats the possibility that a subset/state of physics rules gathers in increasingly isolated space-times, but outside of it, the rules are more flexible
            	      - whats the possibility that every science rule we take as certain is a false similarity or other false object?

  - answers questions like:


## Interface Analysis

  - objects:
  - structures:
  - concepts:

  - definition:

  	- the interface network is the set of networks that act as useful filters/standards for comparing metadata 

    	- it can refer to a set of specific interfaces for a given problem space
    		- the specific interface network for the debugging code space could be layers of network filters like dependencies, logic structures, side effects, and types
    		- these specific interface networks are often implementations of the general interface network with mapped objects:
    			- dependency interface is a combination of the cause/function interface
    			- types (data, classes, etc) interface is a subset of the general type interface
    			- side effects are a subset of the variance interface (gaps in intent & execution, prediction of emergent attributes after nth iterations of combinations or other operations)

    	- the abstract interface network includes layers of network filters like:
    		- intent (priority)
    		- perspective (the unit filter object)
    		- function (can include patterns, logic, strategies, core functions, and any other set of operations/objects that has order)
    		- structure
    		- concept
    		- information (organization, formats, types, info objects like problems/questions/insights/assumptions)
    		- potential
        - change
    		- cause
    		- system

	- core functions (filter, find, apply, derive, build, change) mapped to user intents (identify cause, predict a variable, build a function) can be used to generate & design a query on the interface network

	- like all other sets of objects on an equal interface, any item in the set can be used to find the others

	- each interface network in the set of interfaces (core function interface network, general interface network, specific interface network) can be used to generate the others
		- intent interface can be used to generate the type interface
		- dependency interface can be used to generate the side effect interface
		- interface network can be used to generate the core function interface

	- the filter interface is more clearly usable as a method to generate the others bc most problems can be reduced to a structure that can be filled in different ways for different reasons
		- it can even generate the change interface, by framing each process as a filter between i/o

	- finding the starting interface & direction of traversal across the other interfaces in the network is its own interesting problem, beyond just generating the relevant & useful interfaces in a network
	
	- framing a conflict of type 'competition' as opposing direction/intent or equivalent direction/intent is a calculation that can be automated using any of these kinds of analysis, but the logic & intent interfaces are best at this, and selecting those type of analysis is an important tool to build

	- other uses of the interface network include:

		- finding explanatory variables on multiple interfaces (a trajectory on the interface network) & translating them to a shared interface where possible

			- maybe you can identify that theres an important type, intent, & conceptual variable to identify an object
			- then you can decide if its worth storing that info separately, or standardizing those variables to the same interface
				- if the type variable is explanatory & you need to keep it, you can still standardize it to intent (whats the primary unique function achieved by each type)
				- concepts can also be standardized to other interfaces (what intents do concepts like 'power' achieve in the system & what position do they occupy)
			- which interface to standardize to depends on which use you intend to use the information for
				- if you need to implement it immediately, an interface like intent that is semantically adjacent to the structural & logical interfaces will be more useful
				- if you need to identify new types, standardizing to the type interface will be more useful

	- The overall workflow of this tool can be built with an interface query:

		- find problem type & format the problem as a combination of information problem types (information (problem, assumption) interface, type interface), as well as any related problems (information (problem) interface, pattern interface, and the change interface to generate related problems if none are logged)
		- find solution requirements (structure interface where requirements are limits/thresholds)
		- apply a directed graph (structure interface) of various information formats (interface interface, information interface), positioned in the sequence likeliest to find the missing information to solve (structure interface, similarity concept interface)
			(if its missing cause information, standardize to the causal interface or generate information about likely causes from other interfaces like the pattern interface or generate adjacent or proxy information to cause information like a set of tests to filter out non-cause information or generate interaction pattern information to predict which objects will interact, generating causes)
		- if the information formats applied dont reveal enough info, apply combinations of the formats (structure interface, core interface)
		- if no solution space can be identified or reduced, return the queries and the problem & problem space metadata

  - attributes:
    - generatability/common derivable core functions with other interfaces
    - information loss
    - variance focus (what variance is exaggerated for comparison by this interface)
    - position of interface on default interface network (what distortions produce this filter/perspective from unfiltered origin)

  - functions:

    - determining position/trajectory on interface

    - selecting interface as best standard for comparison (identifying when a particular specific interface will reduce solution set across any possible host system)

    - generating specific interfaces (filters) for a problem/space

    - generating full set of general interfaces (intent, concept, structure)
        - these can be generated by identifying the key differentiating factors across systems, which can be generated as combinations of objects 
          - type is a combination of attributes
          - intent is a combination of function effects
          - concept is a network of networks describing a structural concept (balance, power)
          - structure is a combination of information & rules 

    - identifying all interfaces with variance that cant be captured in other interfaces

    - calculate when to skip interim variables/interfaces

        - depict the spine variable & the finger position variable to demonstrate/identify chirality, skipping the connecting functions, because there are multiple connecting functions (endpoint/side selection, extremity development) and they dont determine change in either variable, as the key important relationship is the spine symmetry and the orientation transformed about the finger position interface being reversed according to the spine symmetry

          - the spine isnt symmetric from the side, which implies a bias toward the front, which is a platform where features are concentrated, so the development of limbs (using derivable intents like duplicate, backups, protective, flexible, movement, alternative, balance intents) & their focus toward the front is derivable from the spine features, so we can skip to the finger order interface to identify the concept of chirality or an example of it/its patterns in the system

        - the interim interfaces & variables may not add change to this relationship so they dont need to be depicted or stored in this context

        - this is useful for determining where change can be stored/routed in a system
          - if there is demand for change (stressors demanding new functionality) but all components but one are maximizing their change handlers, then you know theres one potential variable where change will gather/be routed, if its possible to route change from the variance injection point to that variable's causal stack at some layer/point

        - its also useful for determining interface trajectories/adjacent interfaces

      - different interfaces to approach security analysis:

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

          - for a password system, the relevant basic objects are:
            - 'memory access patterns' as retrieving a memory has patterns just like retrieving a password from browser storage has patterns or typing someone else's password has patterns
            - 'memory limits' meaning that a memory has more limits on memorable passwords than browser stored passwords or an experienced hacker
            - 'augmentation' meaning password salts
            - 'validation' meaning hash check patterns
            - 'generation' meaning the rules used to generate different types of password (like how passcodes typically have repeated patterns) & the enforced rules to limit passwords (requiring special char types that are usually positioned together if manually generated)
            - 'reverse computation requirements', meaning the cost of rainbow tables and other tools to reduce computation time

          - all of which can be generated with standard system objects/functions/attributes (limits, patterns, core operations like reverse and high-level operations like generate/validate) applied to password system objects/functions/attributes (password rules, char limits)

    - interface operation functions:

      - apply an interface as a standard to another interface:
          - intent / structure interface: assess intent interface by a standard of structure interface (which structures can simplify the intent interface)
      
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

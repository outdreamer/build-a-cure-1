# Implementation Instructions


## Object Model Analysis

	- this is a simple index of objects as class instances

	- uses:

		- predict interactions & optimal versions of objects/attributes/types/rules
			- predict emergent objects/attributes/types/rules

		- problem-solving automation method to query objects/attributes/types/rules
		- reduce solution space or identify causative factor in problem

	- tech debt:

		- identify data sources (code bases defining schema/class definitions)
		- implement data sanitization & import
		- implement identification functions (objects/attributes/types/rules) to gather more data pre-indexed
		- implement object operation functions (combine, merge, apply, mix, filter)
		- implement object function set (change functions, boundary functions, probability functions)


## System Analysis

	- extension of object model

	- fits objects indexed in object model together in a system

	- observes not just rules between objects, but other key system data like:

		- variance (gaps in rule enforcement) & variance sources (gaps in system boundary allowing variance from other systems to leak in)
		- emerging objects
		- system errors & error-handlers
		- vertices (factors that generate or influence the system development)
		- incentives (forces with a built-in reason lending it extra momentum/gravity pulling agents in that direction)
		- interface metadata (intent, pattern, types, function, etc)
		- relationship metadata (related systems, system position in system interface network)


## Intent Analysis

	- alternative index to system/object indexes
	- indexing objects in a system by intent allows for quick optimization
	- this kind of analysis is useful for finding bugs
		- if a function's lines are indexed by intent, it's clearer when an intent has already been handled or when there's a reversal or gap in logical flow


## Logic Analysis

	- automating the selection, position, optimization, & implementation of logical rules is possible with this analysis

	- use cases:

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


	- tech debt:

		- analysis & classification of known bug types

		- function to identify new bug types

		- function to identify known bug types in logic
			- gaps in logic enforcement (variance gaps, assumptions)
			- overlapping/repeated logic checks (extraneous validation)
			- side effects that dont match function intent

		- function to identify logic bug resolution methods:
			- bug 'overlapping logic' has bug resolution method:
				- identify isolated logic operations
				- identify scope required of each operation
				- identify required position of each isolated logic operation


## Variance Analysis

	- alternative index, indexing objects by change/potential/uncertainty

	- variance is semantically the opposite index (gap) to the filter index (limit)

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


## Structural Analysis

	- indexing objects by structure allows clear matching of useful structures to objects/attributes/types/rules
	- this allows objects to be graphed in a standard way, which means translating objects like problems into a computable interface

	- use cases:

		- which objects are chained (cause, risk, variance, errors, gaps, limits)
		- which are dimensions (isolatable attributes of change patterns)
		- which have position
		- that a type stack (which type values on different type layers) and a network/tree (type hierarchy) are useful structures to capture type relationships


## Transformation Analysis

	- this regards the potential to break down & format a problem into many different combinations of solved problems (optimal transport, linear algebra, finding prediction function, etc) or known interfaces (type, intent)
	- some sets are more adjacent than more optimal sets & may be a better investment for short-term gains

	- example:
		- when approximating area of an object that is similar to a square but has a convex arc instead of a side (like an opened envelope), it may be more efficient to:
			- calculate the integral of the arc-ed shape and add it to the square area
			- alternatively, if those functions arent available or if the arc is a very low angle and similar enough to a straight line:
				- the arc can be broken into sub-lines & the area of those shapes calculated & then added to the square area


## Info Analysis

	- on this index, a lot of human & biological problems (problems associated with sentient life) can be clarified

	- these objects are related to agents & their communication: 
		- perspective, strategy, decisions, intent, game, motivation, problems

	- these objects can be defined as combinations of general interface objects:
		- game is a system with conflicting/overlapping intents between agents, usually with low-stakes intents
		- perspective is a filter produced by chains of distortions


## Problem Analysis

	- on this index, problems are mapped to structure, once problems have been converted to an information problem, which has a clear mapping to the structural interface

	- problems can always be framed as info problems (missing info, conflicting info, unconnected info, mismatches, imbalances, asymmetries)
		- finding a prediction function can be framed as an optimal path in a network of variable nodes

	- once you frame a problem as an info problem, you can map info to structure:
		- conflicts can be vectors with different direction or which overlap


## Interface Network

	- this is the set of networks that act as useful filters/standards for comparing metadata 

	- it can refer to a specific set for a specific problem space

		- the specific interface network for the debugging code space could be layers of network filters like:

			- dependencies
			- logic gaps/order/validity
			- side effects
			- types

		- these specific interface networks are often implementations of the general interface network with mapped objects:
			- dependency interface is a combination of the cause/function interface
			- types (data, classes, etc) interface is a subset of the general type interface
			- side effects are a subset of the variance interface (gaps in intent & execution, prediction of emergent attributes after nth iterations of combinations or other operations)

	- whereas the general interface network includes layers of network filters like:

		- intent (priority)
		- perspective (the unit filter object)
		- functions (can include patterns, logic, strategies, rules, and any other set of operations/objects that has order)
		- structure
			- sub interfaces of structure include:
				- difference/position
				- shape
				- direction
		- concepts
		- types
		- variance (change/potential)
		- cause
		- conflict (problem/solution)
		- system

	- a super-interface involves the core functions that can generate the general interface network:

		- filter/find/identify
		- apply/combine
		- build/fill
		- derive/predict
		- change/transform/process

	- like all other sets of objects on an equal interface, any item in the set can be used to find the others
		- in a set of (4, 6, 2, 3) you can start with 4 to find 2 or 3 to find 4

	- each interface network in the set of interfaces (core function interface network, general interface network, specific interface network) can be used to generate the others
		- intent interface can be used to generate the type interface
		- dependency interface can be used to generate the side effect interface
		- interface network can be used to generate the core function interface

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

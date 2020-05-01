# Intro


## object model

	- this is the standard object-function-attribute model you encounter in programming, applied to systems
	- by attribute, I mean an inclusive set of terms including parameter, variable, input, output, & property


## abstract network

	- this is the network of abstract concepts which are based on core structures (power, balance) 


## interfaces

	- this is a standardizing filter (can be attributes like cause, change, potential, intent, structure, etc)

	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/interface.svg


## core functions

	- layer diagrams involve applying layers of chained transforms to core functions to generate new object combinations through paths on these diagrams
	- these diagrams can be applied to objects/attributes/systems, which can be framed as a function

	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/solution.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/insight.svg


## useful structures

	- system diagram	
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/system.svg
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/variance.svg

	- function diagram
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/function.svg

	- problem diagram
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg

	- insight path
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/insight.svg

	- info problem type
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg

	- intent of alternate paths
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/cause.svg

	- intent organization
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/intent.svg

	- causal structures
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/cause.svg

	- variance gaps
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/variance.svg

	- perspective
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/perspective.svg


## mapping concept to structure

	- diagram:
		- https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/concept.svg

	- example: 
		- create a program that checks if a system is robust automatically, regardless of which system
		- what would a concept like 'robust' mean for a system?
			- given the definition route to 'robust' as 'strong enough to withstand various circumstances'
				- you can infer that if a system is robust, it can retain its structure despite application of various change types
				- so query for change types in that system
				- then check which change types break the system & the ratio of (change types handled/total change types)
				- assign a ratio to 'strong' adjective
				- check if the change type handled ratio is above or below the strong ratio
				- if above, the system is 'robust'


## mapping problem to structure (asymmetry, conflict)

	- for a conflict like vectors aiming at a corner of a closed shape (where the shape is formed by the intersections of limiting attributes), the structural way to solve that problem is:

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
 

## graphing solution for a problem space

	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/function_map.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/map.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/prediction.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg


## limitations

	- depends on queryable information (the system must be discoverable) and definitions (for efficiency, although the definitions should be derivable if the system information is accessible)
	- the set of dictionaries used may need updating to build the right queries (there may be more core functions or interfaces to add) but it will discover that during the query
	- some query sets/chains will be more efficient than others, but that will become clear with meta-analysis of queries after its used, so query analysis needs to be done regularly to update query-building logic
	- it will generate possible solutions as it runs and the first generated solution is unlikely to be the most optimal
	- some calculations may need to be made before query can be run (minimum information to solve a problem, relevant insight paths to select interface trajectories, problem solving cost analysis) which can add to solve time
	- some problems are inefficient to solve (resources should be allocated elsewhere bc solving the problem is too costly or efficiencies are imminent in the host system)
	- standard queries (example filters) may beat custom queries for some problems but it may be clear after, so both may be optimal to run


## faq

	1. whats the need for mapping information problems to structure (math) problems? for example, isnt an information asymmetry already structural?

		- yes and no. 

			the problemm is already captured on a layer of abstraction above the agent layer (what you could call 3-d space or physical reality), 
		which is what I sometimes mean when I say the structural/math layer though I should really say the physical information layer, 
		where most problems should be transformed to unless you have existing solutions or a complete interface map so you can query for a solution on other interfaces.

			but the information asymmetry is an abstract problem has many solutions, and applying each solution would look different between different problem spaces.

			one way to solve it is by distributing all information to all agents - another way is by splitting hte information and sharing it equally - another way is removing the information.

			these solutions would look different depending on the problem space - distributing all information or removing it may not be possible depending on what resources you have.

			but once you have the problem matched to these solution structures, you can apply the solution structures to 3-d space, looking for objects that could fulfill the definition of solution terms.

			what does 'distribute' mean for a particular problem space? these are the questions that can be answered on the 3-d space layer.

				if you have info tech, you can distribute information that way, at risk of the info being hacked
				if you have social networks, you can distribute it that way, at risk of distorting it

			different solutions comes with different intents & problems like risks, and these objects are also automatically identifiable once the solution is applied

			distributing information may give conflicting agents power over each other - but only one of them may use it - thats an information problem as well, which can also be framed as an info asymmetry.

			whats the solution that causes the fewest risks & subsequent info asymmetries? that depends on the problem space.


	2. does every object need to be mapped to a common shape (like a square or circle) with your system?

		- that strategy can be used to compare attribute sets that match these common structures, to find structural solutions that can then be applied to the original problem 

		- in the absence of other problem-solving methods, finding structures with problem-solution matches already indexed can be an efficient method of solving the original problem.

		- that doesnt mean there arent cases where finding a new structure (like a core function combination circle layer system or a function system) isnt useful for depicting information in ways that will reveal problem cause & other important info, 
		  even revealing solutions if the information is organized in the right structure


	3. whats the difference between your system/interface/abstract network and a typical concept map?

		- good question, there are a lot of points to make here

			- when I say the abstract network, I mean the correct network indicating the actual positions of abstract concepts (like balance, power) that have their own sub-networks of other concept versions,
				where the concepts differ from & connect to each other given how they really interact in other spaces, given their definitions
				
				- these concepts emerge in the structural layer (power is ability/options, so power comes from inputs/connections, etc) so the difference between the concepts that qualify for the abstract network
				and core structures in the structural layer is minimal.

			- a concept map typically won't assign meaning to the position of each concept, contain the other versions of the concept, or organize the concepts without a structural method to differentiate & connect them.


	4. whats the difference between the abstract/interface network and an attribute/property graph?

		- attributes arent the only useful object to consider (consider types, which are attribute sets) and dont support more complex analysis 
			(like changing attributes, attributes that are likely to interact, etc)

		- that type of graph is useful for finding connections between various specific attributes of objects - they typically leave out other considerations like 
			- cause
			- system structures (boundaries, sub-systems)
			- intent
			- function (functionality building or emerging from attributes)
			- potential (interaction space)
			- concepts (trajectory on abstract network used by system)

		- the attribute graphs dont reveal much about the problem types in the system of object interactions or how they evolved and what direction the attributes are headed in 
			 (about to converge with other attributes or create a new type)

		- like other information depicting methods, attribute graphs:
			 - dont focus on or derive generative/determining/causative/equivalent attributes
			 - dont have a concept of alternate attribute paths, system boundaries, governing system rules, a way to convert between functions/attributes, or a method to derive missing attributes
			 - leave out attribute metadata like attribute type (input/output, emergent, possible, requirement, dependency, type)
			 - attribute states/trends
			 - predict attribute interactions
			 - dont have system analysis across the whole set of objects described 
			 - dont include pattern analysis from prior queries of other graphs
			 - dont have a method to find causative attributes automatically
			 - dont typically acknowledge the importance of attribute sets as a definition of types (showing which attributes are related to types)
			 - dont tell you which attribute sets influence other sets to cause a correlation n degrees away
			 - are typically used with specific objects
			 - dont reveal the core functions building an attribute set, which are the causes of the attribute values
			 - dont have a concept of symmetries, interfaces, potential, change, etc


		- also the structures I use require other shapes than a network (symmetry stack, trade circuit, potential field) which is useful for showing connections but can't display all connection/relationship types, 
			requiring a layered network like the interface network

		- some networks will display relationships' most simple attributes, like which objects are connected, the direction of the relationship input/output, or inheritance relationships,
		  but the function interface will display connections between objects given their actual relating function shapes

		- however most things can be framed as a set of attributes, just like most things can be framed as a network, a set of filters, a function, a system, etc

		- even concepts can map directly to attributes & be framed as a network of attributes or a route on a network,
			and the most abstract concepts like power map to core structures like inputs or high-connectivity nodes in a network, which are core attributes of a system (hubs, injection points, gaps, etc)


	5. how is this different from category theory
		- a theory of how types evolve is a useful tool to use when implementing a method of automating problem-solving, if you are restricted to type data
		- my system has a component that involves deriving & analyzing core functions/objects/attributes and how they interact & evolve, but is not restricted to the object relationships defined in that theory,
			as real object interactions dont involve adding an attribute at a time or combining two defined objects but rather:

				- deriving definition routes to capture an object
				- transforming attributes to functions & back
				- trends & interactions like attribute accretion into types, attribute collisions/conflicts, attribute potential, etc


	6. how is this different from machine learning

		- in addition to the dependencies of machine learning (info & compute) vs. the dependencies for interface analysis for insight extraction (concept/logic maps & dictionaries), this differs in various ways

		- machine learning uses a network of functions which filter information for patterns according to input data

		- interface analysis uses function (core function), causal (causal shape), potential (interaction space), interface (symmetry), concept (structure maps), & system (variance gaps) analysis 
		  to identify missing semantic information, like:

			- probable sources of error
			- efficiencies
			- insights about the variables producing an output variable
			- intent & optimizations of the system containing the relationship being studied

		- that doesnt mean you cant use system analysis to improve machine learning methods or integrate it with machine learning, to produce:

			- a network with every common type of core function represented in the method of filtering weights in a weight path (a hybrid network with various input passing/aggregation strategies represented)
			- calls to other networks containing insights or pattern information when a particular pattern is identified
			- networks using standardized data across the supported interfaces (data standardized for the causal, structural, system, potential, change interfaces)

			- and you could also use machine learning to make prediction functions for sub-tasks in interface analysis, in the absence of the concept/logic maps/definitions

		- machine learning is specifically for 'figuring out a variable relationship/prediction function', with an alternate intent of 'finding patterns', which is why its useful across a variety of problem types
		- but like category theory, property graphs, & concept networks, it also doesnt have a concept of:

			- translating abstract interface objects like cause/intent to structure
			- identifying object types (concepts, functions, attributes, systems)
			- deriving relationships using core functions & patterns
			- switching between various analysis methods in the absence of information


	7. whats the difference between this & existing system analysis:

		- the more accurate term for my project is interface analysis (to automate problem-solving), 
		  but a subset of that involves my own implementation of system analysis that can derive, identify, & optimize important system objects like:
			- problems (conflicts, false assumptions, unenforced rules, system-invalidating errors)
			- variance injection/accretion/interaction points
			- misaligned intents
			- attribute collisions
			- incentives/efficiencies/paradoxes

			using the problem-solving automation methods described in the docs, after converting the system to a standardized format & including metadata with the system objects

		- as far as I know, classical system analysis:
			- applies to systems with an existing physical structure like circuits or cells (rather than finding semantic objects like problems in a system graph of info objects)
			- involves mapping the system objects & their interactions & looking for a standard set of error types (rather than describing the interface trajectory of the system after standardizing it)
			- correcting errors manually rather than automatically
			- analyzing the system on the physical information interface rather than other interfaces like intent/cause


	8. whats the difference between this and simulations of agent-based games

		- some of my methods involve making changes to object positions & assessing the impact of that change, which is where the similarity ends
		- simulating info object (incentive, question, problem, system) combination types (merge, collide, compete, inject, etc) is not the same as simulating the combination of physical objects
		- my methods to find the cause of a phenomenon impacting various objects (like deriving that a bottle was the source of contamination causing an illness) involves using cross-system insight paths
			(like those found below, including finding the "attribute alignment" and "high-connectivity hub nodes"), which determine most emergent interaction patterns that occur in the physical world
		- my system analyzes agent position based on info & physical assets rather than just physical assets


	9. is this too abstract to be useful? how would you implement this?

		- the fact that we can imagine what a concept is means it can have structure, & interfaces act like standardizing filters:
		  while they are abstract terms, they have intrinsic physical attributes & map to structures even when they are abstract enough to have few physical attributes

		- the docs for some implementation strategies are here:
			https://github.com/outdreamer/build-a-cure/blob/master/docs/core_analysis/derivation_methods.md
			https://github.com/outdreamer/build-a-cure/blob/master/docs/specific_methods/problem_solving_matching.md

		- most of my implementation strategies vary on:

			- the starting point of the analysis (which interface the query starts from)
			- the structures relevant (which structures or type of graphing method to use)
			- the intent (create a prediction function, reduce solution space, compare solutions, or match problem with solution)
			- the core abstract function represented (is it a find method, an apply method, a combination)
			- the models used (object model, interface query)

		- but they have in common:
			- using core objects & patterns
			- using info objects like problems/incentives/sub-systems/efficiencies & concepts like probability/relevance to create prediction functions
			- applying structure to unstructured information


	10. what is an interface 

		- its a standard for comparison - in my system its a standard that reduces systems so they can be compared


	11. what is a problem space

		- its the space where youd graph all the info relevant to a problem - I often use tech as a key determinant of a problem space bc which tech you have often determines which strategies you can use 
		  but it includes all the other resources you might have access to (info, potential, energy, physical assets, etc)


	12. why improve problem-solving at all?

		- the problems with current solution methods:

			- solutions that are slow to implement, static, not shared, not organized, not generalized, & include repeated work
			- solutions often dont use prior knowledge (insights/patterns) to inform new solutions
			- known/discoverable systems with known/discoverable rules are treated as unknowns
			- errors are found with common known or easily derived rules ("change/remove assumptions") or causes ("misaligned attributes")
			- problems of the same type persist across systems
			- problems can be standardized to info/structural problems, which have associated solutions, and can be used as building blocks of solutions
			- work devoted to repeating a solution could be work devoted to innovating problem-solving
			- problem-solving isnt automated
		
		- current methods are focused heavily on information - if people become too focused on information (what is true at a given time), they'll never change again & time will end,
			they'll just calculate everything from the point that they find a way to do so

			- instead of focusing on information as the priority, they need to focus on preserving variance potential, so there are still questions to answer

			- outrunning the onset of the information calculation singularity involves:

				- creating self-sustaining variance sources & protecting existing ones (maintaining ambiguity/alternative options)
				- automating what can be & also automating the update of automation tools
				- evaluating information on the basis of change/potential
				- analyzing reason/cause rather than information
				- this means avoiding optimizing everything
				- there should always be at least two comparable alternatives so a decision is difficult & not certain
					- at least two systems, at least two perspectives, at least two metrics, at least two intents, etc - the ark requires differentiation to sustain potential

	13. what do you mean by 'using potential as a base rather than time'

		- time as a base for assessing change is useful in solving information problems
		- time occurs when there are no symmetries allowing for reversibility - in order for something to be reversible, symmetries have to align to allow for efficient organization of energy flow so a system can form to be a platform for the change
		- potential is the ability to change, time is the realization of change
		- im using potential as a proxy for the time variable, just like using the derivative rather than the function
		- potential is an important input of time - if there is potential for change, time can occur 
		- focusing on time over-focuses on information, which is the result of a measurement, and measurements have unintended side effects like over-dependence on the measurement
		- potential also captures a lot of potential information:
			- whether something is about to happen (whether a function is about to change)
			- whether something is possible or unverifiably possible
			- whether something deviates from or complies with known patterns (whether it's likely to be new or not)
			- how similar something is to output of known generators (adjacence to functions as a analytical metric, rather than the prediction function itself)
			- possibilities & ambiguities (where information is lost like in a black hole or uncalculatable like where there are too many alternatives) 
		- evaluating change with respect to potential measures whether you're increasing the number of possibilities (enabling information to occur as time passes) or decreasing them
		- if you make a decision that closes too many doors, potential, change, & time will be permanently lost, if the door goes with it (if it's irreversible)
		- other types of time are useful to evaluate change 
			- whether youve changed in conceptual time, causal time, potential time, or information time, & whether the change is absolute/specific - did you change everyone's time or just yours?
			- these metrics differ in how other types of time pass
		- rather than asking 'is this resource needed at a given location' - we can ask questions like 'did we enable people in that location to solve a resource deficit?'


## Problem-solving Insight Paths 


The right questions to ask to reduce time to solve a problem (see example filters as problem-reducing questions)

In the patterns from system_analysis.json, you have example filters to use when reducing a problem before trying specific methods to solve it.

These are the objects to look for in order to quickly:
- identify causes of system error
- identify determining variables of a system
- understand a system quickly
- optimize a system

All systems will have core abstract concept implementations:

"concept_structure_map": {
	"power": "position",
	"balance": "equivalent",
	"efficiency": "path",
	"change": "distance",
	"potential": "unoccupied accessible adjacence",
	"relative change": "ratio",
	"base/standard/interface": "origin change",
	"symmetry": "origin",
	"information": "structure",
	"truth": "match",
	"priority": "direction",
	"intent": "output",
	"position": "input"
}

But specific concepts evolve within a system given unique combinations of core objects.

Example:
	- a "signal joint" evolves as a concept in the gene system because it's an output of an important combination of core processes that is not matched with an equivalent handler, so it can cause further complexity bc its allowed to interact with other systems instead of decomposing it after it's used.
	- an "improvisation" is a change given a starting position and new problem information that doesnt match an existing solution

- cause cant be traced when:
- when inputs/system/measurement tools decays/changes before it can be measured
- when change/decay outputs dont follow patterns or have multiple alternative possible patterns


# Analysis

When a system is totally unknown, you should diversify across all interfaces at first - example of finding value in a set:

	- analyze a set from:

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
		- system interface: what variance injection points are in the set generation/selection/aggregation/interaction/organization

	- then when you find a pattern match on an interface set, you can restrict the search to those

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


## System info objects

	- why is it so useful to use system info objects like inefficiency or asymmetry as a way to frame & solve problems automatically? 

		bc these objects offer the most flexibility and occupy an interim interface between physical reality & conceptual networks, so its a good interface to standardize those interfaces to, theyre standard core objects with high interaction potential on similar interaction layers

	- how to generate interface filters (system, type, function), starting with unit interfaces function & attribute:

			abstract    pattern

			set 		system

			subset 		filter

	function    

			intersect   change (convert attribute to function)

	attribute

			set  		type


## Examples of insight paths (specifically system filters)


```
{
	"attribute": {
		"attribute cluster": "species differentiation features tend to cluster"
		"attribute similarity": "location/agents (hospitals & staff/patients) with isolated conditions to prevent overuse of resource needed (cleaning supplies) for mixed condition (non-isolated hospitals/staff), where isolated conditions align with invalidation of cleaning supplies for that condition",
		"attribute alignment": "rotation force aligned with input force creates momentum",
		"attribute matching": "stacking objects that can make cubes in the knapsack problem to reduce unused space between objects",
		"attribute accretion": "symmetry stacking occurs to develop granular features (symmetries in the bio system like the spine/limbs)"
	},
	"metric": {
		"inadequate metric": "",
		"incorrect test": "",
		"incorrect threshold": ""
	},
	"concept": {
		"definition route": "",
		"definition structure": "most abstract concepts have a definition network"
	},
	"error": {
		"false similarity": "there are many routes to a shape or point which may differ on important metrics like intent",
		"false contradiction": "",
		"false potential": "",
		"false constant": "",
		"false conflict": "",
		"false category": "",
		"false assymption": "",
		"false paradox": ""
	},
	"state": {
		"state permutation": "thermostat that switches off if natural temperature is equal to set involves permuting state of temperature variable to find a case where AC/heat wouldnt be needed for intent of conserving resources"
	},
	"type": {
		"constant attribute set": "types are a set of attributes that stabilize long enough to be identifiable as a type and interact to form other types"
	},
	"problem": {
		"conflict": "",
		"competition": "",
		"distribution": "",
		"routing": "",
		"grouping": "",
		"organization": "",
		"imbalance": "",
		"catalyst": ""
	},
	"logic": {
		"implication": "",
		"contradiction": "",
		"condition": "",
		"equivalence": "",
		"assumption": ""
	},
	"pattern": {
		"repetition": "",
		"order": "",
		"position": "",
		"function distortion": ""
	},
	"intent": {
		"intent ambiguity": {
			"unanchored/unmatched intent",
			"non-standard distortion",
			"distortions without intent",
			"neutral intent",
			"unknowable intent",
			"alternate intent"
		}
	},
	"potential": {
		"enforced rules": "",
		"breakable rules": "",
		"boundary gaps": "",
		"possibility spectrum": "",
		"interaction space": ""
	},
	"system": {
		"scale": "",
		"localized/mismatched complexity",
		"difference from random configuration",
		"difference from unit configuration",
		"alignment/efficiency ratio",
		"sub-system interactions",
		"threshold adjacence chains",
	}
	"change": {
		"symmetry": "",
		"balance": "",
		"power": "",
		"variance injection": "point where a rule can be broken or has an enforcement gap",
		"variance accretion": "",
		"change demand/supply": "change occurs from triggers (phase shift, threshold, interaction) and the structures that can support them (matter state)",
		"error_types": {
			"rule change",
			"direction change",
			"threshold change",
			"definition change",
			"phase shift"
		}
	},
	"cause": {
		"cause direction": "",
		"alternative": ""
	},
	"interface": {
		"perspective": "",
		"standard": "",
		"filter": ""
	},
	"point": {
		"injection points",
		"decision points",
		"limit points"
	},
	"function": {
		"core function": "",
		"filter": "",
		"equivalence": "",
		"route": ""
	}
}
```


How to generate this list of useful filters to evaluate a system:

	You apply core concepts to core components on core interfaces until you reach a function/object/attribute that explains/generates/determines/summarizes a system:

	"filter_generation_map": {
		"equivalence of core structure": "alignment"
	}

	- "equivalence" is the core concept, the core interface is "structure", and the core structure metric is "direction"
	- "equivalence of direction on the structure interface" parses to "alignment", which is a useful filter for evaluating a system.

	This filter can be applied to generate the next outer layer of filters:

	{
		"alignment of core system component": "attribute alignment"
	}

	which is a "core concept (filters.alignment) of core component (attribute) on a core interface (system)"


What kind of information can you apply to a system once its framed as a set of generative filters to highlight its inconsistencies:
	- randomness
	- change
	- average
	- extremes
	- balance
	- completeness (in combinations)
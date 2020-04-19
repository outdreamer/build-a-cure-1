'''

Go over:

	- object model

	- abstract network

	- interfaces
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/interface.svg

	- core functions
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/solution.svg
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/insight.svg

	- useful structures
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

	- mapping concept to structure
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/concept.svg

		- create a program that checks if a system is robust automatically, regardless of which system
			- what would a concept like 'robust' mean for a system?
				- given the definition route to 'robust' as 'strong enough to withstand various circumstances'
					- you can infer that if a system is robust, it can retain its structure despite application of various change types
					- so query for change types in that system
					- then check which change types break the system & the ratio of (change types handled/total change types)
					- assign a ratio to 'strong' adjective
					- check if the change type handled ratio is above or below the strong ratio
					- if above, the system is 'robust'

	- mapping problem to structure (asymmetry, conflict)
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
 
	- graphing solution for a problem space
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/function_map.svg
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/map.svg
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/prediction.svg
		https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg

	- the right questions to ask to reduce time to solve a problem (see example filters as problem-reducing questions)

	- limitations
		- depends on queryable information (the system must be discoverable) and definitions (for efficiency, although the definitions should be derivable if the system information is accessible)
		- the set of dictionaries used may need updating to build the right queries (there may be more core functions or interfaces to add) but it will discover that during the query
		- some query sets/chains will be more efficient than others, but that will become clear with meta-analysis of queries after its used, so query analysis needs to be done regularly to update query-building logic
		- it will generate possible solutions as it runs and the first generated solution is unlikely to be the most optimal
		- some calculations may need to be made before query can be run (minimum information to solve a problem, relevant insight paths to select interface trajectories, problem solving cost analysis) which can add to solve time
		- some problems are inefficient to solve (resources should be allocated elsewhere bc solving the problem is too costly or efficiencies are imminent in the host system)
		- standard queries (example filters) may beat custom queries for some problems but it may be clear after, so both may be optimal to run


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
		A "signal joint" evolves as a concept in the gene system because it's an output of an important combination of core processes that is not matched with an equivalent handler, so it can cause further complexity bc its allowed to interact with other systems instead of decomposing it after it's used.

- cause cant be traced when:
	- when inputs/system/measurement tools decays/changes before it can be measured
	- when change/decay outputs dont follow patterns or have multiple alternative possible patterns

When a system is totally unknown, you should diversify across all interfaces at first - example of finding value in a set:

	- analyze a set from the:
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

	- key concepts of this problem (like the "tradeoff of search start point/split function/organization vs. performance", "subset gains", "pattern matching", and "potential worst/best case scenario of solution") 
		should be found quickly from various interfaces:

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


Examples of each filter follow:

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
		"false assymption": ""
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
		"equivalence": ""
	},
	"pattern": {
		"repetition": "",
		"order": "",
		"position": "",
		"function distortion": ""
	},
	"intent": {
		"intent ambiguity": ""
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
		"sub-system interactions"
	}
	"change": {
		"symmetry": "",
		"balance": "",
		"power": "",
		"variance injection": "",
		"variance accretion": "",
		"change demand/supply": "change occurs from triggers (phase shift, threshold, interaction) and the structures that can support them (matter state)"
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
	"function": {
		"core function": ""
	}
}

How to generate this list of useful filters to evaluate a system:

You apply core concepts to core components on core interfaces until you reach a function/object/attribute that explains/generates/determines/summarizes a system:

"filter_generation_map": {
	"equivalence of core structure": "alignment"
}

"equivalence" is the core concept, the core interface is "structure", and the core structure metric is "direction"
"equivalence of direction on the structure interface" parses to "alignment", which is a useful filter for evaluating a system.

This filter can be applied to generate the next outer layer of filters:

{
	"alignment of core system component": "attribute alignment"
}

which is a "core concept (filters.alignment) of core component (attribute) on a core interface (system)"

'''
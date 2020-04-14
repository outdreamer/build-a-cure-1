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
		- for a conflict like vectors aiming at a corner of a closed shape, the structural way to solve that problem is 
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
		"boundary gaps": "",
		"possibility spectrum": ""
	},
	"system": {
		"scale": ""
	},
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

'''
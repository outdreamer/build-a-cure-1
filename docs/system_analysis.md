# System Analysis

## System Analysis applications

	- system analysis should be able to answer questions like:
		- what is a way to reduce computation time in a ml model?
			- with answers like:
				- compressing features along mathematical symmetries of object behavior
		- how do you find the likely relevant causes of a process in a system? With answers like:
			- scan the relevant properties & rules of interacting objects, where relevance has various definitions (distance, adjacency, similarity)

		- use logical unit isolation as a source for boundary/symmetry physics
			- 'how to estimate which phase change a rule implementation is at'
		    - required input-mocking or prevention for pathogens
		   	- single live pathogen exposure at ratios amenable to stressor-handling potential energy as a way to build immunity
			- estimate phase changes with optimal transport as a method of getting optimal/efficient/possible paths between function i/o out of operation (core function) data
			    example: https://broadinstitute.github.io/wot/
			  - you also need to estimate probable & multi-prioritized transport paths
			- cycling on/off antitumor drugs like mebendazole & essential oils with antitumor effects to prevent tumor growth (such as 1/week, then switch to new antitumor substance next week to avoid hepatotoxicity & other toxic buildup)

		- look at a data set & tell you there's an antecedent variable determining this batch of variables, and an imminent type convergence that will make these two variables intersect, and a plateau of change rule changes in the system so the predictor can expect to remain valid for a while after the type convergence.

		- why use system analysis in a neural network? because:
		  - the neural net needs some concept of system mechanics built in in order to fill in the gaps left by data
		  - if you integrate system analysis, the neural network can modify itself to accommodate its changing inputs & output relationships
		  - when a more efficient method to execute an operation is found, 
		    the system analysis nodes in your neural network will make sure your network is updated with the latest optimal strategies
		  - the system analysis nodes will be able to steadily reduce the neural network structure with enough uses to the final set of explanatory features & conceptual metadata, so all that's left is the most efficient prediction function rather than a neural network model function
		  - this will make problems currently solved with AI future-proof & automatable

## General metadata

	- change rules (subtypes like the change rules that dont modify identity/boundary, change rules that add randomness, change rules that add convergence)
	- derivation dependency network between metadata objects (types, variables, system structure, patterns, layer variance)
	- the causal network that can generate a set of values for a variable given a random walk with probability x
	- causal molecules
	- apply metadata analysis to each operation
		properties of an operation:
		- network of side effects (vectors, value sets, probability distributions, ranges, & complexity)
		- network of transformation distance/angles in relevant spaces
		- network of change responses to set of all possibly relevant transforms (capable of impacting at least one attribute or rule of the operation or its inputs) done on the operation itself
		- relevant maximizing dimensions
		- structure required to hold info at any given point & full set of info states
		- structure requried to hold sub-operations (vector shape) 
		- position in operation network (starting from origin & navigating outward by minimal incremental steps or attribute improvements)
		- related operations
			- alternative operations with no undesirable side effects
			- alternative operations with irrelevant undesirable side effects
			- reversing operations
			- optimizing operations

	- find the metadata that is most useful in determining other information:
		- are core functions the best method to derive the system structure?
		- once you have system structure, can all the sub-components be derived? Can other systems be derived?
		- once you have the flow network indicating the derivation dependencies, you'll have a framework for deciding which metadata to use to solve which problem types.

	- what does "defined" mean in a space? It means an object has accreted into a measurable phenomena that is consistent by some metric

## General process of system analysis

	- derive core functions/operations
	- classify these core operations
	- find all combinations of these operations that follow patterns of normal interaction & variance (variables like position, compounding ratio, associativity, etc)
	- filter combinations by which are absolutely possible (consistent with the absolute host system), 
		down to the conditionally possible (consistent, within certain conditions/states of the system)
	- derive the system limits
	- filter combinations by which comply with system limits (inflection points, convergence/divergence points)
	- derive change rules
	- filter combinations by which comply with change rules & subtypes
		- for each type of change rule:
			- derive which object interactions are allowed within a constant system of identified objects, and what problems those interactions solve
	- filter combinations by which enable the most/least variance & map them on a manifold or other suitable structure indicating direction of that position/state (set of combinations) 
		toward or away from variance
	- filter combinations by applying patterns of "key derivation structure :: system structure" to tell which combinations to check first
		example: 
			- the "usual number of moves" in chess at which the game is determined is a key derivation structure in the chess system 
			- the "usual number of moves" players plan ahead is another key structure
			- the "function relating the set of possible moves & the set of optimal moves as the game progresses" 
				is another key structure to derive rules like "predict the outcome" or "predict the next move"
			- in the physics system, change rules that dont alter identities (symmetries) are a key structure (described with eigenvectors)
			- apply insights to derive factor matrixes to compute eigenvectors of original matrix:
				- https://www.quantamagazine.org/neutrinos-lead-to-unexpected-discovery-in-basic-math-20191113/
				- "break into components"
				- "isolate unique subsets of variables" (related to pca)
				- "remove the smallest number of variables at a time to minimize error"
				- "remove one variable of each type"
					- rows representing coefficients for all variables of one function
					- column representing coefficients for a particular variable across all functions
				- "variables in a function are by definition related"
				- "removing one item from a list with a known composition metric (sum or product or other dependent variable) lets you calculate the missing item"
				- "apply diagonal transform"
				- "group sub components in different way to get component"
			- vectors are like sliders/dimensions representing a spectrum or other range type - an isolated variable whose value changes across that range
			- this means you can use vectors to represent emergent variables (branches off a vector once it reaches a threshold value to activate the emergent variable)
			- eigenvectors dont change direction bc they represent change
			- degree of order, degree of change, ratio of change to threshold :: change potential (possible moves if limited, states if not)
			- different implementation of randomness, measured by system or component state (or other system object state)
			- this is a good example of how to apply a structure to implement a concept:
				apply('random', 'system_objects') should:
				- pull the definition of randomnesss
				- reduce randomness to concise insight (if not already stored in db): 
					'equal distribution of outcomes across range'
				- produce a list of all system objects & their attributes (like state) and subtypes (like change rules) that can vary
				- filter by which system objects vary equally among all possible values
				- also query for functions that would adjust the system (and its objects, their attributes & types) to maximize randomness
					- query should be formatted like the question:
						"if randomness is equal distribution of outcomes across range, how do you guarantee that in a system with other sources of randomness?"
						- add variables that increase range of possible values without changing distribution
						- add variables that increase equivalence of distribution
			- markov chain: where the set of possible new states is determined by current state & change rules (how to move pieces) & system limits (number of open spaces)
			https://www.quantamagazine.org/mathematicians-calculate-how-randomness-creeps-in-20191112/
			- randomness usually occurs with the patterns:
				- starting from the same origin & diverging at equal angles
				- converging to the same filter point (system entry point, like inputs to a function)
	- find the rules of which objects can generate key object combinations that are important 
	- find the rules of finding which key object combinations are important
	- talk about differences between systems & spaces they inhabit
	- when you describe the attributes & functions of an object, make sure to list key attributes of each function in a keywords attribute for quick searching for relevant interactions
	- why would "finding the symmetries that involve transforms that dont compromise identity of any objects in a system" 
		solve the question of "how to model these specific object interactions efficiently"?
		- because they were trying to model the object interactions that would stay within a range of identities (particles, energy) that can be transformed into each other & back
	- when that system changed, what happened to the object interactions?
	- find the symmetries applicable in a space, find the rules that explain interactions within that object identity range
	- symmetries can describe the rotation of attributes around a type (axis)
	- identify coordinating/competitive and dominant/passive types to predict diverging/converging behavior
	- examine how types (attribute sets, like a set of biometrics or symptoms) move when they evolve in different parts of the system
		and whether you can derive a rule in their attribute set branch positions for converting one to the other
	- attribute set value network: contains combinations of common values (or values known to indicate a particular identifiably distinct state, like a medical condition) in an attribute set, 
		where vectors indicate the known causal flow between attribute value combinations
	- the origin of a type: 
		- when attributes cluster, it's because they have coordinating functions (or their inputs/outputs do)
		- when attribute sets split, it's because the attributes didnt have enough variance to describe input variance (like in a new environment or disordered system)
	- interactive system analysis with a sample db of rules/types:
		- examine possible sub-systems given core functions & output set of likeliest sub-system sets
	- object modifications:
		- small changes in structure can invalidate functionality - find a list of those change types
		- each object has a field of potential in which it can be distorted outside its normal boundaries, until it's not recognizable as the same type
	- list methods of variance flow on the change interface (function):
		- how variance accretes in various metrics according to distortion of problem
		- ex: diabetes can cause problems like hormone disruption and kidney problems, 
			and the problem that shows up first depends on which system is more distorted by diabetes,
			as they have different markers but indicate the same underlying condition
	- list methods of identifying metrics of optimization, such as gaps in efficiency:
		- how a priority/intent/problem can be handled with fewer resources

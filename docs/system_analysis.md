# System Analysis

How to decide which layer to choose core functions at?
- the lowest layer is mathematical, directly operating on numerical values (add, multiply, etc)
- then above that you have functions (composed of those lower math operations) having successively emerging intents, starting with functions that are system agnostic & apply to all systems (find, combine, merge, build, etc)
- above that, youll have a layer of functions composed of lower operations that apply exclusively to the relevant system you used to derive the core functions 
	(for a biosystem, functions like "borrow a gene", "learn an attacker profile", "send signal")

# System Analysis applications

System analysis should be able to answer questions like:
- what is a way to reduce computation time in a ml model?
With answers like:
- compressing features along mathematical symmetries of object behavior

Or questions like:
- how do you find the likely relevant causes of a process in a system?
With answers like:
- scan the relevant properties & rules of interacting objects, where relevance has various definitions (distance, adjacency, similarity)

# Functions

## Find
- find(target, data, filters): 
	- find target type & data type, get relationships between them ('this type is often found at end of document'), apply filters to output

## Apply
- apply(concepts, source_functions, target_function, problem_space):
	- takes concepts or source_functions & assigns them to structures known to interact in that problem space to achieve that function
	- in the absence of concepts or source_functions, it pulls those objects from the problem_space definition
	- example:
		- apply(['power', 'balance'], [], 'decentralize', 'government') should return an insight: 'give components of government power over each other'
		- apply([], [], ['give components of government power over each other'], 'government') should return:
			- a set of insights about the existing & optimal power distribution rules between government agencies:
				- 'technology-progressive agencies may have more power in the form of information' (tech power must be distributed or otherwise limited)
				- 'information should be distributed by need' (agencies with more information like intel agencies will have more power)
				- 'legislative power should be distributed by relevance, intent, & ability' (women should make laws for women, etc)
				- 'veto power should be by consensus weighted by demonstrated ability' (no one person should get to make important decisions)
				- 'enforcement should not be biased' (enforcers would otherwise have endless power)
				- 'enforcement should be automated' (automaters will have more power which must be limited)
				- 'enforcement should be a backup method to prevention' (agencies that do prevention should work with agencies that automate enforcement)
		- apply([], ['max', 'count', 'split'], 'find_biggest_number_in_string', 'programming') should return a function: "max([x for x in input.split('') if int(x)])"

## Generate
- generate(type, input_ranges, output_distribution):
	- gets structures of subtypes within that type
	- applies input_ranges (limits of variables) to generate the set of type examples with output_distribution

## Derive
- derive(target_objects, problem_space): 
	- fetches patterns & functions of the problem space
	- applies them layer by layer (from abstract like apply_filter() to concrete like count()) to derive relationship between objects in target_objects
	- if no results, applies system analysis to find gaps in change & functionality explanations & filters this list by target_objects

# Notes

exploits -> relevant properties 
delegate cost -> efficiency from alignment that goes unregulated (no system rules) where exploit is gap in regulation

core function + core object -> interaction rule of core attributes that aligns with core function + core object priority
- depict core functions on their own direction to indicate a dimension when graphing

- find the rules of which objects can generate key object combinations that are important 
- find the rules of finding which key object combinations are important

- talk about differences between systems & spaces they inhabit

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

minimum information:
- with a line in a space, you have this information:
	- the type of change
	- the change rate
	- the angle compared to a standard, like an axis
	- its distance
- and you need to know the following to find its equation:
	- whether its a segment or the full line
	- the space its in
- with cancer you need to know
	- its position in the system
	- its input resources
	- its limits
	- its change methods (stress-handling methods, learning methods, etc)
	- whether it converts to other objects (like other cancers or a pathogen) & how
	- its history (how did it evolve)
	- its types
	- its target priorities
	- its cooperative agents (which organisms it helps or can receive help from)
	- how it interacts with other objects (that arent immediately classifiable as resources or targets)

- given different information, you can use different methods
- some methods are immune to information but most require a clear minimum


Apply metadata analysis to each operation
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

time can be defined as:
	- how many systems are capable of interacting on the same interface layer & the trajectory across the manifold of possible interaction combinations of those systems
		- whether other layers of interaction are system-adjacent (possible) or whether interface physics prohibits interactions on those layers for this system interaction trajectory (timeline)

	- if a variable changes with time (possible variance), that doesnt mean time (possible variance) caused its variance, 
		but the system collisions enabling the set of interactions possible in that layer

	- the flow of system molecules follows a physics that should be able to explain system change rules
	- the key question is: what is the system (set of core functions) that could generate the set of possible systems we assume exist, 
		and what host system could enable these core functions to result in combinations explaining those systems?
	- what is the host system in which system molecules exist? its modelable as a network with different states (structural math layer) in a particular interface (core dimension set)
	- what is the path between the math layer & the others that allows the math layer to contain its own internal rules and also capture all other rules?
		- the math layer is so important bc its the rules of value & structure, & it's relevant when we can observe/measure other systems to the point of being able to assign value & structure
		- systems that cannot be measured can be guessed but not proven, unless the set of proofs leaves only one possibility for that system's position
		- if there is only one possibility left to the question that explains the variance in this universe, then time doesnt exist in this universe
		- the point wouldnt be to predict future behavior, but to derive source rules of the universe
			& then optimize them for a universe where time could exist (every question cannot be answered in that universe)
			& then detail the steps necessary to trace that universe to this one
		- if there is a universe where every question can be answered, it might poison adjacent universes with its certainty, so they might pool their variance to introduce chaos to that one
			if there are remaining problems to solve in those other universes (systems with non-determinable winners using info available inside the universe, in that state)
		- information has to leak to preserve variance in this system
	- when you standardize the other layers to the position interface, it can be captured in the math layer
	- what is the causal relationship between these layers? does math cascade into the others or just capture their structure, once it decays into information?
	- math is the unit system in the system layer, just like information is the unit object in the conceptual layer (unit/key object: out of which all other objects are built)

- example of a different conceptual system:
	- if power favored centralization, another core concept like balance would have to favor a chaotic process or not exist at all, or another core concept would need to be added to the network

why is object-attribute-rule model insufficient? bc 
	- there are subtypes of rules that need to be handled differently (change rules, boundary rules, etc)
	- objects exist in a broader system that may invalidate isolated analysis (system analysis)
	- the object evolution is not derived (causal analysis can provide this)
	- it doesnt have a model for deriving & applying patterns of change/boundaries/rules

why is pattern separate from function table? bc
	- pattern is a sequence (of anything), function is a sequence (of operations) with expected input/output
	- you want to store some common patterns in a data set (such as variable value trajectories, like if butterfly always comes after larvae),
	  so you can identify insights of the data set & similarity to other data sets
	- the function is a specific implementation of a pattern sequence, restricted to operations & input/output, & there are many functions that can produce each pattern

why is strategy different from insight?
	- insight is the rule, strategy applies a rule in a context to achieve a goal
	- strategy:
		properties:
			- a context condition, involving evaluating information about objects in isolation, without a system context
			- an intent
			- insight(s) describing the functions needed to get from starting point (condition x) to the goal (z)
			- objects & a function relating them

		- ex: 
			- "given condition x, do function y to achieve intent z"
			- "if the object is decomposable into subcomponents, split it into sub components & handle them separately to achieve the goal of deriving its functions"

		- sometimes there will be strategies that have no context so theyre basically just core functions,
			like:
				- "break into smaller objects and handle those one at a time", 
				which is a strategy that applies to solving problems in general & also fighting pathogen infections in the bio system
				- "break into subsets and recombine to get original"

		- often strategies will involve conditions to choose between insights:
			- "if insight x doesnt work in the range of metric y, try insight z"

	- insight:
		properties:
			- a rule set where the insight applies, explaining how one object in the rule set is linked to another
			- bc of this, theyre usually tied to a system context, & applicable in a set of systems rather than applicable to any object
			- objects & a function relating them
		- ex: 
			- "function y is useful for intent z"
			- "power favors decentralization" (system context: abstract network + any system that interacts with the concept of power, which is any system involving resources)

why is intent different from strategy?
	- intent is the target end state, and the strategy is the plan to get there

why is priority different from intent?
	- priority is a concept, intent is a concrete goal

	priority:
		- properties:
			- abstract concept that applies in most if not all system contexts
		- ex: efficiency, balance, fairness, stability, relevance

	intent:
		- properties:
			- current/target objects & functions relating them
		- ex: "if condition x, maintain efficiency of function y outputs"

- list methods of variance flow on the change interface (function):
	- how variance accretes in various metrics according to distortion of problem
	- ex: diabetes can cause problems like hormone disruption and kidney problems, 
		and the problem that shows up first depends on which system is more distorted by diabetes,
		as they have different markers but indicate the same underlying condition

- list methods of identifying metrics of optimization, such as gaps in efficiency:
	- how a priority/intent/problem can be handled with fewer resources

general process of system analysis:
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

general metadata:
- change rules (subtypes like the change rules that dont modify identity/boundary, change rules that add randomness, change rules that add convergence)
- derivation dependency network between metadata objects (types, variables, system structure, patterns, layer variance)
- the causal network that can generate a set of values for a variable given a random walk with probability x
- causal molecules

examine shape of universe nexus by which problems are solvable & which are not
unsolvable problems are dependent on a conclusion that is not constructable with known information or functions
for the most part, unsolvable problems related to objects that are not understood or not based in our universe, 
so we only see their impact on other objects as they cascade into our perceivable universe or theorize their construction by processes we can perceive

common types of problems usually considered unsolvable:
- computationally expensive but not impossible (information-dense, like how many particles are in the universe or how many prime numbers there are)
- imperceptible relationship/object considered impossible to verify (what is the structure of other universes' nexuses)
- conceptual relationships not mapped to math operations


find the metadata that is most useful in determining other information:
- are core functions the best method to derive the system structure?
- once you have system structure, can all the sub-components be derived? Can other systems be derived?
Once you have the flow network indicating the derivation dependencies, you'll have a framework for deciding which metadata to use to solve which problem types.

Just like the uncertainty vs. certainty pattern, 
there are patterns in the minimum information required for certainty (guaranteed that it can be known)
& patterns in the minimum information required for uncertainty (guaranteed that it cant be known)

By navigating the certainty interface (angles, distance, order), can you derive the shape of the corresponding object in the uncertainty interface?

- what does "defined" mean in a space? It means an object has accreted into a measurable phenomena that is consistent by some metric
- how do different layers of interaction objects emerge? 
	- why do collections of properties accrete into objects on one layer & other property collections gather on other layers? 
	- do mostly objects with similar types, functions, attributes, attribute values, or complexity interact?
	- how do objects of very different types (an attribute & an object) usually interact in systems, or do they not have behaviors defined outside of similarly typed object interactions?
		example: does a cat respond to teeth (attribute) the same way in any object, or only when attached to certain objects, like a dog, or when it has a certain value (sharpness: high)
- what happens when a system or space is exhausted and all combinations & interactions have been defined? 
	- does the interface of variance freeze/stabilize into a network
	- does its remaining variance gather on other interfaces/layers? 

insight path:
	- with a path relating three objects (a, b, c):
		a    b   c
		   \
		a(x) b   c
			   /
		a(x) b   c (2X)

		- each operation function has a 'reason' such as a 'need' or 'intent': 
			- "a needs an x & b has a function y which outputs an x, so a does y on b to get x"
			- "c needs its property X to be larger so combine with b, which also has property X, where the combine operation is cooperative & doesnt take X away from b"
	- the insight path can be represented as:
		- a set of functions/patterns operating on objects/types
		- where insight components are replaceable with:
			- object metadata:
					- dependencies
					- attributes
					- type_stack
					- alternatives/approximations/antagonists
					- input_variables/output_variables
					- intents/functions/core_functions
				- where dependencies are:
					- source/target objects (receive input from, give output to) 
					- hierarchical objects (objects that generate & objects generated by)
			- an approximation of any of the above
			- a combination of any of the above (operations + inputs, operation function types + input source objects)
			- a generator function to create a random example of an object or object metadata, restricted by params:
				generate(object(type="person"))
				generate(object(type="function", attributes="no(side_effects)", inputs="dataset", outputs="correlations"))
				generate(object(variance=[3x5])), where 3 is the number of variables and 5 is the sum of their variance scores, 5 being the largest
				generate(metadata(type_stack=['species', 'canine', 'chihuahua']))
			

	- Example: 

		A specific rule set representing a simplistic system in a problem space, mimicking the above rule set:

			doctor    					 			patient   					drug

			  				ask

			doctor(patient.symptom_info) 			patient   					drug

				   												drug.molecule.share_electron(patient.component="bloodstream".molecule(attribute.bond="covalent").electrons)

			doctor(patient.symptom_info) 			patient   					drug.molecule.electrons(2e)

		1. "the doctor asks the patient to get the symptom info"
		2. "the drug needs an electron to work so it shares one with a molecule the patient's system produces"

		The insights that are stored in an insight path would include:
			- "doctor ask patient to get info" (get_types, None, get_types, None, get_types) # no operations done on functions, just objects
			- "x ask y to get info" (get_vars, None, get_vars, None, get_types)
			- "person ask person to get symptoms" 
				(a doctor type is person, a patient type is person, an info type is symptoms - for situations where a doctor isnt present)
			- "machine ask person to get info" (person alternative is machine)
			- "x ask y to do function get(implement, data, type)" 
				(function get(implement, data, type) is a function that gets information from data that fits the type)
			- "x ask y to do core_functions(find, match, implement, query, fit, equals)" 
				((find, match, implement, query, fit, equals) are the core functions necessary to build get()
			- "doctor ask assistant to get info"
				("assistant" is a source dependency of "patient" bc the patient becomes relevant to the doctor bc of the "assistant")
			- "machine ask patient to get info"
				("machine" is a target dependency of "doctor" bc the doctor enters the info into the machine)
				- note we can get to this insight by various paths, 
					as reflected in "machine ask person to get info" above, which varies only by type(patient) = person
					which we got to using the types of all objects, then using the alternative of a person (machine)
			- and so on until youve covered all the patterns producible from the dependencies, attributes, types, alternative vars, functions, core functions

		Youd ideally store each insight with the functions used to generate it, in the same order as objects & functions in the rule:
			functions = [get_types, None, get_types, None, get_types]
		in case you want to try to derive the original rule from the insight & its generating functions.

		The insight path itself would be:

			- any combination of these insights that fits into the 3-step rule set above
			- any combination of these insights that fits into a subset, transform, combination, alternative, or approximation of the 3-step rule set above
				- this is bc the rule set can be modified by operations inherent to the rule set to derive other insights, 
				  without logically violating the objects' & functions' rules
				- these inherent operations include:
					- core_functions & functions of rules in the set
					- standard abstract operations (get_type, get_example)
					- conceptual abstract operations, like merge(intent1, intent2):
						def merge(a,b):
							if a.prop.intent == (-1 * b.prop.intent):
								merge_operation.conflicts.add('opposite_intent', a.prop.intent, b.prop.intent)
								# check if this conflict neutralizes a function of either object

			- it might seem best to store an insight path only if its logically consistent 
			  & doesnt violate standard & conceptual operations that hold in the original rule set,
			  but if its abstracted at all, other rules can apply:
			  - when you change "doctor" to "x", then personal interaction rules dont apply because x could be a machine

			- however there are filters that apply for:

				- an insight:
					- it must explain the rule interaction accurately

				- an insight to be part of an insight path:
					- it must contribute to the explanation of how an origin object of a possible route in the rule set gets to its target object
						- for trees, the routes go in one direction, so it's a clear matter of:
						  "explain how the top node gets to the bottom node, which this insight interacts with"
						- for other structures like networks, it may be a more complex route from start to finish of any given path in the network

				- ideally each insight would contribute more than other insights considered, 
					so there should be a "best-fit" insight path composed of the "best-fitting" insights,
					as well as a stack of other explanatory insight paths,
					such as an "abstract" insight path composed entirely of abstract insights,
					containing no specific information except core-function versions of objects & functions, 
					for example the abstract core-function decomposition of "machine" may be any of these depending on context like intent:
					  	- information-storage unit (intent="store")
					  	- operation-executor unit (intent="run_tasks")
					  	- experience unit (intent="entertainment")
					  	- communication unit (intent="interact")
					so the insights containing "machine" would be considered abstract if they had this replacement done

				- the full stack of insight paths can include:
					- an abstract insight path
					- a best-fit insight path
					- a most-efficient insight path
					- a most-reusable insight path (has objects in common with many other systems)

		Then you could apply the generated insight paths from a rule set to a new system's rule set with similar dynamics, 
			as determined by the number of matching insights in the new rule set.

space analysis:
- patterns in ratios between uncertainty generated by a function combination vs. uncertainty-reduction function patterns & potential
	(how does it hide information vs. how can information be derived)
- examine the relationship between the transformation function converting one space into another, and the transformation function converting a space's insights to another space's insights
- shapes of cause & type hierarchies relevant to different spaces
- operations invalidated within a space
- set of all possible spaces (fulfilling concept combinations) & link to the objects best described in that space whose differences are relevant to those concepts
- within a description system, there will be rules linking objects (like a shape & another shape type) that align with significant properties like symmetry that are inherent to the system
	"given any line segment, an equilateral triangle can be constructed with the segment as its base"
- core operations done on one property (length) vs. another property (angle)
- look up math on how to calculate ranges of all possible combinations of a vector set (span is one type of full combination set)
- when you do analysis of vector combinations, look at the full range of the set of transforms to achieve each core operation & try to derive a type of transform or set of patterns like related alternative type patterns
- when you analyze problem spaces (like euclidean space), examine how core operations & objects accrete in a space (multiple, shift, embed) on every interface layer
- spaces as the intersection of spectrum variables

value analysis:
- derive number type useful for a particular operation ("quaternions for 3-d rotation")
- value accretes into units (numbers)
- what accretions turn into objects that attract/hold (or provide a platform or conduit for) the most variance?
- attributes accrete into attributes ("equipollent when they are parallel, of the same length, and similarly oriented")
- vectors are probably best structure to store patterns & variable value sets

structure analysis:
- when choosing between nodes & links to model objects in a network:
	node: many connections to many other objects having a similar property, like having a type in common, usually unique
	links: usually many connections between two objects at a time, having many possible variations, can be repeated
	
sub-interface interactions:
	- is it better to standardize to object interface, variable interface, type interface, or function interface?

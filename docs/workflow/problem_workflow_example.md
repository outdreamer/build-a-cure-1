Problem: find core distortion functions explaining variation across generated data sets (differing from functions used to generate them, which will involve application of objects like patterns of variable distributions & system objects like intersections & common priorities like 'minimizing work') - in order to make a robust prediction function with one data set.

Here we are applying the problem vectorization workflow.

The titanic data set survival variation is explained with the distortion functions:
	- concept: survival ability, functions: health (process more stress than other people), skills (swim, steer, row), experience (navigate ship), intelligence (organize labor to build raft)
	- concept: priority policy, function: be identified as belonging to a protected group, prioritize people in protected groups
	- concept: randomness, functions: occupy position nearest to life boats, avoid icebergs/storms, run out of space in lifeboats, find raft materials
	- concept: personality, functions: altruism/collaboration, selfishness/competition

To generate the solution path, first implement an insight path in the form of a solution automation workflow, particularly problem vectorization:

	1. fit the problem to a system

	2. identify important structures of the problem system:

		- data set => alternate data set => function to generate alternate data sets
		- concept of distortion => implies concept of a standard => concept of a base to begin distortions with
		- calculating 'explanatory' attribute of distortion functions => metric to evaluate 'explanatory' attribute of distortion functions 

	3. identify missing structures of the problem system (solution format)

		- the prediction function is the missing structure to build

	4. identify interim structures to get information about the missing structures (minimum information to solve)

		- the prediction function can be built from:
			- distortion vector sets converting another function (like a random/average/linearized function)
			- a combination or set of related function components (terms, operations) or structures (lines, positions), or variables
			- function to compose the prediction function using composition functions
			- a generator structure (a system or function that generates the data is a better predictive tool than one relationship in the system)
			- functions to predict subsets (outliers, average-circling values)
			- embedded functions at various points to predict changing values
			- function to identify concepts/cause/intents & aggregate them in a structure that generates or matches the prediction function
			- function to link probable states (different data sets or different distortion levels)

	 	- which have required inputs like:
	 		- distortion combination function
	 		- explanatory (fit) metric selection function
	 		- standard success (accuracy, work) metric selection function
	 		- bases (including inputs like function components, a default function, or an interface) to begin distortions from
	 		- interim structure selection function

	5. generate missing structures inputs & the structures themselves
		- our solution selects the distortion vector set format & the base interim object to build a prediction function, rather than all of the methods listed above

	6. apply relevant insight paths, insights & other relevant interface objects

		- apply insight: 'functions that hold across systems are likelier to be true' to the structures (distortion functions, generated data sets, bases, target functions) to arrive at a solution-filtering method:
			- distortion vector sets that can translate multiple bases to multiple targets are likelier to be true (true in this context meaning, 'robust & generative of the prediction function for a period of time')

	7. apply solution filters

		- apply distortion function metrics

	8. apply solution aggregation methods

		- in order to get a prediction function from a set of distortion vector set, the distortion vector sets need to be combined in some way (average weight being a standard way)

	8. apply aggregated solution filters

		- apply prediction function metrics


Once you have the solution path identified, you can execute the solution path to generate the prediction function:

	1 - 3. find/generate requirements for important & interim structures
		- generate alternate data sets
		- select interim structure (distortion functions from various bases)
		- find/generate required inputs (distortion bases, explanatory metrics)
		- find/generate interim structure (distortion function sets, metric calculation function)

	4. assemble required structures (possible sets, metrics, filtered sets) & fill with content
		- assemble interim structure into target structure (prediction function)
		- apply metric calculation functions & calculation result logic

	5 - 6. iterate & apply structure to final output
		- after iteration is complete, fit remaining sets to a structure (if there is only one set of distortion functions, return that set)


The actual solution path (once the automation workflow identifies the interim objects like bases, to connect distortion functions to alternate data sets/target functions) would take the form:

	1. generate alternate data sets
		- fit origin data set to a causal system
		- use adjacent points in variable interaction space (given causation patterns) to generate alternate data sets
		- this can also be done with distortion functions & bases

	2. find bases & targets relevant for distortion functions
		- randomness, as a constant line used as a starting point to generate the target (the regression line)
		- average/extreme (average line, extreme line)
		- step function matching subset regressions
		- alternative functions for outliers & for average-circling values
		- linear (one standard regression line)
		- linearized shape (three lines rather than a parabola)
		- concepts (connecting data set concepts like function types for variable types)
		- system functions (crossing a phase shift limit, breaking a boundary, reusing a core function, responding to an incentive, correcting bias, changing intent direction, converging to a type, variance handlers)
		- function composition components (functions that can build the regression function, subset functions, or data set attributes like outliers/probability distribution)
		- function subsets (values in range/domain a - b, values following a pattern, values having an attribute, values in subsets of size z)
		- adjacent functions 
		- function-generating structure components (functions that can build a system structure that would generate the function, which can be used to infer other data sets)
		- common operation unit functions (add 1, multiply by 1, take to the power of 1) and component functions (add term, add constant, add multiplier)
		- common shape functions (circle, line)
		- state conversion functions (functions to convert between states of increasing curvature)
		- causal functions (like if a causal loop adds an averaging effect)

	3. generate sets of distortion functions using those bases
		- starting from a random base (constant linear function indicating randomized distribution of outcomes across input values), how can you get to the default prediction function of origin data set

	4. evaluate metrics of distortion function sets (like cost given bias inherent to those functions or that space, and whether distortion functions are explanatory across data sets & bases) & filter solution set

	5. evaluate fit of sets to problem space & filter solution set

	6. fit remaining sets to structure (like a network of solution sets, having been aggregated/organized)

		- example: they can be aggregated according to probability (how likely is randomness to be explanatory), to a component or subset (does randomness explain a subset of the data or a ratio or component)


Actual queries implementing solution path

- to generate alternate data sets using the origin data set:

	1. identify variables (age, gender, roommates, proximity to life boats, room number)

		- identify variable metadata (extreme versions of those variables (ranges), variable types, variable change probabilities, variable relationships, variable averages)

	2. identify bases (concepts, function versions, function subsets, function components, variable patterns, common structures like lines)

	3. identify & generate missing information (minimum information to solve the problem)

		- if variables can interact but dont appear to directly in the origin data set, find the output of their interaction in a generated data set

			- a wide range of age in a set of roommates indicates the concept of a family, (one combination of age x roommates = family concept) so combine those in a different way to get different concepts that might be relevant (same age x different gender = couple, same age x same gender = colleagues or friends), which have similar probabilities to families, so if the origin data set has an extreme proportion of any of those, alternate the proportions to create an overall equal distribution of those concepts across generated data sets

		- if a variable relationship has a certain level of noise, that implies an alternative relationship might hold in different circumstances or across a subset of the data, so create a set of alternate variable relationships to explain the noise and assign the alternatives probabilities, where alternate generated data sets might have the noise explanation as the primary data set descriptor and the original data set's primary descriptor might be the noise in the alternate generated data set

			- similarly, map outliers as a combination of variables/values and generate alternate combinations of variables/values that can generate them for alternate generated data sets

		- treat a data set as a set of subsets (splitting data by ranges, patterns, centrality orbits, and other concepts) and unify explanatory models of subsets based on variable aggregation/function development dynamics

		- derive inferrable variables & translate data sets to those variables if their probability distributions are more known

			- example: deriving the concept of 'state at time of impact' (with values like steering, sleeping, being sick) is inferrable & may be traceable to available data on survival (people who woke up faster may have been likelier to survive, people in rooms with windows were less likely to be kept awake from boat rocking, people farther from kitchen or traveling alone may have been less likely to get sick), and more information may be available about sleep patterns or other states to estimate the proportion of people who were likely to be sleeping at time of impact than is available for other variables

		- derive components of the data set and generate alternate combinations of components

			- example: the inferred concept of 'roommate' from the room number variable implies the location concept of 'room' (with core objects including walls) - were there areas of the ship where people were sleeping in open areas and is a concept of an open room possible or likely in the problem space (where the open area travelers had different survival rates), or was someone sleeping/trapped/another relevant state in some location concept considered not a room, even if it had walls (captain steering)

				- if so, alternate generated data sets could have variance in survival on a 'null' value for room number, or add a 'state' variable describing their activity at the time of impact

		- identify standard statistics that are missing & fill them in: 
			- if an average value is missing from the data, include that in a generated data set, as well as data around that value, for a subset of generated data sets that have the same average as an assumption

		- in the absence of other information, a probability distribution associated with variable values & metadata or their patterns can be used to generate other data that creates that probability distribution across all generated data sets

			- you can also apply limiting patterns or rules, like:
				- 'if the maximum variance seen across standardized data sets with this metadata (causal distance/structure/level of predictability from inputs) is under x, keep variance across generated data sets under x'

		- generating the 'best case scenario' where everything goes right & other scenarios can help generate alternate data sets, with various alternated conditions:
				- what if the weather was better than reported, what if most people could swim, what if some people survived extreme conditions but eventually succumbed

		- trying to predict survival from age/gender/room number may be inherently a flawed question to ask
			- trying to predict skills or likelihood of roommates both surviving from the data set may be a better question to ask
			- these questions can be used as a proxy for 'general survival', if you can build 'general survival' from contextual survival types like 'survived events' or 'co-survival'
			- generating the contexts where those variables would be causative might exclude the 'sinking ship with this technology' context
			- there were limited survival supplies and so a certain ratio of travelers werent going to survive even in the best circumstances
			
			- identifying the definition of 'survival' may include other contexts like: 'surviving certain events like the lifeboat hitting a rock' or 'surviving until they got to land' or 'surviving drifting for a period of time', so identifying which definition applies is relevant to correctly interpreting the data

		- survival may depend on other factors not included or inferrable with the data set, like independent causal chains (randomness chains like being rescued by passing ships or populations or tides that point them to land, which can be modeled with additional data or if those probability distributions are inferrable)

	4. check if the distortion functions that generate a prediction function from one base/data set can be used to generate a prediction function using another base/data set

		- can distortion functions of altruism/selfishness generate a prediction function given the priority policy base (once standardized to that base)?
			- example: a policy protecting weaker groups is a form of altruism

		- if so, these rules are likelier to be true than distortion functions that cannot be reused across bases

	5. filter out unnecessary functions in a set and filter possible alternate sets by patterns/probability or other interface information

- then apply structure to distortion function sets (position sets in a network relating them)

	- example: weight the distortion function sets to aggregate them to a final base & distortion function set
	
		- if there is x% randomness likely in the data set, weight the randomness distortion functions by a metric based on x

		- if the subset functions have z% accuracy across data sets, weight the subset distortion functions by a metric based on z

		- if a set of distortion functions is explanatory across data sets, weight that set higher

- the network of related distortion function sets for a particular base should be explanatory if the problem is solvable with the data or interface information available

- ezample logic of function to break a problem into sub-problems

      1. decompose a problem into sub-problems, using core functions like alternate/meta/find applied to problem objects (like how measurement is a core object of a solution, and the prediction function is the default solution object, and a variable is a sub-component object of the prediction function, and so on)

        - an example is breaking a problem into a problem of finding core components & arranging them in a way that passes filters formed by its solution requirements
          - a requirement of a function that follows another is a possible match of input/output, if the functions are dependent, rather than relatively independent functions (occupying different function sequences), thereby translating a requirement to a filter that can be used to reduce the solution space to only function sequences that have matching inputs/outputs.

      2. Now that we have the sub-problem sets, we can solve the sub-problems in each set.

        For example, to 'find core distortion functions to generate variation across generated or available data sets', you can generate some likely vector sets (based on difference from randomness, difference from averages, difference from common functions, etc) explaining the variation, then apply structures to organize the vectors (by applying requirements of those structures, like how the position or sequence structure has requirements for how it can be applied given its definition). 

        For example, a requirement of a function that follows another is a possible match of input/output, if the functions are dependent, rather than relatively independent functions (occupying different function sequences), thereby translating a requirement to a filter that can be used to reduce the solution space to only function sequences that have matching inputs/outputs.

        Another indicator that one function follows another is that one function reduces the work of the other function. For instance, if one function is 'go to a hub node' and another function is 'find the nearest node to a hub node', the first function drastically reduces the work of the second function, so it can be inferred that the second function follows the first function.

        Rules like this can be derived given the definitions of the objects involved, as well as common interface objects, like common core functions, distortion patterns, or intents, on relevant interfaces to the problem objects (like in this case, how intent is a relevant interface to the function object).

        The objects involved, like a function sequence, postion, & function (including function sub-components like input/output/work, etc) have interface objects like intent, and common intents include 'reducing work' and 'organizing objects to coordinate' (like sharing resources created by work by linking input/output).

        The solution to 'find core distortion functions to generate variation across generated data sets' involves:

        A. generating other data sets if they haven't already been generated (by identifying variable limits & combining alternate variable values according to a likely distribution of variable values, given common patterns based on variable metadata)

        B. identifying common bases to base distortion functions on:
          - random (start from random decomposition of a data set like a random combination of explanatory vectors, or by assuming as much as possible of the variation is noise, and the actual prediction function is a constant linear function)
          - average (start from average or general prediction function found for a data set)
          - common structure functions (reverse, inverse, opposite, magnify, shift)
          - common shape functions (line, wave, parabola, circle)
          - common concept functions (type, convergence, efficiency) and specific concepts to the problem space (for predicting a species, this could include DNA distortion functions, conflict distortion functions, environment distortion functions)
          - common causal functions (variable loop, like hormone disruption leading to aggression leading to structural damage leading to mutations leading to hormone disruption)
          - component functions (add variable, add term, add operation (exponent, multiplication), add constant)

        C. then apply structures to those distortion functions (combining them, positioning them in a sequence, applying splits between alternates, etc) and test what metadata (level of work/accuracy) is found & probable/required for matching structures that explain the data, and whether that level of work/accuracy matches the problem space

          - if 50 iterations of a function are necessary to get from the base to the actual prediction function, that is less likely to be true than one requiring 5 iterations, unless the problem space has a bias or requirement of extra work (if a base 10 or 5 is applied, those iterations would have different costs)
          - if the distortion functions predict the actual prediction function with near perfect accuracy, that is less likely to be true across all generated data sets than a less accurate set of distortion functions
          - if the problem space has a bias toward a particular operation (like favoring addition over exponents, by making addition less work than exponents), that can filter out distortion functions involving exponents as less likely

        D. filtering out the least explanatory distortion function sets across all generated data sets

        E. finding a structure to contain any remaining explanatory distortion function sets, like a directed network of distortion function sets that should be applied with various contexts like phase shifts or assumptions, or taking the average of various sets of distortion functions to produce a robust default set, with conditional distortions of the default set.

      3. After problems have individual solutions, you need a way to integrate the solutions - aggregation or averaging solutions is an appropriate solution integration method for solutions to the same or similar problem formats, but not across any problem set.

        For example, if one sub-problem set is to generate a prediction function, and another sub-problem set is to measure the prediction function success, the solutions to the measurement should be applied after generating possible prediction function solutions, to filter the set into a subset that is likelier to be successful.

        The positions of each sub-problem set can be derived using logical positioning. A generative set should be followed by a measurement set because the output of the generative set (prediction function generated) matches the input of the measurement set (prediction function to measure) - this is input-output chaining as mentioned before. A causal set may identify missing information in a variable set to establish cause between variables - that type of structure (missing information) should be followed either by generating the missing information, and if not generatable, should be integrated into the accuracy/confidence/error metrics, as not being able to find the information required to solve the problem (creating an accurate, robust prediction function).

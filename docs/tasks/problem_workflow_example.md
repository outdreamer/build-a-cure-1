Problem: find core distortion functions explaining variation across generated data sets (differing from functions used to generate them, which will involve application of objects like patterns of variable distributions & system objects like intersections & common priorities like 'minimizing work')

The titanic data set survival variation is explained with the distortion functions:
	- concept: survival ability, functions: health (process more stress than other people), skills (swim, steer, row), experience (navigate ship), intelligence (organize labor to build raft)
	- concept: priority policy, function: be identified as belonging to a protected group, prioritize people in protected groups
	- concept: randomness, functions: occupy position nearest to life boats, avoid icebergs/storms, run out of space in lifeboats, find raft materials
	- concept: personality, functions: altruism/collaboration, selfishness/competition
	
To generate alternate data sets using the origin data set:

	- identify variables (age, gender, roommates, proximity to life boats, room number)

	- identify variable metadata (extreme versions of those variables (ranges), variable types, variable change probabilities, variable relationships, variable averages)

	- identify bases (concepts, function versions, function subsets, function components, variable patterns, common structures like lines)

	- identify & generate missing information 

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

	- check if the distortion functions that generate a prediction function from one base can be used to generate a prediction function using another base

		- can distortion functions of altruism/selfishness generate a prediction function given the priority policy base?
			- example: protecting weaker groups is a form of altruism

		- if so, these rules are likelier to be true than distortion functions that cannot be reused across bases


The actual solution path would take the form:

1. generate data sets
	- fit origin data set to a causal system
	- use adjacent points in variable interaction space (given causation patterns) to generate alternate data sets

2. find bases relevant for distortion functions
	- randomness/constant line
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

4. evaluate metrics of distortion function sets (like cost given bias inherent to those functions or that space) & filter solution set

5. evaluate fit of sets to problem space & filter solution set

6. fit remaining sets to structure (like a network of solution sets)


To generate that path, you would need to first implement an insight path in the form of a solution automation workflow:

1. fit the problem to a system

2. identify important structures of the problem system:

	- data set => alternate data set => function to generate alternate data sets
	- concept of distortion => implies concept of a standard => concept of a base to begin distortions with
	- calculating 'explanatory' attribute of distortion functions => metric to evaluate 'explanatory' attribute of distortion functions 

3. identify missing structures of the problem system (solution format)

	- the prediction function is the missing structure to build

4. identify interim structures to get information about the missing structures

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
 		
Then once you have those structures generated, you can execute the solution path to generate the prediction function:

1 - 3. find/generate requirements for important & interim structures

	- generate alternate data sets
	- select interim structure
	- find/generate required inputs (distortion bases, explanatory metrics)
	- find/generate interim structure (distortion function sets, metric calculation function)

4. assemble required structures (possible sets, metrics, filtered sets) & fill with content

	- assemble interim structure into target structure (prediction function)
	- apply metric calculation functions & calculation result logic

5 - 6. iterate & apply structure to final output

	- iterate
	- after iteration is complete, fit remaining sets to a structure (if there is only one set of distortion functions, return that set)
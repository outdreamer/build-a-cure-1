Problem: find core distortion functions explaining variation across generated data sets (differing from functions used to generate them, which will involve application of objects like patterns of variable distributions & system objects like intersections & common priorities like 'minimizing work')

The titanic data set survival variation is explained with the distortion functions:
	- concept: survival ability, functions: health (process more stress than other people), skills (swim, steer, row), experience (navigate ship), intelligence (organize labor to build raft)
	- concept: priority policy, function: be identified as belonging to a protected group, prioritize people in protected groups
	- concept: randomness, functions: occupy position nearest to life boats, avoid icebergs/storms, run out of space in lifeboats, find raft materials
	- concept: personality, functions: altruism/collaboration, selfishness/competition
	
To generate alternate data sets using the origin data set:

	- identify variables (age, gender, roommates, proximity to life boats, room number)

	- identify variable metadata (extreme versions of those variables (ranges), variable types, variable change probabilities, variable relationships, variable averages)

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

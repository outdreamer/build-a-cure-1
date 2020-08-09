# Intro


## Intro Example

	This project is intended to automate interface analysis (a method to solve problems automatically), to produce solutions to input problems. This tool is based on a core concept of organizing information in a way so that solutions to problems are retrievable or buildable with a query set. Organized information is information that has had structure applied to it, so queries with this tool are applying structures (like filters, limits, or networks) to input information to create solution structures (like requirements, metrics, foundations, solution-generating methods, or the solutions themselves). 

	The problem in this case can be seen as a scaffold (like a network) and the solution is the content filling the scaffold (like an optimized route in that network).

	This program would take the problem statement:
		- "build a tool to detect & display bacteria in a room"

	and output possible solutions such as:
		- "grow bacteria until it's more measurable"
		- "use an animal model in an air-conditioned building (when people aren't in it like at night) that would quickly show signs of infection if the virus was live and present"
		- "display points on an AR interface with magnified bacteria attributes, or applying other data visualization rules to indicate attributes"

	along with other  olution metadata like probability of success, sufficiency of information to select the optimal solution, and which solution is optimal, given which sets of resources are available.

	Another example input problem statement:
		- 'preventing infections from pathogens'

	would have possible solution output:
		- 'create artificial or hybrid pathogen to fight the deadlier pathogen'
		- 'remove deadly components of the pathogen on the structure (surface or protein or genetic) interface that is within 3 causal or system nodes'
		- 'point deadly pathogen at harmful cells like cancerous cells'
		- 'create a cell that will generate antibodies on demand'
		- 'calculate all harmful pathogens and install antibodies for each of them or their most common attributes'
		- 'calculate the stressors that will produce which antibodies'
		- 'calculate which stressors will produce evolution to handle the pathogen stressor'
		- 'create more filters to validate edits done to genes'
		- 'create more backup copies of original DNA to help the system remember which copy to use for comparison during validation'
		- 'create a pathogen to propagate original DNA after any infection'
		- 'calculate benefits of various pathogens and apply them to add functionality to the bio system'

	and other solution metadata.

	Another example problem statement:
		- 'build an optimal thermometer'

	would have possible solution output including:
		- 'automatically shut off the thermometer when optimal temperature is adjacent or reached'
		- 'have backup energy sources for emergencies'

	and other solution metadata.


## Summary

	Much of this project automates the problem-solving methods & structures I use mentally. Other components of this project include important specific functions, like predicting, finding & using important system filters.

	Example of a common system filter, permuting assumptions like system position (position swaps, where position can refer to node identity or system position)

	    - investment risk allocation vs. capital allocation (swap objects allocated)
	    - battery ion vs. base metal (swap a variable on top of a foundation to the foundation position)

	You can predict which system filters will be useful based on system priority

	    - a system prioritizing efficiency will find similarities more useful, and similarities will be more causative & likely to occur in that system

	    - a system prioritizing stability will prioritize & generate more limits, to prevent change types

	You can also predict which system filters will be useful across systems, based on system intent ('find' benefits from gaps & inefficiencies, 'build' benefits from efficiencies)

	The inputs to this system are:
		- a set of core definitions
		- a way to discover information to feed into the system 
			(this means internet access so API queries & searches can be done, if the specific system of the problem space isn't an input, formatted as a system network definition)


	Example of problem-solving workflows this project will automate:

		- how to solve the problem of automating the generation of info objects (summaries, explanations, perspectives, etc)

			- specifically, how to 'explain a complex concept in a concise way' (which is a 'mapping' problem type, mapping expert keywords to concise keywords):

				- explaining ml as 'exploring different combinations of embedded weights on input feature data & weight paths, using filters to determine which weighted feature combinations contribute to incremental prediction function updates' involves:

					- standardizing the concept of an artificial neural network using its concise definition
					- identifying the right objects that are most important to include (combinations, weights, weight paths, features, filters, learning, prediction function)
					- modifying & connecting these objects using the right functions
					- mapping structural objects like weights & filters to a semantic structural definition involving key concepts like learning rate & prediction function
					- explaining why you'd use the mechanics of the system, not just how

				- theres a gap in usual explanations between 'a set of combinations, weights, layers, & filters to update learning rate' and important interim objects like 'weight paths' and the semantic reason of why a set of combinations, weights, layers, & filters would produce a good prediction function, as opposed to standard regression (good for standard or preliminary relationship analysis) or starting from a function of theorized important variables from pca and making incremental adjustments across the most different data points (good for weight initialization)

					- the reason is that adding extra weights in a path (node in a new layer) allows the previous weight state to be changed again, allowing it to be tuned to data & add extra complexity, generality, or accuracy, which helps fit a function to data

						- a visual is small boundaries/gates representing the generality of a theorized function, positioned around the correct function, preventing the function from getting beyond them

					- other important objects in the ML space:

						- errors: the lack of built-in error handling is a reason for regularization layers - other error types can be caught with system/variable pattern layers

						- causal structures: after initial data analysis, the network has the potential to identify other causal structures/levels missed when removing correlated variables that is not exploited

						- function network: the network has the potential to identify an output function network as opposed to one prediction function, where functions can be used under data conditions or to represent anticipated changes to the function

						- system fit: given the inferred system the function occupies, missing or future variables (what did data set likely miss given the noise, despite lack of clear impact of missing variables), error types (what problem types occur), & application intents of the function (used in what decision types) can be theorized

					- these objects can have a map to adjacent objects of a prediction function
						- node layers can represent subset function tangents that are reduced in length to generate a curve

					- 'a set of combinations, weights, layers, & filters' => 'to update learning rate' => 'to get prediction function'

						- origin: weights, layers, & filters
							- semantic: importance, change types, contribution rate

						- interim: weight paths
							- semantic: type paths, attribute sets, causal clusters

						- aggregate: function variant
							- semantic: accurate subset prediction function, general subset cluster prediction function, type specific prediction function, & other variants

						- final: prediction function
							- function generated by network of prediction function variants (with regularization & other extra processing determining which variants & components of them make it to the final function)

					- the ML mechanics of weight paths or regression problem of fitting a curve are similar to the mechanics of deciding which subsets to use when calculating area under the curve 

						- do you use the successively largest shapes that reduce the remaining area to be calculated
						- do you evenly split based on the best subset that mimics the curve the most
						- do you use adjacent functions & their metadata (like area) & the transformations of their metadata, given the transformation of the adjacent function to the original
						- do you match pieces of the function that would create larger or more measurable shapes
						- do you match change rates with change rates of metadata (area)

						- 'a set of combinations, weights, layers, & filters to update learning rate' maps clearly to 'a set of sums, sizes/shapes, scale/accuracy, & split function to update change rate metadata (area) calculation'

						- to map ML to this problem (finding fewest or best objects to use when calculating the area under a particular function), you could assign:
							- feature variation to component (subset or adjacent function) shape
							- feature weight to component (subset or adjacent function) size
							- weight paths to various strategies to split/aggregate, transform/distort, compare/map:
								splitting functions, adjacent function transformation functions, metadata transformation functions (when x & y change in function1, how does metadata change, and how does that relate to how x & change in function2 & how function2 metadata changes), change rate distortion metadata functions (as more sides are added to a polygon to create a curve, how does area change), or subset matching functions to reduce calculations
							- prediction function to best calculation route to determine area under a curve

						- why would you map ML to this problem instead of using a ML network? so you could apply methods of solving the area under the curve to the prediction function
							- using 'subset aggregation' & 'change rate distortion of metadata' to determine the best version & method of combining feature weights to get their aggregate object (weight set, or prediction function), which is area in the other problem space

						- thats the problem expanded by a dimension (to focus on different metadata with an extra dimension, which is aggregation of a different type (shapes of 2-dimensional orthogonal change) than aggregating change rates to form the curve)

							- whats the problem reduced by a dimension? finding the right length of a line for a target intent

							- the next lower dimension problem is finding the right position

							- whats the map of the lower dimensional problem (finding length) to the higher dimensional problem (calculating area)
								- does it cross any metadata of the interim dimension problem (fitting prediction function), such as constants, exponents, coefficients, inflection points, change rate patterns, etc

								- how do change rate & type interaction spaces differ as dimensions are added

				- this explanation can be generated using system analysis (the system interface on the interface network)
			

		- how to solve the problem of automating insight generation & discovery in an efficient way

			- using the pattern interface, identify that insights occur in patterns as people discover levels of detail & complexity in a field

			- identify questions as a key input to insights, especially insights that shift a paradigm (epiphanies)

			- frame questions as a source & destination node on a network, where the standard answer is the path connecting them

			- identify question path patterns across insights

			- use these patterns to jump to the correct insight quicker than normal discovery times

			- using insight paths, question shortcuts, & filters, you can skip ahead in designing an optimal solution, such as:

				- building a tool in the best way first, rather than waiting to discover errors or efficiencies & building them later

				- finding an accurate prediction function network that adapts the best to change

				- how to guess the existence of a sub-system in the absence of information or ability to measure the sub-system

					- for example, if you were a doctor in the 19th century, how would you guess the existence of DNA:

						- given that:

							- you know that families have traits in common, but not why
							- you know about the standard set of organs because you're a doctor & you had to do autopsies to learn how to do surgeries

						- an insight path to generate a theory of the existence of DNA:

							- check known objects for contribution ('if someone is missing an organ, has nerve damage or a brain injury, or drinks a lot of alcohol - do their traits change?')
								- look for counterexamples to any apparent contributions to the output
							
							- check related types for similarities & similarity source location ('are there other species like humans with similar abilities? is there anything functional they have different? where are these functions stored?')
							
							- check for related functionality under changing conditions & permuted assumptions ('when a trait (like hair) is damaged, what happens? some traits are repaired')
							
							- given lack of known object (organ/nerve) impact on traits, change layer or scale (infer that there may be a sub-system we cant see)
							
							- change causal direction/structure ('if organs dont change traits, do traits change organs? is there another causal node leading to both of them or in between them?')

							- apply insights

								- 'changes tend to cascade up in scale'
								- 'complex systems with high variation tend to have many layers & objects'
								- 'if something is damaged & is repaired, there is usually a set of instructions to repair it'

							- apply question shortcuts

								- 'is blood composed of discrete units, like water is composed of drops' (infer existence of cells)
								- 'do blood units differ from liver units, such as by intended function' (infer different cell types)
								- 'are there units with intent/function' (infer existence of microorganisms, match it to medical conditions)
								- 'do some units have intent to give or take functionality from people (make them healthy or sick)' (infer existence of harmful microorganisms)
								- 'could these units be in food or tools we use' (find different examples of resources with microorganisms, like plant fungus & bacteria in dairy)
								- 'would a harmful unit for one species harm another species' (infer high variation in microorganisms)
								- 'does high variation in microorganisms imply smaller inputs generate them' (infer existence of sub-system generating microorganisms & cell types)

								- note: how would you arrive at blood as an object to focus on in the first place, in the above question path?

									- insights like:

										- 'constants can form a platform for change to occur' (noting that blood characteristics dont change much across patients

									- find importance of blood by noting that:

										- lack of blood causes death (implying it's important)
										- that leeches sometimes remove symptoms of illness (implying that blood is related to illness, which can distort traits)
										- that blood circulates through the whole system (implying it's a hub node)

										- so 'important, relevant hub nodes' are a good place to start a question path within an insight path

							- apply testing/filtering insights (to narrow down the possible set of implementations/structures that could explain trait differences & behavior)

								- identify 'mixing bacteria colonies' as the best test, because this tests functionality emerging from combining microorganism species ('does it kill the same plants')
									- if it doesnt kill the same plants as the other pathogen, this supports the theory of smaller inputs than the microorganism layer

								- extrapolate conclusions implied by each inferred relationship output by previous queries
									- if it explains most differences between species, it must be flexible, with many possible versions (infer a set of combinations)
									- if it explains functionality, it must be related to needs (infer stressor as an input to evolution)
									- if it's used as instructions to repair, it must be stored in various places, otherwise anyone without combinations of components would lose the ability to repair
								
							- the next logical conclusions after these testing filters may be:
								- the repair instructions are stored in units of components that are repaired (hair, nails)
								- the function (change unit) instructions are stored elsewhere, and not in organs that youve seen patients with severe damage or without (brain, kidney, appendix, etc)
								- there are units with intent that create functions (confirmed by experiments with pathogens from milk & plants)
								- pathogens have functions & units with intent, and they dont have organs that we cant live without (so its not in brain, kidney, appendix, blood, etc)
								- the units with intent may be located wherever else they are needed to create functions
								- the units may contain function or repair instructions
								- repair is a function
								- the units may contain instructions to create function instructions (function instructions like 'send pain' or 'pump blood')

							- then you could apply more insights given good system design insights or other optimization insights, to guess the likeliest implementation of 'units that contain instructions':
								- 'the safest place to store extra copies of instructions is at every possible location, in case one location is damaged'
									- this would lead to inferring that the units containing instructions each contain all instructions

						- chaining these insights/questions/tests/conclusions enables converting a question ('what explains trait differences') into a theory ('theres a sub-system that contains instructions'), which can be narrowed down with queries, filters, & insights

						- linking these objects requires:
							- having an object in common with a previous point
							- applying core functions like 'given condition', 'apply edge case context', 'remove assumption', 'change variable', etc
							- changing stage (testing/system discovery/filtering, applying question/insight path), according to distance to target (theory of sub-system to explain trait differences)

						- this is one of many insight paths to generate this theory, given a doctor's perspective from that problem space & its technology

							- there are more concise versions based on plant trait inheritance in a garden, or observing plants/animals in different environments evolve different traits, given the faster evolution, or through studying particles/matter state changes with technology or heat sources

							- there are also more abstract paths

								- using system insights like:

									- 'noise appearing in high variation outputs with minimal functionality are often generated by interference in communication between high-variation inputs on a sub-system or other layer'

								  which explains noise (mutations) that cause trait differences, you can cover almost the same cognitive distance as the above example insight/question/filter chain, but with one insight (not covering non-mutation trait similarities)

					- another example: how would you automate identifying gravity without advanced measuring tech or information that makes it obvious, & without someone telling you there's something to figure out or telling you what to focus on:

						- meaning in the absence of a set of coincidences + prior exposure to similar patterns, like:

							- coincidental free time from industry & resource access, a natural object in a location providing an attribute useful as protection
								- with a coincidental useful side effect that becomes apparent when you use it for the protection (tree producing shade with a side effect of apples)

							- exposure to other similar patterns like natural processes happening without human interference 
								- adjacent to the concept of defaults or initial/origin values, or stability/equilibrium

						- adjacent/obvious sources of the insight:

							- sun/weather/shadow patterns

							- invisible rules explaining changes like pathogens follow or generate

							- object interaction patterns in contexts outside of counter-examples (even when interfering force is applied, objects stabilize on the surface)

						- reason/intent to focus on it:

							- something broke or broke something else when it fell (something important like a building or delicate like medical tool)

							- building a machine to use accessible/costless/self-sustaining resources to power it 
								(a ball falls with similar force if dropped from a high enough position as someone throwing it)

							- building a machine to fly (get something at top of trees, construct large buildings, travel faster using wind once airborne)

							- make a ball that bounces higher

							- prevent domino effects from falling (objects knocking each other over)

							- make things lighter to carry

							- looking for fundamental forces

							- explain nature

						- queries to generate a theory of an invisible force governing some motion:

							- useful objects/attributes/functions common in other patterns

								- default behavior (any automatic process could be useful if you can chain/organize/link them in some way that produces an intent you can use)
									- adjacent concepts to default like 'origin' or 'initial value'

								- stabilization (a process that self-restores can be useful as an energy source or a boundary or a constant)

								- equilibrium (a source of balance, or a point to base distortions on)

								- emergent attributes at rest, as prediction tools

							- insight paths

								- system: there are core functions that determine most complex systems that are not in flux from variance injection

								- type: there are different types of forces, such as forces between specific objects, forces that are created by other object forces, input forces, core forces

								- scale: if the earth is relatively big, why would it have similar rules to objects that are small, like animals & buildings have different rules (phase shift)
									- similarly, there may be contexts of different scales where gravity doesnt apply

								- interface: changes happen on the earth surface bc it provides a foundation for those changes to occur
									- those changes dont seem powerful enough to damage the foundation
									- the foundation must have more powerful forces than the changes produced on it

								- variable type differences: given that gravity appears to be constant & universal, and that generally there are different variable types than just constants in a system, it would make sense for gravity to be a constant and for other variables to vary
									- constants tend to be inputs/assumptions, like fundamental forces

								- change: if gravity wasnt a constant or fundamental force, other things would be changing faster or in different ways than they are

								- potential: given that if something has the potential to change, it would be changing with these core distortion functions (combine, merge, split, move, intersect), there would be evidence of those distorted versions of the force if it wasnt a constant or a fundamental force

							- pattern insights

								- usually if a pattern appears in many circumstances in a system of interacting objects, it's because there's a function generating it, not because it keeps happening by accident

						- then apply filters to reduce solution space of possible theories as to the specific function:

							- filtering out counter-examples:

								- objects carried by wind: gravity applies to denser/heavier/higher mass objects

								- objects that float rather than sink to the surface: water has other forces like boundary & chemical rules

							- filtering out immeasurable sources of the insight

								- stars: cant measure how far away they are without tech or math methods or historical information (given slow rate of change of cosmic events), so developing a theory of gravity using star movements is non-adjacent

									- it's possible if they become focused on shadow/weather movement patterns, from which they could infer:
										- sun & earth rotation and gravity from the fact that the rotation repeats
											- which implies one of them is circling the other but not getting significantly closer
												- given historical mentions of similar weather patterns


		- how to solve the problem of selecting between alternative solutions

			- specific solutions:

				- select between solutions for recycling unused waste resources (research enzymes, research using it as fuel, burn it, leave it in space, build new products with it)
				- select between solutions for determining area under a function (add area of subsets, estimate area from adjacent function transforms, transform it until it's composable with known values)
				- select between routes 

			- solution selection abstraction:

				- select metrics (specificity, testing, uncertainty reduction, cost assessment, completeness, success, intent, requirements)
				- select starting point for queries on interface network
				- select starting structures (problem/solution definition, object model)
				- select starting abstract core function (filter, derive, build, change)


		- how to solve an information problem

			- convert it into sub-problems (missing information, info asymmetry, randomness, ambiguous alternatives)
			- query for solutions to those sub-problems (determine missing information, distribute information, test randomness as equivalence of possible outcomes & remove, find attributes that can break ambiguity)
			- find the sub-problem solution sets that cooperate & select one that fulfills solution requirements


		- how to design a product that will prioritize a concept (like anonymity, trust, relevance, equality, distributed power, or checks on power)

			- find structures with those associated concepts (just like the concept of power could have the structure of a hub node in a network), or find conceptual network path building those concepts
			- apply filters to the structures found, testing combinations for the concept based on its definition, or apply filters to the conceptual network path until it has structure


## Useful Diagrams

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


## Terms

### object model

	- this is the standard object-function-attribute model you encounter in programming, applied to systems
	- by attribute, I mean an inclusive set of terms including parameter, variable, input, output, & property


### abstract network

	- this is the network of abstract concepts which are based on core structures (power, balance) 


### conceptual math

	- an example is applying the concept of 'meta' to the concept of 'game' and getting output of the operation like 'a game where games can be created by agents inside the game' or 'a game to design games', given similarities between attributes/functions of objects in the definition & relevant spaces

	- its useful to think of it like conceptual light (information) that can be combined with other concepts given trees of structural layers applied, where the concept is embedded, reflected, or absorbed on the way to the final structural layer - so the computation would be a trajectory on that tree linking the two concepts being combined


### interfaces

	- this is a standardizing filter (can be attributes like cause, change, potential, intent, structure, etc)

	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/interface.svg


### core functions

	- layer diagrams involve applying layers of chained transforms to core functions to generate new object combinations through paths on these diagrams
	- these diagrams can be applied to objects/attributes/systems, which can be framed as a function

	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/solution.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/insight.svg


## Analysis examples

### mapping concept to structure

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


### mapping problem to structure (asymmetry, conflict, lack, mismatch)

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
 

### graphing solution for a problem space

	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/function_map.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/map.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/prediction.svg
	https://github.com/outdreamer/build-a-cure/blob/master/docs/objects/problem_space.svg


## Limitations

	- depends on queryable information (the system must be discoverable) and definitions (for efficiency, although the definitions should be derivable if the system information is accessible)
	- the set of dictionaries used may need updating to build the right queries (there may be more core functions or interfaces to add) but it will discover that during the query
	- some query sets/chains will be more efficient than others, but that will become clear with meta-analysis of queries after its used, so query analysis needs to be done regularly to update query-building logic
	- it will generate possible solutions as it runs and the first generated solution is unlikely to be the most optimal
	- some calculations may need to be made before query can be run (minimum information to solve a problem, relevant insight paths to select interface trajectories, problem solving cost analysis) which can add to solve time
	- some problems are inefficient to solve (resources should be allocated elsewhere bc solving the problem is too costly or efficiencies are imminent in the host system)
	- standard queries (example filters) may beat custom queries for some problems but it may be clear after, so both may be optimal to run


## FAQ

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

		- that doesnt mean there arent cases where finding a new structure (like a core function combination circle layer system or a function system) isnt useful for depicting information in ways that will reveal problem cause & other important info, even revealing solutions if the information is organized in the right structure


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


	9. whats the difference between your conceptual math and 'conceptual math' as indicated here:
		https://towardsdatascience.com/email-spam-detection-1-2-b0e06a5c0472

		- that type of 'conceptual math' is removing attributes of an object and checking for a matching object in a network map
		- my type of 'conceptual math' involves operations on the structures of a concept
			- for example, applying or finding a concept to a system, so the concept can be detected in structures specific to the system
				- applying 'power' to a system would impact the sources of power in that system (like functionality, function inputs, & hub nodes), adding efficiencies making each operation more powerful, alignments to maximize impact of operations, etc
				- the abstract concept of power has structures indicated by its definition routes indicating core applications of power, like delegation & trust
				- applying one abstract concept to another might involve translating both to a system standardized to another interface (than the conceptual interface) so their corresponding structures can be compared, their application calculated, and then translated back to the conceptual interface
				- the concept of power would have different structures in different systems, like how different incentives allocate power differently, but a system would have its standard defined abstract structures in defined positions (function inputs)
				- executing conceptual math operations as indicated in this repo involve standardizing to these interfaces (such as a system), and could involve different power structures each time the same operation is done, depending on context
				- this means the core operation of conceptual math from this repo 'find power' (applied to a system), would still identify a function input as having power even without 'function input' as part of the definition of power or stored as an example of power structures.


	10. is this too abstract to be useful? how would you implement this?

		- the fact that we can imagine what a concept is means it can have structure, & interfaces act like standardizing filters:
		  while they are abstract terms, they have intrinsic physical attributes & map to structures even when they are abstract enough to have few physical attributes

		- the docs for some implementation strategies are here:
			https://github.com/outdreamer/build-a-cure/blob/master/docs/core_analysis/derivation_methods.md
			https://github.com/outdreamer/build-a-cure/blob/master/docs/workflow/problem_solving_matching.md

		- most of my implementation strategies vary on:

			- the starting point of the analysis (which interface the query starts from)
			- the structures relevant (which structures or type of graphing method to use)
			- the intent (create a prediction function, reduce solution space, compare solutions, or match problem with solution)
			- the core abstract function represented (is it a find method, an apply method, a combination)
			- the models used (object model, interface query)

		- but they have in common:
			- using core objects & patterns
			- using info objects like problems/incentives/sub-systems/efficiencies & definitions & concepts like probability/relevance to create defined structures like prediction functions
			- applying structure to unstructured information

	11. can this really be used to automate math insights? that requires complex thought that cant be automated.

		- whoever told you that is full of

			Lattice multiplication method automation
				- https://github.com/outdreamer/build-a-cure/tree/master/docs/specific_problem_analysis/multiplication.md

			Integration method automation
				- https://github.com/outdreamer/build-a-cure/tree/master/docs/objects/problem_space.svg

			Eigenvector/eigenvalue relationship derivation automation
				- https://twitter.com/alienbot123/status/1154930391012167680
				- https://github.com/outdreamer/build-a-cure/tree/master/docs/specific_problem_analysis/automate_math_proof_example.md

			Set generation automation
				- using a similar method as this example of attribute/function combination, generate all possible sets:
				  https://twitter.com/alienbot123/status/1245950414278627328

			- more evidence of damnation:

				- Problem solving automation workflow identifying structure implementing the concept of randomness, which can be used to generate functions with conceptual properties like high ratio of 'calculatability of answer' to 'verification of answer'

				- Identifying randomness as a determining vertex linking the concept of 'average' and the concept of 'balance' or 'equality'

				- Generating the symmetry concept as a combination of reversible changes without losing information

				- Identifying structure as an interface that can capture non-structured information like concepts


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


	14. what does the interface actually contain?

		- the interface (a standardizing filter) is the following:
			- the definition of the concept 
				(the definition of 'cause' for the causal interface)
			- the filter or conversion function to isolate attributes relevant to that interface 
				(causal filter would isolate dependencies on other networks)
			- the set of core objects, attributes, & functions that generate them on the interface, organized as a network
				(causal core functions like 'create' or 'change', and core objects like 'causal network')

		- standardizing an object to the causal interface means mapping how that object occupies or interacts with the network of core causal objects/attributes/functions - this means a query or traversal of those core items


	15. what is the actual workflow to use this?

		- the general program steps include the following:

			1. check pre-existing output of the program (pattern indexes, concept definitions, etc) to see if it can be used as an input filter for a new problem (the system filters below are some of the outputs of this program) to break the problem into solved problems

			2. if it isn't composable with solved problems, but the problem type is still identifiable, then select a solution strategy & starting point

			3. then select threshold metrics to switch between strategies 

			4. then execute the solution strategies, checking at various threshold points for problem-solution match

			5. if no match found for one strategy, switch to other strategies

			6. if no matches found across all strategies, switch to uncertainty description patterns & methods

			7. output either insights found, problem-solution match, or uncertainties that need to be resolved (gather more data, answer this question, etc)

			8. store any info objects found that arent already in indexes (insights, patterns, problem-solution matches, interfaces, functions)



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

But specific concepts evolve within a system, given unique combinations of core objects.

Example:
	- a "signal joint" evolves as a concept in the gene system because it's an output of an important combination of core processes that is not matched with an equivalent handler, so it can cause further complexity bc its allowed to interact with other systems instead of decomposing it after it's used.
	- an "improvisation" is a change given a starting position and new problem information that doesnt match an existing solution

- cause cant be traced when:
	- inputs/system/measurement tools decays/changes before it can be measured
	- change/decay outputs dont follow patterns or have multiple alternative possible patterns


# Analysis

When a system is totally unknown, you should diversify across all interfaces at first - example of finding value in a set:

	- finding value in a set - analyze a set from:

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


## System objects

	- why is it so useful to use system objects like inefficiency or asymmetry as a way to frame & solve problems automatically? 

		- bc these objects offer the most flexibility and occupy an interim interface between physical reality & conceptual networks, so its a good interface to standardize those interfaces to, theyre standard core objects with high interaction potential on similar interaction layers

		- most of the system filter insight paths represent efficiencies & symmetries that become system defaults

			- copying is more efficient than generating an entirely new object, so attribute alignments tend to develop in systems
			- objects with existing (lower cost) alignments tend to cluster into attribute sets
			- most systems need to handle change and constants cant handle change, so constants tend to be fewer in number than variables
			- ambiguities tend to develop in systems with more randomness bc randomness triggers more new interactions, which make change that may stabilize to the normal distribution more efficient, & create objects with similarities, obscuring cause

	- how to generate interface filters (system, type, function), starting with unit interfaces function & attribute:

			abstract    pattern
			set 		system
			subset 		filter

	function    

			intersect   change (convert attribute to function)

	attribute

			set  		type

	- you could extend this to find new objects on the next outer layer after another transform/combination

	- example of system object 'alternate routes'

		- an alternate route is an important system object that can be used to reduce solution spaces for analyzing causation in a system

		- a definition can be more useful if framed in objects on a certain interface

		- equal

			- indistinguishable given measurable attributes & their values - equal in value

			- symmetric (buildable with components the other is built with) - equal in origin (resource attribute set indicating starting position)

			- independent (not buildable with the components that the other is built with) - not equal in origin


## Examples of insight paths (specifically system filtering insight paths)


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
	"info": {
		"efficiency": ["similarity", "overlap", "expectation"]
	},
	"error": {
		"false similarity": "there are many routes to a shape or point which may differ on important metrics like intent",
		"false contradiction": "",
		"false potential": "",
		"false constant": "",
		"false conflict": "",
		"false category": "",
		"false assumption": "",
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

The most common useful sets are:
- core functions
- boundary rules (enforced & unenforced)
- variance injection points
- attribute alignments (similarities, equivalents, alternates, opposites - real & false)
- causal direction/degree
- embedding direction (do you use a tree of networks or a network of trees to frame a pattern)
- symmetry stacks (example: diverging in position, then diverging in shape, then diverging in color)
- intersecting patterns
- interaction space
- potential field
- neutralizing/invalidating rules
- efficiency overlap
- vertex intersection
- tradeoff spectrums


Other useful objects:
- optimality topology (optimizing in one metric direction as a tradeoff or adjacent to optimizing in another)


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
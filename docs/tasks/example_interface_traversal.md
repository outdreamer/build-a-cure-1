# example interface traversal flow diagram and move to spec

		- Here's an example of why different interfaces are more useful in different situations, given a standard problem like 'build a function automatically for a given function intent'.

			Intent interface

				If you want to build a function automatically, and you have code indexed by intent, then you don't need to write code, you need to write the intent & sub-intent sequence or other structure. I would call that 'standardizing to the intent interface' or 'applying intent structures' to the overall function intent, which is the problem definition ('build a function with this overall intent'). If you already have code indexed by intent, framing a function as a set of intents is trivial. If you don't already have code indexed by intent, the process you use to decompose an overall function intent into a structure of sub-intents is a tool that can be re-used to index existing functions by intent.

			Information interface

				If the problem can be framed as an information problem, you can query information problem type rules & patterns to solve it automatically. Building a function automatically given an overall intent would mean:
					
					- solving a series of information problems like:
						- 'information mismatch' (object1 doesnt match object2 and it should, so assign object2 to object1)
						- 'conflicting information' (object1 doesnt match object2 so merge their conflicts) 
						- 'required information' (object1 is required to have this attribute value so assign it)
						- 'missing information' (object1 is missing this attribute so return False or query for that information or generate it).

			Cause interface

				If the problem can be framed as a cause problem, then you are querying for causes. Building a function automatically given an overall intent would mean: 

					- finding the causes of bugs
					- finding the causes of different types of logic & structures (like sequences) applied to different types of logic (inherent rules governing logic given the point/definition of logical operations, like 'an if condition usually precedes a non-if condition' because the point of an if condition is to test for a case to apply logic, where the logic applied is not another condition)
					- finding the causes of functions & function-related objects like side effects, memory usage, optimizations done on other functions, etc
					- then you'd compose these causes in a structure that would allow automatic generation of functions from a given intent (first apply logic-related causes to generate a function causing the given function intent, then check for optimization-causes in the generated function & apply optimizations if those causes are found in your generated function structure, then apply tests for bug causes, etc).

			Structure interface

				If the problem can be framed as a structure problem, then you are querying for structures. Building a function automatically given an overall intent would mean:

					- finding structures to standardize functions to (limits, filters, networks of relationships, directed networks of operations)
					- finding structures to standardize intents to (directions as priorities or more structural goals, possible usage ranges as intents, abstraction as an indicator of intent (neutral/mathematical functions can be used for anything), using intent as a proxy structure for the concept of permission by organizing information access by intent)
					- matching intent & function structures that fulfill the given overall function intent without causing invalidating side effect intents

			Pattern interface

				If the problem can be framed as a problem of resolving which patterns to combine in what structures (where patterns include abstract/generalized structures (such as variables, variable patterns, input-output path patterns, or type patterns) that resolve to specific logic when converted into information, meaning theyre assigned constants), building a function automatically given an overall intent would mean:
					
					- finding which patterns or alternative pattern sets (a variable type relationship pattern, an input-output type trajectory pattern, a logic sequence pattern, an optimization pattern) can generate the required logic when constants (specific information-filled versions of the abstract pattern structure) are applied
						- the output of that may be as diverse as an input-output table to handle a variety of use cases observed, a prediction function trained on input-output data, a logical sequence, a code query, an intent sequence, a directed logic network, etc - depending on the patterns used

			System interface

				If the problem can be framed as a problem of fitting the function to a system, building a function automatically given an overall intent would mean:
					- identifying starting & ending position to map intent to structure in the system (get from input start node to output end node)
					- identify default & alternative (higher cost, lower step count, etc) paths between start & end node
					- identifying system objects like efficiencies, incentives, etc, especially those structures clearly relevant to the default & alternative paths between start & end nodes identified
					- applying definitions of those system objects to select the logical step sequence (avoid conflicts, target rewards without side effects, minimize costs, apply symmetries for standardization purposes)
					- checking which routes fulfill given function intent

			Concept interface

				If the problem can be framed as a set of concepts required for the solution (framing the intent in terms of concepts like 'distribute power evenly'), or if you have conceptual information indexed for code, building a function automatically given an overall intent would mean:

					- using conceptual math operations to determine which structure of concepts is most useful for the given intent (if combining 'power' and 'efficiency' in a 'sequence' or 'balanced' structure would produce the optimal function for an intent like 'distribute power evenly', that is calculatable if you have other functions indexed by conceptual structures, or if you have conceptual math operations accessible to determine what structure of concepts would generate the required concept set, or if you have intent indexed by conceptual structures, or if you can standardize intent & concept to another interface where you have conceptual structures indexed, etc)
						- for example if you have functions indexed with conceptual structures like the individual concepts required (power, efficiency, distribution), what operations can be applied to these concepts to create the optimal concept combination ('distribute power evenly') - meaning conceptual operations like 'inject power to distribution structure', 'limit distribution structure with power injected by efficiency', etc.
						- these conceptual operations involve finding matching structures across the concept definitions:
							- 'injecting' power into a structure manifesting the 'distribution' concept is possible if the distribution-manifesting structure has an input opportunity of some structure, and power can be translated into a structure that can be used by the structure having that input opportunity (a distribution structure such as a function having an input opportunity in the form of a parameter, where power can be translated into a usable structure like information assigned to that parameter), given the definition of the 'inject' operation as 'input the injectable to the receiver'
						- you can avoid doing structural operations by storing the structures for each concept and then storing patterns/outputs of their operations
							- if combining power & efficiency produces a structure set, that can be derived by querying the structures of power & efficiency and combining those structures in a way that doesnt invalidate either definition
						- you can also apply logic to the concept operation ('inject power to distribution, limited by efficiency') to create the output concept of that conceptual operation ('efficient distribution of power'), and then do a structure query of that output concept
						- once you have function structures matching the output (having found function logic matching 'efficient distribution of power' once translated to the structural version 'minimized cost of allocating inputs' if inputs are the structure found in the function system matching the power definition, where 'minimized cost of allocating inputs' can mean 'diversifying calls for this intent across various alternative functions' or 're-using existing functions where possible to minimize the cost of building a function on-demand or at compile time' or 'a function set that minimizes the memory/space requirements of allocating inputs'), you check if those structures optimally fulfill this function's intent, 'distribute power evenly', and then execute the final steps to resolve those structures into function logic (with input-output requirement chains, intent-matching, etc)

			Problem interface

				If the problem can be framed as a problem in a problem network of related problems, and/or a problem space, you can calculate attributes like whether the problem is about to be invalidated by other functions built for other problems, whether the profit opportunity of solving the problem is worth the probable cost, whether the whole problem space is about to fundamentally change, etc. Building a function automatically given an overall intent would mean:

					- determining whether the problem of organizing logic is a solved problem if framed differently (can AI generate code with enough accuracy to invalidate further investment)
					- determining whether solving an adjacent or proxy problem invalidates solving this specific problem (can concept or intent identification tools or even existing code bases invalidate the need for a tool to build functions automatically, or can code bases be re-written in a way that invalidates automatic code generation, by simplifying code-writing to a task of intent-writing or code query-writing or another process simple enough to invalidate complex code and the need to generate it)
						- determining if a solution like logic automation can replace code generation (a tool that automatically applies the definition of logic, including all related objects like logical fallacies, to prevent logically 'jumping to conclusions' or 'ignoring assumptions' or 'over-applying bias vs. updating bias', then indexing code as these logical objects so logical rules can be applied to optimize/generate code)
							- this would involve writing high-level logic language like 'find information, avoid misidentifying object1 as object2, combine common attributes of these objects with versioning in case of conflicting values, avoid this conclusion & this fallacy error type', which would allow logical object definitions (of what a fallacy is, what a legitimate conclusion/assumption/implication is, etc) to be applied automatically, rather than the existing method of applying conditional/contextual/specific low-level logic developer-defined definitions to be applied manually, which involves writing low-level logic like 'select * from table, check if object1.attribute.value == object2.attribute.value, etc'.
					- determining whether the problem can be formatted as a set of solved problems (applying organization to information, applying definitions, finding matching structures, generating tests) or in a format that is solved (route optimization)

			Given the information you have, one interface may be more useful to standardize to than another. If you already have intent or cause information indexed or otherwise adjacently calculatable, or if those interfaces contain the required solution information (as in, the problem is 'finding the cause of some measurement', so the solution is going to be findable on the causal interface), you'd be better off standardizing to those interfaces first, without other information.

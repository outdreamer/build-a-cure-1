- insight extraction
	
	- definitions:

		- map terms to context, usage, & alternatives

		- track concepts
			- when referenced explicitly & implied ('use again' => 'reuse')
			- when useful or required for understanding (is 'reuse' an important concept for understanding logic)

		- update terms with more specific information (low level => binary => boolean)

			- dont specify a term that is repeated (boolean is repeated)

			- replace terms with standardized version (replace 'may not be unique' with 'ambiguous')

			- update references with referenced terms ('four functions' => 'gate operations' mentioned before)

		- pull definitions from:
			- context
			- example (like with truth table & nand gate, removing specific values where necessary)

		- define functions

			- pull relevant verbs to identify functions of an object ('is updated' for memory element, 'tracks state' or 'has a state-tracker role' as one of its functions)

			- pull function definitions from steps

				- indent logic that has iterable or condition context (within a loop, if a condition occurs)

				- indent logic that gives context (in the form of implementation details, like origin point)

				- truth table
					- list all the combinations of two inputs
					 	- start from (0, 0,  0, 1,  1, 0,  1, 1)
					- for each of these input combinations
						- list the output for each of these four functions

	- apply unique information filter:

		- remove unclear segments
			- uses a new term without a clear reason to use it
			- uses a general term that can apply to multiple objects without clarifying which object

		- remove segments that dont add meaning
			- rhetorical questions
			- repeated segments

	- apply definition

		- expand examples given a definition

			- given that a path is 'ambiguous', list the ways it can be ambiguous (which has a structure in this context of 'not 1-1 input-output mapping'):

				- same input, different output
				- different input, same output
				- same input-output, different path

	- identify & organize information:

		- add categories to indicate information intent (design system spec, implement system, hardware components & topics)

			- add new category when a new topic or intent is detected at the same level/topic
				- design & implement are on the same intent level
				- hardware components & hardware problems are at the same level, regarding the same topic

		- add missing information

			- for steps (convert to digital, map input to output, and convert to analog), a related 'intent' object (specifically 'build a function' intent) is missing 

		- identify definition

			- pull definition of 'dont care conditions' by converting "user doesn't care what, what will be the output in these five cases" to "input value sets that dont change relevant output"
			- statement: 'user doesnt care what will be the output in these cases'
				- 'x doesnt care about y' means 'x finds y irrelevant' or 'y is irrelevant to x'
			- standardized statement: 'these cases are irrelevant to the user'
			- irrelevant definition:
				- operates on a different interaction layer (inactive on a relevant interaction layer)
				- useless: doesnt change/help any important things like required inputs
				- pointless: doesnt change/help any important things like intents
					- this includes different intents, so if it fulfills similar intents (is an equivalent), its also irrelevant in a pointless way
			- standardized statement: 'the output of these cases doesnt help/change the user'
			- implied question: what would execute help/change intents for the user
				- user inputs
				- functions to fulfill user intents
			- implied conclusion: these cases dont fulfill user intents or provide user inputs or do anything
			- applied implied conclusion & irrelevant definition to statement:
				- these cases:
					- active:
						- are never triggered
						- are never handled
					- inputs:
						- dont change inputs
							- only change irrelevant inputs
					- outputs:
						- dont create outputs
							- only create irrelevant outputs
					- input/output conversion:
						- change inputs to outputs in irrelevant ways
			- apply irrelevant definition
				- these cases involve inputs that produce the same outputs as the other cases, dont produce an output at all because theyre not allowed, or produce outputs that cant impact the user (cant be measured)
			- apply 'abstract' standardization
				- apply 'remove redundant objects' filter
					- 'these cases' is redundant because a case is an input value set
				- check for different functionality
						- 'produce same outputs' => 'produce irrelevantly different outputs'
						- 'produce outputs that cant impact the user' => 'produce irrelevant outputs'
							- 'impact the user' is 'relevant'
						- 'dont produce outputs' => 'not relevant to user'
					- these are all reducible to 'dont change or create relevant output' 
			- standardized statement:
				- 'dont care conditions: input value sets that dont change relevant outputs'
					- with an 'abstract' intent, we lose information like 'inputs that produce the same output in different ways'
					- with a more specific definition of 'relevance' or additional defining information about the dont care conditions, we can specify rules, generalize more accurately, or add other information

		- derive/identify related information

			- identify steps for an intent (reduce operations in a function, map inputs to outputs, implement a definition of an 'OR gate', test if a gate is universal)

				- "We define an example logical gate as a Boolean function f of x, y, z, it is defined as, as x prime yz plus xy prime plus y prime z, and we claim this function with this gate is universal. And how do we prove this? The first one will show that, I can use this function block f or this gate to implement the inverter. And how do I do that? I set, the second and the third parameter to f as constant to 1, so if I plug in this into the definition of f, I got x prime times 1 times 1 plus x times 1 compliments plus 1 compliments times 1. And because 1 compliments equal to 0, so this last of two terms disappeared, and then 1 times anything is, that thing itself, so this give us x compliments, that is exactly the inverter. And to draw a, a diagram, I can show this, so this is my logical gate f, and how I feed into this system is I feed x and 1, 1 into f. And, but higher from outside the box, what people see is, I give it input x to the system, and then the system outputs x prime, which is equivalent to the logical AND, logical NOT gate, the inverters. So next, we show you how to implement the OR gate, and then similarly, we put the middle, parameter to 0, and then plug in to the definition of f, so we, what we get is x prime and a y 0, so this becomes 0 times z, and the z is the new y here. And plus the first variable, which is x, times the compliments of the second variable, which is zero compliments, plus the compliments of the second variable times the third variable, which is y here. And because we know that 0 complements is 1, and 0, cancel this one so the only thing left is x plus y, which is the logical OR. 'Kay? And then to show this concept, we can go the same figure, is thus the box you feed the x and the y, and internally you are taking 0 as the middle, parameter, let this function f, give you x plus y, so from outside, this looks like a OR gate. And then similarly, we can implement the AND gate, and, which is a little bit of, more, I mean, complicated than, AND, than OR gate or NOT gate. And here is the logical implementation here, with two functional blocks, this one, the first one, get y complements, the second one get x times y, and from the outside you see x, y coming in, and then from outside you see x times y coming out, so, this is the logical AND. And because I can implement a logical AND, logical OR, and inverters, using this f, so I know that f is universal, and I can use f to implement any kind of Boolean functions or any kind of digital systems."

				- identify operations
					- operations:
						- set parameter
						- set parameter to constant
						- identify equivalents (value * 1 = value, whether an input/output mapping mimics an OR gate or the complement of a variable)
						- remove zero term (opposite of 1 is zero, 0 * value = 0)
						- remove neutralized term set
						- apply definitions
							- to specify (inject structure)
							- to identify similarities (categorize examples of a type, identify equivalents)
						- organize function as sequential logic tree

				- apply operations to find equivalents, neutralizations, zeros, identities, & values in function structures (sets, sequences, etc)

				- identify intent by outputs
					- outputs:
						- categorizations (identify an operation set as equivalent to an OR gate)
						- reduce operations
						- possible routes (from input to output)
						- functionality (implement AND/OR/NOT)
						- implications (universal gate implements AND/OR/NOT)


			- identify requirements to identify an object (universal gate) from this paragraph:

				- "A gate or a set of gates is called universal, if it can implement all digital systems or all the Boolean functions. So this is a very, very strong statement, a gate will be able to implement all the Boolean functions, so how can we verify that, there's no way you can en, enumerate all the Boolean functions. So how we do this is, we start, from the definition of Boolean functions, we've realized that, all of the Boolean functions can be expressed as the logical AND, the logical OR, or inverters, so by putting these three gates together, we have the so called, the standard universal gate, so all the Boolean functions, should be able to implemented by these three logical gates. And now this seems becomes easier, so for us to prove, any logical gate is universal, we only need to show that this cage can be used to implement the standard universal gates which is logical AND, logical OR, and the inverter."

				- universal gate definition: a gate set that can implement all digital systems (or all the boolean functions)

					- requirement: 
						- implements all digital systems (general)
							- implements all boolean functions (specific)
								- implied question: what is the input of boolean functions?

					- question: how to verify that a gate set is universal

						- standardized question: how to verify a gate set can implement all boolean functions

					- problem: verify a gate set is universal

						- standardized problem: how to verify a gate set can implement all boolean functions

						- problem limit: no way to list all the boolean functions it can implement

						- problem type:

							- limitation problem: 
								- question: why cant you just list all the functions it can implement
								- answer: its inefficient to just list all the functions it can implement with the intent of verifying all the functions it can implement

							- information problem: 
								- question: 'what does universal mean'
								- standardized question: "what structure does a 'universal gate set' take"
									- definition: 'meaning' indicates 'structure once standardized to relevant system'
						
						- solution:

							- origin assumption: start from component definition:
								- "boolean function: can be implemented with just AND, OR, & NOT"

							- standardize & apply component definition:

								- universal gate: gate set that can implement all digital systems (or all the boolean functions)

								- apply 'specify' intent to make the definition clearer or more relevant

									- inject component definition (boolean function: can be implemented with just AND, OR, & NOT)
											
										- standardize component definition to same format as universal gate definition, for comparison/analysis
											- identify problem type 'comparing different objects'
												- identify corrective action for that problem type: 'standardize the objects until their differences are maximized'
												- apply corrective action for that problem type:
													- identify a common standard for comparison: 'abstract'
													- apply common standard for comparison:
														- identify abstract version of universal gate definition: 'components that can implement functionality'
														- identify abstract version of boolean function definition: 'a function that can be implemented with components'
											- identify problem type 'mismatch' in definitions: 'order of logic'
												- identify corrective action of that problem type: 'reverse logical order'
												- apply corrective action of that problem type:
													- boolean function: 'AND, OR, & NOT components that can implement boolean functionality'
											- identify problem type 'recursive reference': 'boolean is a component set implementing boolean'
												- identify corrective action of that problem type: 'give specific example'
												- apply corrective action of that problem type:
													- boolean function: 'AND, OR, & NOT components that can implement conversion of 0/1 to a 0/1'

										- inject new definition with same order as universal gate definition:

											- universal gate: gate set that can implement all boolean functions
												- requirement: gates
													- output: boolean function

											- boolean function: AND, OR, & NOT component set that implement conversion of 0/1 to a 0/1
												- requirement: AND, OR, & NOT components
													- output: 0/1 converted to 0/1

										- apply universal gate requirement/output to boolean function requirement/output
											- to implement a universal gate that can implement boolean functions,
												- you need AND, OR, & NOT components (requirements of boolean function)

								- output universal gate definition of 'specify' intent: gate set that can implement AND, OR, & NOT
									- now you have a clear structure to look for when identifying universal gates

							- solution metric: to test if a gate is universal, it needs to be able to implement AND, OR, & NOT

		- group relevant processes:
			- conversion of digital to analog & continuous to discrete

		- identify steps & organize into a list
			- instructions (execute this, apply this)
			- possibilities (if, then, can)
			- requirements (should, follow, given)

		- identify alternatives, examples, attributes/rules of an object and organize into a list

		- identify functions from examples

			- identify input, logic, output

			- identify assumptions, implications, expectations, requirements, intent

			- identify metadata like optimization potential

			- identify rule "sequence of gates applied to inputs (x, y, z) produces outputs (sum and carry)" from the paragraph:
				"Consider this example. It has three input x, y, and z and then two output, S and a C, and this basically implements a which is going to add up x and y plus a carry z, and S is the new sum, and the C is the new carry. And the functionality of S is given as the Exclusive-OR of x, y and z., and then the functionality of C is given as xy plus z times, the Exclusive-OR of x and y. So from this definition, we can also draw the logical diagram of this function. So input x, y, z, output sum and a carry, and the inside, we have the basic logical gates, gate, gate, OR gate and the two Exclusive-OR gate. So for example, the first one, is the Exclusive of x and the y. It will be Exclusive-OR with z again, implement has. So this is input from z. 'Kay? And what is interesting in this example here, it also shows that, this Exclusive-OR of x and the y, also comes to this AND gate, or the AND with z here, to produce this term"
			
				- produce/output is the connecting verb between input & output
				
				- sequence implied by:
					- 'first one' (sequence is relevant)
					- 's is the new sum, c is the new carry' (s & c are the objects being changed, the output)
					- 'also comes to this gate' (extra operation)
					- 'with z again' (extra operation)
					- 'xy plus z times the Exclusive-OR of x and y' (chained/embedded operations)
					- 'inside is the gate' ('inside' should be standardized to 'in between')
				
				- ignore the actual values
					- functionality of sum & carry
					- list of gates

		- identify info objects (examples, questions, assumptions, function implementations, problems & solution methods) as insights, if they add useful/relevant information (usable for common intents)

			- insight types:

				- match intent
					- match solution to problem
						- solution to problem 'build a boolean function' is 'universal logic gate'
						- solution to problem 'implement a system better' is 'adding gate'

				- find/identify intents:
					- relevant differences
						- can be framed as solution to problem 'identify differences' from a list of common problem types

				- build intent:
					- relevant components/processes
						- internal function component list
						- prior/post logic external to function

					- implement solution
						- function step list

				- define intent:

					- definitions
						- references
						- usage
						- contextual
						- alternate routes
						- functions/attributes
						- types

					- examples

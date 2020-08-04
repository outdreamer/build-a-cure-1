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

			- identify requirements of a universal gate from this paragraph:
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

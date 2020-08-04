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

	- identify & organize information:

		- add categories to indicate information intent (design system spec, implement system, hardware components & topics)
			- add new category when a new topic or intent is detected at the same level/topic
				- design & implement are on the same intent level
				- hardware components & hardware problems are at the same level, regarding the same topic

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

		- identify examples, function implementations, problems & solution methods as insights

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

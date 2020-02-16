# Selecting a Problem Solving Automation Starting Point


## Relationships

- problem space: 

	- definition: 
		- relevant information to solving a problem, or info describing a system with problems

	- attributes:
		- can interact with multiple systems (bio, chemistry, markets)
		- can have a similar structure to systems (host space, network structure, etc)
		- can be a system
		- is restricted by information thats definitely or possibly relevant to the problem

	- examples:
		- 'how to break a problem into sub-components'
		- 'how to find information in a data store'
		- 'given current tech, whats the best way to count votes'

		- for a problem like 'conflicting intent with incentives in loan market', the problem space contains:
			- relevant objects (loans, loaners, borrowers, interest rates, banks, reserve, laws)
			- relevant variables (market demand & supply for business of borrower, resources of both primary agents)
			- relevant rules (existing laws, process to get laws passed)

- solution space:

	- definition: 
		- the set of possible combinations of resources that can achieve a demanded intent in the problem space

	- attributes:
		- can be a new trajectory between nodes (ordered combination)
		- can be the injection of variance or other systems/patterns into the relevant problematic systems
		- can define a path in an unused/unenforced variance gap
		- can decompose a problem shape into a point by reducing its dimensions
			- example: 
				- a problem shape in a problem space is a shape that doesnt need to exist at all, and is a combination of problem dimensions (conflict, inefficiency, mismatch, missing information) which dont add value to the problem space, so it can be reduced without creating other problems

	- examples:
		- 

- system:

	- definition: 
		- set of rules & objects

	- attributes:
		- can interact with multiple problem/solution spaces

	- examples:

		- for a problem space of solving a memory storage problem, these can be relevant systems:
			
			- software/hardware evolution
				- open source
				- automation patterns
				- platforms/frameworks
				- marketplaces
				- security
				- full tech stack
				- algorithms
				- data structures
				- memory optimization
				- computation (space/time tradeoff, parallel execution, pre-computation, queuing)

			- chemistry
				- materials science

			- physics
				- electricity


I. Match problem & solution using definition & standardization, applying increasing limits until problem & solution match
../docs/problem_solving_matching.md:  II. Solve problem with structure fitting
../docs/problem_solving_matching.md:  III. Solve problem with solution function selection
../docs/problem_solving_matching.md:  IV. Solve problem with Conceptual Query
../docs/problem_solving_matching.md:        Input concepts:
../docs/problem_solving_matching.md:        Input relationship network:
../docs/problem_solving_matching.md:        Concept Intents:
../docs/problem_solving_matching.md:  V. Solve problem with Conceptual Combination Metadata query (different starting point as IV)
../docs/problem_solving_matching.md:  VI. Vectorization of Problem & Solution Space
../docs/problem_solving_matching.md:        I. identify variables, metrics, concepts (and their metadata like definitions, types, priorities)
../docs/problem_solving_matching.md:        II. from previous objects, identify meaningful level of variance
../docs/problem_solving_matching.md:        III. from level of variance to aim for, identify intent & check that it matches problem solving intent
../docs/problem_solving_matching.md:        IV. now you should have:
../docs/problem_solving_matching.md:        I. pre-computation
../docs/problem_solving_matching.md:        II. out of the remaining options, you can use filtering rules when iterating through the remaining possible combinations of steps 
../docs/problem_solving_matching.md:        III. remaining solution (or solution set if irreducible) example:
../docs/problem_solving_matching.md:  VII. Modeling gaps in Problem Space Systems as Solutions
../docs/problem_solving_matching.md:  VIII. interface/symmetry derivation 
../docs/problem_solving_matching.md:    - by 'interface derivation' I mean finding the symmetries in a problem space, such as finding the 'spectrum interface' in the chaotic-evil matrix, or finding the 'rotation' interface in the shape progression problem space, and then stacking or otherwise arranging them in the order that they are most useful for generating/revealing solutions
../docs/problem_solving_matching.md:  IX. System derivation
../docs/problem_solving_matching.md:          - 'If "this sentence is false" is true, then it is false, but the sentence states that it is false, and if it is false, then it must be true, and so on.' https://en.wikipedia.org/wiki/Liar_paradox
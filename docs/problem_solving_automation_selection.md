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

- system:

	- definition: 
		- set of rules & objects

	- attributes:
		- can interact with multiple problem/solution spaces

	- core components:
		- intents
		- needs
		- forces
		- limits
		- potential (variance, opportunities, unused paths)
		- conflicts (paradoxes)

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


## Choosing automation starting point

- Based on where the problem is & what type it is, you can start with different methods:
	- if youre trying to invent something, you can start with structure-fitting or a conceptual query
	- if youre trying to figure a system out, you can start with system derivation
	- if youre trying to predict an optimal function of variables in a system, and you have the system knowledge & intents mapped in the system, you can start with vectorization of the problem space
	- if youre trying to find a path across a variance gap or use unused variance, & you have the system knowledge, you can start with modeling gaps in the problem systems as solutions
	- if you need a quick approximation of system understanding and dont have time for system derivation, you can start with interface derivation
	- if you have a lot of specific information about objects in the system and are missing a few relationships, you can use queries on the object model

- The methods listed in problem_solving_matching.md use different starting points:
	- matching structures
	- solution/problem/system metadata
	- using conceptual/intent/variance interfaces
	- derivation methods (systems, interfaces, functions, structures)

- These differ in:
	- focus/scope/interface
	- info requirements (host system is known, some variable relationship rules are known, some definitions are known, variance gaps are known)
	- tool access (pre-computed conceptual network, access to common solution functions)
	- primary solution function (query, transform, matching)

- the methods in problem_solving_matching.md are examples of how to automate problem-solving, not examples of how to solve a particular problem type
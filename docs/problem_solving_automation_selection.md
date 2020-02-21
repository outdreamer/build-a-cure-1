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

	- structures:
		- dimensions containing system structures (network, chain, tree, slice) and problem structures

	- examples:

		- 'how to break a problem into sub-components'
		- 'how to find information in a data store'
		- 'given current tech, whats the best way to count votes'

		- for a problem like 'conflicting intent with incentives in loan market', the problem space contains:
			- relevant objects (loans, loaners, borrowers, interest rates, banks, reserve, laws)
			- relevant variables (market demand & supply for business of borrower, resources of both primary agents)
			- relevant rules (existing laws, process to get laws passed


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

	- structures:

		- interaction matrix of potential interactions between system components
		- trajectory
		- shape filling a gap
		- map between problem & solved problems
		- set of decomposing functions for a problem shape

	- examples:

		- solution space for 'finding area under a curve' includes:

			- breaking non-linear form into a progression (sum of sub-shapes)
			- finding area of transformed/adjacent objects
			- finding area of terms & mapping to influence on original function area
				- influence can be in the form of original value, term metadata, or set of alternate terms that can create the same output
				- example:
					- if theres a x^2 term in the equation, that limits the ways that the area can vary (in relative terms to the function with that term removed, which is less limited)

			- finding relationship between metadata of generating functions of boundaries (generating function for adjacent object boundary & generating function for original object boundary) & relationship between generating function metadata & boundary function output metadata (summed distance to axis standard)


- system:

	- definition: 
		- set of rules & objects

	- attributes:
		- can interact with multiple problem/solution spaces

	- core components:
		- forces
			- limits/needs/incentives/intents/paradoxes
			- function sets
				- change rules
				- organization rules
				- interaction rules
				- binding/combination & separation rules
				- pattern rules
				- boundary rules
				- alternation rules
				- information rules (storage, replacement, merging, monitoring, indexing)
				- filtering/matching/application/derivation rules
				- learning rules
				- uncertainty/risk/potential rules
				- variable combination & replacement rules
				- variance leakage rules 
					(how does system become overwhelmed, does it have outlets to reduce variance, does it have interfaces with other systems to delegate variance)
				- solution rules
					(variance/stressor/error detection, tracing, identification & handler)
				- stabilizing rules
				- emergence rules
				- abstraction rules
		- potential (variance, opportunities, unused paths, adjacent states)
		- conflicts
		- distortions/differences from standard types or core objects
		- cooperation/communication/binding sites (openings in system)
		- structures:
			- layers
			- vertices 
				- core points (corrollary of core functions)
				- sets of generating functions/objects/attributes/constants/types that determine the system
				- for example, the center is a vertex of a circle
			- hubs
		- relationships:
			- relevant interfaces & interface trajectories
			- applicable spaces

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

- based on where the problem is & what type it is, you can start with different methods:
	- if youre trying to invent something, you can start with structure-fitting or a conceptual query
	- if youre trying to figure a system out, you can start with system derivation
	- if youre trying to predict an optimal function of variables in a system, and you have the system knowledge & intents mapped in the system, you can start with vectorization of the problem space
	- if youre trying to find a path across a variance gap or use unused variance, & you have the system knowledge, you can start with modeling gaps in the problem systems as solutions
	- if you need a quick approximation of system understanding and dont have time for system derivation, you can start with interface derivation
	- if you have a lot of specific information about objects in the system and are missing a few relationships, you can use queries on the object model

- the methods listed in problem_solving_matching.md use different starting points:
	- matching structures
	- solution/problem/system metadata
	- using conceptual/intent/variance interfaces
	- derivation methods (systems, interfaces, functions, structures)

- these differ in:
	- focus/scope/interface
	- info requirements (host system is known, some variable relationship rules are known, some definitions are known, variance gaps are known)
	- tool access (pre-computed conceptual network, access to common solution functions)
	- primary solution function (query, transform, matching)

- the methods in problem_solving_matching.md are examples of how to automate problem-solving, not examples of how to solve a particular problem type

- solution methods for specific problem types include:
	- intent-mapping
	- interface math
	- system analysis
	- derivation methods listed in derivation_methods.md

- solution methods for specific problem types can be used in a solution-automation engine, but theyre not solution-automators themselves
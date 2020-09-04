''' poc system object identification:

- import system as network

	- system of rules like:
		- 'A communicates info to B'
		- 'B converts info to a format that is interpretable by C, D, & E'
		- 'B sends the info to C, D, & E'

- pull efficiency definition: 

	- interaction that fulfills an original intent with higher or similar resources after units of work, compared to units of work

	- pull sub-object definitions
		- interaction: function connecting multiple objects
		- cost: unit of work
		- benefit: resource that can be an input for an intent

- convert definitions to system interface

	- find routes that 'fulfills original intent with higher or similar resources after units of work, compared to units of work'

	- convert sub-objects to system interface
		- resources in the system
		- intents supported by the system
		- original intent of the system
		- units of work in the system

- create combination list of objects in system
	
	- resource A + function B for intent C
	- function A + object B + function C for intent 'get function C output D'

- identify objects or combinations matching converted structural definition routes

	- identify relevant object filters in the system
		- units of work that result in higher or similar resources after the units of work
		- intents that have a high association with high resource/work ratio
		- resources that enable a high ratio of work units (resources that are an input to many functions)

	- identify system structures often found with this object type (efficiency) or related object types (inefficiency)

		- attribute: required/unnecessary

			- required/unnecessary standard system components (using info objects found in systems, like ambiguities)
				- required/unnecessary ambiguities (options, unenforced rules, variables that should be constants or removed, etc)

			- required/unnecessary specific system components (objects/functions/attributes)
				- required/unnecessary sub-components (function inputs/outputs)

			- required/unnecessary combination components
				- condition-function-intent interaction
					- conditional work outside of context (conditions like validation checks applied where not needed)
				- node-middleman-node interaction

		- object: optimization opportunity

			- optimization opportunity (a trajectory between nodes that increases a resource/cost ratio)
				- alternate functions with an intent in common with varying speed in input cases that dont occur in this system

		- object: scope

			- efficiencies can be local to agents or interactions rather than system-wide
				
	- iterate through objects & combinations
		- does system object combination 'resource A + function B for intent C' match the efficiency definition 'high benefit/cost ratio' in its structural version 'high resource output compared to work input'?
			- does it have an optimization opportunity (does it match an inefficiency structural definition)?
				- if so, how could that inefficiency be converted to an inefficiency?
					- apply all mechanisms to reduce work units that could result in higher resource outputs, such as:
						- 'removing middlemen (unnecessary nodes/functions for an intent)'
						- 'removing unnecessary inputs/outputs that create costs'
						- 'calling conditional functions as needed (when the condition occurs) rather than every time'
						- 'removing interactions that dont change outputs'
						- 'removing ambiguities that dont add necessary variation'

- example output:

	- applying insight path from efficiency definition:

		- iterate through attributes/functions/objects, checking for required/unnecessary components & other structures associated with the target object definition to identify

		- 'A communicates info to B'
			- does this communication contain unnecessary info?

		- 'B converts info to a format that is interpretable by C, D, & E'
			- is this conversion function necessary?
			- can this conversion function be done by A, or automatically?
			- can C, D, & E learn to interpret the original format?

		- 'B sends the info to C, D, & E'
			- does B send the info in one message or separately, and is there a need for separate messages or can they be condensed?

	- example efficiency opportunities:
		- if the conversion function is not required to be executed by B, the middleman node B can be removed, and the conversion function can be taught/distributed to receivers/senders or automated
		- if the messages dont need to be sent separately each to C, D, & E, the messages can be condensed into one message
		- if the messages dont need to be sent at all, but can be left in a place that C, D, & E go regularly, the 'send' function can be replaced with a 'leave in position' function

'''
''' poc system object identification:

- import system as network

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

	- identify relevant objects in the system
		- units of work that result in higher or similar resources after the units of work
		- intents that have a high association with high resource/work ratio
		- resources that enable a high ratio of work units (resources that are an input to many functions)

	- identify relevant combinations in the system
		- does system object combination 'resource A + function B for intent C' match the efficiency definition 'high benefit/cost ratio' in its structural version 'high resource output compared to work input'?
			- does it have an optimization opportunity (does it match an inefficiency structural definition)?
				- if so, how could that inefficiency be converted to an inefficiency?
					- apply all mechanisms to reduce work units that could result in higher resource outputs, such as:
						- 'removing middlemen (unnecessary nodes/functions for an intent)'
						- 'removing unnecessary inputs/outputs that create costs'
						- 'calling conditional functions as needed (when the condition occurs) rather than every time'
						- 'removing interactions that dont change outputs'
						- 'removing ambiguities that dont add necessary variation'
'''
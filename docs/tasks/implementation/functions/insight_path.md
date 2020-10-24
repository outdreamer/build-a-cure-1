# Insight path


	- example

	  - finding which combinations of objects produce the most important errors to avoid (such as intent misalignment or minimizing risk to important objects/functions)

	  	- for example, if a button triggers a weapons, how do you identify which errors are important to minimize 
	  		(programmatically, if your program has no insights like 'avoid accidental button pushes' stored in its rule set)

	  		- there are many different definition routes of an error like 'accidental button push', such as:
			  	- unintentional event (assume everything can be unintentional - meaning 'having no intent stack')
			  	- false assumption (assumption that 'every button push is intentional')
			  	- intent mismatch (agent intent to 'protect agent against structural damage' and weapon intent to 'cause structural damage' dont align)
			  	- illusory intent ('intent to move' can look like 'intent to push button')
			
			- how would you identify an 'accidental button push' as an important error to avoid programmatically:

				- one route is:
					- query for 'important' definition ('lack of it puts metrics of potential (like life) at risk')
					- query for 'accident' definition ('unintended side effect')
					- query agent intents (like 'protecting agent from structural damage')
					- identify all the types of that agent intent (structural damage to the agent: boundary damage, frame damage, scale-specific damage, etc)
					- check if the weapon has any objects/functions/attributes that can exert that agent intent type (switching it on)
					- check if there is any benefit to that event interfering with the agent intent (does it fulfill a more important agent intent)
					- if not, its an error type

				- now we've found an important error type to avoid ('accidental trigger of the button push', which is important bc it puts the agent's intent to protect themselves from structural damage at risk)
				- a solution route for that error type is:

					- if so, query for all the direct events that can trigger those objects/functions/attributes (push button)
					- query for any agent intents that would trigger a direct event or execute the direct event
						- direct intents like 'moving weapon'
						- indirect intents like 'having a defensive reaction while holding weapon'
					- check if there's a way to prevent those agent intents in the weapon design 
						- adding validation checks (automating rules like 'button must be pushed multiple times')
						- analyzing intent before execution (is intent implied by metadata of event, like number of button pushes)
					- check if the functionality triggered is necessary to the weapon intents 

			- this is an insight path to solve a problem like 'design a tool optimally the first time rather than after creating errors'

			- another example is the thermometer design path in the readme, which uses an insight path including 'attribute alignment'

	  - so its clear how to apply definition routes & common transforms to build a path between problem space & a solution

	  - how would you identify the right objects to check for to filter the solution space, such as 'invalidating rules' or 'counter examples' or 'benefits of an error'

	  - in the case of checking for 'benefits of an error', you have insights like:
	  	- there are very few absolute rules
	  	- if youre about to apply an absolute rule, dont apply it automatically (dont hard code it or set it as default)
	  	- to tell if a rule is absolute, check for coutnerexamples where it might not apply or be optimal

	  - if you didnt have those insights, how could you derive that checking for objects like 'benefits of an error' is important before executing rule to 'automate a rule to prevent that error'?

	  	- you could derive the above three insights, and order them to create an insight path

	  	- you could implement 'cost-benefit analysis' or 'automate as few rules as possible' or 'dont assume' or 'dont generalize without good support from data' as an absolute filter before automating any rule

	  	- you could store insights about other errors that have some usefulness & query for those insights instead (an alternate insight path to the three-insight path above)

	  	- you could query for core objects (including info objects like 'counterpoint' or 'counter-example') and check if they're relevant (a counter-example would be good to avoid automating the wrong rule)

	  	- you could query for problem type objects (info asymmetry or mismatch, like the mismatch between a rule about to get automated & the assumption that the rule applies to an absolute scope) and check for each problem type when its structure is applied to the problem space

	  	- you could query for common patterns (like an anomaly) and check if those patterns interfere with the automation of the error-preventing rule


      - example of deriving which object combinations are useful given the full set & definition alignment

          operations = ['find', 'get', 'update', 'apply', 'build', 'combine', 'connect', 'convert', 'balance', 'map', 'match', 'fit', 'filter', 'derive']
          objects = ['strategies', 'questions', 'incentives', 'efficiencies', 'metadata', 'definitions']
          structures = ['paths', 'limits', 'boundaries', 'bonds', 'gaps', 'layers']
          system_objects = ['attributes', 'objects', 'systems', 'sub_systems', 'types', 'functions']

        - example: how would you determine that problem & solution are complementary objects that provide a useful relationship in the set of combinations of objects in the above list
          - problem definition: one object in the set of (conflict, mismatch, ambiguity)
          - solution definition: one object in the set of (conflict/ambiguity resolution, mismatch/imbalance correction)
          - aside from the common terms, you can determine their useful relationship from the definition of 'resolution' or 'correction':
            - resolution definition: 
                - structural definition: clarifying an ambiguity
                - alternate specific definition: decomposing a problem
            - correction definition:
                - structural definition: restoring an original attribute used as a metric of success, such as direction
            - both 'resolution' and 'correction' involve reducing a metric (either by adding information or using definition of success/intent & applying it)
            - a problem normally interacts with agents, specifically by interfering with their intents
            - agents intend to reduce problems
            - 'reducing a metric' could be applied to the 'problem' object as 'reducing number of problems or inputs causing a problem'
            - so we can see why 'reducing a problem' would be useful in the sense of adding efficiency to agents' work toward their intents
            - we can also tell that it could be useful bc it involves a common interaction type like 'reduce' on core objects (problem, solution)
            - so matching problems & solutions is an important relationship in the full set of combinations of core objects above

        - generalized insight path of above:

          - find definition routes of objects
          - isolated interaction types between definition routes of one object ('resolution' or 'correction'), removing references to the other (which is trivial to compute)
            - find definition routes of isolated interaction types (resolution, correction)
            - find common objects/functions/attributes of isolated interaction type definition routes (solutions add information to information asymmetries & ambiguities, solutions align direction to resolve conflicts)
            - translate common objects to core objects (solutions reduce metrics of problems & problems)
            - check for agent interactions with original objects/functions (problems interfere with agent intents, agents sometimes have intent to 'reduce problems')
            - get definition of 'useful' (optimizing/increasing a success metric)
            - check if those core objects/functions are useful to agents (solutions are useful when agents have intent to 'reduce problems')
            - apply core definition (solution defined as 'reducing a metric') to check if it is useful to agents when applied to the other object (problem) - 'reducing a problem' is useful for agent intents when they encounter problems
            - output agent intents fulfilled by useful object combination (matching solution with problem by 'reducing problem metric or problem' is useful for agents with intent to 'reduce problems')
            - add rules specific to insight path if successful at finding useful combination (solution definition was adjacent to 'reduce' core functions, so store 'rules that are adjacent to core functions are likelier to be useful' as an insight)


	  - insight path to find out that the error is the goal in a curiosity algorithm, where the primary intent is 'maximize learning', defined by 'maximum number of new rules added to rule set'
	    - curiosity definition is 'finding new things and how they work'
	    - 'finding out how they work' can be reduced to 'derive' function
	    - a related term to 'derive' is 'learn'
	    - example of learning in an agent space occurs when 'new information doesnt match existing information'
	    - definition of error is 'when measured information doesnt match predicted information'
	    - 'new information not matching existing information' can be classified as an error, if 'new information' is replaced by 'measured information' and 'existing information' replaces 'predicted information' (predicted by existing rule sets)
	    - so 'maximized error' is the goal as a proxy for 'maximized learning'

	  - other routes to automate solving the problem (of 'which objects/functions/attributes should be maximized in order to maximize learning')
	    - an insight path that derives that differences/mismatches/imbalances/asymmetries are associated with learning (rather than just errors) & maximizes those
	    - an insight path that derives the full set of likely combinations in a space (like the full set of species combinations) and aims at the most different combination to maximize learning

	  - the above is a specific insight route composed of insights - generalizable to the insight path:
	    - lookup definition of algorithm type (curiosity), given that the algorithm type includes associated intents
	    - decrypt definition to core functions/objects/attributes
	    - find related terms to core function terms that are relevant to the problem space (learning is a relevant term to machine learning algorithms that automate finding/discovering/predicting) in order to take advantage of related term definitions as a method of finding objects/functions to automate the solution, given that related terms provide alternate routes/interpretations of a process
	    - translate the related term to the problem space (make it relevant to agents & information)
	    - find related terms that match the relevant related term definition (definition of error, definition of surprise, definition of change)
	    - classify related term (learn) as the most similar relevant related term (error)
	    - replace term in target intent with relevant related term (target of a curiosity algorithm is to maximize learning/error)

	- with a path relating three objects (a, b, c):
		a    b   c
		   \
		a(x) b   c
			   /
		a(x) b   c (2X)

		- each operation function has a 'reason' such as a 'need' or 'intent': 
			- "a needs an x & b has a function y which outputs an x, so a does y on b to get x"
			- "c needs its property X to be larger so combine with b, which also has property X, where the combine operation is cooperative & doesnt take X away from b"
	- the insight path can be represented as:
		- a set of functions/patterns operating on objects/types
		- where insight components are replaceable with:
			- object metadata:
					- dependencies
					- attributes
					- type_stack
					- alternatives/approximations/antagonists
					- input_variables/output_variables
					- intents/functions/core_functions
				- where dependencies are:
					- source/target objects (receive input from, give output to) 
					- hierarchical objects (objects that generate & objects generated by)
			- an approximation of any of the above
			- a combination of any of the above (operations + inputs, operation function types + input source objects)
			- a generator function to create a random example of an object or object metadata, restricted by params:
				generate(object(type="person"))
				generate(object(type="function", attributes="no(side_effects)", inputs="dataset", outputs="correlations"))
				generate(object(variance=[3x5])), where 3 is the number of variables and 5 is the sum of their variance scores, 5 being the largest
				generate(metadata(type_stack=['species', 'canine', 'chihuahua']))
			

	- Example: 

		A specific rule set representing a simplistic system in a problem space, mimicking the above rule set:

			doctor    					 			patient   					drug

			  				ask

			doctor(patient.symptom_info) 			patient   					drug

				   												drug.molecule.share_electron(patient.component="bloodstream".molecule(attribute.bond="covalent").electrons)

			doctor(patient.symptom_info) 			patient   					drug.molecule.electrons(2e)

		1. "the doctor asks the patient to get the symptom info"
		2. "the drug needs an electron to work so it shares one with a molecule the patient's system produces"

		The insights that are stored in an insight path would include:
			- "doctor ask patient to get info" (get_types, None, get_types, None, get_types) # no operations done on functions, just objects
			- "x ask y to get info" (get_vars, None, get_vars, None, get_types)
			- "person ask person to get symptoms" 
				(a doctor type is person, a patient type is person, an info type is symptoms - for situations where a doctor isnt present)
			- "machine ask person to get info" (person alternative is machine)
			- "x ask y to do function get(implement, data, type)" 
				(function get(implement, data, type) is a function that gets information from data that fits the type)
			- "x ask y to do core_functions(find, match, implement, query, fit, equals)" 
				((find, match, implement, query, fit, equals) are the core functions necessary to build get()
			- "doctor ask assistant to get info"
				("assistant" is a source dependency of "patient" bc the patient becomes relevant to the doctor bc of the "assistant")
			- "machine ask patient to get info"
				("machine" is a target dependency of "doctor" bc the doctor enters the info into the machine)
				- note we can get to this insight by various paths, 
					as reflected in "machine ask person to get info" above, which varies only by type(patient) = person
					which we got to using the types of all objects, then using the alternative of a person (machine)
			- and so on until youve covered all the patterns producible from the dependencies, attributes, types, alternative vars, functions, core functions

		Youd ideally store each insight with the functions used to generate it, in the same order as objects & functions in the rule:
			functions = [get_types, None, get_types, None, get_types]
		in case you want to try to derive the original rule from the insight & its generating functions.

		The insight path itself would be:

			- any combination of these insights that fits into the 3-step rule set above
			- any combination of these insights that fits into a subset, transform, combination, alternative, or approximation of the 3-step rule set above
				- this is bc the rule set can be modified by operations inherent to the rule set to derive other insights, 
				  without logically violating the objects' & functions' rules
				- these inherent operations include:
					- core_functions & functions of rules in the set
					- standard abstract operations (get_type, get_example)
					- conceptual abstract operations, like merge(intent1, intent2):
						def merge(a,b):
							if a.prop.intent == (-1 * b.prop.intent):
								merge_operation.conflicts.add('opposite_intent', a.prop.intent, b.prop.intent)
								# check if this conflict neutralizes a function of either object

			- it might seem best to store an insight path only if its logically consistent 
			  & doesnt violate standard & conceptual operations that hold in the original rule set,
			  but if its abstracted at all, other rules can apply:
			  - when you change "doctor" to "x", then personal interaction rules dont apply because x could be a machine

			- however there are filters that apply for:

				- an insight:
					- it must explain the rule interaction accurately

				- an insight to be part of an insight path:
					- it must contribute to the explanation of how an origin object of a possible route in the rule set gets to its target object
						- for trees, the routes go in one direction, so it's a clear matter of:
						  "explain how the top node gets to the bottom node, which this insight interacts with"
						- for other structures like networks, it may be a more complex route from start to finish of any given path in the network

				- ideally each insight would contribute more than other insights considered, 
					so there should be a "best-fit" insight path composed of the "best-fitting" insights,
					as well as a stack of other explanatory insight paths,
					such as an "abstract" insight path composed entirely of abstract insights,
					containing no specific information except core-function versions of objects & functions, 
					for example the abstract core-function decomposition of "machine" may be any of these depending on context like intent:
					  	- information-storage unit (intent="store")
					  	- operation-executor unit (intent="run_tasks")
					  	- experience unit (intent="entertainment")
					  	- communication unit (intent="interact")
					so the insights containing "machine" would be considered abstract if they had this replacement done

				- the full stack of insight paths can include:
					- an abstract insight path
					- a best-fit insight path
					- a most-efficient insight path
					- a most-reusable insight path (has objects in common with many other systems)

		Then you could apply the generated insight paths from a rule set to a new system's rule set with similar dynamics, 
			as determined by the number of matching insights in the new rule set.

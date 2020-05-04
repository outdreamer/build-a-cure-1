#functions = get_data('system_analysis/maps/functions.json')
#structures = get_data('system_analysis/maps/structures.json')
core_functions = [
    "find",
    "move",
    "embed",
    "filter",
    "build",
    "wrap",
    "change",
    "connect",
    "separate",
    "aim",
    "align",
    "compare",
    "compete",
    "combine",
    "share",
    "activate", 
    "store",
    "return",
    "remove",
    "compress",
    "chain",
    "stack",
    "split"
]
core_attributes = ['dependency', 'importance', 'position']
core_objects = ['function', 'attribute']
function_pairs = set()
object_pairs = set()
attribute_pairs = set()
mixed_pairs = set()
mixed_function_object_pairs = set()
mixed_function_attribute_pairs = set()
mixed_attribute_object_pairs = set()

new_cf_copy = [item for item in core_functions]
new_co_copy = [item for item in core_objects]
new_ca_copy = [item for item in core_attributes]
combinations = itertools.product(core_objects, core_objects)
for cl in combinations:
	object_pairs.add(' '.join(cl))

combinations = itertools.product(core_functions, core_functions)
for cl in combinations:
	function_pairs.add(' '.join(cl))

combinations = itertools.product(core_attributes, core_attributes)
for cl in combinations:
	attribute_pairs.add(' '.join(cl))

''' functions, attributes '''

fa_copy = core_functions
fa_copy.extend(core_attributes)
combinations = itertools.product(fa_copy, fa_copy)

print('new_cf_copy', new_cf_copy)
for cl in combinations:
	ff = [item for item in cl if item in new_cf_copy]
	atf = [item for item in cl if item not in new_cf_copy]
	if len(ff) == 1 and len(atf) == 1:
		mixed_function_attribute_pairs.add(' '.join(cl))

''' attributes, objects '''
ao_copy = core_attributes
ao_copy.extend(core_objects)
combinations = itertools.product(ao_copy, ao_copy)
for cl in combinations:
	of = [item for item in cl if item in new_co_copy]
	af = [item for item in cl if item not in new_co_copy]
	if len(of) == 1 and len(af) == 1:
		mixed_attribute_object_pairs.add(' '.join(cl))

''' functions, objects '''
fo_copy = core_functions
fo_copy.extend(core_objects)
combinations = itertools.product(fo_copy, fo_copy)
for cl in combinations:
	functions_found = [item for item in cl if item in new_cf_copy]
	objects_found = [item for item in cl if item not in new_cf_copy]
	if len(functions_found) == 1 and len(objects_found) == 1:
		mixed_function_object_pairs.add(' '.join(cl))

all_pairs = [item for item in core_functions]
all_pairs.extend(new_co_copy)
all_pairs.extend(new_ca_copy)

combinations = itertools.product(all_pairs, all_pairs)
for cl in combinations:
	mixed_pairs.add(' '.join(cl))

print('\nobject_pairs', object_pairs)
print('\nfunction_pairs', function_pairs)
print('\nattribute_pairs', attribute_pairs)

print('\nmixed_pairs', mixed_pairs)
print('\nmixed_function_attribute_pairs', mixed_function_attribute_pairs)
print('\nmixed_attribute_object_pairs', mixed_attribute_object_pairs)
print('\nmixed_function_object_pairs', mixed_function_object_pairs)

'''
	- in this layer you should have common objects like 'variable' ('attribute change' meaning an attribute with a change function) and 'type' ('attribute combine' meaning an attribute set)
	now we can filter the list to identify certain objects that are more useful

	- iterated versions included more sophisticated objects like:
	'variable' ('attribute change apply' meaning an attribute with a change function that can be applied to it)
	'variable version' ('attribute value change' meaning a change to the attribute value)
	'variable state' ('attribute change position' meaning a specific version of the attribute value)

	this is how we can produce definition routes to an object

	- interpretations of combinations

		- chain of attributes:

			- 'position position'

				- embedding: 'a position of a position'

				- type: 'a position type of position'


		- chain of functions:

			- 'change change':

				- injection: a change applied to a change/a direction to apply a change to a change
				- sequential: change the first way, then change the second way
				- type: an unexpected value in a change, all relevant changes, or the definition of change (a change type added)

				- this function combination could be used to assess change rates, change types, or change ratios
				
			- 'share embed'

				- sequential: share, then embed
				- injection: share the embedding, embed the share
				
				- you could use this function combination for more sophisticated functions like 'deploy' or 'distribute'


		- chain of objects:

			- standard definitions:

				- function attribute:
					- an attribute of a function

				- function function
					- a function that applies to, can be activated by, or can generate a function

				- attribute attribute
					- an attribute that describes an attribute (attribute metadata)

				- attribute function
					- a function that generates or describes an attribute

		- these involve:
			- embedding one object in the other (an attribute of a function means an attribute contained in the function object)
			- applying one object to the other
			- causing/depending on the other
			- one following the other in a sequence
			- one acting as a function on the other, by qualifying/modifying the other ('a change change' = 'a change type of change')

	- mixed combination of functions/objects/attributes 

		- attribute function

			- 'dependency change':
				- injection: a change applied to the dependency or one of its components
				- type: a change applied to all dependencies or the definition of dependencies
				- sequential: change the dependency attribute (to something else) 
					- which, given its definition, could mean a reversal of cause (a related object of dependencies), or a type change (to another attribute or converting it to a function)

		- function attribute object 

			- 'change position tree' could refer to:
				- an object: 'a tree storing change positions'
				- a function: 'change the position tree'
				- an attribute: 'a tree attribute of the change position object'


	- how could you identify useful objects like a pattern intersection, an unenforced rule, or an attribute alignment, once you generate the set of n-degree combinations of core components (in mixed_pairs)?

	- an 'unenforced rule' is an 'attribute object' and would have the definition combinations:

		- 'subset rule' (a partially implemented rule)
		- 'function without limit' or 'function without filter' (a rule without validation)
		- 'intent condition mismatch' (a function whose intent doesnt match the conditions in it)

	- how would you identify that object of an unenforced rule as a particularly important one, even if you didnt know that it was causing errors?

		- first you would try to identify which structures of the 'subset rule' are valid

			- valid in this context means "what is 'subset rule' referring to" - a partially implemented rule, or a subset of the complete rule

			- system analysis questions about the generated 'subset rule' object:

				- intent: what are subsets used for?

					- does this fall in one of those categories (find, separate, identify)

						- find:
							- given that the 'find' intent could be applied to errors (a related function object), is there an error in the subset

						- identify:
							- is there something unique about the subset

						- separate:
							- should the subset not interact with the other subset 
							- is the other subset supposed to be derived from this subset
							- what information is lost if the other subset is not stored or derived

					- is it premature to store a subset object separately, without something to find/identify in the set, or a reason to separate the subsets

					- is the other subset automatically stored or is it lost

				- change: how are subsets usually changed?

					- would this ever be restored to the full set
					- are there rules to ensure that will happen

				- definition: is a subset of a rule just another rule set?

					- is there a reason to make a distinction between the subset and the rule


		- the output of that analysis should include: 'partially implemented function' or 'function with errors' or 'function missing validation'

		- iterate through the different structures of 'subset rule'

		- then identify the intent of the target output (function)

			- you build a function to automate a process, to reduce non-natural (manmade) errors

		- then youd identify how a 'subset rule' structured as a 'partially implemented function' could happen

			- lack of resources to implement the full rule set to complete a function

		- then youd identify the causes of those ways it could occur

			- lack of planning/organization (adjacent to lack of bias, or randomness)

		- 'injecting randomness into an ordered system' is associated with objects like experiments

		- if the enabled intent of 'subset rule' structure 'partially implemented function' (enabled intent meaning 'function building') is not randomness, there is a mismatch between the objects/attributes of:
			- the 'subset rule' object cause (lack of planning - randomness) 
			- the enabled 'function building' intent (organized ordered processes)

		- a mismatch could be important bc its a common problem type, especially if 'lack of planning' or 'randomness' is a common occurrences 
			(which we'd know if we derived where randomness could occur given its definition)

		- if you already had 'attribute alignment' as a pattern to look for, or 'intent mismatch' or 'direction conflict' as a specific problem type to identify, you could identify that 
			a mismatch between randomness injected in an ordered system and the intent of ordering a system was an indicator of the importance of the core object combination

		- you could also use insights like 'subsets of a system should be similar to the system' 
			(so the metadata of system components (intent to disorder a system) should be similar to the metadata of the system (intent to order a system))

		- as a backup, you could identify that the randomness invalidates the object intent, which seems like an indicator that it shouldn't happen

		- edge case: if your function is to generate randomness, this process would have to examine other metadata, to find that:
			- a partially implemented randomness function (with errors) doesnt generate the target randomness type (evenly distributed output probabilities)


	- the general overview of this method to filter the most important objects in core object combinations is:

		- derive metadata of the core object combination (subset rule) with system analysis
		- find & iterate through structures of core object combination intents (structure in which it would be found, like 'partially implemented function')
		- find & iterate through metadata of structures
			- target intents like 'function-building' have intents like 'reducing manmade error')
			- causes like 'lack of organization'
		- pull any related definitions (randomness definition)
		- iterate through problem types like mismatch, and iterate through metadata of the objects, looking for inconsistencies, assuming that the structure is intentional 
			(youd intentionally implement a 'partially implemented function' in order to do what intents - to 'inject randomness in an ordered system'?
		- check if each problem type instance found is useful in some way (does it generate randomness, and is that the intent of the function?)
		- if not, and if this is an important problem type to avoid, the object 'subset rule' is probably an important specific instance of that problem type 
			('function missing validation', or an 'unenforced rule')


	- this analysis can be used to derive the full set of attributes (relevance, connectedness, variation, etc) and concepts (equivalence)


	- example of deriving attribute:

		- core component combinations like 'distance between nodes' or 'number of connections between nodes' would be output by the above combinations if you included the full set of core structures & other components

	- example of deriving concept:

		- once you have patterns with multiple attributes in common, you know there is a possibility that a new concept is identifiable

		- identifying two attributes with similar or equal values and identifying two functions with similar or equal routes would alert you to the possibility that this pattern is a concept

		- how would you derive the concept of equal from 'similar' (meaning 'similar in value' or 'adjacent in distance')

			- 'similar in value' has a point where the two objects are the same, not requiring qualification of their similarity - its the unit case in a comparison problem space
				- to get there you'd need to permute the two objects or apply the concept of balance to them if they start out as unequal

			- 'adjacent in distance' has a point where the two objects occupy the same position, overlap, or merge depending on potential for occupying a point, 
				which is also the unit case in the graphing problem space, related to the comparison problem space
				- to get there you could change their positions until they were the same, identifying the boundary between the unit case and the next 'not equal' or 'adjacent' case

			- the fact that this attribute describes two different systems (differing in number of dimensions or structures applied) implies its an abstract concept 

			- the more different the systems described by the attribute, the more abstract the concept that the attribute is an implementation of

			- to get from similar/adjacent to equivalence, which is a network of different types of equal, you could add permutations like the point (structure) differs from the value (number)

			- example permutations:
				- adding a dimension
				- converting to a different space
				- change an attribute value beyond a phase shift

			- the full set of equivalence definitions includes definitions on different interfaces, like:
				"structure": ["conditionally interchangeable", "absolutely interchangeable", "approximately interchangeable", "minimally distant", "efficiently convertable"]

			- these definition routes can be derived with core component combinations & permutations like applying filters (conditions), intents (approximate), or attribute modifiers (efficient)

'''

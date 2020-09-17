'''

- standard operations

## Match

- fit

## Find

- filter (rule, gap)

- find(target, data, filters): 
	- find target type & data type, get relationships between them ('this type is often found at end of document'), apply filters to output


## Apply/Change

- transform/rule

- apply(concepts, source_functions, target_function, problem_space):
	- takes concepts or source_functions & assigns them to structures known to interact in that problem space to achieve that function
	- in the absence of concepts or source_functions, it pulls those objects from the problem_space definition
	- example:
		- apply(['power', 'balance'], [], 'decentralize', 'government') should return an insight: 'give components of government power over each other'
		- apply([], [], ['give components of government power over each other'], 'government') should return:
			- a set of insights about the existing & optimal power distribution rules between government agencies:
				- 'technology-progressive agencies may have more power in the form of information' (tech power must be distributed or otherwise limited)
				- 'information should be distributed by need' (agencies with more information like intel agencies will have more power)
				- 'legislative power should be distributed by relevance, intent, & ability' (women should make laws for women, etc)
				- 'veto power should be by consensus weighted by demonstrated ability' (no one person should get to make important decisions)
				- 'enforcement should not be biased' (enforcers would otherwise have endless power)
				- 'enforcement should be automated' (automaters will have more power which must be limited)
				- 'enforcement should be a backup method to prevention' (agencies that do prevention should work with agencies that automate enforcement)
		- apply([], ['max', 'count', 'split'], 'find_biggest_number_in_string', 'programming') should return a function: "max([x for x in input.split('') if int(x)])"
		- apply([], insight, 'strategy', problem_space) would apply that insight to the problem space, 
			converting it into a usable strategy with an intent 
			(agent & possible intents would be part of the problem space object)


## Generate

- generate(type, input_ranges, output_distribution):
	- gets structures of subtypes within that type
	- applies input_ranges (limits of variables) to generate the set of type examples with output_distribution


## Derive

- derive(target_objects, problem_space): 
	- fetches patterns & functions of the problem space
	- applies them layer by layer (from abstract like apply_filter() to concrete like count()) to derive relationship between objects in target_objects
	- if no results, applies system analysis to find gaps in change & functionality explanations & filters this list by target_objects


- examples

	- interface operations examples

      - apply an interface as a standard to another interface:
          - intent / structure interface: assess intent interface by a standard of structure interface (which structures can simplify the intent interface)
      
          - concept-structure traversal (a multi-interface traversal linking the concept & structure interfaces, so a target concept combination/set/path or target structural attribute can be achieved with a combination of filters & limits or functions applied to adjust the structure until it matches the target structural attributes or concepts) 
            - general: - find a structure for a certain intent that matches a conceptual priority (like relevance, organization, robustness, equivalence, or trust) - modify a structure with a certain intent so it matches a conceptual priority (like power or a conceptual structure like power distribution) 
            - specific: - find a structure in the finance space that minimizes trust in transactions - modify a multiplication method to find a method minimizing larger calculations 
          
          - structure-math interface mapping 
            - general: use a multi-interface traversal to map problem structures to math objects to apply math insights to problem structures 
            - specific: if the problem is 'predict the shape of the boundary of an even distribution of change across directions from the same origin' (for problems like 'finding a container needed for an experiment growing microorganisms given the requirement of the same origin and non-overlapping paths', or 'predicting the threshold marker needed for comparing speed metrics'), apply the 'circle' definition route using the 'evenly distributed outward motion' route to infer that the boundary could be circular, with variable advantages depending on problem metadata 
          
          - a question-answer interface traversal 
            - general: frame a question as missing information structured as a source position and a target position on a network, and the answer as the most robust path, the most relevant path for a particular intent & objects related to it, the path that moves the nearest to the target position, or the quickest path that moves in the prioritized direction on the network 
            - specific: - frame a question like 'how to build a filter' as an optimal path-finding problem on the network between some undefined starting component set & the destination filter object - frame a question like 'why would you build a filter' as a adjacent object- finding problem to find objects that can be produced if the filter is the starting point (input) or to find intent directions moved in when you follows paths to build the filter (reasons to build it) or subsequent paths using the filter (other applications of the filter) 
  
      - merge interfaces:
          - function + pattern interface: merge networks of functions & patterns into one standard interface definition (input/output/logic + metadata of both objects)
      
      - expand an interface by another interface:

          - function * pattern interface: 
            function patterns (what patterns are there in functions), pattern functions (what functions generate patterns)
            function pattern functions (what functions generate function patterns), pattern function patterns (what patterns are there in functions that generate patterns)
          - cause * type interface: 
            causal type interface (what types of cause are there), type cause interface (what causes types)
            causal type cause (what causes causal types), type cause type (what types of type causes are there)

      - combine interfaces: 
        - combining the pattern & intent interface with combination type 'group' would produce patterns grouped with intents 
        - combining the pattern & intent interface with combination type 'merge' would produce merged objects containing attributes common to both patterns & intents 
          - function to merge interfaces: 
            - function + pattern interface: merge networks of functions & patterns into one standard interface definition (input/output/logic + metadata of both objects) 
        - combining the pattern & intent interface with combination type 'unify' would produce unified objects like intents distorted by patterns  
      - inject interfaces: 
        - injecting the pattern interface in the intent interface would produce: 
          - intent examples & abstractions (applying the definition of 'pattern' to include specific & abstract patterns) 
      - apply interfaces  
        - applying the pattern interface to the intent interface with would produce intent patterns, intent component patterns (intent function patterns), intent interface related object patterns, etc  
        - function to apply an interface to another interface: 
          - intent / structure interface: assess intent interface by a standard of structure interface (which structures can simplify the intent interface)
        - function to expand an interface by another interface: 
          - function * pattern interface:  
            function patterns (what patterns are there in functions), pattern functions (what functions generate patterns) 
            function pattern functions (what functions generate function patterns), pattern function patterns (what patterns are there in functions that generate patterns) 
          - cause * type interface:  
            causal type interface (what types of cause are there), type cause interface (what causes types) 
            causal type cause (what causes causal types), type cause type (what types of type causes are there) 

    - concept operations examples

          I. combine (expand, add, set)

            1. merge with override/backup/overlap rules
              "power merged with information" => 
                "power as an input to information" => "powerful position can use information at increased scale & impact"
                "information as an input to power" => "insights"
                (can continue merging with each object interacting with the other & its attributes/types/rules)

            2. collide (compete for position)
              "power or information" => "is power different from information in this context" => "do other objects enable functionality, beyond information, or is information the key enabler"

            3. intersection (retain common components)
              "common components of power & information" => "enablement, context, control, dependence, responsibility"

            4. union (retain all components)
              "power and information" => "multiple power types, creating a backup system of control if one power source fails"

          II. filter (find, reduce, subtract, subset)

            - x without y
              - "power without information" => "information-derivation method", "power from non-information source", "limited power"

          III. apply (expand, group, iterate, multiply, set)

            - apply to another (x * y)
              - "balance of power" = "symmetry between input & output dependencies"

            - apply to itself (x ^ n)
              - "power of power" => "the enabler of enabling" => "input", "abstraction", "coordination"

          IV. standardize (simplify, compare, divide, subset)

            - x standardized by y
              - "power standardized by power" => 
                "power explained by power" => 
                "explain power using only objects in power definition (input/output/objects)" =>
                "enabling happens from providing inputs to a high proportion of other objects or to very important objects (having important, causative, or many connections)" => 
                "high ratio or symmetry of power object outputs: important object inputs or high causation ratio" 
                  (given that important objects can be powerful just because they enable many other objects, even if they dont provide all of the inputs of other objects)

'''
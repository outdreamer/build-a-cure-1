# Functions

## Function interface

  - rule: static function
  - function: rule tree, composed of:
    - conditions (if/for/while/validation/organization)
    - assignments/relationships (equate an attribute with a value)
    - processes (format/return)
  - operation: sub-function or function step
  - intent: purpose for a function (at granular layers or in strict environments, purpose can be tightly aligned with the function logic, with no side effects)
  - role: function & a position in a system
  - pattern: sequence of specific/identified objects
  - connection: causal relationship (some type of interaction occurs)
  - insight: important/relevant/new/unique/abstract/cross-system relationship
  - strategy: insight & a plan intent on how to implement it, usually to achieve a specific goal intent


## Functions Types

    - core functions

        - build
          - copy/replace/remove
          - combine
            - group
            - merge
            - connect/bind
                - communication
                - mark/identify/recognize
                - find path
                - find map (common language)
          - boundary
          - fit/fill
          - match
              - request/response handling
          - position
            - move
            - rearrange
            - distribution
            - order

        - change
          - change prevention (regulation)
            - testing/assessment/metric selection
            - repair
          - change variable metadata (type/value)
          - change process/variable status (activate)
          - convert/translate/format
          - change reversal/compounding
          - differentiation (commitment to a state from a core state)


    - core structure function definitions

      - connect
        - concepts
        - functions

      - limit
        - concepts
        - functions

      - change
        - concepts
        - functions

      - combine
        - concepts:
          - anomaly/counterexample/outlier
          - conflict
          - symmetry
          - common shape (circle)
        - functions:
          - neutralizing/opposing
          - promoting/synergistic
          - core structure combinations

      - distribute
        - concepts:
          - network
        - functions:

      - filter
        - concepts:
          - network
        - functions:

      - organize
        - concepts:
          - filters
          - position
          - adjacence
        - functions:
          - info rules (storage/compression)
          - specific structural core intent rules (combine/connect/filtering/boundary)


    - emergent/interaction layer functions

        - learning (built by change function)
        - competition (built by change/find/test functions)
        - finding/borrowing/generating functionality & other resources (built by find/build functions)

    - sub-system functions

    - interim functions
        - provide resources used as inputs to activate other functions (a set of molecules that when detached can activate other processes)
        - these functions may be cross-system, or may be unnecessary middlemen in a function chain whose functionality should be merged with other functions
      
    - platform functions
        - provide platform for functionality (variance allowing functionality to develop on foundational structures)

    - intent functions
      - direct/indirect intent
      - multiple/single intents
      - certain/uncertain intent
      - abstract/neutral/specific intent
      - intent-related intents (intent-modification intent)

    - attribute-based relationship types
        - explicit (such as 'convert input energy into output structure')
        - implicit (such as unintended side effects of outputs, interim functions between input/output, and unpredicted emergent functions at scale or across many linked integrated function chains)
     

## Match

- fit

## Find

- filter (rule, gap)

- find(target, data, filters): 
	- find target type & data type, get relationships between them ('this type is often found at end of document'), apply filters to output


## Apply

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


## Core Concept Operations

  - this is the set of core conceptual math operations between concepts

  - core function + core object -> interaction rule of core attributes that aligns with core function + core object priority
  - depict core functions on their own direction to indicate a dimension when graphing

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

'''
  - definition: 
    - the system interface is the structural version of the meaning interface
    - the fundamental system question 'how does info fit in a system' is relevant to the fundamental meaning question 'what structures are relevant to this intent'
    - this is a format accessible once information is standardized to object model 
    - this involves framing information as a connected network with a boundary defining the system, that has core system operations, structures, & objects 
 
    - differences from existing analysis
      - existing analysis: this is isolated analysis that involves measurements of data & data dependence
        - example: how to build a tool to measure what information is being communicated between two cell types
      - system analysis: this derives the system identity (structure) so that insights about relationships within the system (and corresponding information production) can be derived & their changes predicted on demand
        - example:
          - why would a particular cell type with x functionality & attributes need to or accidentally communicate with the other cell type
            - what is each cell type lacking that the other type could provide
            - what common intents do they have which would prompt them to cooperate, share, or trade
            - are they likelier to cooperate or compete, or be governed by neutral rules prioritizing only common priorities across most systems like specialization/distribution/efficiency/potential energy/alternatives/balance (chemistry/physics governing non-intent (accidental) interactions like collisions/merging)
            - what outputs would that communication produce & what side effects would they produce that we might be able to find in existing data
              - example:
                - if the communication results in matching a false information to a signal checker, that might trigger a process that produces measurable side effects
                - if one of the cell types is commonly found with another type that can use that false information, that may be more measurable or already measured in existing data
                - if the side effects would propagate to a measurable metric (adjacency to skin barrier might produce visible impact)
          - why would an object having these variance gaps need to interact with another object having these variance gaps
            - missing functionality/adaptabilty in original variance gaps

    - general process of system analysis
      - derive core functions/operations
      - classify these core operations
      - find all combinations of these operations that follow patterns of normal interaction & variance (variables like position, compounding ratio, associativity, etc)
      - filter combinations by which are absolutely possible (consistent with the absolute host system), 
        down to the conditionally possible (consistent, within certain conditions/states of the system)
      - derive the system limits
      - filter combinations by which comply with system limits (inflection points, convergence/divergence points)
      - derive change rules
      - filter combinations by which comply with change rules & subtypes
        - for each type of change rule:
          - derive which object interactions are allowed within a constant system of identified objects, and what problems those interactions solve
      - filter combinations by which enable the most/least variance & map them on a manifold or other suitable structure indicating direction of that position/state (set of combinations) 
        toward or away from variance
      - filter combinations by applying patterns of "key derivation structure :: system structure" to tell which combinations to check first
        example: 
          - the "usual number of moves" in chess at which the game is determined is a key derivation structure in the chess system 
          - the "usual number of moves" players plan ahead is another key structure
          - the "function relating the set of possible moves & the set of optimal moves as the game progresses" 
            is another key structure to derive rules like "predict the outcome" or "predict the next move"
          - in the physics system, change rules that dont alter identities (symmetries) are a key structure (described with eigenvectors)
          - apply insights to derive factor matrixes to compute eigenvectors of original matrix:
            - https://www.quantamagazine.org/neutrinos-lead-to-unexpected-discovery-in-basic-math-20191113/
            - "break into components"
            - "isolate unique subsets of variables" (related to pca)
            - "remove the smallest number of variables at a time to minimize error"
            - "remove one variable of each type"
              - rows representing coefficients for all variables of one function
              - column representing coefficients for a particular variable across all functions
            - "variables in a function are by definition related"
            - "removing one item from a list with a known composition metric (sum or product or other dependent variable) lets you calculate the missing item"
            - "apply diagonal transform"
            - "group sub components in different way to get component"
          - vectors are like sliders/dimensions representing a spectrum or other range type - an isolated variable whose value changes across that range
          - this means you can use vectors to represent emergent variables (branches off a vector once it reaches a threshold value to activate the emergent variable)
          - eigenvectors dont change direction bc they represent change
          - degree of order, degree of change, ratio of change to threshold :: change potential (possible moves if limited, states if not)
          - different implementation of randomness, measured by system or component state (or other system object state)
          - this is a good example of how to apply a structure to implement a concept:
            apply('random', 'system_objects') should:
            - pull the definition of randomnesss
            - reduce randomness to concise insight (if not already stored in db): 
              'equal distribution of outcomes across range'
            - produce a list of all system objects & their attributes (like state) and subtypes (like change rules) that can vary
            - filter by which system objects vary equally among all possible values
            - also query for functions that would adjust the system (and its objects, their attributes & types) to maximize randomness
              - query should be formatted like the question:
                "if randomness is equal distribution of outcomes across range, how do you guarantee that in a system with other sources of randomness?"
                - add variables that increase range of possible values without changing distribution
                - add variables that increase equivalence of distribution
      - find the rules of which objects can generate key object combinations that are important 
      - find the rules of finding which key object combinations are important
      - talk about differences between systems & spaces they inhabit
      - when you describe the attributes & functions of an object, make sure to list key attributes of each function in a keywords attribute for quick searching for relevant interactions
      - why would "finding the symmetries that involve transforms that dont compromise identity of any objects in a system" 
        solve the question of "how to model these specific object interactions efficiently"?
        - because they were trying to model the object interactions that would stay within a range of identities (particles, energy) that can be transformed into each other & back
      - when that system changed, what happened to the object interactions?
      - find the symmetries applicable in a space, find the rules that explain interactions within that object identity range
      - symmetries can describe the rotation of attributes around a type (axis)
      - identify coordinating/competitive and dominant/passive types to predict diverging/converging behavior
      - examine how types (attribute sets, like a set of biometrics or symptoms) move when they evolve in different parts of the system
        and whether you can derive a rule in their attribute set branch positions for converting one to the other
      - attribute set value network: contains combinations of common values (or values known to indicate a particular identifiably distinct state, like a medical condition) in an attribute set, 
        where vectors indicate the known causal flow between attribute value combinations
      - the origin of a type: 
        - when attributes cluster, it's because they have coordinating functions (or their inputs/outputs do)
        - when attribute sets split, it's because the attributes didnt have enough variance to describe input variance (like in a new environment or disordered system)
      - interactive system analysis with a sample db of rules/types:
        - examine possible sub-systems given core functions & output set of likeliest sub-system sets
      - object modifications:
        - small changes in structure can invalidate functionality - find a list of those change types
        - each object has a field of potential in which it can be distorted outside its normal boundaries, until it's not recognizable as the same type
      - list methods of variance flow on the change interface (function):
        - how variance accretes in various metrics according to distortion of problem
        - ex: diabetes can cause problems like hormone disruption and kidney problems, 
          and the problem that shows up first depends on which system is more distorted by diabetes,
          as they have different markers but indicate the same underlying condition
      - list methods of identifying metrics of optimization, such as gaps in efficiency:
        - how a priority/intent/problem can be handled with fewer resources


  - structures: 
    - structural system objects like connections/boundaries 
    - structures applying info system objects like variance/dependencies/equivalencies/efficiencies/incentives/asymmetries (info/risk/time) 
  
  - objects: 
    - information objects (contradictions, implications, perspective)
    - structure objects (direction, boundary, node, connection, filter)
    - system objects (inefficiencies, incentives, errors, alternatives, opportunities)
    - variance objects like variance injection points (gaps in rule enforcement) & variance sources (problem types, gaps in system boundary allowing variance from other systems to leak in) 
    - tradeoffs: options with mutually exclusive contradictory benefits (if you take one option, you have to sacrifice the other), often a false trade-off or dichotomy applied when both are simultaneous options rather than contradictory 
    - incentives: a reason to take an action (a benefit or cost) - usually interpreted as default in a system 
    - inefficiency: defined as not using a cost-reduction or benefit-increasing method (using extra unnecessary resources, not using a requirement-reduction method, not reusing solutions, etc) 
    - opportunity: potential move with a potential benefit, with a limited time component 
    - exploit opportunities: opportunity with temporary local (selfish) benefits that allocates cost disproportionately to the system (destroying a system-maintenance concept like 'trust' or 'rule of law') or other objects in the system, with negative emergent side effects (hoarding resource incentives, requirement for monitoring & rule enforcement investment, misallocation of justice) 
    - vertices: important variables that generate/cause/determine/change system development, preferably all of the above but also variables that execute a subset
  
  - functions (optimize, traverse, open/close, apply system filters, reduce dependencies, close variance injection points, enforce rule, identify system objects given their definition, such as a variance gap, map a system layer graph representing combinations, identify/derive system context, find interactions of interaction spaces (which interactions are common across agents, likely given other interactions, etc)) 
    - system analysis function (identify boundaries, gaps, limits, layers, incentives/intents/questions, & other system objects)
    - function to generate a different object (like a different concept network) by varying attributes: 
      - example: if power favored centralization, another core concept like balance would have to favor a chaotic process or not exist at all, or another core concept would need to be added to the network 
    - function to predict which system filters will be useful based on a system priority 
  
    - tests
      - questions to test system filters
        - why do phase shifts happen - bc of the ability for aggregated information to be measured as something else 
          - example: molecules identifiable as a set, data identifiable as a cluster, pattern identifiable as an emergency
        - what are the aggregate effects of many errors in selection of algorithms/parameters/processing/deployment - what phase shifts emerge from repeated or interacting error types?
        - why do you arrange dimensions at 90 degrees? to examine the full interaction space of all possible combinations of the two variables
        - why are polynomials with a leading coefficient of one & having optional zero coefficients capable of being multiplied & added to give the roots to the system of equations?
            - bc scaled versions (through multiplication) and combinations (through addition) can position leading coefficients to be 1 while also positioning trailing coefficients to be zero
            - is there a polynomial coefficient set that you cant multiply or add in a way that makes a coefficient in a position to be one and every coefficient after it except the solution coefficient to be zero? 
              no, bc that would mean the leading term cant be solved
            - once you have leading coefficients equal to one and the trailing coefficients equal to zero, the system is solved for each variable
            - why would you try to solve for each leading term in a matrix? bc they are ordered at that point (formatted to have the same positions in each row) and the solution is also ordered (on the right side)
              - using the concept of position to produce additional organization of information, you can benefit from the alignment of the variable positions by isolating each variable (transforming with multiplication & addition of coefficients until the variable solved for in each row has a coefficient of 1 and all other coefficients except the solution are zero)

  - attributes (cohesiveness) 
      - relationship metadata (related systems, system position in system interface network)
 
  - concepts: closed system (a system that can exist without other systems), optimized system (a system that generates zero variance, whose inputs/outputs are all connected without side effects) 
  
  - related questions: 
    - what known/potential inputs/outputs available in the system could build the path?
    - what is the function linking these variables, given the core functions used to build this system?
    - how can this system be optimized 
    - are too many assumptions hard-coded in this system 
    - is this system capable of a particular function 
    - does this system coordinate with other systems in a stable way 
    - is this system adjacently exploitable 
    - does this system contain more potential (options) than it needs 
    - what input/output paths are available that can achieve a particular intent 
    - where would this system generate coincidentally similar structures (a query to identify false similarities) 
    - what system structures (or buildable system structures) fit in this unknown information-generating sub-system 
    - system-problem interface: what problem types does this system have (gaps, misalignments, mismatches, inefficiencies & conflicts)
    - predict which system filters will be useful based on a system priority (the problem of adding/fitting/reducing structure, which can be used to solve related problems like prediction: which variables are explanatory given what we can measure, and causation: how alternatives can converge to the same level of variance/change patterns)
    - how does a system become overwhelmed with variance (in various forms, including randomness), does it have outlets like interfaces with other systems to delegate variance
    - as change increases, how does context change (where unit of context are additional conditions)
    - what is a way to reduce computation time in a ml model?
      - with answers like:
        - compressing features along mathematical symmetries of object behavior
    - how do you find the likely relevant causes of a process in a system? With answers like:
      - scan the relevant properties & rules of interacting objects, where relevance has various definitions (distance, adjacency, similarity)
    - use logical unit isolation as a source for boundary/symmetry physics when optimizing structures like functions in a system
      - 'how to estimate which phase change a rule implementation is at'
        - required input-mocking/prevention for pathogens
        - single live pathogen exposure at ratios amenable to stressor-handling potential energy as a way to build immunity
      - estimate phase changes to get optimal/efficient/possible paths between function i/o out of operation (core function) data
          example: https://broadinstitute.github.io/wot/
        - you also need to estimate probable & multi-prioritized transport paths
      - cycling on/off antitumor drugs like mebendazole & essential oils with antitumor effects to prevent tumor growth (such as 1/week, then switch to new antitumor substance next week to avoid hepatotoxicity & other toxic buildup)
    - analyze a data set & indicate that it contains:
      - an antecedent variable determining this batch of variables
      - an imminent type convergence that will make these two variables intersect
      - a plateau of change rule changes in the system so the predictor can expect to remain valid for a while after the type convergence.
    - why use system analysis in a neural network? because:
      - the neural net needs some concept of system mechanics built in in order to fill in the gaps left by data
      - if you integrate system analysis, the neural network can modify itself to accommodate its changing inputs & output relationships
      - when a more efficient method to execute an operation is found, 
        the system analysis nodes in your neural network will make sure your network is updated with the latest optimal strategies
      - the system analysis nodes will be able to steadily reduce the neural network structure with enough uses to the final set of explanatory features & conceptual metadata, so all that's left is the most efficient prediction function rather than a neural network model function
      - this will make problems currently solved with AI future-proof & automatable

    - how to calculate the derivation dependency network between metadata objects (types, variables, system structure, patterns, layer variance)

    - what does "defined" mean in a space? It means an object has accreted into a measurable phenomena that is consistent by some metric

    - why is it so useful to use system objects like inefficiency or structural objects like asymmetry as a way to frame & solve problems automatically? 
      - bc these objects offer the most flexibility so they can capture the most variation, and occupy an interim interface between physical reality & conceptual networks, so its a good interface to standardize those interfaces to, theyre standard core objects with high interaction potential on similar interaction layers
      - most of the system filter insight paths represent efficiencies & symmetries that become system defaults
        - copying is more efficient than generating an entirely new object, so attribute alignments tend to develop in systems
        - objects with existing (lower cost) alignments tend to cluster into attribute sets
        - most systems need to handle change and constants cant handle change, so constants tend to be fewer in number than variables
        - ambiguities tend to develop in systems with more randomness bc randomness triggers more new interactions, which make change that may stabilize to the normal distribution more efficient, & create objects with similarities, obscuring cause

    - how to generate interface filters (system, type, function), starting with unit interfaces function & attribute:
        abstract    pattern
        set     system
        subset    filter
      function    
        intersect   change (convert attribute to function)
      attribute
        set     type

      - you could extend this to find new objects on the next outer layer after another transform/combination

    - the most common useful filtering objects to build insight paths are:
      - similarities/differences
      - core functions
      - boundary rules (enforced & unenforced)
      - variance injection points
      - attribute alignments (similarities, equivalents, alternates, opposites - real & false)
      - causal direction/degree
      - embedding direction (do you use a tree of networks or a network of trees to frame a pattern)
      - symmetry stacks (example: diverging in position, then diverging in shape, then diverging in color)
      - intersecting patterns
      - interaction space
      - potential field
      - neutralizing/invalidating rules
      - efficiency overlap
      - vertex intersection
      - tradeoff spectrums
      - optimality topology (optimizing in one metric direction as a tradeoff or adjacent to optimizing in another)

    - how to generate this list of useful filtering objects to evaluate a system:
      You apply core concepts to core components on core interfaces until you reach a function/object/attribute that explains/generates/determines/summarizes a system:
        "filter_generation_map": {
          "equivalence of core structure": "alignment"
        }
        - "equivalence" is the core concept, the core interface is "structure", and the core structure metric is "direction"
        - "equivalence of direction on the structure interface" parses to "alignment", which is a useful filter for evaluating a system.
      This filter can be applied to generate the next outer layer of filters:
        {
          "alignment of core system component": "attribute alignment"
        }
        which is a "core concept (filters.alignment) of core component (attribute) on a core interface (system)"

    - what interfaces are useful to apply to a system next, once its framed as a set of generative filters to highlight its inconsistencies:
      - change: base (average, randomness, extreme, balance)
      - intent: completeness (in combinations) for an intent

  - examples

    - example of system object 'alternate routes'
      - an alternate route is an important system object that can be used to reduce solution spaces for analyzing causation in a system
      - a definition can be more useful if framed in objects on a certain interface
      - equal
        - indistinguishable given measurable attributes & their values - equal in value
        - symmetric (buildable with components the other is built with) - equal in origin (resource attribute set indicating starting position)
        - independent (not buildable with the components that the other is built with) - not equal in origin

'''
```
{
  "attribute": {
    "attribute cluster": "species differentiation features tend to cluster"
    "attribute similarity": "location/agents (hospitals & staff/patients) with isolated conditions to prevent overuse of resource needed (cleaning supplies) for mixed condition (non-isolated hospitals/staff), where isolated conditions align with invalidation of cleaning supplies for that condition",
    "attribute alignment": "rotation force aligned with input force creates momentum",
    "attribute matching": "stacking objects that can make cubes in the knapsack problem to reduce unused space between objects",
    "attribute accretion": "symmetry stacking occurs to develop granular features (symmetries in the bio system like the spine/limbs)"
  },
  "metric": {
    "inadequate metric": "",
    "incorrect test": "",
    "incorrect threshold": ""
  },
  "concept": {
    "definition route": "",
    "definition structure": "most abstract concepts have a definition network"
  },
  "info": {
    "efficiency": ["similarity", "overlap", "expectation"]
  },
  "error": {
    "false similarity": "there are many routes to a shape or point which may differ on important metrics like intent",
    "false contradiction": "",
    "false potential": "",
    "false constant": "",
    "false conflict": "",
    "false category": "",
    "false assumption": "",
    "false paradox": ""
  },
  "state": {
    "state permutation": "thermostat that switches off if natural temperature is equal to set involves permuting state of temperature variable to find a case where AC/heat wouldnt be needed for intent of conserving resources"
  },
  "type": {
    "constant attribute set": "types are a set of attributes that stabilize long enough to be identifiable as a type and interact to form other types"
  },
  "problem": {
    "conflict": "",
    "competition": "",
    "distribution": "",
    "routing": "",
    "grouping": "",
    "organization": "",
    "imbalance": "",
    "catalyst": ""
  },
  "logic": {
    "implication": "",
    "contradiction": "",
    "condition": "",
    "equivalence": "",
    "assumption": ""
  },
  "pattern": {
    "repetition": "",
    "order": "",
    "position": "",
    "function distortion": ""
  },
  "intent": {
    "intent ambiguity": {
      "unanchored/unmatched intent",
      "non-standard distortion",
      "distortions without intent",
      "neutral intent",
      "unknowable intent",
      "alternate intent"
    }
  },
  "potential": {
    "enforced rules": "",
    "breakable rules": "",
    "boundary gaps": "",
    "possibility spectrum": "",
    "interaction space": ""
  },
  "system": {
    "scale": "",
    "localized/mismatched complexity",
    "difference from random configuration",
    "difference from unit configuration",
    "alignment/efficiency ratio",
    "sub-system interactions",
    "threshold adjacence chains",
  }
  "change": {
    "symmetry": "",
    "balance": "",
    "power": "",
    "variance injection": "point where a rule can be broken or has an enforcement gap",
    "variance accretion": "",
    "change demand/supply": "change occurs from triggers (phase shift, threshold, interaction) and the structures that can support them (matter state)",
    "error_types": {
      "rule change",
      "direction change",
      "threshold change",
      "definition change",
      "phase shift"
    }
  },
  "cause": {
    "cause direction": "",
    "alternative": ""
  },
  "interface": {
    "perspective": "",
    "standard": "",
    "filter": ""
  },
  "point": {
    "injection points",
    "decision points",
    "limit points"
  },
  "function": {
    "core function": "",
    "filter": "",
    "equivalence": "",
    "route": ""
  }
}
```
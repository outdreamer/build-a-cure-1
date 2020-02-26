## Identifying Key Objects


# Definition differentiation

    - given that most conceptual objects are related, how do you identify which are most important in determining another object?
    - identify that "intent" is highly related to "priority"
    - identify that "insight" is highly related to "strategy"
    - identify that "role" is highly related to "function"

### Questions

  - How to decide which layer to choose core functions at?
    - the lowest layer is mathematical, directly operating on numerical values (add, multiply, etc)
    - then above that you have functions (composed of those lower math operations) having successively emerging intents, starting with functions that are system agnostic & apply to all systems (find, combine, merge, build, etc)
    - above that, youll have a layer of functions composed of lower operations that apply exclusively to the relevant system you used to derive the core functions 
      (for a biosystem, functions like "borrow a gene", "learn an attacker profile", "send signal")


### Generate Important Object Model Interactions

    - how would you generate the useful interfaces/parameters of the object model, if you didnt already know these useful ways to use object/attribute/rule/type definitions?

    - given common functions (combine, fit, relate, distribute) and the set of objects (attribute, type, function, object), you can generate the set of interactions:
      - generate full set of unit shapes possible with functions (network, sequence, tree, layer, etc)
      - combine shapes with all objects (attribute tree, type network, function layer)
      - combine functions with all shapes to get higher shape layers, like system shapes (network tree)
      - combine functions with all objects (change function type, distribute object function, type fitting attribute, fit relation function)

    - then you can identify the useful interactions out of that set using filtering rules:
      - filter by interactions that maximize variance of entities involved
      - filter by interactions that are unitary/simple to get core interactions

    - this process can be applied to other systems

    - another useful process is identifying unique objects & core functions in a system, which should be run before the above object interaction generating process


### Identifying important semantic objects in a problem space

    - identifying optimal structure, or object identity:
      - exploit opportunities, monster systems/assumptions, risk chains, error & variance cascades/flow, transaction iterations, trade loops

      to understand a particular problem space:
      - markets, function prediction/derivation/reduction, attribute/path optimization, compression, metadata generation (moment-generating function), etc

    - how would you identify those important objects in a system?

      - you can filter combinations by variance & usefulness, like in the "object model generation" example above

        - "type networks" and "variable networks" are particularly useful combinations, for example

      - but this leaves out a method to identify the combinations of combinations with significant variance interactions:

        - such as connecting the following interacting variance rules to identify that (given these variance rules) an exploit opportunity is an important object in the problem space:
          - "agents vary by intention"
          - "intention varies from stated intention"
          - "rules vary from enforcement rules"
          - "implementations vary from implementation rules"
          - "optimal implementation varies from actual implementation"
          - "beneficiaries of a rule optimization efficiency vary by distribution"
          - "agents identifying a rule optimization efficiency first can imbalance the distribution of benefits in their favor"
          - "exploit opportunity"

        - the existence of this object is dependent on whether each rule in the chain holds (if rules are unenforced, if agents vary by intention, etc)

        - examples of objects:
          - rule: a path
          - rule optimization: method to find a path at reduced cost (reduced distance, ie a shorter path)
          - rule optimization efficiency: the shorter path itself, or a pattern in rule optimization methods

      - some of those important objects happen to be interfaces (simplifying standards for comparison)

        - the previous example was generated using the variance interface
        - some interfaces that are also important objects or direct combinations of important objects include:
          - trade loops (closed systems are an implementation of a combination of the boundary/type interface and the structure/loop interface)
          - risk chains are an important object that you could generate using the structure/gap interface, given that risks are uncertainties/info asymmetries
            risk is also an interface itself, so applying it to the structure/chain interface creates the risk chain object

        - shape configurations involve different values of the parameters, which can be core components (number of sides, angle, number type, etc), that accrete into shape types with differentiating derivable/emergent attributes

    - also fitting known structures & known permutations of structures to explain a possible missing object or combination in a system

    - what parameters apply across interfaces? 
      - info, similarity, change, combination, position, structure, concepts, time, other interfaces

    - condition/alternate flow
      - what influences the accidental evolution of alternates, other than symmetries (complexity/intent/resource/stressor alignments)?

    - what are the patterns of stressor demand/change supply matching?
      - this is the same problem as intent (gap)-function matching - the stressor demands that you do something new, and you supply change to handle it
      - look for variable sensitivity (high output change from low input change)
      - distortion patterns of function-finding, function selection, function estimation, function generation (same for function patterns & variables)
      - alternate calculation methods & combinations of inputs/conditions/operations/metrics

    - system operations:
        - emergent intersecting property (momentum, size, shape) interacting with a closed system (cell)
        - closed system components within a host closed system (organelles within cell)
        - closed & open system components within a host closed system
        - system/component boundaries/layers


### Object Layer & Interface Identification

    - there may be an optimal layer or other set of objects on one layer or across layers with which to frame a problem

      - when framed in this way, the problem is always solvable 

        - same operation as selecting a host system to represent a problem space, or selecting structures to represent the problem space objects themselves
        https://twitter.com/remixerator/status/1205700297965727749

    - there may be an optimal interface to solve a problem, based on problem type or available resources (info, info-generating, variance-minimization, & other resource types)

      - evaluating solutions for system impact is a key failure point to focus on, to prevent this method from generating same error types as existing methods
      - this means identifying chains of interacting patterns that can produce variance objects (like a black swan or other types of risk chain) & at which times its likely to do so, based on chained interaction times

    - all interactions that are not predicted in a emergent problem or designed solution space are sources of variance (and also may be exploit opportunities), that can convert a solution into a problem, or occasionally produce a solution by coincidentally interacting order & variance (a mutation that generates a function to protect from a pathogen, by trial & error of which mutations survive)

    - designed objects often differ from emergent objects in chaotic ways that produce more variance rather than reduce it, unless design is built on understanding of emergent objects higher up causal chain

    - in a math space, interfaces can take the form of standard unique shape units

    - how would you identify all the interfaces in a space? 
      
      - interfaces: simplifying filters that standardize across most/all objects in a way that highlights their differences for comparison

      - this is a similar problem to identifying symmetries

      - symmetries involve variables that dont change when another variable changes

      - interfaces involve standardization (removal of variables that dont change) to leave the variables that change


### Identifying useful object combinations

    - combine risk, cause, variance, and probability objects (uncertainty, causal loop, variance generator, probability distribution)

    - combine structural & conceptual objects (vector + priority)

    - what is the set of interface objects optimal for solving a problem of particular dimension (x, y, z) & shape a?


## Determining optimal search terms for learning automation

  - deciding what to invest time learning, after it's clear that you need more information

    - example:
      - for instance with splunk, how would you identify what level of expertise is required in order to design optimal queries?
        - different query design + latency + data mismatch because of compute/aggregate/cache data strategies that differ from a standard db implementation

    - the optimal level of learning is where you can:
      - identify a clear design intent for deviations from standard implementations in a tool

    - identify gaps in understanding & translate into optimal search keywords for learning automation

      - identify priorities & decision algorithm of solution design, abstractions with opinionated implementations, hidden complexity, errors from interacting structures (compounding intent/patterns/gaps) 
      - identify lack of understanding
        - there is a level & pattern of complexity that is common to understanding of a tool:
          - people dont normally develop a solution of complexity 2 for a problem of complexity 1 - there are reasons for the complexity mismatch
          - so to identify lack of understanding, look for over-simplification in summarization of a tool
          - sometimes the lack of understanding will be on the implementation side rather than the user side, bc of lack of planning/organization
      - how do you identify key objects/terms that are necessary for acquiring a functional level of understanding that is capable of anticipating/minimizing errors in implementing that tool?
        - a beginner wouldnt know to search for 'abstract syntax tree' when education themselves about testing tools, or 'latency' or 'caching' when learning a new data storage/query tool
      - how do you map lack of understanding to these terms once you identify lack of understanding and key terms to acquire functional understanding?
        - you can derive key concepts of the problem space and map them to key concepts of solution space
          - key concepts of security problem space:
            - standardization
          - key concepts of security solution space:
            - standardization applied to code interpretation: formatting/parsing/translation
              - query for 'code security formatting parsing translation' should lead you to 'abstract syntax tree'
                - query result keywords:
                  - interpolation, string 
                    - data type is key concept of string
                      - machine interpretation of data type by language
                        - machine language
                        - keywords: query for "code machine language parsing" has suggested related keywords: Lexical Analysis, Compiler, Backus–Naur Form, Context-free Grammar, Code Generation
                          - keyword results: query for "code parsing compiler security" or "code parsing lexical security" would then also lead to 'abstract syntax tree' concept in subsequent results
                        - top results: query for "code machine language parsing" leads to "abstract syntax tree" in first few results
          - in this way you can derive which concepts are important to learn to acquire functional understanding for a particular problem
          - how do you score these concepts based on importance, once you find them?
            - repeated abstract concepts inherent to sub-tools like languages (which is a sub-tool of the security intent) are likelier to be important
            - concepts with clear differences in intent are likely to be important (caching & latency reduction are sub-tools of data storage/retrieval intent with clearly different intent matrixes)

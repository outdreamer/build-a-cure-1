# Idea Implementations

## Object Model Applications

  ### Problem Type Prediction for a System

    - given a system structure, which problem types are likely to occur?

    - problem types:

      - conflicts
        - conflicting inputs/requirements/logic/incentives/assumptions

      - asymmetries
        - resource asymmetries (misallocated info, cause, power, variance)
        - emergent patterns created by imbalances in usage patterns

      - variance injections
        - unrestricted inputs
        - unhandled error types

      - misaligned incentives 
        - (monitoring function not given reason to check lib building monitoring function)

      - incorrect position/structure/rule/direction
  
  ### Problem Source Identification

    - example: if a bottle containing juice is the only thing someone drinks regularly and it makes them sick, how do you figure out that it's most probably bc of a chemical on the inner lining of the bottle, programmatically - ranking less probable causes as well

      - query object definitions involved (bottle, juice, person) and relationships involved (containing, drinking)

      - query attributes of objects that interact (with output: bottle lining-juice, bottle cap-juice, manufacturing machinery-juice, juice-person, etc)

      - query known strategies of implementation - with output:
        - 'aligned supply and demand may not match in quantity, quality, or timing'
        - 'goods are often not purchased immediately because supply and demand matching is imperfect as information is often unavailable'
        - 'to protect goods while waiting for purchase, chemicals are used'
        - 'to find protective chemicals, companies do research'
        - 'interim sub-optimal solutions are often used while waiting for optimal solutions'
        - 'companies often use easiest chemical to find, which are often within a set range of permutations away from or combinations of common chemicals'
        - 'a company usually finds an optimal solution before the sub-optimal units are purchased'
        - 'if a company finds an optimal solution, they often still try to sell the remaining supply of the sub-optimal solution'
        - 'usually the company produces x batches before they find a better solution, if they integrate customer feedback and use third party evaluators'

      - query causes of that illness (medication, nausea, food poisoning)

      - eliminate unlikely causes using filtering rules, for efficiency (reverse later if none found among likely rules)
        - 'regular use of a product can produce sustained or compounding impact'
        - 'toxic chemicals are more likely to be used by large companies with ties to legislators'
        - 'ingesting chemicals is x times more toxic than breathing or touching chemicals'
        - 'the industry producing this product has x lawsuits/reports and z oversight relative to other industries'
        - 'the industry producing this product has a regulation loophole x that would allow exploit y'
        - 'this company's business model doesnt incentivize quality control at the source level'

      - after scanning all the objects someone interacts with regularly, this set of interactions should be able to identify the bottle lining as the problem

      - if no problem source is found among their current objects, their purchase history & that of those they interact with can be scanned for prior exposure or dietary causes

      - uses insight path technology

  ### Interaction Predictions

    - before buying a product, after scanning the objects you own, this tool would be able to tell you how the product might negatively interact with the other objects
    - example: when buying essential oil, it would answer questions like:
      - 'how will this interact with the furniture in my house, if used as directed?' (diffuser)
      - 'how will this interact with the furniture in my house, if used as people use it for alternative purposes than directed' (medical)
      - 'how effective will it be for a particular problem/use case' (this is simulated product testing using object model queries like in the previous section)
    - it would also scan the commonly used & potential use cases for possible intentions with the product
      - 'if youre planning on using it for use case "self-treatment", only take x amount for y period of time if youre otherwise healthy'


## Variable Accretion Patterns

  - visualize:

    - emergent properties as circuits within an object/system/type set

    - variables as an output vector or tensor composed of tensors or vector sets
      - several metrics united by origin point, 
        such as how a species' features are composed of a network of many causative factors, 
        where a variable like dog paw shape is representable as a subset of these network paths, 
        and a smaller subset of network path patterns (causation physics)

  - add examples of system/object/rule/type change patterns

  - add examples of variable gathering patterns into a type

  - add examples of variable accretion patterns (how an object like a system or a type becomes influenced by a new variable)

    - variable path pattern convergence/divergence and interaction with systems/objects/types/rules

      - this should enable you to predict:
        - variable flow (which variables are about to be irrelevant, which variables would disrupt others, which variable types to use)
        - variance flow:
          - in system/object/rule/type:
            - stability/boundary/change/isolation patterns (core/granular functions without side effects, independent closed loop systems)
            - exchange rates (how it trades variance with other objects and how the sum of all trades influences system variance)
        - impact between variables & other system objects
        - impact of variable survival success on external system dynamics
        - optimal variables/functions/paths for a function/system/type
        - optimal origin positions of concepts to allow successful systems to evolve

    - stable variable collisions occur when variables:

      - dont disrupt the system interactions
          example:
          - produce metabolites that are handled by existing mechanisms
      - actively coordinate with the system interactions for existing intents
          example:
          - aligns intents
          - links trade loops to optimize trades
      - supports emerging intents that have not been exhausted out of full set of possible system intents
          example:
          - creates a type split
      - replace system interactions
          example:
          - provide extra regulatory layers as a backup check
          - provide self-repair or self-regenerative capacity to create independence within the system

    - unstable variable collisions happen when variables:

      - introduce more variance than needed or supported, or enter the system at a point or state where supporting functionality is inaccessible or underivable
          example: 
          - interfering with a gene that is not regulated/protected
      - interfere with system interactions
          example: 
          - prevent cell communication
      - remove barriers between systems
          example: 
          - removing barriers between organs or systems can produce cascading problems (blood barrier, intestinal/mucosal barrier)
      - a variance injector that interferes with causal variables or system-wide variables
          example: 
          - mutagenic compounds disrupt bio system on a system level

    - example:

      - more complex models progress to simpler models with increases in system stability, which create a system that can interact with more systems without a corresponding degree of change disrupting its functioning, but rather aggregates logic & fits it in the places where it can enhance stability, as a steadily increasing degree of exposure to new variables allows the system enough time to produce handlers that standardize chaotic inputs to usable inputs

      - this progression makes it possible to identify:
        - when a simpler model is the future & more useful version of a complex model
        - which direction the complex model is progressing in (away from/toward standardization/simplicity)
        - the set of reasons why its moving in that direction (system unraveling through interaction with more complex systems its not prepared for, etc)


## Concept Operations

  - this is the set of core conceptual math operations between concepts

  I. combine (add)

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

  II. reduce (find, filter, subtract)

    - x without y
      - "power without information" => "information-derivation method", "power from non-information source", "limited power"

  III. apply (expand, group, iterate, multiply)

    - apply to another (x * y)
      - "balance of power" = "symmetry between input & output dependencies"

    - apply to itself (x ^ n)
      - "power of power" => "the enabler of enabling" => "input", "abstraction", "coordination"

  IV. standardize (simplify, compare, divide)

    - x standardized by y
      - "power standardized by power" => 
        "power explained by power" => 
        "explain power using only objects in power definition (input/output/objects)" =>
        "enabling happens from providing inputs to a high proportion of other objects or to very important objects (having important, causative, or many connections)" => 
        "high ratio or symmetry of power object outputs: important object inputs or high causation ratio" 
          (given that important objects can be powerful just because they enable many other objects, even if they dont provide all of the inputs of other objects)

## Problem Solving Operations

  I. Match problem & solution using definition & standardization, applying increasing limits until problem & solution match

    - get a problem, standardize & define it: 
      problem: "funds cannot always be verified to exist with existing currencies"
      standardize: 
        "there is no way to check prior transaction info to determine funds availability"
        "transaction info exists in isolation of other transaction info"

    - define solution requirements: 
      "must be usable by any trader", 
      "transactions must be verified", 
      "must be relatively quick to enable normal transactions"
      + standard currency definition attributes

    - reduce problem into necessary solution boundary:
        "transaction info exists in isolation of other transaction info"
        "group transaction info" (transaction log)

    - apply solution requirements to solution boundary to check if its sufficient:

      apply(requirements, "group transaction info") => 
        still has problem "transactions are still isolated from previous transactions so previous transactions can be faked to give illusion of funds"

    - iterate same process, with new problem "previous transactions can still be faked"

    - standardize:
      "previous transactions are editable"

    - reduce problem into necessary solution boundary:

      "make previous transactions not-editable"

    - apply solution requirements to solution boundary to check if its sufficient:

      apply(requirements, "make previous transactions not-editable") =>
        still has problem "cannot check that each transaction is based on a non-edited transaction history"

    - iterate same process, with new problem "cant verify each transaction's transaction history"

    - standardize: "make sure each transaction is using correct transaction history"

    - reduce problem into solution boundary:

      "make sure each transaction is using correct transaction history" => "give software doing each transaction access to correct transaction history"     

    - apply solution requirements to check if its sufficient:

      apply(requirements, "give software doing each transaction access to correct transaction history") =>
        still has problem "transaction software might not have access to correct transaction history"

    - iterate with new problem "transaction software might not have access to correct transaction history"

    - standardize: "access to transaction history is not guaranteed"

    - reduce problem to solution boundary:

      "include transaction history in each transaction process"

    - apply requirements & check if its sufficient:
      apply(requirements, "include transaction history in each transaction process") =>
        still has problem: "if software process cant fetch transaction history, the transaction is not verifiable"

    - iterate with new problem "software process needs guaranteed access to transaction history"

    - standardize: "transaction history needs to be an input to the software process" (do_transaction() function)

    - reduce problem into solution boundary:

      "transaction history needs to be an input to the software process" => "transaction history is a parameter to do_transaction() function"

    - apply requirements & check if sufficient:
      apply(requirements, "transaction history is a parameter to do_transaction() function") => 

      still has problem: "if param is not populated, transaction cannot be done"

    - iterate with new problem "tx history param is not guaranteed to be populated"

    - standardize "make sure tx history is guaranteed to be populated"

    - reduce to solution boundary:

      "make sure tx history is guaranteed to be populated" => "add tx history further up causal chain so its embedded in guaranteed input to do_transaction(), like the transaction itself"

    - apply & check if sufficient:

      apply(requirements, "add tx history further up causal chain so its embedded in guaranteed input to do_transaction(), like the transaction itself") => solved

    - further requirements can be added to the solution with the same procedure (hash to make the tx log shorter, etc)


  II. Solve problem with structure fitting

    - rather than sculpting an invention using an increasing set of limits, you can select or derive a structure that probably matches, then check if it fits

    1. using the requirements of a solution, design a structure (or range of structures) that may match the problem space

    2. check if it fits the problem space

      - 'fits the problem' means it:

        - fills in gaps of the problem if the problem root cause is a lack of something (missing info or resources)
        - corrects alignment of vectors in the problem if the problem root cause is a misalignment (misaligned incentives, priorities, etc)
        - reduces problem dimension if the problem root cause is complexity (too many factors to measure, doesnt fit existing tools, can be solved if broken into smaller problems)

    example:

      - derive possible structures given the problem definition & the set of target concepts:

        - problem root cause (problem type) of "requiring trust" is "lack of information"
        - how can you use concepts (uniqueness, randomness, relevance, trustless) and the standard transaction structure to create a "trustless transaction"?
        - you already have a standard structure for a transaction (two nodes, exchange of resources each node has using connection between nodes, each node has different information resources)

        - now you can either use general distortion methods & topical distortion methods to design a new structure to solve the problem, or you can add distortions based on which distortions would produce optimized relationships between structure nodes to find the structure that is likeliest to solve problem

          1. query to retrieve common distorting functions of successful inventions (combine, embed, randomize, rotate) or existing alternate transaction types (privatize, encrypt, publish, verify)
            and apply these and combinations of these and check each output transaction structure to see if it fits problem space

          2. or start with standard structure of a transaction and add distortions based on which distortions would fulfill intents leading to target concept combinations "trustless transaction"

            1. start with standard transaction structure 

            2. which distorting operation might reduce trust (info asymmetries) required in transaction?

               - distribute information by adding it to both sides until its equal (both entities have the information)
               - distribute information by removing it from both sides until its equal (neither entity has the information)
               - distribute information to a third party (encrypted or inaccessible information store that can provide zero-knowledge proofs of contents)
            
            3. key objects of distorting operations are: information, distribution, balance, sides

            4. find requirements for relationships between distorting operation objects:
              - which sides need to be balanced in information in the first place?
                - each participant in a transaction (balance in information between requester & sender of funds)
                - each third party node verifying & executing transactions (balance in information between transaction log and new transaction)
            
            5. find structures to achieve requirements

              - what distorted transaction structure can balance information between transaction log and new transaction?

                - given the standard transaction structure & the distorting operation ("distribute information by adding it to both sides"),
                  what is the new transaction structure after applying this distorting operation that fulfills the overall priority of "reduce required trust"?
                    - implementation of distorting operation to problem objects "add information to the transaction that balances its information distribution with the transaction log"
                    - apply distorting operation implementation to problem space: 
                      - "which information does the transaction log have that the transaction does not?"
                      - "transaction log has history of prior transactions, which the standard transaction structure does not"
                    - check if applied distorting operation implementation moves problem space toward priority (trustless) or reduces problem dimension (info asymmetry):
                      "does including transaction log (or subset of it) with transactions reduce trust required (info asymmetry between prior & current transactions)?"


  III. Solve problem with solution function selection

    - for each problem dimension, there is a set of functions that can reduce the problem dimension to a point, by finding the formula for the shape of that problem dimension (like a line)

      - there are many ways to build a formula for a line, but the best ways usually:

        - fulfill an attribute (such as simplicity, least number of transformation operations, shortest distance between points, definition of similarity such as adjacence)
        - match existing unique formulaic patterns (a unique formula cant be classified as just a transform of another formula)
        - use existing resources (if you have x & y, a solution formula using x & y to reduce problem dimension x is more optimal)

      - example:
        - a problem space has several dimensions, one of which is missing information or conflicting incentives
        - a solution formula to reduce these dimensions might be a formula to get or derive information, or a formula to align incentives


  IV. Solve problem with Conceptual Query

    - get a conceptual combination with a query of problem space & find an abstract structure that fits this combination, then find a specific structure that fits the combination

    - example:

        Input concepts:
          - uniqueness
          - randomness
          - symmetry
          - relevance

        Input relationship network:
          - uniqueness on both sides of a symmetry can be used for verification
          - relevance can organize information where its value is optimized
          - the value of information is optimized when its distributed
          - distributing information on both sides of a symmetry would allow verification of new information
          - symmetries exist between types (two objects of a type, such as a transaction)

        Now we will look for intents & structures that could alert us to problem spaces where this conceptual insight network would be useful.

        Concept Intents:
          - verification (uniqueness, randomness, symmetry, relevance)
          - distribution (symmetry, relevance)

        General Structures:
          - communication structures (internet)
          - storage structures (log, database, hash function)
          - combination structures (log, database, function, distance, similarity)
          - interaction structures (relevant properties, interacting relationship functions between objects)

        Conceptual Solution Boundary Requirements:
          - in order for uniqueness to be useful as an identifier, it must be paired with each object to identify (tx id + tx)

        Conceptual Boundary Decomposition:
          - combining unique identifiers enhances uniqueness (tx id + tx log hash)
          - uniqueness enables using uniqueness symmetries for verification (uniqueness of tx log hash would probably only perfectly match a specific tx log's hash)
          - verification also requires symmetry in verification ability (all parties involved must have access to info needed to verify)
          - tx log is an asset everyone has access to
          - tx log has a unique hash
          - combining unique tx log hash with tx id pairs information by relevance (each tx has a related tx log history)
          - each tx also has a required range of tx log histories, that would allow the tx to take place 
            (any log history enabling the transaction, which allows the transaction to happen - meaning the funds exist & are valid)
          - each log history used for new tx must have symmetry (match) with log history of other traders (must be accurate)

        Output conceptual relationship structure (this is the network of rules representing the invention):
          - host information in the object that requires it, for each object to be a source of verification that also uses verification as an input
          - tx objects need to be symmetric in some way with other tx objects (tx log provides the symmetry to conduct match/check operations)
          - tx objects need to be unique in some way compared to other tx objects (tx id/tx log hash)
          - embed the logs needed to verify new tx in each new tx
          - by combining uniqueness identifiers, aligning information symmetries, or organizing by relevance, the tx funds can be verified using the tx history
            - three different conceptual paths to arrive at the same conclusion: "include hash of the prior tx log with the new tx log entry"
  
        Specific Problem Space Structures:
          - log
          - transaction metadata
          - internet
          - tx log/ledger/database
          - hash function

        Output concept-structure matches:
        - uniqueness: tx log should have a unique hash
        - randomness: any node can verify, equally likely to be able to verify, have same resources such as tx log & software
        - symmetry: 
          - tx log should match the claim of each transaction
          - ledger has embedded concept of balance in asset trade amounts & assets
          - matching of information supply & demand (allocate tx history to tx metadata, where it has most value)


  V. Solve problem with Conceptual Combination Metadata query

  - if you know that a certain configuration of uniqueness & randomness can output a lack of predictability, and you know that a lack of predictability means randomness can be verified (trust in randomness is not required), then for any problem with a target intent of "verifying randomness", or similar intents ("verifying information", "correcting info asymmetry", "not requiring trust"),
      you can match that configuration of uniqueness & randomness with the problem and see if it reduces the problem dimensions (solves the problem)

  - this can also be abstracted:
    - rather than storing "uniqueness/randomness config => unpredictability", you can store:
      - "consistent variance => upredictability"
      - "consistent variance => randomness"
      - "distributed variance == randomness"
    - these abstract rules between conceptual configurations (a combination of concepts in a particular structure, like a system) can generalize the configuration to more problem spaces

  - these abstracted configurations have different metadata (intent, priority, logic flow, variance level, causation) and can therefore be useful in different (possibly meaning "additional") circumstances than the original configuration


## Concept Derivation

  - identifying unique objects in a system that cant be defined in terms of standard operations on other objects

    example:
    - power cant be defined as a simple combination of other objects in the networks it participates in, because its an abstract property having many possible implementations, all having one thing in common, which is the role/behavior of "enabler/enabling", and power is therefore occupying more than one semantic layer, as it can be an object, role, function, input/output, depending on which structure is more relevant to the host system for this implementation of power

    - however, defining it in terms of these possible structures it occupies (input, role, function) is too simplistic - for example you cant define power as simply "an input" because while that is true, given its enabling functionality, it leaves out a lot of information and fails to distinguish it from other inputs, which may not be powerful since they are common or easily substituted with alternatives

    - even defining power by its core unifying function "enabling" is too simplistic because often power does more than just enable something, given the connectedness of systems - meaning that enable one thing often disables another thing in the system or an adjacent system, which creates effects other than enabling, as the disabled process may disable the original enabled process down the causal path

  - therefore we can conclude that abstractions are concepts that:

    - can take many structures (the concept of equivalence has many possible implementations)

    - can impact many systems varying by system attributes or system types (abstract, calculatable, variable, understood, types, functional, prioritized, optimized)

    - cannot be perfectly defined as a simple function of other objects, but rather are definable with a set of simple, core boundary rules that differentiate them from other concepts
      - these boundary rules do not involve other concepts on the same layer, but rather core components
      - for example, the core components of common shapes are: line, point, curve, corner
      - the set of common shapes are the uniquely identifiable combinations of these components (circle, square, triangle) that are not identifiable as simple transforms of other common shapes, but rather are composed of simple limit rules based on their core components (line, point, curve, corner)

      - "enablement" doesnt perfectly capture "power", and the concept of "enablement" also relies on the concept of "power", but it does differentiate power from other concepts & unite its possible implementations & meanings
      - "symmetry" doesnt perfectly capture "balance"
      - "similarity" or "substitutability" or "identity" doesnt perfectly capture "equivalence"

    - are uniquely identifiable compared to other concepts
      - balance is related to symmetry so these are not unique concepts but embedded/dependent/overlapping/hierarchical concepts
      - however balance is clearly differentiable from power, as balance inherently involves equivalence and power doesnt, whereas power inherently involves enablement and balance doesnt


## Selection of optimal generative function
  - see problem-solving section "Solve problem with solution function selection"


## Identifying important semantic objects in a problem space
  - example: identifying optimal structure, or object identity (exploit opportunities, monster systems/assumptions, risk chains, trade loops, variance cascades/flow, transaction iterations) to understand a particular problem space (markets, function prediction/derivation/reduction, attribute/path optimization, compression, metadata generation (moment-generating function), etc)


## Standard Neural Network Design for initial complex problem factor identification reduction
  
  - given that neural networks apply "apply, aggregate, & filter" functions to sort causative information into a standard shape like a tensor or vector set 
    (representing function variables generating an output variable)

    to identify sources of causation (like feature position or feature shape),
    
    how can neural network structure & algorithms be designed to generate a network & algorithm that is likeliest to be able to identify causative factors in the largest range of problem types?

  - there is an optimal network structure & algorithm that can handle the derivation of most causation shapes, since features aggregate in sets that have patterns between input features & output sets

  - the goal of optimizing neural network use is to identify the prediction function from as little data as possible

  - once you can identify an accurate prediction function using one data point (so its robust to changes in causation), the field of machine learning would be invalid

  - in order to do this, you need to identify:
      - candidate variables (cant verify which are actual variables without more data points)
      - variance patterns in the data point (one candidate variable leading to other candidate variables with net impact on overall variance)
      - causation shapes related to those variance patterns (causal loop, causal vector, causal network, etc)
      - priorities (structural priorities like aggregate, distribute, balance - functional priorities like align incentives, produce variance, optimize - conceptual priorities like change)
      - patterns, structures, generative functions, etc - all derivable objects on all interface layers
    - or any subset of these which can explain the complexity of the data point

  - given the profile of these derived interface objects, you can design a neural network that can identify:
    - the minimum information of future data points necessary to accurately categorize a new data point as belonging to the class of the training data point
    - the change patterns objects of this class are likely to display

  - so a neural network that can identify any prediction function takes these interface object derivation functions as input, 
    and if they are above a threshold, 
    integrates them into a final decision of class & other metrics like 
      - change patterns
      - minimum information
      - optimal network design for this complexity level (which will probably involve fewer calculations than the 
        original classification calculation because not all information from derived interface objects 
        provided enough variance compression to be included in the final classification)

  - given that existing networks identify feature contribution, using metrics like feature position, 
    more accuracy in generating prediction functions can be added without extra computation using other interface object metrics like:
      - feature type
      - feature variance
      - feature priority
      - feature distortion
      - feature uniqueness
      - feature causation shapes
      - feature change patterns

  - this means a set of networks evaluating the contributions to final classification for a given complexity level or other system metric made by:
    - causal shape
    - change patterns
    - type stack
    - conceptual query

  - can produce answers to questions like:
    - which interface object combinations can be used to generate an accurate prediction function?
    - which interface object combinations map to which prediction functions?
    - which interface object prediction-function generating networks should be used first on a problem, 
      given that interface layer's higher independence/causation/variance-generation?
    - which problem types (conflict, alignment, asymmetry, lack) map to which interface objects?

  - so instead of doing problem-solving operations like:
    - get data
    - apply standard DNN or neural network structure designed by auto ML
    - use prediction function until no longer valid

  - you can problem-solving automation operations like:
    - get data point
    - apply interface object derivation function
    - check if problem is solved
    - if not, apply interface-based neural network design function to generate optimal neural network for this problem until problem is solved, 
      at which point, store this interface object combination in index of solved problems
      and to make each new prediction, first apply interface object derivation function to each data point to format it 
      in ways that the neural network trained to identify contribution of interface objects to final classification can interpret
    - if problem changes:
      - generate new prediction function, according to previously identified change patterns of derived interface objects if they exist
      - re-apply whole process to generate the new prediction function or a neural network architecture to generate the new prediction function


## Object Layer & Interface Identification

  - there may be an optimal layer or other set of objects on one layer or across layers with which to frame a problem
    - when framed in this way, the problem is always solvable 
      (same operation as selecting a host system to represent a problem space, or selecting structures to represent the problem space objects themselves)
    https://twitter.com/remixerator/status/1205700297965727749

  - there may be an optimal interface to solve a problem, based on problem type or available resources (info, info-generating, variance-minimization, & other resource types)

    - evaluating solutions for system impact is a key failure point to focus on, to prevent this method from generating same error types as existing methods
    - this means identifying chains of interacting patterns that can produce variance objects (like a black swan or other types of risk chain) & at which times its likely to do so, based on chained interaction times

  - all interactions that are not predicted in a emergent problem or designed solution space are sources of variance (and also may be exploit opportunities), that can convert a solution into a problem, or occasionally produce a solution by coincidentally interacting order & variance (a mutation that generates a function to protect from a pathogen, by trial & error of which mutations survive)

  - designed objects often differ from emergent objects in chaotic ways that produce more variance rather than reduce it, unless design is built on understanding of emergent objects higher up causal chain


## Identifying useful object combinations

  - combine risk, cause, variance, and probability objects (uncertainty, causal loop, variance generator, probability distribution)

  - combine structural & conceptual objects (vector + priority)

  - what is the set of interface objects optimal for solving a problem of particular dimension (x, y, z) & shape a?


## Derivation methods

  I. Differentiation
    - what is the path definitely not?
    - "what is the probable function linking these variables, given that it is an adjacent transform of a square (related function type) and is a distant transform of a manifold (unrelated function type)?"

  II. Pattern analysis
    - what would the path between inputs/output be, given patterns of other paths?
    - "what is the function linking these variables, given common function patterns between variables of these types/topics/ranges/other metadata?"

  III. Optimal path analysis
    - what would the optimal path be, given a certain intent, object identity, & host system?
    - "what is the function linking these variables that is most efficient/involves fewest variables/involves known constants?"

  IV. Causation
    - given the position between these causal factors, which causal patterns are likeliest?
    - "given that a species occupies an interim position between evolution, efficiency, time, and environment, what is the likeliest causal shape linking a species with its environment?"
      - for more evolved organisms, this is a network causal shape, though species with less developed cognitive ability may have simple or uni-directional shapes with environment
    - "what is the function linking these variables, given these functions linking other adjacent generating variables/functions further up/down the causal shape (stack/line/tree/network)"

  V. Type stack
    - given a known type stack progression, what is the likeliest position or extension of that stack?
    - "given that these species evolved this way, what level of variance is the missing link between them likely to have?"
    - "what is the function linking these variables, given the type stacks of the function objects (dimensions, adjacent functions, identifiable shapes, etc)"

  VI. System analysis
    - what known/potential inputs/outputs available in the system could build the path?
    - "what is the function linking these variables, given the core functions used to build this system?"

  VII. Intent analysis
    - what intents does this path align with or could be built from?
    - "what is the function linking these variables, given the variable intents a, b, c and the combination intent matrix ab, bc, ca, and the possible output intents of that matrix, and similarity to output intent of y"


## Definition differentiation

  - given that most conceptual objects are related, how do you identify which are most important in determining another object?
  - identify that "intent" is highly related to "priority"
  - identify that "insight" is highly related to "strategy"
  - identify that "role" is highly related to "function"


## Insight Shapes (Unit, Paths)

  - use patterns in network structures & insight paths to predict:
    - probable missing pieces of networks
    - insight path of a route type (optimal/realistic)
    - insight path trajectory for a particular assumption set


## Variance Shapes
  
  - given that variance flows through systems in patterns, what are the common variance shapes, given host system type & structure + set of unknowns?


## Pattern Shapes

  - given that observed patterns often have patterns, what are the common pattern & pattern-generation shapes, given variance level & observation tools?


## Prediction Shapes

  - given that predictions are often between similarly complex systems & target metrics, what the common shapes of predictions, given system type & structure and metric type + set of unknowns?


## Risk Shapes

  - a chain of risks (uncertainties) is a common structure seen in market patterns (such as trades, product engineering, demand assessment, & prediction markets)

  - other risk shapes include:

    - asymmetries:
      - info asymmetry (info being better than no info, all other things being equal)
      - understanding asymmetry (understanding being better than a prediction hypothesis)
      - risk chain asymmetry (luck being better than preparation, in edge cases)

    - equivalencies:
      - randomness (in input identity)
      - balance (in resource distribution)

    - variance generators:
      - risk generators (variance-producing variables, such as equal distribution of information, randomizing functions, etc)
      - complex systems (which have greater complexity than that which can be understood by its observers using existing tools) like markets
      - boundary-changing variables

    - variance reducers:
      - risk-reduction structures (using diverse models to check predictions rather than one)
      - risk-distribution structures (distributing different information to different positions/agents)
      - probable convergence/divergence points (singularity, filters, constants, etc)
      - boundaries/limits (minimizing risk & establishing probabilities)
      - optimization methods

    - variance movers:
      - categorizing functions (delegating risk to the accuracy of the function combination of variables, constants & operations)
      - probability distributions (delegating risk to accuracy of distribution selection)


## Causal Shapes

  - most causal shapes are cyclical, tensor, layer, or network-shaped rather than one-directional vector-shaped, which is why some existing methods are inherently incapable of producing system-fitted insights that wont break the system when applied (a particular drug that is not evaluated for bio-system impact, just impact on a particular pathogen or process)

  - part of the problem with using a one-directional vector to model a relationship is that the underlying parameter (usually time) may not be relevant for predicting the relationship evolution

  - rather than modeling it by a standard of changes over time, it can be modeled by a standard of changes over variance potentials
    - will a particular variance source change compoundingly or converge to a constant in all possible parameterizations of that variance source
    - does a particular variance source have the potential to generate variance or will it eventually become static in all possible implementations, 
      meaning it either:
        - doesn't exist (at any time), like a final output that doesnt ever return to interact with other systems as an input
        - is one of the few things that does exist (across all times), like a concept that never stops influencing variance


## Predicting Interface Evolution
  
  - given that we currently understand object & system definitions, the object model seems optimal to us right now, with current tech & information

  - what if the assumption that the object exists is flawed?
    - its not an entity that exists, unless its exerting influence to generate variance in some system & cant be controlled
    - it only exists according to its relationships to other entities (define an entity using other entities)

  - what if the structure assigned to the object (a separate entity) is flawed? 
    - should be a type stack, a subset of a network, a formula, etc, rather than a list of attributes & rules

  - what if the idea of a system is flawed?
    - the assignment of a host system can be so catastrophic to the accurate representation of a problem that it may be better to avoid this & use only rules that apply to all systems

  - what if the idea of a definition is flawed?
    - if definitions/facts begin to decay the more theyre assumed & depended on, if stretched beyond their capacity

  - what if the idea of interface selection is flawed?
    - what if there's an optimal interface to represent all information (interface-building formula), rather than a specific one (causal, object, type, function, priority, system, structure interface)
    - an interface is just a standardizing filter - a formula to generate the right standardizing filter for a particular task would be better than relying on interface definitions

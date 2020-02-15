## Problem Solving Operations


### Common solution functions/strategies

  - distort/standardize
  - alternate/stabilize
  - isolate/combine
  - position (arrange)
  - compress/expand
  - transform (change)
  - fit (match/contain/fill structure)
  - differentiate (key points of difference)
  - filter (find: start from everything & reduce)
  - derive (build: start from scratch & build)
  - metadata (minimum information to derive)
  - generate (using limits, interfaces, symmetries, variables)
  - map (physics of limits, combination, calculation, approximation, measurement)


### Alternate structural layers

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

    - there are multiple ways to represent problem spaces:

      1. dimension stacks:

        - any problem metadata attributes of the problem are represented as dimensions & stacked

          - similar to how adding a dimension to a square makes a cube, stack dimensions in ways that clearly describe the problem
          - the order of the dimension stack itself may give the solution, if the problem is a variable-ranking problem

      2. shape assigned to problem types

        - problem types (like conflict or missing info or imbalance) have semantic shapes:
          - competition: a missing shape to create an archetype (a shape with a triangle missing to create a circle), like receptor binding, to indicate competition for a resource (the triangle) between agents (multiple circles looking for a triangle to complete their shape)
          - conflicting vectors (incentives, intents): vectors leading an agent in conflicting/diverging directions, where each vector starts at the agent or pushes the agent
          - missing info: lack of enforced rules creating an opening where info can gather
          - imbalance: different sized vectors creating bias on one side of a symmetry

    - example:

      - the attributes permuted to create various math objects (spaces, functions, sets, groups, number types) can be arranged in a way so that their intersections reveal meaningful combinations

        - math-attribute structure fitting example: 

          - if you start from a circle of nodes representing default spaces and you permute the operations or number types of that space, you have a set of new spaces
          - in what structure can you arrange these circles & transforming vectors in a way that reveals the semantic overlap of these attributes?
          - for instance, how can you arrange the objects (vectors, angles) and operations (multiplication) in a way that reveals the emergent attributes (associativity, commutativity) of various combinations/transforms (normal numbers, default vector space, quaternions) - so that their intersections reveal corrollaries in attributes/rules/types?

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


      - counterexample:

        - one problem with solving problems on the structure interface is that the analysis becomes over-specific
      
        - for example, solving the problem of 'which structures tend to have which effects' solves the problem of drug design in isolation
        - really you would need to predict good compounds/organisms attacked by a drug structure like useful bacteria cell membranes in addition to the negative compounds/organisms like pathogen cell membranes
        - in order to predict that, you need to know how similar structures can evolve in a bio-system with different output intents (protect or attack bio-system)
        - otherwise your drugs will work on the pathogen but also have severe negative consequences that you only find out about after patients die
        - you can solve this on the structural level by making the drug extra specific to the pathogen, but that is less efficient than finding a drug that only targets the pathogen because it attacks an attribute/mechanism specific to pathogens (not the cell membrane but an energy source or process used only by pathogens)

        - to predict the similar structures with different intents, you need to find structures that generate these structures in the system
          - example: 
            - the corners of a cube would likely generate 3-d triangular clusters of any component small enough within the cube, and because the corners are evenly spaced, these triangular clusters would probably have similar functions/intents
            - but a shape with alternating or intersecting structure-generating structures (like the corner generates the triangular clusters), would probably produce similarly shaped objects with different function/intent, because one corner might be surrounded by waves and another corner might be surrounded by openings, so the triangular clusters would probably still evolve in each corner type but with slight differences that produced different function/intent

      - solving problems with structural analysis also requires predicting change rules with standard physics

          - if you have a triangular cluster, it will probably change into a rounder shape if it has space to interact with other non-triangular shapes, bc its corners will get rounded out
          - similarly, the key variables creating differentiation will evolve on this structural difference interace
            - differentiation has to be consolidated to the interfaces that can change, otherwise a system cant adapt to new conditions
            - if compounds cant get mutated/broken, theres no potential for adaptation
            - so differences are concentrated on the boundary/exterior when functionality requires differentiation (in compounds, receptors, general chemicals, etc)
          - so if you have a system where an object having corners will be introduced to environments where it will be rotated & allowed to interact with shapes having some degree of difference, you can calculate which shapes would produce this level of difference & the output function of the triangle, which is rotation, as well as its probably future state, which is circular, unless the other shapes are sufficiently different that they break the triangle into smaller triangles or bind to it to form larger shapes

      - structural differentiation output (intent/function) can be calculated once system structure & priorities are known

        - example: 
          - once its determined that a system prioritizes backup alternatives, you can determine that each differentiated object of a type will have enough similarity to the other types to generate the other alternatives if necessary
          - once you know that this is the determining factor in differentiation, you can predict the level of differentiation and predict the variations of an object (like proteins or enzymes with different functionality, whose functionality & degree of difference should be predictable given system priorities)

        - the reverse can be true as well - calculating system structure from internal object behaviors, if they follow these patterns so you can posit the existence of system objects like corners/openings

        - similarly you can use the middle interface (system objects) to infer the system structure or the objects in the system

      - system/object requirements can be calculated using this analysis as well

        - once requirements are known, differentiation probabilities can be reduced with that information

          - if its required that every protein has an off-switch, then that wont differentiate the protein definition/template, but if some proteins dont have an off-switch bc theyre so important or difficult to make, that can be used to calculate probable proteins that exist in a system requiring proteins of different functionality to handle various stressors


  III. Solve problem with solution function selection

    - min info => selection of structural layer

    - structural example:

      1. how to identify the correct interface to solve the problem of 'area under curve' for a non-standard shape:

        - do you identify the nearest standard shape & derive the transformation function mapping standard shape area/metadata to non-standard shape area/metadata?

        - do you identify the standard shapes that are best at approximating the non-standard shape (easily added objects like rectangles that can approximate an asymmetric curve's underlying positive area)

        - do you identify sub-functions or functions on intervals of the curve & approximate their areas instead, summing them after their areas are found?

          - can you arrange these sub-component (functions/shapes split by interval) in a way that forms standard (and therefore more calculatable shapes)?

            - is there a way to arrange sections used to approximate area under the curve in a way that forms parabolas, etc

          - matching distortions (matching area above line with area below line so line can be used instead of curve)

        - can you map it to another function of variables with similar or equivalent variance & use that to map the area attribute?

          - a mapped problem might be: 

            - "calculate a metric of expanded dimension (dimension + 1) of a point (meaning a line) differentiating the line from a limit relevant to lines"

              - is there a relationship between point & line that mimics the relationship between line & area so calculating the line metric once expanded from a point can give a transformable answer into the area metric for a shape limited by the lines?
            
            - "calculate a metric of reduced dimension (line) for an area to describe difference between line & limiting line"

              - is there a relationship between cube & square metrics that can be used to estimate or calculate area if you have volume of shape created by curve expanded by another dimension?

        - calculate in the reverse direction:

          - how to derive set of lines possible for a particular area?
            - determine if the line described is likely to be a possible output for an input area

        - can it be reduced to area of another function with same probability distribution of outputs (y)

        - do you identify attributes higher up causal stack that can calculate area faster than approximation functions? 

          - distorting variables of a straight line or rules detailing when standard/type/rule boundaries break

        - what sets of limits & forces describe the motion between a standard & a distorted function?
          - how does value accrete when bounded by two points, but unrestricted in one direction (when a line becomes curved)?
          - what are other limits that can cause a similar accretion (triangle with corner accretion point removed and standardizing to the line?
          - what impact do these limits have on change/combination rules (to predict impact of transforming curve into line or expanding line by another dimension)?

      2. given these solution functions, how do you select which one is likeliest to produce solution given optimization metrics (accuracy, time)


    - add variable-selection example with separate alts having equivalent outputs:
      - if one alt is disabled, then it would give a false result for anyone checking it for ability to impact the output, even though the alternative was being variably used instead
  
    - should be possible to estimate the value added by choosing a path between equivalent-seeming alternatives before its clear which one is correct, 
      given the variable networks/layers & metadata (structure, complexity) of the variance between alternative paths, 
      & relative to problem space metadata (path optimization metrics, intent)
      as well as which path will probably be correct, with increasing certainty given additional metadata,
      based on variable complexity relationships and other metadata relationships

    - lets say youve derived a network of possible functions to achieve a certain goal
      - how do you choose whether to narrow it down further or accept this level of variance in your solution set, requiring a context to select a particular function from the set?
      - if its unclear whether an alternative metric/metric value is optimal 
        (metrics or metric values are similar & differences arent clearly relevant to goal)
        thats a good candidate network for postponing the selection to selection demand time

    - for each problem dimension, there is a set of functions that can reduce the problem dimension to a point, by finding the formula for the shape of that problem dimension (like a line)

      - there are many ways to build a formula for a line, but the best ways usually:

        - fulfill an attribute (such as simplicity, least number of transformation operations, shortest distance between points, definition of similarity such as adjacence)
        - match existing unique formulaic patterns (a unique formula cant be classified as just a transform of another formula)
        - use existing resources (if you have x & y, a solution formula using x & y to reduce problem dimension x is more optimal)

      - example:
        - a problem space has several dimensions, one of which is missing information or conflicting incentives
        - a solution formula to reduce these dimensions might be a formula to get or derive information, or a formula to align incentives

    - identifying which function combinations are used optimally elsewhere and which function combinations havent been used is another function selection mechanism

    - the evolution of functional layers (core to interim to output functions) is another source of insights on system development & design

    - determining which interfaces, attributes & concepts determine the biggest difference in function performance 
      (scale physics, structure physics, info physics, causal shapes, change physics, logic, types, dimension sets, metric selection, complexity, etc)

      - selecting standard model for optimal problem reduction into components 
        (framing it as a task suitable for organizational, optimal transport, route optimization, distribution, position assignment, sequence ordering model, etc)

      - selecting adjacent models that existing problem structure can be converted/broken into (system molecules forming problem structures)


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


  V. Solve problem with Conceptual Combination Metadata query (different starting point as IV)

    - if you know that a certain configuration of uniqueness & randomness can output a lack of predictability, and you know that a lack of predictability means randomness can be verified (trust in randomness is not required), then for any problem with a target intent of "verifying randomness", or similar intents ("verifying information", "correcting info asymmetry", "not requiring trust"),
        you can match that configuration of uniqueness & randomness with the problem and see if it reduces the problem dimensions (solves the problem)

    - this can also be abstracted:
      - rather than storing "uniqueness/randomness config => unpredictability", you can store:
        - "consistent variance => upredictability"
        - "consistent variance => randomness"
        - "distributed variance == randomness"
      - these abstract rules between conceptual configurations (a combination of concepts in a particular structure, like a system) can generalize the configuration to more problem spaces

    - these abstracted configurations have different metadata (intent, priority, logic flow, variance level, causation) and can therefore be useful in different (possibly meaning "additional") circumstances than the original configuration


  VI. Vectorization of Problem & Solution Space

    - example:

      - problem: 'find lines that are duplicates in files and remove duplicates, leaving lines in order'

      1. map to vectors

        - variables

          1. meaning

            - line content

              - words in line
                - word positions
                - standardized word form (distortions removed)
                - standardized word meanings (generic, common)

              - expanded content
                - content types
                  - examples
                  - extra information

          2. order

            - resolving altered & new lines that are not duplicates

        - metrics

          - duplicate sentences
          - order in sentence list
          - position in word list
          - equivalent meanings
          - relevant meanings

        - concepts

          - equivalence
            - synonym
            - order
            - alternate meanings of same word

          - relevance
            - relevance by extension: related information of existing sentence or new sentence
            - relevance by order: new sentence should come after original sentence
            - relevance by type: sentence should be positioned in set of other sentences because of common type/meaning/topic

          - priority
            - when two possible duplicates are unresolvable, how do you decide between them?

          - variable rank

            - does line position override other variables?
              - questions are determined without user input:
                - without a user telling the algorithm which variables are in which ranks, figure out which variables out-rank other by which match problem complexity & intent
                - given that the problem is 'merging two files, removing duplicate lines':
                  - the intent is likely not to include two lines with one word difference
                  - the user probably doesnt intend advanced semantic analysis, or the problem statement would include keywords like 'analyzing sentence meaning'
                  - so extra computation shouldnt be invested in advanced semantic analysis in the case of deciding between duplicates
                  - that means less computation-heavy variables should be ranked higher, such as line order 
                    (two sentences are likelier to be duplicates if they are nearer in order)
                - now your algorithm has determined rank of a variable compared to another programmatically, without user input other than the problem statement
                - this means the problem statement has to be well-defined & standardized & reflect user intent

            - similar analysis can be done to select variable value-selection or ranking logic:
              - does generic or common definition come first when selecting better synonym to merge, given a pair of similar words that are clearly alternates in the duplicate sentences

      A. vectorization

        I. identify variables, metrics, concepts (and their metadata like definitions, types, priorities)

        II. from previous objects, identify meaningful level of variance
          - lines that are equivalent

        III. from level of variance to aim for, identify intent & check that it matches problem solving intent
          - intent: 'remove one of a pair of lines that are equivalent'
          - problem solving intent: 'merge files, removing duplicate lines'

        IV. now you should have:
          - a set of initial nodes (variables)
          - a set of concept nodes (to evaluate variables like meaning with object definition for equivalence)
          - a set of final metric nodes (to test variable values)
          - a set of intent directions (to test trajectory from initial variable nodes, to concept nodes, to final metric nodes, to check that this trajectory aligns with intent direction)

        - This means you've vectorized the problem space.
          - From the initial problem definition, you've created a simple network for solution theories to traverse.
          - From here, the automation of this method is calculatable.
          - You figure out which items in the problem space are input variables, interim nodes, and output metrics, then you convert each to vectors & transform the input vector to the output vector using the interim transforming vectors (core functions, concepts, types, priorities) as tools.

        - in order to map a semantic object to a vector, you need to identify:

          - which objects can be used as filters to further solution intent (and which objects are key determinating objects & which can be removed)
          - how to arrange those objects as filters to get from starting variables to output metrics/intents

- objects:         - position  - lines           - words       - meaning                 - relevance                     - relevant lines & append rules                                - de-duplicated merged file
                                                                                         - equivalence                   - equivalent lines & merge rules
- object intents:  - isolate   - target var loop - compare sub-components of target var  - alt defs of sub-c comparisons - map aggregate output def sub-c matches to target var & rules
- transforms:                  - iteration1      - iteration2  - variable                - concept                       - concept-iteration1 & concept-rules                           - aggregate iteration1 output
- transform intents:           - iterate         - iterate     - alternate               - differentiate                 - apply & apply                                                - aggregate

          - the vectors connecting these objects represent a solution space (network starting from variable layer to target metric/intent layer) 
          - the vectors connecting the specific versions of these objects (using specific definitions & rankings) represent a possible solution

          - this is different from:
            - a conceptual query: bc it involves object definitions on other layers than conceptual & fits concepts to a structure first (assigning concepts like equivalence to the word variable similarity comparison)
            - object definition: bc it involves concept queries
            - problem shape dimension reduction: bc it queries concepts & object definitions & key problem-solving metadata like metrics, and assembles them in order as filters between variables & intents, and the trajectory between these filters is the output solution
              whereas problem shape dimension reduction assembles a problem shape as a set of composing dimensions, which each step in the solution should reduce these composing dimensions, and the solution is the order of operations that reduces the problem shape dimensions the best according to some solution metadata (like solution metrics)

          - assembling object networks to allow causal shapes:
            - you may want to assemble networks logically to allow for other causal shapes
              - for example, attaching an alternate & feedback network so the metrics can be used to modify the variables

        - This frames the problem as an optimization problem from starting variable network nodes to target metric/intent network nodes, as opposed to framing the problem as a shape dimension-reduction problem, splitting the problem into dimensions and applying solutions to reduce dimensions until the problem is a point.

      B. filtering solution space

        I. pre-computation

          - rather than trying every trajectory, you'll want to pre-compute some metadata

          - for example:

            - if there are operations between node layers that point in a direction that is so different from solution intent directions that it couldnt be converted into a solution intent direction with available remaining operations, you'll want to rule out those operations, and possibly the whole node if every operation on it is irrecoverable

            - if there are initial steps that reduce a high level of variance/make a high level of progress toward a direction, where the remaining available operations are unlikely to produce an irrecoverable intent direction, those should be prioritized when searching for solution trajectory (which will be the output logic function representing the optimal solution to the problem)

        II. out of the remaining options, you can use filtering rules when iterating through the remaining possible combinations of steps 

          - is this definition divergence likely to be within the range of potential created by change rules?

          - is this level of computation likely to be required for this problem definition?

        III. remaining solution (or solution set if irreducible) example:

          - iterate through lines in both files by position

          - identify similar sentences 

            - if equivalent, add the sentence & set iterator to next line

            - if similar, evaluate words for equivalence

              - standardize words to common form
              - assess meaning of words
              - if there is a clear word pair (similar words with slightly different meanings), 
                - apply equivalence & relevance definitions to find word that is likelier to fit in sentence
                - if there isnt a clear likelier fitting word, select the more general/common word

            - if dissimilar, evaluate sentence for relevance (extra information, examples, etc)

              - if relevant sections identified, 
                set iterator to next line not in relevant section
                if relevant section not found in other file
                  append relevant section 
                otherwise 
                  iterate through relevant sections, treating them as sub-files

              - if no relevant sections identified, check for advanced semantic equivalence

              - if no advanced semantic equivalence found, add to unique sentence list & append to end of file when done iterating
                - check every new line for match with these dissimilar & irrelevant sentence list items in case it's a duplicate of a later sentence

            - write new file of merged duplicates, relevant sections, and unique irrelevant sections

    - now you can see how building a network of several interface layers (variables, concepts, metrics) allows:
      - vectorization of the problem
      - translation of the problem space into solution space (matching intent direction)
      - filtering of solution space
      - finding of optimal solution trajectory (or set of solution trajectories)


  VII. Modeling gaps in Problem Space Systems as Solutions

    1. model the openings created by variance

      - example:

        - intersecting variables create an expanded space in which combinations of their possible values can occur
        - this combination space can fit various structures, so that some combinations are likelier than others
        - anytime a rule is not enforced or a boundary is not protected, that creates an opening for variance to develop, which means structures reducing or modeling that variance can be inferred given system metadata

    2. posit the existence & structure of missing objects (like variables, rules, types, intents) by inferring missing objects implied by structures

      - examples:

        - a square or any shape with symmetries around a central axis implies:
          - the existence of a central point, even though that's not explicitly stated by the square structure
          - diagonals connecting opposite corners
          - forces aggregating any internal objects to the corners
          - slight rotation function if positioned on a surface at an incline & increased by a dimension to a cube
          - intersections of two sets of parralel lines or two sets of perpendicular lines

        - a circle implies:
          - a rotation
          - a square which the circle touches the side midpoints of
          - a square joined by four tangents of the circle
          - an infinite set of vectors diverging equally from origin

    3. use core functions & attributes of structural mechanics (simplest, fewest, most similar structures) to determine the missing object in the openings created by variance

    4. integrate the output of 2 & 3 to generate the likeliest structures in the openings created by variance

    - this differs from vectorizing variables & other objects, as well as problem space dimension reduction as a way to frame solutions, in that it models solutions as objects to find in an opening created by variance, which involves deriving as much of the host system structure as possible from the problem statement (intersecting variance creating missing information about the structure of their interactions)

    - for example, several variable combinations could explain a gap - each possible structure & set can be assigned probability based on inferring system structure containing the gap

    - in the examples above, the variance gap is the unenforced rules (what can be inside/outside the square & how could it behave) created by intersections of objects/attributes/rules (definition of a square), and the system structure being inferred is the host system with rules like "there is an important point in the center of objects with intersecting symmetries"

    - you can also derive sub-systems/objects that are likely to occupy the opening, such as systems/objects with adjacent permutations of variables after you derive those variables
      - example: you can derive that a square object has variables "number of sides" (created by examining variations of the explicit corner, angle, & side objects in the 'square' system) and then permute this variable to generate adjacent objects (for example to check if triangular systems/objects would explain openings created by variance) or implicit objects (center, rotation, diagonals)


  VIII. interface/symmetry derivation 

    - in order to automate problem-solving, you may need to derive the interfaces/symmetries of a problem space, and then stack/arrange them in order that maximizes their utility as a set of filters that generate solutions from the original problem statement

    - by 'interface derivation' I mean finding the symmetries in a problem space, such as finding the 'spectrum interface' in the chaotic-evil matrix, or finding the 'rotation' interface in the shape progression problem space, and then stacking or otherwise arranging them in the order that they are most useful for generating/revealing solutions


  IX. System derivation

    - deriving system structure from scratch rather than using system structure to solve problems

    - involves calculating several objects of lack rather than content:

      - gaps: opportunities for variance to fill, patterns to evolve, shapes to converge
      - emergence: unpredicted items (objects/functions/attributes/interfaces/changes/limits)
      - paradoxes: conflict implying a requirement for change in system structure or an unknown system structure (pieces missing to explain paradox)

    - given core functions (apply x to y) or core variables (x, y) of a known variable interaction, what are the possible dimensions within that interaction?

      - example:

        - given two interacting variables with synced intervals (x & y in euclidean space), what are the dimensions possible within that plane?
          - interaction rule dimensions:
            - overlap rules
          - limit rule dimensions:
            - the limiting rule on limits that can apply in the plane
          - isolated motion rule dimensions:
            - how can a line move through the plane
          - what objects evolve in the plane:
            - corners/curves/extremes/origins
            - patterns (accretion of cooperating/repeated/overlapping rules)
            - alternatives (many ways to derive a shape)
            - symmetries (change governed by a limit)
            - concepts (equivalence/distance/similarity)
            - transformations/components (series or set of lines/shapes to generate a function)

        - it may seem like those are not dimensions but are attributes within intersecting dimensions, however they provide an interface for change so they can be considered dimensions in different spaces 
          (where values are graphed against the dimension of equivalence/symmetries/alternatives)

        - these dimensions within the interaction of two variables can be used to derive the system where the variable interaction is taking place

    - emergence:

      - key objects in the emergence prediction problem space:

        - limits
          - phase/paradigm/state shifts

        - unexplored/unused interaction potentials

        - convergence of items (structure, intent, types) to standard emergent products (attributes like relevance, concepts like power or change)

      - causes of emergence:

          - symmetry (similarity/alignment)
            - example:
              - when growth happens in the same direction, an illusion of a limit can emerge (circle or other shape that seems limited but is only appearing to be limited by a circular boundary, and the primary factor creating that shape is the growth in the same directions (away from center)

          - cooperation (when forces cooperate through compounding/synergistic effects, more changes happen & more emergent attributes can occur)
            - example:
              - when electrons sync their spin, attributes like energy or charge can emerge

          - cascading effects (variance triggers)
            - example:
              - when energy is injected to a system above the rate & distribution it can handle (by storing or using it immediately), energy emerges from the system in various formats (heat, electricity)

          - phase shifts (emergent attribute is measurable above a limit)
            - example:
              - when molecules bind at scale, an object like a drop of liquid emerges

          - need/demand:
            - emerging shapes of need that fit a demand created by a gap in functionality that is beginning to be required by intersecting items 
            - example:
              - a process that is causing problems by going unrestricted is a functionality gap creating demand for an operation that can detect its required limits, determine the lack of limitations & limit its operation

          - emergence of non-linear functions:

            - randomness:
              - equivalence between competing alternative forces, generating equal distribution in growth (circle) or lack of influence on/distortion of natural accretion of motion (momentum)

            - exponents:

              - when variables are isolated, they have nothing but themselves to interact with (expanding x by itself = exponents)

            - intersecting symmetries:

              - when symmetries intersect in a way that allows a standard for comparison (different spectrums at a perpendicular to indicate application of one variable to another in a way that aligns their unit intervals or their centers), it creates room for repetition & ambiguity aspects of non-linearity as happens in a circle

                - symmetries allowing a circle to happen for example:
                  - symmetric rotation around a center & symmetric growth of lines intersecting with that center (outward growth direction)
                  - symmetry of two real number variables (x & y)

              - when a limit exists that interacts with symmetries, growth can occur within that limit, up until the point where growth needs to break that limit
                - the boundary of a circle presents a way to manage growth that has equal opportunity in any direction on the plane
                - the circle has efficiencies toward equal/random distribution that a cornered shape doesnt
                - the most efficient path linking four points equidistant from center is possible with a circle, which allows for momentum to add force to the motion, beyond what a square would allow, which requires more effort to maintain than allowing momentum to advance the motion
                - the square is more linearly derivable than a circle (the square requires a shift of a line in a direction, the circle requires a rotation of a line in all directions), but they can both be transformed into the line interface
              
            - conflicting directions (an extra dimension to the line object):

              - the evolution of a shape with sides (as opposed to a line) involves conflicts in direction, which adds a dimension to the line object
              - this allows the creation of closed loops (common shapes like circle/triangle) where a point need to be compared to another point, but within a limited path of divergence that has one or more turning points where the motion begins to point back to the original point (opposite point on a circle or corners)

            - stabilized equilibria between linearly defined shapes

              - all shapes, even circles, can be reduced to a combination of lines
              - but the shapes in between the shapes with clearly defined maps to line objects (shapes with corners) have efficiencies that accrete enough energy & momentum within limits to achieve stability
                - like a wave is limited on either side but maintains its energy to vacillate between extremes with momentum
                - whereas a shape with corners achieves stability through patterns like:
                  - periodic pausing of motion (allowing corners to develop)
                  - interacting lines which have limits in their interaction types (must link at ends, cant overlap)

            - lack of enforcement of attribute:
              - when an attribute is not enforced (direction), such as when an object is allowed to spin or otherwise change direction, it can generate non-linearities
                - for example, when a line is allowed to spin between limits (parallel alignment with dimensional axis), it can generate a parabola or wave through tangential points of its center

    - paradox: calculating something that doesnt seem directly calculatable from existing resources
      - https://en.wikipedia.org/wiki/Paradox

      - attributes:

        - contradiction: a significant variable misrepresented as insignificant (like time)

          - truth of axioms change according to timing of event, but if the event happens at all, its taken as an absolute contradiction when its really a time-dependent contradiction

          - can occur with mutually exclusive states where conflicting directions are falsely associated (falsehood of an interpretation in a scope doesnt mean falsehood of the same interpretation in a different scope)

        - self-reference: a lack of information about options

          - 'If "this sentence is false" is true, then it is false, but the sentence states that it is false, and if it is false, then it must be true, and so on.' https://en.wikipedia.org/wiki/Liar_paradox
            - true in the sense of meaningful equivalence ('this sentence' equals 'false')
            - false in the sense of consistency between extrapolated implications ('this sentence' equaling 'false' doesnt equal 'this sentence is false' equaling 'false'

          - this is usually a lack of information (ambiguities) about scope & alternate variable values

            - can truth exist on a spectrum
            - can truth apply to different sentence attributes ('this sentence' object in the sentence, the whole sentence, & sentence implications

    - the paradox of a 'list that contains all lists' seems unsolvable (the list needs to contain itself to be a complete set) until you notice that the list of lists is complete even if its missing one because that can be derived from the variation in the other lists, which describes the variables that can change

      - similar to listing n - 1 boolean values of different category values instead of n boolean values
      - the list of all lists contains the list of all lists in itself, so its structure/variables/contents each describe itself, even if its not stored as an item in the list

    - these paradoxes are an alternative to interfaces and involve the apparent impossibility of solving a problem without solving the problem from a system perspective (deriving all possible lists in a system) rather than in isolation (listing all things)

    - system derivation is a way to solve problems like:

      - paradox problems: 

        - is this really two contradictory meanings that invalidate each other, contained in the same consistent system
        - are they misrepresented/not actually contradictory if you correct their system scope/resolve their lack of information/change the variable position

      - variable potential: is there room for variables to accrete/overlap/replace/conflict

      - finding set of system/filters where seemingly conflicting rules are possible, to allow a seemingly impossible relationship between variables (definition of truth, ambiguity, scope, implication)

      - finding minimum requirements of host systems (deriving as little about system structure as possible to solve original problem, to avoid over-specifying system structure)

    - paradoxes usually point to areas that need alternate layers/variance injected (variance demand), where your existing system analysis can identify points where variance can develop (variance supply)
    - paradoxes are a counterpoint to interfaces in that interfaces provide a standard for comparison that leaves out information (reduction), and paradoxes are a false limitation that imply the requirement of variance (expansion)
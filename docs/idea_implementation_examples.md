# Idea Implementations

## implementation of code selection algorithm to select function combinations according to data structure & priority at function stack run time
    - example:
    - select code that is optimized for fewest lines of code/quickest execution time/data storage usage/state storage/memory usage based on input data structure & variance
      - "if input has variance k, allow for conditions checking for parameters of variance"
        - "if input has types [a, b, c], select conditions checking for corresponding types [a1, b1, c1]"
                  if word_type in a1_type_list:
                    type_a.add(word)
                  elif word_type in b1_type_list:
                    type_b.add(word)
                  elif word_type in c1_type_list:
                    type_c.add(word)
                  else:
                    no_type.add(word)
        - "if input has types [a], organize code so that assignment is done at end of condition set"
                  word_type = None
                  if original_type in type_list:
                    other_type = logic_operation(word, original_type)
                    if other_type:
                      word_type = other_type
                    else:
                      word_type = original_type
                  if word_type:
                    type_a.add(word_type)

## implementation of code building algorithm:
    function_metadata = {'input': line, 'output': pattern, 'attribute': {'subtype': 'type'}}

    Prerequisites:
      - the codebase if available should have index_metadata() run on each function so that metadata is queryable for code-building

    1. generate function interface:
      A. using pattern of other generate_*_pattern(line) functions if any are found in available codebase with indexed function metadata
      B. using definition of pattern found in definitions or functions, which is:
        'a variation of a word list with some words replaced with different types of types'
      C. determining the pattern definition implementation relevant for this function, which is: 
        'a variation of a word list with some words replaced with word types'
      D. checking for a function to determine type of a word
      E. using function find_type, which takes in word & returns types list
      F. using input data type line, split into words
      G. iteration through words in line
      H. if type list is returned from find_type, append type list
      I. if no types found, append word

      def generate_type_patterns(line):
        new_pattern = []
        for w in line.split(' '):
            types = find_type(w)
            if types:
              new_pattern.append(types)
        if len(new_pattern) > 0:
          return new_pattern
        return False

    2. look for other functions with similar interfaces:
      A. note that get_alt_sets has similar input/output:
         input = pattern_line, output = list of words or lists of type options

      B. look at where that function is used (get_alts)

      C. check if get_alts has any useful functionality for generate_type_patterns interface intent 'generate pattern'

      D. note that get_alts has pattern characters '|' in its output, which makes it relevant for 'generate pattern' intent

      E. pull in all logic from get_alts and position existing generate_type_patterns interface logic to route input/output similarly

        def generate_type_patterns(line, av):
          new_pattern = []
          for w in line.split(' '):
              types = find_type(w, av)
              if types:
                new_pattern.append(types)
              else:
                new_pattern.append(w)
          all_alts = []
          if len(new_pattern) > 0:
            all_alts = new_pattern
          index_lists = []
          if all_alts:
              if len(all_alts) > 0:
                  for sub_list in all_alts:
                      if iteration == 0:
                          original_sub_list = sub_list
                          sub_list = sub_list if type(sub_list) == str else ' '.join(sub_list)
                          new_sub_list = remove_unnecessary(sub_list, av)
                          sub_list = new_sub_list if new_sub_list else sub_list
                          if type(original_sub_list) == list:
                              sub_list = ''.join(['|', sub_list, '|'])
                      index_lists = append_list(index_lists, sub_list)
                  index_lists = set([il.replace('  ',' ') for il in index_lists])
                  if len(index_lists) > 0:
                      if '|' in ' '.join(index_lists):
                          if (iteration + 1) <= 1:
                              return get_alts(pattern, iteration + 1, av)
                      return index_lists
          return False

      F. check if all logic is necessary & remove if not:
        - we wont be doing more than one iteration 
        because find_type will not return patterns, only lists, 
        so remove that part of logic pulled in from get_alts

        def generate_type_patterns(line, av):
          new_pattern = []
          for w in line.split(' '):
              types = find_type(w, av)
              if types:
                new_pattern.append(types)
              else:
                new_pattern.append(w)
          all_alts = []
          if len(new_pattern) > 0:
            all_alts = new_pattern
          index_lists = []
          if all_alts:
              if len(all_alts) > 0:
                  for sub_list in all_alts:
                      original_sub_list = sub_list
                      sub_list = sub_list if type(sub_list) == str else ' '.join(sub_list)
                      new_sub_list = remove_unnecessary(sub_list, av)
                      sub_list = new_sub_list if new_sub_list else sub_list
                      if type(original_sub_list) == list:
                          sub_list = ''.join(['|', sub_list, '|'])
                  index_lists = append_list(index_lists, sub_list)
                  index_lists = set([il.replace('  ',' ') for il in index_lists])
                  if len(index_lists) > 0:
                      return index_lists
          return False

        G. do same check for any embedded function calls in get_alts logic (append_list)
          and consolidate variable names:

        def generate_type_patterns(line, av):
          new_pattern = []
          for w in line.split(' '):
              types = find_type(w, av)
              if types:
                  new_pattern.append(types)
              else:
                  new_pattern.append(w)
          if len(new_pattern) > 0:
              index_lists = []
              for sub_list in new_pattern:
                  original_sub_list = sub_list
                  sub_list = sub_list if type(sub_list) == str else ' '.join(sub_list)
                  new_sub_list = remove_unnecessary(sub_list, av)
                  sub_list = new_sub_list if new_sub_list else sub_list
                  if type(original_sub_list) == list:
                      sub_list = ''.join(['|', sub_list, '|'])
              index_lists = append_list(index_lists, sub_list)
              index_lists = set([il.replace('  ',' ') for il in index_lists])
              if len(index_lists) > 0:
                  return index_lists
          return False

        H. verify that output matches intent with test data & match input/output relationships to other generate_*_pattern functions if found

        I. if any other generate_*_pattern functions are embedded in other functions, check if that logic is necessary/relevant to this function intent:
          - generate_indexed_patterns() is necessary to ensure uniqueness of repeated vars in a pattern before storing the pattern
          - generate_synonym_patterns() is relevant if there are any words in this pattern 
          - generate_operator_patterns() is relevant if there are any words that could be standardized to operators in the pattern
          - get_specific_pos() is relevant if variables in the pattern arent already pos tags
          - get_all_pos() is relevant if there are words in the pattern that could be converted to pos tags
          - generate_correct_patterns() is applied to other patterns before applying get_alts()
          - generate_pattern_type_patterns() is relevant in that it assigns types to generate a pattern so this function could be extra useful for input/output relationship comparison

## Object Model Applications
  
  ### Problem Source Identification

    - example: if a bottle containing juice is the only thing someone drinks regularly and it makes them sick, 
        how do you figure out that it's bc of a chemical on the inner lining of the bottle, programmatically?

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
      - eliminate unlikely causes using filtering rules, for efficiency (reverse later if none found among likely rules):
        - 'regular use of a product can produce sustained or compounding impact'
        - 'toxic chemicals are more likely to be used by large companies with ties to legislators'
        - 'ingesting chemicals is x times more toxic than breathing or touching chemicals'
        - 'the industry producing this product has x lawsuits/reports and z oversight relative to other industries'
        - 'the industry producing this product has a regulation loophole x that would allow exploit y'
        - 'this company's business model doesnt incentivize quality control at the source level'
      - after scanning all the objects someone interacts with regularly, this set of interactions should be able to identify the bottle lining as the problem
      - if no problem source is found among their current objects, their purchase history & that of those they interact with can be scanned for prior exposure or dietary causes
      - this uses insight path technology

  ### Interaction Predictions

    - before buying a product, after scanning the objects you own, this tool would be able to tell you how the product might negatively interact with the other objects
    - example: when buying essential oil, it would answer questions like:
      - 'how will this interact with the furniture in my house, if used as directed?' (diffuser)
      - 'how will this interact with the furniture in my house, if used as people use it for alternative purposes than directed' (medical)
      - 'how effective will it be for a particular problem/use case' (this is simulated product testing using object model queries like in the previous section)
    - it would also scan the commonly used & potential use cases for possible intentions with the product
      - 'if youre planning on using it for use case "self-treatment", only take x amount for y period of time if youre otherwise healthy'

## Insight Paths
  - use patterns in network structures & insight paths to predict probable missing pieces of networks or trajectory of insight path

## Math/Language translation function

  - build math logic/plain language translation function - example: https://adventuresinmachinelearning.com/improve-neural-networks-part-1/
    - in order to implement this, you need to:
      - implement function to break_into_core_functions
      - apply break_into_core_functions() to math and language functions
      - compare both once standardized with break_into_core_functions() & build map of corrollary functions
      - use this as a dictionary for future translation calls
      - the reason is partly to translate and also to make intent-derivation clearer for people who dont like math

    - operator map:
      +: unify
      -: reduce
      /: standardize by dimension
      *: expand by dimension
      ^: apply to itself
      =: match (symmetric despite operation type x)

    - example of operator -> language:
      1. math rule: 
          'W += -alpha * (1.0/m * tri_W + lamb * W)'
      2. structural language version:
          'changes to W take the form of a constant multiplier of (the change in W value applied to the standard of m, summed with a second constant multiplier applied to the previous value of W)'
      3. organized structural language version:
          'initial change between W and previous W based on m, aggregated with a transform of previous W has a constant relationship to output change in W'
      4. abstract organized structural language version:
          'a constant multiplier of previous W and ((the difference between previous & current W) based on m) determine new W'
      5. derived language version
          'the constant multiplier of previous W is different than the m standard applied to the difference multiplier'
      6. structural derived language version
          'constant multiplier of previous W does not equal difference multiplier based on m'
      7. derived math rule:
          'lamb does not equal (difference multiplier divided by m)'
      8. derived math rule with operators:
          'lamb != (change in W)/m'

      - function metadata:
        - intents:
          - 'differentiate influence of change constants'
        - use cases:
          - 'gradient descent'

      - in that example, we went from math rule 1 => math decomposition into language functions 2 => language decompositions 3 - 5 => mapping 6 => math rule 7 - 8

      The overall workflow is:
      - math rule
      - math decomposition to language
      - language decomposition to abstraction
      - abstraction mapping
      - structure application => insight identification
      - math rule

    - example of language -> operator:
      1. language rule: "control the power of power to control power"

      2. operator mapping: "p = x * (p ^ p) + y" (make a function with output: power, built out of inputs: power ^ power)

      3. reductino: 
        "y = p - x * (p^p)"
        "y = p(1 - xp)"

      4. language mapping: "finding the x & y values of that equation would let you control power"

      5. aside from other methods (function query, conceptual mapping), you can continue the translation or reverse it back to language:
        "y can be determined by power expanded by the dimension of (1 - (x expanded by the dimension of power))"
        
        - function query:
          "1 - a quantity" is usually assessing a ratio, such as a probability

        - definition query:
          "power" usually indicates a position having a useful resource, like energy, understanding, or information

        - what ratio can you determine with an expansion of x from power, that when applied to power, produces y?

        - is it possible to determine the winner of a conflict involving a power grab?
          winner = power (1 - (x applied to distance from understanding))
          winner = power (1 - (x applied to informational advantage))

        - apply power to distance from understanding = if the agent has a low distance from understanding (1 - 0.01 = .99) & applies that to some other source of power, they'll win
        - apply power to informational advantage = if the agent has a high informational advantage & applies that to some other source of power, they'll win

        - what is the identify of the other source of power, or is it the general concept, meaning any source of power?

        - relationship query: which objects can interact with information/understanding objects? 
          - information tech, information communication methods, information storage methods, information protection methods, prediction methods

        - the power applied to the second source of power (information or understanding) must be one of the above methods/technologies

        - what do x & y represent? 
          - x may be a constant, which may be a value representing the output of doing an operation on the multiplier
            - x * power = vary power by x, which represents application/implementation/execution success variance
          - y may represent any output of power applied to the ratio of 1 - (x applied to power), which in this example we've assumed to be the winner of a conflict betweeen competitors trying to get some resource
            - y could also be any other output, such as consequences, side effects, contributions to emergent patterns, changes in intents/incentives, priorities, etc

        - translate this back to a linguistic insight:

          "to optimize power usage (resulting in output y), use two coordinating sources of power, and expand x by one source, get the ratio, then expand it by another source"

        - what do operators like "expand" (which we assigned to the multiplier operator) mean for human users?

          - multiplication is a type of combination operator, that takes an item and pairs it with every object of the other item to generate an object of a number of dimensions equal to the number of multipliers (4 * 5 = a rectangle of 4 rows and 5 columns)

          - when we say something like "expand information by power", we're saying, "apply information to every object within power" or "apply power to every object within information"

          - the output insight is: "to control power, control the inputs of power"


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

      - more complex models progress to simpler models with increases in system stability, 
        which create a system that can interact with more systems without a corresponding degree of change disrupting its functioning, 
        but rather aggregates logic & fits it in the places where it can enhance stability,
        as a steadily increasing degree of exposure to new variables allows the system enough time 
        to produce handlers that standardize chaotic inputs to usable inputs

      - this progression makes it possible to identify:
        - when a simpler model is the future & more useful version of a complex model
        - which direction the complex model is progressing in (away from/toward standardization/simplicity)
        - the set of reasons why its moving in that direction (system unraveling through interaction with more complex systems its not prepared for, etc)


## Crypto

  1. use predictive tools to predict transactions & calculate them in advance to speed up tx
    - this would assess people's known resources to build an index of global demand/supply, then calculating through these resource distributions, economic incentives for trades, social networks, platform dominance, & product availability & findability (search results rankings) - which tx were likely to happen where for which products, then calculate those tx in advance


## Concept Operations

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

## Concept Derivation

## Selection of optimal generative function
  - see problem-solving section "Solve problem with solution function selection"

## Exploit Opportunities

## Risk Chains

## Trade Loops

## Monster Systems

## Object Layer Identification

## Randomness Generator

  1. calculate maximal variance points in a system (variables most unrelated to all other variables), and equalize their contributions
  
    example:
      - "cloud size" is directly related to adjacent water, wind patterns, temperature & elements in adjacent air
      - "cloud size" is indirectly related to moon phase (influences wind patterns), sun exposure (influences temperature), pollution (influences elements in air)
      - "cloud size" is very indirectly related to astrology 
        (influences moods, emotions, subconscious, dreams, & market decisions, which influences market trends, which influence side effects of production like pollution)
      - cloud size is so indirectly related to astrology that it may be considered independent of astrology, despite the fact that every object is inherently related to other objects
      - we can say that "cloud size" has a "maximal causative distance" or "minimal dependence" on "astrology"
      - other ways to get a variable that has a minimal dependence on some other variable is to query its dependent variables 
        (cloud size is caused by element distribution, so element distribution is independent of cloud size)
      - in reality this is not real independence, because many dependence relationships are circular, either 
        - directly (one circular loop between two nodes), or
        - indirectly (the output dependent node, cloud size, goes through many systems before returning some input requirement of the input independent node, element distribution)
        - this is because there are very few to zero ways to generate an output that has no side effects on input requirements (input inputs)
          - an example is "victimless crimes" like ejecting junk into space, which may not impact us immediately but definitely will return some causation (in the form of required inputs to some process) to our species eventually
      - another example is "corners of a square":
        - each side of the square is equal, so it's equally likely that the "square" system will generate a movement of balls within the square, that pushes a ball to one of its corners
        - the corners represent a maximal variance variable (corner), which are unique in that if a ball is in one corner, it necessarily cannot also be in some other corner
        - this is the foundation of identifying not just maximal variance-generating independent variables in a system, but also system nodes (gathering points of inputs/outputs) & interfaces (standards)

  2. design systems that optimize the number of independent max variance points
    - how do you design a system with maximal variance-generating independence points?
      - take the problem of a square - how would you generate the corners such that:
        - each corner is unique compared to other corners
        - each corner exerts the same influence on the ball movements within the square
        - each additional corner adds to the variance of the ball movements
      - eventually if you add too many corners, you get a circle - is this the maximal variance implementation of a square, or is there some point between a square and a circle with more variance-generating points than either?
        - it depends on the variables that youre trying to optimize the randomness of - if they can occupy any point on the circle, a circle may be more appropriate - if they can only occupy a corner, you need to find some combination of corners that is not a circle in order to maximize their variance

  - mentioned here:
    https://twitter.com/remixerator/status/1148816151125712896
    https://twitter.com/remixerator/status/1004578257637953537
    https://twitter.com/remixerator/status/1004578256820064257


## Vuln potential of a solution

  1. identify conceptual/type interactions of the solution
    example: explore the interaction of random applied to random (or algorithms applied to themselves, like hash of a hash) for possible interference opportunities


## Invention Prediction

  1. Reverse-engineer: apply known useful functions (combine, reduce, standardize, compare, duplicate, randomize) 
    to fulfill common useful intents (predict, verify, find, etc) & assess value of output product in problem space

  2. Conceptual query: apply structure to conceptual combinations & check matching problem spaces if the output product has value for an agent in that space


## Protocol Recommendations
  
  1. Auto-update crypto keys/algorithms to use constants that are always guaranteed to be below x% risk that they'll be hacked given common computational resources.
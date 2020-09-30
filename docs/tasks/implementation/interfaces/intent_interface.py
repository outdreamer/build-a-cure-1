'''
  - definition: 
    - intent can be defined as possible reasons to use a function (or use an object as a function): 
      - possible outputs (optionally including the explicit intended output, resource access/usage like memory retrieval, object lock, routing information to a function while it's being looked for elsewhere, or processing usage, and side effects) 
      - explicit intents ('calculate x') 
      - implied intents (the implication of an intent like 'calculate x' is to 'use the output of that calculation to make another decision') 
      - embedded intents (implementing a function optimally has an embedded intent of 'optimize this function') 
      - injectable intents (intents that can be injected into a range of functions, like the 'use processing power' intent can be injected into any function) 
  
  - attributes (implication, directness, alignment) 
    
    - intent types:

      - abstract intent:
        - filter
      - abstract intent stack:
        - filter 
          - filter by delimiter if input is a string
          - remove delimiter if split is followed by join (non-standard use of split function)
        - organize (into subsets)
        - isolate (examine one subset at a time)
        - assign/derive position attribute (position has meaning in the input sequence)
        - optimize search (find the meaning within a positioned subset, beyond derivable position meaning)
      - side effect intents are not equivalent to the direct/intended intent of the function, though they can be required sub-steps in creating the function output
      - side effect stack:
        - remove delimiter/filter from string
        - create groups of characters
        - change memory storage/access (string to list)
        - change interface (string functions to list functions)
      - intended/supported/expected:
        - the intended use is that which should be supported by the item, at the supported level of abstraction, and including the network of supported use cases
      - direct:
        - obvious uses of a particular item like 'splitting a list of characters' is an obvious use of the split sequence function
      - indirect:
        - non-obvious uses of a particular item
          - alteration allowed by super type (sequence): 
            - if the split function implementation has support for attempting to convert inputs to a sequence of characters (if a character sequence is its only supported type) before throwing an error, then a sequence of bytes or character encodings could theoretically be input to the function
          - use of function side effect (removal of delimiter):
            - if the split function is followed by a join, it may used to remove the delimiter or replace the original delimiter with the new delimiter input to the join function
          - use of function side effect & lack of validation (organization):
            - if the split function doesnt check its requirements (string data type of input, sequence attributes/methods of input) there's more room for indirect intents
              - if a set, tuple, or list can be split by the function, then the function can be used as an organization or division method, creating sub-tuples, sub-sets, and sub-lists
              - that intent could be used for other intents not typically associated with the split function, such as optimizing search of a data structure (searching subsets rather than entire sequence)
              - the lack of enforcement of data type creates a variance gap, allowing variance to be:
                - exploited (alter data type to trigger bug)
                  - variance exploit is internal to the function & only supports malicious intents
                - injected (use function for clearly unintended functionality, like optimizing search of some object)
                  - variance injection uses function for other intents that cant be fully derived from the function itself, which are a system-level exploit
      - underivable (unless system allows one unique abstract path, which is uncommon in a changing system)
        - once you derive the limit of the possible intents of a function (like optimizing search by splitting some group into subsets), deriving intents beyond that may not be derivable
        - the reason is that this outer layer of possible derivable intents is abstract, and abstract intents fit many problem types
        - what could they be optimizing the search of? any type of content:
          - the optimal function for an encryption algorithm with a particular intent stack
          - the password for a user given their decision history
          - a keyword in a document
        - however you do know some things about their possible intents despite the abstraction layer:
          - the object must be difficult to find 
            - very similar to other objects, of which there are many
            - hard to guess given the usual amount of information known about the object when finding it becomes necessary
            - unfindable with existing filters so that search of it must be optimized
            - the space to search must be disorganized (not organized by the identifying attributes of the object to find)
              - math functions may use only two dimensions, but searching along these dimensions is costly
              - to find functions of a type (where the type is not clearly defined but its clear when a function is not a member of that type), you need efficient filters to reduce the search space
              - for example, filters for encryption functions can include:
                - narrow identifying attributes (clearly that type)
                  - repetition (repeated convergence of values at an interval, like a wave function)
                  - symmetry:
                    - symmetry in variance:
                      - ambiguity (not clear which parameter path was taken to generate a value using other parameters)
                      - lack of clarity in definition of object 
                        (not a clearly determined & therefore simple shape like a circle, with so few direct parameters (2, radius & origin) that it doesnt allow much ambiguity)
                - wide dis-identifying attributes (clearly not that type)
                  - functions with parameters having 1:1 or other simple relationship types
                    - linear functions
                - space-reduction patterns (clearly or clearly not in this section)
                  - non-linearity + ambiguity means circles, waves & circle/wave-adjacent shapes will be relevant to find these functions, 
                    so non-circular shapes can be ignored for finding this particular subset of encryption functions
                  - this is because given the symmetries, there are many ways to calculate target parameters of a circle using other information about it
                    - if you know the radius & origin, you can calculate the circle
                    - if you know the ratio of the circle compared to the unit circle, you can calculate the circle
                    - if you know the square parameters containing the circle with 4 intersection points, you can calculate the circle
                    - the circle is easily determined by its direct parameters bc of the clarity of its definition, but the derivation of other methods that could be used to calculate the circle is the set of alternative paths that are not directly calculatable
                - base or adjacent functions (and their identifying attributes/rules) to the target function type
                  - prime-finding function (adds uniqueness to the equation)
          - the object must be important
            - this implies the object is newly identified as important, like a new prediction signal
          - from there you can derive other intents given these filters
            - youre looking for a difficult to find object that escapes existing filters which is important, like:
              - a prediction signal
              - a search method
              - an encryption function

  - objects (priorities: abstract directions that intents may fulfill or move agents toward, whereas intents are more granular) 
  - concepts (applicability: what a function can be used for) 
  - functions: 
    - allow combination of intents to find malicious intent structures (like a sequence of neutral-intent functions that has an emergent malicious intent when used in that sequence) 
    - operate on intents (intent-modification intent) 
    - derive intent as a dependency of the intent interface conversion function  
    - map intent to direction & assess solution progress by movement in that direction 

    - required functions for each intent:
      - intent-derivation function (whats the probable intent stack/network of a particular event)
      - intent-metadata function (does this intent have side effects or is it granular/neutral)
      - intent-combination function
      - intent-similarity evaluation function
    - required functions for system intent analysis:
      - intent-pattern matching
      - identify gaps in rule enforcement in system
      - identify gaps in information about rule enforcement in system
      - identify gaps in computational possibility about intent 
        (some intents may not be computable, some components may not be predictably interactable until tested or more info is injected)
    

  - structures: 
    - intent matrix is the interaction space of a set of intents, where its emergent intents can be traced across the interaction space 
    - intent stack is the set of adjacent intents of a function, from granular/neutral/abstract to specific/explicit, across various interfaces like logic, abstraction, & structure 
  
    - methods to model intent:
      - network of nodes where each node represents a state & connections are functions transforming one state to another
      - network of system component nodes where direction indicates intent
      - network of variable nodes where sets of node combinations (and their transformation trajectories) achieves an intent
      - model intent as a gap in a structure (missing corner on a triangle) that needs to be supplied with a path or other structure to be considered 'complete' (or the opposite problem of an external structure that needs to be reduced in order to be considered 'closed')

  - related objects

    - related questions: 
      - find specific implementations of a general intent like 'optimization', such as a specific intent of 'optimizing the metric in question'
      - which intents should follow or be combined with which intents 
      - which intents are likelier, given the context implications of the function 
      - which intents are missing, given an overall function intent 
      - which intents do the optimized/simplest/reusable function versions fulfill 
      - intent-logic interface question: which intents align with logical objects (assumptions, conclusions) 
      - intent-system interface question: which intents are common to all functions in the system 
      - intent-function interface questions: 
        - which functions are most exploitable for malicious/neutral intents 
        - which functions' explicit intents don't match their implicit intents (or emergent intents when combined with other functions), which is like analyzing the structural difference between developer expectation vs. user intention 
      - do variable, type, logical, & output intents match overall given function intent 
      - what is the logical sequence that best fulfills this intent (useful for automating code generation) 
        - what is the function linking these variables, given the variable intents a, b, c and the combination intent matrix ab, bc, ca, and the possible output intents of that matrix, and similarity to output intent of y 
      - what intents/directions/priorities does this path align with or could be built from? 

      - intent-matching applications:
        - function chaining for target intent
        - testing
        - finding exploit opportunities
        - predicting output intents of object combinations
           - example: predicting industry tech combinations:
            - risk analysis (finance, insurance)
            - science
            - statistics
            - machine learning
            - information tech
            - quantum
            - computing
          - when these combinations have been exhausted with normal methods of value creation (automation, standardization, combination, platform, search, metadata), 
            there will be a phase shift in the direction of the variance/vulnerabilities of the last combination 
          - can you derive the order each component combination will happen in?
          - the main concern is whether there will be safeguards to control the last combination's potential exploits, or whether any safeguards will be invalidated by prior tools

  - examples:

    - function intent-indexing example
      - rule gaps are created by trust (lack of enforcement in rules)
      - layers of rule gaps can form a possible exploit trajectory to achieve a malicious intent that seems legitimate at various points of validation
      - if a function has multiple intents, that set should be propagated to the next line
      - you can index intent using various layers of functions, which are assumed to have indexable intents
        - sample intent map (semantic: core: code):
          assume: input: parameters
          define: assign: variable = value
          check: condition/filter: if/else/then/switch
          vary: change: iterate (for)
          apply: transform: processing functions (format)
      - so in a code sample from the sample logical flow in "Select & apply method of reducing possible relationships" of Problem Source Identification example 2,
        you can assign intents to each line:
        1. assume: variable1 is variable and in hypothesis_objects and data_is_available(variable1):
          "since location differs between samples:"
        2. check: condition2 variable2 is variable and in hypothesis_objects and data_is_available(variable2):
          "if window.position can differ:"
        3. vary: for each value in variable2 in each variable1
          "if so, alternate window.position across locations:"
            "if window.position is iterable"
              "if len(window.position.possible_values) > 0:"
                "iterate window.position.possible_values"
                - repeat for location
        4. check: does value match any target directions (focus condition intents)?
          "check if alternate window.position achieves student.intents aligning with location object metadata: does opening the window achieve anything in south vs. north room?"
      - the output intent of the combination of these four intent sets in order should be symmetric with the overall function intent
        - the output combination intent, by layer:
          - semantic: "assume, check, vary, check"
            combination intent: "filter subset by iterable subset matching set"
            - the subset is the set of possible value combinations that pass each filter (in this case, that means only variable values of defined variables & the data type we expect, etc)
            - you can derive from this simplified intent form that you should have added a check of the set variable (focus condition intents), without which the whole function is invalid, so that condition should be one of the first checks
          - semantic + objects:
            1. assume variable1 varies (location is a variable)
            2. check variable2 varies (window is a variable)
            3. vary variable2 and variable1 to get combinations (location + window values)
            4. check each variable2 & variable1 combination for match with any target intents (focus condition intents)
            combination intent: "given that variable 1 and variable2 are both variables, vary variable2 and variable1 to get combinations matching target intents"
            - this leaves out the logic to assess the key emergent variables of variable1 & variable2 combinations (temperature, sunlight), 
              which are the actual attributes that should be used for comparison with target intents, 
              since they have a computable/measurable relationship (temperature maps directly to "temperature regulation")
          - semantic + objects + variable values:
            - you can add data analysis based on generated test data to conduct possible intent sets with various data permutations, which should alert you to exploit opportunities
        - given the abstract function intent "find variables explaining target variable", the other intents:
          semantic: "filter subset by iterable subset matching set"
          semantic + objects: "given that variable 1 and variable2 are both variables, vary variable2 and variable1 to get combinations matching target intents"
          line up with what the function is supposed to do, though they are incomplete and have variance injection opportunities (given the lack of direct mapping between combinations & target intents)
        - you can see how lack of direct intent mapping & alignment can alert you to exploit opportunities, or tell you when a function is not done or sub-optimal as youre building a function

    - intent matching examples:

      - "exploit requires that the user has recently visited a site with a TLS cert chained to an ECC-signed root certificate, since the root certificate must already be cached by the targeted system. If a targeted system doesn't have the root certificate cached, an attacker could still pull off an exploit by adding JavaScript that accesses a site chained to the root certificate."
        - intent of sending a request to another site:
          - retrieve info
            - execute function on info
            - display info
          - if there is no subsequently retrieved or already loaded code using the contents of that info, thats a signal that this info is being used for other intents that dont match the intents for visiting a web site (view info, interact with info)
          - the intent of sending a request to a site has sub-intents related to all the site's objects/attributes/types & their side effects
            - if a request has a side effect "caching info", that must be assumed to be a possible intent of the request, rather than more common explicit intents like displaying info

      - an intent of an item (object/function/system) is a 'reason to use it'
        - with human actions, there are good & evil reasons to do anything, although some reasons are more adjacent than others - what matters for deriving intent is the context around the action
          - example: 
            - action: good/evil reason
            - you can see that some reasons are more adjacent (likelier, involving less work) than others - however sometimes functions that required more work in the form of transforms are the correct explanation, when nodes become truly independent so they have to do more work themselves
        - intent stack is full set of reasons to use it, based on known/derivable intents
          - overlapping variance gaps of layered systems in exploit.svg create opportunity chains between system variance gaps
        - function metadata should all be assumed to be possible intents:
          - side effects of a function
          - non-standard uses of a function
          - underivability of a particular intent for the function
          - variance gaps of a function 
        - unknown intent examples:
          - 'to crash the asteroid into the other asteroid' 
            - isnt a known intent, but it will be in the problem space where space mining is an actual problem relevant to solve & the tech is there to support it, or if alien species are doing this
            - this is also not a need of any known system (unless theyre already crashing asteroids into other asteroids using explosions, radiation, & gravity manipulation & Im just a fool)
        - known intent examples: 
          - 'to find the word in the document'
          - 'to classify the species'
        - derivable intent examples:
          - 'to distribute fault for a problem' is a derivable intent using core functions:
            - 'avoid punishment'
            - 'minimize effort'
            - 'ignore error potential'

'''
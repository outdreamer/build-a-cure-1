## Intent matching

  - an intent of an item (object/function/system) is a 'reason to use it' 

    - intent stack is full set of reasons to use it, based on known/derivable intents

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
                
                - narrow identifying attributes (clearly that type)
                  - repetition (repeated convergence of values at an interval, like a wave function)
                  - ambiguity (not clear which parameter path was taken to generate a value using other parameters)

                - wide dis-identifying attributes (clearly not that type)
                  - functions with parameters having 1:1 or other simple relationship types

                - space-reduction patterns (clearly or clearly not in this section)

                - base or adjacent functions (and their identifying attributes/rules) to the target function type

          - the object must be important
            - this implies the object is newly identified as important, like a new prediction signal

          - from there you can derive other intents given these filters

            - youre looking for a difficult to find object that escapes existing filters which is important, like:
              - a prediction signal
              - a search method
              - an encryption function

  - rule gaps are created by trust (lack of enforcement in rules)

  - layers of rule gaps can form a possible exploit trajectory to achieve a malicious intent that seems legitimate at various points of validation

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

  - intent matching example:

    - "exploit requires that the user has recently visited a site with a TLS cert chained to an ECC-signed root certificate, since the root certificate must already be cached by the targeted system. If a targeted system doesn't have the root certificate cached, an attacker could still pull off an exploit by adding JavaScript that accesses a site chained to the root certificate."

    - intent of sending a request to another site:

      - retrieve info
        - execute function on info
        - display info

      - if there is no subsequently retrieved or already loaded code using the contents of that info, thats a signal that this info is being used for other intents that dont match the intents for visiting a web site (view info, interact with info)

      - the intent of sending a request to a site has sub-intents related to all the site's objects/attributes/types & their side effects
        - if a request has a side effect "caching info", that must be assumed to be a possible intent of the request, rather than more common explicit intents like displaying info


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
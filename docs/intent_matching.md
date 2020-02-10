## Intent matching

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
# Problem Source Identification


    - uses insight path technology, the interface nexus, object model, and semantic logic through dependency analysis


    1. key variable prediction with rules: 

        - if a bottle containing juice is the only thing someone drinks regularly and it makes them sick, how do you figure out that it's most probably bc of a chemical on the inner lining of the bottle, programmatically - ranking less probable causes as well

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


    2. key variable prediction with semantic logic iteration & alt state variable network with output intents:

        - "They measured performance in two southern Californian classrooms—one with big windows, one with small windows—and found that the kids with the bigger windows fared better, confirming [the researchers'] beliefs. But when they repeated the experiment in northern California, where it's cooler, big windows made no difference. It turned out that daylight didn't play a role in performance, but fresh air did—the classes in warmer southern California had their windows open."
        https://phys.org/news/2020-01-teens-climate.html

        1. Problem definition

          - problem type: "info asymmetry"

            - problem type metadata:

              - problem subtype:
                - "different outcomes for same action, where one outcome was successful, but not for difference hypothesized (sunlight)"

              - missing info (question), given the info asymmetry problem type:
                - hypothesis: "sunlight improves performance"
                - question: "which factors determine performance differences between rooms in different locations"
                  (given the implication of study, which is that "sunlight doesnt appear to improve performance on its own")

              - explicit info:
                - objects:
                  - windows
                  - rooms
                  - locations
                  - performance test
                  - sunlight
                  - test takers

              - retrievable info:
                - differences between locations:
                  - pollution exposure
                  - weather patterns (temperature)
                - definitions of objects, including intents

              - derivable info:
                - whether known interactions between objects can explain the metric difference, or if additional data is required
              
            - rules:

              - inputs:

                assumptions:
                  - "environment impacts performance"
                  - "sunlight impacts performance"

                observations:
                - rules in terms of hypothesis objects (assumption: "sunlight is relevant/explanatory"):
                  "performance metric increased with more sunlight in south rooms with big windows"
                  "performance metric did not increase with more sunlight in north rooms with big windows"
                - rules in terms with hypothesis objects removed (removes assumption that "sunlight is relevant/explanatory"):
                  "performance metric increased with more sunlight in south rooms with big windows"
                  "performance metric did not increase with more sunlight in north rooms with big windows"

              - outputs:

                interpretations:
                  - "location impacts performance"
                    - someone might expect different performance based on location alone, if school districts have different funding or nearby pollution sources
                    - however location isnt assumed as a causative factor but rather an interface with which to isolate the variables to be studied (sunlight)

                implications:
                  - "sunlight doesnt appear to improve performance on its own"

                contra-implications:
                  - "this doesnt mean sunlight isnt a factor at all"


          2. Relationship-finding vectors

            - iterate through object attributes/rules/types, evaluating them for possible distortions/states or other values that could definitively occur or possibly emerge naturally

              - window:
                - window object is a tool with multiple values for its position attribute: open/closed
                - window.position is a tool to serve various intents:
                  - temperature regulation
                  - pollution protection
                  - air dissipation
                  - wind route manipulation
                  - alternate to air conditioning systems

              - location:
                - location object is a place type with key differences in various attributes, like weather, ecology, population & industry
                - location.weather attribute differs in temperature attribute values
                  *** 
                  this should be flagged as a particularly interesting possible relationship, 
                    because it relates to attributes/rules of other objects already identified 
                    (window as tool of temperature regulation)
                  ***

              - room:
                - room object has an intent attribute with multiple values: "focus", "removal of distractions", "work alignment", "performance test"

              - student:
                - student object has multiple intents: 
                  - "maintain optimal conditions for focus"
                  - "maintain focus so you can remember information you studied"

              - "conditions" objects involved in student object intents should be flagged as a source of variance that can interact with other objects, which are environmental, and therefore it should be queried
              
              - condition:
                - condition objects with output intent "focus" include: "caffeine", "water supply", "electrolyte balance", "sleep", "quiet", "temperature regulation"
                  ***
                  temperature regulation should be flagged as particularly relevant, and store the possible relationship:
                    student.intents for metric "test performance" includes "maintain focus conditions"
                    conditions where intent = "focus" includes "temperature regulation"
                  ***

            - after iterating, you should have a list of the relevant object definitions (including intents, types, rules, alternate values, etc)

            - you should also now have the important attributes/rules with possible relationships, organized by their common factors, which may be sources of relevance:

              - temperature relationships:

                - window.position can be determined by temperature regulation intent
                - location differs by temperature in weather patterns
                - student.intents for activity = "test-taking" includes "maintain focus conditions"
                - conditions where intent = "focus" includes "temperature regulation"

            - deriving emergent relationships:
              - from this set of relationships organized by relationship factor, you can also derive emergent relationships by adding/removing/altering variable values & looking for anticipated state change points to see if theres a state change (governed by energy management patterns)


          3. Standardize variables by relationship metadata (directness, variance maximization, uncertainty)

            - given that you have at least one relevance factor to explore, standardize the relationships:

              - its determinable that the key potential sources of variance are:
                - naturally-determined environment conditions (location.weather)
                - artificially-determined focus conditions (window.position, room.temperature)

              I. logical variable reduction:

                - origin relationship:
                  location => weather => room => window => student => focus conditions => performance

                - you can remove the student object from the analysis, because we mainly care if the room & location.weather & window.position impact the focus conditions required for performance:
                  location => weather => room => window => focus conditions => performance

                - you can also remove the environment objects from the analysis, because we mainly care about the resulting variable attributes that could interact with focus conditions, leaving only the temperature attribute to link the weather, location, window, and focus conditions, since window, location & weather can be collapsed to variable attributes: sunlight & temperature

                  - temperature || sunlight => focus conditions => performance

                - you can further collapse the focus & performance into one variable:

                  - temperature || sunlight => focus conditions

                  - the reason we wouldnt choose to leave in performance over focus conditions is:
                    - focus conditions have a known direct link to performance (if its known, it shouldnt be included in data set, which should maximize variance)
                    - temperature & sunlight may have a direct link to focus conditions, and this direct link is measurable through attribute interactions
                    - the relationship between temperature & sunlight and performance is unknown and may not be explainable by this causal chain, but we're trying to explain it by proxy, through measuring the theorized relationship between temperature & sunlight and focus conditions, given that focus conditions are a key input of performance
                    - performance for a set of focus conditions can be checked after the temperature & sunlight => focus conditions relationship is established, since the focus conditions => performance relationship is known (or at least better understood)

                - out of the resulting reduced hypothesized relationship:
                  "temperature || sunlight => focus conditions"

                  we are determining if temperature or sunlight is the greater determining factor
                  (in this particular iteration of variable alts - excluding other variables like motivation/preparation and other temperature variable alts like air conditioning access, etc)
                  
                  - implicit causal shape assumptions:
                    - we are assuming they dont both influence performance
                    - we are also ignoring the small correlation between temperature & sunlight (cloudy days & nights can be hot, but sunlight is associated with higher temperature overall)
                    - we are checking for an isolated direct one-directional relationship, not a causal network or loop

                - you can also reduce alternate variable values explored to focus on those directly impacted by hypothesis objects

                  - leaving out alternate focus conditions that arent directly impacted by temperature like caffeine & quiet, 
                    although these arent entirely unrelated as caffeine may increase body temperature 
                    & a noisy environment may mean people are talking/moving more & that may increase room temperature

                  - in this study we're looking for direct relationships (causal adjacency) rather than indirect relationships
                
                - so if you use a semantic logic iteration through related object attributes, you only have to iterate through objects: location.weather, window.position, focus conditions
                - if you use a alternate state variable network, you only have to iterate through objects: temperature, sunlight, focus conditions


              II. identifying key output variable:

                1. collapse variable links with known mappings (focus conditions & performance => focus conditions)

                2. collapse variables having common output attribute into standard interface of that output attribute (window, room, location => temperature)

                3. dont collapse variables being studied as alternatives (keep sunlight & temperature separate, given that we are assuming one or the other is determinant)

                4. apply dependency analysis:

                  - without the right focus conditions, the impact of "location => weather => window => room => student" relationship doesnt matter because "student => brain => focus => pass test" relationship is not executable without focus conditions in place
                  - this can be determined by inputs of the "test object", where performance is known to be heavily influenced by focus conditions
                  - this means you can approach this problem from the reverse direction, iterating through focus conditions first & the impact of each variable & relationship on each condition
                
                  - if variables have similar variability or have common transformations explaining their variability (like taking one variable to the power of another variable), check if removing them alters output, otherwise they may be directly related rather than independent


              III. identifying key attributes providing interface to evaluate impact on output variable:

                - how could you automate the selection of the key attributes (sunlight, temperature) providing the best interface for comparison to evaluate impact on the output variable?

                - without using the prior method of dependency analysis & consolidation of known directly mapped variables, you can also identify relevant interfaces by:

                  1. the highest-variability attributes the objects (window, location, room) have in common: temperature, chemical exposure, radiation exposure

                    - then filter that list by which attributes are relevant to the hypothesis objects & available data

                      - temperature is derivable from hypothesis objects & data, but chemical & radiation exposure is not
                      - we dont know if windows have uv protection, if students rotated near window throughout test to distribute exposure, how much the sunlight increased room temperature, whether all tests occurred on sunny days, etc
                      - we do know what the temperature was in each combination of (window, room, location) states, or we can derive it based on intent (if a room is too hot and there is a window that can be opened, opening it can reduce temperature, which fulfills a focus condition of "temperature regulation") without even asking the schools if their windows were opened, although to be safe we should check that the windows could be opened, which is an assumption to this analysis that varied object attribute states (window.position) without verifying if they could be varied

                  2. the variables likeliest to cause disruptions in focus conditions (variable network hub variables, variables that are used in check/vary intents within focus condition functions)

                    - temperature can disrupt (and be disrupted by) various focus conditions: quiet, caffeine, electrolyte balance, water supply, temperature regulation
                      - so check if temperature can be calculated by other variables or a combination of variables

                  3. variable scope

                    - temperature impacts relationships on a molecular level
                    - focus is determined at a molecular & cellular level

                  4. system variable network position

                    - chemical system variable network has temperature in a hub position
                    - filtration, communication, immune, temperature regulation, & other systems also have temperature in a hub position
                    - input system (relating location, room, window) has an output variable network that interacts with bio system and chemical system

                  5. key rules

                    - energy is a key input/output of many physical systems (bio, chemical, environmental)
                    - temperature is a key factor in energy management (storage/flow)
                    - these rules are key hubs on rule networks because they determine many other rules

                
                Standard interface network analysis:

                  1. causal shape

                    - given that causal loops are generally more powerful than causal vectors, 
                      and temperature/sunlight are nodes in a causal loop, where sunlight/window/room/location all impact temperature, 
                      its likely that temperature is the determining factor, 
                      especially given that temperature also occupies causal shapes involving other relevant objects (caffeine, quiet, etc)

                  2. type

                    - variable type:

                      - given that temperature is a variable determined by & influencing many other variables, 
                      but that it condenses all of this information into a single point on a single spectrum variable, 
                      serving as a two-way bottleneck for aggregating information, 
                      it may be indexed as a variable of types: 
                        "filter", "information compressor"
                      which are particularly useful variables to use as interfaces

                  3. priority

                    - given that:

                      - temperature object has rules & attributes with stronger output priorities like "efficiency" & "path of least resistance"
                      - window object has strong output priorities "transport" (light) and "filter" (air)
                      - location has priority "differentiation => efficient gathering of resources by location environment conditions => efficiency"
                      - room has priority "focus condition maximization => test time reduction => efficiency"
                      - sunlight object has subcomponent objects like radiation with stronger output priorities like "distribution" than efficiency
                      - "efficiency" is a more common priority
                      
                      it may be hypothesized that temperature is the more useful variable to use as an interface


          4. Select & apply method of reducing possible relationships

            I. Method: Semantic logic iteration through related object attributes identified by relationship-finding vectors

              - iterate through those relationships for each relevance factor (temperature)

              - what order do you iterate through relationships for a relevance factor in?
                - you can start with objects having known differentiating factors 
                  (different locations were chosen for a reason, and the window is an important object in the hypothesis even with assumptions removed)

                - you can also approach from other known relationships, such as that performance is heavily influenced by focus conditions,
                  in which case youd iterate through focus conditions, and check which alternate states of the other objects could impact each focus condition

              - since location differs between samples:

                check if window.position can differ:
                if so, alternate window.position across locations:
                  check if alternate window.position achieves student.intents aligning with location object metadata: does opening the window achieve anything in south vs. north room?

                  iterate through possible intents of different window positions (temperature regulation, pollution protection, air dissipation, etc)
                  for each intent of window.position:

                    check if output intents of intent would differ across locations: would open windows have different output intents in north & south rooms?
                    yes, because of difference in weather patterns:
                      output intent of open window in hot south room = hot - hot = cool = "temperature regulation"
                      output intent of open window in cool north room = no difference in temperature regulation = cool - cool = "no temperature regulation"

                      given that window.position can serve intent "temperature regulation" across locations & temperature is the key relevance factor for this relationship set,
                      check if the different output intents have different impact on other possible relationships under 'temperature':

                      iterate through all remaining temperature relationships (if there are a lot, select for relationships involving known important factors like focus conditions first):

                          does output intent "temperature regulation" influence student.intents or condition.intents?

                          yes, it serves the students' "maintain focus conditions" intent, which is served by conditions with "temperature regulation" intent
                            (we could reduce this to just analyzing the condition.intent, since the student is aligned with this intent & doesnt add variance for the purposes of this study)

                            now that youve identified theres a logical flow between all relationships of a relevance factor (temperature), 
                            check if the implications of this logical flow match the observed rules:

                              implications for relevant variable variants (vary temperature):
                                - if room is in higher-temperature location, window can be opened to reduce temperature, which is a focus condition intent required by students' test-taking intents

                              does this match the observed rules:

                                - yes, this explains why the two locations had different outcomes for the same action - locations vary by temperature
                                  - output new theory: "temperature determines performance differences because focus conditions require temperature regulation, which is enabled by window.position changes in high-temperature locations"

                                - no, continue iteration

            II. Alternate state variable network

              - you can also generate a network of alternate variable values among variables suspected to be relevant & check for output intents, 
                rather than narrowing down relationship sets with semantic logic conditions between objects like variables & intents

                - what are the output intents of the vectors: 

                  [window = open, location = north, weather = storm, sunlight = low, quiet = low]
                    - output intent: "contradicts focus conditions = 'quiet'"

                  [window = closed, location = north, weather = hot, sunlight = high, caffeine = high, sleep = low]
                    - output intent: "contradicts focus conditions = 'sleep', 'temperature regulation'"

                  [window = open, location = south, weather = hot, sunlight = high, caffeine = high]
                    - output intent: "serves focus conditions = 'caffeine', 'temperature regulation'"

                - now you can answer the question:
                    - "which of these vectors serve/maximize the key variable 'focus conditions'?"

              - visuals to visualize a alternate variable state network:
                - you can assign a radius to each variable, where possible variable values have different positions on the resulting variable circle
                - the output intents would be outside the last variable circle, and would have an attribute (color/direction) indicating output intent value:
                  (negative, neutral, positive impact on focus conditions)
                - the goal is to arrange & navigate the variable circles toward the target output intent to optimize some metric (least number of steps, most independent variables, etc)

              - if you pick the right starting variable for the vector's first item, you can reduce the trajectories required in your network of possible variable value combinations
              
              - radiate outward from origin variable node by assigning vector position by variability (high variance attributes come first in vector determining output path in network)

              - first filter vectors by which are possible, if data is available, or to explore alternate conditions (if windows are not openable because students are too short to reach and if teacher wont open it for them)
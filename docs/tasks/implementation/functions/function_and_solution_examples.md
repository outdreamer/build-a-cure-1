# Examples

	- more examples of applied analysis

## example of conceptual math: 
      - calculating structure of a concept definition
      - determining structure that a concept takes in a context
      - a concept applied to/injected in another concept
      - identifying concepts in a context & their corresponding values in another context
    
## example of interface query:
      - which interface to start from or end at, in what sequence (start from system interface, stop at pattern interface, aim for math interface)
      - which interfaces to embed/apply to which interfaces (apply trust to the information interface, embed power in the cause interface)

## interface query targets

    - direction of math-structure query:
      - finding shapes that are useful for a context
      - finding contexts that are relevant to a shape

     - function fitting a context, context fitting a function, causal structure fitting a function, errors or missing information fitting a function, tests determining a function

## example filter analysis

      - problem: design/select optimal options for a program
        - apply filter: reduce solution space by options that are possible (set of variables)
          - apply filter: reduce solution space by options that users would want to change (which options to include)
            - apply filter: reduce solution space by options that users would be willing to learn
              - apply filter: reduce solution space by options that devs are willing to maintain
                - apply filter: reduce solution space by options that comply with configuration patterns (option usage, like the number of buttons normally forming a set of alternatives, reducing learning time)

        - alternate filter set to produce the optimal design of a configuration set
          - apply filter: which options are likeliest to change (identifiers, free text fields, etc)
            - apply filter: which options are likeliest to capture information (type attribute captures a lot of information)

        - these filter sets may produce the same answer, but one is more efficient than the other

## deriving missing info with patterns & concepts

    - when you have one sample, it's possible to estimate distance from average using extreme attribute value sets & mapping the attribute sets to assign probability given the relationships within the sample, as a prediction tool with minimum information

      - example: if you're in a position and you want to know if its an average or extreme position, you can: 

        - maximize attribute values 
          (maximize elevation after deriving the concepts of ground & relative height and noticing that height can change between positions, maximize horizon landmarks, maximize connections between nodes, maximize variation within node sets), 
        - to imagine other possible positions (a place with more landmarks, more variation in elevation, etc) 
        - and then all the possible adjacent positions (places that would be found near each other or places that would turn into each other), 
        - to derive paths in the system of attribute sets indicating positions, 
        - then assign probability between sets (places that are likelier, given attribute relationships in your position like how neighborhoods cluster and how that clustering rule might be causative/caused by the attribute sets), 
        - then identify the most probable positions as nearer to the average & identify other measures of average, and identify combinations that can create the average (other routes to the average) 

        - then identify the least likely or most extreme positions and take the average from distance to those or distance to probable positions

        - the most variation there can be seen when applying concepts like agency (planned cities or artificial natural landmarks), concepts which can be derived from the attribute values of your position

        - anything that's not required or can be transformed in some way is a candidate for a variable
          - anything that doesnt have a point/intent is not as likely to be a variable, bc things usually change for a reason but universal change laws can still produce changes without intent

        - some attribute values would be non-adjacent to derive from other positions, but become more adjacent to derive once other linking concepts/attributes are derived:
          - deriving the concept of an island from a landlocked position would be difficult without the concepts of a lake or a boundary, moat, container, limit, or anomaly
          - deriving the concept of a cave without seeing one would require assumptions of non-uniformity, or concepts like gaps or scaffolds, or understanding of structural physics allowing cave ceiling to be supported without a full structure underneath 
          
        - how would you derive the concepts that could illuminate the most alternate structures created by intersecting/aligning attribute values:
          - core structure analysis & assumption permutation would get there the fastest without system filters (attribute alignments, unenforced rules) or intent analysis (focusing on structures with a point)
          - deriving links between known objects
            - linking the concept of water and the concept of land requires deriving the concept of a shore, which would lead to the repeated compounding interaction between water & rock leading to erosion & caves
            - or alternately linking the core structure of layers to derive earth plates, & assuming they can change position, leading to earthquakes, leading to gaps in rock structures)
          - identifying the cause of the object (natural landmarks) variation as on the element layer & deriving those relationships given your position's attribute values, then assuming different element distributions & combinations to build the landmarks up from that layer
          
        - assuming time independence - not assuming to be at a state of development that would guarantee a likely possibility is manifested somewhere


## prediction of missing vars example

      - with titanic data set, a missing variable would be 'mental state' to include states like 'shock', which could be a cause of death in that situation

        - how do you predict the existence of a mental state like that which could influence passenger survival? there are many routes, such as:

          - using the difference in age of passenger as an important prediction variable & pulling the definition
            - then deriving that the reason the age is logged at all is because different mental functions are acquired at different times (an embedded time parameterized variable)
            - from the difference in mental functions with respect to time, derive that mental states can develop which are influential in decisions, a key object of survival
            - once you know that mental states differ and can predict survival, you can identify different mental states that would directly impact survival (loss of motor control, which is a core function of the brain-body connection, linking mental state to mental decisions to physical actions), and filter that list by which mental states are likely due to probable emotions & other mental objects in that context

            - the key objects to identify:

              - mental state

                - mental state types (lack of focus or diverted focus, impact of emotions like fear such as a state of shock, etc)

              - mental function

                - decisions
                  - mental decisions
                  - implementations of those mental decisions (physical actions)

                - plans
                  - attempted unsuccessful decision implementations can be the result of bad planning (planning being a mental function), which can be another influential factor in survival

                - connections between mental objects (decisions, plans, strategies, insights, intents, priorities) & attempts/implementations/actions (physical output of decisions & other mental objects)

          - another way to derive the mental state variable as an important predictor:

            - a concept of dysfunction would be able to identify a lack of correct functioning in original objects of the data set

              - dysfunctional health is associated with the age variable

              - dysfunctional mental health is also associated with the age variable and inferrable from the dysfunctional health state

              - lack of functioning across mental objects is derivable from that conclusion, with a default input of mental objects

          - another way is using system filters or other interfaces

            - a concept of control would be default to the agent interface (agents have agency/independence)
            - this concept can be used to form questions like 'do passenger agents have the option of decisions in this situation'
            - the source of their control isnt important, unless you have data about injuries (like a concussion impacting their mental function)
            - applying the concept of control accessible to agents would be a possible explanation for differences in the data set - some passengers have more control than others
            - from this concept, mental functions (strategies + perspective + problem + priorities = plan) & objects (functions => rules => strategies) can be inferred

        - another missing variable is variation within variables across attribute values, such as gender/age

          - by identifying the unenforced rules in gender roles (component object of gender variable)
            - then identifying the stressor set that could trigger fulfillment of different gender roles
            - you could predict the existence of a passenger that survives bc of permuted gender role (woman with useful skills from being given tasks for men may survive at higher than average rate)

          - you could also predict the concept of a 'protection policy' by pulling contemporary definitions of gender roles, noting that women & children are 'protected/useless', and men are 'protecting useful' role
            - this definition would help predict the existence of a policy to save women & children first
            - the contemporary state of tech necessitates a policy like that rather than a protocol to use tech to signal for help in case of an accident, with an accident protocol designed based on precedents & bio understanding
            - protected groups would be routed to safety-generating resources like lifeboats first
            - example inferred passenger types with inferred objects like protection policy:
              - a woman who was not protected might be in a different survival group if she had prior knowledge of sailing/accident protocol or knowledge of nearby landmarks to swim to
              - a woman who was protected might not survive for other reasons (due to mental state values like senile/in shock)

        - identifying different causes of data corruption error

          - different reasons for errors might have a different impact on the prediction function, which can often be identified

            - a cause of 'logging error' in logging the wrong value for a variable would have a high probability of causing error, if there are no data validation rules (logging passengers' attributes was checked many times)
            - a cause of 'identification error' in logging the wrong value because a variable value was ambiguous (age or gender was not determinable and was logged incorrectly from this misidentification) would change the probability of error
            - a cause of 'trusting logging errors' in trusting an error made at initial log time (the log was never checked) would have a high probability of causing error but a presence of trusted logs in the process wouldnt change the probability of error added by the logging process, while a lack of trusted logs would change the probability
            
            - these causes have different probabilities & different impact on the actual vs. the average error set, in the error interaction space

        - this method works in the absence of these objects already identified as important or already defined

        - this method works when definitions are detectable (finding adjacent attributes & probable set of required functions relevant to an object given interaction probability to assemble its definition)


## example of math-structure query:

      - lets say you want to design a game with a particularly high level of complexity to make it interesting (an attribute of games)

        - how could you query the math interface to use patterns of math structures to automate the game design to create complexity?
          
          - define objects like complexity within the context as 'maximize options' or 'maximize possible routes to a game outcome'
          
          - one parameter of the game is interface points (such as starting/ending/goal points - like the basket in basketball or the holes in golf - where game level/points/wins/remaining possible moves are determined by interaction with those points)

          - increasing that parameter would add more complexity (more ways to score points), but you can only fit so many on the board 
            - how many points do you choose, given that some values of this parameter will make the game impossible, boring, a test of luck rather than skill, remove luck completely making it predetermined, make the game have emergent effects you arent aiming for, etc
          
          - math structures can be used to calculate game-specific concepts like intersection probability
            - example: 
              - on a poker table, the likelihood of a collision can be calculated using the rectangle shape & sphere shape dynamics, where the middle two holes add complexity to the game
              - if one shape has more possible intersections of components than another shape, that would add to the complexity metric, without having to find that shape or think about it manually

          - other ways to increase complexity include making sure:

            - every position/state/outcome has many different possible routes to get there 
              (structural query: many paths across the board can result in a position/state/outcome)

            - a low ratio of game iterations with a high ratio of irreversible potential-decreasing moves that determine the game at an early stage 
              (structural query: very few paths from origin to win state have a few number of steps)

            - applying extra distortion/combination functions to move calculations results in more possible ways to win a given iteration 
              (structural query: more combinations of step inputs/components or steps produce more paths from origin to win state)

            - many moves, many routes, and many move functions or components are optimized in the above metrics, which all add options to the game structure, increasing complexity
            - you could produce that set of structural targets & their queries to optimize complexity, by looking for routes to optimize the number of objects (strategies, moves, move functions, move components), possible combinations (routes, states, wins) in the game structure

      - this is a simple example where the problem space is already mapped to structure (shape of a game board) so no conversion is necessary to transform it into the structural interface, and no attribute subsets are queried for in the math interface, except the shape subset, which is a determining subset that doesnt usually come with other attributes (a game board doesnt always have other determining attributes like texture, the shape is usually what matters)


## testing for independent variables

      - a slice of a bottleneck (filter and/or limit applied that enforces interaction, like a type) may include enough random independent variables to generate a normal distribution of a dependent variable, if a series of variance gaps in a system has alignment (similar direction moving toward the bottleneck), where the bottleneck forces the variables to interact in a way that doesnt enforce similarity/convergence of the variables (leaves open the possibility of coordinating/cooperative differences)

      - example: 
        - a subset (out of the total observed outcome set) is likelier to contain a proportional number of successes (subset size/total size) than all the successes
        - just like a subset is likelier to contain one success than zero if subsets have size 1 and the observed outcome set has the same size as the possible outcome set
        - this means the outcomes are likelier to be distributed across subsets organized by adjacence than concentrated in one subset, as the subset size decreases
        - as the likelihood of a multi-subset observed outcome distribution increases, the likelihood of a convergence to the average increases 
          - 1,2 and 5,6 are in more different subsets organized by adjacence
          - adjacence is a good determinant of subsets because we're measuring difference compared to the average, and adjacence measures difference
          - the average of 1, 2, 5, 6, is nearer to the average than the average of 1, 2, 3, 4 or 3, 4, 5, 6 (which are more adjacent than 1, 2, 5, 6 even though theyre in different subsets)
          - the subset (1, extreme value) is likelier than (1, adjacent value) (there are more ways to pair 1 with an extreme value than an adjacent value bc its on the edge)
          - the likelihood of pairing a value with its non-averaging value (1 being the averaging value of 6, 2 being the averaging value of 5) is higher than pairing a value with its averaging value
          - the likelihood of pairing a value with adjacent values (pairing 1 with 4 or 5) to its non-averaging value than with adjacent values to itself (pairing 1 with 2 or 3) contributes to the convergence towards the average (pairing 1 with 4, 5, or 6 is likelier than pairing 1 with 2 or 3 and contributes more to the convergence toward the average)
          - the likelihood of pairing a value with non-adjacent values is higher than pairing it with adjacent values (if the possible outcome size is greater than 5)
          - are there more or less subsets that would produce an average closer to the original distribution average value? if the set of possible outcomes has a large size, there are more possible outcomes that would produce an average in the set of outcomes farther away from the mean (if the outcomes can be 1 - 10, there are more non-5 outcomes than 5 outcomes, so the average of paired subsets are likelier to converge to the distribution average 5, because you can pair 1 with 10 and other very non-average values (2, 3, 8, 9) in more equally possible ways than you can pair 1 with 5 or average-adjacent values (4, 5, 6, 7) because there are more very non-average values

        - subsets are a key object because the sum (implying 'of multiple numbers') is a component of the average - an average takes more than one observation to calculate, and the average is a standard to measure the relationship of one outcome value to the set of all observed outcome values, given adjacence to the average, an average giving more information in one number than either endpoint
          - subsets are the core unit structure containing the implementation of the concept of difference (& enabling the sum/average requirements) in this problem

        - so the direction moves toward the average with more fulfillments of variance gaps in the form of unenforced convergence, where differences are allowed to develop & coordinate
        
        - another quicker way to generate this conclusion is how there are more adjacent similar ways to generate an average value than an extreme value for most outcome subsets
          - there are fewer different steps required to transform a given outcome subsets 1,2 and 5,6 to the average (converge to the value that is most similar to all other values) than to the extremes, given that the extremes are likelier to be farther away from factors that can be used to generate them (likelier to be prime), given that outcome numbers are the product of different routes between other numbers

        - the slice structure indicates that the independent variables are being measured in a similar way or similar time, where conditions are held constant during the measurement (the outcomes and subsets are assumed to be relevant to each other, being organized into the same experiment's total outcome set)

        - each outcome isn't required to converge or coordinate with the other outcomes (independence), like with the independence of closed non-adjacent systems with minimal or no enforced interaction between systems

        - the limit being applied is the assumption of relevance of outcomes within an experimental total outcome set

        - the filter is the standard applied (average), which standardizes to an interface that allows comparison between independent variables

        - the variance gaps (unenforced rules, given that subsets aren't assumed to be dependent, so there's no default required reason for them to relate to any value) are the probability of different subsets to create an average near to the total set average, which converges to the total set average

      - given that the ratio of area contributed by a subset can be calculated by the degrees away from the equal distribution that the parameters (sample size, subset size) have moved it, does the area calculation of a subset of the final curved distribution get clearer as a function of degrees?

        - the ratio of area contributed by x = 1 through x = 3 of a normal distribution can be calculated by the degrees of steps taken away from default parameters for the equal distribution, separating the continuous curve of changes into a sequence of steps from the angular versions in between the line of the equal distribution and the continuous curve

        - other way to frame the question: is the area of the final curved distribution contributed by x = 1 through 2 faster to calculate if you know the area contributed by that subset for the previous less curved function & the transform function from the previous curved function to the final curved function, or faster with a standard integral calculation

        - another way to frame the original problem ('why does the average of many random independent variables produce a normal outcome probability distribution)
          - why is the average of a set of constant probability lines likelier to be curved & closer to the absolute average than not, as the number of constant probability lines applied increases? 
          - why does an average of constant probabilities across possible outcomes lead to a probability curve with central tendency similar to a parabola
          - the curvature is from similarities in probabilities between similar values (1.2 is similar in probability to 1.3, so they are connected with a small change in value, leading to a curve when applied across other adjacent/similar values) and from the continuity of possible values (1.2 is a possible outcome rather than just integers)
          - similarity across probabilities (similar probabilities of getting 1.2 and 1.3 as an average) and values (similarity of 1.2 and 1.3) is a symmetry that you could identify programmatically to predict the output shape of the distribution 
            - or identify the same contrary conclusion leading to an inevitable implication, which is that it is very unlikely to get a gap in the final distribution where some values are never seen regardless of how many variables are used, or that a large jump in probability occurs between very similar values
              - meaning there's a closed relationship between the parameters (outcome averages, possible outcome size, adjacence of possible outcome values, number of variables, & converging probability)

          - when there is a large difference in outcome between similar inputs (volatility in probability of 1 and 3, which are similar in a set of outcomes from 1 - 6), there are other parameters contributing to the outcome probabilities (similar to how being an endpoint value decreases the possibility of being paired in a subset with adjacent values)

            - how would you identify these parameters adding volatility? by checking default system filter objects:

              - differences

                - in structure (subsets)

                  - in content filling structures (values in subsets)

              - existing known objects of the problem (or existing known objects defined in terms of the same object, like 'average')

                - extremes

                  - differences (start with 'differences' query above)

                - averages

                  - pairs are the unit input to the sum/average
                    - the importance of subsets as a fundamental input to the concept of the sum/average
                  - the concept of value pairs that can produce an absolute average-adjacent value
                    - averaging pairs
                    - generalization to the concept of value subsets producing an average
                      - averaging subsets
                      - the concept of ambiguity subsets producing an average
                        - indistinguishable averaging subsets
                  - there are fewer averaging values for extremes than for average-adjacent values (1 can be averaged by values near 5 - 6, whereas 3 can be averaged by values near 2 - 4)
                  - erasure of extremes
                    - ambiguity between subsets (1 and 5 generating the same average as 2 and 4)
                      - the average is determined by ambiguities (in how many different subsets can be used to generate a particular average)
                  - the importance of the average as an input to the concept of probability
                  - each subset of values is likely to have an average similar to the absolute average, based on:
                    - the number of ambiguous routes to the average possible in that subset, across value pairs/subsets 
                      (a subset from 1 to 6 includes 3 distinct pairs of values that can produce the absolute average of 3)
                    - the number of non-average values
                    - the number of adjacent values that are non-averages and non-averaging
                  - the proportion of ambiguities increases as size n increases

                - independence

                  - one input to the average doesn't influence other inputs to the average
                    - adjacence within a value pair as a contrary force to the average
                    - the full set of adjacent inputs has inequality in distribution (1 has fewer adjacent inputs than 2)

                - random (distribution for each variable)

                  - each possible outcome value is equally likely
                  - each average outcome value is likelier to be similar or equal to the average possible value than another value
                  - when permuting the concept of similarity, do averages change in behavior? (start with 'independence' query generating 'adjacence' concept and 'adjacent pairs' inequality or 'adjacence' query)

              - derived objects that are relevant to the system 

                - after you vectorize the problem (fit it to a function structure with direction from input to output), some of the relationships with derived objects is:
                  - variables => subsets => adjacence of subsets => sum => average => outcome probabilities
                  - variables => extremes or opposites => sum => average => outcome probabilities

                - opposite

                  - values on opposite sides of the average are likelier to have an averaging effect on each other than not
                    - 4 through 6 are averaging for 1, whereas 3 doesnt move 1 closer to 3 than other numbers ((5 + 1)/2 and (6 + 1)/2 are closer to 3 compared to 1, than (1 + numbers lower than 3)/2 are closer to 3 compared to 1) - opposite side values have an impact that increases the similarity to 3 as opposed to the non-opposite side values which dont measurably increase the similarity to 3 compared to the original value (1 + 2)/2 = 1.5, where 1.5 is more similar to 1 than it is to the average 3
                      - the threshold for similarity of the average of a pair to the average or to an extreme input is another attribute differentiating the impact of pairs on the final outcome set average

                - adjacence

                  - adjacence between outcome values can be a factor in the average of that subset, depending on the proportion of adjacent subsets and the averaging effect of pairs of these adjacent subsets


            - given the input problem objects:
              - average
              - sum
              - value
              - set

            - now you have a set of important objects for this problem (not all of which are necessary for a given solution, selected from standard/permuted/combined system objects):
              - subsets
              - extremes
              - opposites
              - thresholds
              - equivalence
                - similarity/adjacence
              - ambiguities
              - alternates

            - and these objects can generate the significant derived objects when combined with problem objects

              - averaging subsets (2,4)
                - ambiguous averaging subsets (2,4 and 1,5 and 1,5,3)
              - adjacent subsets (1,2)
              - averaging thresholds (the point where opposite values start moving an extreme closer to the average than adjacent values move the extreme so it doesnt reduce the distance to the average by more than a factor)

            - these derived objects enable evaluating the problem in a structural way that predicts the outcome under computation constraints (not actually calculating the answer)

    - when applying ambiguity reduction to a problem like 'finding the parameters of the curve', find vertexes to begin search at by filtering:

      - having a related contrary set (if the vertex is not the parameter, the other values in the set will also not be)
      - having equidistance to other vertices, measured by numbers/size of contrary sets (each vertex is n unit contrary sets away from other vertices)
      - minimizing number of test steps (triviality of invalidating the vertex & its contrary set)
      - mapping sequence of vertices to test by which contrary sets invalidate which other contrary sets (so only contrary sets with ambiguity in the form of undetermined contrary sets are competing)
      - subsets optimizing an attribute (number types, number differences, etc) associated with variation across parameters (ensuring subsets have variation within contrary sets optimizing these attributes to find other patterns in parameters)
        - ensuring subsets have different organizing attributes
          - ensuring subsets are organized in a way that will allow useful organizing attributes to be found early, without violating contrary set & invalidating parameter set organization & other filters
      - which parameter values will invalidate other parameter values (if a parameter has to be x steps away from another parameter value, make sure invalidating sample parameters aren't checked within a subset
      - which distortions will isolate or reduce possible parameters or parameter relationships, so fewer filters can be used (maximizing some metric, framing it as a combination of different components, etc)

      - objects include:
        - filters to search one parameter
        - filters to search parameter sets
        - invalidating parameter sets (if x is not 1, y is not 2)
        - contrary sets (if x is not 1, it is also not 2)
          - the other version is alternative sets (if x is not 1, 2 or 3 are not ruled out)
        - filters to determine filters (rule out sets or paths in a network of sets)
        - organizing filters by maximum probability of related subsets being adjacent, or maximum probability of variation once filters are applied (once x subsets are ruled out, the remaining subsets are likely to be very different)
        - compounding/probable sets (if x is not 1, it is less likely to be 2)
        - interacting sets (if x is not 1 and x is not 2, it is also not 3)
        - set variation
        - set organization
        - set traversal sequence
        - ambiguity maximization, across set traversal sequence

        - how would you identify the best tests to do to reduce solution space?
          - after modeling the likely set of distributions, and identifying which tests reduce uncertainty the most in those distributions, selecting for the most common tests across distributions that reduce uncertainty


  - most variables can be converted into one that has a normal distribution by injecting a symmetry or adding interactions from different enough sources that it generates randomness

  - why are randomness & symmetry often found together, like with the central limit theorem or circles? 

    - because symmetries are a default object that develop in complex systems on top of efficiencies, and growth on those symmetries is random (undirected) because symmetries dont typically come with default filters/limits directing the output

    - the normal distribution would likely be generated by a set of subsets where each subset has most of its values in the 1 standard deviation range and a few outliers in either or both directions

      - theres some variation in the subsets, which could include other patterns in small quantities that dont influence the average

      - why would 'most values in the 1 standard deviation range + a few outliers' be the standard or most common pattern in random independent variables?

      - this involves random independent variables like dice 1 outcome & dice 2 outcome - meaning the common pattern takes the form of most values in the 3 - 4 range, and a few values in the 1-2 and 5-6 range

      - given the commonness of that pattern, it can be interpreted as a default state of the dice probability distribution, where other patterns are distortions of that default

      - that common pattern has a hard limit placed on the central values 3 - 4, and the set of values that are outliers are less limited (can be 1 - 2 or 5 - 6 or a combination) - it requires some central values, but the outlier values are more flexible

      - the alternate version of that common pattern is that 'the proportion of 5/6 values relative to the proportion of 1/2 values will be equal (the sides of the curve are similar in shape), and the proportion of 3/4 values will be greater than those outlier values'

      - randomness means 'lack of influence or direction' in this case, which translates to 'lack of default similarity in adjacent outcomes', removing the normal semantic value of position

      - this means in a large sample with random selection, that a sequence of different values is likelier than a sequence of the same value

      - the 3/4 set is different from the 1/2 set and the 5/6 set

      - this means the 3/4 set is likelier to appear with the 1/2 set and the 5/6 set (same relationship applied to the interim sets, 2/5, in relation to the extreme outlier sets 1/6)

      - given the ratio of the outliers in the set of 1 - 6 (4/6), the likelihood that the average set (3 & 4) will provide the most difference from the previous value in set type is higher than the likelihood that another outlier will provide the most difference from the previous value in the set type metric (average, interim, extreme set types)

      - this implies the dynamic is more of a circle shape than a spectrum, where the pairs of adjacent values in a random sequence occupy points in a circle and the central tendency holds (pairs are likelier to include a 3/4 than other values, pairs are less likely to include two consecutive extreme values like 1/6)

      - analyzing adjacent pairs as the important objects is more useful than analyzing individual outcomes in isolation

      - random can also mean 'difference is default' - difference in this case represents the efficiency, and the distortions from that efficiency represent the outlier values

      - so in random functions, given the definition of random, there are biases rewarding:
        - difference between adjacent values (only 1/6 probability of the next value being the same value, and 2/6 (1 and 6) values have only a 1/6 probability of the next value being one unit away) if the number of possibilities is greater than 2
        - similarity to default/efficient value
        - difference in set type (average vs. extreme)
        - compliance with common patterns (like 'many symmetry origin values (like an average) plus few extreme/different values')

        which favors difference (given the concepts of limits which have limited directions of difference, averages which have more limited difference degrees, difference types (extreme vs. average), difference in probability of various adjacent pairs, & the number of options), even though the difference is not enforced (theres no rule guaranteeing the next value will be different or a specific degree of difference)

      - violation of randomness about a symmetry:

        - a random variable will change if another symmetry is adjacent enough to exert gravity on the variable, at which point the random variable will conver to & be distorted around the new symmetry

          - if a fly gravitates around one light but in their random motion, they encounter the edge of the light's reach, and another light is more nearby at that limit point than the original light, they may gravitate toward the new light - same with symmetries that are sufficiently adjacent as to be nearer to another symmetry's limit than the original symmetry's radius 

            - factors include if lights are likely to be evenly distributed, if they have different radii, if they have different types of light, etc

          - the corresponding example with the dice includes factors like:
            - people who use dice often happen to buy magnets (or magnetic material is often used in building/furniture construction)
            - the dice contain metal that responds to that charge 
            - the charge is strong enough to exert a force if the dice are thrown near enough to those objects (standing near a wall or sitting on furniture)
            - people arent careful to remove magnetic material from the experiment location

          - this is an object called an 'efficiency/symmetry overlap', where radii (or the equivalent semantic object) provide an intersection between symmetries
          
          - this either must not happen much in nature, or the overlap isnt usually enough to cause more than a few outliers, or these trends arent often described

      - how would you generate an independent variable? 

        - for example, how would you generate a high degree of randomness in the compounds that your bio system encounters?

        - youd make sure to interact with many different objects (like plants, locations, and experiments combining other objects) 

        - youd seek out differences, and try to eliminate certainties & their patterns

        - the way you would seek out differences & eliminate certainties would probably not be random - it would be normally distributed - youd try one interaction for a while, then move on to another interaction within a similar range of difference, and the final output would gravitate toward an average, since different compounds are usually different to test out variable combinations or because of local/conditional optimality, rather than because theyre known to be absolutely optimal by nature, and the average is often the most stable & therefore the most efficient state, given that very different values are unlikely to coordinate with all other system objects as well as the average does given its commonness, which implies that functions to handle it already exist

        - so stability often develops from aggregating many sources of difference, around the sets that offer the most difference in set type (default/efficient/common/average vs. extreme/conditional type) and the least difference in value (1/3 and 4/6 rather than 1/6 and 2/5) because of efficiency/commonness/stability, which may as well be proxy variables for each other in this context

      - a ratio of randomness is allowed in nature because the rules limiting interactions are finite

    - why do symmetries evolve in complex systems? so that differences can develop/stack within the symmetry range, leading to more differences when those differences interact with differences from other symmetries


## intent analysis computation example: function design for a particular intent

      - example for selecting bernoulli function as a parameter to embed other difference-maximizing sigmoid-scaled regression functions into, in order to find an error-minimizing function:

        - embedding difference-maximizing sigmoid-scaled regression functions into the bernoulli distribution for each xi/yi pair produces the cross-entropy loss function:

            - https://towardsdatascience.com/the-statistical-foundations-of-machine-learning-973c356a95f

            - given the classifier modeling function generating each yi from xi, which for fitting a function for linear regression is:
                o(ax + b), where o(t) is a sigmoid function to differentiate outcomes
              
              for the probability of E given p above with the binomial distribution function (bernoulli case) 
                p^(p occurrences) * (1 - p)^(not-p occurrences)

              framing it instead as the probability of yi given xi,
                f(xi)^(yi) * (1 - f(xi))^(1 - yi)

              then substituting the classifier modeling function for f(xi),
                o(ax + b)^(yi) * (1 - o(ax + b))^(1 - yi)

              then apply the log to find the maximum of the function

      - the reason for applying the bernoulli distribution for each x & y pair is not-determined, whereas the reason for applying the log is determined (calculate maximum)

        - meaning there are other ways to map each xi to yi than by:

          - mapping number of occurrences of an outcome => yi
          - mapping likelihood of an outcome => function applied to xi

        - so why use this specific function to model xi & yi?

          p(E|p) = p    ^(p occurrences) * (1 - p)    ^(not-p occurrences)

          p(yi | f(xi) = f(xi)^(yi)            * (1 - f(xi))^(1 - yi)

          p (probability of event 'TTH' | probability of 'H' 0.3) = 0.3 ^ (H occurrences) * 0.7 ^ (not H occurrences)

          p (probability of event yi | f(xi)) = f(xi) ^ (yi) * (1 - f(xi) ^ (1 - yi)

          = the likelihood of getting outcome yi, given the connection function f(xi) = connection function ^ outcome * (1 - not connection function) ^ (1 - outcome)

        - we're treating this as a conditional probability problem, where we want to find the success of a predictor f(xi) on an outcome yi, so f(xi) is treated as a proportion that can predict the outcome

        - other models like Bayesian probability would fit their functions of p(B|A) as probability of (yi given f(xi)), or some parameter/parameter set/component of f(xi)

        - so the above example uses the sigmoid-scaled linear function (maximizing differences to aggregate values near 0 or 1), by injecting it into the bernouill model (which is appropriate for estimating probabilities of boolean outcomes 1/0) in the position of a predictor, applying it to each data point & summing the outputs, wrapping it in the structure of a general error-calculation function

        - this is why this set of operations done to these functions can produce a loss function for estimating error of a classifier


## example of system analysis standardization in a problem space like markets

  - what is the correct position of a market, insurance, price, future value predictions, trades, currencies, etc given their definitions?
      - a market being a reason to trade unevenly distributed resources, like matching supply & demand
      - insurance being the allocation of risk

## example definition route of symmetry (same regardless of a transform & transform direction):

    - structural definition:
      - when energy gathers into a state that is easier to create than to destroy (when it uses efficiencies & shortcuts)
      - when the boundary formed is stronger than the energy contained in it
      - when information leaves traces/side effects that are not erased by reversing the transform (not a closed system with energy storage built in)
      - example of processes that are easier in one direction: it can be easier to navigate over a local maxima than to navigate up a global valley, or to navigate a map to identify type than a map to identify individual members of a type, which can change in ways that differ from the type definition, average, etc


## example of applying definitions to find important concepts

    - finding value in random sequence

      - implementation of random definition, including error types & output probability distribution
      - index of randomly generated data, iteratively checked for matches of adjacent or low-cost accessible subsets
      - subset hashing

## system object: 

	- false difference

	    - some weapons seem dangerous but are mostly only usable in certain contexts which are easily avoidable
	    
	      - deep fake tech is mostly used for criminal intents in the context of 'convincing a stupid person to vote for a corrupt candidate', though they can be used in other criminal contexts like 'revenge' or 'mocking a video of a hostage to secure payment' or 'deep fake porn' - all contexts which are avoidable with various technologies

	- false correlation example:

	    - false correlation between two functions:
	      - parabola representing position from origin around a circle
	      - linear function with positive slope representing change rate of motion around circle
	    - the first half would seem correlated, the second half would not - it would seem like a false correlation
	    - the two variables are related because of the shape they are describing motion around, but not causative of each other unless there are other factors involved like a compounding force/momentum
	    - but if you just looked at the first half of the functions, it would look like a similarity

	    - how to generate the list of change types to check for when looking for minimum information like pivot points or vertices that could contradict the apparent correlation:
	      - find attributes of the change type (inflection point or change in direction at the top of the parabola is a significant factor)
	      - find standardized format (compare change rate of the parabola to the linear function which already represents a change rate - which would identify a slowing of the change rate in the parabola that indicates a limit or inflection point)
	      - apply change patterns (a curve like the first half of a parabola doesnt normally just drop back to a position of zero after its change rate slows down)

	- base object or foundation layer

	  - whats the best base object for building a prediction function:
	    - constant/tangent subset functions (like a tangent at a maximum of length 1)
	    - averages/differences
	    - adjacent functions
	    - probabilities/patterns
	    - filters

	    - adjacent/tangent subset functions, where deactivated nodes function as:
	      - the subset functions that couldnt be transformed to components of the actual prediction function without a forced value intervention
	      - transformation functions (or their parameters/values like direction) that didnt convert adjacent subset functions to components of the prediction function

	    - filter functions, where:
	      - the likeliest limits narrowing down a solution space into a function are successively selected & applied in subsets
	      - likeliest vertices determining/generating a function are applied in subsets 
	        - test that change is slowing which means approaching a limit or an inflection point, and check for enough vertex points past the possible pivot point to confirm which one
	      - the likeliest changes/types are applied in subsets
	        - slow change is likelier to follow slow change, direction change likelier to follow stabilization of curve


## example of deriving an alternate method

    - how would you determine how to use matrix multiplication to solve systems of linear equations, without knowing matrix multiplication?

      - use common function in solutions: organization
      - apply that function to inputs (disorganized info) using a common definition of organization (order)
      - what changes across functions that could benefit from being ordered? variable position
      - once ordered, what has been added? standardization of variable position
      - whats missing for full standardization of position? coefficients with value zero, which adds the information necessary to make functions have an equal number of terms
      - what other changes would add information?
      - another common function in solutions: 'applying a filter to isolate differences'
      - what describes difference across core objects (variables)? coefficients
      - isolating the differences in a function takes the form of a vector of their coefficients
      - now you have an ordered vector of coefficients
      - whats the best way to compare lists of numbers, where the positions align (theyre ordered in the same way, and are of equal length bc of adding variables with zero coefficient)? stacking them
      - whats the goal of the solution (find value of each variable that fulfills all equations in the set), framed in this format of stacked lists? 
        - a format where each row may set each variable equal to its solution value
      - what could produce this format, where a variable is isolated on each row (other variables have coefficient zero)?
      - using a version of the other functions in the set, as assumptions of transforms that can be done on other functions in the set, which therefore dont disrupt the validity of the function being reduced to a variable and its solution, since the reason theyre in the same matrix is because theyre supposed to be solved together
        - rules about the values of x & y also apply to rules about the values of y & z,
          if x, y & z are in the same set of linear functions that have a common solution,
          so rules about x & y values may be used to reduce the y term in the rule about y & z values, leaving z to be equated with its solution
      - another way to get here is noting that not every function will have every variable, and that a function missing a variable can be framed as having that variable with a zero coefficient, and zero coefficients of other variables are that frame applied to the solution for the remaining variable
      - now that youve identified the important object of assumptions that can be used as information to organize the system, you can examine how these assumptions allow paths to the target structure implied by your goal, which is a matrix where each variable indicated by the column has its own isolated row where its been tranformed so the other variables have zero coefficients
      - operations like multiplication and addition are within the bounds of the function type definition (linear) which allows shifting and scaling without leaving the type
      
      - this means by:
        - using other functions in the set as a base
        - using term coefficients, variables, & solutions as core objects
        - identifying assumptions that can be used as inputs to generating a set of definitively allowed operations
        - using the zero coefficient format to frame solutions
        - using multiplication/addition as changes allowed within the type symmetry
        - identifying target structure, 

        you can know that these operations will add information to the structure, 
          - given the organization already applied when creating the matrix, 
            - by producing an insight like:
              - "rules hold across functions in the system, within a limit allowed by a type symmetry defined in the problem" (system of linear equations)

      - which can be reduced to a general method like:

        - standardize objects (terms) to a common format where common format parameters (order & position) & their common definitions are applied
          - identify insights like 'in order to align the position attribute, the missing variables in each equation need to have a coefficient of zero'
        - align relevant attributes (position), objects (terms), and functions (equals)
        - isolate variables of difference (coefficients) across objects (terms), where a constant is considered a solution term & isolated from the other terms bc of its different type
        - identify target solution format (set of equations where each variable is equal to a constant)
          - identify implied insights like 'a solution defined in this way also has missing variables with a zero coefficient'
        - query for available rules to use:
          - identify assumptions (both implications derived from the structure, such as the implication of a rule being included with other rules, & explicit assumptions)
          - identify operations that dont change the problem space (operations that preserve linearity of functions)
        - map isolated, standardized, formatted, & aligned objects to the target solution format, using assumptions & common operations & containing structures (like sequences of operations) that dont change the problem space, to keep organization, structure, & alignment relevant
        
      - you can also start from the target solution format (or insights to build it, like the zero coefficient method of aligning term positions), and derive organization methods, assumptions, & operations that can convert the function set to that format of variables & constants, given that solution format

      - you can also start from the insight interface rather than the structural interface and build assumptions from those insights, then look for objects matching the objects in those assumptions and check if information is gained by applying the assumptions to those objects which helps the target solution intent of 'aligning each isolated variable on one side and a constant on the other'

      - you can start from the core interface using operations core to the problem type (linear equations) and the core objects of the matrix structure (coefficients of a function)

      - to do: look for corrollaries between matrix multiplication and ml, as theyre both combining sets of equations using value vectors as input to create an output set of coefficients/values, such as:

        - a matrix of values is used in the position of a term or a function in the matrix multiplication example
        - by applying order & position in the form of node layer & trajectory (like a row in the matrix), the info of the input vector is organized in a way that adds value once applied across the rows
        - by varying weights & weight path patterns within a range (maximizing differences & other useful metrics across weight paths), it mimics the variation of operations within a range (linear)
        - weight paths can map to rows in the matrix, bc the rules/success of one can be used to infer the rules/success of another - same for nodes in a layer & nodes across layers that contribute to each other (nodes can be used to infer the success of later nodes, even before multiplying all of the node outputs & weights for the final node)
        - consecutive weights in a path can map to consecutive multiplication operations applied to a function in the set - so the weight path would indicate the steps required to turn a function (initial weights multiplied by input features) into a prediction of the dependent variable
        - the rules of other functions are used as inputs to other function reductions, so they act similarly to filtering influences in the neural net, like threshold values, optimization limitations, weight path differences, weight path gaps, weight paths & patterns indicating type or other determining metadata, pooling functions, etc
        - standardization allows for comparison of values across both structures (standardization of position vs. standardization of value)
        - alignment between data set patterns and aggregation & weight patterns
        - networks infer the coefficients and matrix multiplication infers the values needed to produce the coefficient sets
          - you could start with a set of probable coefficients as determined by function patterns, and reduce them to the solution of those sets of equations to see if it can produce real data
          - in a matrix, the coefficients act like data vectors, and the solutions are the coefficients:
            - "what value of x, y, & z will make this coefficient data work together"
          - in a network, the data is used to produce function coefficients
            - "what coefficients of x, y, & z can make this value data work together" 
              - translated to a matrix structure: which scalars applied to data with the multiplication operation can isolate the most representative data or most probable weight paths/patterns
          - the coefficients & the variable values occupy a similar position to the weights & the input values - can you extrapolate this to isolated scalars applied to different terms
            - matrix multiplication is to solve a set of equations - weight paths represent theories of operations to transform equal/random coefficients to prediction coefficients
            - if you could select the representative data vectors out of the data set, matrix multiplication might be a useful operation to solve for linear coefficients of the function
              - which method do you use to relate a function's linear version with other versions, where you know either the coefficients or variable exponent output values, but you dont know the exponent used for variables & you have enough examples to calculate it? how does the log change in relation to the prediction function as you change exponents?
              - where input data values are the terms in the matrix, where variables are the coefficients you use to modify those values to get the dependent variable value 

      - integration methods are another place to look for corrollaries, bc the method of aggregation can be used to achieve different levels of complexity better than other methods

        - example: aggregate, starting with big blocks or even blocks, until the level of change allowed without crossing a boundary is insignificant, where the change rate between block sizes as they decrease mimics momentum patterns like found in type differences & differences between function versions (like the generalized version and the specific or adjacent or subset versions)

        - absolute change: a metric measuring across change types (so the absolute change value at the top of a parabola would include the slope & impending direction change & tangent encounter & impending intersection with 0)

        - the momentum of change in a wave is like an ellipse, which has slower change in some areas - do rules from ellipses apply to waves?

      - the main causal structure where existing prediction tools are useful is where the variables are all on different dependence paths/tree branches that dont tie back to the causal network except to contribute to the dependence variable (& other irrelevant variables to that function), or theyre on the same degree of causation (or the same layer) away from the dependent variable

        - all other causal structures arent well-handled by existing prediction tools


## example of identifying important variables

  - identify parameter subsets relevant to a function

    - what is the relationship between parameters of one function subset and parameters of another subset? 
      - example: in a function with an s-curve, one parameter set for the upright parabola function subset has an opposite parameter to the parameter set for the upside down parabola function subset
      - the significance of these relationships is that being able to generate all parameter sets of all function subsets involves finding common parameters & the transforms to translate parameter sets into the other sets

    - other parameter sets of a polynomial or other curve include:

      - the vectors that can be used to generate them, such as a 90 degree vertical wavelength vector from the axis to each curve midpoint

      - alternate ways to split a function (like horizontal slices, subsets determined by change rates, etc) can also have parameter sets with relationships to other parameter sets that produce a more efficient function description or generation method

      - minimal parameter subsets, like min/max points plus a vector set in between each to indicate direction/speed/iterations of change

    - these alternate parameters sets to frame/generate/compress a function can map to semantic objects 
      - the vertical vectors that can be used to generate a polynomial function could map to causal factors, and the same can be said for any other set with the potential to generate the function

    - other function metadata, in addition to alternate determining/generative/causative/descriptive parameters for the function & function subsets
      - alternate functions producing output probability distribution
      - adjacent functions using function parameters or parameters subsets, and functions that are likely to occur in a sequence including the original function
      - opposite functions (functions/parameters generating the exact opposite function given opposites of parameters or parameter subsets)
      - symmetry functions (functions of symmetries that determine/limit/filter the function)
      - vertex functions (functions generating determining/generative/causative/descriptive vertices, vertex subsets or vertex parameters)

    - determining: removes all uncertainties (no alternate function states left possible)
    - generative: can re-create the function in isolation of any other information
    - causative: generative factors that are causative (not all possible generative factors would be the cause or capable of being causative given other information)
    - descriptive: describe the function or its parameters or the subset that is its determining/generative/causative parameters, may compress the function or describe a subset of its information, and may describe output of the parameters or emergent function behaviors/states

    - determinant component-based (using variables and subset components like rows, highlighting useful differences like switching pairs) definition route: 
      - the determinant of a 2x2 matrix is the difference between:
        - a's impact on the top row x d's impact on the bottom row
        - c's impact on the top row x b's impact on the bottom row 
      - the difference in impact of two different sets of pairs, other than defined multiplication (a's impact on top x b's impact on bottom, c's impact on top x d's impact on bottom)
    
    - the standard output-based definition route: "the determinant is the scale of the impact on the n-dimensional multiplication metric (length, area, volume) given by a n x n matrix"
    
    - how do you connect these two definition routes?
      
      - aggregate variables (impact of a vs. total impact)
      - connect process uniting the two or the primary intended process (multiplication) with metric for that process (length/area/voluem)
      - highlight the point of using the matrix multiplication (to transform a vector set or its metric by a certain factor)

    - how do you identify the reason, or why you would use permuted vectors & the difference between them to calculate the multiplication metric, from these definition routes:

      - the reason to multiply permuted vector pairs:

        - multiplying the original pairs (a x b and c x d) gets you the area describing the original vectors: 1 * 2 = area of 1 x 2 rectangle 2
        
        - switching the pairs allows examining the interaction space of the components (the shape created by the points: 
          (a,b), (c,d), (a,d), (c, b) to find the changes possible with the variables described by different values of x & y
        
        - the generalization is permuted subset determinants scaled by the remaining row
          - 'permuting' meaning pairing a remaining element with those it isnt multiplied with (same row) and elements it doesnt alternate with (same column)

      - addition/subtraction operations are alternated to handle component pairs that align with different subsets

      - the reason to subtract one permuted pair from another:

        - from the interaction space, to get the length of the sides of the interaction space, we subtract coordinates:

          (c - a, b - d) is the length of the differences between the two points (a,d) and (c,b): (x' - x, y' - y)

        - the output of the subtraction represents the difference in scale changes achievable from the two permuted operations (a,d) and (c,b),
          - with the assumption that the difference between them is relevant

          - sub-reason why their difference is relevant: bc we are looking for the length of the shape generated by connecting origin points and permuted points, not the length creatable by adding them, so we have to subtract them

        - 1 2    2  2     = 6  6    = factor of change matrixes: 6 3   3  3   = determinant  -6
          4 2    2  2       12 12   =                            3 6   6  6

      - connecting rule: from variables & sub-components & subsets, the interaction space can be generated, and an aggregate impact matrix determined from different combinations of the variables/sub-components/subsets

        - sub rules:
          - given that multiplication generates multiplication metrics like length/area/volume, and subtraction generates difference metrics in a dimension, which combination of multiplication, subtraction, and variables/sub-components/subsets will produce a multiplication metric for the original operation
            - generate interaction space
            - find each difference between generated points & original points of interaction space
            - sum differences 

      - the generalized definition route & conceptual path linking definition routes to explain the intent of the operation would involve objects & processes like the multiplication of the remaining row elements to embedded objects that may be an element or a matrix (x * y subset matrix scaled by a third element z)


## example of deriving a method with pattern matching


  - do repulsion principles mimic or have causal relationship to symmetries around boundaries (like whole numbers represent a container that is full) 
    - or do they indicate a lack of symmetries in that space (attractive forces act on the irrational & fractions rather than integers)

  - as change is injected into the number of sides (moving towards non-linearity) of a closed regular shape (polygon), change may leak outward from the center to form a polynomially described wave/spiral or other shape described by the polynomial's exponential motion
    - in what space would the number of sides or non-linearity of a closed regular shape leak into another direction, indicating the wave shape
    - how do you map the polynomial shape to the change generated by adding (or subtracting) a side

  - polynomials are like transforms around a base which forms the constant for the symmetry to develop at (adding or subtracting versions of the base, as the transforms)

  - cyclotomic polynomial roots may act like a wave function around the x-axis

  - imaginary numbers are like roots with a value attribute that compresses to a position attribute (square root of -1)

  - the roots (intersections at zero) are the different types of transform (addition & subtraction of scaled base versions) positioned as equivalents

    - the implied question is:

      - "how do you transform a set of addition transforms of this scaled base version into a set of subtraction transforms, given the constant term" (using the root values as the base)
      - or "how do you equate these two vectors (addition/subtraction set constants) with one number, in the case of a one-variable polynomial"
      - or "how do you combine the concept of area related to points, lines, squares, cubes, etc to generate these vector sets"

      - system analysis of solution: https://www.quantamagazine.org/new-math-measures-the-repulsive-force-within-polynomials-20200514/

        insight: "polynomials and power series can confirm attributes of the other"

        convert problem type:
          "question about the size of roots of polynomials"
          "question about the size of values associated to a power series"

        requirement: coefficients needed to be positive or negative whole numbers

        insight path:
        "
        a non-cyclotomic polynomial
        found its roots
        raised those roots to different powers
        multiplied them together
        took the square root of that product
        based on that square root, he could construct a power series with the essential property (coefficients are whole numbers)
        "

        intent:
        "
        a non-cyclotomic polynomial             (roots not on unit circle/roots following repulsion pattern)          get relevant object (non-cyclotomic polynomial)
        found its roots                         (found numbers that equate its transform vectors)                     find the symmetry of sets generated by its transform types
        raised those roots to different powers  (permute polynomial exponents and apply to roots rather than base)    create polynomial with roots as bases (or even orthogonal change distortions of roots as bases)
        multiplied them together                (apply change from roots orthogonally)                                multiply terms of multivariate polynomial (multiply orthogonal change distortions of roots)
        took the square root of that product    (find number to produce product with one multiplication (squared))    find alternate standard generative factor (specifically square root) of the product of that multiplication
        "

      - insights (mostly based on similarities):

        - after finding roots, youre doing a similar operation twice:
          A. first create alternate output (root to a power) of factors (roots)
          - then (after multiplying the alternate output)
          B. find alternate factors (roots vs. the final square root) of output (product of distorted roots)

        - another key point is the default relationship between roots (multiplied by each other) and the interim operation (multiply roots taken to powers) between symmetric operations A & B 
        - another point is the transformation of a root into a polynomial term, given that its being multiplied by itself
        - then these polynomial terms are being used to create another polynomial term (x^2), whose output x is relevant to a related power series of the original polynomial, with integer coefficients
        
      - generate insight chain (of specific insights):

        - factors (x - a) are important objects in polynomials and act as power series factors (x - c), so given that theyre an important object, we can select the 'factor' operation as something to try in the insight path first
        
        - given that factors differ between the two function types, we should look for alternate factors as one of the insight path steps

        - since we're transforming something, symmetries should be a key object we use first (like embedded or containing symmetries, such as the symmetry between the two similar operations)

      - questions

        - what is the relationship between polynomials with duplicate roots & distribution of roots around the unit circle
        - why would this function/insight/intent path produce a power series with integer coefficients (scalars) applied to some center c?


## example of applying structurized concept to other standardized concepts

  - example of a phase shift about a vertex:

    - in the problem of a rock on a hill, how do you determine at which point it will start rolling down?

      - vertex: minimum side length to maintain position

      - at increasingly large incremental additions to the side length variable, there will be a phase shift at the vertex (minimum side length to maintain position), after which it will start moving
      
      - this is because either:

        - the attribute (change rate of side length facing ground) and the attribute (slope of the hill and emerging force) align (rate of side length decrease increases and slope increases) or intersect (change rate of side length matches slope of hill in a way that fulfills motion intent)
        
        - the 'side length facing the ground' and 'its adjacent side in the direction of downward motion' are similar enough to allow momentum to develop from repeated motion (if the adjacent next side is too different, the rock might stabilize again)
        
        - the shape of the side length facing the ground and the next n sides aligns with the shape of the ground 
          (a curve can align with more ground shapes, but a rock with different side set shapes aligns with a smaller number of ground shapes)


## example of object inference

  - how do you infer the existence of objects we cant measure:

    - the same way you infer that a whole object is complete, without being able to measure an object in its entirety simultaneously (being able to see it from every angle and on every scale at once)

    - without being able to see an object, you still use intersections of its vertices (one of its determining behaviors & one of its identifying attribute values) to rule out or otherwise limit the possible solution set of possible identities & degrees of completeness, between the object and adjacent possible objects, where each vertex intersection you check is between the object and the adjacent possible objects, even though you cant see the whole object in every possible way to measure it

    - example: without being able to see a ball in its entirety, you can check:

        - vertex intersection of its shape:
          - vertex 1: that it casts a sphere's shadow
          - vertex 2: that its boundary is circular

        - vertex intersection of its motion:
          - vertex 1: that it bounces instead of falling once
          - vertex 2: that it rolls on a hill in a vacuum of other forces (responds to gravity)

        - vertex intersection of its symmetries:
          - vertex 1: doesnt dissolve in substance that dissolves non-plastics
          - vertex 2: doesnt rest in a square or triangle shape even when compressed to those shapes

      - and you dont have to check other vertices for most probable relevant intents (dodging ball, throwing ball) bc the intersections of these vertices rule out other adjacent classes of objects:
        
        optimization vertexes:
        - 'not made to maximize difficulty on some metric'
        - 'not made to maximize ability to catch'

        symmetry vertexes:
        - 'not aligning weight & size attribute values with hands & strength attribute values' 

        structural vertexes:
        - 'not a block'
        - 'not a disc'

        intent vertexes:
        - 'not a hat'
        - 'functional for intents that are not entertainment intent'
        - 'not used for physical games'
        - 'not manmade' (also a control vertex)

      - you can see that subsets of the vertices and their intersections (like two sides of a triangle forming a point) are sufficient to identify the object for a subset of intents relevant to the object

    - so we can infer whole objects and object identities without documenting their every particle from every angle

    - similarly we can infer other objects we cant fully measure (symmetries, origin, paths) using various vertexes and their intersections:

      - infer symmetries with vertex intersections:
        - radius & origin
        - adjacent symmetries & limits

      - infer origins with vertex intersections:
        - current potential energy and distance from possible origin points
        - current potential energy and patterns of movement

      - infer paths with vertex intersections:
        - destination and alternative selection metrics
        - efficiency or resource conservation priorities


## detecting objects of uncertainty

    - for genuinely invisible sub-systems, we may only be able to find related objects (the boundaries containing them, the filters allowing them to develop) rather than their trajectories on the shape/other attribute interfaces

    - we may also be able to predict a finite set that they may be contained in (given the full set of combinations, what is a probability distribution not found in any natural process but still possible, that could describe uncertainty object behavior that we cant measure)

    - we may also be able to derive accurate opposite insights (given the existence of an object, what is impossible to describe, limit, define, etc)

## minimum information:

    - whats the most efficient way to depict a physical object - as a network graph of:
      - splits & projections
      - splits & limits
      - gaps & limits
      - corners & angles
      - shapes & positions
      - intersections
      https://en.wikipedia.org/wiki/Orthographic_projection#/media/File:Graphical_projection_comparison.png

      - limits may seem like the best object but youd have to list limits of every side or side type
      - positions & shapes may seem ideal too but then youd have to store shape information
      - intersections may seem useful (intersections of functions like planes & lines at certain points) but theyre similar to number of sides in count

## reverse engineer a system from filters

  - it should be possible to reverse engineer a set of system-generating rules by observing outputs and calculating 

    - the set of core components that would create them with the least work (prioritizing resource re-use, sharing functions, cost minimization, etc) & other determining factors of most system development like other system interactions
      - example: the most efficient way to achieve two functions that are variants of each other is using a variable as a function input

    - the set of required components for a system to function, & then calculating the sub components of required components simultaneously with information about other sub components as more calculations are done
      - example: the bio system needs a storage function, and edit function, a regulatory system, etc

    - a causal diagram and a system diagram can intersect on the causes that maintain their shape in the system
      - example: a causal structure that is generative & causative of system changes


## deriving limits of a system

  - math doesnt just describe concepts like 'whole number', it also describes basic interactions like pairs, sets, combinations, which appear in most systems 
    - are there objects in systems that are real (change other objects) but not describable (have no structure or measurable/constant structure) with our measurement/description tools

    - this system of math describes certain change types, values, & relationships 

      - so something that doesnt have a structure, or value, or cant be changed with any operation, and doesnt relate to anything might not be describable with known math

      - for example a space-time with one object, which has no other objects to be used to compare to it except the defined boundary of the space-time (which itself may not be measurable or comparable to the object), and the space-time is in constant flux so position, structure, & change cant be measured, just estimated 
        - or the idea of distance is invalid because change is so fast or chaotic it cant be measured, so you might try to describe its behavior with a probability distribution, but if it doesnt follow one, you may need a network of distributions, rather than a scalar value describing some distance type between positions
        - or its in all positions as a possibility (an adjacent structure that would generate or attract the object at faster-than-information speed) and its next occupied position cant be measured, so the idea of distance is invalid, because not only is it equally likely to be in any position, but its next position is also equally likely as any other position because distance doesnt matter, as it can either travel fast enough to make distance irrelevant or it can travel through other spaces faster or each position is a potential object thats about to crystallize and which position actually does is determined by the travel of faster objects like energy

      - math breaks down with some interactions of change types that create ambiguities so information cant be measured

      - if you try to create another description system, you end up changing definitions, variables, bases, or methods but not the system itself, which is founded on numbers having absolute value & core operations to compare/combine them

        - in order for the system to exist, some objects have to be defined (a base concept crystallized into a structural object)
        - what description system do you get if you dont use units/value as a base (ranges, definitions, attribute sets, interfaces as a base)
        - are there other possible description systems than these
        - in generating other description systems, you end up adding assumptions to physics rules instead
          - if there was a system with no concept of equal (no objects are ever allowed to be equal) or where continuity didnt exist (no fully connected objects or whole objects, just sets/sequences) - you can create other spaces with defined operations, but if you tried to apply it in euclidean space (y could never equal x and x could not cause y), you wouldnt be able to do some operations like comparison or cause, so that would be applicable for spaces where objects couldnt occupy the same position or spaces that could only contain one object so objects couldnt interact
      
        - in general it describes change & relationships & spaces but not structures like rules/filters that generate description systems & its advantages, and describes information but not:
          - missing information
          - possible information (ambiguity resolution, adjacent/likely information, shapes of uncertainty, information route)
          - unmeasurable information
          - information logic (what constitutes validity or logical inference in a space, given that validity is usually defined for core objects rather than all the possible emergent interactions in a space, and whether space components like number types or definitions are generated by or used to generate other spaces given inferrable/measurable logic)
          - information metadata (intent, cooperative/contradictory information)
          - semantic information (how does position/distance/value map to the concept of equivalence/similarity, given the concepts of thresholds indicating which value differences are important)
          - embedded information (parameters, bases, conversion functions applied, prior parameter values)
          - complex information (concept position in a network is generally attempted to be described as a network but that leaves out position/direction as information, even though the information of concept node cluster or linking function is useful in 2d, partially real numbers that are generated by combinations of attributes but arent completely described or understood in all their possible interactions)
          - meta information (describing itself): what is the set of all equals, what is the most unique number, what is the average definition of difference

    - are there materials/processes that erase information (convert back into a superposition) or which can vacillate between discrete/continuous like waves, skipping information & leaving gaps that can break the chain of information (breaking time reversal symmetry)


## finding an example supporting or implementing a rule in a system

  - an example of how over-dependence on a fact makes it false:

    - fact: "fossil fuels are valuable in a problem space with cars that use them or their byproducts for fuel"
    - heavy investment in fossil fuels could indicate their popularity
    - if many entities rely on them, their supply will be reduced, assuming they cant be generated with imminent tech
    - the competition given reduced supply will produce fast innovation, resulting in side effects
    - side effects in a fundamental interface for existence could put existence at risk
    - side effects from mining could also produce an environment that generates new "fossil fuels" or their equivalent position (natural resources that are easy to use for a fundamental intent), but this is not as likely as causing side effects that put the whole system at risk

      - why is this less likely to produce good side effects?

        - the methods of transforming substances into other substances have costs (pollution of reaction byproducts)
        - the elements likeliest to be useful as fuel produce the most pollution
        - the elements likeliest to survive millions of years in this environment on/near the surface are the likeliest to produce the most pollution
        - the mechanism of using fuel (engine & other components) isnt likely to require innovation invalidating fossil fuels right away
        - alternate fuels arent as adjacent as digging in the ground & burning, which are core mechanical/chemical functions
        - the byproducts of fossil fuels & reactions arent likely to be easily generated using alternate methods, given likely tech

    - over-dependence on that fact (beyond its ability to support stress) makes it false: they were valuable in that problem space, but over-dependence on them created negative systemic side effects, and now dependence on them is a liability

      - the fact collapsed into a network of related facts like "alternate fuels are valuable" and "an additional use of fossil fuels could cause system collapse"

      - this is a mismatch problem type of imbalanced dependence & support functions
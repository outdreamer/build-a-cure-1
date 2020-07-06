  - fix indexing 'NNP NN NNS1 of JJ JJ JJ2' or postpone to pattern evaluation time
  - fix missing alts
      pattern_index::verb_phrase::plays a |VB NN| role::a NN role
  - fix one-letter alts: pattern_index::phrase_identifier::ALL_N DPC ALL_N |VBG VBD|::N D N V
  - generalize alt logic to use embedded pair finding
  - fix supported stem assignment (endings like 'is': {'functions a', 'acts a', 'plays a', 'operates a', 'works a'})
  - fix charge function ('edit' is assigned positive score)
  - add core clause patterns 
  - fix pattern matching functions
  - finish pos, clause, modifiers code from find implementation

  - make function/query list for workflows, starting with information formats

  - why do phase shifts happen - bc of the ability for aggregated information to be measured as something else 
    - example: molecules identifiable as a set, data identifiable as a cluster, pattern identifiable as an emergency

  - what are the aggregate effects of many errors in selection of algorithms/parameters/processing/deployment - what phase shifts emerge from repeated or interacting error types?

  - identify attribute: attributes can be reduced to 'position', implemented as a:

      - relationship type (relative difference)
      - structure type (shape)
      - change type (generators of difference)

    - the structural network can frame these position differences to capture all attributes
    - add function to derive structures of an object given its attributes/functions (related attribute sets indicating a type or sub-system, etc)

  - identify function: a function can be reduced to a 'change unit'

  - identify object: an object has attributes/functions and is not itself either of those (for standard definition of object, even though both attributes/functions can be framed as objects)

  - after identification functions

    - import rules for selecting interfaces to solve a problem on

      - determine minimum information
      - query for rules making inferences from available information sets
      - Function interface helps find unused functions
      - Intent interface helps predict system priorities & find exploit opportunities
      - System interface helps find efficiencies
      - Pattern interface helps find insight paths/similarities

    - import insight history data to identify insight paths 
      - info insight paths like 'lie => joke => distortion => insight'
      - system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub'

    - network design favors adjacent features
      - to get around this, build in a concept of default core objects like boundaries/limits/intersections to the network structure or data propagation (send data on possible boundary line positions) to look for & focus on those first rather than continuous sets of adjacent high-variance, pattern-containing features
      - why would patterns like textures make it through as a semantic filter - bc the repetition is interpreted as significant by network design, or the texture is likely to be located in more data subsets than a shape
      https://www.quantamagazine.org/where-we-see-shapes-ai-sees-textures-20190701/

    - document how rules develop on stability & how foundations are connected & destroyed

    - example of conceptual math: 
      - calculating structure of a concept definition
      - determining structure that a concept takes in a context
      - a concept applied to/injected in another concept
      - identifying concepts in a context & their corresponding values in another context
    
    - example of interface query:
      - which interface to start from or end at, in what sequence (start from system interface, stop at pattern interface, aim for math interface)
      - which interfaces to embed/apply to which interfaces (apply trust to the information interface, embed power in the cause interface)

    - direction of math-structure query:
      - finding shapes that are useful for a context
      - finding contexts that are relevant to a shape

    - define core operations: apply (expand one by the other), inject (input one to the other), embed (attach one as a component/attribute of the other)

      - power dynamics

          - rules: 
            - if a person abuses their power without contribution, the others will notice and take their power away

        - truth (type of power in the form of constant, reliable information) dynamics
          - the truth has a limit on how much it can be stretched or re-used before over-dependence will make it false or reveal its limits

        - trust (type of power in the form of delegation of an unenforced opportunity/responsibility) dynamics
          - rules:
            - there is an incentive to trust people in an absence of resources
            - there is an incentive to trust people to create resources (positive expectations, as an input to peaceful coexistence)
            - there is an incentive to not trust people if they have resources like:
              - information about signals of untrustworthiness
              - fear response or memory of untrustworthy behavior
              - logical knowledge of incentive structure to abuse trust

        - the operation of injecting truth into trust on the power interface means applying the truth dynamics as an input to trust dynamics
          - example: what happens when trust is embedded in a context, and one side has more information about untrustworthiness?

    - example of math-structure query:

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

    - systematize your definitions of info objects, to include analysis that produces relationships of core objects like opposites to their relevant forms (anti-symmetry) in addition to permuted object states (asymmetry), such as an anti-strategy, anti-information, anti-pattern

      - add technicality, synchronization, & certainty objects leading to inevitable collisions
        - the collision of compounding forces producing a phase shift
        - lack of attention in one driver and false panic in a second driver leading to a car crash given the bases where their processes originate
      - define alignment on interfaces (compounding, coordinating, parallel, similar, etc)
      - start with these info object transforms that filter the most info: opposite, invalidating, symmetric, core, aligning, boundary-breaking, phase shift activating, structure stabilizing, constant changing, converging
      - add core info objects (core strategies, core assumptions) so you can make a network of graphs for a system

    - add object metadata:

      - spaces where the object can change:

        - attribute spaces: 
          - default space (probable default position in a system, etc)
          - potential/probable space
          - adjacent space (accessible positions using minimal work)
          - extreme space (attributes/functions at its limits)
          - partial space (attributes/functions with subsets of its definition)

        - object spaces:
          - interaction space (what it can interact with)
          - efficiency space (set of efficient positions)
          - perception space (what it can seem like)
          - system space (what contexts it can exist in)
          - query space (which queries can produce it or its changes)

    - space can mean:
      - the interface filter including structures for a given attribute/object like cause
      - the impact of the attribute/object on other interfaces (impact of cause on other interfaces, like info problems)
      - an interface applied to another to create a space (causal interface framed as a set of problem spaces)

    - make a system layer diagram with interfaces to allow specification of core interfaces & other interface layers (interface interface)

    - make a system layer diagram for structures to include layers of structures (beyond core structures like curves, to include n-degree structures like a wave, as well as semantic output structures like a key, crossing the layer that generates info structures like an insight, a probability, etc)

    - testing for independent variables: 

      - a slice of a bottleneck (filter and/or limit applied that enforces interaction) may include enough random independent variables to generate a normal distribution of a dependent variable, if a series of variance gaps in a system has alignment (similar direction moving toward the bottleneck), where the bottleneck forces the variables to interact in a way that doesnt enforce similarity/convergence of the variables (leaves open the possibility of coordinating/cooperative differences)

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

    - when you have one sample, it's possible to estimate distance from average using extreme attribute value sets & mapping the attribute sets to assign probability given the relationships within the sample, as a prediction tool with minimum information

      - example: if you're in a position outside and you want to know if its an average or extreme position, you can: 

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

    - add note on evaluating object attributes, plus the ability to occupy invalidating positions/structures or fulfill invalidating intents of a system, and system requirements for those objects (invalidating position/structure/intent) to be possible
      - example: 
        - object attributes: a chemical on its own
        - system position: a chemical adjacent to another chemical in a system with high temperature
        - system structure: a system designed to make any adjacent chemicals explode, vs. a system that standardizes chemicals to a harmless format
        - system position & structure: a chemical with an extra electron at a position in the system where an extra electron would cause an explosion

        - "Similar logical patterns are absent in SARS-CoV-2, indicating that the virus evolved naturally." - the evolution of a virus to fit within certain systems confirms that changing the system metadata (inputs, structure, side effects, priorities, functions) invalidates the virus without invalidating the system
          - removing/adding the transforms that made the virus deadly/innocuous to a system
          - sending type signals within a contained limit around the virus to give the impression of systems that it wouldnt be deadly in
          - changing the position of a virus (so necessary bacteria interpret pathogens as energy sources)

    - document generated function types
      - decoy rules that consider probable usage, so usage follows the actual rule
      - cost-based system rules
        - avoiding assumptions or other objects where the cost of being wrong is too high to recover from 
          - in a case with multiple alternative explanations, but one is very high-cost if it's true or false, so assuming anything that rules it out cant be assumed without a high ratio of information or high number of indicators
        - cost as an aggregation/interaction rule (lowest cost routes should be assumed first)
        - cost that exceeds the value of intent should be assumed to be either false, unlikely, developing into a more efficient rule, being interacted with from another object/function/attribute, or being destroyed

    - organize notes on embedded/chained interfaces (which interfaces to use first when describing each primary interface, to produce the formatted & filtered information likeliest to be useful in the most situations to produce the default interface network)

    - organizing the stock market similarly to insurance to inject agency, investors can influence the market so that objects like competitions/incentives are created in a way that maximizes gains (making industry players compete in an industry that your other investment is capable of invalidating if they stop improving customer service vs. certain product features), or creating platform/foundation tools that are necessary components of the industry (prediction tools, specifically claim-testing tools or price assessment tools), or evaluating agent interactions at scale (what are the obvious ways & distortions of those ways to manipulate/evaluate/predict the market, who has the ability to act on those manipulations, and what is the net effect if all agents who can act on that do so)

    - example of concept analysis in design of sorting function:
      - similarity in navigation, equality in split => optimal for target value near initial split points or similar positions to the split points
      - assumed difference embedded in pre-computation of attributes => optimal for target value with different pre-computed attribute value, or target values in similar position to values with different pre-computed attribute values or adjacent values

    - document generated object change types
      - constant to variable
      - variable to removal of assumption in variable type/data type

    - document objects outside of system context

      - what types of objects/functions/attributes survive outside of a system that isn't closed by default, and to what extent

      - what interfaces capture the objects outside of a measurable system context with potential for information (maintenance of a fact for enough time & space to be measured or depended on)
        
        - potential

          - probability of being interacted with by a system
          - probability of decay without a host system
          - lack of information (lack of position, structure, time, etc) or lack of measurable information (changing too fast for an observer to interact with it)

        - attributes

          - opposite: everything outside of systems is:
            - not the system
            - not yet/anymore in the system
            - not compatible with the system (unmatching elements)
            - not valid in the system (like everything that cant be proved or controlled in/by a system)

        - cause 

          - generators of systems or generator side effects or system side effects

    - document interface math examples, like standardization of all distinct components into their own interfaces, rather than within a system context
      - rather than framing the behavior of objects in a system, you can:
        - remove the assumption of the system limits forcing interactions
        - frame each object on its own interface (containing all its possible forms, variables, attributes, generators, cooperative contexts, etc)
        - compute the interactions of those interfaces

    - apply combinations of core operations to get information object layers ('democracy games', 'barriers to intents or false information') once definitions are standardized to system interface

      perspective: priority set with object positions & default paths
      strategy: efficient path between points
      joke: difference between expected & actual position
      error: difference between expected & actual decision
      argument: position of objects or path between points with supporting connective functions
      game: incentivized motion within a system having limits to prevent motion
      filter: barrier creating a difference between input & output

    - add interface diagram & interface query map
      - interface query map indicates position of interfaces to query
        - examples of targets of interface queries:
          - function fitting a context, context fitting a function, causal structure fitting a function, errors or missing information fitting a function, tests determining a function
        - the position of interfaces is determined by intent of problem/solution and cost/optimization metrics and available information or testing/derivation (information capture/generation) resources

    - add conceptual math diagram

    - target objects of problem space analysis to find an 'ethical' or other algorithm to guide an object through a system:

      - events that reduce potential (irreversible outcomes like an agent death)
      - intent vs. outcome within context (repeated intents & exploits of intent stacks for malicious intents)
      - symmetries like ambiguity, potential, & alternative-generating paths/bases
      - assumptions/limits (neutral intents are likelier to be used maliciously than positive intents)
      - context trajectory (such as maintaing a path through contexts to avoid calculations)

      - once these objects are identified as necessary to understand the problem, then the implemented objects can be identified in the problem space, & the solution can be calculated

    - example filter analysis

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

    - apply the set of core structures, functions, objects, and attributes to itself to get next layer of transforms & systems to run next error analysis
      - attribute spaces (object model + structure interface = a calculation method for attributes)
      - false similarity (info interface attribute + core attribute = an error type/definition route, if agency is involved)
      - filter chains (structure interface + structure interface = a core object to frame info)

    - derive the context set that a prediction function has varying degrees of success in (type distance, missing variables, changing problem space, etc)
      - this can be used to reduce the uncertainty by first identifying which contexts a function will be successful in predicting and then checking for those contexts in the problem space

    - rank methods of structure application for different contexts
      - expansion/compression (by intent, function, etc)
      - filters/connections
      - systematization
    
    - prediction/change/context as fundamental function objects

    - prediction of missing vars example

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

    - mapping function, to map problems to structures & other problem types

      - problem types

        - find structure

          - find combination (build)
            - of filters
            - of functions
            - of objects
            - of sets
            - of limits

          - find sequence (route)
            - of network nodes representing
              - steps
              - positions
              - sets
              - intents

        - correct imbalance (align)
        
          - in direction
          - in resources
          - in functionality
          - in intent

          - example: find combination of terms to build a prediction function for a data set

            - of filters
              - which filters should be applied to reduce solution space, find relevant objects, or find steps to produce or build the solution

            - of functions
              - which functions are possible solutions to a prediction function problem
                - 'take an average metric of the set of functions predicting x% of the data with fewer than y terms'

            - of objects
                - 'average', 'function set', 'term count', 'accurate prediction ratio'

            - of sets
              - which objects should be grouped (function set, term set)

            - of limits
              - which assumptions are required and which are flexible

            - of matches
              - which objects need to match, to what degree (function terms and data)
              - which set of reductions works the best with a given set of expansions

            - of imbalances/asymmetries (questions)
              - which metric sets are the best filters for a given problem

            - you could graph the problem/solution with any of those objects, if they supply all the info needed to frame the problem
            - navigating on the filter or mismatch section of the network may be faster given the commonness of those objects

          - example: find resources to fulfill a lack of a resource

            - cause of problem: missing resource or its alternatives, or missing resources to generate it or its alternatives, or dependence on resource or its alternative

            1. create missing resource

            - navigate up causal stack: find combinations of functions & objects that generated it
            - navigate sideways: find alternatives or find alternative combinations to generate it

            2. invalidate dependence
            - navigate up causal stack until dependence cause is found: find combinations of functions & objects that generated dependence
            - navigate sideways: find functions to invalidate dependence (generate resource) or correct problem (imbalance, lack, mismatch) causing dependence

            - solution intents 1 & 2 have a 'generate resource' intent in common, which fulfills both solution intents - so if the intent changes between them, the solution involving generating the resource may cover the next problem iteration too, or the intent that invalidates the problem may prevent future iterations


      - ways to map this:

        - attributes that differentiate problems that are shared with possible solutions
        - mapping intent to direction and assessing progress by movement in that direction
        - networks with clusters & other structures representing decisions
        - system layer graph representing possible steps
        - function sets mapped to sequences given a metric like progression toward goal
        - mapping related/approximate problem or problem higher up causal stack, having lower dimension, like a generative problem
        - mapping change types to dimensions and graphing/calculating dimensions where change types change (an aggregate, interface, or deciding dimension where change type is uncertain but not random)
        - using a layered graph to visualize change of different types/metrics built on a symmetry (vertical axis if horizontal sections are split)
        - mapping language to structure directly ('find' maps to a set of vectors leading from a node indicating possible start positions, with option to use core function vectors to reach target node)
        - a trajectory between low-dimensional problem graphs where each graph is a decision step, and attribute sets & problem of similar type occupy a similar position on an axis depicting all the graphs traversed
        - a metric like size of variable interaction space mapped to length/area/volume to indicate how much of the problem is left, and a metric like number of variables mapped to number of sides of the shape to graph the problem according to structural metrics


      - limits in visualization

        - if you reduce a shape of a subset of problem dimensions, those variables (side length if defined as a cube, or variable set like identities of sides, number of corners/sides, angle of corner, shape identity), cant be used later in the solution, so even though some reductions may seem obviously right, more than one solution should be tried

        - mapping problem types to functions has side effects without limits & standardization applied to the format:
          - removing a problem variable can only be mapped to lowering the number of variables (whether limits, multipliers, or other objects) creating a shape once the problem variables are formatted with the same term set


      - parameters to graph problems

        - number of problem-causing variables/solution metrics fulfilled
        - complexity: 
          - number of core function steps required
          - number of variables
          - number of differences/inefficiencies
          - number of counterintuitive steps (requiring non-standard solutions)
          - number of contrary processes (requiring scoped/nuanced solutions)
        - abstraction (does it solve the same problem when framed on an abstraction layer above)
        - number of steps required to create problem from stable system state, once work is standardized, & adjacence of steps required
        - how much work is required to convert to a particular problem format (route, combination, composition)
        - type/intent ranges/direction (of individual objects or composite stack)
        - similarity (how similar to a standard problem type, or how near to limits within a type dimension)
        - ratio of positive to negative outputs


    - solution decomposition function

    - solution aggregation function

    - make doc to store insight paths, counterintuitive functions, hidden costs, counterexamples, phase shift triggers

    - function to detect patterns in queries & outputs to optimize queries & find insight paths to improve response time

      - example: 3-step jumps with direction change, navigating across a certain pathway in standard structures across interfaces, starting with system then cause & intent, etc
      - this has to identify & remove unnecessary steps that dont change the output
      - identify & replace with faster ways to get to the output without changing the output
      - test cases to determine if output would be changed by removing a step and/or replacing it with another step

  - abstract functions

      - derive combinations & make sure you have full function coverage of all important combinations

        - check codebase function index for combinations
        - check that you have sample data in json for each combination

      - attribute/object/function match functions
      - specific interface identification function
      - standardization network-framing function to describe a system as a network (the standard structure) & position each object, identifying connecting functions
      - system analysis function (identify boundaries, gaps, limits, layers, incentives/intents/questions, & other system objects)
      - isolation function, representating function/attribute changes independent of system context with respect to position or time (snapshot/state or subset)
      - function to define (isolate an object/concept/function for identification, identify definition routes)

  - give example of each type of problem-solving workflows

    - workflow 1:

      - finish function to determine relevance filter ('functions', 'required') from a problem_step ('find incentives') for a problem definition, to modify problem_steps with extra functions/attributes ('change_position') to be more specific to the problem definition ('find_incentives_to_change_position') for problem_steps involving 'incentives', so you know to use the function_name to modify the problem step if it's between the type 'functions' and the object searched for 'incentives'

      - finish function to get all codebase functions & store them in a dict with their type, context/usage, and intents, just like functions are stored in the problem_metadata.json example for workflow 1
      - finish common sense check
      - finish defining objects in object_schema.json
      - finish organizing functions.json by type, with mapping between general intent functions like 'find' to specific info-relevant terms like 'get'
      - add common phrase check & filter problem steps by repeated combinations with common phrase check
      - finish get_type function to map info to structure using the new functions.json organization
      - finish apply_solution to problem_definition using problem_steps
        - involves building a function to evenly distribute objects (like information/types), given problem positions/agents/objects

  - need to fill in content:
    - finish intent/change type calculation for a system intent
    - selecting optimal combination interfaces to start from when solving problems 
      (how many degrees away from core functions, specific layers or sub-systems, what position on causal structures)
    - key questions to filter attention/info-gathering/solution
    - key functions to solve common problem types
    - development of key decision metrics (bias towards more measurable/different metrics rather than the right metric)
    - trajectory between core & important objects
      - example of choosing inefficiencies/exploit combinations in a system
    - research implementing your solution type (constructing structures (made of boundary/filter/resource sets) to produce substances like antibodies, using bio system stressors)
    - emergent combinations of core functions (include derivation of invalidating contexts for core functions)

  - extra tasks

    - add precomputing if a sub-pattern was already computed:
               'ALL_N ALL_N of ALL_N ALL_N'
         'ALL_N ALL_N ALL_N of ALL_N ALL_N ALL_N'
    - add formatting to allow multiple items as keys in json and maintain order for interface network paths

  - alternate utility function implementations have variation potential in the exact operations used to achieve the function intents, but there are requirements in which definitions these functions use because they are inherent to the system. For example, the embodiment may use a specific definition of an attribute (standardized to a set of filters) in order to build the attribute-identification function using a set of filters - but the general attribute definition is still partially determined in its initial version by requirements specified in the documentation, such as a set of core attribute types (input, output, function parameter, abstract, descriptive, identifying, differentiating, variable, constant), the definition of a function, and the definition of conversion functions between standard formats.


  - given that a set of genes produces a range & methods with which change can occur, is there necessarily a determinable difference between which changes can be expected to disrupt the system and which changes its change methods can handle
    - are there necessarily some changes that cant be handled given the ways it can change
    - is there definitely a set of genes that produces a system supporting a set of possible change types that dont allow the system to be destroyed by external pathogens, or does this protected system have the potential to exist genetically, but not coordinate in a way that would be able to function in the real world
    - there is no default mechanism determining the gaps in change rules allowing variance injections in a system generated by genes (which kinds of gene edits are prohibited absolutely, which kinds are contextually possible, etc - these rules are not analyzed for gaps in coverage of change rules by default)
    - these gaps may allow changes to bubble up or cascade system-wide depending on the specificity
      - a rule that allows removal and a rule that allows copying could be used to change the change rules, possibly invalidating themselves or the system
    - how do you find these gaps in enforcement that can be hijacked to disrupt the change rules - with intent structures like chains, networks, & trees

      - whats the intent of deploying a gene edit producing a randomizing function on change locations to every cell? if theres a cell that will become hostile once random changes are made, that could be the intent


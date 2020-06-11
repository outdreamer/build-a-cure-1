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

          - when there is a large difference in outcome between similar inputs (volatility), there are other parameters contributing to the outcome probabilities (just like being an endpoint value decreases the possibility of being paired in a subset with adjacent values)

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


              - conceptual routes

                - independence

                  - one input to the average doesn't influence other inputs to the average
                    - adjacence within a value pair as a contrary force to the average
                    - the full set of adjacent inputs has inequality in distribution (1 has fewer adjacent inputs than 2)

                - random (distribution for each variable)

                  - each possible outcome value is equally likely
                  - each average outcome value is likelier to be similar or equal to the average possible value than another value
                  - when permuting the concept of similarity, do averages change in behavior? (start with 'independence' query generating 'adjacence' concept and 'adjacent pairs' inequality or 'adjacence' query)

                - adjacence

                  - adjacence between outcome values can be a factor in the average of that subset


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


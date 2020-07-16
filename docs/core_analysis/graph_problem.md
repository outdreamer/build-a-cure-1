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


## example of concept analysis in design of sorting function:
      - similarity in navigation, equality in split => optimal for target value near initial split points or similar positions to the split points
      - assumed difference embedded in pre-computation of attributes => optimal for target value with different pre-computed attribute value, or target values in similar position to values with different pre-computed attribute values or adjacent values


## example of deriving questions to translate into query sequence

  - stat problem: "Sunrise problem: What is the probability that the sun will rise tomorrow? Very different answers arise depending on the methods used and assumptions made"

    - interface analysis questions:

      - what are the shapes & patterns of errors in assumptions & selection/generation of methods? (what ratio of incorrect are people with each additional assumption, given the level of certainty per assumption & complexity of problem)
      - what are the consequences of not correcting those errors? (how wrong will the predictions be)
      - what are the shapes of cause in generating/selecting assumptions & methods
      - what is the usual correct assumption pattern once false assumptions are corrected, and whats the insight path to transform the incorrect to the correct version?
      - whats the rate of discovery of new sub-systems, objects, or variables in related systems like physics
      - whats the likelihood we created certainty out of what ratio of our assumptions (over-relying on assumptions to make them conditionally true)
      - whats the possible causative impact of measurements & application of science knowledge on other knowledge
      - whats the possibility that a subset/state of physics rules gathers in increasingly isolated space-times, but outside of it, the rules are more flexible
      - whats the possibility that every science rule we take as certain is a false similarity or other false object?

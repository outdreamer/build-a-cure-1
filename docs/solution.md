# Solution Object


## Attributes

  - types

    - meta solution

      - method for evaluating solutions or determining solution starting point (choose between methods in problem_solving_matching.md)
      - method for automating solutions
      - method to update solution definition metadata (a method that can add new solution type when found)

    - solution generator

      - function derivation method
      - solution selection method

    - solution framework (limits reducing solution space)

    - problem decomposer (reduces problem dimensions, matching dimensions of solution to dimensions of problem)

    - problem metadata manipulation
      - changes problem space
      - postpones solving problem
      - matching problem with other problem to neutralize both
      - problem analysis: 
        - calculating probable solution cost
        - calculating value of problem reduction vs. problem solution (vs. secondary or source problem reduction/solution)
        - learning: using understanding as an alternative to using/selecting existing tools or solving problem directly

    - solution selector

        - existing tools: as an immediate implementation option

    - interim solution 

      - common components of solutions:

        - a granular solution strategy
        - method to determine minimum info needed to solve problem
        - method to determine definition
        - identify objects in data
        - identify important objects/rules/variables/layers/systems

    - transforms unsolved problem into solved problem (transforms unsolved problem like markets or energy storage or evolution into an optimization/organization problem)

    - solution function built on core functions:

      - apply
        - transform
        - rule

      - derive
        - definition
        - function

      - find
        - object
        - gap

      - fit/match
        - structure

  - limits

    - time limit
      - only applicable in a certain time window

    - abstraction
      - structural/conceptual or specific to context
      - choosing the abstraction level that will reduce misunderstandings while optimizing reusability

    - reusability
      - only applicable once, as with solutions that are easily identified or stop working once you use them the first time
      - how to design/choose solutions for reusability

    - cost/benefit analysis 
      - such as learning/understanding/integration/implementation/migration/functionality gap cost potential

    - problem-type & problem-space scope
      - only handles asymmetries or structure-fitting or optimal transport or classification

  - relationships

    - core solution functions used
    - adjacent/related solutions
    - side effects (closed system or leaks variance)
    - composability (cooperates with other solution functions)
    - order/position in solution chain/network (if it needs to be used with other solutions)
    - structures & interface queries that can produce this solution


## Common solution functions/strategies

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
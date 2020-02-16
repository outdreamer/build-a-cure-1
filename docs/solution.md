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

    - problem metadata manipulation (changes problem space, postpones solving problem, matching problem with other problem to neutralize both)

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

    - time limit (only applicable in a certain time window)
    - abstraction (structural/conceptual or specific to context)
    - reusability (only applicable once, as with solutions that are easily identified or stop working once you use them the first time)
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


## Solved problem types

  - solved optimization problems

    - find optimal path

    - find optimal distribution

    - find matching structure

  - solved filtering problems

    - break problem into smaller problems & combine solutions of sub-problems

    - filter/rank variables (PCA/ICA/dimensionality reduction methods)

    - classify/differentiate/group


## Transforming problem into solved problem

  - every time you transform a problem into a solved problem, you risk losing information or using a structure thats inappropriate for that problem 

    - if a problem is in a state of flux & about to become another type, or about to merge with another problem, making the default solution method inadequate
    - if info is misleading or incomplete

  - every problem can be translated into the common solved problems:

    - some are more optimal than others
    - some have requirements that are fulfilled
    - some are more adjacent (require less transforms) to the problem



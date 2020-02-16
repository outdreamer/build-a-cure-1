# Solution Object

## Attributes

  - types

    - solution generator

    - solution framework (limits reducing solution space)

    - problem decomposer (reduces problem dimensions)

    - interim solution (common components of solutions, like a granular solution strategy)

    - problem metadata manipulation (changes problem space, postpones solving problem, matching problem with other problem to neutralize both)

    - solution function built on core functions:

      - apply
      - derive
      - fit/match

    - problem-type specific (only handles asymmetries or structure-fitting or optimal transport or classification)

    - transforms unsolved problem into solved problem (transforms unsolved problem into an optimization/organization problem)

  - abstraction

  - reusability

  - composability (cooperates with other solution functions)

  - side effects (closed system or leaks variance)


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

  - every time you transform a problem into a solved problem, you risk losing information or using a structure thats inappropriate for that problem (if a problem is in a state of flux & about to become another type, or about to merge with another problem, making the default solution method inadequate)

  - every problem can be translated into the common solved problems, but some are more optimal than others, some have requirements that are fulfilled, some are more adjacent (require less transforms) to the problem



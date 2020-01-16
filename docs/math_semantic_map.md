## Math/Language translation function

  - build math logic/plain language translation function - example: https://adventuresinmachinelearning.com/improve-neural-networks-part-1/
    - in order to implement this, you need to:
      - implement function to break_into_core_functions
      - apply break_into_core_functions() to math and language functions
      - compare both once standardized with break_into_core_functions() & build map of corrollary functions
      - use this as a dictionary for future translation calls
      - the reason is partly to translate and also to make intent-derivation clearer for people who dont like math

    - operator map:
      +: unify
      -: reduce
      /: standardize by dimension
      *: expand by dimension
      ^: apply to itself
      =: match (symmetric despite operation type x)

    - example of operator -> language:
      1. math rule: 
          'W += -alpha * (1.0/m * tri_W + lamb * W)'
      2. structural language version:
          'changes to W take the form of a constant multiplier of (the change in W value applied to the standard of m, summed with a second constant multiplier applied to the previous value of W)'
      3. organized structural language version:
          'initial change between W and previous W based on m, aggregated with a transform of previous W has a constant relationship to output change in W'
      4. abstract organized structural language version:
          'a constant multiplier of previous W and ((the difference between previous & current W) based on m) determine new W'
      5. derived language version
          'the constant multiplier of previous W is different than the m standard applied to the difference multiplier'
      6. structural derived language version
          'constant multiplier of previous W does not equal difference multiplier based on m'
      7. derived math rule:
          'lamb does not equal (difference multiplier divided by m)'
      8. derived math rule with operators:
          'lamb != (change in W)/m'

      - function metadata:
        - intents:
          - 'differentiate influence of change constants'
        - use cases:
          - 'gradient descent'

      - in that example, we went from math rule 1 => math decomposition into language functions 2 => language decompositions 3 - 5 => mapping 6 => math rule 7 - 8

      The overall workflow is:
      - math rule
      - math decomposition to language
      - language decomposition to abstraction
      - abstraction mapping
      - structure application => insight identification
      - math rule

    - example of language -> operator:

      1. language rule: "control the power of power to control power"

      2. operator mapping: "p = x * (p ^ p) + y" (make a function with output: power, built out of inputs: power ^ power)

      3. reductino: 
        "y = p - x * (p^p)"
        "y = p(1 - xp)"

      4. language mapping: "finding the x & y values of that equation would let you control power"

      5. aside from other methods (function query, conceptual mapping), you can continue the translation or reverse it back to language:
        "y can be determined by power expanded by the dimension of (1 - (x expanded by the dimension of power))"
        
        - function query:
          "1 - a quantity" is usually assessing a ratio, such as a probability

        - definition query:
          "power" usually indicates a position having a useful resource, like energy, understanding, or information

        - what ratio can you determine with an expansion of x from power, that when applied to power, produces y?

        - is it possible to determine the winner of a conflict involving a power grab?
          winner = power (1 - (x applied to distance from understanding))
          winner = power (1 - (x applied to informational advantage))

        - apply power to distance from understanding = if the agent has a low distance from understanding (1 - 0.01 = .99) & applies that to some other source of power, they'll win
        - apply power to informational advantage = if the agent has a high informational advantage & applies that to some other source of power, they'll win

        - what is the identify of the other source of power, or is it the general concept, meaning any source of power?

        - relationship query: which objects can interact with information/understanding objects? 
          - information tech, information communication methods, information storage methods, information protection methods, prediction methods

        - the power applied to the second source of power (information or understanding) must be one of the above methods/technologies

        - what do x & y represent? 
          - x may be a constant, which may be a value representing the output of doing an operation on the multiplier
            - x * power = vary power by x, which represents application/implementation/execution success variance
          - y may represent any output of power applied to the ratio of 1 - (x applied to power), which in this example we've assumed to be the winner of a conflict betweeen competitors trying to get some resource
            - y could also be any other output, such as consequences, side effects, contributions to emergent patterns, changes in intents/incentives, priorities, etc

        - translate this back to a linguistic insight:

          "to optimize power usage (resulting in output y), use two coordinating sources of power, and expand x by one source, get the ratio, then expand it by another source"

        - what do operators like "expand" (which we assigned to the multiplier operator) mean for human users?

          - multiplication is a type of combination operator, that takes an item and pairs it with every object of the other item to generate an object of a number of dimensions equal to the number of multipliers (4 * 5 = a rectangle of 4 rows and 5 columns)

          - when we say something like "expand information by power", we're saying, "apply information to every object within power" or "apply power to every object within information"

          - the output insight is: "to control power, control the inputs of power"

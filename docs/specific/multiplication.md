# Multiplication Object


  - strategies:

    - break problem into smaller problems:

      - example: 
        - 'rather than multiple x by y, find out how many x by x subset squares exist in x by y and add the remaining unit squares'
        - 'use subsets of a base like base 2'


  - method interfaces

    - efficient subset thresholds (bases)
    - efficient organization methods (frame subsets in a way that takes advantage of simpler multiplication)
    - efficient filters (reduce distance to final number with filtering operations)


  - method concepts

    - convergence
    - similarity (position/adjacence)


  - custom analysis methods:

    - system analysis method to multiply x by x

      - query for interfaces building object relationships: square inside a circle

        - result interfaces:
          - circle/square
          - threshold (the relative sizes of a circle & square that would allow overlap between meaningful identifying attributes like corners & perimeter)
          - sets (embedding one shape in another, overlapping their attribute sets)

        - result relationships:
          - find circle dimensions needed for square of size x
          - find relationship of circle area to square area if square corners hit circle radius

        - use circle area to find square area, which is x by x

    - this is a tangential method that likely requires more operations than multiplying x by x, but if you have that query & results available quicker than lattice or other common methods, it may still be faster
      - another example is adding two triangles to get the area of the square, if you can derive the triangle dimensions allowing for overlap between triangle perimeter & square perimeter faster than multiplying x by x
      - another example is if you have an expanded version of the expansion (x by x by x) and youve computed the division of x^3 / x and have it cached or a divisor method thats faster than existing multiplication algorithms

    - interface analysis:

      - this involves identifying the key interfaces (trajectory, intersection, angle, alignment) of the problem space 

      - a physics simulator could be faster as well - simulating the trajectory of electrons through a square of balls could estimate the number of balls more rapidly than division
        - this is an example of applying a filter (trajectory) to solve a problem in a new way

      - trajectory physics could also be faster - which path from (0,0) to (x,y) involves the fewest summing operations

    - a conceptual query could be faster too:

      - applying one symmetry to another
      - applying one ordered list to another to create an alignment between each pair of values (perpendicular angle) and calculating their intersection (x,y)
      - applying one ordered list (spectrum) to another at the angle where they provide symmetries for those lists if the list values can be negative (perpendicular angle)

  - real world use case of multiplication:

    - when do you apply one variable value to another variable value?
      - when you want to create x sets of x to create combinations & trajectories & pairs of units limited by x & x
      - given the key interfaces (combinations, trajectories, pairs):
        - to get from origin to point B, you need to know the coordinates of (x, x) in relation to your origin point
        - the full set of trajectories & pairs from origin to point B limited by metric values x & x represents the area of x * x
          - if overlaps are removed
          - if prioritizing efficiency/speed
          - without extra information about extra dimensions (topology) between origin & point B
        - in a system limited by four equal sides 
        - or a variable applied to itself, like layer applied to layer to generate the full set of interface layer (types of type, intents of intent) combinations

      - so you apply one variable value to another variable value when you want to evaluate combinations, pairs, or trajectories in a matrix shape

      - you can see how to map a structural problem (whats the area of x & y) to a semantic problem (how to calculate all possible combinations, pairs, trajectories between two ordered lists)?

      - just like finding midpoints of square & adding diagonal internal square connected by midpoints & four corner triangles may be faster

      - also like an ordered list (x * y) is the same type as parameters (ordered lists x & y) so mechanics of 'ordered list' type spaces can be exploited to find efficiencies to combine ordered lists with the 'apply method', where metadata (count) of one ordered list is used to generate duplicates of the other, retaining order

      - with simple multiplication, identifying key interfaces for efficiency (phase shifts):
          - 4 x 5 (original operation)
          - 5 = 1/2 of 10 (symmetry finding of middle value, which may be low cost operation)
          - 4 x 1/2 = 2 (symmetry finding of middle value, which may be low cost operation)
          - 2 x 10 = 20 (addition of 10 + 10)
        - this is finding the proportion of one multiplier to a standard (10)
        - the reason you'd use 10 is that it standardizes the problem to a simpler problem, which is counting steps (addition of 10 + 10 is simpler than 5 + 5 + 5 + 5)
        - the interface of 10 is not just significant for its positional value but also because when you reduce everything to the standard of 10, some operations get simple enough to be a phase shift 
          (20 x 10 shifts 2 to the next digit position and adds a 0)
        - phase shifts (thresholds/boundaries/intersections of attributes) are an important concept for predictions
        - phase shifts are another key interface to evaluate the problem from - how do you find the important thresholds in a problem space?
          - you can use variables like digit position to derive that anything that changes the position is an important threshold, and from there you'd find 10 as a standard
          - the reason 10 is a useful interface is because it makes operations like multiplication more efficient, as rather than apply one number by another (10 x 20) you can just do a phase shift operation (change position of non-zero digit and add a zero in first position)
        - this is for when you dont have all the information and you dont already know the relationship between these two variables or why & when a phase shift provides an efficiency

  - this is an example of how you could map an abstract/structural solution to another interface, like one with agents/positions and intents/directions

  - deriving existing methods:

    - lattice method:

      - identify concepts:
        - alignment/position
        - type subsets (where type differentiates subsets by digit position)

      - from concepts, identify conceptual strategies:
        - break into sub-problem (unit operation: multiplying a pair of digits) to standardize operation objects (adding objects of similar type - one digit at a time) to obtain product sum for digit position

      - from strategies, identify variables:
        - digit pairs
        - digit position
        - order of addition of subset products

      - from variables, identify intents & intent order, for overall intent (expand x by y)
        - find structure that allows pairing of digits from each multiplier (matrix)
        - find sub-structure that allow examination of subsets (perpendicular intersection)
        - isolate multipliers by digit in matrix (align multipliers across row & column)
        - identify subsets (digit pairs from each multiplier) by perpendicular intersection
        - multiply subsets (products of digit pairs from each multiplier)
        - store subset product in perpendicular intersection
        - identify property indicating same digit position (adjacency - example: second digit in column 1 is same digit position as first digit in column 2)
        - modulate adjacency to align digit positions (store subset product diagonally to allow straight line alignment of digit position values)
        - order/prioritize subsets (smallest or first digit position added first)
        - add subsets in order, retaining order of sums
        - identify semantic position of sum order (digit position in base 10 number system)
        - position sums in digit positions in order (maps directly to digit position in base 10 number system)


# Existing Methods

## normal modern method

  - multiply digits of each number & sum the products
    - grid method multiplication is a way to visualize this

  - lattice multiplication
    - method of organization that involves chained summing of digit-position-aligned subset products, where diagonals represent digit positions

### adjacent method

  - multiply adjacent numbers & subtract/add to correct after multiplying adjacent numbers
    - rather than multiplying 9 x 11, 
      - multiply 9 x 10 (adjacent number to 11 thats easier to multiply at scale)
      - add 9

## Historical methods

- https://en.wikipedia.org/wiki/Multiplication#Historical_algorithms

### chinese method

  - "rod calculus involving place value addition, subtraction, multiplication and division"
  - decimal multiplication table

### Russian method

  "To do the method, begin by writing the two numbers you want to multiply at the top of two columns. 
  In the left column, you progressively halve the number and take the integer floor of any “and a half” values, all the way down to 1. 
  In the right column, you double the number as many times as there are digits in the left column.
  With your completed table, scan through and remove any rows where the left column has an even value. That includes the original term at the very top.
  Now, when you add the remaining terms in the right column, you get the solution."


### Egyptian method

  "The Egyptian method of multiplication of integers and fractions, documented in the Ahmes Papyrus, was by successive additions and doubling. 
  For instance, to find the product of 13 and 21 one had to double 21 three times, obtaining 2 × 21 = 42, 4 × 21 = 2 × 42 = 84, 8 × 21 = 2 × 84 = 168. 
  The full product could then be found by adding the appropriate terms found in the doubling sequence:
  13 × 21 = (1 + 4 + 8) × 21 = (1 × 21) + (4 × 21) + (8 × 21) = 21 + 84 + 168 = 273."

### Babylonians

  "The Babylonians used a sexagesimal positional number system, analogous to the modern day decimal system. 
  Thus, Babylonian multiplication was very similar to modern decimal multiplication. 
  Because of the relative difficulty of remembering 60 × 60 different products, Babylonian mathematicians employed multiplication tables. 
  These tables consisted of a list of the first twenty multiples of a certain principal number n: n, 2n, ..., 20n; 
  followed by the multiples of 10n: 30n 40n, and 50n. 
  Then to compute any sexagesimal product, say 53n, one only needed to add 50n and 3n computed from the table."

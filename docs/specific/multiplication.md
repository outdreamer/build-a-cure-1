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

  - system analysis method:

    - to multiply x by x

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
    - a physics simulator could be faster as well - simulating the trajectory of electrons through a square of balls could estimate the number of balls more rapidly than division

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

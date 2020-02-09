# Multiplication methods


- method object:

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
    - similarity (adjacence)


## normal modern method

  - multiply digits of each number & sum the products
  - grid method multiplication
  - lattice multiplication

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

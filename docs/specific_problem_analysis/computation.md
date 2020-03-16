# Computing/distribution

    - identifying servers that have resources optimized for various pieces of task
    - identify optimal server path to break down task into pieces with operation order that can be done at each communication step to operate under communication cost thresholds
    - storing metadata at definition time to make computation distribution/delegation/communication calculations pre-computed on some level
      - metadata like:
        - data computing request potential
        - data variance/patterns
        - matching data variance/patterns with sub-structures like value functions:
          - for compartmentalization & storage optimized for access:
            - if you can fill a math progression or other function having inherent position with data, you can store progression function & data map, and use that structure to find data quicker
          - for quick computation:
            - if you can fill a math progressionw with data, you can access computed values by position (if data is in the 3rd term, you know what the data will be before looking up the data)
        - data range/data type/data probability distribution & change patterns can be computed after definition time

    - error types

      - intersections/processes with obvious error opportunities:
        - data splitting
        - data merging
        - data indexing & caching
        - computation indexing & caching (false positions to answers, false answers)
        - computation timing
        - computational order error (non-commutative)
        - connectivity

      - non-obvious error opportunities or lack of optimization

        - organization method of distributed datasets allows for random or specific task optimization, rather than absolute optimization 
          (multiple indexes for same dataset or storage of metadata properties & locations in each dataset so many organization methods can be used on same dataset)

          - theres a lot of room for pre-computing, pre-indexing, & pre-combining within & across data set combinations

        - lack of relationship metadata between datasets 
          (which dataset contains more items of type c, etc)

        - identifying key vertices (factors on an analytical layer) to split the data set beforehand and creating multiple clusters split in different ways likeliest to be needed

          - identifying key splitting order & intervals at query time
          - identifying optimized stack components for computation tasks
            (servers/file systems/folder structures/databases/indexes/metadata/order/organization/languages/algorithm/data structure)

          - identifying mix of processes/computations that can be applied to dataset to optimize a task
            - one subset can be processed linearly, another can be processed in parallel, another can be pre-computed
            - another subset's handler can be evaluated at runtime if its likeliest to change
            - mixing these on the same dataset may improve performance

    - example of using function chains (operations done on an input/object) to predict position & other data structure metadata without traversal

      - if a list contains integer range from 0 to 10, and the compatible set of operations for the output of the list definition includes split & reverse functions, and the probable parameter of the split function is 2 (split list by midpoint), then the probable position of value 7 is:
        - position 4 if reverse is applied
        - position 1.3 if split(2) then reverse is applied
        - position 3 if split(2) is applied

      - so any call to find index of 7 in the list can calculate & check that set of probable positions rather than all positions
      - it can also check which operations were done in which order on the original list (function chain) to determine position without traversing list

  - storing grouped data in different structures according to their value attributes & relationships
    - storing a list as a network structure of values (pairs of connected values, organized by similarity or other metrics to reduce traversal time)
    - storing a list as a network structure of generators/transformation functions (where hub nodes represent generative functions for the values around it)


- idea; recomputing new encryption key pair & re-encrypting any content at rest using algorithm stored on systems legitimately using the key so that attackers have a limited time window to use that key pair even if they crack it
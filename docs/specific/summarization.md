## Summarization algorithm

    - add summarization algorithm converting text to a set of network graphs, then selecting most relevant network graph for headline

      - isolate unique points, reduce to standard words, identify newest points & create a network graph

      - repeat that process for various types of points (different intents, different abstraction layers) and determine probable matching set (intended by author) and the most relevant set (relevant to audience)

      - "people can coordinate votes to prevent coordinating votes"
      https://www.vox.com/2020/1/29/21094603/supreme-court-decision-on-immigration-neil-gorsuch-democrats

      - "not every combination of constitution system usage (population, distribution, & party identity) is beneficial for every party agenda"
      https://www.vox.com/policy-and-politics/2020/1/30/20997046/constitution-electoral-college-senate-popular-vote-trump
        - doesn't mention an improved version of the system that would avoid these sub-optimal combinations

    - write function to identify contradictory information (retracted studies, false information, conspiracy theory (anti-vax), opinion) & selecting least likely to be false
      - this will be useful when youre pulling non-research study data, like when youre looking up a metric or compound if you dont find anything on wiki

    - write function to rank & identify authoritative sources (wiki is more trustworthy than a holistic or commercialized blog based on editing metadata)

    - function to identify & remove common article intents with high probability of falsehood to reduce it to just facts
      - add intent matching so you can compare treatment relationships with article intents to see if its actually a sentence with a treatment in it
        - finish treatment failure condition - make sure it adds nothing if theres no treatment in the article - this is related to intent function

  - add to translation/summarization alg:

    - process translated as "adding dimensions to difference in mass (powers of the base) increases vacillations in wave according to collision momentum transfer rules between limits"

    - notice that a vacillation decreasing in momentum would produce a fractal/spiral shape with a symmetric transform done - and that could produce a circle under certain conditions

    - vacillation = pendulum swing with only one initial force application 
      - with curvature applied this would be a spiral approaching a center
      - if the curvature transform was balanced in the right way (like an equivalent effect as zooming in), it wouldnt trend toward the center but produce a circle

    - this type of problem can be indexed as 'core function combinations'
      - example: 
        - the core functions here are 'flip around axis' (similar to inverse, identity matrix, rotate)

    - how do you identify core functions in a list:

      - algorithm would look something like this (at definition time):
        - store central values about which other values vary (like clusters of centrality aggregators)
        - store operations to generate set of values around that particular central point in each cluster
      - a way to generalize this is to find the symmetries (other than just centrality) to gather points around when generating sets of values to derive core functions from

    https://www.quantamagazine.org/how-pi-connects-colliding-blocks-to-a-quantum-search-algorithm-20200121/

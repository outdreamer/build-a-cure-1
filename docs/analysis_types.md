# Analysis Strategies for Application in Specific Problem Spaces

## Work distribution & incentivization

  - system users should always be system builders, so their incentives don't crystallize into an irreversibly static state

  - users should be builders by the end of each game

  - the questions of each problem space can be mapped to user tasks within a game, defined by a set of rules creating similar questions answerable in the game

  - when builders have taught enough users, builders should move on to being users of another game, in an alternating cycle

  https://twitter.com/remixerator/status/1217718371816329217

## Randomness Generator

  1. calculate maximal variance points in a system (variables most unrelated to all other variables), and equalize their contributions

    example:
      - "cloud size" is directly related to adjacent water, wind patterns, temperature & elements in adjacent air
      - "cloud size" is indirectly related to moon phase (influences wind patterns), sun exposure (influences temperature), pollution (influences elements in air)
      - "cloud size" is very indirectly related to astrology 
        (influences moods, emotions, subconscious, dreams, & market decisions, which influences market trends, which influence side effects of production like pollution)
      - cloud size is so indirectly related to astrology that it may be considered independent of astrology, despite the fact that every object is inherently related to all other objects
      - we can say that "cloud size" has a "maximal causative distance" or "minimal dependence" on "astrology"
      - other ways to find a variable with minimal dependence on some other variable include:
        - varying abstraction level:
          - the concept of 'balance' is indirectly related to everything but only specifically related to a small subset of things (justice, symmetry, etc), most of which are either conceptually abstract, or mathematically abstract (specific to mathematics, like a low-level operation or attribute that can be calculated numerically)

        - querying its dependent variables 
          (cloud size is caused by element distribution, so element distribution is independent of cloud size)
          - in reality this is not real independence, because many dependence relationships are circular, either 
            - directly (one circular loop between two nodes), or
            - indirectly (the output dependent node, cloud size, goes through many systems before returning some input requirement of the input independent node, element distribution)
            - this is because there are very few to zero ways to generate an output that has no side effects on input requirements (input inputs)
              - an example is "victimless crimes" like ejecting junk into space, which may not impact us immediately but definitely will return some causation (in the form of required inputs to some process) to our species eventually
      - another example is "corners of a square":
        - each side of the square is equal, so it's equally likely that the "square" system will generate a movement of balls within the square, that pushes a ball to one of its corners
        - the corners represent a maximal variance variable (corner), which are unique in that if a ball is in one corner, it necessarily cannot also be in some other corner
        - this is the foundation of identifying not just maximal variance-generating independent variables in a system, but also system nodes (gathering points of inputs/outputs) & interfaces (standards)

  2. design systems that optimize the number of independent max variance points
    - how do you design a system with maximal variance-generating independence points?
      - take the problem of a square - how would you generate the corners such that:
        - each corner is unique compared to other corners
        - each corner exerts the same influence on the ball movements within the square
        - each additional corner adds to the variance of the ball movements
      - eventually if you add too many corners, you get a circle - is this the maximal variance implementation of a square, or is there some point between a square and a circle with more variance-generating points than either?
        - it depends on the variables that youre trying to optimize the randomness of - if they can occupy any point on the circle, a circle may be more appropriate - if they can only occupy a corner, you need to find some combination of corners that is not a circle in order to maximize their variance

  - mentioned here:
    https://twitter.com/remixerator/status/1148816151125712896
    https://twitter.com/remixerator/status/1004578257637953537
    https://twitter.com/remixerator/status/1004578256820064257

## Exploit Opportunity Analysis

  - exploit opportunities involve a divergence between some expected legitimate input/output & actual malicious input/output

  - inputs providing exploit opportunities can involve input assumptions related to:
    - hardware (memory, CPU, threads, queries)
    - language (stack/heap implementation)
    - storage management (cache mechanism, garbage collection mechanism, optimization)
    - condition (limit, metric)
    - code (default tool, code, tool version, tool source, tool-management tool)
    - config (definitions)
    - permission (intended permissions vs. allowed permissions)
    - intents (user, dev, protocol)
    - actions (user (explicit decisions, implicit preferences), dev (auto/forced updates, data corruption fixes), automated (script running past its intended window of use), third party (browser, OS, anti-virus, isp))
    - functions (retrieved, generated, lack of assumption coverage of input space)
    - parameter values
    - outputs (info leaks)

  - exploit opportunity types:
    - unenforced expectations of rule implementation methods (protocols)
    - intent-expectation divergence
      - expectation: "input intents are legitimate"
        example: using legitimate input intents (login, use form, retrieve results) to build malicious output (info about data source/query engine/caching mechanism/filter used)
        (searching big/complex/varied queries to find limits of query engine & matching with known query engine limits)
      - expectation: "output intents are legitimate"
        example: using legitimate tools (database query, session, form) to build malicious output intent "retrieve info from unauthorized account"
        (searching for theorized terms used by other user to find out what other user is seeing in search results that could be used to derive other user's information exposure & habitual use)
      - expectation: "input content is legitimate"
        example: sending spam emails with target keywords designed to train theorized spam-detection AI model to target associated keywords in emails
      - expectation: "input use is legitimate"
        example: sending legitimate requests to establish pattern of use that can later be exploited 
          (login from many locations/devices simultaneously from beginning of use to avoid identification as hackers later)
      - expectation: "inputs cannot be used to get unauthorized info x"
        example: 
          - "using system stat/monitoring logs to identify readable folders by logger process"
          - "injecting rule to remove comment chars in regex filter to activate disabled code not evaluated by tests"
          - "separating submitted chars with delimiter to accumulate code chars in non-code files to make them eventually identified as code once full code char string is accumulated"


## Vuln potential of a solution

  1. identify conceptual/type interactions of the solution
    example: explore the interaction of random applied to random (or algorithms applied to themselves, like hash of a hash) for possible interference opportunities


## Invention Prediction

  1. Reverse-engineer: apply known useful functions (combine, reduce, standardize, compare, duplicate, randomize) 
    to fulfill common useful intents (predict, verify, find, etc) & assess value of output product in problem space

  2. Conceptual query: apply structure to conceptual combinations & check matching problem spaces if the output product has value for an agent in that space


## Calculating which calculations are optimal

  - given that certain calculations have known cost estimates, which calculations are optimal, in what order/frequency, and given what information?

  - example: when deriving a prediction function, when do you query for function & function generator patterns, when do you request more data, when do you continue assessing regression, when do you apply standardization?

  - is it optimal to solve this problem set or another problem set, or deploy resources to both?

  - solution distribution: should this solution be deployed at run time, in a specific system, should the solution be stored as its generator function, etc


## Bio System Analysis

  - nth iteration simulations: analysis that treats cyclical, recursive, cascading & iterative processes as trade loops between positions & systems
    - example: in addition to analyzing how a drug is metabolized:
      - how its structure will interact with other structures
      - how the resulting structures after the nth-interaction will interact with other resulting structures, etc
      - how the dna of a probiotic or other microorganism treatment could get re-purposed by microorganisms
      - how the activity of a gene could get accidentally impacted in other pathways & which of those pathways are possible given a treatment
      - how an interaction can be minimally modified to produce extremely different results
      - how nth-iteration interactions will be timed with other processes cycling in that time
      - how causal cascades can cycle to be interactive with the treatment
      - how functionality gaps or interactions at nth-iteration can provide opportunities for mutation & other randomness sources 

  - given the known vulnerabilities of the bio-system:
    - which problems are solvable (killing pathogen, deploying a substance to a position) with what methods (evolution, medicine, stressor distribution)
    - which problems are inevitable
    - which problems are solvable with auto-generated vs. external resources
    - which stressor patterns can prevent which problems

## Protocol Recommendations
  
  1. Auto-update crypto keys/algorithms to use constants that are always guaranteed to be below x% risk that they'll be hacked given common computational resources.

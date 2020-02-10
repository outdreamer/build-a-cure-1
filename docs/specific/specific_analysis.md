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


## Optimization

  - Determining which queries/calculations are optimal

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
  

## Optimal Resource Trades

  - famine, farmland, mine field location data
  - cost of removing mines
  - cost of transporting people
  - which land is for sale & at what cost
  - how much land is necessary to support a person
  - set of resource trade sets across projected weather patterns for next 10 years to generate migration paths
  - which farmland is more optimally used for something else (harvesting other natural resources, water supply, city)
  - which cities have industries to support new workers moving there
  - what distribution of cities/farms is optimal for reducing resource transportation cost
  - how much does it cost to train someone to maintain a garden
  - what is the configuration of farmland & farm input supply chains that reduces supplies transportation cost
  - what is the import/export potential of each region (which crops & other resources can they produce)
  - what distribution of industries should occur by distance from ocean/water source
  - what infrastructure can optimize farmland at lowest cost
  - which laws are commonly reused across governments & are generally agreed to not be exploitative of citizens
  - what distribution of courts/police/lawyers is necessary to distribute fairness in markets
  - what compoments of this can be automated/updated automatically & which should be done with manual input
  - what tools do they need other than farmland 
    (water source, sun, cell phone, charger, electricity, portable wi-fi generator, app to track their assets, app to trade by phone, app to request supplies/loans)


## Ideas


### To do

  - solution type: balance info asymmetry
  - matching


### Crypto

  1. use predictive tools to predict transactions & calculate them in advance to speed up tx

    - this would assess people's known resources to build an index of global demand/supply, then calculating through these resource distributions, economic incentives for trades, social networks, platform dominance, & product availability & findability (search results rankings) - which tx were likely to happen where for which products, then calculate those tx in advance


### ML

  1. not only does ML have the potential to derive combinations like type paths & insight paths, it can derive other system/interface metadata such as core functions:
    - example:
      https://techxplore.com/news/2020-01-alphafold-protein.html

  2. you don't have to rely on disorder to detect order if you have an ordered way of generating disorder patterns

    https://techxplore.com/news/2020-01-brain-like-network-disorder.html


## Security

  1. one-time use stack (network, os, app) in extension of one-time password

    - when ISP tech is distributed (network drones/satellites), you can also switch network providers for each message, in an agreed-on stack-switching pattern determined at start of conversation, using agreed-on pattern decompression algorithm


## Bio
  
  1. Look for symmetries in nature because that's where the variance is likely to be routed
    https://phys.org/news/2020-01-lizard-snake-size-unrelated-climate.html

    The symmetry presented by stability provides a platform for variance (coronavirus) to develop.


## Computing/distribution

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


## Learning models

    - brain learns through various reward models:
    - short term rewards: storing useful information
    - long term rewards: storing useful functions
    - adaptive/reusable rewards: storing functions by relevance or abstraction
    - on-demand rewards: storing function-generating methods/interfaces
    - reward potential-maximization: storing derivation method core functions


## Election security

  - apply your other solution to election security:

    - given a range of expected votes in a category, how much does final result deviate from expected votes

      - if an attribute like intelligence is associated with a particular vote, and outcome count deviates from known attribute count to this degree, what set of ratios of deviation can be attributed to noise and what percentage to interference/fraud?

      - what is the path between the determining attribute (intelligence) & the output concept (interference/fraud)?
          - is lack of intelligence a few transforms away from the output concept
            - meaning, if stupidity is associated with voting for the x party, is interference actual fraud given that its still indicating the expected stupidity rates in population?
            - or if stupidity is associated with voting for the x party, is the result inevitable, regardless of how it's achieved (they wouldve voted the same way as the fraudster tricked them into voting or artificially chose their vote with data manipulation)


## Navigation model

    - predict variance sources & ratios:
      - type/shape/movement/interaction interface variance sources:
        - is an object that moves in restricted directions likely to be sentient life (delivery robot)
        - can sentient life move in restricted directions (drug addict, multi-tasking, drunk)
        - can interactions predict movement types (waving across street, looking at phone, predicting drivers' moves, checking street for cars/behind car before crossing/backing up)
        - are objects of a certain shape or size associated with different movement types (small objects are faster, larger objects have more obvious momentum physics, smaller objects likelier to be capable of flight)
      - assumption/hypothesis interface variance sources
        - are assumptions of a certain variance level given a certain minimum information associated with prediction accuracy
        - are multiple contradictory starting hypothesis associated with higher prediction accuracy, if so, with what degree of variance between hypotheses?


## Quantum physics

  - examine when randomness can masquerade as entanglement due to limited options of core function interactions due to the system development being in an initial phase
    https://phys.org/news/2020-01-supercomputers-link-quantum-entanglement-cold.html

  - information organized by relevance & efficiency

  - useful for computing attribute & variance flow as well as flow between flow of energy into measurement delivery 
    (optimize energy distribution between particle position/spin attributes according to measurement limits)
    https://en.wikipedia.org/wiki/Partial_differential_equation

  - look for new objects in inter-system physics - as an object occupies a current & target system as well as the space in between that isnt classifiable
    - what physics apply between systems (space-times here)
      https://arstechnica.com/science/2020/02/white-dwarf-causes-strange-relativity-effect-called-frame-dragging/

  - examine how info is being destroyed in black holes & in quantum physics - is this a process that can be used for encryption or is the info irretrievable?

  - scale transitions

      - give example of emergent effects of phase/scale transitions across threshold values that exert more variance than systems can hold

      - quantum scale transitions as delegation of information to optimal/efficient/low-energy positions
        - appears to be in multiple positions until it determines which position is more efficient or easier to maintain
      

## Communication

  - tokenizing common content/content-generation functions on clients & in communications
  - calculating computable sub-components & delegating computation to nodes on network trajectory
    - this means if executing a process on content isnt efficient on the source system, calculate network trajectory to route communication toward servers that are better for that computation & start sending content unprocessed and process it on those servers
    - if you had a communication protocol that supported common content tokens, sending content to servers that are better at converting content to tokenized form would be better than a random or non-optimized server
    - sending converted tokenized content & the id of the tokenization map on different routes adds some interim security
  - using neutrinos as a way to speed up communication using them as jumping-off/charging points

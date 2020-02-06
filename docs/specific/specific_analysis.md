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

  3. Identify necessary structure and identify interface combinations/trajectories that can generate that structure


## Determining which queries/calculations are optimal

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


## Cancer & Stressors


  ### Predictive tools

    - prediction function for computing which pathogen combination will produce the target antibodies
    - prediction function for drug impact between species, mapping species transform function to changes in drug impact
    - prediction function for what ratio of compounds is present in nutrients & drugs with differing success rates
      https://phys.org/news/2016-07-happy-hormone-calcium-cows-humans.html
    - functionality prediction functions, indexing genes, structure & sub-components by functionality


  ### Theories

    - does cancer eventually try to build its own organ or bio-system, so letting a tumor survive for a period of time could trigger internal tumor immune processes?
      - tertiary lymphoid structures act as a regulatory system of the tumor, adjusting its pressure & distribution
      https://medicalxpress.com/news/2020-01-scientists-powerhouses-tumours.html

    - https://twitter.com/remixerator/status/1216501559787282432
    - https://twitter.com/remixerator/status/1138707042187661312


  ### Interfaces

    - attack points
      
      - causal level

        - attacking higher up the causal stack means attacking cancer's evolutionary & learning processes, so it cant evolve resistance to drugs

      - object level

        - attacking on the mutation level

          - how to trigger loss-of-function mutations of cancer mutations
          - how to trigger mutations of mutations (reverting to original state)
          - if chains of mutations are the combined trigger, can mutations be inserted in that chain to push it in another functional direction

      - system level

        - evaluate position as a variable (whether TADs & gene position & adjacent genes can be rearranged to prevent mutations)

        - evaluate alternative backups to commonly mutated genes/proteins/enzymes - how do you trigger functionality that evolves backups

        - genetic level

          - can genes producing a commonly mutated cancer-causing gene be adjusted to produce functionality without vulnerabilities exploited for cell division

        - functionality level

          - can system structure be changed so variance is increased & so functionality is allowed to accrete to produce backup functionality

        - signaling level 

          - 

    - system 

      - deviating from genetically optimal environments as a cause of systemic stressors that lead to cancer
        - if you have night owl genes but force yourself to be a morning person
        - if you have genes that can handle low calcium levels but you eat a lot of calcium
      - can you delegate computation to tumor cells to prevent them from splitting
      - cancer tends to make use of whatever tools already exist, which means its moves are predictable given available resource combinations
      - does cancer also have unpredictable activity in generating new tools, not just adjacent combinations of existing tools but systemic tools like new pathways?

      - from a system that has systemic issues that seem unexplainable by known rules, seek a new object (interface, system, rule, type, attribute, etc)
        https://medicalxpress.com/news/2019-12-artificial-intelligence-previously-unknown-features.html

    - attribute

      - invalidating
        - toxicity (invalidates usefulness of a treatment)

      - variance
        - binding variety
        - movement types (rotation, density distribution)
        - adjacent interfaces (receptor, immune, etc)

      - signaling
        - ionization
        - surface structure
        - vocabulary (interpretability of signals)
        - state change metrics/limits

      - support
        - metabolism
        - filtration

    - rules

      - types

        - bind
        - boundary
        - position
        - grouping/accretion
        - distribution
        - testing/assessment/metric selection
        - change
        - regulation
        - communication
        - repair
        - movement
        - duplication
        - request/response handling

    - structural

      - boundaries
      - surfaces
      - receptors

    - many object types can be an interface in a specific system, in addition to standard abstract interfaces
      (function/metabolic interface, system//immune interface, structure/cell interface, communication/nerve interface)

    - stressor

      - change requests, or problems of type 'mismatch' between change demand & change supply

      - stressor accretion/compounding/neutralizing/type patterns

      - patterns in stressor handler gaps
        - which stressor types/handler types are prioritized first
        - what variables influence priority of stressor handlers

      - variable coordination that produces stressors 
        - repeated interactions from static positions or sources of components
        - mismatches
        - allocation of cell division from low priority tasks (maintaining flexibility/elasticity) to high priority tasks (handling excess inflammation)
        
      - lack of usage by genetically/systemically optimal timing linked to illnesses (hormone production & hormone usage)
        https://medicalxpress.com/news/2020-01-sex-linked-earlier-menopause.html

      - muscles have stressor handler for excess lactate, and cell types in other tissues do not
        https://medicalxpress.com/news/2020-01-lactate-prompt-cancer-formation.html

      - trigger inflammation in adjacent areas using pathogens with neutralizing effects or competing for same resources to make different cancers fight
        https://medicalxpress.com/news/2019-12-insights-armies-strategically-stationed-cells.html

      - required nutrients that are not handled well bc of genes from stressor-handling lineage may act as a stressor
        https://medicalxpress.com/news/2010-06-calcium-consumption-prostate-cancer-chinese.html

      - mental processes that generate stressor requests & handlers (future planning, hope, expectations, pressure, empathy, pain management, & perception of potential as a factor in aging & disease)
        https://medicalxpress.com/news/2020-01-racial-discrimination-telomere-shortening.html

        - check whether empathy with terminal patients is associated with higher risk of disease in doctors/nurses

        - link between mental bias & disease from lack of flexibility
          https://medicalxpress.com/news/2020-01-long-term-memory-gating.html

    - processes

      - mutations

        - compounding mutations can be chained with intent analysis to predict which function chains will cause cancer
          https://medicalxpress.com/news/2020-02-cancer-years-diagnosis-earlier.html

        - of the cancers that dont have driver mutations that have been identified, the functionality can accrete randomly, given the host system structure allowing the functionality of cell division to occur

          - for a simplistic example, if the cancer-causing mutation had a triangular shape, then cancerous functionality could be generated by function chains forming a triangular shape, and could also emerge from a corner of the host system where unused functionality accreted

      - electrical

        - charge
          https://medicalxpress.com/news/2019-02-electrical-prostate-cancer-cells.html

        - electrical logic processing
          https://medicalxpress.com/news/2020-01-evidence-previously-unknown-electrical-property.html

        - light

          - timer triggering

          - hormone impact/production

          - can bioluminescence treat cancer
            https://medicalxpress.com/news/2016-03-tumors-cell-electric.html

          - https://medicalxpress.com/news/2016-02-harnessing-power-cancer.html

        - lasers

        - photosynthesis

      - inflammation/irritation

        - examine routes to delegate/distribute/generate histamine using existing bio system resources as an anti-cancer agent from imidazole
          https://en.wikipedia.org/wiki/Histamine

      - learning

      - competition

      - finding/borrowing/generating functionality & other resources

      - energy management (storage, sharing, production, source-switching, conversion)

      - emergent effects:

        - example of emergent effects 

          - there are intended & unintended ways to activate a process, such as cell death

            - apoptosis (cell stressor & stress-handler are aligned with limited side effects in the cell itself ignoring the outer system, as this is a granular function - it gets the signal to kill the cell, and it activates that process)

            - variance injection that triggers cell death in unintended ways (over supply of stressors for cell stress-handlers in ways that produce variance that disrupts the cell membrane from the inside)

            - acidity is a resource for this process, but it can also kill the cell if over-supplied

            - the synergy between histidine & the mechanism of this virus has multiple possible explanations:
              - the virus needed to use existing system resources to be able to attack host cells
              - the virus needed to use an inflammatory agent to hide its activity from immune system
              - the immune system evolved a cooperative process with viruses like this to promote inflammation in a cost-efficient way by delegating it to pathogens

            - examples of ways to generate the above list (and the full version):
              - examine relationships/processes for common priorities (efficiency, reducing cost, cooperation effects, inflammation response)
              - examine inputs/outputs (required resources)
              - examine labor/energy processing (cooperative can be parasitic or symbiotic, where one agent is delegating more labor to other agents, or where labor is being traded evenly)

            - you can permute the other interface objects & object attributes/rules to generate the full list of possible explanations, starting on the most explanatory interface and traversing to other interfaces based on available/derivable information

            https://phys.org/news/2020-02-chemists-unveil-influenza-protein.html

      - function types

        - explicit function (such as 'convert input energy into output structure')
        - implicit function (such as unintended side effects of outputs, interim functions between input/output, and unpredicted emergent functions at scale or across many linked integrated function chains)
        - provide resources used as inputs to activate other functions (a set of molecules that when detached can activate other processes)
        - connect functionality (binding structures)
        - provide platform for functionality (variance allowing functionality to develop on foundational structures)

      - organization (chromosome position, storage compression, topologically associated domains, binding/accretion rules)

        - shapes that have rotation-compounding structures (corners/wheels)
        - https://medicalxpress.com/news/2020-01-inflammation-game-changer-cellular-death.html

      - communication

        - excess energy allows for acquiring extra resources (borrowing functionality from a bacteria farther away, spending more time computing something or testing variations)
          just like excess information is distributed according to thermodynamics

          - if energy is efficiently converted into information in a system (like the cancer system or the bacteria system) that system will require less energy & other inputs overall
            - such as the information of how to acquire information or switch energy sources

          - the distribution of structures within a cup of liquid can influence how quickly the energy dissipates

          - information dissipates according to common priorities like efficiency, but it can be overridden by concentrated energy, like when a cancer cell is surrounded by healthy cells so it shouldnt be able to produce legitimate semblance of signals, but if it has better energy usage (like functionality to acquire information as needed), it may be able to override the healthy cell communication, which is almost costless if they are adjacent neighbors in a circle around the cancer cell, but can still be beaten by more efficient energy storage (able to produce or find information as needed)

          - efficiency dissipates in similar ways - if one source process is efficient, other subsequent processes or attributes may also be more efficient - the efficiency dissipates or cascades through the system, possibly in a compounding way

          - energy can produce efficiency: the government of energy by rules like thermodynamics & chemistry has effects on subsequent process like information retrieval & position (communication & distribution) which can impact energy production

          - summary: 
            - concentrated energy produces information efficiently 
            - cancer cells often have concentrated energy in various formats like mutations, functionality, information, etc
            - the thermodynamics of energy impact how efficiency, communication, information, & other outputs of energy are distributed

          https://phys.org/news/2020-01-supercomputers-link-quantum-entanglement-cold.html

        - still relies on distribution of cells for cell communication (enough normal cells around mutated cell to block it from joining other mutated cells)
          and relies on the mutated cell not already having resources to exploit surrounding cells as energy sources

          - dishonest signals that provide some benefit to surrounding healthy cells (pay a toll/tax/bribe for safe passage) have a higher likelihood of preserving cancer growth

          - the advertisement is an inherently false signal that has filters/tests built-in to the bio system so that correct signals can get through

          - legitimate signals are likelier to be:
            - local (granular function)
            - verifiable on several metrics (where a false signal would fail)
            - no side effects that dont have handlers built-in (for example, they dont cause mutations or output toxins without handlers)

          - the reason the system has these filters is to avoid over-handling a stressor, as it occasionally has signals that look like stressors which it has to avoid over-handling, like how the immune response can look like a stressor when its a stress-handler, so these filters exist to make sure the distinction between those categories is determinable most of the time

          - these filters keep some openings functional, but these filters dont make every variance opening safe - for instance with energy sources, which there are few regulations on

          - the insight of the process is 'ensuring output of false signals is an input for legitimate cells to communicate'

          https://medicalxpress.com/news/2020-02-cancer-easy-cell.html

        - blood flow

        - oxygen supply

        - quick metabolism/distribution of unnecessary clusters

        - look for intersection between "happiness" hormones and cell communication 
          https://phys.org/news/2016-07-happy-cows-nutritious.html

        - cells experiencing stress cluster together, which reduces cell communication & leads to cancer
          https://phys.org/news/2020-01-cells-stress.html

        - dairy congests system & interferes with cell communication, leading to higher cancer rates in some cancers, particularly gender-specific or hormonal organs & filtering organs
          https://medicalxpress.com/news/2019-10-dairy-products-higher-prostate-cancer.html
          https://medicalxpress.com/news/2013-03-high-fat-dairy-products-linked-poorer.html
          https://medicalxpress.com/news/2014-11-lactose-intolerants-cancers.html
          https://medicalxpress.com/news/2011-08-poor-awareness-bowel-cancer.html

    - objects

      - drug
      - proteins, enzymes, lipids
      - pathogen
      - mutation
      - antibodies
      - memory cells


# Ideas


## Solution Type: balance info asymmetry


### Crypto

  1. use predictive tools to predict transactions & calculate them in advance to speed up tx
    - this would assess people's known resources to build an index of global demand/supply, then calculating through these resource distributions, economic incentives for trades, social networks, platform dominance, & product availability & findability (search results rankings) - which tx were likely to happen where for which products, then calculate those tx in advance


## Matching


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


## Scale transitions

    - give example of emergent effects of phase/scale transitions across threshold values that exert more variance than systems can hold

    - quantum scale transitions as delegation of information to optimal/efficient/low-energy positions
      - appears to be in multiple positions until it determines which position is more efficient or easier to maintain
    

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

  - are the best encryption functions those with the fewest symmetries?

## Communication

  - tokenizing common content/content-generation functions on clients & in communications
  - calculating computable sub-components & delegating computation to nodes on network trajectory
  - using neutrinos as a way to speed up communication using them as jumping-off/charging points

## Hacking

  - assumption manipulation
    - threshold/metric/condition manipulation
    - input manipulation
    - verification gaps


## Bug Identification

  - non-standard exploit-finding patterns:
    - faked signals for unrelated purposes
    - output communication/processing chains mapped to intents
    - sub-intent combinations/chains as intents, assumptions as exploit opportunities (assume code functions are the primary exploit layer to focus on, rather than systems or processes using functions like 'garbage collection' or 'memory optimization')
    - indirect intents (actions not clearly benefiting any agent like 'transporting message', which form extra opportunities when combined with other actions not clearly benefiting any agent, like activities considered necessary or default)
    - matrix of compatible tech & possible alternate intent paths allowed between intent limits/filters


## Prediction

  - surprising patterns often come in the form of:
    - compounding patterns that go unmeasured (black swan pattern)
    - compounding patterns that are measured in ways that they dont vary from expected patterns (different dimension as a host of variance)
    - compounding patterns that are measured in ways that vary from expected patterns but not at point of measurement (wave function & line intersection)

  - expectation vacillation is optimized when neither extreme is expected permanently & expectations gravitate toward local inflection or threshold points
    - expecting evil & expecting sainthood are both sub-optimal in most situations, 
      whereas expecting moderation is usually more useful bc it allows more freedom, and more freedom allows more self-optimization than using forced optimization rules, 
      which change slower than local (self) optimization rules

  - prediction functions

    - its not important to just identify the best-fit balancing bias/variance for a model, its also important to identify:
      - the adjacent models that exist with common distortion functions applied to the best fit model
      - the change patterns applied to the best fit model


## Code Conversion

  - syntax rules
    - type declarations (python libs for this)
    - conditions (try/except => TryOrElse)
    - returns

  - code conventions (not enforced but still need to be translated per conventions of project)

  - function lookup & mapping:
    - common function mapping (map, filter, zip)
    - input/output/intent/use-case matching


## Test Automation

  - test generation

    - unit testing:
      - assumptions
      - inputs/outputs
      - conditions
      - intents/use cases

    - integration testing: 
      - function chains
      - system context
      - user decision history (visited insecure website/cleared cache)

    - identify objects that need to be mocked bc of security/deployment constraints

    - generate assert statements, conditions, and mock objects as needed
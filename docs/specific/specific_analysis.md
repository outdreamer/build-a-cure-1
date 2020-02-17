## Ideas


### To do

  - solution type: balance info asymmetry
  - matching


### Resource distribution

  - example: allocate hospital equipment as needed


  - stat analysis: 

    - gather data on suspected variables as best predictors of optimal distribution 
      - patient mortality 
      - patient ratings
      - employee ratings
      - employee efficiency
      - patient/employee infection rate
      - equipment costs (cleaning, replacement)


  - system analysis:      

    - attributes:

      - source variables:

        - equipment state (cleanliness/functionality)
        - test effectiveness (accuracy/completeness/cost/risk)
        - operations inefficiencies (variables are not being checked completely due to gap in oversight)

      - target variables:

        - budget optimization
          - keeping resources at maintainable/computable level 
            - only have x equipment given y cleaning supplies & z employee hours
            - only aim for b predictions given budget for c neural network trainings, allowing room for new prediction requirements
        - patient mortality
        - patient infection rate from equipment
        - patient ratings

      - vertices:

        - points of infection
        - points of pathogen resistance to handling methods (medicines, filters, cleaners)
        - points where operations/budget allocation are overwhelmed with handling methods
        - points of information bubbling (false boundary around information, preventing it from being communicated)

      - symmetries:

        - gathering points/spaces/rules/shapes for transformations
          - limits (potential for change determining which changes can occur, dimensions)
          - platforms for change (central point around which change can occurs, foundation)
          - set of operations that doesnt change object metadata (retains original information, transforms are reversible)

        - example:
          - once you have resources (equipment to last x time period) or a filter applied to resources (resources at a certain hospital), that can be a symmetry if it satisfies the other requirements, and while the original dimensions are intact (equipment is functional, location is intact)

          - hospital symmetries:
            - protocols (treatments, allocation, testing, feedback integration, reporting)
            - filters (floor filter provides a platform for equipment position to change)

    - identify problems:

      - identify priorities

        - budget optimization
          - equipment cost minimization
        - patient mortality minimization
        - infection from equipment minimization

      - identify rules

        - identify incentives
          - keep purchasing x amount of supplies from this supplier to get a discount
          - stay under budget
          - spend less on equipment to spend more on insurance/doctors/legal teams

        - inflexible rules
          - replace/clean/test/maintain equipment every x time period

        - output rules
          - cleaning/testing/maintenance methods have x impact on equipment value, functionality & other metadata

      - identify problem types

        - insufficient resources

        - insufficient resource distribution

          - information distribution (management layers, patient/employee feedback, reporting flaws)
          - equipment distribution
          - incentive distribution (no reward/punishment for following/ignoring procedure)
          - time distribution (inadequate planning/research/budgeting/optimization)
          - education distribution (no cross-training, no backup training (education on how to do research vs using existing knowledge))

        - insufficient variance handlers
          - no way for doctors to communicate with website devs
          - no way for patients to communicate with research teams
          - no way for doctors to communicate with report builders/budget decision makers
          - no way for doctors to communicate with other hospitals at various stages of diagnosis/treatment (using another hospital's research/reporting team tools or insights)
          - lack of data updating tools/processes (referring to outdated doctor office number/treatment method)
          - lack of process updating tools/processes

        - insufficient outlets for variance without handlers
          - delegating excess liability/risk is not supported by existing methods (insurance, consultants, legal contracts, regulations)

        - inefficiencies

          - processes
            
            - scaling
              - identifying phase shifts
              - bottlenecks
                - a process can only handle x amount of inputs before scale makes a phase shift happen, triggering different rules

            - delegation
              - alternatives
              - sorting
              - threshold selection
                - false boundaries/limits
                - limit manipulation (staying just under reporting level of expenditure)

        - variance gaps: gaps that allow variance emergence/injection

          - enforcement

            - delegation of enforcement:

              - staff are allowed to choose whether to implement optimal processes bc enforcement cost is high or not automated yet

            - example: an open system (like a door without a filter in the form of a guard) can let variance into the system (hospital) that may introduce more variance than can be handled

          - communication

            - info asymmetries/miscommunications

            - monitoring

            - lack of communication of reasons to align incentives/motivations with optimal rules:
              - patient doesnt know reasons why a test is being chosen
              - nurse doesnt know reason for process/limitation or data insight
              - doctor doesnt know reason why they have to fill out a new report

          - learning/optimization
            - no handler to self-optimize or adapt to new systems/problems

        - conflicts:

          - mismatch between stressor & handler 
            - gathering customer feedback doesnt handle customer feedback, but it may handle customer emotions

          - conflicting incentives
            - local incentives for doctor, insurer, or consultant contradict global incentives for hospital, industry, government


    - identify solutions:

      - identify rule optimizations:

        - if you find cheaper equipment without sacrificing attributes needed, you can replace equipment more often & reduce cleaning cost

        - if you invest more in predicting patient problems (infections, misdiagnosis) & optimizing their experience, you can spend less on gathering/incorporating feedback (web site cost, meetings)

        - if you invest in automating (robot vacuum, uv light) or optimizing a problem (filters to remove pathogens from places so those places dont have to be cleaned), you can spend less on maintenance costs (having a team come in and clean)

        - if you present patients with risk/cost data, they can have options, which delegates liability 
          - patients can view results of different equipment & pay different rates
            - if infection rate with existing equipment is 0.01%, give them option to buy new equipment from vending machine (like they can buy new scrubs) to reduce infection probability
            - if misdiagnosis rate is lower with live-streaming/recording of consultation, give them option to stream/record the discussion
            - if crowd-sourced doctor forums respond quicker than their doctors, give them option to crowd-source diagnosis & treatment plan
            - if theres an existing model to predict diagnosis for second opinion, give them option to buy a prediction from that model or contribute to training a new one

        - identify which processes are cheapest to automate without cascading errors
          - high-priority problems that follow clear rules but are likely to be ignored/subject to human error bc they are common & tedious
          - cleaning
          - testing needles & other key points of infection
          - blood drawing

        - identify which research in which tools would reduce costs overall
          - develop tool to sanitize any equipment known to be a point of infection (needles, paper towels, sheets, shoes)
          - develop cheaper & more accurate tests to check which pathogens are present on a surface
          - develop prediction models to identify which cleaners will work better on which pathogens, which surfaces are likely to be contaminated given direction of cough, etc
          - develop cheaper infection-prevention equipment (suits for patient that allow iv & tests, quarantine tools)

          - if you devote more time to research, youll have more budget to work with, you may be able to resell the solution, and your staff will have more time for more research

        - identify which processes would benefit from prediction function

          - which conditions would benefit from a quick research review (for new alternative treatments if one treatment is causing problems for the patient)
          - estimating which tests are accurate & which need to be optimized
          - insurance purchase (which problems are most difficult to predict/prepare for/handle)
          - risk allocation
            - which patients have risks of causing what problems (high risk of not being believed, mental illness, suing, reporting, ability to automate doctors)
            - where would extra funds have the most impact in preventing these patient problems

        - you can spend less on monitoring/data science/optimization if you remove interim or repeated processes

          - rather than 2 layers of management above an employee, build tool to identify link between first round of reporting vs second round of reporting
            - which info is left out when communicated to higher manager from middle manager
            - if middle manager is a problem resolver, identify which problems can be automated and which problems should be communicated to higher manager that are being left out

          - rather than 3 identifiers or 3 forms:
            - standardize
            - reduce similarities
            - identify which info is relevant to which agents
            - merge where possible

        - identify implementation cost of solutions

          - cost of teaching/incentivizing employees to follow new procedures
          - cost of enforcement/monitoring
          - cost of organizing & executing solution deployment


## Work distribution & incentivization

  - system users should always be system builders, so their incentives don't crystallize into an irreversibly static state
  - users should be builders by the end of each game
  - the questions of each problem space can be mapped to user tasks within a game, defined by a set of rules creating similar questions answerable in the game
  - when builders have taught enough users, builders should move on to being users of another game, in an alternating cycle
  https://twitter.com/remixerator/status/1217718371816329217


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
      
  - quantum => info => energy dissipation:
    - when quantum superposition resolves into information, which resolves into efficiency & energy, how does it cycle back into enabling additional variance (more quantum uncertainties)
    - theres an element of dimensional collapse/compression/removal involved in these processes, releasing the variance from the structures that store it
    - the dimensions of potential in a superposition collapse into information about particle attributes
    - the dimensions of information collapse into energy, which can collapse into efficiency (path of least resistance that achieves an intent) if combined with enough other efficiency pathways
    - examine the pattern of high dimensional objects appearing to have lower dimensions at various points of measurement
      - this is similar to alternate paths producing the same output from the same input
      - as variance flows into various dimension sets, the overlap of output with other dimension sets is less likely but not impossible & may occur at predictable intervals,
        like how integers have more limiting attributes than numbers in between, so boundary physics applies to integers & they can act as a filter
    - examine when emerging attributes cant be contained within a space & leak into others

## Communication

  - tokenizing common content/content-generation functions on clients & in communications
  - calculating computable sub-components & delegating computation to nodes on network trajectory
    - this means if executing a process on content isnt efficient on the source system, calculate network trajectory to route communication toward servers that are better for that computation & start sending content unprocessed and process it on those servers
    - if you had a communication protocol that supported common content tokens, sending content to servers that are better at converting content to tokenized form would be better than a random or non-optimized server
    - sending converted tokenized content & the id of the tokenization map on different routes adds some interim security
  - using neutrinos as a way to speed up communication using them as jumping-off/charging points


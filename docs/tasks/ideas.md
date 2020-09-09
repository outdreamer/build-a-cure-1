to do: organize into docs

  - pre-approved transactions on a schedule that give id service provider permission to update id
    - businesses contact id provider to check that id hasnt changed or get new id if its changed
    - then makes call to bank associated with id or updated id, which is expecting the transaction at that schedule & has already allocated/locked funds for that transaction
    - this means customers dont need to update card numbers or bank account numbers if prior numbers are compromised, but the id provider does need to track the original number & changes, and new numbers need to be unique across customers
    - transactions that are already configured/scheduled and havent been canceled are automatically approved
    - transactions that are implied/predicted (purchasing jacket if the weather is colder or moving to a colder location) have conditional pre-approval
    - customers can register their original id number with a particular business & optionally approve a budget with ratios of intents for transactions at that business/business type/product/product type, or range of transaction amounts, intents, types & other variables for their id number (by importing prior purchase histories or filling out new configurations or making new purchases) so transactions outside of that range arent allowed or have extra security intent layers applied
    - intents can be used to add validation to purchases (what are you buying this for? for event x coming up, which the calendar app api can provide validation of)
    - they can dis/associate other info with their id as needed (voting, address, purchase/subscription/transaction/configuration history)
    - using contribution to economy/markets/financial instruments/purchases/legal frameworks (like whether they can influence/create purchases or markets or product regulations) as an input to credit (indicating their value-creation potential)

  - identify mechanisms to identify proxy variables of a missing variable

    - includes inference of alternate variables that could generate the same information
    
    - also includes inference of side effects of the missing variable
    
    - example: if you dont have a variable like 'level of education' or 'level of intelligence' which is a predictor of income, how could you derive it from other variables, as an interim dependent variable to predict, before other dependent variables like income can be predicted?
      
      - apply a variable type pattern: 
        - 'variables with metadata similar to income have a predictive variable with metadata similar to education (which could point to intelligence, info access, tech access, group membership, and other variables with similar functionality to education)'
      
      - identify functionality produced by other variables you do have in the data set
        - 'what functionality does a system with these types of variation in genes, experiences, medicine, & information access produce?' 
          - output: the concept of 'agency' (and its related functions), which is a causal input/output of intelligence

      - identify insights in interactions of other variables explaining the missing variable
        - "these data points are distributed in physical position (data comes from several countries), which implies difference in 'information access', which is correlated with target dependent variable 'income', if you add a related interim variable (given insights like 'accessible information is not always used') like 'information usage' (a proxy for intelligence variable) that varies by cross-indexing with pollution-location data (creating mutations), indicating the 'information usage' is impacted by gene mutations (a gene determining information usage, such as intelligence genes) or other side effects of pollution (impacting 'information usage' functionality)"

        - bc we had:
          - location data in the original data set
          - another data set relating location & pollution
          - an insight data set about information usage not being equivalent to information access (indicating a need for different terms)

          we could:
            - identify the concept of 'gene' from any genetic attributes like gender/race in the data set 
              - the definition of the concept can be as simple as 'a set of constants for a record' or 'a set of constant inputs for a record' or 'a set of constant inputs of original position for a record', depending on necessity of specification
              - later we alter the gene concept to generate the 'genetic mutation' concept by applying the core function 'change' to the 'gene' concept, so we probably dont need 'constant' in the gene definition
              - we also infer a core component like 'functionality' being determined by the 'gene' concept, which can be added to the definition in this initial step rather than inferred later from other components
              - we also infer that the 'pollution' concept can be an input to the 'gene mutation' concept, which may be included in the original definition as a variable rather than inferring 'pollution' from other components like 'location'
            - identify a relationship between the 'location' variable correlating with the 'information access' variable
            - identify location-specific variables, like the 'pollution' concept
            - pull 'pollution-location' data
            - generate a possible interim 'information usage' variable by altering the 'info access' variable or pulling an 'info access' insight about the difference between those two terms
            - identify a relationship between 'info usage' and 'pollution-location' data
            - infer concept of 'gene' from original data set if it had any genetic attribute data
            - infer concept of 'gene mutation' from pollution definition
            - generate the concept of a possible function linking 'gene' concept and 'functionality', with 'gene' as an input
            - identify 'info usage' as an example of 'functionality'
            - infer that 'gene mutations' are also possible inputs to 'functionality', in addition to 'genes'
            - infer that 'gene mutations' are a possible input to functionality example 'info usage'
            - infer that inputs to gene mutations ('pollution') is a possible input to functionality example 'info usage'
            - infer that related variables to pollution ('location') is a possible input to functionality example 'info usage'
            - infer that 'info usage' variation generated by 'gene' concept or 'pollution' concept is a possible input to 'income'

        - you could infer the link from functionality (such as info usage) to 'intelligence' by further inferring that functionality varies in effectiveness by usage ('info usage' usage, or learning), which implies the concept of 'agency' or 'intelligence' (defined in similar terms as 'having the option of using a resource')

        - you could also infer 'education' as 'info storage' (remembering it) or 'info exposure' (reading it rather than just having access to it) from the 'info access' variable in the original data set, where education is an alternative or proxy variable for intelligence in some cases

  - identify other things the data set might be able to predict other than y's

    - subsets or the data set might predict other dependent vars beyond or adjacent to y, like outputs of y that can serve as predicted dependent variables instead
    - example: the image of a dog/cat can predict species type, as well as locations of animals, objects found in domestic settings, species variation in similarly developed species, etc

  - identify extra variables having patterns that if included in independent vars, can explain y's or other dependent vars
    
    - example: if you add a random sequence or a sequence with some similarity to another column (indicating an independent but coincidentally similar value), and it increases variation explained in the data set, you might have a more simple, homogeneous system that has similar core functions used across positions/layers/other subsets (square container producing triangular shapes of components inside corners), or you might have a very complex system that generates a variety of objects within a certain range (cell surface structures having similar shapes across very different cell types)

  - document what concepts look like in data sets:
    - first identify sets of core bases/functions/assumptions/values that can generate variation seen in data set
    - then systematize sets
    - then identify trajectories in those set systems that can be identified as a unique concept according to your definition

  - example of other derivable content metadata (giving context to an isolated descriptive variable analysis):
    - the insight path an author took to generate their work, given their input info (what trajectory did they take from A 'reading the bible' to B 'writing this poem)
    - other effective/creative/robust insight paths (how to get from A to B in a more creative way)
    - the structures like core functions/bases/layers/objects to generate the content (take a plot from an old bible story, add drama, add local/contemporary plot lines, mix characters, apply a structural pattern like syllables to refine it)
    - generative variables of the content, rather than just the descriptive variables (find objects that generate attention (drama), find new combinations of character attributes, find a structural pattern & apply it)

  - example of UI for implementing intent-matching for code generation

    - form accepting intent queries like 'build streaming platform optimizing for metric c with these data sources'
    - upload a diagram positioning data sources, formatting/aggregation/analysis processes, metrics, query types, permissions, visuals, & target output, which produces various implementation diagrams the program derives, which the user selects between
      - including attributes/functions like:
        - which data should be streamed where
        - which data should be encrypted in what way
        - which actions should follow which actions
        - which data should be accessible by api, to which apps
        - which queries are expected, from which users/apps

    - identify uncertainties like config relevant to their intent and ask questions to confirm to reduce produced set of implementation diagrams

  - social manners perspective/intent translations with structure mapping in specific systems (like govt system using the satire perspective)
    
    - diplomatic perspective:
      - from 'flaw/mistake' to 'optimization metrics' or 'variance source'
      - from 'get/make/trick them into' to 'inspire'
      - from 'please dont do that' to 'thank you for being self-aware enough to not do that' or 'i hate when this other person does that, im glad you dont do that'
      - from 'youre annoying' to 'i need to recalculate my trajectory/i need time to process that'

    - neutral perspective:
      - from 'flaw/mistake' to 'unknown optimization metrics'
      - from 'get/make/trick them into' to 'convince'
      - from 'please dont do that' to 'track every occurrence in a database'
      - from 'youre annoying' to 'i need you to share that with the team' (delegating negative feedback)

    - govt satire perspective:
      - from 'flaw/mistake' to 'tactic'
      - from 'get/make/trick them into' to 'win them over'
      - from 'please dont do that' to 'taxing that'
      - from 'youre annoying' to 'redrawing district borders so their vote doesnt count'

    - work productivity perspective:
      - from 'flaw/mistake' to 'would you like to work on our mistake-fixing algorithm'
      - from 'get/make/trick them into' to 'incentive alignment algorithm'
      - from 'please dont do that' to 'cost-allocation learning optimization algorithm'
      - from 'youre annoying' to 'busy work algorithm'
    
  - query for specific info object structures in a language map:

    - ambiguously controversial paths (cant pin down anything you said as wrong but it sounds controversial)
      - from standard path 'fill out the self-reporting census form' to ambiguously controversial path 'exploitation of the race/gender/disability option'

    - things that sound controversial but are just accurate:
      - having one set of optimal attributes creates a system with more ways to be wrong than ways to be right, so the minority at the top will be oppressed until a new optimal is chosen, which is a slower evolution process than having more than one optimal set 
        (uses controversial word 'minority' and controversial depiction of 'minority at the top' being 'oppressed' in some way, which is true bc of the ratios and power dynamics resulting from them, but is controversial-sounding bc of the different positions of those objects compared to their standard positions in how theyre usually used)

  - document nn-intent matching
    
    - in an algorithm, functions emerge like minimize, aggregate, differentiate, compete/win, choose
    
    - these functions between data objects (like variables, types, etc) are suitable in a particular structure (like a sequence) for different problem types, which are appropriate/optimal for different data variance, variable type sets, category difference complexity, causal structures, different bases & ranges of difference, modeling sub-systems & alternate routes, etc)

      - when detecting the difference between cat & dog:
        - were a hundred different variables combined, weighted & changed, with interim variables at various points, then selected after having to compete? then an algorithm/network with a similar function structure might be able to capture that difference
      - does a particular variable in the data set (output dog feature) indicate a path between other variables not in the data set (causal path between DNA & output features), which could be captured with a particular structure of nodes/layers or level of variation between weight paths?
    
    - how do core network algorithm structural operations (power, scale, add, average, differentiate) map to functions & structure of a problem type (categorize, predict) or function assembly/filter (average)
      - 'type patterns' and 'weight path patterns'
      - 'averages of adjacent points' mimicking 'features with similar positions' and 'change about a base'
      - 'a sequence of repeated options determining possible combinations' (like DNA) and 'initial starting nodes & node sequences across layers' and 'weight path patterns, starting at a base like average'
      - 'unit vectors with different direction get a vote in determining function curvature' and 'different weight vectors get a vote in determining variable importance'
      
    - how does the problem type map to the function & function assembly?
      - if problem type is 'identification' and function assembly has a gap indicating an ambiguity, the identification cant occur in that gap, so functions with ambiguities arent good for the identification problem type, unless the ambiguity captures alternate structures (like variable values, causal paths, or variable sets)

    - treat other objects than params (assumptions, processing steps) as prediction inputs

  - whats the reason for number relationships (numbers being a definition of value, math having a set of relationships between values)
    - can one number have a limited number of properties before its overloaded - whats the reason properties are distributed across intervals & sequences of numbers
    - is it so awareness of a particular number gives you adjacent numbers near it that together cover a wide range of number properties, so the rest can be derived?
    - are there intervals of numbers that are property dense or sparse?
    - are properties denser in numbers that are more measurable or calculatable?
    - do properties have similarities (type), symmetries (function & series), coordinations (orthogonality & area measure), & efficiencies (translating to a space with computations reduced or embedded) that mean they'll accrue into particular property sets more than other property sets?
    - which properties are never observed together (which numbers cant be combined in any space)?
    - which properties could be changed without changing the net or general behavior of the system?
    - what is the full set of possible difference or change types (generated with components of difference & change), and is there a gap in descriptions for them? (usable as a filter)
    - what type of information is not structurable?

    - what happens when you stress information (injecting change/difference variables, adding assumptions, using it as a dependency)?
      - it vibrates under stress, and breaks into objects of potential (like a superposition), objects of change (adds a variance/expands in dimension, crosses a phase shift threshold)
        https://en.wikipedia.org/wiki/Hilbert_space#/media/File:Standing_waves_on_a_string.gif
      - what makes it stabilize into measurable values?
        - common assumptions, intents, efficiencies, matching structures (coordinations)

  - function metadata

    - add 'because' operator to link each decision to an intent, implication, interpretation, or assumption
    - add 'meaning' operator to index functions by meaning in addition to intent/cause/assumption/implication/context
      - "object.attribute1 = 'value' means "users can configure a variable that they will probably have different preferences on that will not add excess complexity or vulnerability to the system"
      - 'what does it mean' translates to 'what structure does it have in a relevant system' (such as relevance to users' system of use cases & preferences), or 'how does it fit within this system'
      - functions/libraries/applications should be indexed by meaning so they can be fit into a global function system across applications ("we're building this app because there's a need for this degree of difference given user intents, which means there is a mismatch in supply & demand for that market")

  - organize security methods

    - vms, servers, networks, encryption algorithms with intent & approved actions (browse web, email, edit doc, test software)
    - approved workflows: use components like approved action sequences of previous sessions as the site matches requested actions
    - centralized data store: if you go to a site for 'change your address intent', it retrieves or infers & confirms your updated address with an address storing server/network that picked it up from an original update you submitted with authorization procedures, rather than you having to update it everywhere
    - code changing per request: once code-generation is automated, generate slightly different site code for each request (swap out dependencies, use alternative functions or workflows that have ambiguous/neutral impact on intent & execution)
    - request demand-supply matching: 
      - assign cause (demand/need/requirement or reason for intent) to each intent (I have to go to the car insurance site bc the insurance provider submitted a request to pay a bill to a third party request tracker that approves site access requests)
        - example: does a site dev want the site to be tested? then it can accept 'test' intent workflows, otherwise request patterns similar to test request patterns & no other request patterns will be assumed to be illegitimate
    - intent-based navigation & configuration (generate config for a particular priority set like 'safety first, then functionality, then performance' or intent like 'protect my system from all third parties' or 'ask me for permission to train a model to filter external requests')
    - changing encyption algorithms on server & client according to a function with ambiguities built in (following a particular algorithm with different algorithms for example)
    - context-fitting & request metadata matching: 
      - one person couldnt execute two simultaneous processes, so check for computations done on computer that would preclude a particular process
      - one person couldnt execute two simultaneous requests without software (verifying requests across sites with anonymizing functions), so check for approved 'bot developer' intents
      - people dont usually just infer that they should change a configuration on a site, it usually happens after they receive information about that configuration (verify information across requests at different sites to establish request legitimacy)
      - apply request/communication patterns, like that info objects such as conclusions usually follow other info objects like news articles, and actions follow conclusions
      - predictability of requests is an identifying feature and a way to generate probable data (like a probable conversation or headline, given new information queried) but also a security flaw, as it can be mimicked easier when its more predictable
      - explanation of their cause/intent for a request wont usually differ drastically from previous explanations/intents/causes without exposure to information (request change rate metadata)
      - match intents across processes/context: if a user is checking their email, its highly unlikely they also suddenly simultaneously want to encrypt all their files and show a popup with a skull on it asking for credit card information
        - similarly with info security: a person who typically uses an app to exchange updates with family or do science research (fact-based usage) is unlikely to suddenly be interested in fake news, logical  fallacies, emotional language, or want to find out about antivax cults they can join (conspiracy-based usage)
        - deriving intent from context: if they use dark web tools, like degrading content, or are poor in some way, they are likelier to be interested in using email spam automation software, intents which can be tested with fake site generation to test if they would download it
        - if a set of funds have been requested, are those funds verified, and can the payment be allocated after verifying network path & in pieces according to path traversed so far (adding trustless design) - with an associated purchase, allocating the payment across product shipment trajectory & damage checks or other quality tests
    - reducing requests needed by deriving code on-demand rather than pulling it, and aligning intents across code bases to identify code that can be shared/reduced
      - example: running bug-spotting/fixing programs locally & testing in a local vm rather than installing updates, running installed updates in a local vm with extra security until typical period of attacks has passed
    - computation network: calculating whether a request like 'have you calculated this & cached result' or 'calculate this' is the more efficient operation with calculation server networks

  - example of choosing priorities/metrics to value:
    - something that not everyone has the potential to be (non-structural) is more valuable if it optimizes some metric
    - reductiveness: the lowest/simplest structure that complies with a metric (reductive choice like a parasite) also reduces potential, whereas the highest structure that complies with a metric (empowering choice like a mammal) increases potential
    - evaluating the potential of lower life forms is less optimal than fixing them, so the metric becomes whether you fixed/empowered them or reduced them, bc they cant fix themselves
    - the metric is whether you got the point (empowering, fixing, making other life forms complex), not whether a lower life form can become complex
    - potential is an important metric bc more complex life forms are supposed to have the potential to be complex, so its more wrong for them (like a puppy or human) to not optimize a complexity metric than it is for a simpler life form with less potential (parasite)
    - some metrics will be alignment with priorities rather than reaching a threshold value

  - example of how the physics system has structures preventing certain cascading change types (local scope bubbling) & allowing others (nuclear chain reactions), partially through forces like gravity keeping objects at a distance: https://www.sciencealert.com/time-travel-through-a-quantum-world-has-nothing-to-fear-from-the-butterfly-effect
  - physics vertexes
    - potential energy collapses, cascades, & aggregates into structural information (like numbers) on efficiencies, in a way that maximizes difference
      - an example of a cross-interface insight
      - symmetries are an input of interchangeability, such as two functions that can be transformed into the other that perform a similar computation, creating an efficiency (if you have one function in the symmetry, you can generate another, in case the first function doesnt compute what or how you need it to)
    - black hole unpacking function (allows information to develop)
    - universe overlap/collision/combination
    - lack of universe-preventing conditions (like how information can develop if black holes are far enough away) or potential to avoid destruction mechanisms
    - variance injections & interaction rules allowing variance cascades to prop up a universe structure, allowing time to develop
    - upward arc on a wave or parabola (development of time marks the upward arc), where the downward arc is the unraveling of time back to the origin big bang (collapse into a black hole, eject variance, rebound universe), as material or structure allowing material of the universe is stretched temporarily to hold the variance injected via the entry point (whether black hole, universe collision, or something else)
      - what other types of universe are there, other than a universe allowing sequence between states (conditional/temporary truth) achieving/executing absolute truths?
        - other structures include:
          - similar rules but different origin position, different rules (including most extremely different rule set) but similar origin position, & other permutations of universe constants/rules & generative structures like filters/containing sets
            - universe defined as a set of possible trajectories from the various different generative structures, or a space between the various different limiting structures
          - state circuits/networks (illusion of time, but still on the same circuit/network, meaning the states are pre-determined in that theyre guaranteed to be on the circuit/network)
          - a universe of vertexes (generators/determinators/descriptors of other variables, like a set of constants such as identities of nodes on the abstract network), where the primary function is preventing change or routing changes to universes with the potential handlers to contain it in a stable way
            - a universe with a 'regulation' intent that prevents excess change from other universes
          - a universe with different fundamental definitions/dimensions of change/core components/interfaces
            - a universe that builds its foundation off of a different interface than the structural interface
            - a universe with a different definition of information/randomness/position/change
            - a universe with different dimensions of change than position/time/structure
          - universe with potential to switch off time with sub-interface alignment (coordinating changes on quantum interface like with a quantum chain reaction to prevent or reset variance)
          - universe with potential for extreme information states
            - at one extreme, truth can crystallize into a universe-determining input rule if not prevented from doing so, and at the other extreme, structures allowing guaranteed variance to develop first can prevent truth from developing at all
            - universe where information (stable states) is not allowed to develop (a universe requiring distributed randomness, or lack of information), and measurable information is an abstract concept that the universe structure can never create a sub-structure to contain
              - where every possibility is equally likely, invalidating the concept of probability
            - universe where noise/randomness is an intent rather than a side effect of intent alignment & development, so reversing the intent development process to be an input rather than the output of interaction rules allows certain types of information & randomness to develop
            - universe where the ratio & types of information/time allowed to develop allows/prevents certain types of information derivation about universe manipulation/traversal, which if combined with other types from adjacent universes on a certain definition of distance, would invalidate origin or other types of universes
          - universe where potential (in the form of variance injection points) is evenly distributed as a constant condition, so certainty cant develop (in any form, including time/structure/priority)
          - universe where some calculation types are conditionally/contextually possible, like at regular intervals where variance drops below a certain level because of passing adjacent universes
          - universe where information derivation-loss ratio makes calculations irrelevant because of the symmetry types present, which make info loss from info asymmetries trivial (where symmetries can be combined to offset every asymmetry)
          - universe where efficiencies develop in a way that certain priorities are incentivized despite universal constants exerting limits on direction change
            - prioritizing similarity or optimization contradicting a universe constant ratio of variance
            - prioritizing calculation types that prevent measuring information of a particular type
          - universe that involves trajectories between bases as a way to measure change (a changing interface network vs. change on an interface network)
          - universe where external universes are determining, rather than internal states or generative rules
            - coordinating rules in universe development have compounding effects on potential of universe interactions
            - universes where the generative rules, other constants/metrics, and position with respect to other universes are changeable from inside/outside (input/output sides, reversing causation)
          - the influence of one universe on another implies a notion of universe-external time (if a state change occurs, time has passed, even if the state is a change to the set of generative rules), where in reality, the universe relationships might not change (a static game), unless it's possible to coordinate/hook up their dimensions to influence each other
            - but this type of time may not exist, or may only exist conditionally when two universes interact, which doesnt change the absolute rules governing their interactions because the change stabilizes reliably enough to invalidate the idea of change of that type, so universe-external time can only exist in universe-to-universe interactions, but not in universe-to-universe relationship interactions
          - universe where time (in the form of potential or energy) is possible while the universe is being used for calculations, but decays & disperses when not being used, potentially being stored as variance in adjacent universes while not being used
          - universe where time is determined by calculation potential 
            - if something can be calculated from something else & vice versa (independent variables generating a dependent variable), time has not passed while that relationship is true
            - if something cannot be calculated from something else (asymmetry or information loss), time has passed
            - the set of time-independent calculation relationships may determine the amount of time a universe has until it either decays, compresses, changes its determining factors, or finishes its original intended calculation
          - time defined as the potential to calculate trajectories around a universe's singularities, or the ability to arrange calculations in a way that doesnt make all information calculatable
    - calculation trajectory (calculations possible in this universe or space-time used to calculate position in regard to the others, given intents possible with those calculations
      - calculating position (knowing if your space-time is a pawn/knight & the pawn/knight functions, and deriving the existence of other positions) & possible intents of that position (& the ensuing functionality) enables determining the set of possible moves on the board, the limits of the board, the point of the game, and the optimal positions/moves/states in the game, giving you a direction to move in if you can coordinate with other players
        - derive information with rules like:
          - if there is a universe that can destroy yours when adjacent, you know that its not adjacent to you
            - similarly, if there is another pair/set of destroying universes when in certain positions that are related to your universe (inputs/outputs/alternatives of yours, or cooperating with yours), you know theyre not in those positions
          - if there are rules that are invalidating to particular types of potential/information/randomness/change that have been measured or determined to be valid in some measured or possible context, you know those rules are not absolute

    - structure-information interface:
      entanglement, as the accretion of possible information into a core function (information generator, like the physical component of an assumption - a defined relationship, with its own definition of difference (reducing distance type of difference between entangled particle positions)
      polarity, as the accretion of information into a core function
      wave-function collapse, as the angle at which information appears to have one dimension of change

  - ways to navigate space-time
    - alternate routes to arrange spacetimes in a way that makes origin & target space-times adjacent or traversible
    - navigating by symmetries as a guide to reversible routes through space-times; where theres a window of opportunity to reverse trajectory (on a space-time tree branch ending with a dead-end leaf) if a structure of symmetries like a foundation or net or symmetry-generating structure is within reach

  - browser optimizing web sites based on clear feature-execution mismatch created by malware or outdated code given origin code intent, a ratio of version/other change allowed, intent of site actions (not making changes that would break other functionality calculatable on the page)
    - browser configurations like versions/modes/settings applied for tabs

  - add structures to diagram: interface overflow (to sub-interfaces), interface foundation

  - program should be able to identify, predict, & finally calculate structures that will be useful for an intent, to avoid reducing/searching a solution set

    - identify with structure-matching (which of these structures can fulfill this goal)
      - example: finding a 'progression' structure for a function

    - predict with intent-matching (find structures matching these intents)
      - example: for calculating area, which structures fulfill that intent

    - calculate with intent structures (derive intent-structure relationships and find operation sequence that will produce target intents)

      - example: 

        - which structures simplify difference calculations (like area) extending the addition/core/unit operation (like how multiply is an extension of add) when increasing a parameter like number of dimensions, given that 
          - the add operation has a 'combine value' intent
          - multiply has a 'combine value with different direction' or 'describe interaction space' or 'find intersection area of limits' intent
          - length has a 'describe difference' intent for a dimension count of 1
          - and so on for other operations

        - the addition operation has an associated structure 'align with overflow in left direction' because inherent to the definition of values in their standard western depiction, higher digits are on the left, and the extra value from an operation like 8 + 3 (10) would overflow into the next digit because thats a unit of change that can be registered in the next digit's column, with no more than one digit to the left being able to register the excess change from addition two digits in a particular column (greatest value being 10, by adding 9 + 9)
          
        - tests:

          - this is a good unit test for whether your program can generate math methods by applying structure:
            - if the program can identify:
              - 'column as a digit store' (given that existing numbers use columns as a digit store, which could also be done with rows after converting numbers to row format)
              - 'alignment of digits'
              - 'adding digits in the same aligned column'
              - 'overflow extra value to the left'
              as concepts & operations that would respect inherent digit definitions/rules while executing the addition operation, and design the addition operation itself, that would be a successful basic test

            - an example trajectory using the interim objects:
              - insight paths:
                - 'compare relevant objects'
                - 'compare standardized objects'
                  - identifying the 'position' attribute as an input to the 'compare standardized objects' insight path (or identifying the 'comparison standard' object or 'standard as a required input for comparison' in the 'compare' definition route) which produces an input to the alignment process, as alignment is a process that should happen between similar objects (such as objects that have been standardized for comparison)
                - 'apply sequence to operations based on which operations enable other operations'
                - 'handle extreme cases'

              to generate the addition method would be:

              - 'compare relevant objects'
                - 'relevance = similarity on an interaction layer'
                  - 'compare objects that interact'
                    - 'digits in the same position (distance from right) interact'
                      - 'apply a standard that aligns objects that interact (digits), to compare digit object values'
              - 'execute the add operation after digits are aligned, for relevant comparisons' (this operation is enabled by the previous operations, which is why it comes after them)
              - 'handle extreme cases, where value cannot be described by the digit value range'
                - 'extra values of addition operation need to be routed to other digits'
                  - 'adjacent digits interact'
                    - 'extra values need to be routed to adjacent digits'
                      - 'adjacent left digits can hold extra values' (increasing from 9 to 10 moves value left)
                        - 'extra values need to be routed to adjacent left digit'
                          - 'add from right to left'
              - 'apply a default operation mode, limit to unit operation, or fulfill "isolatable operation" requirement':
                - 'add one pair of aligned digits at a time' so impact of each operation can be assessed & routed

          - other default operations, like multiplication (2 x 25) identifying 'multiply digits in one number (20, 5) by each digits in the other number (2) and add the output of each multiplication (40 + 10)' as a standard rule to execute multiplication operation, with a multiplication definition that doesnt include those rules, such as:
            - 'find the area of the space bordered by the limits generated by lower x bound = 0, upper x bound = x value, lower y bound = 0, upper y bound = y value'
            - 'add the x-value y times'
            - 'find an adjacent more calculatable or pre-computed value & subtract the difference'
            - lattice multiplication
            multiplication operation definitions which are also alternate outputs of the 'generate a multiplication method' query

          - 'find a structure where calculating the output of numbers multiplied by themselves (exponents) is a set of addition operations' (log function)

          - 'find the unit object of nonlinearity' which should have:
            - info output: x ^ 2
            - structural output: variable ^ (next value other than 1)
            - conceptual output: 'compounding change', 'multi-dimensional (multiplicative) change' (change of variable, and change of a dimension)

          - the program would integrate intent relationships like:
            - 'a unit change in this direction has x impact on change in other directions, and a change of degree n toward other change types & states'
              - which would help predict what impact a change would have on change metrics, which are also calculatable from other change types/states, such as estimating the impact on area from a unit change in one direction (of various change types, including a unit addition/multiplication/parameter change, etc), and include the impact on difference from related change types (impact on tangents, inflection points, subsets, and related objects), and related change states (difference from adjacent functions like with one-off parameters (constants/exponents one degree away)
              - where the intents are structural by default ('multiply by this constant' having intents like 'increase the scale of this function from the unit version, keeping this maximum as a center or this point as an origin')

  - joke insight path examples

    - expectations

      - inevitabilities/incentives/assumptions as a source of expectations

      - hypothetical questions & question chains ('what if x') to generate assumptions
        - what if function x normally associated with object 1 is instead in object 2, which shows no evidence of function x

      - assumptions & assumption chains
        - not just "that inanimate object x has feelings" but also "and has tried to manage them but fell for a sock anyway" to fulfill an 'explanatory alternate route' intent of "how it got stuck"

        - permuting the assumption that a gender will be classified as an object of the gender classification system rather than an object of a different classification system, like race or social status or species
          https://www.twitter.com/alienbot1/status/1053376572558852100

    - intent
      - missing the point
        - the point of preventing animal cruelty is not "so they dont have obvious evidence to point to when justifying organizing criminal enterprise against humans"
      - invalidating the point
        - protesting animal cruelty using signs & bumper stickers made with glue made out of dead animals
      - making a point in an unexpected route
        - preventing animal cruelty so they taste better

    - structures
      - switching positions/structures
      - relevance cycles
      - efficiencies
      - similarities
        - differences can be found in:
          - attribute value, attribute structure, attribute metadata
          - adding/removing variables, variable structures (sets, sequences, networks)
          - identifying variables likely to change
          - identifying variables & patterns likely in a system/context
          - interfaces (priorities, abstract attributes like relevance/meaning/sense, logic)
        - difference types:
          - absence of object
          - combined object in a set
          - distorted object
          - filtered/subset object
          - ambiguous/alternative/interchangeable object
          - new object type
          - developed object with new functionality/attributes
          - deconstructed object
          - formatted object
          - object generator/effect
          - illusory/implied difference
          - reference vs. structural vs. systemic difference
      - extremes
      - bases
        - maintaining a base of reality is useful for highlighting differences
          - "reverse-engineering how an idiot came to a conclusion without the assumption that a cult got to them"
      - paths
        - alternate routes are a place to inject assumptions

    - logic
      - validity
        - illogical connections are a plact to inject assumptions
        - system has to make sense (have some organization) to maximize impact

  - variance generators (of noise) including objects on same interaction level and components that can build changes on interaction level as well as containing object interaction outputs that can cascade to lower interaction level changes

  - how to erase causation contributed by a prior/root cause to subsequent variables if root cause & subsequent variables are both included in the data set

  - example of intent mapped to structure: the outlier or data point in the middle of two categories isnt supposed to be categorized, its supposed to be identified as belonging to a different group (a group in a state of change), which can be used to derive group boundaries, but shouldnt necessarily be integrated into a categorization function

  - example of alternate explanations: for a pattern like why people have different responses to a pathogen, is it bc of coincidences like that:
    - the pathogen fits into the bio system in a way that requires the same functions used to protect it from another second condition, taking protection against that condition away
    - the pathogen coincidentally applies mutations that the bio system hasnt yet evolved to handle
    - the pathogen applies mutations that coincidentally spiral out of control bc theyre mutations to important/core change/regulation rules, or that it causes another error that triggers the second condition
    - the pathogen evolved in an animal that didnt have those vulnerabilities so it was able to live in the host indefinitely rather than killing the host
    - the pathogen needs a function that requires evolving other functions that are coincidentally harmful to the bio system
    - the pathogen misidentifies the genes to target or cant identify the right genes in different systems
    - how to generate the set of possible alternate explanations:
      - apply structures (evolution process of change sequences), concepts (identification function error, coincidence), functions (functions producing changes, such as mutations), and position them using other structures (causal network)

  - with information representing the constant vertices of a system, by representing information a certain way, efficiencies are gained in other information, like related calculation outputs 

      - what does the efficiency provide to uncertain/uncalculatable objects external to information?
      - with certain concepts as priorities or embedded in the structure (like orthogonality generating intersection spaces for mapping interactions), certain efficiencies in calculations are created
      - what filter set or subset of possible concepts can explain the information description system?
        - what other objects are explanatory, in addition to concepts (a slice of a system with a similar object or pattern), filters, core/generative functions, limits?
      - what connects the constants in this system, representing information behavior descriptions - are there system objects like validation/formatting filters, efficiencies aligning between information & uncertainty objects, or other objects beyond the conceptual layer of discoverable information systems?
      - given that information attracts information differently in different structures, what intents can those structures & the information rules be used for?
      - if paradoxes are representable as holes in logical value connections (gaps or jumps in the information system, like asymptotes are for values), what type of information values can occupy those holes, or do they act like a symmetry to connect different spaces?

      - does information withdraw into a superposition (structure with multiple potential information states) or an abstract generalization (generative structure of information or concept network trajectory of the information) or a compression (retaining some attributes of the information), once you remove its structure or remove it from a space where it can stabilize enough to attain a structure?

    - intent implemented on the web could look like approved workflows for accessing a site or across sites, where actions, requests or workflows can be pre-purchased and approved algorithmically 
      ('how to build a bomb' search isnt purchaseable with a 'purchase chemical' request or across purchase bundles)

  - tool to make bacteria grow until detectable & then represent with AR

    - this closes the gap in information:
      - the information needed for the product (a testing & display tool) was insufficient
      - the mechanism to make the information sufficient is accessible (solutions to feed bacteria)
      - rather than make the measurement tool better, you can make the information more accessible (change the position of information rather than the position of the measurement tool)
      - the AR component would augment the size to make it displayable to users without using the measurement tool (microscope) or indicate size/type of pathogen with standard data visualization rules

      - applying the testing tool to hub nodes (then inputs/outputs of hub nodes, and adjacent objects to hub nodes) to check with increasing certainty whether surfaces were compromised
      - redistributing resources based on immunity/infection status to avoid cleaning, like distributing unchecked, unsanitized, or contaminated goods to consumers with immunity/infection 
      - keeping an animal likely to develop fast infections in buildings and then using air conditioner to distribute viral RNA when the building is unused and checking remotely if the animal shows symptoms to see if a building is safe is one way around the limitation to detect live copies of the virus, since the animal symptoms are easier to measure than a pathogen, so the problem becomes ensuring the animal will develop symptoms rather than immunity, and making sure the symptoms show up faster than a test done on hub nodes or quickened with enzymes/sugar/cells that help the pathogen replicate

  - analyzing just by change rate makes it less likely to spot other patterns like overlap/intersection of patterns

  - difference develops where there's potential for new interactions to develop (so a steady or increasing rate of change) & intent (like a possible gain from the difference)

  - the object model may not be the right default to start from in most situations - there arent many whole objects in existence if there are any
    - even particles have sub-particles, and the extent of that chain isnt known, and may have a causal relationship where the smallest particles act as inputs or injection points
    - should ratios/bases or sets be used instead ('a set of particles' rather than a 'plant' as a standard unit)
    - when selecting a default, you should be checking for attribute matches (does a whole object make sense to describe a set)
    - the idea of a whole number may describe something that doesnt exist in 3-d physical reality - does that mean its a concept that will never occupy a form, or is it a goal physics will move towards, or it causally independent from other systems or interfaces that are known, or it evolves as brains can measure information

  - mask design can be optimized as a cover with one output flap like an esophagus preventing input on one nostril so the other can be used exclusively as an input with a filter 
    (better to sanitize at point-of-usage in environments with many unpredictable interactions like wind direction and interpersonal contact, which can get around most masks)

  - types can be represented as directions (going farther from origin goes further up type stack, where similar types are adjacent)
  - change phases for causal analysis (interim, changing, diverging, standard, efficient state, constant, interacting, converging, on the verge of obsolescence, outlier, etc)
    - superficial cause, alternate cause in the case of a function, addressing input/output causes
  - framing on interfaces, decomposing causation, then identifying parameters of problem on layer & matching solution
  - independence (closed trade loops) as time storage
  - vertex as a pivot point for an interface

  - when physics rules stabilize, they attract & generate information, which gathers into measurable numbers
  - if the point of the universe is not to find the initial filters but to prevent that information from being discovered, that could keep open options for other change sources

  - an infinite series implies a stabilized symmetry (a platform for change that goes on forever) - clearly there are different degrees of stability - how do these different degrees of stability relate to different infinities like infinite sets given by number groups
    - the chain of events mentioned here implies a stability in the energy preservation with each successive event
      - https://www.quantamagazine.org/what-goes-on-in-a-proton-quark-math-still-conflicts-with-experiments-20200506/

  - organize db by intent & features for quicker access - like if types are a common filter, organize a graph into type clusters, and store node id's to limit size of various different graphs to depict the same database, a subset of indexes represented per graph

  - product platform:
    - filters: predicting filters that will be used the most (features that differentiate products and alternate purchases the most)
    - products: product query language ('product with feature x and without component y')
    - supplies:
      - adjacent supply cost estimation ('adjacent product built from these suppliers would cost x')
      - estimate future demand & estimate cost of production methods (how many times will you need it? if above x, then its more cost effective to build it yourself, buy from these suppliers with price-lowering trends, buy this robot to make it regularly, or build a robot to do it - plus the timed sequence of those purchases for most cost effectiveness)
    - code as solutions:
      - code search (code as product solutions, like code to print a product or code to predict a compound or adjust vitamin combination as needed)
      - feature-to-code translation ('need a product with existing feature x and add new feature y')

  - explore how to map position (a state structure) to variable structures like networks/loops/trees (like how rank assigns standardized relative position to values - how would you assign a position to nodes in a network in a similarly standardized way - an attribute like connection count or node type, or a trajectory position, or another method)

    - how do rankings map to ratios, and what errors would result from direct mappings of various initial data types?

    - is there a standard set of structures like networks that should be applied to a sequence to get its probable prediction function the fastest (framing numbers as 1, a map from number type to node types, 2, a node's connection count, & 3, distance between nodes, in order to map the sequence in the most robust way)

  - type of chart: a map of the trajectory between low-to-high dimensional representations of a function

  - what attributes determine symmetries so you could differentiate between symmetries (distortion functions, origin)

  - manual code should only be used when there's an unsolved problem in a domain that doesnt respond to algorithmically determined solutions (when optimization of implementation is uncertain), otherwise algorithms should be selecting code

  - vertices: variables where once theyre assigned a value, the rest of the uncertainties are resolved or resolvable

  - data structures:

    - what kind of data structure would look like the original sequence from one angle, but look like its metadata (like the ordered sequence, or average value statistics) from another angle?
      - is the extra storage of a tree, network, or other structure with more than one dimension worth the computation gains
    - is the best storage format of a list where position would be checked later in code a map retaining order, with keys as ordered values & values as positions in original sequence (in case original position is significant and youre not just trying to find if the value is in the sequence)

  - if something can generate a change predictably/consistently, it's a change supply - otherwise it's a change request, so output as well as causal position relative to the output is important when determining category
  
    - time may be a variance gap (a space where change is possible) to resolve a question/problem set - so not resolving it can preserve time, unless resolving it will allow for more potential or moving on to other variance gaps

  - vitamin 3-d printer to print vitamins so that you can design your own multivitamin that:
    - fits your bio conditions & requirements
    - is released in the right order & timing
    - excludes interactions that are contradictory (antimicrobials & probiotics)

  - multiple servers/processors in one computer with one-way data transfers, so one server can be for local communication, one can be for offline work, one can be for browsing internet, and local/offline can communicate to internet-browing processor but not the other way around

  - rules-to-code translation tool - translating domain-specific plain language rules to robot code can be short-term useful for automation of service industry tasks like:
    - converting recipes/flavor-mixing strategies to cooking robot code (chefs can use a tool like this to make money short-term or sell their rules, if they have unique strategies)
    - converting new plant designs to genome editing code
    - converting local social insights to global code (avoid personalities like this, use these tactics to persuade, make this argument to get them to an insight position, etc)
    - converting adaptation insights to change-attracting system adaptation code
    - converting routing mechanisms/optimizations to drone code (short-term human insights like 'avoiding a particular street bc of construction' that data isnt adequate for)
    - the general task of converting rule sets (systems) or human-made visuals (graphs, blueprints) to code

    - machine learning can be used for initial conversion, then tweaked with coded filters like priorities, logic, organization, output
    - system analysis can be used to optimize beyond those standard filters
    - this needs to identify existing rules (or specific versions of abstract rules, distorted versions of standard rules) & filter them out
    - this is an alternative & and an interim step to raw code-generation given a set of intents

  - data viz can be automated using:
    - lie core function layer graph or individual lie type graphs, with an output intent layer (hide information, layer information, minimize information, obfuscate information)
    - intent-structure maps (this graph structure serves this intent stack, just like a function serves an intent stack)

  - each superposition contains components representing different possible filters for the physical laws they create at scale
    - some superpositions collapse into a particular attribute set
    - superpositions with different configurations may represent other interface queries or structures
    - knowing the internal structure of a superposition would mean we get to choose which queries come to life & become real
    - the design implies we shouldnt get to choose - but external forces (or unmeasurable/uncomputable forces inside the universe) should get to determine which configurations collapse & which differences are allowed
    - information has a lifecycle - its likelier to become more true the more its observed, up to a maximum - then it's likelier to erode as its depended on
    - observing a state (to produce the information of the observation) may initialize the static nature of that information, so other observers see either static information or lack of it depending on their perspective, as information becomes truer the more its observed, and they may focus on the lack of information or a different perspective than the initial state of the information


## search ideas:

      - inferring useful search filters based on customer usage history & intent
        - linked searches/user data with type/intent identification - if they are in a location with a certain pathogen and they search for cleaners, theyre probably trying to clean that pathogen so cleaners should be specific or at least an optional search results set should be linked to
      - automated attribute extraction/addition to search as a filter
      - search results as graphs: variables entered in search to display relationships found in data or graph images or graphetized articles
      - processed (aggregated) results - find the average/combined or plain language definition when searching for a definition
      - predicting what questions theyll ask next and adding those search results (or a summary) on the side
      - intent-based search guidance:
        - usually people who search for an answer are studying for a test, so additional widgets like suggested content could include snapshots of/links to: 'study guides', 'summaries', 'tutorials'
        - people searching for recipes are hosting a party & cooking other things, so suggested content could include snapshots of/links to: 'flavor graphs'
        - people searching for symptoms are trying to diagnose themselves or someone else, so suggested content could include links to diagnostic tools or graphs of symptom set frequency for conditions

      - automatic aggregated information formatting queries as an alternative to unstructured/keyword searches pointing to isolated content in manually entered formats like:

        - 'show me stock/financial instrument/cryptocurrency popularity data in graph format' and the output would be a graph of relative usage statistics available, with suggested content links to definitions of the financial instruments since that's a related intent to looking up their popularity, which implies an intent to invest/profit
        - 'show me product search data according to demos in a table with sorts' and the output would be a table with product search data by age group, economic group, in a table format, with sorts to sort each column
        - 'show me insights from language tutorials' would return a list of insights about learning a language, which is a primary implied intent of that search, with suggested content links to music in that language which is one way to learn a language

        - this would be done by:
          - using previous queries & feedback on search results
          - auto-formatting
          - aggregated data from existing content
          - pulling definitions of keywords like 'demos' to determine what supported keyword they mean, or create a new term out of core functions (groups separated by attribute & attribute value)

      - graph search (with queries like 'show me relationship between time and gdp' or show me relationship between using lysol and cancer')

        - could scan studies related to graph for logical fallacies and adjust graph accordingly, then present a composite graph of data found

        - data from searches & product purchases can be integrated into graph (buying lysol followed by searches for cancer symptoms)

        - 'deploy an AI model to do tasks: find/predict relationship, categorize, or rank' option can be included to train on public data based on plain language queries like the above

      - search data + verified purchases can be used to assess the value of a particular product solution for a problem (like a supplement to treat a health condition), to offset fake reviews or faulty recommendation/removal algorithm or account for product fixes over time, as well as customize it to the user (avoid this product if you have condition x, this product has correlation with onset of condition y

        - customization can also be done for user groups like intelligence - so people likelier to believe a story without checking it like anti-vaxx stories can be shown true stories with more repetition

        - example of a system object being useful for customatization (a false categorization):
          - busy can look like stupidity under certain circumstances - what are those circumstances and when are they most important to avoid 
            (if someone's too busy to check a news site, send them a notification about a pandemic so theyre likelier to see it)

  - shared custom meaning/dictionary maps so communication can be queries on their shared custom dictionary map - or a common map where queries specify pattern & sub-set to apply pattern to, and sub-sets are rotated


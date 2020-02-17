- evaluate how tools develop in problem spaces at different layers:

  - identifying core problems
  - identifying problems with typical solutions of core problems
  - identifying problems with typical regulations/conventions that result from typical solutions or problems
  - evolution of tool types at various levels of implementation & order/phase of problem-solving trajectory:
    - configuration to regulate solution switching
    - dependencies to delegate functionality
    - testing to capture adjacent (one-degree) functionality exploits
    - protocols to reduce solution space vs. enforcing solution rules

- solution attributes

  - solution reusability: how to design/choose solutions for reusability
  - cost/benefit analysis (such as learning/understanding/integration/implementation/migration/functionality gap cost potential)
  - abstraction level: choosing the abstraction level that will reduce misunderstandings while optimizing reusability

  - solution types:
  
    - tools: as an immediate implementation option
    - learning (understanding as an alternative to using/selecting existing tools)
    - problem analysis: calculating probable solution cost, calculating value of problem reduction vs. problem solution (vs. secondary or source problem reduction/solution)

- tool selection (tools as a subset of solutions, which also includes learning, calculating solution metadata before investing)

  - tool indexing

    - tool index update strategy (when do you recalculate tool index):

      - how often do you update your knowledge of new tools/features to make calculations about migrating to/integrating a new tool

    - tool attributes (how do you index tools):

      - optimization
      - granularity/abstraction: needs to do one specific task really well, or needs to cover an abstract problem gap with minimal impact/side effects
      - integrations
      - time to learn/integrate/migrate
      - complexity: is source code available/understandable, how many security researchers have reviewed it using what tools
      - existing tool support
        - does it already interact with our other tools
      - simplicity/understanding status of tool
        - this tool is simple enough to be known to be exploitable in these ways so we have pre-designed plans for using this tool optimally
      - modularity
        - can it be swapped out & replaced seamlessly or does it have other dependencies making replacing it a complex calculation
      - current/planned features
        - it does x or will do x and thats all we care about, bc there arent good alternatives that can do x
      - delegation
        - features are not in a space we want to invest time in building/learning so we need to delegate labor to this tool
      - trust
        - we trust this tool provider bc theyre a, b, c (big company, good disaster response, good feedback integration into tools, etc)
      - standards compliance
        - this tool design implements standards with consistency/completeness
      - incentives
        - if third party tool is provided by a secondary platform/marketplace, 
          what guarantees are offered by the platform provider & by the third party tool provider for implementation side effects
          (third party tool integrated with a secondary platform tool)

- choose processes to automate

  - automation attributes:

    - resource investment (cost/time/security of sending data in a certain format or with a certain procedure)
    - understanding of problem space (are the rules clear enough that we can safely automate with little expectation of variance injection)

- inefficient process identification

  - inefficiency attributes:

    - granular/conflicting intent (only serves one intent optimally at sacrifice of another related intent that people often need together)
    - lack of clarity in cost/benefit structures (bc of abstraction, its not clear how a tool will provide a cost when interacting with another tool)

  - how do you minimize inefficiencies in workflow

    - translating task into clear requirements to reduce questions
    - identifying information gaps to distribute information where its relevant & needed


- error handling

  - what strategies do you use for anticipating problems (of a certain type & in general)

  - add error-generation

    - add diagrams for error types:
      - misalignment
      - assumptions without supporting logical/information links
      - incorrect position/function/structure/scope/limit/range/definition

    - examples:
      - p-hacking 
        - what range of significance levels do verified processes exhibit (when first noticed/converging/diverging/decaying)?

      - nearest neighbors hacking

  - give example of error types mapped to structural deficits


- planning decisions

  - how much time do you invest in planning & what are your planning strategies to avoid having to solve problems later?


- learning decisions

  - how do you educate yourself on inherent limitations of a tool 

    - if its designed for another intent
    - if its too new for advanced error handling
    - common problems with tool or third party tool integrations in forum posts/issues
    - corrections/features added by user request in version/release history (to address user identified problems or misunderstandings)

  - identify obvious errors possible in a tool

    - assumptions:

      - in a data visualization tool, an obvious error is data leakage (revealing data that shouldnt be shown to the user)
      - data that is retrievable is assumed to be relevant to the user

    - example:

      - if youre tracking the movement of particles in a square shaped container and two of your variables track the movements between opposite corners, their movement might seem directly related, but the reason theyre moving is not a variable relationship, but the shapes nearest to them determining their motion

        - this error (illusion of relationship) has the error stack:

          - mistaking correlation for similarity/equivalence/causation

          - misidentifying variables
            - there shouldnt be variables for the movement in each corner 
            - the variables should be the placement/other attributes of influential objects like corners if the shape isnt as simple as a clearly defined archetype like a square, or the function to generate the shapes having those influential objects

          - mistaking indirect cause for direct cause
            - the reason theyre related is a causal relationship they have in common (shape of corners) but its not a direct relationship (movement in corner A determines or is equivalent to movement in corner B)

        - this is an obvious error of the problem type 'determining movement between shapes' with the attribute:
          - 'shapes having multiple similar sub-objects like corners which can produce the illusion of relationships'
          - which is sub-type of the problem type: 'alignment isnt direct relevance'

        - how would you identify this obvious error in the above problem of predicting movement of particles within a shape container?

          1. you could start on a high level by looking for known error types (false positive) or error causes (false assumption)

          2. you could also start on a low level by generating the full set of different shape configuration data within a space & examining them for errors

            - you can generate the full set of different shape configurations using types, core functions, & interactions:
              - shape types (square, triangle)
              - shape core functions (transforms: scale, remove, expand)
              - shape interactions (combine, collide, oppose)
              - shape components (corners, inflection points, extremes, arcs, diagonals, angles, edges, centers)

            - and then examining them for error types & causes, given error type definitions
              - 'false positive' means 'something that looks like something else but isnt'
                - this can manifest in the problem space as:
                  - 'two different relationships seeming like the same or related relationship'
                    - which in this problem space could be the motion of particles in two similar sub-shapes like corners

          3. you could start with common errors in this & similar problem spaces or space stacks
            - given that a common problem is 'similarity implying relationship' in the stack of spaces (adjacent/causative dimensions), does that problem show up in this problem space, and if so, where is it likeliest to show up? (where are the similarities that could create a false correlation)

          4. you could derive the obvious errors using problem space metadata
            - problem space metadata:
              - allows alignment
              - allows any shape in coordinate plane

            - problem space anti-metadata:
              - no rule preventing repetition:
                - "given that there's no rule in the problem space prohibiting shapes from repeating, and that repeated shapes are possible in space of any dimension greater than 0 (point), repetition could lead to the illusion of a relationship due to similarity in the repeated shapes"


  - how do you decide what to invest time learning

    - example:

      - for instance with splunk, how would you identify what level of expertise is required in order to design optimal queries?
        - different query design + latency + data mismatch because of compute/aggregate/cache data strategies that differ from a standard db implementation

    - the optimal level of learning is where you can:
      - identify a clear design intent for deviations from standard implementations

    - how do you identify lack of knowledge and translate that into optimal search keywords for learning maximization?

      - identify priorities & decision algorithm of tool developers

      - identify abstractions with opinionated implementations

      - identify hidden complexity

      - identify errors from cooperative structures (compounding intent/patterns/gaps) 

      - identify lack of knowledge

        - there is a level & pattern of complexity that is common to understanding of a tool:

          - people dont normally develop a solution of complexity 2 for a problem of complexity 1 - there are reasons for the complexity mismatch
          - so to identify lack of knowledge, look for over-simplification in summarization of a tool
          - sometimes the lack of knowledge will be on the implementation side rather than the user side, bc of lack of planning/organization

      - how do you identify key objects/terms that are necessary for acquiring a functional level of understanding that is capable of anticipating/minimizing errors in implementing that tool?

        - a beginner wouldnt know to search for 'abstract syntax tree' when education themselves about testing tools
        - a beginner wouldnt know to search for 'latency' or 'caching' when learning a new data storage/query tool

      - how do you map lack of knowledge to these terms once you identify lack of knowledge and key terms to acquire functional understanding?

        - you can derive key concepts of the problem space and map them to key concepts of solution space

          - key concepts of security problem space:
            - standardization

          - key concepts of security solution space:
            - standardization applied to code interpretation: formatting/parsing/translation
              - query for 'code security formatting parsing translation' should lead you to 'abstract syntax tree'
                - query result keywords:
                  - interpolation, string 
                    - data type is key concept of string
                      - machine interpretation of data type by language
                        - machine language
                        - query for "code machine language parsing" has suggested related keywords:
                          - Lexical Analysis
                          - Compiler
                          - Backus–Naur Form
                          - Context-free Grammar
                          - Code Generation
                          - query for "code parsing compiler security" or "code parsing lexical security" would then also lead to 'abstract syntax tree' concept in subsequent results
                        - query for "code machine language parsing" leads to "abstract syntax tree" in first few results

          - in this way you can derive which concepts are important to learn to acquire functional understanding for a particular problem

          - how do you score these concepts based on importance, once you find them?
            - repeated abstract concepts inherent to sub-tools like languages (which is a sub-tool of the security intent) are likelier to be important
            - concepts with clear differences in intent are likely to be important (caching & latency reduction are sub-tools of data storage/retrieval intent with clearly different intent matrixes)

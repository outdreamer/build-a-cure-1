
# Analysis Strategies for Application in Specific Problem Spaces

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
    - unenforced expectations (protocols)
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


## Protocol Recommendations
  
  1. Auto-update crypto keys/algorithms to use constants that are always guaranteed to be below x% risk that they'll be hacked given common computational resources.

## function list

  - to do:
    - add functions from interface definitions as files in functions/ folder and resolve duplicates
    - add 'to do' items from analysis & code to do lists as function list with dependencies (finish function list in next 2 weeks)

  - core language functions
    - expand on core math-language operation mapping (like add: combine, subtract: differentiate (isolate difference), multiply: expand by, divide: standardize by) with interface queries for core operations

    - define core operations: apply (expand one by the other), inject (input one to the other), embed (attach one as a component/attribute of the other)
      - the operation of injecting truth into trust on the power interface means applying the truth dynamics as an input to trust dynamics
        - example: what happens when trust is embedded in a context, and one side has more information about untrustworthiness?

  - function to generate function types
      - decoy rules that consider probable usage, so usage follows the actual rule
      - cost-based system rules
        - avoiding assumptions or other objects where the cost of being wrong is too high to recover from 
          - in a case with multiple alternative explanations, but one is very high-cost if it's true or false, so assuming anything that rules it out cant be assumed without a high ratio of information or high number of indicators
        - cost as an aggregation/interaction rule (lowest cost routes should be assumed first)
        - cost that exceeds the value of intent should be assumed to be either false, unlikely, developing into a more efficient rule, being interacted with from another object/function/attribute, or being destroyed

  - definition import function

  - function to select metric threshold value selection

  - after identification functions

    - import rules for selecting interfaces to solve a problem on

      - determine minimum information
      - query for rules making inferences from available information sets
      - Function interface helps find unused functions
      - Intent interface helps predict system priorities & find exploit opportunities
      - System interface helps find efficiencies
      - Pattern interface helps find insight paths/similarities

    - import insight history data to identify insight paths 
      - info insight paths like 'lie => joke => distortion => insight'
      - system insight paths like 'three core functions + combine function with this definition + n distortions to nearest hub'

    - network design favors an adjacency definition that differentiates features
      - to get around this, build in a concept of default core objects like boundaries/limits/intersections to the network structure or data propagation (send data on possible boundary line positions) to look for & focus on those first rather than continuous sets of adjacent high-variance, pattern-containing features
      - why would patterns like textures make it through as a semantic filter - bc the repetition is interpreted as significant by network design, or the texture is likely to be located in more data subsets than a shape
      https://www.quantamagazine.org/where-we-see-shapes-ai-sees-textures-20190701/

    - function to detect patterns in queries & outputs to optimize queries & find insight paths to improve response time

      - example: 3-step jumps with direction change, navigating across a certain pathway in standard structures across interfaces, starting with system then cause & intent, etc
      - this has to identify & remove unnecessary steps that dont change the output
      - identify & replace with faster ways to get to the output without changing the output
      - test cases to determine if output would be changed by removing a step and/or replacing it with another step

  - abstract functions

      - derive combinations & make sure you have full function coverage of all important combinations
        - check codebase function index for combinations
        - check that you have sample data in json for each combination

      - attribute/object/function match functions
      - standardization network-framing function to describe a system as a network (the standard structure) & position each object, identifying connecting functions
      - system analysis function (identify boundaries, gaps, limits, layers, incentives/intents/questions, & other system objects)
      - isolation function, representating function/attribute changes independent of system context with respect to position or time (snapshot/state or subset)
      - function to define (isolate an object/concept/function for identification, identify definition routes)

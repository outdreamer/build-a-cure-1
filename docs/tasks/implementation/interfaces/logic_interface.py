'''
  - definition: 
    - automating the selection, position, optimization, & implementation of logical rules is possible with this analysis 
    - this analysis can optionally include related interfaces of logic (patterns, functions, intent, cause, change) 
    - this analysis is used at its most basic level for identifying valid rules ('x, so y' or 'x, so not z') 
    - relevant logical objects with defined rules optionally include assumptions, requirements, implications, conclusions, fallacies, inferences, etc, and logical structures like sequences, connections, alternatives which follow the rules of logic (some rules have to follow other rules, logically, so their appropriate structure is a sequence - whereas some rules cannot be implemented simultaneously like mutually exclusive rules, so their appropriate structure is a tree branch) 
    - using these logical object definitions & associated logical structures, you can derive what is logical in any given rule set 
    - this means you can derive emergent structures of possible error contexts/rules, like:  
      - when there is a difference between the implication of a rule and the implementation of handlers for that rule, there is an opportunity for misuse of that rule 
      - if you have logic to handle the 'dog chases cat' rule but you don't have logic to connect & handle the causes of that optionally including 'the cat did something', then the 'dog chases cat' scenario could cause variance in the system, such as being used out of context (even when the cat did not do something), or not being prevented in the system (by handling what the cat did to prevent the chase event) 
      - when an assumption may seem to fit in a system where its applied (assume that people are biased), but the implications of that assumption don't fit the system (the system user/designer/implementer may also be biased), the assumption shouldn't be used or should be adjusted to fit the system (all agents are potentially biased at any point because bias is part of the learning process) 
      - enables automation of the selection, structurization (limiting, connecting, scoping, positioning), optimization (reducing number of rules or high-cost rules or distributing/reducing costs better), & implementation of logical rules 

    - add note on evaluating object attributes, plus the ability to occupy invalidating positions/structures or fulfill invalidating intents of a system, and system requirements for those objects (invalidating position/structure/intent) to be possible
      - example: 
        - object attributes: a chemical on its own
        - system position: a chemical adjacent to another chemical in a system with high temperature
        - system structure: a system designed to make any adjacent chemicals explode, vs. a system that standardizes chemicals to a harmless format
        - system position & structure: a chemical with an extra electron at a position in the system where an extra electron would cause an explosion

        - "Similar logical patterns are absent in SARS-CoV-2, indicating that the virus evolved naturally." - the evolution of a virus to fit within certain systems confirms that changing the system metadata (inputs, structure, side effects, priorities, functions) invalidates the virus without invalidating the system
          - removing/adding the transforms that made the virus deadly/innocuous to a system
          - sending type signals within a contained limit around the virus to give the impression of systems that it wouldnt be deadly in
          - changing the position of a virus (so necessary bacteria interpret pathogens as energy sources)

  - functions: 
    - function to identify logical problem types 
      - gaps in logic enforcement (variance gaps, fallacies, incorrect contexts, assumptions) 
      - overlapping/repeated logic checks (extraneous validation) 
      - side effects that don't match function logic objects, like implication 
    - logic correction functions 
      - identify isolated logic operations 
      - identify scope required of each operation 
      - identify required position of each isolated logic operation 
    - logical operations: 
      - building a conclusion out of logical units means each assembly step complies with the rules of the space 
        - "adding a line to a line may produce a square, or an right angle, but it wont produce a circle" 

  - attributes (validity, cohesion (measure of system fit, like fit to a 'common sense' or 'pattern' system)) 

  - objects (fallacy, assumption, implication, justification, explanation, argument, conclusion, contradiction, inference/deduction/guess) 
    - logical fallacy: mismatch of logic structures/functions/objects/attributes (scope, relevance, fit, position), such as a false alternate path with different output metric value than original path
    - assumption: depending on information, like the relevance of a particular rule or insight, as if it is true (or an adjacent/alternative definition of truth, like relevance or fit)
    - implication: context implied by a logical structure, assumption beyond explicit meaning
      - 'dog chases cat' implies context of a prior event like the:
        - 'cat did something' (implies a system where there is a reason of responsibility for every decision or fairness in allocating costs)
          - 'the dog wants something the cat stole' (specific implication)
        - 'the dog is bored' (implies a system where there is lack of work allocation and attention/work are not maximized/optimized)
          - 'the dog doesnt have toys' (specific implication)
        - 'the dog wasnt trained' (implies a system where default behaviors like instincts can be relearned)
      - a headline like 'politician takes a bribe' has implications of relevant context of prior events, like: 
        - 'this is newsworthy since it doesnt happen all the time' (infer a system that doesnt often produce crimes of corruption)
        - 'this is one of the politicians who were caught taking a bribe' (infer a system that is bad at catching criminals)
        - 'this is one of the politicians who the newspaper doesnt like' (infer a system where bias is present in information sources)
        - 'the politician agreed to take the hit for someone else' (infer a system where favors are traded, sometimes to give impressions of false information to protect social assets like reputation)
        - 'the politician was tricked into taking a bribe unknowingly' (infer a system where tricks & liars are common)
        - 'the politician was sacrificed as a scapegoat' (infer a system where criminals' costs are allocated to innocent people)
        - 'this coverage is to pretend the police were making progress against corruption, even though other politicians were also known to take a bribe without the news coverage' (infer a system where information sources enable authorities to hide information about their own decisions that is negative to keep power)
      with varying levels of probability (the more work it takes to generate the justification for an implication, the less likely it is to be true)
    - justification
      - alignment of logical objects (conclusions/assumptions) & related decision objects (patterns, intents) with distortion functions producing the decisions
    - explanation
      - description of logical objects & structures that connect a starting & end rule
        - an explanation of 'how' is a structural route, an explanation of 'why' is a causal route
    - conclusion
      - a logical rule converted into an assumption
    - contradiction
      - a mismatch between rules
      - specific case is a paradox, which is a false contradiction (often from different definitions or scopes of common objects between the rules)
    - inference/deduction
      - matching logical structures
        - if the dog wont stop chasing the cat, someone can infer inferences like that it doesnt want to or that it cannot regulate itself or that it doesnt have other options in another way, like lack of information about negative consequences
      - inferences are potential logical connections, whereas implications are probable logical connections

  - structures: 
    - logical overlap, conflict, limit, gap, misalignment 
    - logical sequence (logic that has a position attribute, where it has to follow or be followed by other logic) 
    - logic tree (logic with contradictory alternatives that cannot occur simultaneously, to handle different conditions) 
    - logical connection (logic that enables other logic, because their inputs, outputs, & objects like implications match rather than contradict each other) 
    - logical circle (a logic structure that depends on its output) 

  - concepts: 
    - necessity (does a route necessarily imply a conclusion) 
  
  - answers questions like: 
    - is this rule logical or does it have logical errors like contradictions 
    - do these rules contradict each other 
    - does this rule fit the system it's used in 
    - is this assumption valid 
    - are these rules fit to the right logical structure  
    - does this rule prohibit another rule 
    - should this rule follow this other rule 
    - what is the implication of this rule 
  
  - solves problems like:
    - construct a logical argument 
    - identify a fallacy

 - examples:

     - if the following code appears in this order:

        - if variable1 is None:
            return False
          return operation(variable1)
        
          - variable1 is not checked for False (theres a gap in enforcement between the None & False definitions) so the operation could fail

        - if variable1 <= 0:
            return False
          return int(variable1)
          
          - theres a potential gap in enforcement of data type, where variable1 might not be an integer even if its positive

        - if not variable1:
            return False
          if variable1:
          
          - there's an unnecessary condition which is invalidated by prior code (if variable1 is not defined, it would never get to the third line, so the third line is unnecessary)
'''
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


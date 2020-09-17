''' executes a problem-solving automation workflow (deconstruct input structure into sub-structures & assemble/integrate into target structure)
          - visuals
            FIG. 12. 'Network of problem sub-problems, breaking a problem into components problems' illustrates an example of breaking a problem into a set of sub-problems, which once solved, can be aggregated with a solution-aggregation method as shown. 
            FIG. 14. 'Design Interface Query' illustrates a method of assembling input information into structural meaning relevant to the input intent, using a structure containing information formats. 
          - break the problem space into sub-problems, that can execute their own interface traversal & solution-matching process to find sub-solutions  
          - find a structure to combine solutions & combine sub-solutions to create the origin problem's solution, once the sub-solutions to sub-problems are found 
          - example logic of function to break a problem into sub-problems, shown in FIG. 12 (Network of problem sub-problems, breaking a problem into component problems) 
            - this logic includes functions to decompose/aggregate problems/solutions (as shown in FIG. 12, Network of problem sub-problems, breaking a problem into component problems) 
                1. decompose a problem into sub-problems
                2. solve sub-problems after the decomposition
                3. identify structures to combine sub-solutions
                4. apply structures to combine solutions & test combined solution output
            - The initial split of sub-problems is indicated in the boxes under the original problem statement, which is 'find a prediction function for a data set'. 
            - The subsequent splits of sub-problems are indicated with the connecting operations creating the splits in between the shapes inside the sub-problem boxes.
            - The bottom half of FIG. 12 indicates a logical solution aggregation structure, which depicts the logical method of aggregating sub-problem solutions into an origin problem solution, formatted as a directed network.
            - The sub-problem aggregating network on the left of the bottom half of FIG. 12 begins to resemble a sub-problem solution aggregating network on the right, with solution details such as requirements, queries, & operations applied.
            - This solution-aggregation structure can be applied to sub-solutions (like by positioning causative sub-solutions before filtering sub-solutions), given the logic establishing precedence (logic derivable with iother interface objects, like using logic interface analysis indicating that requirements establish sequence of conditions, or causal interface analysis indicating that inputs establish direction of causation, since filters can be applied on info, so info is required to use the filter). Because causal structure & generator functions (core functions, variable/component combination functions, base-distortion functions, etc) are alternate solution formats of the origin problem, they can be merged & the output solution can be filtered for success solving the origin problem, 'find prediction function for data set'. 
            - These sub-solutions can be organized by dependence (causal interface) or requirement (logic interface). The causal structures & generator functions can link the data set to an output function format. The function format produced by the causal structures (such as linking variables in a causal network to generate the prediction function) & function generators (such as an average base with distortion functions generating the prediction function) is an input format to the compare function that compares alternative solutions (prediction functions). Applying structure to combine sub-solutions can also be done with analysis from other interfaces (insights like 'connect formats by adjacent structures' or patterns like 'reduce complexity with standardization' or intents like 'find a sequence of solution formats matching this intent sequence').
            1. decompose a problem into sub-problems, using core functions like alternate/meta/find applied to problem objects (like how measurement is a core object of a solution, and the prediction function is the default solution object, and a variable is a sub-component object of the prediction function, and so on) 
              - an example is breaking a problem into a problem of finding core components & arranging them in a way that passes filters formed by its solution requirements 
                - a requirement of a function that follows another is a possible match of input/output, if the functions are dependent, rather than relatively independent functions (occupying different function sequences), thereby translating a requirement to a filter that can be used to reduce the solution space to only function sequences that have matching inputs/outputs. 
            2. solve sub-problems after the decomposition 
            3. identify structures (like a sequence containing combination operations, or other combination structures like an unordered set, or filters) to combine solutions 
              After sub-problems have individual solutions, the user needs a way to integrate the sub-solutions so they can solve the original problem 
              - for example, once the problem is broken into a set of filter structures to reduce the solution space, the user needs a way to arrange those filters so their output generates the solution (so that the input/output of the filters match, & the sequence of filters makes progress toward reducing the solution space). 
              - the positions of each sub-problem set can be derived using logical positioning. A generative set should be followed by a measurement set because the output of the generative set (prediction function generated) matches the input of the measurement set (prediction function to measure); this involves a basic input-output chaining operation as mentioned before. A causal set may identify missing information in a variable set to establish cause between variables - that type of structure (missing information) should be followed either by generating the missing information, and if not generatable, should be integrated into the accuracy/confidence/error metrics, as not being able to find the information required to solve the problem (creating an accurate, robust prediction function). 
            4. apply structures to combine solutions & test combined solution output 
              - function to convert/represent objects (like a system/decisions/problem/solution) as a particular format (like a set of vector trajectories across interfaces, or a function) 
              - function to check if a structure (like a solution) fits/matches another structure (like input assumptions & limits or a solution metric) 
                - checking if a solution matches a metric structure is shown in FIG 11 (Finding alternate solution formats that fulfill different metrics)
                - matching a problem format to a solution format is shown in FIG 9 (Problem formats, with matching solution formats of problem formats) and FIG 10 (Problem-solution structure matching: apply a solution function to a structure containing the problem to find specific solution structures for that problem)
              - FIG. 10 depicts an example of object structure application, by applying a function to a structure containing an object to find specific object structures for that object).
                - Specifically, FIG. 10 depicts an example of applying a solution function (like 'apply definitions of objects') to a structure (like a system or network) containing the problem ('optimize a route'), to find specific solution structures for that problem (like specific functions or routes).
                - As an example, FIG. 10 depicts a route optimization problem structure, to optimize a route from nodes S to E in a system network.
                - The first step in applying one structure to find another is finding & standardizing definitions.
                - The FIG. 10 includes a route optimization problem definition, an efficiency definition, and a cost definition, which can be retrieved from a data store or otherwise found/derived/generated.
                - The default problem structure (for the route optimization problem) can have many solution formats, which apply the definition of efficiency (like resource re-use) and the solution metric (cost-reduction and benefit-maximization to reach the end point from the starting point) to network structures (like paths & nodes), given that the default problem format is in a network structure.
                - Standardize definitions: focusing on the cost-minimizing definition, and the structural definitions of cost, we can standardize definitions to arrive at a structural definition of efficiency by applying the structural cost definitions:
                    - minimizing cost:
                        - minimizing number of steps
                        - minimizing complexity of step
                        - minimizing distance of step
                        - maximizing certainty of step (uncertainty is high-cost)
                        - selecting for necessity of step (only select required steps)
                        - maximizing reuse of step
                        - maximizing abstraction of step (unless abstraction adds steps like queries)
                - Apply definitions to find matching structures: as an example of applying the object definitions to translate the problem into a solution, now that we have a structural definition of efficiency, we can translate the problem from 'find a route between start & end points fulfilling a metric the most' to a problem of 'add efficiencies until cost is reduced'.
                    - Translating the new problem to add more structure (making it more specific & executable) means changing variables like:
                        - scope of cost (whether it reduces all costs or just a certain type of cost or just a cost on a particular route)
                        - type of cost
                        - type of metric calculation (how to calculate cost, cost definition, etc)
                        - type of efficiency (applying structural definitions of efficiency to the network structure, like route invalidation (position start & end in adjacent positions), cost distribution (routes are equally costly), cost reduction (path-shortening, system organization), cost invalidation (routes are equally costly), etc)
                        - logical & causal position of solution (create a cost-reduction generator or reduce costs for just this system)
                        - whether to re-calculate optimized route at each application of additional efficiencies

'''
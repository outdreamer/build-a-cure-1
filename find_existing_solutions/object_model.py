'''
this function set is to automate the generation of logic with a certain intent (find, derive, build) for a particular object:
    (definition, translation, argument, fallacy, insight, perspective, function, solution, etc)

Examples of differentiation/filtering rules for object definitions:

why is object-attribute-rule model insufficient? bc 
    - there are subtypes of rules that need to be handled differently (change rules, boundary rules, etc)
    - objects exist in a broader system that may invalidate isolated analysis (system analysis)
    - the object evolution is not derived (causal analysis can provide this)
    - it doesnt have a model for deriving & applying patterns of change/boundaries/rules

why is pattern separate from function table? bc
    - pattern is a sequence (of anything), function is a sequence (of operations) with expected input/output
    - you want to store some common patterns in a data set (such as variable value trajectories, like if butterfly always comes after larvae),
      so you can identify insights of the data set & similarity to other data sets
    - the function is a specific implementation of a pattern sequence, restricted to operations & input/output, & there are many functions that can produce each pattern

why is function different from insight?
    - function can be an abstract operation applicable to all systems, whereas insights are usually relating one identified object with another identified object, 
    implying a host system like the abstract network if the objects are both concepts & other complex systems on the info layer if the objects are physical
    - there seems to be a gap in insight coverage bc insights arent normally thought of as numerical, but insights can store math relationships if theyre abstract:
        "y = 2x" is not an insight, but "the slope of a function is the rate of change" is an insight, and so is "the slope can be determined from the change in y / the change in x"
    - core functions like "split this sequence into its smallest parts" arent an insight, its a function 
    - it might be an insight if it was "the optimal way to solve an unknown problem is break it down",
        which has a related object in the form of the function output (achieve the intent: "solve a problem")
    - functions are relationships between objects like insights are, but insights contain information about optimal & true paths between objects

why is strategy different from insight?
    - insight is the rule, strategy applies a rule in a context to achieve a goal
    - strategy:
        properties:
            - a context condition, involving evaluating information about objects in isolation, without a system context
            - an intent
            - insight(s) describing the functions needed to get from starting point (condition x) to the goal (z)
            - objects & a function relating them

        - ex: 
            - "given condition x, do function y to achieve intent z"
            - "if the object is decomposable into subcomponents, split it into sub components & handle them separately to achieve the goal of deriving its functions"

        - sometimes there will be strategies that have no context so theyre basically just core functions,
            like:
                - "break into smaller objects and handle those one at a time", 
                which is a strategy that applies to solving problems in general & also fighting pathogen infections in the bio system
                - "break into subsets and recombine to get original"

        - often strategies will involve conditions to choose between insights:
            - "if insight x doesnt work in the range of metric y, try insight z"

    - insight:
        properties:
            - a rule set where the insight applies, explaining how one object in the rule set is linked to another
            - bc of this, theyre usually tied to a system context, & applicable in a set of systems rather than applicable to any object
            - objects & a function relating them
        - ex: 
            - "function y is useful for intent z"
            - "power favors decentralization" (system context: abstract network + any system that interacts with the concept of power, which is any system involving resources)

why is intent different from strategy?
    - intent is the target end state, and the strategy is the plan to get there

why is priority different from intent?
    - priority is a concept, intent is a concrete goal

    priority:
        - properties:
            - abstract concept that applies in most if not all system contexts
        - ex: efficiency, balance, fairness, stability, relevance

    intent:
        - properties:
            - current/target objects & functions relating them
        - ex: "if condition x, maintain efficiency of function y outputs"
'''

def derive_objects_in_network(subset, row, av):
    ''' derives objects/nodes in a network using limiting rules to identify unique objects accreting variance sets '''
    return row

def fit(structure1, structure2):
    ''' 
    fit structure1 to structure2
    if structure2 is a structure, this function is checking for a match between the two or a position where they fit 
    if structure2 is a gap, this function is checking if structure1 can explain the gap 
        (fitting a new/transformed model to explain variance left over from other variables)
    '''
    return False

def reduce(structure1, structure2):
    ''' reduce problem structure by solution structure '''
    return False

def find_definition(type, row, av):
    ''' this function:
    - iterates through list of known objects of object_type
    - aggregates lists of patterns, pattern attributes, types, and interactions
    - figures out which are explanatory/determinant variables producing the object
    - determines which attributes vary across examples of the object
    - derives network of rules from patterns & pattern attributes
    - describes rules known to explain variance in object behavior or attributes 
    - identifies patterns explaining types of the object
    '''
    patterns = set()
    variables = set()
    rules = set()
    types = set()
    objects = row[object_type] if object_type in row else None
    if objects:
        pattern_list, articles, av = derive_and_store_patterns(object_type, objects, av)
        if pattern_list:
            patterns = set(pattern_list)
            rules = get_rules_from_patterns(patterns, objects, av)
            variables = get_variables_from_patterns(patterns, rules, objects, av)
            types = get_types_from_patterns(patterns, variables, objects, av)
            extreme_examples = get_extreme_examples(types, patterns, variables, objects, av)
            ''' get most different examples within calculated possible range or within object list '''

    return row

def fill_definition(object_type, row, av):
    '''
     build an object of object_type using row data if present, 
    otherwise fetch definition for object_type & generate using variable type/names/metadata 
    '''
    constructed_object = {}

    definition = find_definition(object_type, row, av)

    if definition:

        for category in definition['types']:
            ''' for dog, this is 'mammal', 'animal', 'oxygen-based life', etc '''
            category_definition = find_definition(category, row, av)

        for attribute in definition['attributes']:
            ''' extremities, priorities, structure, organization, requirements '''

            data_type = attribute['data_type']
            value = None
            if data_type == 'option':
                value = get_random_value(attribute['values']) 
            elif data_type == 'spectrum':
                value = get_random_value(attribute['values']) 
            elif data_type == 'combination':
                value = get_random_subset_mix(attribute['values'])
            elif data_type == 'function':
                ''' 
                can be a function of other attributes that are already filled, 
                or a function to generate attributes like variance 
                '''
                value = apply_attribute_function(object_type, attribute, row)

            if attribute['type'] == 'input':
                ''' this is an input to creating a dog object, like nutrients '''

            else:
                ''' this is an output property, like adaptability '''
                tests.append(attribute['name'])

        for rule in definition['rules']:
            ''' change, boundary, interaction, decision, learning, instinctive '''

        ''' check that all required inputs are populated '''
        for attribute in definition['attributes']:
            if attribute['type'] == 'input':
                if attribute['name'] not in constructed_object:
                    return False
                else:
                    value = constructed_object[attribute['name']] 
                    if not value or value == '':
                        return False

        ''' run output attribute tests '''
        for attribute in definition['attributes']:
            if attribute['type'] == 'output':
                compliance = test_compliance_with_prop(attribute, constructed_object)
                if not compliance:
                    return False

        return constructed_object
    return False

def get_random_subset_mix(values):
    return False

def get_random_value(values):
    return False

def test_compliance_with_prop(attribute, constructed_object):
    return False

def apply_attribute_function(object_type, attribute, row):
    return False
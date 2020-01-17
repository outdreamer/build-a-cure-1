
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
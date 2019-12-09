import itertools
from utils import write_csv

def generate_datasets(component_list, target_component, index, rows):
    '''
    iterate through all combinations of elements in rows and 
    generate a dataset for each one to check for relationships
    '''
    datasets = []
    combination_list = []
    for i in range(0, len(component_list)):
        new_combination = itertools.combinations(component_list, i)
        print('\tgenerate_all_datasets: generating index set for elements', new_combination, 'to predict', new_combination[-1])
        # this doesnt invalidate target_variable param bc we might not always use it in this function
        dataset = generate_dataset(new_combination, target_component, index, rows, True)
        if dataset:
            datasets.append(dataset)
        combination_list.extend(new_combination)
    print('\tgenerate_all_datasets: combination_list', combination_list)
    #list(zip(bio_component_set, meta_component_set))
    return combination_list

def generate_dataset(element_list, target_component, index, rows, write):
    '''
    the intent of this function is to combine two elements like symptoms & conditions into a data set,
    with the goal of exploring all possible prediction relationships between variable sets
    the target_component is the name of the element youre trying to predict ('conditions')
    this will require that you already generated the rows for the other element names in element_list
    right now youre still generating all metadata on every run, 
    but youll need to add filtering by the metadata_keys parameter
    '''
    dataset = []
    filename = ''.join([s[0] for s in element_list]) if len(element_list) > 3 else '_'.join(element_list)
    element_path = ''.join(['datasets/', filename, '.csv'])
    #make sure target variable isnt included in index set except in last position
    for r in rows:
        row = {}
        for field in r:
            if field in element_list:
                row[field] = ','.join(r[field]) if type(r[field]) == set else r[field]
        dataset.add(row)
    if len(dataset) > 0:
        if write:
            wrote = write_csv(rows, element_list, element_path)
            if wrote:
                return element_path
    return False
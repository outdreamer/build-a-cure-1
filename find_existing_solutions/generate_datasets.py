import itertools
from utils import write_csv

def generate_datasets(generate_source, generate_target, index):

    '''
    1. determine which datasets would likely be relevant for the given generate_target
    2. generate combination datasets of the identified relevant datasets

    - generate combination datasets:
        supervised data:
          [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, property] 
          # to predict a certain property that a structure has, like activating a particular gene or binding to something
          [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, genes] 
          # to predict which genes will interact with a compound
          [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, mechanism] 
          # to predict which processes will activate/neutralize/bind with a compound
          [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, metabolism] 
          # to predict how a compound will be metabolized
          [structure, structural_metadata, mechanism_of_action_metadata, sub_component_metadata, dose] 
          # to predict a non-toxic dose of a compound
          [structure, structural_metadata, mechanism_of_action_metadata, symptom] 
          # to predict a symptom caused by a structure
          [symptoms, successful_treatment_structure_label] 
          # to predict successful treatment structures for a set of symptoms
          [symptoms, structure, structural_metadata, mechanism_of_action_metadata, success_for_treating_condition_C] 
          # to predict successful treatment structures for a condition given the symptoms indicating the phase

        sequential data:
          [past_conditions, future_conditions] # to predict the conditions a patient will likely develop
    '''
    
    if generate_target and generate_source:
        generate_source = index.keys() if generate_source == 'all' else generate_source.split(',')
        if generate_source:
            if len(generate_source) == 0:
                generate_source = index.keys()
        rows = read('data/rows.csv')
        if rows:
            combination_list = []
            for i in range(0, len(generate_source)):
                new_combination = itertools.combinations(generate_source, i)
                print('\tgenerate_all_datasets: generating index set for elements', new_combination, 'to predict', new_combination[-1])
                # this doesnt invalidate target_variable param bc we might not always use it in this function
                dataset = generate_dataset(new_combination, generate_target, rows, True)
                if dataset:
                    combination_name = '_'.join(new_combination)
                    dataset_path = ''.join([cwd, '/datasets/', combination_name, '.csv'])
                    save(dataset_path, dataset)
                    combination_list.extend(combination_name)
            print('\tgenerate_all_datasets: combination_list', combination_list)
    #list(zip(bio_component_set, meta_component_set))
    return combination_list

def generate_dataset(element_list, generate_target, rows, write):
    '''
    the intent of this function is to combine two elements like symptoms & conditions into a data set,
    with the goal of exploring all possible prediction relationships between variable sets
    the generate_target is the name of the element youre trying to predict ('conditions')
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
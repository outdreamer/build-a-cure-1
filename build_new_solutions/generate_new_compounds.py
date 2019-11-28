# generate possible compounds, filter the list, and predict if it'll be a good candidate for the target condition the neural network was trained on
# generate possible smile formulas, then check with a validator api

'''
elements are differentiated by their number of protons - a default numerical index with meaning
then after converting smile formula youd have strings like this: 1=(36 38)-39
you could build the bond pair data a little faster with this method than an image 
how will you numericalize the bond pair data?
you could add increasing values for stronger bonds or bigger shapes
could use a recurrent neural net

how many possible compounds are there without filtering?
link_chars = '[].=#$:/\()+-'
range = 100 # find upper limit of atoms per element
(number of element chars 118 + number of possible atoms per element 100 + number of link chars 13) ^ 100 = 2.29719567e236 possible combinations
thats not something we can encode unless validators can drastically reduce that number - could also pull validated compounds from online data sets

bio system macromolecules (DNA, proteins, polymers, cellulose) wont be indexed the same way as compounds so keep the range small
'''

output_label = 'Successful Treatment (true=1, false=0)'
column_list = ['Pair 1', 'Pair 2', output_label]
element_list = ['carbon', 'helium', 'helium ion', 'nitrogen', 'oxygen']  # continue until all the elements & element states you have access to or can make are in this list variable
relationship_list = ['single bond', 'double bond', 'etc']  # this should contain all possible bond types
impossible_rules = ['carbon+some element carbon cant bind to with a certain bond type']  #fill in this list with all known impossible bindings
explosive_rules = ['C3H5N3O9'] #nitroglycerin

# plus any other filtering lists that would exclude a compound from being a candidate for treating a human condition
toxic_rules = []

# now that we have our core components & our filtering rules, we can iterate through all possible combinations:
possible_pairs = [] # initialize a dictionary to store the generated compound combinations that aren't filtered out by any rules

# use the product function to generate all possible connection pairs
# itertools.product('ABCD', 'xy') produces: Ax Ay Bx By Cx Cy Dx Dy

max_number_of_connections = 100 # this should be the maximum number of bonds between molecules in a compound, and may also be the number of features (variables) in your data set if you dont add metadata to your analysi

for generated_pair in itertools.product(element_list):
  if generated_pair not in impossible_rules and generated_pair not in explosive_rules and generated_pair not in toxic_rules:
    for r in relationship_types:
      if ''.join(generated_pair, r) not in impossible_rules:
        possible_pairs.append(generated_pair)

all_valid_molecules = [] # this will store all the valid molecules of various connection numbers

for i in range(0, max_number_of_connections + 1):
  # lets say i=5 for this loop, so we'll be generating all possible molecules with 5 bonds

  new_list = [possible_pairs for j in range(0, i)] # get a list of possible pairs lists of length i to feed into product function
  all_molecules_with_i_connections = itertools.product(new_list)

  valid_molecules = [] # next we'll filter this 

  for m in all_molecules_with_i_connections:
    # validate that this doesnt violate any of the rules

    if m not in impossible_rules and m not in explosive_rules and generated_pair not in toxic_rules:
       # if i is less than your maximum molecule size (5 < 100), you'll need to pad the data with zeros to make sure those columns arent empty

       if i < max_number_of_connections:
          
          m = [*m, *[0] * (max_number_of_connections - i)]

       valid_molecules.append(m) 

  all_valid_molecules.extend(valid_molecules)

# here possible_compounds will contain any combinations that made it through the filters, which you can then feed into your neural network to see if it predicts they will succeed or fail against a medical condition.

# Your generated compounds (essentially your extra test data that you're generating to test the predictions of the network) need to be in the same format & order, & must be scaled & processed the same way as your original training data. 

data_column_list = column_list.remove(output_label)
generated_x = pd.DataFrame.from_records(all_valid_molecules, columns=data_column_list) 

# re-using the same column name list assumes your data is in the same order as original data set if it has embedded positional information
generated_x_test = scaler.transform(generated_x)
predictions = mlp.predict(generated_x_test)

# now you should have output values indicating true/false (should be a 0 or 1 in your actual data set) to the question of whether the neural network thinks this molecule might be a good candidate treatment for this condition.
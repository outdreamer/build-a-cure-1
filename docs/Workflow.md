# Workflow

Overall steps to make a neural network to predict the answer to a question (like 'will this compound probably treat this condition') using supervised learning (training on data that includes the answer category, which is called the target/output label, which in this compound-prediction problem type would be "true" it does make a good treatment candidate for a condition, or "false" it does not)


## 1. Install tools

Run setup.sh on your local after adjusting the variables as needed.
```
setup.sh
```

Login to your server after the script is done with:
```
ssh -i mykeyname.pem ec2-user@<ec2-ip>
```


## 2. Assemble your data

### Option with expert knowledge on a medical condition:

1. Make a spreadsheet
2. Make a column for each variable, and one column for the associated output category value, which the network is being trained to predict
3. Decide which variables you want to use (just the chemical structure, or other metadata about the compound like class, charge, etc)
4. Gather the input variable data in the spreadsheet
5. In the output label column (usually after the input columns), assign a label value to each row indicating whether the associated compound is successful at treating this medical condition. If there are two categories like success/fail, this would be just a 0/1 value.

### Option with script:

Run this command (preferably on your EC2 so you don't have to upload it later) to pull data for chemical structures, specifying which metadata you want to include & for which condition:
```
python3 pull_data.py --metadata "all" --condition "diabetes"
```

This will create the dataset.csv for you out of known & studied compounds, with the final output label column indicating whether each chemical structure is successful at treating diabetes

Metadata options include: 'properties', 'functions', 'contraindications', 'side effects', 'interactions', 'symptoms', 'conditions', 'all'
Condition should be the scientific name for a condition, as used in scientific research studies


## Augmenting Data

It may seem like there isn't much data (if there are 100 compounds that have been tested against this condition, you have 100 rows by default) but that's ignoring all the information about the other compounds people were ingesting that had no effect (normal vitamin intake, normal pollution intake, etc) if there is data on that.

So in addition to those 100 compounds, you also have vitamins & common pollutants (at normal levels), as well as elements & molecules that are in every person's bio-system by default, like oxygen, water, etc, which interact with the sub-systems involved in this condition. Then if you're including microorganisms in this data set (if you can represent them accurately in the same data structure of pairs + connection types), you can include microorganisms that most people have in their system like common gut bacteria, viruses, fungi, parasites, & any byproducts of their interactions, as unlikely to be candidate compounds for this condition. So while that may be assuming a little much, it does augment the data, which means the neural net will likely be more accurate than if you trained on just 100 rows.

Another way to augment the data is by including any variants of molecules that are processed the same way in the bio-system. So rather than just a row for compound A, you'd have a second row for compound A with mod B, which is known to be processed the same way with no emergent properties that might cause side effects in new or edge cases. The "element-element relationship type" structure for each column may be a little simplistic - for example maybe you'd like to examine the impact of molecules in motion (if you have data on that or have a theory about how that interaction would differ). Then you could store data as "element-element relationship type change-rule". It's possible to push more metadata (like adjacent or likely pairs, or properties like decay rate or solubility) in each cell in the spreadsheet but this is a good start.

If you want to add default compounds to your data set, which are unlikely to cure a condition because they're in constant or frequent exposure to the relevant systems for most people (standard vitamins at daily values, common chemicals found in widespread pollution, etc), run augment_data.py:
```
python3 augment_data.py --metadata "all" --condition "diabetes"
```

This is recommended because there will probably not be enough data to train your network on otherwise.


## 3. Execute model training

1. Copy the code of the network & library you want to use from nn_examples.py to a new file called 'train.py'
2. Copy your spreadsheet if it's on your local server to the EC2 instance:
```
scp -i mykeyname.pem dataset.csv ec2-user@<ec2_ip>:/home/ec2-user/build-a-cure/dataset.csv
```
3. Run the nohup command to continue training the model even after you log out of your server:
```
nohup python3 train.py >train.log 2>&1 < /dev/null &
```

## 4. Tune params

Adjust the parameters of the network as needed. This is called hyperparameter selection & you'll find resources like this online: 
https://adventuresinmachinelearning.com/improve-neural-networks-part-1/

Hyperparameter selection can be automated with methods like gridsearch if you have the resources for that. 

Once the network is trained, you can test it on your test data to see if you can increase the accuracy by adjusting the network parameters or data itself.

## 5. Generate set of new compounds to test

To find new drugs for a condition, you'll need to generate the set of possible compounds of a certain size, then filter it by those which are toxic, explosive, or have been ruled out as unsuccessful for this condition in research.
```
python3 generate_new_compounds.py
```


## Choosing a network architecture

- See ML_rules.md for info

## Semantic chemical structure metadata 

- Identify known, available, & derivable chemical properties of a compound
- There will be some redundancy if you include derivable properties with your chemical structure data, so that needs to be considered when customizing your solution.
- The mechanism behind or reason for the successful or failed attack should ideally be included ("this structure on the compound tears the cell barrier" or "induces apoptosis by depriving it of contrary signals", etc) in as structured a format as possible (numerical mappings could work for an initial version)
- Side effect data should be included if possible for a safer drug recommendation function, which means side effect neural networks (& toxic compound identification networks) are prerequisite to this one.
- In terms of other metadata to consider, the standard properties listed on wiki are nice to have but emergent interaction behaviors are the tricky ones that could be really valuable.
- With regard to prediction specificity, you have to decide if you want to predict just compounds relevant to the specific type, or if you want to know about compounds that would treat the broader types of the condition.


## Order of operations

Prerequisites if you want to analyze more than just chemical structure data:
- build networks or functions to identify chemical structure metadata (functions, properties, symptoms, conditions treated, side effects)
- property network/function should include chemical properties like toxicity in humans, dose, etc
- side effect network/function should include impact on processing sub-systems & combined with other medical conditions & compounds
- add metadata to chemical structure spreadsheet


## Alternate tools 

Once the compound data set is built & you have some networks or functions to identify compound metadata, you can check reverse relationships:

- predict chemical structure of a set of properties, side effects, symptoms, or conditions
- generate chemical structure having a property
- predict new conditions triggered by this untested compound
- generate rules necessary for this compound to work
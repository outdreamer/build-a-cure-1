#python3 pull_data.py --metadata "all" --condition "diabetes"

import sys 
for arg in sys.argv:
	print(arg)

# metadata options include: 'properties', 'functions', 'contraindications', 'side effects', 'interactions', 'symptoms', 'conditions', 'all'
# condition param should be scientific name of condition as used in science research studies
# symptom param will be supported in future

''' you also may want to assemble the master data set of chemical structures & conditions they treat as the output label '''

'''
This script will create the dataset.csv for you out of known & studied compounds, 
with the final output label column indicating whether each chemical structure is successful at treating that condition
'''

''' strings to look for on wiki 

Example:
	Cytotoxicity in cancer cells
	anti-tumor
	suppress/interfere/inhibit activity of carcinog/canc/tum

Patterns:
	suppress/interfere/inhibit activity of drug/medication/enzyme
'''
#python3 pull_data.py --metadata "all" --condition "diabetes"

import sys 
for arg in sys.argv:
	print(arg)

# metadata options include: 'properties', 'functions', 'contraindications', 'side effects', 'interactions', 'symptoms', 'conditions', 'all'
# condition param should be scientific name of condition as used in science research studies
# symptom param will be supported in future

'''
This script will create the dataset.csv for you out of known & studied compounds, 
with the final output label column indicating whether each chemical structure is successful at treating that condition
'''

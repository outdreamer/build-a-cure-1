
'''https://www.rd.com/health/best-cancer-hospital-every-state/'''

def get_organizations(condition, org_types):
	'''
	- tool to assemble hospital/research program/university/pharma company or organization data sets
	- tool to filter organizations by medical condition being researched or specialized in
	'''

def get_treatments(condition, context):
	'''
	- tool to assemble treatment data sets
	- tool to filter treatments by success probabilities & relevance based on mutations & other details
	'''

def get_studies(condition, status, success):
	'''
	- tool to assemble research study data sets
	- tool to filter research studies by success & status (in progress, closed, accepting apps)
	'''

def get_doc_insights():
	'''
	- apply insight extraction method to research studies to quickly grasp them
	'''

def get_doctors(condition):
	'''
	- tool to assemble specialist doctor email data sets
	- tool to filter doctors by whether theyre living, accepting new patients
	'''

def get_symptoms(condition):
	'''
	- tool to assemble clinical trial data sets
	- tool to filter clinical trials by application dates, location/hospital, inclusion & exclusion criteria
	'''

''' for diagnosis '''
def get_contraindications(condition):
	''' look for medications that have this condition 
	as a contraindication to use them for eliminating causes '''

''' for alternative treatments '''
def get_all_symptoms_by_phase(condition):
	''' look for info on different types & phases, 
	getting all symptoms in order by timeline
	then look for different treatments, 
	and different alternatives available online & otc,
	filtering by contraindications that are least harmful & most informative
	'''

def find_alt_chemical_structures(structure):
	''' find all the alternative ways a chemical structures 
	could be built with non-toxic substances '''


- find compounds studied for condition A
- find compounds with function X
- find compounds with neutralizing side effects
- find compound with fewest side effects
- find metadata (side effects, functions, known & likely properties) of compound X
- find (effective, toxic) dose of compound X
- find symptoms of condition Z
- find symptoms triggered by compound X

for every function with a compound X input, also find the same for compound mixes and with rules applied (like a particular state or condition or resource limit)

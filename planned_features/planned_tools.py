from chembl_webresource_client.new_client import new_client

''' mine assay, activity & target data to create a prediction function for system impact & side effects '''

''' ideally you want to be able to map predicted compound functions to a general impact which is mapped to side effects '''


def get_alt_treatments(role, function, original_treatment):
  ''' find other inhibitors of cyp3a4, in addition to fluconazole '''
  other_treatments = set()
  return other_treatments

def get_atc_class(class_name):
	print(new_client.atc_class.get(class_name)) #'H03AA03',
	atc_classifications =
	{
		'level1': 'H', 
		'level1_description': 'SYSTEMIC HORMONAL PREPARATIONS, EXCL. SEX HORMONES AND INSULINS', 
		'level2': 'H03', 
		'level2_description': 'THYROID THERAPY', 
		'level3': 'H03A', 
		'level3_description': 'THYROID PREPARATIONS', 
		'level4': 'H03AA', 
		'level4_description': 'Thyroid hormones', 
		'level5': 'H03AA03', 
		'who_name': 'combinations of levothyroxine and liothyronine'
	}


def validate_structure(smile_formula, label):

def get_reason(activity, target):
	''' get the intent that explains why the activity worked on the target
	example: specific like 'pierces cell membrane', general like 'cytotoxic'
	'''

def simulate_interaction(compoundx, compoundy):
	''' check sourceforge for simulators '''

def get_similar_compounds(smile_formula):
	similarity_query = new_client.similarity
    res = similarity_query.filter(smiles=smile_formula, similarity=70).only(['molecule_chembl_id', 'similarity'])
    return res

def get_fingerprint(smile_formula):
	''' fingerprint appears to be the unique id '''
	from chembl_webresource_client.utils import utils
	compound = utils.smiles2ctab(smile_formula)
	fingerprints = utils.sdf2fps(compound)

def get_biggest_common_structure(smile_formulas):
	from chembl_webresource_client.utils import utils
	mols = [utils.smiles2ctab(smile) for smile in smile_formulas]
	sdf = ''.join(mols)
	result = utils.mcs(sdf)

def draw_compound(smile_formula, label):
	''' draw a compound '''
	from rdkit import Chem
	from rdkit.Chem import Draw
	loaded_compound = Chem.MolFromSmiles(smile_formula)
	Draw.MolToFile(loaded_compound, label + ".svg", size=(800, 800))

	''' display chembl compound in jupyter notebook '''
	from chembl_webresource_client.new_client import new_client
	Image(new_client.image.get('CHEMBL25'))
	from chembl_webresource_client.utils import utils
	im = utils.smiles2image(smile_formula)
	mol = utils.image2ctab(im)

def get_categories_from_name(compound_properties):
	category_rules = [
		'If an acid is a binary compound, it is named as hydro[element]ic acid.',
		'If an acid contains a polyatomic ion that ends in -ate, then it is named [ion name]ic acid',
		'If an acid contains a polyatomic ion that ends in -ite then the acid will end in -ous',
		'polyatomic ions with oxygen are called oxyanions'
	]
	'''
	1. pull categories from various names & save as metadata in absence of internet
		IUPAC Names:
			[2-(2,5-dichloroanilino)-2-oxo-ethyl] 2-ethylsulfonylbenzoate
			2-ethylsulfonylbenzoic acid [2-(2,5-dichloroanilino)-2-oxoethyl] ester
			[2-[[2,5-bis(chloranyl)phenyl]amino]-2-oxidanylidene-ethyl] 2-ethylsulfonylbenzoate
			2-esylbenzoic acid [2-(2,5-dichloroanilino)-2-keto-ethyl] ester
		For example, the above IUPAC names would produce the list of categories: 
			ester, acid, amino, radical ('yl'), phenyl group, benzoic acid, acid with polyatomic ion (-ate),  
	'''

def get_steps(source_compound, target_compound):

	''' add filter for target, approval status & condition if you decide to use only chembl data
	activities = new_client.activity
	activities.filter(molecule_chembl_id="CHEMBL25", target_chembl_id="CHEMBL612545", pchembl_value__isnull=False)
	approved_drugs = molecule.filter(max_phase=4)
	drug_indication = new_client.drug_indication
	molecules = new_client.molecule
	lung_cancer_ind = drug_indication.filter(efo_term__icontains="LUNG CARCINOMA")
	lung_cancer_mols = molecules.filter(molecule_chembl_id__in=[x['molecule_chembl_id'] for x in lung_cancer_ind])
	no_violations = molecule.filter(molecule_properties__num_ro5_violations=0)
	tissue = new_client.tissue
	res = tissue.filter(pref_name__istartswith='blood')
	document = new_client.document
	res = document.search('cytokine')
	from chembl_webresource_client.unichem import unichem_client as unichem
	ret = unichem.get('AIN')
	'''

def get_property_predictions():
	'''
	IUPAC name
    InChI name
    pKa
    logP and logD
    Solubility
    NMR spectroscopy
    Isoelectric point
    Charge
    Polarizability
    Topology Analysis
    Geometry data
    Polar Surface Area
    Hydrogen bond Donor-Acceptor
    Refractivity
    Structural Framework
    Lipinski's Rule of Five
    '''
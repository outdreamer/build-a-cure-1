import wget
import urllib
import csv
from xml.dom.minidom import parse
import xml.dom.minidom
from chembl_webresource_client.utils import utils
from chembl_webresource_client.new_client import new_client

'''
Guide to smiles format to represent compounds in strings like: 
CCS(=O)(=O)C1=CC=CC=C1C(=O)OCC

https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system

Smarts queries can be used to find compounds with a certain sub-structure 

branch: parenthesis
atom: square bracket (except atoms of B, C, N, O, P, S, F, Cl, Br, or I, which have no charge, are normal isotopes, not chiral centers & have expected number of hydrogens attached)
bond symbols: . - = # $ : / \
isotope: int + element (carbon-14 = 14c)

You can drastically speed up your analysis if there is an api to check if a compound string is valid,
bc generating smile formulas is quicker than manipulating coordinates
You can probably generate a pretty good prediction function to identify if a compound is valid from existing known compounds
if there is no good validity checker

So you'll be generating multiple datasets:
	- smile + side effects to get a side-effect predictor from formula
	- smile + function to get a function predictor from formula
	- smile + props to get a property predictor from formula
	- chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
	but small changes can invalidate functionality - find a list of those change types
	- to check for validity, you can look for a gui that has validation styling and then find the source code
	the pubchem has a validator in their web ui
		error for invalid structure submitted to api: 
		"Exception during execution: Unable to standardize the given structure"

'''

def check_valid(smile_formula):
	encoded_formula = urllib.parse.urlencode(smile_formula)
	url = ''.join("https://pubchem.ncbi.nlm.nih.gov/#query=", encoded_formula)
	html = wget.download(url)
	error = "Exception during execution: Unable to standardize the given structure"
	if error in html:
		return False
	return True

compound_props = [
	'Compound: Canonicalized','Compound Complexity','Count: Hydrogen Bond Acceptor','Count: Hydrogen Bond Donor',
	'Count: Rotatable Bond','IUPAC Name: Allowed','IUPAC Name: CAS-like Style',
	'IUPAC Name: Systematic','IUPAC Name: Traditional','Log P: XLogP3-AA','Mass: Exact','Molecular Formula','Molecular Weight',
	'SMILES: Canonical','SMILES: Isomeric','Topological: Polar Surface Area','Weight: MonoIsotopic'
]

molecule_props = [
	'acd_logd','acd_logp','acd_most_apka','acd_most_bpka','alogp','aromatic_rings',
	'full_molformula','full_mwt','hba','hba_lipinski','hbd','hbd_lipinski',
	'heavy_atoms','molecular_species','mw_freebase','mw_monoisotopic',
	'num_lipinski_ro5_violations','num_ro5_violations','psa','qed_weighted',
	'ro3_pass','rtb'
]
calculated_props = ['MolecularFormula', 'RingCount', 'NumRotatableBonds', 'HeavyAtomCount', 'MolWt', 'MolLogP', 'TPSA']
full_props = compound_props.extend(molecule_props).extend(calculated_props)				    

def write_compound_csv_from_xml(xml_path, csv_path, get_metadata):
	csv_exists = True if os.path.exists(csv_path) else False
	with open(csv_path, 'w') as f:
		w = csv.DictWriter(f, full_props) if get_metadata else csv.DictWriter(f, compound_props)
    	if not csv_exists:
	    	w.writeheader()
		DOMTree = xml.dom.minidom.parse(xml_path)
		collection = DOMTree.documentElement #PC-Compounds
		compounds = collection.getElementsByTagName("PC-Compound")

		''' to do: reduce overlap in properties, standardize property name from pubchem tag '''
		'''
		<PC-Urn_label>Compound Complexity</PC-Urn_label><PC-InfoData_value_fval>607</PC-InfoData_value_fval>
		<PC-Urn_label>Count</PC-Urn_label><PC-Urn_name>Hydrogen Bond Acceptor</PC-Urn_name><PC-InfoData_value_ival>5</PC-InfoData_value_ival>
		<PC-Urn_label>Count</PC-Urn_label><PC-Urn_name>Hydrogen Bond Donor</PC-Urn_name><PC-InfoData_value_ival>1</PC-InfoData_value_ival>
		<PC-Urn_label>Count</PC-Urn_label><PC-Urn_name>Rotatable Bond</PC-Urn_name><PC-InfoData_value_ival>7</PC-InfoData_value_ival>
		<PC-Urn_label>Log P</PC-Urn_label><PC-Urn_name>XLogP3-AA</PC-Urn_name><PC-InfoData_value_fval>3.5</PC-InfoData_value_fval>
		<PC-Urn_label>Mass</PC-Urn_label><PC-Urn_name>Exact</PC-Urn_name><PC-InfoData_value_fval>415.0047991</PC-InfoData_value_fval>
		<PC-Urn_label>Molecular Formula</PC-Urn_label><PC-InfoData_value_sval>C17H15Cl2NO5S</PC-InfoData_value_sval>
		<PC-Urn_label>Molecular Weight</PC-Urn_label><PC-InfoData_value_fval>416.3</PC-InfoData_value_fval>
		<PC-Urn_label>Topological</PC-Urn_label><PC-Urn_name>Polar Surface Area</PC-Urn_name><PC-InfoData_value_fval>97.9</PC-InfoData_value_fval>
		<PC-Urn_label>Weight</PC-Urn_label><PC-Urn_name>MonoIsotopic</PC-Urn_name><PC-InfoData_value_fval>415.0047991</PC-InfoData_value_fval>
		'''
		fields = {}
		compound_list = []
		for compound in compounds:
			compound_dict = {'properties': {}, 'counts': {}}
			if compound.hasAttribute("PC-Compound_charge"):
				compound_dict['properties']['charge'] = compound.getAttribute("PC-Compound_charge")
			if compound.hasAttribute("PC-Compound_props"):
				property_dict = {}
				properties_list = compound.getAttribute("PC-Compound_props")
				properties = properties_list.getElementsByTagName("PC-InfoData")
				sub_prop_set = properties.childNodes[0].childNodes[0]
				label = sub_prop_set[0].nodeValue
				name = sub_prop_set[1].nodeValue if 'name' in sub_prop_set[1].nodeName else ''
				full_name = ''.join(label, ": ", name)
		   		val = properties.childNodes[1].childNodes[0].nodeName
		   		value = properties.childNodes[1].childNodes[0].nodeValue
		   		if full_name not in fields:
		   			datatype = 'double' if 'fval' in val else 'string' if 'sval' in val else 'fingerprint' if 'binary' in val else 'uint' if 'ival' in val else ''
			   		fields[full_name] = datatype
		   		compound_dict['properties'][full_name] = value
		   	if compound.hasAttribute('PC-Compound_count'):
		   		#add processing if needed (heavy atom, chiral atom, chiral bond, isotope atom, covalent unit, tautomers)
		   		count = compound.getAttribute('PC-Compound_count')
		   		for item in count.childNodes[0]:
		   			compound_dict['counts'][item.nodeName] = item.nodeValue
		   	if get_metadata:
			   	''' get metadata for this formula '''
			    formula = compound_dict['SMILES: Isomeric']
			    standard_formula = standardize_compound(formula)
				calculated_properties = get_calculatable_properties(standard_formula)
			    molecule = get_molecule(standard_formula)
			    molecule_properties = molecules['molecule_properties']
			    for prop in molecule_properties:
			    	compound_dict[prop] = molecule_properties[prop]
				for key in calculated_properties:
					compound_dict[key] = calculated_properties[key]
		  	compound_list.append(compound_dict)
		  	DictWriter.writerow(compound_dict['properties'])
		f.close()
	return True

def get_molecule(smile_formula):
	''' 
	https://github.com/chembl/chembl_webresource_client
	overlap between pubchem (100+ million) & chembl (1.8 million) will be small
	also not sure unichem has the data I need
	'''
	molecule = new_client.molecule
	m1 = molecule.get(smile_formula)
	return m1
	'''
	{
	 'atc_classifications': ['L01XE07'],
	 'availability_type': '1',
	 'biotherapeutic': None,
	 'chirality': '2',
	 'dosed_ingredient': True,
	 'inorganic_flag': '0',
	 'natural_product': '0',
	 'oral': True,
	 'parenteral': False,
	 'polymer_flag': False,
	 'prodrug': '0',
	 'therapeutic_flag': True,
	 'topical': False,
	 'usan_stem_definition': 'tyrosine kinase inhibitors'
	 }
 	'''

def standardize_compound(smile_formula):
	mol = utils.smiles2ctab(smile_formula)
	st = utils.standardise(mol)
	return st

def get_calculatable_properties(smile_formula):
	compound = utils.smiles2ctab(smile_formula)
	'''
	num_atoms = json.loads(utils.getNumAtoms(compound))[0]
	mol_wt = json.loads(utils.molWt(compound))[0]
	log_p = json.loads(utils.logP(compound))[0]
	tpsa = json.loads(utils.tpsa(compound))[0]
	from chembl_beaker.beaker.core_apps.descriptors.impl import _getNumAtoms,_getNumBonds, _getLogP, _getTPSA, _getMolWt, _getDescriptors
	['MolecularFormula', 'RingCount', 'NumRotatableBonds', 'HeavyAtomCount', 'MolWt', 'MolLogP', 'TPSA']
	'''
	descriptors = json.loads(utils.descriptors(compound))[0]
	return descriptors

def download_data(datatype):
	multiplier = {
		'Compound': 5584,
		'Substance': 15483
	}
	filename = ''.join(datatype, '_', lower, '_', upper, '.xml.gz')
	url = ''.join('ftp://ftp.ncbi.nlm.nih.gov/pubchem/', datatype, '/CURRENT-Full/XML/', filename)
	localcopy = wget.download(url) #wget.download(url, bar=bar_thermometer) if you want to see download progress
	print('localcopy', localcopy)
	''' some files in the pattern dont exist, like Substance_000025001_000050000.xml.gz '''
	return filename

def download_xml_and_make_csv():
	cwd = os.getcwd()
	data_directory = '/'.join(cwd, 'data')
	directory = os.path.dirname(data_directory)
	if not os.path.exists(directory):
		os.mkdir(directory)
	datatypes = ['Compound', 'Substance']
	for datatype in datatypes:
		for i in range(0, multiplier[datatype]):
			upper = i * 25000
			lower = (upper - 25000) + 1
			downloaded_file = download_data(datatype)
			downloaded_path = ''.join(cwd, '/', downloaded_file)
			csv_path = downloaded_path.replace('xml.gz', 'csv')
			if os.path.exists(downloaded_path):
				unzip_command = ''.join('gunzip ', downloaded_file)
				os.system(unzip_command)
				wrote_csv = write_compound_csv_from_xml(downloaded_path, csv_path, True)
import wget
import urllib
import csv
from xml.dom.minidom import parse
import xml.dom.minidom
from chembl_webresource_client.utils import utils
from chembl_webresource_client.new_client import new_client

'''
- Guide to smiles format to represent compounds in strings like: 
    https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system
    CCS(=O)(=O)C1=CC=CC=C1C(=O)OCC

- Bond symbols:
    '-': isotope (carbon-14 = 14c)

    '=', '#', '$': Double, triple, and quadruple bonds are represented by the symbols =, #, and $ respectively

    '.': An additional type of bond is a "non-bond" indicated with . to indicate that two parts are not bonded together

   ':':  An aromatic "one and a half" bond may be indicated with :

    '/', '\': Single bonds adjacent to double bonds may be represented using / or \ to indicate stereochemical configuration

    - numbers: may indicate open & close of a ring structure, so include the first & last atom in the ring if you prep bond data
    - (): branch
    - []: atom (except atoms of B, C, N, O, P, S, F, Cl, Br, or I, which have no charge, are normal isotopes, not chiral centers & have expected number of hydrogens attached)

Limitations:
    - SMILES strings can specify the cis/trans configuration around a double bond, and can specify the chiral configuration of specific atoms in a molecule.
    - SMILES strings do not represent all types of stereochemistry:
        - Gross conformational left or right handedness such as helicenes
        - Mechanical interferences, such as rotatable bonds that are constrained by mechanical interferences
        - Gross conformational stereochemistry such as the shape of a protein after folding

Chem rules:
- The bond may result from the electrostatic force of attraction between oppositely charged ions as in ionic bonds or through the sharing of electrons as in covalent bonds. 
- The strength of chemical bonds varies considerably; there are "strong bonds" or "primary bonds" such as covalent, ionic and metallic bonds, 
and "weak bonds" or "secondary bonds" such as dipole–dipole interactions, the London dispersion force and hydrogen bonding. 
- Bond order is determined by the number of electrons available to bind with on each atom's outer layer
- when sharing more than one pair of electrons with one or more atoms, elements can form multiple covalent bonds
- # of valence electrons needed to form octet equals # of covalent bonds that can form
- electronegativity difference between two atoms in a bond can determine what type of bond is used. Note that this usually only applies to covalent and ionic bonds.
    ΔEN>2,the bond is ionic
    0.5≤ΔEN<2,the bond is polar covalent
    ΔEN<0.5,the bond is non-polar covalent
- inert/noble/halogen gases like Ne: they don't form compounds
- they don't bond because each atom the element has 8 valence electrons already. so they are stable, they don't need to bond in order to become stable
- elements with full outer electron layer also wont bond
- since carbon's electron configuration is such that it can accommodate four covalent bonds, it forms covalent bonds very readily & isnt seen in ionic compounds
- electronegativity is the tendency of an atom to pull electrons toward itself when it forms a bond with another atom
- similar electronegativities = covalent bonds (e.g. CO2, H2O) while very different electronegativities = ionic compounds (e.g. NaCl)
- less electronegative elements are "metals" and more electronegative elements in the top right of the PT are "non-metals"
- metal + non-metal = ionic compounds, and non-metal + non-metal = covalent compounds, metal + metal = alloys

- so usually the bond type (covalent vs ionic) & bond order (single, double, triple) will be straightforward to calculate, with some variation if its an ion or other configuration.
- I suppose you could use notation like [number of electrons 1][number of electrons 2].bondtype, which wouldn't erase info if you could preserve the original values after accounting for rounding error

- you could also check the reaction with chemlib's reaction product tool 
another way you could encode it is by using the # of electrons in the first atom in each pair as the x value,
 and # of electrons in the second atom as the y value 
 (optionally including the bond type as z value by strength" & graphing it, 
then deriving the function for each cluster of points using standard math
do chemical compounds with similar formulas calculated in this way share properties?
this implies the side of each bond has embedded meaning since youre grouping them: 
'all the right-side values are x', 'all the left-side values are y'
should you repeat the values to erase this bias? like h2o would be represented as pairs:
[ho], [oh] rather than [ho] and [h, Null]

the meaning is the relationship between bonded elements,
 as well as the sequence between groups of bonded elements so I think its legit
how do you preserve sequence order in that situation?
do you assign an ordinal variable to each pair, so your data set is:
    1,h,o,bondtype, 2,h,o,bondtype
and you have 4 dimensions to graph instead of 3?
once you have the function, each chemical can be represented by its coefficients

if you have a function to calculate/predict bond strength between two atoms given their identity & electron count, 
that could be useful data as well, beyond the bond order

'''

def get_item(s, index, next_type, next_order):
    chars = '()[]=1234567890@#$\/.:=-+'
    item_index = index + 1 if next_order == 'next' else index - 1
    if next_order == 'next' and len(s) > (index + 1):
        if next_type == 'element':
            return s[index] if s[index] not in chars else get_next(s, item_index, next_type)
        else:
            return s[index] if s[index] in chars else get_next(s, item_index, next_type)
    elif next_order == 'prev' and (index - 1) >= 0:
        if next_type == 'element':
            return s[index] if s[index] not in chars else get_next(s, item_index, next_type)
        else:
            return s[index] if s[index] in chars else get_next(s, item_index, next_type)
    return False

def convert_smile_to_bond_pairs(s):
    xs = []
    ys = []
    order = []
    index = 0
    formula_length = len(s)
    for i in range(0, formula_length):
        if i < (formula_length - 1):
            if i == 0:
                next_element = get_item(s, i, 'element', 'next')
                next_char = get_item(s, i, 'char', 'next')
                # to do: include analysis for which chars indicate no bond with the next element, which is mostly '.' 
                # unless there are no bonds left to make (like in a branch)
                if next_char == s[i+1] and next_char == '.':
                    continue # go to next pair
                bonded_pair = (s[i], next_element)
                xs.append(s[i])
                ys.append(next_element)
                index += 1
                order.append(index)
            else:
                previous_element = get_item(s, i, 'element', 'prev')
                previous_char = get_item(s, i, 'char', 'prev')
                if previous_char != '.':
                    bonded_pair = (previous_element, s[i])
                    xs.append(previous_element)
                    ys.append(s[i])
                    index += 1
                    order.append(index)
                # to do: include analysis for which chars indicate no bond with the next element, which is mostly '.' 
                # unless there are no bonds left to make (like in a branch)
                next_element = get_next(s, i, 'element', 'next')
                next_char = get_next(s, i, 'char', 'next')
                if next_char == s[i+1] and next_char == '.':
                    continue # go to next pair
                bonded_pair = (s[i], next_element)
                xs.append(s[i])
                ys.append(next_element)
                index += 1
                order.append(index)   
            # to do: calculate bond order & strength & type
        else:
            print('odd chars count', s[i])
    print(xs, ys, order)
    return {'x': xs, 'y': ys, 'order': order}

def calculate_bond_strength(element1, element2):
    return False

def check_valid(smile_formula):
    '''
    https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/substructure/smiles/C3=NC1=C(C=NC2=C1C=NC=C2)[N]3/XML
    get listkey from previous output
    https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/listkey/xxxxx/cids/XML 
    see if chembl has support for search that returns the error text
    '''
    error = "Exception during execution: Unable to standardize the given structure"
    molecule = new_client.molecule
    molecule.set_format('json')
    result = molecule.filter(smiles=smile_formula)
    print('result', len(result), result, dir(result))
    for item in dir(result):
        value = getattr(result, item)
        print('value', item, value)
    if len(result) == 0:
        ''' this doesnt mean its invalid, just that its not in their db '''
        # _handle_database_error has more relevant errors
        if error in result:
            return False
    return True

''' full list of pubchem props here: https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest '''
final_props = [
    'Compound: Canonicalized','Compound Complexity','Count: Hydrogen Bond Acceptor','Count: Hydrogen Bond Donor',
    'Count: Rotatable Bond','IUPAC Name: Allowed','IUPAC Name: CAS-like Style',
    'IUPAC Name: Systematic','IUPAC Name: Traditional','Log P: XLogP3-AA','Mass: Exact','Molecular Formula','Molecular Weight',
    'SMILES: Canonical','SMILES: Isomeric','Topological: Polar Surface Area','Weight: MonoIsotopic',
    'acd_logd','acd_logp','acd_most_apka','acd_most_bpka','alogp','aromatic_rings',
    'full_molformula','full_mwt','hba','hba_lipinski','hbd','hbd_lipinski',
    'heavy_atoms','molecular_species','mw_freebase','mw_monoisotopic',
    'num_lipinski_ro5_violations','num_ro5_violations','psa','qed_weighted',
    'ro3_pass','rtb',
    'MolecularFormula', 'RingCount', 'NumRotatableBonds', 'HeavyAtomCount', 'MolWt', 'MolLogP', 'TPSA'
]
molecule_props = [
    'acd_logd','acd_logp','acd_most_apka','acd_most_bpka','alogp','aromatic_rings',
    'full_molformula','full_mwt','hba','hba_lipinski','hbd','hbd_lipinski',
    'heavy_atoms','molecular_species','mw_freebase','mw_monoisotopic',
    'num_lipinski_ro5_violations','num_ro5_violations','psa','qed_weighted',
    'ro3_pass','rtb'
]
calculated_props = ['MolecularFormula', 'RingCount', 'NumRotatableBonds', 'HeavyAtomCount', 'MolWt', 'MolLogP', 'TPSA']

def write_compound_csv_from_xml(xml_path, csv_path, get_metadata):
    csv_exists = True if os.path.exists(csv_path) else False
    with open(csv_path, 'w') as f:
        w = csv.DictWriter(f, final_props) if get_metadata else csv.DictWriter(f, compound_props)
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


smile_formula = 'CO'
check_valid(smile_formula)

error_formula = 'CCS(=O)(=O)C1=CC=CHHNHC=C1C(=O)OCC'
check_valid(error_formula)
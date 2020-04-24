# Overview

This tool helps you pull semantic chemical structure metadata.
It will also guide you in building neural networks on that data to make prediction functions that can identify new possible drugs to treat a medical condition.

In future, this tool will help you execute more advanced functions, like:
- recommending a treatment dose given a patient's condition
- designing a stressor plan to fix a medical condition in the absence of any substances that can treat it directly

# Current Functionality

Right now these are the supported use cases/features:

## 1. Generate graph from Smile Formula Bond Pairs

Running generate_smile_graphs.py with a "smile" parameter will generate the bond-pairs from the formula & graph them, 
then store those images in the graphs directory.

The parsing of the formula needs improvement.
```
python3 generate_smile_graphs.py --smile "O=C=O=C=ONHO"
```

## 2. Generate smile formulas of length n

Error parsing needs to be handled better but is logged in data/errors_generated_formulas.txt
Only set a large n if your hardware can handle it.
```
python3 generate_smile_graphs.py --generate 3
```
This will store the generated smile formulas in data/valid_generated_formulas.txt,
after first checking them for obvious errors with the indigo tool.

To convert these formulas into the bond-pair numerical format used in the graph function (#1),
adjust the bonds & graph parameters of the generate_smile_formulas function, which are switched off by default.

## 3. Generate metadata for a keyword

- get all metadata available for a condition:
```
python3 get_metadata.py --metadata "all" --conditions "diabetes"
```
This feature needs a lot of work but it's in progress however will be sporadically functional.

# Setup 

After installing pip3 & python3 (instructions in deploy/setup.sh), you can run:
```
pip3 install -r requirements.txt
```

You need to install Indigo manually for now - download page here: 
https://lifescience.opensource.epam.com/indigo/

# Goals

## Input functions 

These are examples of the core functions of this tool, which pull & process data available online that you can feed into your neural networks.

### Parameters 

Eventually, parameter options will include: 
```
options = [
	'properties', 'treatments', 'contraindications', 'metrics',
	'side-effects', 'interactions', 'symptoms', 'conditions', 
	'bio-metrics', 'bio-symptoms', 'bio-conditions',
	'dependencies', 'alternatives',
	'components', 'stressors', 'outputs', 'inputs', 'filters',
	'functions', 'insights', 'strategies', 'patterns', 'all'
]
```

The metadata that can be requested is the same set of objects, except bio objects (which is intended for a specific patient's data),
and the filters parameter.

The generate param supports the same set of options as the metadata parameter.
This parameter tells the program to combine the requested data into data sets, 
which can be fed into your algorithms to create prediction functions.

Examples:

Pull all metadata for diabetes, then make a dataset where symptoms & conditions are used to predict which treatment would be successful.
```
python3 get_metadata.py --metadata "all" --generate "symptoms,conditions::treatments" --conditions "diabetes"
```

The filters keyword can be used to send params all at once.

### Planned Parameters 

The first version will support fetching studied treatments, then recommending new treatment compounds & microbes

These command options will be supported in future releases rather than mvp:
	--metric "side effects" --filters "minimize"
	--function "neutralize impact of drug X on liver"
	--metadata "stressors" --filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
	--metadata "components" --compound "z" --function "synthesis"
	--bio-metrics "blood ph:7.0,heart rate:60 bpm" --bio-symptoms "fever,tachycardia" --bio-conditions "high blood pressure"

With these tools to pull & organize data, you can build prediction functions.

## Use Cases 

Running get_metadata.py the first time will also generate a small database of insights, strategies, & other objects on your local computer in the data folder, which it will use to speed up future queries.
- pull all metadata:
```
python3 get_metadata.py
```
- pull all metadata & generate all datasets:
```
python3 get_metadata.py --metadata "generate-all" --conditions "diabetes"
```
- get all metadata available for a condition:
```
python3 get_metadata.py --metadata "all" --conditions "diabetes"
```
- find just symptoms & successful treatments of a condition:
```
python3 get_metadata.py --metadata "symptoms,treatments_successful" --conditions "z"
```
- find compounds studied for a condition:
```
python3 get_metadata.py --metadata "treatments" --conditions "diabetes"
```
- find metadata (functions, properties, side effects, symptoms) of compound X
```
python3 get_metadata.py --metadata "all" --compounds "x"
```
- find compounds (microorganisms, genes) with function X
```
python3 get_metadata.py --metadata "compounds" --functions "neutralize impact of drug X on liver"
```
- find compound with fewest side effects
```
python3 get_metadata.py --metadata "compounds" --metrics "side effects" --filters "minimize"
```
- find range of modified compounds with same function X & similar or harmless side effects
```
python3 get_metadata.py --metadata "compounds" --functions "neutralize impact of drug X on liver" --metrics "side effects" --filters "minimize"
```
- find stressors that directly trigger symptom A, function B, metric C, condition D or can construct those objects
```
python3 get_metadata.py --metadata "stressors" --filters "symptoms:A,functions:B,metrics:metricC::metricvalue,conditions:D"
```
- find combinations of components necessary to synthesize a compound
```
python3 get_metadata.py --metadata "components" --compounds "z" --functions "synthesis"
```
- find out if a particular combinations of components can synthesize compound x using standard (non-experimental) methods
```
python3 get_metadata.py --metadata "compounds" --components "a,b,c" --functions "synthesis" --strategies "standard" --filters "compounds:x"
```
- find (effective, safe range, toxic) dose of compound X for a person with a set of biometrics, symptoms, & known conditions
```
python3 get_metadata.py --metadata "compounds" --bio-metrics "blood ph:7.0,heart rate:60 bpm" --bio-symptoms "fever,tachycardia" --bio-conditions "high blood pressure"
```

## Output functions

Using the above input functions in this tool, you can build prediction functions with neural nets, like:

- predict metadata (functions, properties, side effects, symptoms) of compound X
- predict metadata of compound mix X
- predict symptoms of compound X
- predict stressors to fix condition Z
- predict steps to synthesize a new compound
- predict which bioassays a compound will be active in

For every function of compound X, also predict the same for compound mixes and with rules applied.

## Feature Roadmap

In future, this will integrate causal, pattern, intent, & system analysis to reduce the amount of neural network training & data required to build these prediction functions.

This will also be able to identify other types of treatment options than chemical compounds, like:
- protein sequences
- enzymes
- genes
- nucleotide sequences
- microorganisms
- cell structures

Unsupervised learning & other methods will also be integrated in imminent versions.

# Deployment

Azure & Gcloud samples will also be added in addition to the existing AWS implementation.

# Data Sources & Tools

	## Guide to smiles format to represent compounds in strings like: CCS(=O)(=O)C1=CC=CC=C1C(=O)OCC
  	https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system

	### Bond symbols
	    '-': isotope (carbon-14 = 14c)
	    '=', '#', '$': Double, triple, and quadruple bonds are represented by the symbols =, #, and $ respectively
	    '.': An additional type of bond is a "non-bond" indicated with . to indicate that two parts are not bonded together
	    ':':  An aromatic "one and a half" bond may be indicated with :
	    '/', '\': Single bonds adjacent to double bonds may be represented using / or \ to indicate stereochemical configuration
	    - numbers: may indicate open & close of a ring structure, so include the first & last atom in the ring if you prep bond data
	    - (): branch
	    - []: atom (except atoms of B, C, N, O, P, S, F, Cl, Br, or I, which have no charge, are normal isotopes, not chiral centers & have expected number of hydrogens attached)

	### Limits
    - SMILES strings do not represent all types of stereochemistry:
        - Gross conformational left or right handedness such as helicenes
        - Mechanical interferences, such as rotatable bonds that are constrained by mechanical interferences
        - Gross conformational stereochemistry such as the shape of a protein after folding

- UniChem has some of PubChem & ChemBl & SureChemBL:
https://www.ebi.ac.uk/unichem/ucquery/listSources

- Drug interactions:
http://bioinformatics.charite.de/supercyp/

- Patented compounds:
https://www.surechembl.org/search/

- Pubchem looks like it has a good format for structural data of its compounds:
https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/SID/387022308/record/JSON/?deposited=t&version=1&response_type=display
https://pubchem.ncbi.nlm.nih.gov/compound/53994448

- Api docs:
https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial

- Bulk downloads:
https://pubchemdocs.ncbi.nlm.nih.gov/downloads

- List of data sources:
https://cactus.nci.nih.gov/
https://cactus.nci.nih.gov/links/chem_www.html

- Generated compound/reaction/rule downloads:
https://cactus.nci.nih.gov/download/savi_download/

- Other sources:
https://libraries.mit.edu/scholarly/publishing/apis-for-scholarly-resources/
https://dev.elsevier.com/sd_apis.html
https://www.mediawiki.org/wiki/REST_API
https://en.wikipedia.org/api/rest_v1/page/summary/Stack_Overflow
http://export.arxiv.org/api/query?search_query=all:electron
ftp://ftp.ncbi.nlm.nih.gov/
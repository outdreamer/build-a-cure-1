# Overview

This tool helps you pull semantic chemical structure metadata.
It will also guide you in building neural networks on that data to make prediction functions that can identify new possible drugs to treat a medical condition.

In future, this tool will help you execute more advanced functions, like:
- recommending a treatment dose given a patient's condition
- designing a stressor plan to fix a medical condition in the absence of any substances that can treat it directly

# Goals

## Input functions 

These are examples of the core functions of this tool, which pull & process data available online that you can feed into your neural networks.

Eventually, metadata param options (if applicable) will include: 
```
options = [
	'properties', 'treatments', 'contraindications', 'metrics',
	'side effects', 'interactions', 'symptoms', 'conditions', 
	'components', 'stressors', 'outputs', 'inputs',
	'functions', 'insights', 'strategies', 'patterns', 'all'
]
```
- find symptoms of condition Z
```
python3 pull_metadata.py --metadata "symptoms" --condition "z"
```
- get all metadata available for a condition:
```
python3 pull_metadata.py --metadata "all" --condition "diabetes"
```
- find compounds studied for condition A
```
python3 pull_metadata.py --metadata "treatments" --condition "diabetes"
- find metadata (functions, properties, side effects, symptoms) of compound X
```
python3 pull_metadata.py --metadata "all" --compound "x"
```
- find compounds (microorganisms, genes) with function X
```
python3 pull_metadata.py --metadata "compounds" --function "neutralize impact of drug X on liver"
```
- find compound with fewest side effects
```
python3 pull_metadata.py --metadata "compounds" --metric "side effects" --props "minimize"
```
- find range of modified compounds with same function X & similar or harmless side effects
```
python3 pull_metadata.py --metadata "compounds" --function "neutralize impact of drug X on liver" --metric "side effects" --props "minimize"
```
- find stressors that directly trigger symptom A, function B, metric C, condition D or can construct those objects
```
python3 pull_metadata.py --metadata "stressors" --props "symptom:A, function:B, metric:metricC::metricvalue, condition:D"
```
- find combinations of components necessary to synthesize a compound
```
python3 pull_metadata.py --metadata "components" --compound "z" --function "synthesis"
```
- find out if a particular combinations of components can synthesize compound x using standard (non-experimental) methods
```
python3 pull_metadata.py --metadata "compound" --components "a,b,c" --function "synthesis" --props "x"
```
- find (effective, safe range, toxic) dose of compound X for a person with a set of biometrics, symptoms, & known conditions
```
python3 pull_metadata.py --metadata "compounds" --bio-metrics "blood ph:7.0,heart rate:60 bpm" --bio-symptoms "fever,tachycardia" --bio-conditions "high blood pressure"
```

The first version will support fetching studied treatments, then recommending new treatment compounds & microbes

These options will be supported in future releases rather than mvp:
	--metric "side effects" --props "minimize"
	--function "neutralize impact of drug X on liver"
	--metadata "stressors" --props "symptom:A, function:B, metric:metricC::metricvalue, condition:D"
	--metadata "components" --compound "z" --function "synthesis"
	--bio-metrics "blood ph:7.0,heart rate:60 bpm" --bio-symptoms "fever,tachycardia" --bio-conditions "high blood pressure"

With these functions, you can build prediction functions.

Running pull_metadata.py the first time will also generate a small database of insights, strategies, & other objects on your local computer in the data folder, which it will use to speed up future queries.

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

# Data Sources

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
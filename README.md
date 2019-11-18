# Overview

This tool helps you pull chemical structure & symptom data & will guide you as you build a neural network on that data that is trained to identify new possible drugs to treat a medical condition.

In future, this tool will help you execute more advanced functions, like designing a stressor plan to fix a medical condition in the absence of any substances that can treat it directly.

# Goals

## Input functions 

These are the core components of this tool, which pull & process data available online to feed into your neural networks.

- find compounds studied for condition A
- find compounds (microorganisms, genes) with function X
- find compounds with neutralizing side effects
- find compound with fewest side effects
- find range of modified compounds with same function X & similar or harmless side effects
- find metadata (functions, properties, side effects, symptoms) of compound X
- find (effective, safe range, toxic) dose of compound X for a person with biometric set A
- find symptoms of condition Z
- find stressors that directly trigger symptom A, rule B, side effect C, function D, property E, or can construct those objects
- find steps to synthesize a compound 

For every function of compound X, also find the same for compound mixes and with rules applied (like a particular state or condition or resource limit)

## Output functions

Using the above input functions in this tool, you can build prediction functions with neural nets, like:

- predict metadata (functions, properties, side effects, symptoms) of compound X
- predict metadata of compound mix
- predict symptoms of compound X
- predict stressors to fix condition Z
- predict steps to synthesize a compound
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

Unsupervised learning will also be integrated in imminent versions.

Azure & Gcloud samples will also be added in addition to the existing AWS implementation.

## Data Sources

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

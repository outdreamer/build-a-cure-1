'''
Side effect keywords to use to test relationships derived with nlp tools:
  - nouns: effect, activation, activity, reaction, process, role
  - adjectives:
  - objects: 
    - functions: attenuate, enhance, reduce, down/up/regulate, stimulate, de/activate, dis/enable, absorb, catalyze, alleviate, suppress, decline, increase, enrich, moderate, adjust, change
    - experiment:
      - properties: parameters, linearity, sensitivity, precision, repeatability, recovery
    - role:
      - inhibitor, antagonist, catalyst, receptor
      - synergy, cooperative, coordinating, enhancing, activating
      - neutralizing, counteracting, disabling, deactivating, anti
    - process:
      - apoptosis
      - glucolysis
      - transcription
    - states:
      - active, inactive
      - inflammation
    - bio properties:
      - fragility
      - toxicity
    - chemical compounds:
      - molecules
      - bonds
      - elements
      - charge
      - electrons
      - ions
    - bio compounds 
      - proteins
      - enzymes
      - lipids
      - genes: expression, active
      - blood
    - cell components:
      - mitochondria
      - nucleus
      - dna
      - membrane
    - microorganisms:
      - bacteria
      - fungi
      - virus
    - tissue:
      - muscle
      - mucus membrane
      - collagen
    - organs: 
      - liver: synoyms (hepatic), components (hepatocytes)
      - kidney
      - bladder
    - systems:
      - lymph
      - nervous
      - immune
      - circulatory
      - digestive
    - treatments
    - conditions: anything ending in -a is usually a condition
    - tests: pcr
    - metric: levels, quantitative, concentration
'''

verification_dict = {}
output_dict = {}

def test_similarity(verification_dict, output_dict):
  '''
  1. check for coverage of verification_dict 
  2. check for errors (missing components, words that are too different to be correct)
  '''

def get_sub_components(condition_keyword):
  ''' when searching for research on a compound or condition, also check for its sub-components, 
      and the compounds its sub-components can be used to make '''

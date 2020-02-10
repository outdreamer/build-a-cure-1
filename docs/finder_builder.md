## General

  - add example of optimal map strategies for decision delegation & reduction
    - deciding degree of variance resolution:
      - when to implement a filtering interface to allow abstract variance or a specific filter to allow specific variance
      - convergence of alternates
      - decision-limiting potential of alternates
      - interaction potential indicating a requirement for investment in input (manual input, alerting configuration, test/analysis automation, etc)

  - generating find/build functions:
    - prioritize defining & assembling type definitions, both with configuration & programmatically using various sources
      - find source types from which others can be derived
      - apply get_definition to get the definition of those source types
      - then apply transform function for each pair to generate a find function for a type given the find function of an adjacent type
      - find functions use primarily patterns & definitions
      - create function that uses definition to generate patterns given variable values/types/metadata
      - build functions can also be generated using the type definition
      - after generating, functions should be checked for non-identifying factors that dont differentiate them across types

  - generating apply functions:
    - match/align/fit a structure to another structure


  - give example of functionality positioning (brain map):

    - high-traffic routes will involve more adjusted functions
    - gaps in routes (such as boundaries) will allow functional modules to evolve
    - progress & computational capacity of the network can be determined from connection ratios:
      - hub-to-hub distance, maximum trajectory distance, etc

      - signal layers can be optimized by order
        - images can be altered to highlight differentiating attributes so that bigger filters (splitting more data) are positioned first


## Code selection algorithm

  - selects function combinations according to data structure & priority at function stack run time

  - example:

    - select code that is optimized for fewest lines of code/quickest execution time/data storage usage/state storage/memory usage based on input data structure & variance

      - "if input has variance k, allow for conditions checking for parameters of variance"
        - "if input has types [a, b, c], select conditions checking for corresponding types [a1, b1, c1]"
                  if word_type in a1_type_list:
                    type_a.add(word)
                  elif word_type in b1_type_list:
                    type_b.add(word)
                  elif word_type in c1_type_list:
                    type_c.add(word)
                  else:
                    no_type.add(word)

        - "if input has types [a], organize code so that assignment is done at end of condition set"
                  word_type = None
                  if original_type in type_list:
                    other_type = logic_operation(word, original_type)
                    if other_type:
                      word_type = other_type
                    else:
                      word_type = original_type
                  if word_type:
                    type_a.add(word_type)

## Code building algorithm

    function_metadata = {'input': line, 'output': pattern, 'attribute': {'subtype': 'type'}}

    Prerequisites:
      - the codebase if available should have index_metadata() run on each function so that metadata is queryable for code-building

    1. generate function interface:
      A. using pattern of other generate_*_pattern(line) functions if any are found in available codebase with indexed function metadata
      B. using definition of pattern found in definitions or functions, which is:
        'a variation of a word list with some words replaced with different types of types'
      C. determining the pattern definition implementation relevant for this function, which is: 
        'a variation of a word list with some words replaced with word types'
      D. checking for a function to determine type of a word
      E. using function find_type, which takes in word & returns types list
      F. using input data type line, split into words
      G. iteration through words in line
      H. if type list is returned from find_type, append type list
      I. if no types found, append word

      def generate_type_patterns(line):
        new_pattern = []
        for w in line.split(' '):
            types = find_type(w)
            if types:
              new_pattern.append(types)
        if len(new_pattern) > 0:
          return new_pattern
        return False

    2. look for other functions with similar interfaces:
      A. note that get_alt_sets has similar input/output:
         input = pattern_line, output = list of words or lists of type options

      B. look at where that function is used (get_alts)

      C. check if get_alts has any useful functionality for generate_type_patterns interface intent 'generate pattern'

      D. note that get_alts has pattern characters '|' in its output, which makes it relevant for 'generate pattern' intent

      E. pull in all logic from get_alts and position existing generate_type_patterns interface logic to route input/output similarly

        def generate_type_patterns(line, av):
          new_pattern = []
          for w in line.split(' '):
              types = find_type(w, av)
              if types:
                new_pattern.append(types)
              else:
                new_pattern.append(w)
          all_alts = []
          if len(new_pattern) > 0:
            all_alts = new_pattern
          index_lists = []
          if all_alts:
              if len(all_alts) > 0:
                  for sub_list in all_alts:
                      if iteration == 0:
                          original_sub_list = sub_list
                          sub_list = sub_list if type(sub_list) == str else ' '.join(sub_list)
                          new_sub_list = remove_unnecessary(sub_list, av)
                          sub_list = new_sub_list if new_sub_list else sub_list
                          if type(original_sub_list) == list:
                              sub_list = ''.join(['|', sub_list, '|'])
                      index_lists = append_list(index_lists, sub_list)
                  index_lists = set([il.replace('  ',' ') for il in index_lists])
                  if len(index_lists) > 0:
                      if '|' in ' '.join(index_lists):
                          if (iteration + 1) <= 1:
                              return get_alts(pattern, iteration + 1, av)
                      return index_lists
          return False

      F. check if all logic is necessary & remove if not:
        - we wont be doing more than one iteration 
        because find_type will not return patterns, only lists, 
        so remove that part of logic pulled in from get_alts

        def generate_type_patterns(line, av):
          new_pattern = []
          for w in line.split(' '):
              types = find_type(w, av)
              if types:
                new_pattern.append(types)
              else:
                new_pattern.append(w)
          all_alts = []
          if len(new_pattern) > 0:
            all_alts = new_pattern
          index_lists = []
          if all_alts:
              if len(all_alts) > 0:
                  for sub_list in all_alts:
                      original_sub_list = sub_list
                      sub_list = sub_list if type(sub_list) == str else ' '.join(sub_list)
                      new_sub_list = remove_unnecessary(sub_list, av)
                      sub_list = new_sub_list if new_sub_list else sub_list
                      if type(original_sub_list) == list:
                          sub_list = ''.join(['|', sub_list, '|'])
                  index_lists = append_list(index_lists, sub_list)
                  index_lists = set([il.replace('  ',' ') for il in index_lists])
                  if len(index_lists) > 0:
                      return index_lists
          return False

        G. do same check for any embedded function calls in get_alts logic (append_list)
          and consolidate variable names:

        def generate_type_patterns(line, av):
          new_pattern = []
          for w in line.split(' '):
              types = find_type(w, av)
              if types:
                  new_pattern.append(types)
              else:
                  new_pattern.append(w)
          if len(new_pattern) > 0:
              index_lists = []
              for sub_list in new_pattern:
                  original_sub_list = sub_list
                  sub_list = sub_list if type(sub_list) == str else ' '.join(sub_list)
                  new_sub_list = remove_unnecessary(sub_list, av)
                  sub_list = new_sub_list if new_sub_list else sub_list
                  if type(original_sub_list) == list:
                      sub_list = ''.join(['|', sub_list, '|'])
              index_lists = append_list(index_lists, sub_list)
              index_lists = set([il.replace('  ',' ') for il in index_lists])
              if len(index_lists) > 0:
                  return index_lists
          return False

        H. verify that output matches intent with test data & match input/output relationships to other generate_*_pattern functions if found

        I. if any other generate_*_pattern functions are embedded in other functions, check if that logic is necessary/relevant to this function intent:
          - generate_indexed_patterns() is necessary to ensure uniqueness of repeated vars in a pattern before storing the pattern
          - generate_synonym_patterns() is relevant if there are any words in this pattern 
          - generate_operator_patterns() is relevant if there are any words that could be standardized to operators in the pattern
          - get_specific_pos() is relevant if variables in the pattern arent already pos tags
          - get_all_pos() is relevant if there are words in the pattern that could be converted to pos tags
          - generate_correct_patterns() is applied to other patterns before applying get_alts()
          - generate_pattern_type_patterns() is relevant in that it assigns types to generate a pattern so this function could be extra useful for input/output relationship comparison


  ### Another function generation example

    - core functions have the property of being very granular while also being broad function categories bc they represent abstract intents, and functions are indexable by intent

    - you could generate logic manually for a problem like: 
      "classify which attribute type this attribute is (input, output, type, abstract, internal)"

    - but you could also generate a function programmatically:

      - to generate a function that classifies an object by an attribute (object=attribute, attribute=type), query definitions of those

        - definition of classification involves verb "filter" or "sort" (standardize "sort" to "filter")
        - filter is a core function, map filter function to classification function using the rest of the definition
        - from original problem definition, this operation should produce: "filter attributes by attribute.type, given set of possible attribute type values"

        1. identify input requirement: "set of possible attribute type values"
          - query for input requirement: "input, output, type, abstract, internal"
          - add variable to contain list of values:
            'values = ["input", "output", "type", "abstract", "internal"]'

        2. identify required function logic operation: "check if variable value in list of values"
          'if attribute.type in values'

        3. identify input requirement: "attribute object has type property"
          - check that requirement is valid across input data, if attribute object definition & usage is accessible
          - add condition to check for this property in the attribute input
            "if 'type' in attribute:"

        4. identify that attribute.type check #3 should precede attribute.type value check #2, because if the attribute.type check fails, the attribute.type value check cant be run
        
        5. identify that an indexed list is required to store output, and find data structure matching that requirement
        'outputs = {}'

        6. identify that the indexed list should contain the attribute identifier (attribute.name) (which is the filtered variable) filtered by type, 
          and that the attribute.type is the indexed list key (filtering variable)

        7. add an insertion of the attribute.name to the indexed list after condition "if 'type' in attribute:"
          'outputs[attribute.type] = attribute.name'

        8. generate a function name based on intent: 
          intent (core function): filter
          inputs: attribute objects
          identifying logic: filter relevance (type)
          - filter attribute objects by a standard of 'type'
          reduce name:
          - classify attributes by type

        9. now you should have an ordered list:
          'def classify_attributes_by_type(attribute):'
          'outputs = {}'
          'values = ["input", "output", "type", "abstract", "internal"]'
          "if 'type' in attribute:"
          'if attribute.type in values'
          'outputs[attribute.type] = attribute.name'

        10. determine output conditions based on conventions or output possibility elimination rules
          'if outputs:'
            'return outputs'
          'return False'

        11. add output conditions

        12. add indentation to organize logic operation order & selection, given function intent
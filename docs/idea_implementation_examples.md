# Idea Implementations

## implementation of idea: "code selection algorithm to select function combinations according to data structure & priority at function stack run time"
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

## implementation of code building algorithm:
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


## Math/Language translation function

  - build math logic/plain language translation function - example: https://adventuresinmachinelearning.com/improve-neural-networks-part-1/
    - in order to implement this, you need to:
      - implement function to break_into_core_functions
      - apply break_into_core_functions() to math and language functions
      - compare both once standardized with break_into_core_functions() & build map of corrollary functions
      - use this as a dictionary for future translation calls

    - example:
      - math rule ''
      - language rule ''
      - math decomposition
      - language decomposition
      - mapping
      
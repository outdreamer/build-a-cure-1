def get_relevant_path(problem_metadata, relevance_filters):
	other_filters = relevance_filters
	relevant_path = []
	specific_attribute_values = []
	for key, value in problem_metadata.items():
		if key in relevance_filters: # functions or whichever filtering key comes first in dict
			other_filters.remove(key)
			if type(value) == dict:
				for function_type, functions in value.items():
					if type(functions) == dict:
						flattened_sub_dict = flatten_dict(functions)
						for rf in other_filters:
							''' if rf = 'required' in functions '''
							if rf in ' '.join(flattened_sub_dict.keys()) or rf in ' '.join(flattened_sub_dict.values()):
								''' check if dict can cast to str or dump json, check that this sub-dict is worth pursuing '''
								for function_name, function_metadata in functions.items():
									''' function_name = change_position '''
									if type(function_metadata) == dict:
										flattened_function = flatten_dict(function_metadata)
										if flattened_function:
											if rf in ' '.join(flattened_function.keys()) or rf in ' '.join(flattened_function.values()):
												''' if rf = 'required' in {"input": {"required": ["incentive", "efficiency", "intent"]}} '''
												for attribute, attribute_metadata in function_metadata.items():
													''' attribute = 'input' '''
													if type(attribute_metadata) == dict:
														for attribute_name, specific_attribute_values in attribute_metadata.items():
															''' attribute_name = 'required' '''
															if attribute_name == rf: # required
																if type(specific_attribute_values) == list:
																	relevant_path = [key, function_type, function_name, attribute, attribute_name]
																	''' relevant_path = ['functions', 'interactions', 'change_position', 'input', 'required'] '''
	if len(relevant_path) > 0 and len(specific_attribute_values) > 0:
		return relevant_path, specific_attribute_values
	return False, False

def get_relevance_filters(relevance_intents, problem_object):

	''' for an intent like 'specificity', which we interpret as 'add conditions/modifiers',
		and a sub-intent like 'find reason/intent', 
			we look up:
				- required inputs 
				- specific intents

		to get guaranteed aspects of the problem object that can be used to modify a general problem step like 'find incentives'
			to add a reason for that step, 
			such as the name/function intents of functions using incentives as an input,
			where the 'reason for the problem_step' is the item we've identified as relevant for the goal of 'find specific intent' for the problem_step
	'''
	search_intents = get_data('search_intents.json')
	if search_intents:
		if 'problem' in search_intents:
			'''
			problem_search_intents = {
				'specificity': [
					['required', 'functions']
				],
				'intent': [
					['required', 'functions'],
					['intents', 'functions']
				]
			}
			'''
			for relevance_intent in relevance_intents:
				if relevance_intent in search_intents['problem']:
					if type(search_intents['problem'][relevance_intent]) == list:
						return search_intents['problem'][relevance_intent]
	return False
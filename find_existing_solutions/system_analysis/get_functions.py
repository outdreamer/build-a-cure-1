from type_functions import *
from utils import get_data 

def get_solution_type(solution_step):
	print('function::get_solution_type')
	type_words = get_type_words()
	solution_words = ' '.join(solution_step).split(' ')
	solution_word_count = len(set(solution_words))
	union_count = len(type_words.union(solution_words))
	''' if difference ratio between total solution step words & common words with type words is small '''
	if union_count / len(type_words) > 0.5:
		return 'type'
	return 'specific'

def get_insights(problem_metadata):
	print('function::get_insights')
	''''
		2. are there insights related to objects in problem metadata?
			- fetch common cross-system insights
			- are there related solution types for the problem, the problem type, the problem components, or related problem types?
	'''
	insights = {'insights': [], 'solutions': []}
	insight_path = 'insights.json'
	insights = get_data(insight_path)
	return insights

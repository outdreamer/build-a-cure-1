'''
	Workflow 1a: Transform into combination of solved problems
	Workflow 1b: Transform into an interface problem type (problem type that can frame all problems, like route optimization, a market trade problem, an inefficiency, or a filtering problem)
		This version skips the problem type analysis & just fetches a solution for common problem types with which other problems can be framed
'''

problem_def = {}
problem_path = 'problem.json'
with open(problem_path, 'r') as f:
	problem_def = f.read()
	f.close()
if problem_def:
	solved = solve_problem_with_problem_type_conversion(problem_def)
	print('solved', solved)

def solve_problem_with_problem_type_conversion(problem_def):

	if problem_def:

		problem_metadata = get_problem_metadata(problem_def)
		insights = fetch_related_insights(problem_metadata)
		related_solutions = []
		related_problems = []
		solved_problem = None
		converted_problem = None

		''' fetch insights related to this problem '''
		if insights:

			if 'solutions' in insights:
				''' found insights about solutions for this problem type '''
				related_solutions = insights['solutions']

			if 'related_problems' in insights:
				related_problems = insights['related_problems']

		''' try solutions identified as related to this problem or problem type before converting '''
		if related_solutions:
			solved_problem = apply_solutions(problem_metadata, related_solutions)
			if solved_problem:
				return solved_problem 

		''' if solutions of this problem type didnt work, try solutions of related problems '''
		if related_problems:
			for p in related_problems:
				converted_problem = convert_to_solved_problem(problem_metadata, p)

		''' if there are no related problem types/related problems, convert to an interface problem type '''
		if converted_problem is None:
			converted_problem = convert_to_interface_problem(problem_metadata)

		''' apply solutions for converted problem '''

		''' to do: before converting to a problem type, check that there are solutions/types available for that problem type '''

		if converted_problem:
			''' get solutions from insights for the converted problem '''
			related_problem_insights = fetch_related_insights(converted_problem)
			if related_problem_insights:
				if 'solutions' in related_problem_insights:
					''' found insights about solutions for related problem type '''
					related_problem_solutions = related_problem_insights['solutions']
					if related_problem_solutions:
						solved_converted_problem = apply_solutions(converted_problem, related_problem_solutions)
						if solved_converted_problem:
							solved_original_problem = convert_solved_problem_to_problem_type(solved_converted_problem, problem_metadata)
							if solved_original_problem:
								solved = test_solution(problem_metadata, solved_original_problem)
								return solved
	return False

''' APPLY DEFINITION '''

def	apply_solutions(problem_metadata, solutions):
	''' to do: decide if you want to return multiple solutions if there are any '''
	solved_problems = {}
	solved_problem = None
	for s in solutions:
		solved_problem = apply_solution_to_problem(problem_metadata, s)
		if solved_problem:
			return solved_problem 
	return False

def apply_solution_to_problem(problem_metadata, solution):
	'''
		4. apply solution for converted problem type
	'''
	solved_problem = {}
	if 'solution_type' in solution:
		if solution['solution_type'] == 'solution_type':
			# this is a solution type, not a specific solution
			solution = apply_solution_type(problem_metadata, s)
			if solution:
				solved_problem = apply_solution(problem_metadata, solution)
		else:
			solved_problem = apply_solution(problem_metadata, s)
		if solved_problem:
			return solved_problem
	return False

def apply_solution(problem_metadata, solution):
	return solved_problem


''' TEST '''

def test_solution(solved_original_problem, problem_metadata):
	'''
		6. test if solution actually reduces or solves original problem
	'''
	passed = is_problem_reduced(problem_metadata, solved_original_problem)
	return passed

def is_problem_reduced(problem_metadata, solved_original_problem):
	passed = False
	return passed


''' OBJECT DEFINITION '''

def get_problem_metadata(problem_def):
	'''
		1. Identify problem metadata
				- problem type
				- default/original problem type (position on problem type network)
				- adjacent problem types
				- component problem types
				- related problem types
				- combination problem types

			- problem structure
				- space (output dimensions to measure solutions)
				- structure (gap/limit/force/conflict/intersection)

			- problem attributes
				- interfaces (dimensions that frame or highlight variable value change rules)
	'''
	problem_metadata = {}
	return problem_metadata


''' QUERY '''

def fetch_related_insights(problem_metadata):
	''''
		2. are there insights related to objects in problem metadata?
			- fetch common cross-system insights
			- are there related solution types for the problem, the problem type, the problem components, or related problem types?
	'''
	insights = {'insights': [], 'solutions': []}
	return insights


''' CONVERSION '''

def convert_to_solved_problem(problem_metadata, target_problem_type):
	'''
		3. if related solution types are found for original/related problem types, how to convert between original & solved problem
			- fetch insights on converting problems to a target problem 
			- if no insights found, apply default process:
				- query source & target problem metadata for common attributes & check for a space that could frame their differentiating attributes 
					(the original problem sapce, the target problem space, or an interim/other dimensional space for conversion)
	'''
	solved_problem = {}
	return solved_problem

def convert_to_interface_problem(problem_metadata):
	interface_problem = {}
	return interface_problem

def convert_solved_problem_to_problem_type(solved_converted_problem, original_problem_metadata):
	'''
		5. convert to original problem type
	'''
	solved_original_problem = convert_problem_to_problem_type(solved_converted_problem, original_problem_metadata)
	if solved_original_problem:
		return solved_original_problem
	return False

def convert_problem_to_problem_type(source_problem_type_metadata, target_problem_type_metadata):
	converted_problem = {}
	if converted_problem:
		return converted_problem
	return False

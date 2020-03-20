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
		converted_problem = {}
		problem_metadata = get_problem_metadata(problem_def)
		insights = fetch_related_insights(problem_metadata)
		if insights:
			if 'solution' in insights:
				''' found insights about related solution/types for this problem type '''
					converted_problem = convert_to_solved_problem(problem_metadata)
		if converted_problem is None:
			converted_problem = convert_to_interface_problem(problem_metadata)
		if converted_problem:
			solved_converted_problem = apply_solution_to_problem(converted_problem)
			if solved_converted_problem:
				solved_original_problem = convert_to_original_problem(solved_converted_problem)
				solved = test_solution(problem_metadata, solved_original_problem)
				return solved
	return False


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

def fetch_related_insights(problem_metadata):
	''''
		2. are there insights related to objects in problem metadata?
			- fetch common cross-system insights
			- are there related solution types for the problem, the problem type, the problem components, or related problem types?
	'''

def convert_to_solved_problem(problem_metadata):
	'''
		3. if related solution types are found for original/related problem types, how to convert between original & solved problem
			- fetch insights on converting problems to a target problem 
			- if no insights found, apply default process:
				- query source & target problem metadata for common attributes & check for a space that could frame their differentiating attributes 
					(the original problem sapce, the target problem space, or an interim/other dimensional space for conversion)
	'''

def convert_to_interface_problem(problem_metadata):


def apply_solution_to_problem(converted_problem):

	'''
		4. apply solution for converted problem type
	'''
	return solved_converted_problem

def convert_to_original_problem(solved_converted_problem):

	'''
		5. convert to original problem type
	'''

	return solved_original_problem

def test_solution(solution, problem_metadata):
	'''

		6. test if solution actually reduces or solves original problem
	'''
	return pass_fail
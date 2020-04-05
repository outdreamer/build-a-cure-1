def test_solution(solved_original_problem, problem_metadata):
	print('function::test_solution')
	'''
		6. test if solution actually reduces or solves original problem
	'''
	passed = is_problem_reduced(problem_metadata, solved_original_problem)
	return passed

def is_problem_reduced(problem_metadata, solved_original_problem):
	print('function::is_problem_reduced')
	passed = False
	return passed
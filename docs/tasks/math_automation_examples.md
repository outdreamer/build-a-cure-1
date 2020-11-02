https://www.onlinemathlearning.com/probability-problems.html

At a car park there are 100 vehicles, 60 of which are cars, 30 are vans and the remainder are lorries. If every vehicle is equally likely to leave, find the probability of:
a) find the probability of van leaving first.
b) find the probability of lorry leaving first.
c) find the probability of car leaving second if either a lorry or van had left first. 
	- concepts: ratio, state, sequence, reduction of sample space

 A survey was taken on 30 classes at a school to find the total number of left-handed students in each class. The table below shows the results:
No. of left-handed students 	
0 	1 	2 	3 	4 	5
Frequency (no. of classes) 	
1 	2 	5 	12 	8 	2
A class was selected at random.
a) Find the probability that the class has 2 left-handed students.

	- problem type: 

		- information gap

			- missing information: 
				- probability of a 2-LH student class

			- given information:
				- n = count in class
				- number of classes with n-LH students
				- relevant definitions:
					- standardized probability definition: ratio of focused outcomes relative to total outcomes, given specified conditions
					- standardized ratio definition: subset of total outcomes fulfilling condition

			- interim information:

				- problem format sequence:

					- find 'operation' structure: the operation that can produce a 'subset' structure
					- convert (find matching) 'metric' structure: the relevant structure matching the metric in the given information (class count ratio with n-LH count)
					- find 'subset' structure: the subset of classes fulfilling the metric
					- apply 'ratio' format: the ratio/proportion represented by that subset
						- selection operation of class count with specified LH metric (2)

		- filter:
			- information boundary: the solution can only include information from classes with the LH metric above a threshold value

	- solution:
		- in order to integrate the problem types information gap & filter into a solution, the connecting information of the information gap problem (connecting the input given info & output missing info) must be derived, then the filter applied to the parameter of the interim info (only some info is input to the interim info operation, input info that is produced by the filter)


	- this problem is an attempt to convert 'count in class' information to 'ratio of count = 2 in all classes' information

		- given info: 'count in class'
		- missing info: 'class count where count = 2 / total class count'
		- apply standardized structural probability definition:
			- apply 'ratio' concept from definition: 'ratio of count in class'
			- apply 'total' concept from definition: 'ratio of count in all classes'

		- apply structural interface to solution structure: 'ratio of count in all classes' = 'subset' structure

		- in order to connect the 'count in class' with the 'ratio of count in all classes', a ratio must be taken, comparing the found count to the total count

		- to produce that information, we need to calculate:
			- the found count
				- apply problem filter: n-LH count where n = 2
					- apply structure to given info: find structure connecting n and n-LH count
						- produces structure: map connecting n and n-LH count
							- apply filter: select mapped value matching n = 2
								- produces structure: '5' value

			- then the total count
				- apply aggregation concept to get denominator:
					- apply 'aggregate' operation to get 'all classes' metric
						- produces structure: '30' value

			- then the ratio of these (with total as the denominator, since the solution format is a subset, or a proportion of a whole)
				- apply 'ratio' structure to 'subset' and 'total' value structures: "'5' / '30'" = 1/6

	- this can take place after standardizing the problem statement to the problem system:

		- find & apply relevant standardizing interfaces, based on given info (including definitions of probability, ratio, etc)

			- if definitions are given or retrievable:
				- apply structure or system interface

			- else:

				- derive definitions:

					- apply object interface

						- find objects/attributes/functions in problem statement: 'find probability of class with 2-LH students'

							- objects: 'probability', 'class', 'student'
								- either derive the function of the 'frequency' concept relative to concepts 'selection sequence' & 'time' as a precursor to the 'ratio' concept, or use language patterns:
									- apply concept interface:
										- frequency: 'outcome count, as a subset of total outcome count'
										- subset: 'count of items with an attribute in a set with variables including that attribute'
										- ratio: 'relationship between subset count and total count'
									- apply pattern interface:
										- probability:
											- 'find x of y' means 'find subset in y set'
											- 'with z' means 'find subset in y set matching z'
											- 'subset' is associated with 'ratio' metric
											- derive structural definition of 'probability': 
												- 'find ratio of subset to set matching metric'
										- class:
											- 'x with z' means 'object with attribute/function/other component'

							- attributes: 'n-LH students in class'
								- identify structure matching this language pattern: 'subset in set' and find structures in given info (map between LH-count and class count)
								- identify variable 'n' in given info & solution filter metric

						- derive relationship between probability & class:
							- combine ('find ratio of subset to set matching metric', 'object with component') = 'find ratio of objects in object set matching component metric'

						- now we have functional definitions:
							- probability is the "application of the 'compare' operation between a subset & a set", or alternatively 'relative frequencies' (sometimes vs. every time)
							- class is an object having an attribute 'count of LH-students' or 'n-LH count'

			- apply problem interface:
					- find problem-solving workflows:
						- apply relevant problem structures to problem type:
							- apply relevant problem structure 'randomly draw sample from set' to this problem type 'find probability': 
								- 'find the probability of randomly selecting an outcome matching this filter from this outcome set'
						
					- find solution format in problem statement:
						- apply structure interface (as in 'apply standardized structural probability definition' section above): 
							solution format: 
								- standardized solution format: 'probability of class count subset compared to total class count'
									- apply 'probability' definition: 'ratio of class count subset compared to total class count'
									- apply 'compare' definition: 'class count subset, divided by total class count'
									- apply other problem metadata & solution format ('subset produced by what filter'): 
										- 'class count matching metric, divided by total class count'
							
					- given that this is a 'find' problem, there will be 'filter' structures to apply to reduce solution space
						- find set of possible filters (metric structure):
							- given attributes (left-handed) & calculatable/derivable object attributes (like count/ratio/difference)
						

b) What is the probability that the class has at least 3 left-handed students?

	- problem type:

		- information gap:

			- missing information:
				- probability of a (3 to upper limit) LH-student class

			- given information:
				- number of classes with n-LH students

			- interim information:

				- find 'operation' structure: the operation that can produce a 'subset' structure
				- convert (find matching) 'metric' structure: the relevant structure matching the metric in the given information (class count ratio with (k ... n)-LH count)				
				- find 'subset' structure: the subset of classes fulfilling the metric
				- apply 'ratio' format: the ratio/proportion represented by that subset

					- in order to connect missing & given information, interim information includes the alternative methods of getting a subset:
						- aggregation operation (adding all the 3 & up LH-student classes, starting from zero)
						- subtraction operation (removing all the lower-than-3 LH-student classes, starting from the total)

		- filter:
			- information boundary: the solution can only include information from classes with the LH metric above a threshold value

	- solution:
		- in order to integrate the problem types information gap & filter into a solution, the connecting information of the information gap problem (connecting the input given info & output missing info) must be derived, then the filter applied to the parameter of the interim info (only some info is input to the interim info operation, input info that is produced by the filter)


c) Given that the total number of students in the 30 classes is 960, find the probability that a student randomly chosen from these 30 classes is left-handed.


ABCD is a square. M is the midpoint of BC and N is the midpoint of CD. A point is selected at random in the square. Calculate the probability that it lies in the triangle MCN. 

	- problem type:

		- missing info: 'ratio' of 'triangle' outcomes in total possible points in 'square' outcome set, selected at random

		- given info: 
			- 'size' of 'triangle' and 'square' ('endpoints' of 'triangle' at 'midpoints' of 'adjacent square sides')
			- 'position' of 'triangle' in 'square' (contained, with aligned edges)

		- interim info:
			- find 'ratio' of 'triangle probability relative to square probability'
				- find 'probability' associated with 'shape'
					- find 'outcome' structure in 'shape' definition: 'point'
					- apply 'aggregate' operation to 'outcomes in shape' structure: 'aggregate points in shape' operation
					- find 'function' structure to 'aggregate points in shape': area function
				- apply 'area function' to find 'triangle probability'
				- apply 'area function' to find 'square probability'
				- divide 'triangle probability' by 'square probability'

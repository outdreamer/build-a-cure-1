# Math terms

- a space is a network: a set with some added structure 

- a topological space:
	- a set of points, along with a set of neighbourhoods for each point, satisfying a set of axioms relating points and neighbourhoods
	- is the most general notion of a mathematical space that allows for the definition of concepts such as continuity, connectedness, and convergence
	- other spaces, such as manifolds and metric spaces, are specializations of topological spaces with extra structures or constraints
	- what is the topology of spaces called?


## Group theory

  - structures to examine:

    - rings for interface network
    - algebras for vertices of a problem space
    - basis of a space: core functions or nodes

## Attributes

	- span of two vectors is the range of their scaled addition = linear combination of vectors
		- if one vector is linearly dependent on the other (can be produced as a linear combination of the others), it's redundant & doesnt add to the span
	- basis of a space: the set of linearly independent vectors that span that space
		- basis vectors i-hat & j-hat are unit vectors of two dimensions x & y
			column 1 = coordinates where i-hat lands
			column 2 = coordinates where j-hat lands
	- transformations keep lines parallel and evenly spaced, and origin is fixed
	- matrix multiplication is applying two transformations, starting from the right side
	- determinant is volume of parallelipiped space created by the vectors
	- degrees of freedom: dimensions of phase space including all possible states of a physical system 
	- jacobi identity: a property of binary operations describing impact of order of operations

	- distance
	- uniqueness
	- equivalence (homeomorphism)
	- intersection (tangent, overlap, collision, cooperation, etc)
	- homogeneity
	- isotropic	
	- continuity
	- convergence
	- connectedness
	- infinity
	- adjacency
	- cooperation (objects/types/attributes)
	- scale
	- discriminant: example of calculating properties of solution without calculating solution directly
		- can tell if solution sub-components (roots) are equal, signed, etc by calculating value of discriminant which is  a function of polynomial coefficients
	- nilpotent

## Types

	- types are determined by sets of attributes (continuous, host system, reversibility, combinability, measurability)

	- number types
	- data types
	- variable types


## Core Shapes

	- vector: intersection of attributes value & direction
	- tensor: 
	- set: accretion of objects
	- unit: lower-dimensional composable threshold for differentiation, syncing, & aggregation of filters (has overlap with interface)
	- map: set of possible transform networks connecting two sets
	- value: difference
	- boundary: stabilized outer range of combinations produceable with internal components 

	- line
	- angle

	- algebraic structures: a group of operations having finite inputs on a set (the algebra refers to the set itself being operated on)

		- groups: 

			- group: 
				- set including a binary operation that combines any two elements to make a third element that satisfies:

			- closure (operation on a member of the set produces a member of the set
			- associativity: independence of order property
			- identity: identity element leaves any element unchanged when combined with it
			- invertibility: reversibility
			- abelian group: commutative group where applying the group operation to two group elements doesnt depend on order of operation
			- related concepts:
				- symmetry
			- a symmetry group: the set of operations that leave an object unchanged (operations that can be captured in a system/interface)
			
			- a lie group: 
				- a continuous group described by several real parameters that is a differentiable manifold, with smooth group operations
				- used for modeling continuous symmetry, like symmetry of rotating a sphere in three dimensions
				- originally used to model continuous symmetries of differential equations
				- a representation of a Lie group: a linear action of a Lie group on a vector space; a smooth homomorphism of the group into the group of invertible operators on the vector space
				- examples: 
					- orthogonal groups:
					- unitary groups:
				- lie algebra: a vector space with a non-associative operation called the lie bracket (an alternating bilinear map satisfying the jacobi order of operations identity)
			
			- finite group:
				- used in galois theory to model discrete symmetries of algebraic equations 

		- rings: 
			- ring: set including two binary operations generalizing addition & multiplication
			- rings are also abelian groups with an additional binary operation that is associative & distributive over the abelian group operation, & has an identity element
			- associative & distributive second binary operation
			- identity

		- fields: 
			- field: a set on which addition, subtraction, division, & multiplication are defined & these operations behave like the corresponding operations do in the fields of real & rational numbers
			field extension: relationship between fields such that the operations of a subfield are the operations of the extended field, retricted to the subfield
			examples: field of real numbers, rational numbers, complex numbers

		- lattice: 

	- categories: 
		- category: a collection of objects linked by arrows, having two basic properties: 
		- the ability to compose the arrows associatively
		- the existence of an identity arrow for each object
		- example: a simple example is the category of sets, whose objects are sets and whose arrows are functions 

	- series:

	- matrix:

	- lagrangian: 

    - quaternions: 
      - ratio of two vectors: https://en.wikipedia.org/wiki/Quaternion
      - quaternion number system is a associative, non-commutative division algebra over real numbers
     

## Functions

	- types:

		- injective function: one-to-one function

		- differential equation: a function linking a function & its rates of change
			- types: Ordinary/Partial, Linear/Non-linear, and Homogeneous/heterogeneous

		- polynomial:

		- homomorphism: a structure-preserving map between two algebraic structures of the same type

		- homeomorphism: a continuous function linking topological spaces that preserves the properties of each space & the inverse function is also continuous

			- continuous deformation arent always homeomorphisms (deforming a line into a point)
			- some homeomorphisms arent continuous deformations

		- immersion: a differentiable function between two differentiable manifolds whose derivative is injective (1-to-1)

	- specific functions:

		- derivative: power * coefficient * (variable ^ power - 1)
			- example: 
				- x^3 derivative is 3x ^ 2 = three squares, which is the minimum necessary to infer triangle & cube shapes as natural next steps 
					- despite the missing information of constants indicating cube position, and information about dimensional expansion & associated volume

			- partial derivative: change of y with respect to one of its determining variables, like y = 3x + 4z, a partial derivative dy/dz is change in y produced by change in z
				- the partial derivative is a good first step to isolating variable influence
				- however it leaves out other corrollaries between variables:
					- dy/ d(attribute that is specific to z)
					- dy/ d(attribute that x & z have in common)
					- dy/ d(attribute causing x and/or z)
					- dy/ d(alternate function compressing x & z efficiently)
					- dy/ d(metadata function describing x & z activities)
					- dy/ d(approximation function)
					- dy/ d(emergent variable w that x & z cause)
					- dy/ d(concept that x & z interact with, like equivalence in the vector space where equivalence vectors display different types of equivalence)
					- dy/ d(interface that x & z can be standardized to, like intent)
					- dy/ d(adjacent functions & transforming variables)
					- dy/ probability distribution of w that describes x and/or z when transformed to outputs in distribution with symmetric transform)
					- dy/ system structures that would leak variance in the shape of x & z
					- dy/ dimension trajectories/stacks that can lead to or connect x & z
					- dy/ limiting variables that can reduce potential for not-x and not-z
					- dy/ filters used to isolate variables
					- dy/ variables that would give the illusion of x & z at measured points
					- dy/ change or boundary rules of x & z

		- integral: 1/(power + 1) * coefficient * (variable ^ power + 1) to calculate metrics of higher dimensions (area under a curve)

			- this is another example of breaking the problem into a more solvable problem:
				- calculating area under a curve by breaking the curved area into a set of objects with more calculatable area (or area that can be added, like objects at unit limits such as integers)


	- intents:

		- decompositions/alternate forms
		- description methods/minimum of information
		- function conversion methods
		- proofs
			- rule of replacement (associativity/distributivity)


## Spaces

    - algebra: 

     	- vector space with a (bilinear) way to multiply two vectors in two vector spaces, like a set with a set of supported operations

	- hilbert space: 

		- generalization of euclidean space, extending vector algebra & calculus methods to infinite dimensions

	- affine space: 

		- a structure that generalizes euclidean space properties 

		- removes the concept of distance & angle measure but keeps the parallelism & ratio of lengths for parallel line segments
		- an affine space has no origin so no vector can be associated to a point
		- an affine space consists of displacement vectors, indicating translations to get from one point to another, & which can be added to a point
		- any vector space may be represented as an affine space

		- affine transformation: a function between affine spaces which preserves points, straight lines and planes

			- sets of parallel lines remain parallel after an affine transformation
			- an affine transformation does not necessarily preserve angles between lines or distances between points, 
			though it does preserve ratios of distances between points lying on a straight line

			- examples: translation, scaling, homothety, similarity transformation, reflection, rotation, shear mapping, and compositions of them in any combination & sequence

	- topological space: 

		- a set of points & neighborhoods for each point with axioms relating neighborhoods & points

		- sufficiently general to allow properties:

			- continuity
			- convergence
			- connectedness

		- examples of topological spaces:

			- metric space: a set & a metric function on the set (example: euclidean space where the metric is the distance of the straight line connecting two points)

	- manifold: 

		- an n-dimensional space where the locality of each point represents a homeomorphism euclidean space of dimension n 


- examine property map to number types, number fields, spaces, and sets

- encryption algorithms

	- attributes:
		- one computationally expensive operation (find prime or curve used to calculate a number, longer key sizes)
		- non-linear relationships

	- requirements:
		- confidentiality
		- authenticity

	- questions:
		- are the best encryption functions those with the fewest symmetries?

	- common core operations:
		- xor
		- substitution
		- affine map
		- permutation

	- concepts:
		- order
		- symmetry
		- random
		- substitution :: map
		- permutation :: combination
		- division :: group

	- attack types from wiki:
		- related key attack
		- known key distinguishing attack
		- key recovery attack
		- biclique attack
		- side channel attacks: attack on data leakage in software or hardware implementations
			cache-timing:
			differential fault analysis: introduce unexpected conditions to reveal internal states within an encryption implementation
		- linear cryptanalysis
		- differential cryptanalysis
		- truncated differential cryptanalysis
		- partial differential cryptanalysis
		- integral cryptanalysis, which encompasses square & integral attacks
		- slide attacks
		- boomerang attacks
		- XSL attack
		- impossible differential cryptanalysis
		- algebraic attacks
# Math terms

- dont forget to fit these:
	- ranking/adjacence
	- outliers


- map of set concepts to system analysis
	- markov chain: where the set of possible new states is determined by current state & change rules (how to move pieces) & system limits (number of open spaces)
	- singleton: unit set with one element
	- set: the list of unique object/nodes in a network
	- space: a network with operations
	- norm: a function that standardizes (so that vectors can be scaled & added) - may be an interface filtering function
	- neighborhood as a metric of adjacence/similarity/distance (how many steps away) if neighborhoods are determined by core functions
	- core points: vertices, not the same as nodes in a network, more like moments in a moment-generating function
	- core functions
		- basis: the set of core functions
		- identity function as the origin function to start from when applying distortions to get other functions
	- core combinations
		- base: the set of core subsets of a set X that can generate a topology on set X, or whose union can generate set X
	- the layers of possible sets of core functions form the interface network
	- generalization: removing differentiating attributes to navigate up an abstraction layer
	- kernel function: similarity function over pairs of data points in raw representation
		- "Any linear model can be turned into a non-linear model by applying the kernel trick to the model: replacing its features (predictors) by a kernel function"
		- "Most kernel algorithms are based on convex optimization or eigenproblems and are statistically well-founded. Typically, their statistical properties are analyzed using statistical learning theory (for example, using Rademacher complexity)"
		- https://en.wikipedia.org/wiki/Kernel_method
	- eigenvector/characteristic vector of a linear transformation: a nonzero vector that changes at most by a scalar factor when that linear transformation is applied to it, like the unit vector specific to a transform, where the eigenvalue is the standardization constant
	- eigenvalue of an eigenvector: the factor by which the eigenvector is scaled
	- eigenvector stack may be a useful framing object - the eigenvectors in multiple related spaces
	- the progression of these determining vectors (from likeliest/simplest/most efficient/most common determining vector configurations) may have useful patterns as well


- standard terms:

	- set: list of distinct objects (network of unique nodes)
	- space: a network of objects with defined functions linking them & operations that can be done on the objects - a set with some added structure 
	- norm: a function that assigns value to vectors in a space/set & allows for additivity & scalability
	- base: a collection of subsets of a space/set
	- basis: set of vectors that can be linearly combined to create any possible element in the vector space
	- neighborhood: neighborhood of a point is a set of points containing that point where movement is allowed without leaving the original point's set
	- algebraic variety: set of solutions to a system of polynomial equations
	- simplex: generalization of a triangle
	- manifold: topological space that resembles euclidean space near each point
	- identify function: always returns same value as its input
	- partially ordered set: a binary relation on X that assigns order to items in the set, though not all items need to be comparable
	- total order: a binary relation on X that is antisymmetric (comparison cant apply in reverse order), transitive (order is extendible), and connex (all items are comparable)
	- chain: set paired with a total order

	- questions:
		- check other number types for alternate solution paths to set of solutions that are more efficient than across real/complex numbers
		- check what differences are created when core functions start at different core points


- set theory of spaces:

	- topological spaces:
		- a set of points, along with a set of neighbourhoods for each point, satisfying a set of axioms relating points & neighbourhoods 

	- metric spaces

	- normed vector spaces: 
		- vector space where norm is defined

	- inner product spaces


- topological space:

	- a set of points, along with a set of neighbourhoods for each point, satisfying a set of axioms relating points & neighbourhoods - https://en.wikipedia.org/wiki/Topological_space
	
	- use cases:
		- can be used to display configurations (attribute value combinations of an object), or sets (vectors, networks, spaces, function sets) as a point

	- is the most general notion of a mathematical space that allows for the definition of concepts such as continuity, connectedness, and convergence
	- other spaces, such as manifolds & metric spaces, are specializations of topological spaces with extra structures or constraints
	- base (subset of elements) can be used to generate a topology on a set
	- weight of the topological space: smallest cardinality of a base is the 

	- questions:
		- what is the topology of spaces called?

	
	- topology examples:
		- metric topology: the topology generated by a collection of open balls
		- discrete topology has the singletons as a base
		- order topology: the topology generated by a collection of open-interval-like sets
	    - metric spaces
	    	- metric: a precise notion of distance between points
	    - proximity spaces
	    	- provide a notion of closeness of two sets
	    - uniform spaces
	    	- axiomatize ordering the distance between distinct points
	    - function spaces
	    	- a topological space in which the points are functions
	    - cauchy spaces
	    	- axiomatize the ability to test whether a net is Cauchy, for studying completions
	    - convergence spaces
	    	- capture some of the features of convergence of filters
	    - grothendieck sites
	    	- categories with extra data axiomatizing whether a family of arrows covers an object, for defining sheaves
	    - other spaces


## Group theory

  - structures to examine:

    - rings for interface network
    - algebras for vertices of a problem space

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
	- infinite
	- adjacency
	- cooperation (objects/types/attributes)
	- scale
	- discriminant: example of calculating properties of solution without calculating solution directly
		- can tell if solution sub-components (roots) are equal, signed, etc by calculating value of discriminant which is a function of polynomial coefficients
	- nilpotent

## Types

	- types are determined by sets of attributes (continuous, host system, reversibility, c  ombinability, measurability)

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

		- group: 

			- a set including a binary operation that combines any two elements to make a third element that satisfies:

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

		- ring: 
			- ring: set including two binary operations generalizing addition & multiplication
			- rings are also abelian groups with an additional binary operation that is associative & distributive over the abelian group operation, & has an identity element
			- associative & distributive second binary operation
			- identity

		- field: 
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
		- vector set
		- related matrices:
			- transpose
			- conjugate
			- identity
		- diagonal
		- determinant
		- inverse

		- find out method to determine adjacent matrix representations for a particular function, and use it in reverse to determine likely functions for a matrix
		- alternative methods of framing a matrix:
			- operator space: 
				- applying operations to vector sets within the vector set & examining the output metrics
				- example:
					- ratio space of a matrix includes the output of vector ratios for properties associated with ratios (like rate of change or similarity) that can be used to describe the vector set
			- path space:
				- applying path analysis to find paths across features in the matrix that reflect its properties
			- data space:
				- applying statistical analysis to vectors as variable values/data points

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
# Math terms


## Points/Questions

	- check other number types for alternate solution paths to set of solutions that are more efficient than across real/complex numbers
	- check what differences are created when core functions start at different core points
	- what is the topology of spaces called?
	- are the best encryption functions those with the fewest symmetries?
	- the layers of possible sets of core functions form the interface network
	- all accreted attribute sets can be collapsed to a point (type) and visualized on a graph to indicate difference between attribute sets, but which attribute set is most informative and should be used as a default base to start from when seeking more attributes (is there a spherical topology where the origin represents this default base attribute set)
	- with the example of an ideal: 
		- given subsets of the integer set having absorption & closure properties, they created an algebraic subtype to encapsulate these properties on that set
		- deriving functions to produce important emergent attributes/objects/rules (emergent attributes of an ideal), given subsets (even numbers) of a set (integers) having attributes (absorption, closure) using a trajectory across function/attribute/set topologies
		- real numbers
			- unit (integers)
				- multiples
					- subset of multiples of 2
						- absorption 				
						- closure
							- ideal
					- subset of multiples of 3
						- absorption 
						- closure
							- ideal
		- the progression from real numbers, to the ideal object, to the attributes/rules of the ideal objects on the attribute/rule topology (jacobson radical) & distance to ring & set object attribute sets, should be describable
		- is attribute or rule interface better when condensing objects for comparison
		- if a sphere is symmetric with respect to the origin when rotated around an axis, that means its exact previous state cant be derived once its rotation position is measured, but the previous state space can
			- measuring the output of a symmetric transform cannot reveal specific information about original position (reduce solution space of possible original positions)
			- the output of symmetric transforms (spin, momentum) might disrupt other systems (adjacent objects to sphere), so to reveal information about a symmetric transform history on an object to derive original position, youd need to position that object next to objects that would respond to the output of that symmetric transform, or in spaces where its output would have an impact on objects that could respond as needed
			- the set of adjacent objects & spaces where the symmetric transform output could be used to derive original position can be used as a parameter to obfuscate the original position (algorithm uses different element in the set each time)
	- interface analysis translates geometry & algebra to interface layer objects


## Spaces as attribute generators

	- euclidean space example

		- core inputs
			- position
			- angle

		- core functions
			- in Euclidean space, the core functions operate on the position attribute:
				- shifting (1-d position transform)
				- rotating (2-d position transform)
				- shift & rotate (3-d position transform)

		- definition of equivalence:
			- "if one object can be transformed into the other by some sequence of translations, rotations & reflections, theyre considered equivalent"
			- the definition of equivalence can be framed in terms of the core functions

		- system analysis:

			- how would you derive/reduce the likely/possible emergent attributes of euclidean space given this metadata?
				- identify the possible change types
				- identify which parameters explain change within these change types (position, angle)
				- identify the core functions, given the sequence of dimension numbers (0,1,2,3 in 3-d space) & the change types possible on each dimension or combination of dimensions

			- extension:

				- what is the operation associated with:
					- dimension reduction

				- what is the extreme version of combined attributes/functions?
					- a dimension resulting from 0th dimension with the dimension reduction operation applied (-1th dimension, etc)

				- what is the concept associated with:

					- angle: anchored difference
					- position: unanchored difference

					- both are measures of equivalence

					- angle measures difference in direction starting from same origin

					- what type of object measures difference in equivalence?

						- is there an "angle" object between anchored (position-dependent) & unanchored (position-independent) difference measures?

						- in what space can you frame anchored differences (angles) and unanchored differences (positions) as dimensions so the angle between them reflects their relationships?

			- as you can see the metadata of each space can be calculated from its definition, as can the extensions of that space


## Map of set concepts to system analysis

	- vector: intersection of attributes value & direction
		- vectors are a useful structure to store intents, ordered lists of objects having a common attribute, & variable value sets
	- unit: lower-dimensional composable threshold for differentiation, syncing, & aggregation of filters (has overlap with interface)
	- map: set of possible transform networks connecting two sets
	- value: position (relative difference)
	- boundary: stabilized outer range of combinations produceable with internal components 
	- norm: a function that standardizes (so that vectors can be scaled & added) - may be an interface filtering function
		- a function that assigns value to vectors in a space/set & allows for additivity & scalability
	- neighborhood as a metric of adjacence/similarity/distance (how many steps away) if neighborhoods are determined by core functions
	- core points: vertices, not the same as nodes in a network, more like moments in a moment-generating function
	- core functions
		- basis: the set of core functions
		- identity function as the origin function to start from when applying distortions to get other functions
	- core combinations
		- base: the set of core subsets of a set X that can generate a topology on set X, or whose union can generate set X
	- generalization: removing differentiating attributes to navigate up an abstraction layer


## Standard terms

## Stats

    - bias error (missing features) is from erroneous assumptions in the learning algorithm
    	- high bias can cause an algorithm to miss the relevant relations between features & target outputs (underfitting)

    - variance error (doesnt generalize well) is from sensitivity to small fluctuations in the training set
    	- high variance can cause an algorithm to model the random noise in the training data, rather than the intended outputs (overfitting)


## Set/category theory

	- geometry: study of structure
	- algebra: study of mathematical relationships
	- Hilbert's Nullstellensatz: establishes link between geometry & algebra, forming the basis of algebraic geometry, specifically relating algebraic sets to ideals in polynomial rings over algebraically closed fields

	- representation theory
		- represents elements of algebraic structures as linear transformations of vector spaces & studies modules over these abstract algebraic structures
		- a representation makes an abstract algebraic object more concrete by describing its elements by matrices & its algebraic operations (for example, matrix addition, matrix multiplication)
		- reduces problems in abstract algebra to problems in linear algebra

	- representation space: executing linear transforms on vector spaces to represent algebraic structure elements

	- vector:

	- spinor:
		- elements of a complex vector space that can be associated with Euclidean space
		- like geometric vectors & tensors, spinors transform linearly when the Euclidean space is subjected to an incremental rotation
		- when a sequence of such small rotations is composed to form a final rotation, the resulting spinor transformation depends on which sequence of small rotations was used
		- unlike vectors and tensors, a spinor transforms to its negative when the space is continuously rotated through a complete turn from 0° to 360° 
		- spinors can be viewed as the "square roots" of vectors
		- lends an attribute of adjacence to otherwise opposing values, crystallizing the concept of a shortcut (a metadata hack) to an operation
	
	- set: collection of distinct objects

	- space: a network of objects with defined functions linking them & operations that can be done on the objects - a set with some added structure 

		- each interface can be framed as a space, having its own operations as well as a set of core cross-interface operations
		- finding the right space to frame a problem in can start with euclidean space
		- examine the progression of spaces in the evolution of systems for patterns

		- space set:
			- topological space
			- metric space
			- normed vector space
			- inner product space

		- types:

			- topological space: a set of points, along with a set of neighbourhoods for each point, satisfying a set of axioms relating points & neighbourhoods - https://en.wikipedia.org/wiki/Topological_space

				- is the most general notion of a mathematical space that allows for the definition of concepts such as continuity, connectedness, and convergence
				- other spaces, such as manifolds & metric spaces, are specializations of topological spaces with extra structures or constraints
				- base (subset of elements) can be used to generate a topology on a set
				- weight of the topological space: smallest cardinality of a base

				- use cases:
					- used to display configurations (attribute value combinations of an object), or sets (vectors, networks, spaces, function sets) as a point
				
				- topology types:
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

			- metric spaces
			- normed vector spaces: vector space where norm is defined
			- inner product spaces
			- hilbert space: generalization of euclidean space, extending vector algebra & calculus methods to infinite dimensions
			- affine space: a structure that removes the concept of distance & angle measure, but keeps the parallelism & ratio of lengths for parallel line segments
				- generalizes euclidean space properties
				- an affine space has no origin so no vector can be associated to a point
				- an affine space consists of displacement vectors, indicating translations to get from one point to another, & which can be added to a point
				- any vector space may be represented as an affine space

	- base: a collection of subsets of a space/set
	- span: the span of two vectors is the range of their scaled addition = linear combination of vectors
		- if one vector is linearly dependent on the other (can be produced as a linear combination of the others), it's redundant & doesnt add to the span
	- basis of a space: set of linearly independent vectors which spans the space (can be linearly combined to create any possible element in the vector space)
		- basis vectors i-hat & j-hat are unit vectors of two dimensions x & y, where column 1 = coordinates where i-hat lands, & column 2 = coordinates where j-hat lands
	- discriminant: example of calculating properties of solution without calculating solution directly
		- can tell if solution sub-components (roots) are equal, signed, etc by calculating value of discriminant which is a function of polynomial coefficients
	- neighborhood: a neighborhood of a point is a set of points containing that point where movement is allowed without leaving the original point's set
	- algebraic variety: set of solutions to a system of polynomial equations
	- partially ordered set: a binary relation on X that assigns order to items in the set, though not all items need to be comparable
	- total order: a binary relation on X that is antisymmetric (comparison cant apply in reverse order), transitive (order is extendible), and connex (all items are comparable)
	- chain: set paired with a total order
	- markov chain: where the set of possible new states is determined by current state & change rules (how to move pieces) & system limits (number of open spaces)
	- differential: change in y due to incremental change in x
	- degrees of freedom: 
		- a single scalar numerical independent parameter indicating the dimensions of a system's phase space (the set of all possible system states)
		- standard movement in 3d space requires 3 position params & 3 velocity params describing speed & direction 
	- jacobian:
		- jacobi identity: operation order impact of binary operations
	- lagrangian: 
		- Lagrangian density: a scalar can be constructed from a field tensor φ and its derivatives
			- evaluate the derivative of the Lagrangian density with respect to the field components & and the derivatives of the field components
		- from this density, the action functional can be constructed by integrating over spacetime, where -g ^ 1/2 is viewed as the 'jacobian' in curved spacetime: integral of Lagrangian density * jacobian d4x
		- lagrangian: the integral of the Lagrangian density over all space
	- hamiltonian: 
		- physics quantity describing total energy of a system (sum of potential/kinetic energy of particles in system) - collapsing one set of variables to another
		- Hamiltonian mechanics aims to replace the generalized velocity variables with generalized momentum variables, also known as conjugate momenta
	- fourier transform
	- functional: a linear mapping from a vector space V into its field of scalars - an element of the dual space which is created by mapping the vector space with transforms to the scalar field
    - quaternions: 
      - ratio of two vectors: https://en.wikipedia.org/wiki/Quaternion
      - quaternion number system is a associative, non-commutative division algebra over real numbers    
	- singleton: unit set with one element

	- algebraic object metadata:
		- a representation of a group: where elements of a group are represented by invertible matrices in such a way that the group operation is matrix multiplication
			- a representation of a lie group: a linear action of a lie group on a vector space; a smooth homomorphism of the group into the group of invertible operators on the vector space
		- presentation of a group: comprises a set S of generators—so that every element of the group can be written as a product of powers of some of these generators—and a set R of relations among those generators
		- field extension: relationship between fields such that the operations of a subfield are the operations of the extended field, retricted to the subfield

	- algebraic structures: a group of operations having finite inputs on a set (the algebra refers to the set itself being operated on) - includes groups, rings, fields, lattices	
	
	- homomorphism: a structure-preserving map between two algebraic structures of the same type
	- endomorphism: a map of a mathematical object to itself		
	
	- category: a collection of objects linked by arrows, having two basic properties: 
		- the ability to compose the arrows associatively
		- the existence of an identity arrow for each object
		- example: a simple example is the category of sets, whose objects are sets and whose arrows are functions 
	
	- series:
	- progression:

	- lattice: a partially ordered set in which every two elements have a unique supremum (a least upper bound or join) and a unique infimum (a greatest lower bound or meet)
		- example: the natural numbers, partially ordered by divisibility, for which the unique supremum is the least common multiple and the unique infimum is the greatest common divisor
		- least common multiple: smallest positive integer divisible by a & b
		- greatest common divisor: largest positive integer that can be multiplied to generate a & b
	
	- tensor: an algebraic object describing a multilinear relationship between algebraic object sets on a vector space
		- defined independently of any basis
		- tensors may map between objects like vectors, scalars, & recursively other tensors
		- tensors can take several different forms:
			- scalars and vectors (which are the simplest tensors)
			- dual vectors
			- multi-linear maps between vector spaces
			- some operations such as the dot product
	- monoid: algebraic structure with a single associative operation and a identity element
	- domain: set of inputs for which a function is defined (the function produces an output for each element in the domain)
	- partial function: where every possible x is not forced to map to a value of y
	- codomain: set limiting the outputs of a function 
	- binary operation: a calculation that combines two elements to produce another element
		- an operation of arity (input number) two
		- binary operation on a set: a binary operation whose two domains and the codomain are the same set
			- examples: addition, subtraction, multiplication, vector addition, matrix multiplication and conjugation in groups
		- may involve several sets:
			- scalar multiplication of vector spaces takes a scalar & a vector to produce a vector
			- a scalar product takes two vectors to produce a scalar 
	- simplex: generalization of a triangle
	- manifold: topological space that resembles euclidean space near each point
	- bilinear map: function combining elements of two vector spaces to produce a vector in a third vector space, where each argument in linear
		- example: matrix multiplication

	- directed graph: a graph with vertices/nodes & edges (ordered pairs) having direction
	- transpose graph: a directed graph with its edges reversed
	- skew-symmetric graph: a directed graph that is isomorphic to its transpose graph, over an isomorphism that is an involution without fixed points
	- involution: function that is its own inverse
    - algebra (over a field): a vector space with a bilinear product to multiply two vectors in two vector spaces
    	- a set with operations of multiplication, addition, & scalar multiplication by elements of the field
    	- satisfies the axioms of a vector space and bilinearity of the product
    	- types:
    		- lie algebra: a vector space with a non-associative operation (the lie bracket)
			- poisson algebra: associative algebra & a lie bracket that satisfies liebniz's law, formed by the tensor algebra of a Lie algebra

	- group: a set including a binary operation that combines any two elements to make a third element that satisfies closure, associativity, identity, reversibility
		- types:
			- abelian group: commutative group where applying the group operation to two group elements doesnt depend on order of operation
			- a symmetry group: the set of operations that leave an object unchanged (operations that can be captured in a system/interface)
			- a lie group: a continuous group described by several real parameters that is a differentiable (smooth) manifold, with smooth group operations
				- used for modeling continuous symmetry, like symmetry of rotating a sphere in three dimensions, & for modeling continuous symmetries of differential equations
				- types:
					- orthogonal groups:
					- unitary groups:
			- finite group: used in galois theory to model discrete symmetries of algebraic equations 
			- module (over a ring): 
				- an additive abelian group (like a vector space)
				- a product is defined between elements of the ring & the module that is distributive over each parameter's addition operation & is compatible with the ring multiplication
				- generalization of a vector space over a field
				- the corresponding scalars are the elements of a ring with identity & a multiplication is defined between elements of the ring & the module
				- R-module: a module taking its scalars from a ring R

	- bracket:

		- lie bracket: an alternating bilinear map satisfying the jacobi operation order identity
		- Poisson bracket: a binary operation that distinguishes a certain class of coordinate transformations (canonical transformations, which map canonical coordinate systems into canonical coordinate systems)
			- canonical coordinate system: canonical position & momentum variables that satisfy canonical Poisson bracket relations

	- liebniz's law: cannot be separate objects or entities that have all their properties in common

	- ring: set (and an abelian group with commutativity) including two binary operations generalizing addition & multiplication, with an identity element
		- rings have an additional binary operation that is associative & distributive over the abelian group operation

		- ideal: subset of a ring with closure & absorption attributes, generalizing certain subsets of the integers like multiples of 2 or 3
			- absorption: addition & subtraction of even numbers preserves evenness
			- closure: multiplying an even number by any other integer produces another even number

	- field: a set on which addition, subtraction, division, & multiplication are defined & these operations behave like the corresponding operations do in the fields of real & rational numbers
		- examples: field of real numbers, rational numbers, complex numbers
		- physics: a physical quantity, represented by a number or tensor, that has a value for each point in space-time
		- field theory: mathematical descriptions of how field values change in space & time or other independent variables

	- affine transformation: a function between affine spaces which preserves points, straight lines and planes
		- sets of parallel lines remain parallel after an affine transformation
		- an affine transformation does not necessarily preserve angles between lines or distances between points, though it does preserve ratios of distances between points lying on a straight line
		- examples: translation, scaling, homothety, similarity transformation, reflection, rotation, shear mapping, and compositions of them in any combination & sequence
	
	- matrix:
		- transformations keep lines parallel and evenly spaced, and origin is fixed
		- matrix multiplication is applying two transformations, starting from the right side
		- adjacent structures:
			- vector set
				- function set
				- data set
			- topology
		- related matrices:
			- transpose
			- conjugate
			- identity
			- orthogonal
		- determinant: volume of parallelipiped space created by the vectors
	- kernel function: similarity function over pairs of data points in raw representation
		- "Any linear model can be turned into a non-linear model by applying the kernel trick to the model: replacing its features (predictors) by a kernel function"
		- "Most kernel algorithms are based on convex optimization or eigenproblems" - https://en.wikipedia.org/wiki/Kernel_method
	- eigenvector/characteristic vector of a linear transformation: 
		- a nonzero vector that changes at most by a scalar factor when that linear transformation is applied to it, like the unit vector specific to a transform, where the eigenvalue is the standardization constant
		- eigenvector stack may be a useful framing object - the eigenvectors in multiple related spaces
		- the progression of these determining vectors (from likeliest/simplest/most efficient/most common determining vector configurations) may have useful patterns as well
	- eigenvalue of an eigenvector: the factor by which the eigenvector is scaled
	- probability:
		- moment generating function
		- expected value
		- cdf/pdf
		- marginal density
		- conditional density
		- joint probability distribution
		- conditional probability: probability, given a starting point/filter


## Attributes

	- angle: direction
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
	- nilpotent
	- ranking
	- closure: operation on a member of the set produces a member of the set
	- associativity: independence of order property
	- identity: identity element leaves any element unchanged when combined with it
	- invertibility: reversibility
	- note that T is a function of p alone, while V is a function of q alone (i.e., T and V are scleronomic)

## Types

	- types are determined by sets of attributes (continuous, host system, reversibility, c  ombinability, measurability)
	- number types
	- data types
	- variable types
	- outliers

	
## Functions

	- types:
		- differential equation: a function linking a function & its rates of change
			- types: 
				- ordinary/partial
				- linear/non-linear
				- homogeneous/heterogeneous
		- polynomial:
		- homeomorphism: a continuous function linking topological spaces that preserves the properties of each space & the inverse function is also continuous
			- continuous deformation arent always homeomorphisms (deforming a line into a point)
			- some homeomorphisms arent continuous deformations

	- specific functions:

		- immersion: a differentiable function between two differentiable manifolds whose derivative is injective (1-to-1)

		- injective function: one-to-one function

		- identify function: always returns same value as its input

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


- encryption algorithms

	- attributes:
		- one computationally expensive operation (find prime or curve used to calculate a number, longer key sizes)
		- non-linear relationships

	- requirements:
		- confidentiality
		- authenticity

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
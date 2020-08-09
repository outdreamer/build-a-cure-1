This article is a great example of automating math proofs

1. query for a useful structure given assumptions (usually a network or matrix to explore relationships en masse, with other rules given relevant restrictions like efficient representation of info)
https://www.quantamagazine.org/mathematician-solves-computer-science-conjecture-in-two-pages-20190725/

Ex: for this problem, assumptions include:
- points must represent unique combinations of bits
- points one unit away must represent one-unit differences
- for a boolean of n bits/dimensions, there are 2 ^ (n) corners possible, since there are 2 possible values for each bit

These assumptions point to a square for a boolean of 2 bits, a cube for a boolean of 3 bits, etc (as in the article)

So you can query for a structure given these assumptions and a program should direct you to a n-dimensional cube as the most efficient representation of this info

2. look for extreme values of metrics intrinsically tied to the structure 

Ex: largest # of connections to similar nodes, or a hub node in a network
hub: a combination of connections
connections: a core unit in the structure
combination: a core function applied to that unit type

3. format the extreme metric values in a way that collects & isolates the relevant data (matrix of start & end points of a network connection) & measures its variation (eigenvalues)

4. distort the values w/ commonly successful operations (multiply by -1, switch the color, halve)

The question framing may contain hints to its solution: 'after switching the value (an operation which maps to "multiplying by -1 to get the opposite") of more than half of the dots, is there definitely a red hub?'

As Huang derived, half ends up being the exponent to raise the number of dimensions to, in order to get the relevant root - the use of 'half' in the assumptions may not be significant but is mirrored by the power of 2 generating the number of corners in the n-dimensional cubes

These possible interactions in the problem space (like the multiple appearances of a certain number (2) in the structure used to frame the problem, and the math function for the switch operation given a definition of 'opposite') are all derivable given the initial requirements

5. check for alternate ways of relating two significant objects (matrix & eigenvalues)

6. check for value relationships with commonly successful operations (multiply the value by itself, etc)

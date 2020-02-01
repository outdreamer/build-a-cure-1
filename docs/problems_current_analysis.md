# Problems with Current Analysis

## Statistics

### Evaluating variables in isolation

- the variable interactions usually studied aren't normally indexed by causal metadata like causal adjacency (direct vs. indirect cause) or causal shape

- same problem as making risk assessment in isolation & evaluating transactions in isolation
	- the risk presented to an insurer is not calculatable from metadata of the insured but from the system the insured exists in
	- the risk in a transaction is calculatable using financial system metadata

- causal shape analysis is crucial for:
	- identifying variables that can be collapsed into other variables
	- which variables that can be replaced with others
	- if there are likely sets of variables that influence the target variable
	- if a variable is an end leaf rather than a causal branch variable
	- if variation is about to converge or expand
	- if variation is concentrated in a sub-system (trade loop) that is largely independent from the host system and can be ignored in many cases

### Checking variables for predictive power instead of predicting variable metadata & sets first

- system metadata should have a minimum of information that can enable identifying probable variable sets

- then predictive functions should be quicker to build, because the solution space is drastically reduced by the system analysis identifying probable variable sets

- first create an interface where the filters allow multiple variable sets & metadata, then once you narrow down which variable sets/metadata are possible, narrow it down by likelihood given system config

- example of how variables are examined almost at the level of trial & error, when predicting the likely sets of variable sets would drastically reduce computation requirements
  https://phys.org/news/2020-01-simple-sequence.html
	

### Treating non-random processes as random

	- rather than deriving core functions and observing the trajectory of variance from core functions to combinations of them & other normal system rules like variance accretion patterns, they assume each variable is so unrelated to other variables or so impacted by many other variables that it's random, when system analysis would identify it as a clear combination of system functions, gaps, filters, & other components

	- the trajectory of heat through a system is predictable like the trajectory of variance through a system is predictable
	- https://phys.org/news/2020-01-supercomputers-link-quantum-entanglement-cold.html
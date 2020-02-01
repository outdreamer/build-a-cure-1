# Problems with Current Analysis

## Statistics

### Evaluating variables in isolation

- the variable interactions usually studied aren't normally indexed by causal metadata like causal adjacency (direct vs. indirect cause) or causal shape

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

- example of how variables are examined almost at the level of trial & error, when predicting the likely sets of variable sets would drastically reduce computation requirements
  https://phys.org/news/2020-01-simple-sequence.html
	
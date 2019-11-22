# System Analysis

How to decide which layer to choose core functions at?
- the lowest layer is mathematical, directly operating on numerical values (add, multiply, etc)
- then above that you have functions (composed of those lower math operations) having successively emerging intents, starting with functions that are system agnostic & apply to all systems (find, combine, merge, build, etc)
- above that, youll have a layer of functions composed of lower operations that apply exclusively to the relevant system you used to derive the core functions (for a biosystem, functions like "borrow a gene", "learn an attacker profile", "send signal")

# System Analysis applications

System analysis should be able to answer questions like:
- what is a way to reduce computation time in a ml model?
With answers like:
- compressing features along mathematical symmetries of object behavior

Or questions like:
- how do you find the likely relevant causes of a process in a system?
With answers like:
- scan the relevant properties & rules of interacting objects, where relevance has various definitions (distance, adjacency, similarity)

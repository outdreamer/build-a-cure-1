# Knapsack problem or route optimization as an example

    "Given a list of 1 million museum artifacts with their weights and monetary values, and a backpack limited to 25 pounds, a computer would have to run through every possible combination to generate the single one with the most lucrative haul. A computer must also figure out whether any given number can be written as the sum of a subset of numbers in the private key, which becomes an easy knapsack problem. It’s akin to filling a backpack with a batch of such differently sized items — like a ring, a painting, a car and a house — and knowing you can’t stuff in anything else after you’ve checked that the ring and the painting fit."

    “NP” problems, which stands for “nondeterministic polynomial time.” The name references how these problems force a computer to go through many steps to arrive at a solution, and the number increases dramatically based on the size of the inputs

    NP problems also have solutions that are easy to verify (it would be trivial to check that a particular list of items does, in fact, fit in a backpack).

    https://www.smithsonianmag.com/science-nature/why-knapsack-problem-all-around-us-180974333/?utm_source=pocket-newtab


## Example of a solution using prior knowledge & inference:

    1. Given that these are objects in a museum, we can infer that:
      - these objects are unique & distinct from each other
      - these objects are rare
      - these objects are valuable
      - these objects are manmade
      - these objects vary in many possible attributes, including:
        - time
        - shape/size/quality
        - cultural history (position in a particular culture, like a military artifact or book)
        - cultural significance (a story attached to it, a path through powerful owners, etc)
        - reason for the object's value (the book is particular insightful, the military artifact was used to slaughter many or important people, etc)
        - mysteries around the object (the object may be so old that its impossible to know who made it, its purpose for the position it was found in or its usage is unknown, etc)

      - certain subsets of these attributes would only produce value in certain conditions
        - for example, the attribute of symmetry is only valuable in a gemstone if it's natural rather than made in a lab
        - gemstones can be valuable for other attribute values, such as occupying a particular path or having an emergent quality from rare attributes that aren't often found together, are likely to be measured & noticed by people, and sync with other systems so people attach cultural meaning to the attribute, such as a gemstone that looks like a particular leader (which wouldnt be inherently valuable in other objects but in the context of a gemstone, that combination of attributes would be particularly valuable)

      - there are different types of value (something that can be resold vs. something that has cultural significance & must be preserved)

    2. Given that these objects are of interest & value to people, we can infer that they have certain attributes that people gravitate to:
      - shiny/rare/other physical attributes with value attached
      - mysterious/historically significant/other cultural attributes with value attached
      - complex/symmetric/other abstract attributes with value attached

      This would be useful if we had to generate the set of objects that is likely to be preserved in a museum given only minimal info about what people value and insights like that objects of interest are likely to be significant (representing a cultural story or reason for development in culture like how religious anti-science movements caused the renaissance, or a first appearance of an insight like Davinci's drawings)

      You can infer from these insights that the objects likely to be in the museum are objects that caused, signified, or solved problems, which are also rare, or alternatively, valuable in their own right like gems.

      We don't have to generate this list for this problem but this is an interesting point if you did need to predict the object types & variance of the objects likely to be in a museum.

    3. Given the above, you can infer that some objects will have more value than others and you can start by assembling the full set of those objects to see if it will fit (assuming you know their positions in the list, as this isn't a data structure traversal problem).

      - you know that a gemstone with a historical & cultural significance & rare physical properties will be more valuable than a common stone with historical & cultural significance, unless the common stone has extreme/rare attributes - but the gemstone is likelier to be more valuable using the base of size, which is a key metric, as they're likelier to be smaller.

      - the ways that the other objects deviate in value from the base of the most valuable calculatable objects, that are bigger than gemstones & slightly less valuable but still worth examining, in case all the gemstones can't fill the bag, can be calculated in a similar way, using inference from prior knowledge.


## Example of a solution using problem space analysis:

  - identify & describe the core metric to optimize (value) on various interfaces:

    - structure:

      - valuable subsets (objects that are more valuable when combined)

      - valuable matches of subsets (objects that fit with other subsets/objects in the bag shape)

        - is there a network or other structure (using objects likely to exist outside the museum) that when completed would have increasing value 

      - value limits (attributes that cause or enforce limits in value)

    - function:

      - what core functions cause changes in value

      - can you arrange objects in sets/sequences to create those changes in value (if you keep a weapon & a gem with certain aligning attributes, which is likelier to attract story-based life forms who purchase or steal it, their value is likely to increase as they are used in another story)

    - type:

      - valuable types (objects with high-value because of their type)

    - change:
    
      - value change rules (objects that are likely to become more valuable over time)
      - rules of imminent value decreases (objects that condemn existing or aligned groups are likely to be destroyed)

    - variance:

      - variance cascades (objects with enough mystery & value to be claimed as property of many entities is likely to increase in value as the fight for ownership continues)

    - attributes:

      - vertex attributes determining pivots in value (attributes like culture/history allow extreme changes in value)
      - phase shift attribute sets (sets of attributes that determine phase shifts in value)

    - problem:

      - conflicting attribute sets/pairs that neutralize each other's value

    - pattern:

      - what pattern of combinations of object values/weights created the most valuable sets in other cases 

    - cause:

      - causal direction:

        - what type of object is likely to have a certain weight, given the monetary value - or what type of object is likely to have a certain value, given the weight

      - reversing the limits as a cause (so instead we're causing the limits):

        - what distortions can be made to the container so that its contents can be optimized (can you fill it by stretching so that the filled shape is more circular, allowing more objects of shapes cooperative with circular objects, or is it maximized in its standard filled shape, so objects can fill its corners)

        - what force can the object exert on the container (can an object distort the container in any way, influencing its boundaries/size/shape)

      - tradeoffs

        - which tradeoffs (in the target metric, value) occur at which intersections of which attribute sets?

          - when a high-value, low-size object interacts with a higher-value, larger-size object (of proportional increase on both attributes), what does the trade-off space look like in various states of the knapsack being filled?

            - for example, if the smaller object is worth 5 points and the slightly larger object is worth 10 points (and the weights are proportional), then adding the smaller object may be better, unless adding the smaller object would prevent adding other objects to make up for the difference in value, because the smaller object has a shape that is likely to prevent other objects from being added (has too many corners or takes up space despite being smaller weight)

            - on the other hand, the larger object would normally not be higher value, because it would inherently prevent smaller objects from being added, so the larger object would inherently be less optimal unless there was a shape distortion that meant the larger object would fit in the remaining space whereas the smaller object wouldnt

        - these trade-offs are important to identify up front so they can be used as a filtering rule


  - interface query of most valuable objects (what combination & path between interfaces produces most valuable objects, other than already known valuable objects like gems, weapons, stories, mysteries, markets/inflation value increases)

- this may seem like the solution is specific to manmade objects, but numbers can be evaluated on the interface network as well
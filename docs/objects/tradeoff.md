# Dichotomy

  - definition: mutually exclusive options or at opposite ends of a spectrum where one has to be chosen at the cost of the other
  
  - some structures are clear tradeoffs/dichotomies, and other structures seem like clear dis/advantages

  - everything can be used for malicious intents, but some structures are more exploitable than others, when there's a gap between logic & intent

  - example of false tradeoff:

    - features as exploits & vice versa

      - in an online marketplace, allowing businesses to change price for a particular customer allows them to give preferential pricing based on relationship with that customer, but these relationships can provide an exploit, if businessperson is the powerless one in the relationship (being extorted for bribes from a gang), so that price-changing option can be used to get preferential pricing
      
      - if site didn't allow price changes, that would protect the business owner to a small degree but would prevent the preferential pricing option to build/maintain relationships

    - what determines classification as a benefit (feature) or a cost (exploit opportunity) can be degrees of distortions/transforms

      - how many steps/requirements and integrations with other exploits are necessary before something is converted into an exploit

    - many tradeoffs are false dichotomies because:

      - when either side is a type class, both types can often apply at the same time
      - when either side is a decision (as in a decision tree), one decision path may converge to the other decision path
      - either path may produce attributes that seem similar enough to be indistinguishable from the other
    
    - within the bias (underfitting due to inflexible algorithm assumptions that miss features) vs. variance (overfitting to an inflexible data set) trade-off

      - https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff
        
      - being adaptable to variance may be a form of bias, in that it may be unnecessary variance that should be hardcoded and is just creating problems by remaining variable
      - the opposite is also true, bias towards adaptability may be a form of variance, if the bias produces random change
      - bias doesnt inherently contradict variance as the definitions imply
      - in the stat example:
        - bias from assumptions may only miss features that are in flux & being phased out, so they dont produce error by the time it gets pushed to production
        - there may be noise along the accurate prediction function
        - the data set may be an average sample, so overfitting it doesnt produce error

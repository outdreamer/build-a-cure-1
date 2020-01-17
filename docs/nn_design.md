## Standard Neural Network Design for initial complex problem factor identification reduction
  
  - given that neural networks apply "apply, aggregate, & filter" functions to sort causative information into a standard shape like a tensor or vector set 
    (representing function variables generating an output variable)

    to identify sources of causation (like feature position or feature shape),
    
    how can neural network structure & algorithms be designed to generate a network & algorithm that is likeliest to be able to identify causative factors in the largest range of problem types?

  - there is an optimal network structure & algorithm that can handle the derivation of most causation shapes, since features aggregate in sets that have patterns between input features & output sets

  - the goal of optimizing neural network use is to identify the prediction function from as little data as possible

  - once you can identify an accurate prediction function using one data point (so its robust to changes in causation), the field of machine learning would be invalid

  - in order to do this, you need to identify:
      - candidate variables (cant verify which are actual variables without more data points)
      - variance patterns in the data point (one candidate variable leading to other candidate variables with net impact on overall variance)
      - causation shapes related to those variance patterns (causal loop, causal vector, causal network, etc)
      - priorities (structural priorities like aggregate, distribute, balance - functional priorities like align incentives, produce variance, optimize - conceptual priorities like change)
      - patterns, structures, generative functions, etc - all derivable objects on all interface layers
    - or any subset of these which can explain the complexity of the data point

  - given the profile of these derived interface objects, you can design a neural network that can identify:
    - the minimum information of future data points necessary to accurately categorize a new data point as belonging to the class of the training data point
    - the change patterns objects of this class are likely to display

  - so a neural network that can identify any prediction function takes these interface object derivation functions as input, and if they are above a threshold, 
    integrates them into a final decision of class & other metrics like 
      - change patterns
      - minimum information
      - optimal network design for this complexity level (which will probably involve fewer calculations than the 
        original classification calculation because not all information from derived interface objects 
        provided enough variance compression to be included in the final classification)

  - given that existing networks identify feature contribution, using metrics like feature position, 
    more accuracy in generating prediction functions can be added without extra computation using other interface object metrics like:
      - feature type
      - feature variance
      - feature priority
      - feature distortion
      - feature uniqueness
      - feature causation shapes
      - feature change patterns

  - this means a set of networks evaluating the contributions to final classification for a given complexity level or other system metric made by:
    - causal shape
    - change patterns
    - type stack
    - conceptual query

  - can produce answers to questions like:
    - which interface object combinations can be used to generate an accurate prediction function?
    - which interface object combinations map to which prediction functions?
    - which interface object prediction-function generating networks should be used first on a problem, 
      given that interface layer's higher independence/causation/variance-generation?
    - which problem types (conflict, alignment, asymmetry, lack) map to which interface objects?

  - so instead of doing problem-solving operations like:
    - get data
    - apply standard DNN or neural network structure designed by auto ML
    - use prediction function until no longer valid

  - you can run problem-solving automation operations like:
    - get data point
    - apply interface object derivation function
    - check if problem is solved
    - if not, apply interface-based neural network design function to generate optimal neural network for this problem until problem is solved, 
      at which point, store this interface object combination in index of solved problems
      and to make each new prediction, first apply interface object derivation function to each data point to format it 
      in ways that the neural network trained to identify contribution of interface objects to final classification can interpret
    - if problem changes:
      - generate new prediction function, according to previously identified change patterns of derived interface objects if they exist
      - re-apply whole process to generate the new prediction function or a neural network architecture to generate the new prediction function

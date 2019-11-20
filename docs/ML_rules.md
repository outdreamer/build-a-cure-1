ML rules

# Basic Machine Learning Terms

## Standard neural net explanation
  - training involves the assignment of weights to each node; after training, predictions can be made
  - the input data is multiplied by a weight in each node
  - if the weight * input value is more than the activation threshold, its passed on to the next layer as important info, otherwise, nothing is passed on
  - if the set of multiplied values that made it to the output layer indicates a certain category, that category is output

## Synonyms & quick terms:
  - estimator: tree
  - model: prediction function
  - feature: weight/parameter value, represented as a number in a matrix
  - filter: a matrix of feature weight values
  - activation map: resulting matrix from applying a filter

## Neural Net Terms:
  - input matrix
    - (w x h x d) input value matrix

  - filter
    - (w x h x d) weight value matrix
    - same depth as the input matrix (w x h x d)

  - weights
    - number used to signal the value being sought (higher weight for value being sought)

  - activation map
    - set of values created by multiplying filter matrix by input matrix & summing the multiplied input & weight values
    - this map is a matrix of x x y x 1 dimensions, unless you apply additional filters (weight matrixes), such as w x h x (d > 1)
    - using more filters allows you to preserve the original dimensions of the input better

  - layer output
    - the first filter applied to the original input layer produces an activation map, describing the locations in the original image for where certain low level features appear
    - this activation map serves as the input for the next layer, and so on
    - as you apply more complex filter layers (features made of combinations of lower-level features), the filters have a larger receptive field

# Math Techniques

## Reducing dimensions
  - conditional heteroskedasticity: when residuals are dependent on the data, like if there's a linear relationship between the data value and the size of the error
  - serial correlation: when a data feature is dependent on another
  - multicollinearity: when the residuals (differences between predicted & actual values) depend on each other
  - neutralization: find dimensions that produce neutralizing impact, and cancel them out
  - composite dimensions: find dimensions that can be compressed to a vector
    example: rather than graphing movement, and speed, and categories of movement (multiple dimensions), graph a vector of their relative position (one dimension)
  - embedded dimensional spaces: find dimensions that have the same input dimension and reduce according to that standard (embedded dimensions like time)
    example: rather than graphing time-based dimensions, graph their functions with time as an input in the same space
  - transform: embed information in another dimension using transforms
    example: rather than graphing the width, height, & depth of an object, embed the depth information in the width or height dimensions by transforming the width or height values

## Assessing displacement between functions/function overlap

  - Convolution
    - a particular kind of integral transform that consists of a math operation on 2 functions (f & g) to produce a 3rd function
      expressing how the shape of 1 is modified by the other (the act of transformation & measuring the difference created by that transformation)
    - convolution of functions f & g = the integral of the product of the two functions after one is reversed and shifted
    - can be derived as the inverse Fourier transform of the pointwise product of two Fourier transforms

    - Cross-correlation
      - a measure of similarity of two series as a function of the displacement of one relative to the other (sliding dot/inner product)
      - commonly used for searching a long signal for a shorter, known feature

    - Convolution & cross-correlation
      - Convolution is similar to cross-correlation.
      - For discrete, real-valued functions, they differ only in a time reversal in one of the functions.
      - For continuous functions, the cross-correlation operator is the adjoint of the convolution operator.

      - Shape comparison:
        - Convolution: flipped graph of g slid across f along the opposite axis as the flip axis, and a graph of the total area in common between the two shapes at every point during the slide
        - Cross-correlation: graph of g slid across f along the opposite axis as the flip axis, and a graph of the total area in common between the two shapes at every point during the slide
        - Auto-correlation: graph of g slid across itself, along the opposite axis as the flip axis, and a graph of the total area in common between the two shapes at every point during the slide

  - Kullback-Liebler Divergence
    - a Kullback–Leibler divergence of 0 indicates that the two distributions are identical

  - Jensen Shannon Divergence
    - bounded by 0 & 1
    - is symmetric & smoother than KL divergence

  - Wasserstein distance
    - used as a loss function in WGAN
    - aims to convert one distribution into another using the least energy
    - better for a smoother learning process during gradient descent bc it doesnt have as many jumps in divergence, unlike KL & JS
    - differentiable in more places than KL & JS
    - differentiability of the loss function is important bc during backpropagation, you differentiate the loss function to create the gradients (slope indicators), and the gradients update the weights

## Transforming one function into another
  - Fourier transform:
    - take a function & create a series of sine waves that combined approximate the original function
    - converting a function into a different domain where operations are easier to do
    - can be used to extract short & long-term trends with transforms of varying size (number of components)
    Example: differentiation in the original time domain is equivalent to multiplication by the frequency in the frequency domain, and multiplication is easier to do

  - Laplace transform: convert a function of t into a function of a complex variable s

  - Taylor Expansion:
    - linearization of a function as a sum of infinite terms, calculated from the original function's derivatives at individual points
    - used to calculate minima, maxima, & inflection points for infinitely differentiable functions
      <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/46dd2bf78ad7d792988cf616a6ea94024f30b3d9"/>
      <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b43af001b691a52034c46ff67dd15b4133285961"/>

  - Maclaurin Expansion:
    - special case of the Taylor series, where the original function is expanded around 0

## Methods of detecting feature importance
  - XGboost (eXtreme Gradient Boosting):
    - highly accurate for classification & regression problems
    - a type of boosted tree regression algorithms

# Error Functions

- Hinge
  - used for classification

-  Huber:
  - used for regression
  - less sensitive to outliers than MSE because it treats the error as a square only inside an intervals

- Relative entropy (Kullback-Leibler, Jensen-Shannon)

- L1 mean absolute error (MAE)
  - np.sum(np.absolute(yHat - y))

- L2 mean squared error (MSE)
  - np.sum((yHat - y) ** 2) / y.size

- Cross-entropy/log loss:
  - measures the performance of a classification model whose output is a probability value between 0 and 1
  - cross-entropy loss increases as the predicted probability diverges from the actual label
  - so a perfect model would have a log loss of 0
  - log loss penalizes especially those predictions that are confident & wrong
  <img src="https://ml-cheatsheet.readthedocs.io/en/latest/_images/cross_entropy.png"/>

  - binary entropy loss:
    - used with 2-category categorical output variables
    - −(ylog(p)+(1−y)log(1−p))

  - categorical entropy loss
    - used with multiple-category > 2 categorical output variables
    - calculate a separate loss for each class label per observation and sum the result
    - −∑ y(o,c) * log(p(o,c)) for 1 to M, the number of classes,
      where y is the binary indicator of whether c is the correct class label for observation o,
      and p is the probability that observation o is of class c

# Training methods

## Pooling
  - used to reduce spatial size (width & height dimensions) and counteract overfitting
    - max pooling:
      <img src="https://cntk.ai/jup/201/MaxPooling.png"/>
    - average pooling:
    - l2 norm pooling:

## Early stopping
  - technique to avoid overfitting when training with an iterative method like gradient descent
  - stops learning when additional learning would increase the generalization error (overfitting)
  - https://en.wikipedia.org/wiki/Early_stopping

## Regularization
  - preventing overfitting by standardizing a function to generalize better for additional data
    <img src="https://en.wikipedia.org/wiki/File:Regularization.svg"/>
  - 'Regularizers allow to apply penalties on layer parameters or layer activity during optimization. These penalties are incorporated in the loss function that the network optimizes.'
  - both L1 & L2 punish large weights
  - L1/Lasso Regression:
    - adds the mean absolute error to the loss
    - does both variable selection and parameter shrinkage
    - favors weights that go to zero bc its function becomes non-differentiable at 0
    - you can end up with a model that has very few parameters, reducing its complexity
    - works best when data is sparse, is more robust to outliers, and analyzes feature importance
  - L2/Ridge Regression (Weight decay)
    - adds the mean squared error to the loss
    - does only parameter shrinkage & uses all coefficients rather than reducing them
    - if variables are correlated, ridge regression might be better
    - works best when least square estimates have higher variance
    - favors smaller weights

## Dense sparse dense
  - In the first D step, we train a dense network to learn which connections are important.
  - In the S step, we regularize the network by pruning the unimportant connections and retrain the network given
  the sparsity constraint
  - In the final D step, we increase the model capacity by freeing the sparsity constraint, re-initializing the pruned parameters, and retraining the whole dense network
  - https://arxiv.org/pdf/1607.04381v1.pdf

## Data Augmentation
  - when you create more data entries with transforms in a way that doesnt change the correct output label, like shifting an image by a pixel, which has the same label but different data arrays

## Transfer learning
  - using a pre-trained model (or its output - the weights & parameters & a particular network type)
    where you replace the last layer with your own classification layer,
    then freeze the other layers (so their weights dont change during gradient descent/optimization) & train your model on your data
  - youd replace more layers the more different your problem is from the problem of the original model trainer, because youd need to use less of their weight/param insights

## Backpropagation

  - Before the CNN starts, the weights or filter values are randomized

  1. forward pass: pass a training data entry through the whole network

  2. loss calculation: evaluate difference between expected & predicted training label using a loss function
    - the training example contains a vector of the inputs/weights & the correct value at the end, which is then compared to the actual value
    - a typical measure of the error is the mean squared error: (correct - actual) ^ 2

  3. backward pass:
    - determine which inputs contributed most to the loss & find best way to reduce loss
    - find minimum on loss graph that is contributed by each input weight using derivative (dLoss/dWeight)
    - with standard optimization for a single input variable to find the function minimizing the loss
    - with gradient descent to calculate the partial derivative of the loss with respect to each weight, to find the set of weights minimizing the loss

    - if the output is on the x-axis and the error is on the y-axis, you see a parabola
    - the minimum of the parabola corresponds to the output x that produces the lowest error
      <img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Error_surface_of_a_linear_neuron_for_a_single_training_case.png"/>
    - each neuron's output is a weighted sum of all of its inputs
    - so rather than a function to find the minimum of a single-variable produced output, we're looking for a set of weights minimizing the error
    - if each weight is plotted on a separate horizontal axis and the error on the vertical axis, the result is a parabolic bowl
    - for a neuron with k weights, this would look like an elliptic paraboloid of k+1 dimensions
      <img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Error_surface_of_a_linear_neuron_with_two_input_weights.png"/>

  4. weight update: adjust the weights in each layer to reduce the loss using method established in backward pass
    - to update the weight using gradient descent, one must choose a learning rate > 0
    - the change in weight needs to reflect the impact on the error of a change in weight between i & j
    - if the partial derivative of error with respect to weight > 0, an increase in weight between i & j must increase the error
    - if the partial derivative of error with respect to weight < 0, a decrease in weight between i & j must decrease the error
    - the change in weight = the partial derivative of the error with respect to weight * -1 * the learning rate

  Insights:

    From wiki:
    - GD with backpropagation is only guaranteed to find a local minimum, not the global minimum
    - GD with backpropagation has trouble crossing plateaus in the error function landscape bc of error function non-convexity
    - backpropagation learning does not require normalization of input vectors, but normalization could improve performance

    From CNN Overview:
    - A high learning rate means that bigger steps are taken in the weight updates, so it may take less time for the model to converge on an optimal set of weights
    - A learning rate that is too high could result in jumps that are too large and not precise enough to reach the optimal point.
      <img src="https://adeshpande3.github.io/assets/HighLR.png"/>

## Gradient Descent to minimize loss

- gradient descent:
  - technique to minimize the error by finding the minimum using iterative steps
  - commonly used to find the set of weights minimizing the error
  - involves calculating the derivative of the squared error function with respect to the weights of the network
  - calculate the partial derivative of the error with respect to a weight w(ij):
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c8ea012fb2e6320752d8fdb92d0758fd2661b8fc"/>
    - where net(j) is the input to a neuron, which is the weighted sum of outputs of previous neurons,
    - o(j) is a neuron's output, or the result of the activation function applied to the (weighted sum of the previous layer's outputs),
      <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/49c9b06579762945e7648f39bb3f4e35c67669c5"/>
    - and w(ij) is the weight between neurons i & j,
    - using the chain rule:
      <img src="chain_rule.png"/>

- gradient:
  - gradients are used to update the weights of the network
  - vector pointing in the direction of the steepest ascent, where the vector's magnitude indicates the ascent steepness
  - partial derivative of error with respect to weight between neurons i & j
    <img src="partial_derivative_error.png"/>

- stochastic gradient descent:
  - gradient descent where samples are selected randomly, rather than in the order they appear in the training set, or in a single group (as in standard gradient descent)

- batch stochastic gradient descent
  - additional operations distribute the gradient:
  https://adeshpande3.github.io/adeshpande3.github.io/The-9-Deep-Learning-Papers-You-Need-To-Know-About.html

# Network Hyperparameters

To find hyperparameters, known methods include:
- manual search
- grid search (http://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/)
- random search
- bayesian optimization
- methods for auto-determining hyperparameter values in AutoML tools like AutoKeras

## Filter size
- use a small filter size if you think smaller features are more important for classification (edge, curve)
- use a larger filter size if you think larger features are more important for classification (cat/dog)

## Stride
- controls how the filter convolves around the input volume
- the filter convolves around the input volume by shifting one unit at a time - the amount by which the filter shifts is the stride
- stride is usually set in a way so that the output volume is an integer and not a fraction

## Padding
- pads the input volume with zeros around the border to preserve the dimensions of the output based on the input
- zero_padding = (filter_size - 1) / 2
- to calculate the output size for any given convolution layer:
  output_height = [(input_height - filter_size + (2 * padding))/stride] + 1

## Number of hidden layers
- hidden layers are between input & output layers
- a small number of layers may produce underfitting, a larger number with regularization can increase accuracy

## Dropout rate
- used to prevent overfitting & increase the generalization of the prediction function
- a small dropout value of 20 - 50% is recommended
- too high and the network will underlearn, too low and the network won't generalize well
- has a better impact on a larger network

## Learning Rate
- defines how quickly a network updates its parameters, controlling convergence speed & network performance
- the learning rate can be static, but adjusting it can overcome inherent problems
- low learning rate slows down the initial convergence/learning process but converges smoothly
- high learning rate speeds up the learning/convergence but may not converge
- usually a decaying Learning rate is preferred

## Momentum
- momentum helps to know the direction of the next step with the knowledge of the previous steps
- it helps to prevent oscillations
- a typical choice of momentum is between 0.5 to 0.9

## Number of epochs
- number of epochs is the number of times the whole training data is shown to the network while training
- ncrease the number of epochs until the validation accuracy starts decreasing even when training accuracy is increasing (overfitting)

## Batch size
- mini batch size is the number of sub samples given to the network after which parameter update happens
- a good default for batch size might be 32
- also try 32, 64, 128, 256, and so on
- https://towardsdatascience.com/what-are-hyperparameters-and-how-to-tune-the-hyperparameters-in-a-deep-neural-network-d0604917584a

# Unsupervised

- unsupervised learning can be used to identify features to use in supervised learning methods

## Dimensionality Reduction

  - LDA (Linear discrimination analysis):
    - used to find a linear combination of features that characterizes or separates >= 2 classes of objects/events

  - SVD (Singular Value Decomposition):
    - generalization of the eigendecomposition of a positive semidefinite normal matrix for any n x m matrix, using an extension of polar decomposition
    - used in least squares data-fitting, multivariable control, matrix approximation, and determining the rank/range/null space of a matrix
    - Example:
      - for 2d matrix M, the unit disc in blue has two canonical unit vectors
      - the action of M distorts the disk to an ellipse
      - the SVD decomposes M into 3 transformations:
        - an initial rotation V∗ (n x n unitary matrix)
        - a scaling Σ (m x n rectangular diagonal matrix) along the coordinate axes,
        - and a final rotation U (the m x m unitary matrix)
      - M = U Σ V∗ (the lengths σ1 and σ2 of the semi-axes of the ellipse (Σ1,1 and Σ2,2) are the singular values of M)
      <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Singular_value_decomposition.gif"/>

  - PCA (Principle Component Analysis)
    - dimensionality reduction technique, projecting original features into a smaller subspace, where the eigenvectors form the axes (eigenvectors only define directions of axes)
    - used to speed up high-dimensional ML by breaking it into dimensions (components) that explain the most variance, in descending order (principle)
    - PCA usually uses SVD over eigen decomposition of the covariance or correlation matrix for performance
    - PCA drops the eigenvectors with the lowest eigenvalues, bc they contain the least information about the original data
    - then it ranks them in descending order and chooses the top n eigenvectors
    - PCA can be done on any set of features (including features from autoencoders) to reduce their number

  - Autoencoders
    - feed forward non-recurrent nn for unsupervised learning
    - used to compress data & learn features
    - used for anomaly/outlier detection
    - has a encoder (reduction aspect) that reduces data the most possible
    - also has a decoder (reconstruction aspect), which aims to re-generate the original input from the encoded version
    - aim to minimize the reconstruction error (RE), which is the mean squared distance between input and output
    - used inside generative networks and also generally in deep learning nn's as its own set of stacked layers in the network for dimensionality reduction
    - basic logic: For each input x,
        Do a feed-forward pass to compute activations at all hidden layers, then at the output layer to obtain an output x'
        Measure the deviation of x' from the input x (typically using squared error),
        Backpropagate the error through the net and perform weight updates

    - Autoencoder Types

      - Denoising autoencoder
        - takes a partially corrupted input during training to recover the original undistorted input
        - a good representation can be obtained robustly from a corrupted input & will be useful for recovering the corresponding clean input
        - this definition of a good representation assumes that:
          - higher level representations are relatively stable & robust to input corruption & you must extract features useful for representation of the input distribution
        - to train an autoencoder to denoise data, it is necessary to perform preliminary stochastic mapping in order to corrupt the data
        - then you must use the mapped version as input for a normal autoencoder, the only exception being that the loss should still be computed for the initial input

      - Sparse autoencoder
        - as initial autoencoders were difficult to train, since the encodings have to compete to set the same small set of bits
        - to solve this, sparse autoencoders uses more (rather than fewer) hidden units than inputs, but only a small number of the hidden units are allowed to be active simultaneously
        - sparsity may be achieved by additional terms in the loss function during training (by comparing the probability distribution of the hidden unit activations with some low desired value),[9] or by manually zeroing all but the few strongest hidden unit activations (referred to as a k-sparse autoencoder).[10]

      - Variational autoencoder (VAE)
        - inherits autoencoder architecture, but makes strong assumptions concerning the distribution of latent variables
        - use variational approach for latent representation learning, resulting in an additional loss component & specific training algorithm, Stochastic Gradient Variational Bayes
        - assumes data is generated by a directed graphical model p(x|z) and the encoder is learning an approximation to the posterior distribution
        - the objective of the variational autoencoder in this case has the following form:
          objective function = [Kullback–Leibler divergence of the encoder parameter's approximation (z|x) of the decoder parameter's posterior distribution(z)] - [E log decoder parameter's posterior distribution(z|x)]

      - Contractive autoencoder (CAE)
        - adds an explicit regularizer in its objective function that forces the model to learn a function that is robust to slight variations of input values
       - this regularizer corresponds to the Frobenius norm of the Jacobian matrix of the encoder activations with respect to the input

    - Resources:
     - https://en.wikipedia.org/wiki/Autoencoder
     - https://blog.goodaudience.com/neural-networks-for-anomaly-outliers-detection-a454e3fdaae8
     - https://medium.com/@curiousily/credit-card-fraud-detection-using-autoencoders-in-keras-tensorflow-for-hackers-part-vii-20e0c85301bd

## Clustering

## K-nearest neighbors
- create tree, using a binary decision

# Supervised

## Multi-layer Perceptron
- a standard feedforward nn consisting of at least three layers (input, hidden, & output)
- each node except for the input nodes uses a nonlinear activation function
- it uses backpropagation to train
- it can distinguish data that is not linearly separable, whereas linear perceptrons can only distinguish data that is linearly separable
  (you can draw a line separating sets of points)
- every layer is fully connected to every other layer

## Support Vector Machine
- a SVM model is a linear classifier that maximizes the gap between categories
- new examples are then mapped into that space and predicted to belong to a category based on which side of the line theyre on
- SVMs can also do non-linear classification with the kernel trick (mapping data into high-dimensional feature spaces to find the dimensions needed to maximize the gap)
  <img src="https://en.wikipedia.org/wiki/File:Kernel_trick_idea.svg"/>
- 'using in a higher-dimensional feature space increases the generalization error of SVMs, but with enough samples it still performs well'
  https://en.wikipedia.org/wiki/Support-vector_machine

## GAN
  - involves a generator model & a discriminator model
  - use the Discriminator for the sole purpose of better training the Generator
  - goal is to learn the distribution of the real data, using the Generator to convert random noise into data similar to the target original data
  - real or generated data is fitted at random into the Discriminator, which acts as a classifier, predicting whether the data is in the Generator category or the real data category
  - Discriminator estimates the probabilities of the incoming sample based on the real dataset (KL & JS & GRS)
  - the losses from G & D are combined & propagated back through the generator, which helps the Generator learn about the real data distribution
  - so the generator’s loss depends on both the generator & the discriminator
  - if the generator doesnt create realistic data, the Discriminator’s categorization loss will be very small
  - small discriminator loss results in bigger generator loss, which means too good of a discriminator always results in a huge generator loss, making the generator unable to learn
  - the process repeates until the Discriminator can no longer distinguish generated vs. real data
  - the Generator tries to fool the Discriminator, and the Discriminator wants to categorize the data coming from the Generator
  - they have separate loss functions, but when combined they take the form:
    <img src="gan_loss_function.png"/>
  - comparing similarity between distributions is key; KL & JS are most common methods
  - GAN models may never converge and mode collapse can easily happen with GANs
  - DRS & MHGAN use the discriminator after training to choose generated data similar to the original data
  - methods:
    - Discriminator Rejection Sampling
  - Metropolis-Hastings GAN
    - uses Markov Chain Monte Carlo (MCMC) for sampling
    - takes K samples generated from independent noise inputs to the Generator
    - sequentially runs through the K outputs and uses an acceptance rule from the Discriminator to decide whether to accept the current sample or keep the last accepted sample
    - the last kept output is the one considered the real output of Generator
  - Wasserstein GAN

## CNN
- convolution (cnn-specific):
  - sliding a set matrix size over the inputs to represent the receptive field
  - the receptive field grows larger with later layers
  - before the CNN starts, the weights or filter values are randomized
- receptive field (cnn-specific):
  - set matrix size (w x h x d), representing the logical size in which to find a particular attribute
- typical CNN layer order:
  <img src="https://adeshpande3.github.io/assets/Table.png"/>
- work well on spatial data (data that is related to nearby data, such as time series data)

## RNN
  - have a problem with retaining important past info with long sequences
  - used with time-series data bc they keep track of all previous data points & can identify patterns developing over time
  - works well with short sequences & has better performance than lstm or gru
  - Attention vector:
    https://machinelearningmastery.com/how-does-attention-work-in-encoder-decoder-recurrent-neural-networks/

## LSTM
- aims to solve the vanishing gradient problem of RNNs by deciding which info is important to keep
- the gates of an lstm use sigmoid activations
- has four gates: update, input, forget, and output
- the hidden state of each cell
  - contains info from previous inputs
  - is used for predictions
- the forget gate decides what info to keep from previous steps
  - passes info from the previous hidden state & the current input through the sigmoid function
  - near 0 values are forgotten & near-1 values are retained
- the input gate decides what info should be added to the current step
  - updates the cell state
  - pass the previous hidden state & current input into both the sigmoid and tanh functions, and then multiply their output
  - the sigmoid will decide what info to keep from the tanh function
- the cell state
  - after the input gate, the cell state is multiplied by the pointwise forget vector
  - then from the input gate output, do a pointwise addition to update the cell state to the new values deemed relevant
- the output gate decides what the next hidden state should be
  - pass the previous hidden state & current input into the sigmoid function, then to the tanh function, then multiply their output to get the next hidden state
- stacking LSTM layers can help but can also lead to overfitting with small data sets

## GRU
- aims to solve the vanishing gradient problem of RNNs by deciding which info is important to keep
- similar to LSTM, has gates to regulate how information is passed within the network (but without the LSTM cell state, just the hidden state) & are a little faster than LSTM
- GRUs also doesnt apply a nonlinearity function (like the sigmoid) before the output gate, but LSTM does apply the sigmoid before the output gate
- has two gates: an update & reset gate to decide which info should be passed to the output
- the update & reset gates can retain info from many time periods before without altering info
- the update gate tells the model how much past info should be passed to the future, deciding what info to forget & what to add
- the reset gate also tells the model how much info to forget

# Augmented Random Search
  - https://arxiv.org/pdf/1803.07055.pdf

# Reinforcement Learning
  - maximizes a reward function using experience about previous action outcomes in an environment rather than using labeled data (as supervised learning does)
    https://en.wikipedia.org/wiki/Reinforcement_learning
  - modeled as a Markov decision process:
    https://en.wikipedia.org/wiki/Markov_decision_process
  - key is to accurately set the reward, which has the formula:
    reward = 2 * lossG + lossD + accuracyG (of the generator & discriminator)
    where the environment is the GAN plus the results of the LSTM/GRU training, and the available actions are changing the hyperparameters
  - useful when a simulated model of the environment is known & interacting with the environment is the only way to extract information about it
  - example use case is to decide whether to update hyperparameters during training by passing the loss value to the reward function of the RL method
  - methods:
    - environment model:
      - criterion of optimality
      - brute force
      - value function
        - Monte Carlo methods
        - temporal difference methods
      - direct policy search
    - no environment model:
      - multi-agent: https://bair.berkeley.edu/blog/2018/12/12/rllib/
      - policy optimization: learning the optimal action to take given a particular state & using methods like actor vs. critic, learning the value of being in a given state
        - proximal policy optimization: directly learns the policy rather than indirectly through the values
        - works well in continuous action spaces
        - can learn the distribution probabilities using mean & standard deviation if softmax is added as an output function
        - problem with policy gradient methods:
          - extremely sensitive to step size parameter value
          - too small step size takes too long
          - too large step size increases noise & reduces performance
          - input data, reward distribution, & observation distributions change
        - ppo can address the policy gradient method problems
          - ppo uses a clipped surrogate objective function & changes the objective function to punish updates that are too big
          - is compatible with methods that share parameters between value & policy function or supplementary losses compared to TRPO
          - ppo has the gain of TRPO
        - ppo alternatives:
          - Asynchronous Actor-Critic: running agents in parallel to stabilize training
          - ACKTR (Actor Critic using Kronecker-Factored Trust Region)
          - acer (Actor-Critic with Experience Replay): requires tracking off-policy correlations & a replay buffer
          - trust region PO:
            - has constraint on surrogate objective function (Kullback-Liebler divergence between old & new policy), used to control over-changing which can lead to instability
          - Source: OpenAI Baselines
            https://github.com/openai/baselines
      - q-learning: learning the q-value reward expected from taking an action given a particular state
        - rainbow: a combination of 7 q-learning algorithms based on policy deep reinforcement learning
          - DQN
          - double q learning
          - prioritized replay
          - dueling networks
          - multi-step learning
          - distributional RL
          - noisy nets
          https://arxiv.org/pdf/1710.02298.pdf
    <img src="reinforcement_methods.png"/>

# Hyperparameter optimization
- Grid search:
  - a comprehensive search of a set of finite possible reasonable hyperparameter values, guided by a performance metric
  - disadvantages: the curse of dimensionality & is often embarrassingly parallel because typically the hyperparameter settings it evaluates are independent of each other
- Random search
  - a search of randomly selected hyperparameter values
  - generalizes to continuous & mixed spaces
  - can beat grid search particularly when a small number of hyperparameters affects the model performance (low intrinsic dimensionality)
  - disadvantages: embarrassingly parallel, and allows including prior knowledge by specifying the distribution to sample from
- Bayesian optimization:
  - an optimization method for noisy functions
  - iteratively evaluates a promising hyperparameter configuration based on the current model & then updates it
  - aims to gather observations revealing as much info as possible about this function and the location of the optimum
  - tries to balance exploration (hyperparameters for which the outcome is most uncertain) and exploitation (hyperparameters expected close to the optimum)
  - performs better than random search & grid search because it can predict the expected return of various changes
- Gradient-based optimization
  - compute the gradient with respect to hyperparameters and then optimize the hyperparameters using gradient descent
  - used in SVM and logistic regression
  - variations include differentiating the steps of an iterative optimization algorithm using automatic differentiation
- Evolutionary optimization
  - an optimization method for noisy functions
  - uses evolutionary algorithms to search the space of hyperparameters for a given algorithm
    1. create an initial population of random outcomes/solutions (i.e., randomly generate tuples of hyperparameters)
    2. evaluate the tuples & acquire their fitness function
    3. rank them by their relative fitness
    4. remove worst perfoming tuples & replace with new generated tuples using crossover & mutation
    5. repeat until no longer improving or optimal state reached
  - used in hyperparameter optimization for statistical machine learning algorithms, auto ML, deep NN architecture search, & training weights in deep NNs
- Radial basis function:
  - assessing value by distance from the origin
  - used to approximate functions
  - also used as a kernel in support vector classification
  - where the approximating function y(x) is represented as a sum of N radial basis functions, each having a different center x, and weighted by an appropriate coefficient w
  - the weights can be estimated using the matrix methods of linear least squares, because the approximating function is linear in the weights
- Spectral methods:
  - posing solutions to differential equations as a sum of basis functions & then choose the sum's coefficients to satisfy the differential equation
  - https://en.wikipedia.org/wiki/Spectral_method
- Finite Element method:
  - subdivides a large system into smaller, simpler parts that are called finite elements
  - the simple equations that model these finite elements are then assembled into a larger system of equations that models the entire problem
  - https://en.wikipedia.org/wiki/Finite_element_method
- Source: https://en.wikipedia.org/wiki/Hyperparameter_optimization

# Activation Functions
- non-linear & differentiable
  <img src="activation.png"/>
- used to introduce nonlinearity to models, allowing models to learn nonlinear prediction boundaries
  <img src="learning_rate.png"/>

## Relu
  - returns the positive part of the input
  - counteracts nonlinearity of the network
  - the derivative of the rectifier function is the heaviside step function
  - have the advantages of being one-sided, have sparse activation, better gradient propagation, efficient computation, and are scale-invariant
  - have the disadvantages of not being differentiable at 0, not centered at 0, unbounded
  - also have the dying relu problem, where they become stuck inactive (vanishing gradient problem) bc of a high learning rate, so to offset this use a leaky relu

## Leaky Relu
  - x if x > 0, and x * 0.01 if x <= 0
  - returns the input value if positive, and 0 or near 0 if negative, where the input is a layer's slope
  - found to decrease training time as ReLUs are several times faster than the conventional tanh function
  - allow a small positive gradient when the unit is inactive
  - use a leaky relu to offset the dying relu problem where many neurons become stuck inactive
  - often used in GANs

## Parameteric ReLUs
  - use the leak coefficient as a learnable network parameter
  - x if x > 0, and ax if x <= 0

## ELUs
  - exponential linear unit try to make the main activations close to 0
  - intended to speed up learning
  - can achieve higher classification accuracy than ReLUs
  - x if x > 0, and a(e^x - 1) if x <= 0

## GELUs
  - Gaussian Error Linear Units
  - GELUs involve the 'expected transformation of a stochastic regularizer which randomly applies the identity or zero map to a neuron's input'
    https://arxiv.org/abs/1606.08415
  - the GELU nonlinearity has the effect of weighting inputs by their magnitude rather than by their sign
  <img src="gelu_relu_lrelu.png"/>

## Softplus
  - softplus/analytic function: smooth alternative to relu
  - the derivative of softplus is the logistic/sigmoid function
  - log(1 + e^x)

## Softmax
  - average the softmax probabilities of multiple versions of the same input (crops of the same image) to achieve a balanced solution
  - used to make multi-class predictions

## Logistic function
  - used to introduce nonlinearity or keep the neural network response bounded by a range
  - appears in feedforward neural networks
  - predicts the probability of outcomes rather than the outcomes themselves; predicted values are probabilities between 0 and 1
  - used by logistic models to describe a binary dependent variable (y) in logistic regression, which estimates the parameters of a logistic model, a subset of binomial regression
  - bc its output is binary, the conditional distribution (y | x) is bernouill rather than gaussian
  - multinomial logistic regression is where the depending variable has more than 2 categorical outputs
  - ordinal logistic regression is a case of multinomial logistic regression where the outputs are ordered
  - derivative of the softplus function

  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/6f42e36c949c94189976ae00853af9a1b618e099"/>
  <img src="https://en.wikipedia.org/wiki/File:Logistic-curve.svg"/>

## Sigmoid function
  - an activation function that takes in a set of values between 0 and 1 and outputs a binary value (0 or 1) based on some limit determined by the function
  - sigmoidal functions that are antisymmetric about the origin lead to faster convergence in backpropagation
  - continuous s-shape function, in certain cases going from y = 0 to y = 1 as in the case of the logistic function
  - frequently used as an activation function as 1/(1 + e^x), which is a special case of L/(1 + e^-k(x-x0))
  - common in statistical CDFs (cumulative distribution functions), for example the integrals of the logistic, normal, and Student's t PDFs (probability density functions)
  - the CDFs for many common probability distributions are sigmoidal
  - used to make binary predictions
  - rather than using sigmoids, you can use tanh & then transform the tanh output with a sigmoid to decide what info to keep from tanh
    https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21

  <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9537e778e229470d85a68ee0b099c08298a1a3f6"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Error_Function.svg/640px-Error_Function.svg.png" style="width:30%;"/>

# Layer Types

## Network layer
  - a linear function of input + weight * bias; nonlinearity is necessary in the activation function to restrict output to a range

## Activation layer
  - used to standardize input, such as values between 0 and 1, excluding negative values

## Dropout layer
  - used to reduce overfitting, by forcing the training process to produce the same result regardless of whether some activations are dropped at random (set to 0)

## Network in network layer (1x1 convolution)
  - method of dimensionality reduction or pooling of features bc it also reduces the volume depth passed to layers, like how max pooling layers reduce the height & width of layers
  - applying 20 filters of 1x1 convolution to 100x100x60 = 100x100x20
  - extracts detailed information

## Fully connected (dense) layers
  - require a large number of parameters, so avoid if possible
  - determines if the high level features (combinations of lower level features) correspond to a particular class
  - checks if the product of the weights x the previous layer values correspond to a classes probabilities, via backpropagation

# Stat terms

- ARIMA (Autoregressive integrated moving average)
  - technique for predicting time series data
  - the evolving variable of interest is regressed on its own prior values
  - the regression error is a linear combination of error terms whose values occurred contemporaneously & at various times in the past
  - the data values are replaced with the difference between their values & the previous values (and this process may have been performed more than once)
  - https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average

- Vanishing gradients problem
  - seen with RNNs
  - may be handled with Gated Recurrent Units
  - happens when gradient values become too small during backpropagation for their contribution in updating weights to be useful
  - makes the network unable to converge to a minimal loss so it doesnt learn new info
  - layers that get a small gradient update (usually the early local layers) stop learning, so the network has short-term memory
  - can this be used in tandem with transfer learning to create later layers?

- Initialization techniques
  - usually the normal distribution is used to initialize the weights, but a different distribution may be better based on the activation function used
  - Xavier initialization:

- Non-convex optimization

- Batch Normalization:
  - a performance-improving technique that provides any nn layer with inputs that are 0 mean/unit variance
  - normalizing the input layer by adjusting & scaling the activations

- Normalization: data preprocessing to standardize the range of independent data values (like compressing from 0 to 1)

- Regression: line-fitting

- Categorization: predicting the class of a test data point based on classes of training data points

- Bayesian: conditional probability

- Probability distribution: probabilities associated with set of possible outcomes

- Linear: any function with no terms having exponents higher than 1

- Bias: measures how badly a model generalizes on new data (high bias = underfitting)

- Variance: measures how sensitive a model is to changes in the data (high variance = overfitting)

- Bias vs. variance tradeoff: error = bias^2 + variance + error_due_to_noise

- Coefficient of determination:
  - proportion of the independent variable explained by the dependent variable
    <img src="coefficient_of_determination.png"/>

- Covariance & Correlation Matrix:
  - the correlation matrix is typically used instead of the covariance matrix
    <img src="cov.png"/>

- Eigendecomposition:
  - the eigendecomposition of the covariance matrix (if the input data was standardized) yields the same results as a eigendecomposition on the correlation matrix
  - this is bc the correlation matrix can be understood as the normalized covariance matrix
  - Eigenvectors (principal components) determine the directions of the new feature space
  - Eigenvalues determine their magnitude, so they explain the data variance along the new feature axes
  - https://plot.ly/ipython-notebooks/principal-component-analysis/#covariance-matrix

## Decision Logic
- ML algorithm logic
  <img src="https://cdn-images-1.medium.com/max/1600/1*Gbfq8wTIyHBnC5oDhzNACw.png"/>

# Network Variations

## U-Net
- architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization
- outperforms the prior best method (a sliding-window convolutional network)
- https://arxiv.org/abs/1505.04597

## Sources:
- CNN Granular Logic:
  https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/

- ML basic docs:
  https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html

- Microsoft Cognitive Toolkit (CNTK) CNN Docs:
  https://cntk.ai/pythondocs/CNTK_103D_MNIST_ConvolutionalNeuralNetwork.html

- Overview of GRUs:
  https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be

- Algorithm Application for Trading Analysis:
  https://towardsdatascience.com/aifortrading-2edd6fac689d

- MLPs are a basic machine learning network structure that could help you find patterns once you have the data
- CNNs are great for images but storing the chemical structure probably takes less space if you use a formula rather than a block of pixels - they've adapted a lot recently so they may be a good option too.
- Reinforcement learning algorithms require structuring your data in a non-standard way (as a set of agents & actions) and have other requirements for most implementations to be relevant.
- Performance of K nearest neighbors degrades when the data is high dimensional. This can be avoided by providing weights to the features itself.

- Many algorithms, including Support Vector Machines, linear regression, logistic regression, neural networks, and nearest neighbor methods, require that the input features be numerical 
and scaled to similar ranges (e.g., to the [-1,1] interval)
- Methods that employ a distance function, such as nearest neighbor methods and support vector machines with Gaussian kernels, are particularly sensitive to this

- Markov process: transitions between states have known probabilities & probability of next state is only dependent on current state, not moves previous to the current state - meaning each move doesn't store information in the process beyond one move.
- with PCA, choose the number of components that has a variance between 95–99% to avoid losing too much information about the data
- "If each of the features makes an independent contribution to the output, then algorithms based on linear functions (e.g., linear regression, logistic regression, Support Vector Machines, naive Bayes) and distance functions (e.g., nearest neighbor methods, support vector machines with Gaussian kernels) generally perform well. However, if there are complex interactions among features, then algorithms such as decision trees and neural networks work better" (https://en.wikipedia.org/wiki/Supervised_learning)
- To measure non-Gaussianity of the linear combination of independent features in ICA, the algorithm uses a nonquadratic nonlinear function f(v), its first derivative g(v) and its second derivative g’(v). This is a good way to measure the difference between the normal distribution (similar to a parabola) and its rate of change, and its rate of change of its rate of change.
- one hot encoding prevents the ML model from interpreting a higher category value as indicating higher importance, if the category distribution doesnt match that pattern (most situations, unless you assign more average categories to higher values)

Methods that assume data is normally distributed:
- Linear Discriminant Analysis (LDA)
- Naive Bayes Classifiers

- With multiple definitions of change (output value change from a function, state changes of the function, and differences between functions), ICA methods will be useful when determining change rules in a system.

Feature engineering
- Log TransformL transform the distributions of the original features to resemble the normal distribution

Feature reduction 
	Linear relationships between features:
		Support Vector Machine: 
		Principal Components Analysis (PCA): used for dimensionality reduction and feature extraction, uses principal components (linear combinations of features) to find the combination that explains the most variance in the data set & minimizes the reconstruction error
		Independent Components Analysis (ICA): used for source separation with linear combinations of non-Gaussian (non-normal) independent features, which implies a sum of those features would be Gaussian distributed
		Nonnegative Matrix Factorization (NMF): used for source separation with linear combination of features into matrixes W & H = X that are nonnegative, first initializing W and H randomly, then at each iteration, update new H given old H and W, then new W given H and old W, using multiplicative update rules, using the Frobenius norm between X and WH until convergence
		Random forests
	Non-linear relationships between features:
		Locally Linear Embedding: a dimensionality reduction technique based on Manifold Learning which looks for a lower-dimensional projection of the data that preserves distances within local neighborhoods - a series of local PCA which is globally compared to find the best non-linear embedding.
		t-distributed Stochastic Neighbor Embedding (t-SNE): minimizes the KL divergence using gradient descent between a distribution of the input feature pairwise probability similarities in the original high dimensional space modeled as a normal distribution, and its equivalent distribution in the reduced low dimensional space modeled as a student's t distribution (like mapping a sphere to a circle or a plane to a line).
		Autoencoders: project data from a higher dimension to a lower one using non-linear transformations, first encoding to a lower dimensional space, then attempting to decode the encoded set into the original data distribution. If each feature is independent, the data set may not be reducible. Uses a non-linear activation function to avoid replicating results of other DR methods.

	High correlation filters
	Backward feature elimination


Supervised learning (has the answer category in the data set, called the output label)
- linear regresion
- k nearest neighbors regression
- decision trees are usually built with recursive binary fitting, which includes greedy splitting (choosing the best split that covers the most data at a given branch)
- to handle decision trees' overfitting problem, tree pruning is used which produces a smaller tree
- to handle decision trees' overfitting, add bagging (averaging a set of observations), random forest (a group of decision trees whose inputs are randomly selected from the full set of inputs to differentiate their contributions & whose output is weighted to give the final output), boosting (using information from prior trees to build a new more optimal tree)

Unsupervised learning (need to find the answer category)
- K-Means Clustering to separate the data into regions formed by a certain distance away from randomly selected points, then doing the same operation again with the points in the center of each region to make new regions until the difference is not noticeable
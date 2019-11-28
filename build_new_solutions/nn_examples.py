# Standardization: scales the input features while taking into account their standard deviation (using Standardization our transformed features will look similar to a Normal Distribution). This method can reduce outliers importance but can lead to different ranges between features because of differences in the standard deviation. Standardization can be implemented in scikit-learn by using StandardScaler().
# Normalization: scales all the features in a range between 0 and 1 but can increase the effect of outliers because the standard deviation of each of the different features is not taken into account. Normalization can be implemented in scikit-learn by using MinMaxScaler().

# https://github.com/keras-team/keras/tree/master/examples
# DNN https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('dataset.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
# make class predictions with the model
predictions = model.predict_classes(X) #model.predict(X)
# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

# MLP https://github.com/Rogerh91/Springboard-Blog-Tutorials/blob/master/Neural%20Networks%20/JMPortilla_SpringBoard_Blog_Neural_Network.ipynb

import pandas as pd
compound_data = pd.read_csv('dataset.csv', names = column_list)
compound_data.head()
compound_data.describe().transpose()
# 178 data points with 13 features and 1 label column (in the other example in that guy's blog)
compound_data.shape # prints the dimensions of the matrix storing this data # (178, 14)
output_label = 'Successful Treatment true/false'
X = element_list.drop(output_label,axis=1)
y = compound_data[output_label]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)
from sklearn.preprocessing import StandardScaler

'''
Scale your data to standardize it if youre going to use a variety of algorithms
Many algorithms, including Support Vector Machines, linear regression, logistic regression, neural networks, and nearest neighbor methods, require that the input features be numerical 
and scaled to similar ranges (e.g., to the [-1,1] interval)
Methods that employ a distance function, such as nearest neighbor methods and support vector machines with Gaussian kernels, are particularly sensitive to this
'''
scaler = StandardScaler()
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

''' add regularization '''

from sklearn.neural_network import MLPClassifier
# if you had 13 features of chemical pairs & bond types
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(X_train,y_train)
'''
 MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(13, 13, 13), learning_rate='constant',
       learning_rate_init=0.001, max_iter=500, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
'''
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
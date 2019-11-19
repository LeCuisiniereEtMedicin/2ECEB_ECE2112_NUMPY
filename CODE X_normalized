import numpy as np
#Lets make a random 5x5 array
X = np.random.random((5,5))
#Get the mean value of the elements in X
xbar = np.mean(X)
#Get the standard deviation of the elements in X
sdev = np.std(X)
#Use the formula to normalize x
z = (X - xbar)/sdev
#Time to Save the Noramlized X, z
np.savez('X_normalized.npy', z)

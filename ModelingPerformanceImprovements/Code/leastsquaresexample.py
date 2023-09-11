'''Python 3 example code for least squares fitting of exponential learning model'''

#Import required libraries
#You will need to install numpy, scipy, pandas, and matplotlib if you haven't already.
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#Load in your data
data = pd.read_csv('LumositySample_user48567.csv')
t = data.gameplay
obsy = data.score

#Show data
plt.plot(t, obsy, 'k-o')
plt.xlabel('Gameplay')
plt.ylabel('Score')
plt.show()

'''Function that defines the exponential model so we can reuse it easily later.
	Returns predicted y based on the parameters and gameplay #'''
def expmodel(c, a, u, t):
	predy = a - (a - u) * np.exp(-c * t) #predicted scores
	return predy

'''Function that computes the predicted performance of the exponential model at times t given parameters c, a, and u.
 Returns the mean squared error (mse) for the predicted and observed scores.'''
def calcmse(params, t, obsy):
    # Parameters
    c = params[0] #assume that the first parameter is c
    a = params[1] #assume that the second parameter is a
    u = params[2] #assume that the third parameter is u
    
    # predicted scores
    predy = expmodel(c, a, u, t) #predicted scores
    # Mean squared deviations between predicted and observed scores -- this is what we want to minimize
    mse = np.mean((predy - obsy)**2)
    
    return mse

'''Starting parameter values for the optimization procedure 
(i.e. guesses for the parameters that are not too far off from optimal values)'''
p0 = np.zeros(3)
p0[0] = 0.5 # parameter c
p0[1] = 100 # parameter a
p0[2] = 50 # parameter u

'''Run the optimizer and get the parameters p that minimize the squared deviations'''
result = minimize(calcmse, p0, args=(t, obsy))
p = result.x
mse = result.fun
c = p[0]
a = p[1]
u = p[2]

#Report the parameters found
print('Best fitting parameters:')
print('c={0:3.3f}'.format(c))
print('a={0:3.3f}'.format(a))
print('u={0:3.3f}'.format(u))
print('MSE={0:3.3f}'.format(mse))
#Calculate the predicted y using the best fitting parameters
predy = expmodel(c, a, u, t)

#Overlay the best fitting curve
plt.plot(t, obsy, 'k-o')
plt.plot(t, predy, 'r-')
plt.xlabel('Gameplay')
plt.ylabel('Score')
plt.show()
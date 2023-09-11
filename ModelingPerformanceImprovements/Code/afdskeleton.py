'''Python 3 example code for least squares fitting of AFD model'''

#Import required libraries
#You will need to install numpy, scipy, pandas, and matplotlib if you haven't already.
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#Load in your data
data = pd.read_csv('LumositySample_user30222.csv')
g = data.gameplay
obsy = data.score
s = data.session
d = data.dayselapsed

#Show data
plt.plot(g, obsy, 'k-o')
plt.xlabel('Gameplay')
plt.ylabel('Score')
plt.show()


def afdmodel(u, b, h, c, s, d, g):
    n = len(g) # We need the total number of gameplays
    # Put your afd code here based on the pseudocode in the book
    predy = u - (b - h) * np.exp(-c * g) #Change this to the correct equation
    return predy

'''Function that computes the predicted performance of the AFD model at times t given parameters c, a, and u.
 Returns the mean squared error (mse) for the predicted and observed scores.'''
def calcmse(params, s, d, g, obsy):
    # Parameters
    u = params[0] #assume that the first parameter is u
    b = params[1] #assume that the second parameter is b
    h = params[2] #assume that the third parameter is h
    c = params[3] #assume that the fourth parameter is c  

    # predicted scores
    predy = afdmodel(u, b, h, c, s, d, g) #predicted scores
    # Mean squared deviations between predicted and observed scores -- this is what we want to minimize
    mse = np.mean((predy - obsy)**2)
    
    return mse

'''Starting parameter values for the optimization procedure 
(i.e. guesses for the parameters that are not too far off from optimal values)'''
#Make sure you define your parameters in the same order as in calcmse 
p0 = np.zeros(4)
p0[0] = 30 #u
p0[1] =  1 #b
p0[2] = 10 #h
p0[3] = 0.2 #c

'''Run the optimizer and get the parameters p that minimize the squared deviations'''
result = minimize(calcmse, p0, args=(s, d, g, obsy)) #data values go into the args
p = result.x
#Report the parameters found
print('Best fitting parameters:')
print('u={0:3.3f}'.format(p[0]))
print('b={0:3.3f}'.format(p[1]))
print('h={0:3.3f}'.format(p[2]))
print('c={0:3.3f}'.format(p[3]))

u = p[0]
b = p[1]
h = p[2]
c = p[3]

#Calculate the predicted y using the best fitting parameters
predy = afdmodel(u, b, h, c, s, d, g)

#Overlay the best fitting curve
plt.plot(g, obsy, 'k-o')
plt.plot(g, predy, 'r-')
plt.xlabel('Gameplay')
plt.ylabel('Score')
plt.show()
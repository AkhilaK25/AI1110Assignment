import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=50
maxlim= 6.0
x = np.linspace(-maxlim+2,maxlim,maxrange) #points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
randvar = np.loadtxt('tri.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def tri_pdf(x):
    if (0 <= x < 1):
        return x
    elif (1 <= x < 2):
        return 2 - x
    else: return 0

vec_tri_pdf = scipy.vectorize(tri_pdf, otypes=['double'])

plt.plot(x[0:(maxrange-1)],pdf,'o')
plt.plot(x,vec_tri_pdf(x)) #plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
plt.savefig('q4.3.png')
plt.show() #opening the plot window

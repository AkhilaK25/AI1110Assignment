import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,40) #points on the x axis
simlen = int(1e6) #number of samplesgoogle drive
err = [] #declaring probability list

randvar = np.loadtxt('tri.dat',dtype='double')
for i in range(0,40):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x,err,'o') #plotting stimulation CDF
plt.plot(x.T,err,color="orange") #plotting theory CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical", "Theory"])
plt.savefig('q4.2.png')
plt.show() #opening the plot window

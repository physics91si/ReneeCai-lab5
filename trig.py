#!/usr/bin/python
#to run this file, type in the command line: "python trig.py"

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

#x assigns an array from 0 to pi with a step size of 0.01
x = np.arange(0,np.pi,0.01)
#y is assigned the function sin(x)
y = np.sin(x)

#This plots the graph of sin(x) from 0 to pi 
plt.plot(x,y)


#The following function gives an approximate integral value by summing up many small rectangles of height y and width dx
def integrate(y, dx):
    np.sum(y*dx) 

#z is assigned the function cos(x)
z = np.cos(x)
#This plots the graph of cos(x) from 0 to ppi
plt.plot(x,z)

#Testing the integrate function with sine and cosine 
integrate(y,0.01)
integrate(z,0.01)

#Using a numpy function, "trapz" (trapezoidal rule), to approximate the integral
#numpy.trapz(function,stepsize) 
np.trapz(y,x)
np.trapz(z,x) 
    

    
    
    
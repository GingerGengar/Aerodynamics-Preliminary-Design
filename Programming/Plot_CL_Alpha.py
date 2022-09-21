#!/bin/python

#Library imports
import matplotlib.pyplot as plt
import numpy as np
import sys

file = str(sys.argv[1])
data = np.genfromtxt(file)

#Plotting Time History of AOA    
figure_CL, axis_CL = plt.subplots()
axis_CL.plot(data[:,0], data[:,1], 'rx',label='Airfoil')
axis_CL.set_xlabel('Angle of Attack (degrees)')
axis_CL.set_ylabel('Lift Coefficient')
axis_CL.set_title('Lift Slope of Airfoil')
axis_CL.legend()
axis_CL.grid()

plt.show()

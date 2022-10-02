#!/bin/python

#Library imports
import matplotlib.pyplot as plt
import numpy as np
import sys

file = str(sys.argv[1])
data = np.genfromtxt(file)

#Plotting Time History of AOA    
figure_CL, axis_CL = plt.subplots()
axis_CL.plot(data[:,1], data[:,2], 'rx',label='Airfoil')
axis_CL.set_xlabel('Lift Coefficient')
axis_CL.set_ylabel('Drag Coefficient')
axis_CL.set_title('Drag Polar')
axis_CL.axis('equal')
axis_CL.legend()
axis_CL.grid()

plt.show()

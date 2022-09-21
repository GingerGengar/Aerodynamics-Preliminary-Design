#!/bin/python

#Library imports
import matplotlib.pyplot as plt
import numpy as np
import sys

file = str(sys.argv[1])
data = np.genfromtxt(file)
data = data[data[:,2]>0]

#Plotting Time History of AOA    
figure_CL_Max, axis_CL_Max = plt.subplots()
axis_CL_Max.plot(data[:,0], data[:,1], 'rx',label='Airfoil')
axis_CL_Max.set_xlabel('Reynold\'s Number')
axis_CL_Max.set_ylabel('Maximum Lift Coefficient')
axis_CL_Max.set_title('Lift Vs Reynold\'s Number')
axis_CL_Max.legend()
axis_CL_Max.grid()

plt.show()

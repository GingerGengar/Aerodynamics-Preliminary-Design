#!/bin/python

#Library imports
import matplotlib.pyplot as plt
import numpy as np
import sys

file = str(sys.argv[1])
data = np.genfromtxt(file)

#Plotting Time History of AOA    
figure_Airfoil, axis_Airfoil = plt.subplots()
axis_Airfoil.plot(data[:,0], data[:,1], 'kx-',label='Airfoil')
axis_Airfoil.set_xlabel('x-coordinates')
axis_Airfoil.set_ylabel('y-coordinates')
axis_Airfoil.set_title('Airfoil Geometry')
axis_Airfoil.legend()
axis_Airfoil.grid()
axis_Airfoil.axis('equal')

plt.show()


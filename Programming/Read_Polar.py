#!/bin/python

#Library Imports
import numpy as np
import sys

#Arg1: The name of the data file
Data_File_Name = str(sys.argv[1])

#Read in the given data file
data = np.genfromtxt(Data_File_Name)

#What to do if data is empty
if (np.shape(data)[0]):

    #Figure out the maximum lift coefficient
    max_CL = np.max(data[:,1])

    #Print out the maximum lift coefficient
    print(max_CL ,end=' ')

    #Figure out if stall angles have been achieved
    if (max_CL > data[-1,1]):
        print('1')
    else:
        print('0')
else:
    print(0,' ',0)

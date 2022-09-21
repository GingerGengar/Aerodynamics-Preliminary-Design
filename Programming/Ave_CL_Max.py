#!/bin/python

#Library imports
import numpy as np
import sys

Input_File = str(sys.argv[1])

#Read in the data file
data = np.genfromtxt(Input_File)

#How much data points were given
Total_N = np.shape(data)[0]

#Indices of which entries are valid
valid_entries = data[:,2]>0

#How many data points are valid
Valid_N = np.shape(data[valid_entries,0])[0]

#Computation of Average Maximum Lift Coeff due to valid data points
CL_Max_Ave = np.mean(data[valid_entries, 1])

#Computation of Minimum cl_Max
CL_Max_Min = np.min(data[valid_entries, 1])

#Print out all of the various data to stdout
print(CL_Max_Min, CL_Max_Ave, Valid_N, Total_N)

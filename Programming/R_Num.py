#!/bin/python
def R_Num(U, L):
    '''U here is the velocity, enter stall speed
    L here is the length, enter target chord length'''
    rho = 1.225 #Density in kg/m^3
    mu = 1.81*10**-5 #kgm^{-1}s^{-1}
    R = (rho*U*L)/mu #Compute Reynold's Number
    return R

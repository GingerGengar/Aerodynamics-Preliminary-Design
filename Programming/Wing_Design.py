#!/bin/python

#Variable declarations
A_w = 0.903224 #Wing Area (m^2)
L_cr = 0.3556 #Wing Root Chord (m)
lambda_w = 1.0 #Taper Ratio

#Compute Tip Wing Chord
L_ct = L_cr*lambda_w

#Compute Span from Wing Area and wing Chord
b = (A_w/L_cr)*(2.0/(1.0 + lambda_w ))

#Compute Aspect Ratio of Wing
A_r = (b**2)/A_w

#Show the Wing Design
HED="#Wing Area (m^2)|Taper Ratio|Wing Root Chord (m)|Tip Root Chord (m)|Wing Span (m)|Aspect Ratio"
print(HED)
print(A_w, lambda_w, L_cr, L_ct, b, A_r)


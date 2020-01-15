//
//  Thermal Expansion lab.py
//  
//
//  Created by Ailey Robinson on 1/15/20.
//

#include "Thermal Expansion lab.h"
import numpy as np
import matplotlib.pyplot as plt

def rul3(dA, dB):
    dQ = np.sqrt(dA**2 + dB**2)
    return dQ

#if q = cA^a B^b where c, m, n are constants, then
def rul4(Q, A, dA, a, B, dB, b, C, dC, c):
    dQ = Q * np.sqrt(((a*(dA/A))**2) + ((b*(dB/B))**2) + ((c*(dC/C))**2))
    return dQ
    
l = 1.05
dl = 0.001
deltal = 0.00125
ddeltal = 0.00001
Ti = 23.4
Tf = 92.5
dTi = 0.3
dTf= 0.1

a = deltal/(l * (Tf - Ti))

dT = rul3(0.3, 0.1)

da = rul4( a, deltal, ddeltal, 1., l, dl, 1., 69.1, dT, 1. )
print('The Coefficient of Linear Expansion is', a, 'plus/minus', da)

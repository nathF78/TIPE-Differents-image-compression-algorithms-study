#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:24:19 2020

@author: nathan
"""
import numpy as np
import math 
 
def mdtc(N):
    C=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if i==0:
                C[i,j]=1/math.sqrt(N)
            else :
                C[i,j]=math.sqrt(2/N)*math.cos(((2*j+1)*i*math.pi)/(2*N))
    return(C)
         
C=mdtc(8) 
CT=np.copy(C)
np.transpose(CT) 
print(C,CT)


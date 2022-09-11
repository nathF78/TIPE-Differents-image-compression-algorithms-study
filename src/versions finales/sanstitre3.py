#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:36:10 2021

@author: nathan
"""
from PIL import Image
import numpy as np 
import RLE

A=np.zeros((8,8))

def zizag(M):
    #assert M.shape[0]==M.shape[1] #vérifions que la matrice est carrée 
    n=len(M)
    
    solution=[0]*(n*2-1)
    for i in range (n*2-1):
        solution[i]=[]
        
    for i in range(n): 
        for j in range(n): 
            a=i+j 
            if(a%2 ==0): 
      
                #add at beginning 
                solution[a].insert(0,M[i][j]) 
            else: 
      
                #add at end of the list 
                solution[a].append(M[i][j]) 
                
    return(solution)

A=zizag(A)
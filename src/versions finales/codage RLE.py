#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:23:09 2020

@author: nathan
"""
import numpy as np

def codage_RLE(M):
    F=[]
    b=0
    for i in range (len(M)):
        if M[i]==0:
            b+=1
        else :
            if b==0 :
                F.append(M[i])
            else :
                F.append("#{int}".format(int=b))
                F.append(M[i])
            b=0
    #faire ppur les elements restants 
    if b!=0 :
        F.append("#{int}".format(int=b))
    return(F)
                
def codage_RLEi(M):
    F=[]
    for i in range (len(M)):
        if "#" in str(M[i]):
            l=len(M[i])
            for i in range (int(M[i][1:l])):
                F.append(0)
        else :
            F.append(M[i])
    return(F)







TEST=[1,5,8,0,0,0,0,0,12,6,0,123,12,0]
print(TEST)
print(len(TEST))
A=np.array(codage_RLE(TEST))
print(A)
B=codage_RLEi(A)
print(B)
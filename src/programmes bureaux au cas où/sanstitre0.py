#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:23:09 2020

@author: nathan
"""
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
    return(F)
                
def codage_RLEi(M):
    F=[]
    for i in range (len(M)):
        if "#" in str(M[i]):
            for i in range (int(M[i][1])):
                F.append(0)
        else :
            F.append(M[i])
    return(F)







TEST=[1,5,8,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,6,0,123]
print(TEST)
A=codage_RLE(TEST)
print(A)
B=codage_RLEi(A)
print(B)
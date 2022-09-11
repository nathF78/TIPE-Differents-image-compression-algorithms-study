#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:44:49 2020

@author: nathan
"""

#module codage RLE
import numpy as np



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
    F=[]
    for i in solution: 
        for j in i: 
            F.append(j)
    
    return(F)

def zizagi(M):
    n=int(np.sqrt(len(M)))
    F=[]
    a=0
    for i in range (1,n+1): #jusqu'a diagonale 
        b=a+i
        F.append(M[a:b])
        a=b
    for i in range (n-1,0,-1): #après diagonale 
        b=a+i
        F.append(M[a:b])
        a=b
    for i in range (len(F)):    #inverser les listes à un indice impaire
        if (i%2!=0):
            F[i].reverse()
    print(F)
            
    A=np.zeros((n,n))
    n=len(F)
    for i in range(n//2):     #matrice finale avant diagonale 
        for j in range (len(F[i])):
            A[i-j][j]=F[i][j]
    for i in range(n//2+1):     #matrice finale après diagonale 
        for j in range (len(F[i])):
            A[n//2-(i-j)][n//2-j]=F[n-1-i][len(F[n-1-i])-1-j]  
    return(A)


def RLE(M):
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
                
def RLEi(M):
    F=[]
    for i in range (len(M)):
        if "#" in str(M[i]):
            l=len(M[i])
            for i in range (int(M[i][1:l])):
                F.append(0)
        else :
            F.append(M[i])
    return(F)

    F=[]
    for i in range (len(M)):
        if "#" in str(M[i]):
            for i in range (int(M[i][1])):
                F.append(0)
        else :
            F.append(M[i])
    return(F)
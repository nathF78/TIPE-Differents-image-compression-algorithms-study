#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:59:15 2021

@author: nathan
"""
import numpy as np
import matplotlib.pyplot as plt
import time

#implémentation manuelle de la transformée de fourrier discrète test 1 et dct 

j=complex(0,1)

def DFT(u,N,k):
    a=0
    for i in range (N):
        a+=u[i]*np.exp(-j*2*np.pi*i*k/N)
    return(a)

def DCT(u,N,k): 
    a=0
    for i in range (N):
        a+=u[i]*np.cos((np.pi/N)*(i+(1/2))*k)
    return(a)
u=[]
nb=[]
temps=[]
T=1



#plt.plot(temps,u)

F=[]
freq=[]
tempsDCT=[]
tempsDFT=[]

for N in range(200):

    for i in range(N):
        t=i*(T/N)
        temps.append((1/(2*T))*i)
        u.append(2*np.cos((2*np.pi/T)*t)+np.cos((2*np.pi*5/T)*t))
        nb.append(nb[-1]+1)
    
    t1=time.perf_counter()
    for i in range (N):
        F.append(DFT(u,N,i))
    t2=time.perf_counter()
    
    tempsDFT.append(t2-t1)
    #plt.plot(freq,np.abs(F))
    
    t1=time.perf_counter()
    FDCT=[]
    for i in range(N):
        FDCT.append(DCT(u,N,i))
    t2=time.perf_counter()
    
    tempsDCT.append(t2-t1)
    print(N)


# plt.plot(temps,np.abs(FDCT)/np.max(np.abs(FDCT)),label="DCT")
# plt.plot(np.abs(F),label="DFT")
# plt.legend(loc='upper right')
# plt.xlabel("fréquence (Hz)")
# plt.ylabel("amplitude")
# plt.xlim((0,10))

plt.plot(tempsDCT,label="temps DCT")
plt.plot(tempsDFT,label="temps DFT")
plt.legend(loc='upper right')
plt.xlabel("nombre d'échantillions")
plt.ylabel("temps de clalcul (s)")


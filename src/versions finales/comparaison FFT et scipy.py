#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:56:42 2021

@author: nathan
"""

#test temps FFT et DCT

import numpy as np
import scipy.fftpack as scifft
import numpy as np
import time
import matplotlib.pyplot as plt

u=[]
Nb=[]
nb=0
temps=[]
T=10
tempsDCT=[]
tempsFFT=[]

for N in range (1,600):
    nb+=N
    Nb.append(nb)
    for i in range(N):
        t=i*(T/N)
        temps.append(t)
        u.append(2*np.cos((2*np.pi/T)*t)+np.cos((2*np.pi*5/T)*t))
    
    t1=time.perf_counter()
    FFT=np.fft.fft(u)
    t2=time.perf_counter()
    tempsFFT.append(t2-t1)

    
    t1=time.perf_counter()
    DCT=scifft.dct(u)
    t2=time.perf_counter()
    tempsDCT.append(t2-t1)
    
    print(N)
    
plt.plot(Nb,tempsDCT,label="temps DCT")
plt.plot(Nb,tempsFFT,label="temps FFT")
plt.legend(loc='upper right')
plt.xlabel("nombre de valeurs")
plt.ylabel("temps de clalcul (s)")
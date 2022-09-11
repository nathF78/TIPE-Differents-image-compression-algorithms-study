#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:58:54 2020

@author: nathan
"""

import matplotlib.pyplot as plt
import numpy as np

def fct(t):
    return(np.cos(2*t)+6*np.cos(t)+t+np.cos(37*t))

def echantillonage(fct,a,p,N):
    X=[]
    T=[]
    i=0
    while i<=p*N:
        X.append(fct(i))
        T.append(i)
        i+=p
    return(T,X)

p=1
T,X=echantillonage(fct,0,p,255)
signal=np.fft.fft(X)
freq = np.fft.fftfreq(len(T),p)
amp=np.abs(signal)
plt.plot(freq, amp/amp.max())
plt.show()
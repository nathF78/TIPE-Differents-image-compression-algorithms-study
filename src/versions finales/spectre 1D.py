#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:03:11 2020

@author: nathan
"""

import numpy as np
import matplotlib.pyplot as plt

def passe_bas(freq,FFT,fc): 
    assert len(freq)==len(FFT)
    for i in range (len(freq)):
        if freq[i]>=fc:
            FFT[i]=0
        if freq[i]<=-fc: #ne pas oublier que la transformée de fourrier est une fct impaire
            FFT[i]=0
    return()
    
def fonction(t):
    return(t)

def FFT(F,Tech,end): #F : tableau de la fct, période echantillonage, fin echantillonage
    b=int(end/Tech)
    fft=np.fft.fft(F[0:b]) 
    amp=np.abs(fft)
    amp=np.abs(fft)/amp.max()
    axefreq = np.fft.fftfreq(len(amp),Tech)
    return(fft,amp,axefreq)

Fech=100
Tech=1/Fech
end=100
t = np.arange(0,end,Tech)
signal = 2*np.cos(2*np.pi*3*t)+np.cos(2*np.pi*8*t)

# signal=[]
# for i in range(len(t)):
#     signal.append(fonction(t[i]))

fft,amp,axef= FFT(signal,Tech,end)

plt.figure("fct")
plt.plot(t,signal,'red')
plt.xlim(0, 2)
plt.show()

plt.figure("spectre")
plt.plot(axef,amp,'red')
plt.xlim(0, 30)
plt.xlabel("f (Hz)")
plt.ylabel("amplitude")
plt.grid()
plt.show() 

#
passe_bas(axef,fft, 4)
amp=np.abs(fft)
amp=amp/amp.max()
#

plt.figure("filtrée")
plt.plot(axef,amp,'blue')
plt.xlim(0, 30)
plt.xlabel("f (Hz)")
plt.ylabel("amplitude")
plt.grid()
plt.show() 

plt.figure("final")
plt.plot(t,np.fft.ifft(fft),'blue')
plt.xlim(0, 2)
plt.show()
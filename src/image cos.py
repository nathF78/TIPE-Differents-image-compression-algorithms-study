#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:04:29 2020

@author: nathan
"""
import numpy as np 
import pylab
from PIL import Image
import numpy as np
import scipy.fftpack as scifft
import matplotlib.pyplot as plt
import scipy.fftpack as scifft



def normalize_img(IMG):
    n=len(IMG)
    norm=np.zeros((n,n),dtype=float)
    maxi=np.amax(IMG)
    mini=np.amin(IMG)
    print(maxi,mini)
    for i in range (len(IMG)):
        for j in range (len(IMG)):
            norm[i][j]=255*(IMG[i][j]-mini)/(maxi-mini)
    return(np.array(norm))

def imgcos (n):
    """
    
    
    Parameters
    ----------
    n : taille de l'image .
    Returns
    -------
    Image 

    """

    f=1/4
    IMG=np.zeros((n,n))
    for j in range (n):
        for i in range(n):
           IMG[i,j]=127*np.cos(2*np.pi*f*(j))
            # if (j//(10))==(j/10):
            #     IMG[i,j]=255
            # else:
            #         IMG[i,j]=0

    IMG= normalize_img(IMG)
    return(IMG)








IMG=imgcos(1477)
FT=np.fft.fft2(IMG)
B=FT[:]
FT=(abs(FT))**2
A=FT[:]
FTi=np.fft.ifft2(FT)
FTi=normalize_img(abs(FTi))


# new_im= Image.fromarray(IMG)
# new_im.show()

new_im= Image.fromarray(FTi)
new_im.show()

# pylab.imshow(np.abs(FT),"Dark2")
# A=normalize_img(A)
# print(np.max(A))
# new_im= Image.fromarray(A)
# new_im.show()
# new_im= Image.fromarray(B)
# new_im.show()
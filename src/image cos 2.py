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

def normalize_img(IMG):
    n=len(IMG)
    norm=[[0]*n]*n
    maxi=np.amax(IMG)
    mini=np.amin(IMG)
    for i in range (len(IMG)):
        for j in range (len(IMG)):
            norm[i][j]=255*(IMG[i][j]-maxi)/(mini-maxi)
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
    p=0.01
    f=1
    IMG=np.zeros((n,n))
    for j in range (n):
        for i in range(n):
           IMG[i,j]=abs(255*np.cos(np.pi*j/2))
           print(j)
            # if (j//(10))==(j/10):
            #     IMG[i,j]=255
            # else:
            #         IMG[i,j]=0
            
        f+=p
    IMG= normalize_img(IMG)
    return(IMG)


                
            

IMG=imgcos(1000)
A=IMG
FT=np.fft.fft2(IMG)

pylab.imshow(np.abs(FT),"Dark2")

new_im= Image.fromarray(normalize_img(np.abs(FT)))
new_im.show()
new_im= Image.fromarray(IMG)
new_im.show()
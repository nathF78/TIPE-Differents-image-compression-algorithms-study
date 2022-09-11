#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:12:22 2020

@author: nathan
"""
import numpy as np 
import pylab
from PIL import Image

#créer une image en niveau de gris avec un carré au centre 


def carré (n,c):
    """
    
    
    Parameters
    ----------
    n : taille de l'image .
    c : taille du carré .
    Returns
    -------
    Image 

    """
    assert n>=c
    l=int(n/2-c/2)
    IMG=np.zeros((n,n))
    for i in range (n):
        for j in range(n):
            if i>=l and j>=l and i<=n-l and j<=n-l:
                IMG[i,j]=255
    return(IMG)

def rectangle(n,l):
    IMG=np.zeros((n,n))
    for j in range (n//2-l//2,n//2+l//2):
        for i in range (n):
            IMG[i][j]=255
    return(IMG)






IMG=rectangle(100, 3)

pylab.imshow(IMG,"Dark2")

new_im= Image.fromarray(IMG)
new_im.show()
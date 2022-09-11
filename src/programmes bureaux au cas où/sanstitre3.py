#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:54:42 2021

@author: nathan
"""

import scipy.fftpack as scifft
from PIL import Image 
import numpy as np

imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/cos(f10).png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc_petit.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/points.png")
img = np.array(imgo) #met l'image sous la forme d'une matrice
#r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
#img=0.2989*r + 0.5870*g + 0.1140*b 
n,c =img.shape
#

#mise de l'image sous forme carré de taille (k*8)*(k*8)
if n>=c:
    img=img[:(c//8)*8,:(c//8)*8]
else :
    img=img[:(n//8)*8,:(n//8)*8]
    
    
A=scifft.fft2(img)
B=np.abs(A)
C=scifft.ifft2(B)
C=np.real(C)
C=(C/np.max(C))*255
new_im = Image.fromarray(C)
new_im.show()

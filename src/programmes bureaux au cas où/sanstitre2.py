#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:46:37 2020

@author: nathan
"""

import bloc
import RLE
from PIL import Image 
import numpy as np
import PSNR


# img=np.zeros((8,8))
# for i in range (0,8):
#     for j in range (0,8):
#         img[i][j]=(randint(1, 255))
    
#mise des coeff de l'image sous forme de matrice 
#imgo = Image.open(r"/Users/nathan/stinkbug.png")
imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc.png")
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
    
#img = np.array([[1,2,3,4,16,17,18,19],[6,7,8,9,16,17,18,19],[11,12,13,14,16,17,18,19],[16,17,18,19,16,17,18,19],[16,17,18,19,16,17,18,19],[16,17,18,19,16,17,18,19],[16,17,18,19,16,17,18,19],[16,17,18,19,16,17,18,19]])

def compressionDCT(mDCT): #utilise la manière au choix de compresser les sous matrices 8*8
    #suppression de tous les coeff à la moitié de la matrice 
    n=len(mDCT)
    p=5
    p=n-p
    for i in range (0,n):
        for j in range (p,n):
            mDCT[i,j]=0
    for j in range (0,n):
        for i in range (p,n):
            mDCT[i,j]=0
                     
def compressionFT(mFT):
    p=5
    p=int(p/2)
    n=len(mFT)
    m=int(n/2)
    for i in range (m-int(p),m+int(p)):
        for j in range (n):
            mFT[i][j]=0
    for j in range (m-int(p),m+int(p)):
        for i in range (n):
            mFT[i][j]=0
    return(mFT)

def rien(A):
    return(A)
    

DC=bloc.DCT(img, compressionDCT)

A=DC
B=RLE.zizag(DC)
C=RLE.RLE(B)

new_im = Image.fromarray(DC)
new_im.show()









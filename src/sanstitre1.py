#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:59:30 2021

@author: nathan
"""

import numpy as np
import pylab
from PIL import Image

def matriceImageLog(matrice,rgb):
    s = matrice.shape
    m = np.log10(1+matrice)
    min = m.min()
    max = m.max()
    m = (m-min)/(max-min)
    im = np.zeros((s[0],s[1],3),dtype=float)
    im[:,:,0] = rgb[0]*m
    im[:,:,1] = rgb[1]*m
    im[:,:,2] = rgb[2]*m
    return im
             

#mise des coeff de l'image sous forme de matrice 
#imgo = Image.open(r"/Users/nathan/stinkbug.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc_petit.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/imageA.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/cos(f10).png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/cos_vertical(f5).png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/test.PNG") 
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/cos(3 et 8hz).PNG") 
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/points.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/plotE.png")
imgo = Image.open(r"/Users/nathan/Desktop/IMG_1766 2.PNG")
img = np.array(imgo) #met l'image sous la forme d'une matrice
r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
img=0.2989*r + 0.5870*g + 0.1140*b 

n,c =img.shape
#

def normalize_img(IMG):
    norm=np.zeros((IMG.shape),dtype=float)
    maxi=np.amax(IMG)
    mini=np.amin(IMG)
    print(maxi,mini)
    for i in range (len(IMG)):
        for j in range (len(IMG)):
            norm[i][j]=255-255*(maxi-IMG[i][j])/(maxi-mini)
    return(np.array(norm))





fttimage = np.fft.fftshift(np.fft.fft2(img))
fttimage=np.abs(fttimage)
# fttimage=normalize_img(fttimage)
A=matriceImageLog(fttimage,[255,0,0])

new_im= Image.fromarray(A[:,:,0])
new_im.show()


(Ny,Nx) = A[:,:,0].shape
fxm = Nx*1.0/(2*Nx)
fym = Ny*1.0/(2*Ny)
pylab.imshow(A[:,:,0],"Greys",extent=[-fxm,fxm,-fym,fym])
pylab.xlabel("fx")
pylab.ylabel("fy")
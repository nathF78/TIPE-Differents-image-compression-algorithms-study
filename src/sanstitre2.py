#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:41:54 2020

@author: nathan
"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
import matplotlib.image as mpimg 
import math
from matplotlib import cm


def mdtc(N): #permet de créer la matrice dtc 
    C=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if i==0:
                C[i,j]=1/math.sqrt(N)
            else :
                C[i,j]=math.sqrt(2/N)*math.cos(((2*j+1)*i*math.pi)/(2*N))
    return(C)
         
#mise des coeff de l'image sous forme de matrice 
imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc.png")
img = np.array(imgo)

#
#Pb Z n'est pas carré (à résoudre)
img = np.delete(img, 1, 1)
img = np.delete(img, 1, 1)
img = np.delete(img, 1, 1)
#a résoudre
n,c =img.shape

#initialisation DCT
C=mdtc(n) 
CT=np.copy(C)
np.transpose(CT) #(inverse mais comme C ortogonale la tC=invC), a faire manuellement sans np

#caclul DCT
matrice_DCT=C = C.dot(img).dot(CT)

#mise en place des axes X et Y
x=np.linspace(0,c-1,c)
y=np.linspace(0,n-1,n)
X,Y=np.meshgrid(x,y)
#

#graph image originale
figo=plt.figure()
original = figo.add_subplot(111, projection='3d')
original.plot_surface(X,Y,img, cmap=cm.coolwarm)
#

#graph image après DTC (domaine temporel)
figf = plt.figure()
final = figf.add_subplot(111, projection='3d')
final.set_zlim(-500, 500) #met une limite pour avoir un graph plus adapté (coeff très grand devant)
final.plot_surface(X,Y,matrice_DCT, cmap=cm.coolwarm)
#
plt.show()

#caclul DCT inverse 
matrice_DCTI=CT.dot(matrice_DCT).dot(C)


#affcher image finale
new_im = Image.fromarray(matrice_DCTI)
new_im.show()










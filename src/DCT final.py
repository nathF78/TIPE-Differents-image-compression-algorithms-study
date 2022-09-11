#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:41:54 2020

@author: nathan
"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm



def mdct(n): #permet de créer la matrice dtc (matrice de changement de base)
    C=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i==0:
                C[i,j]=1/np.sqrt(n)
            else :
                C[i,j]=np.sqrt(2/n)*np.cos((np.pi*i*(1/2+j))/n)
    return(C)

def transpose(M): #a faire manuellement 
    CT=np.copy(M)
    np.transpose(CT) #(inverse mais comme C ortogonale la tC=invC), a faire manuellement sans np
    return(CT)

def compression(mDCT): #utilise la manière au choix de compresser les sous matrices 8*8
    #suppression de tous les coeff à la moitié de la matrice 
    n=len(mDCT)
    for i in range (0,n):
        for j in range (4,n):
            mDCT[i,j]=0
    for j in range (0,4):
        for i in range (4,n):
            mDCT[i,j]=0
    #
    # #TEST supression du 1er coeff
    #mDCT[0,0]=0
    # #

    return()

def add_matrix(M,n,c,m,p1,p2): #injecte les sous matrices de taille p1*p2 dans la matrice de taille n*c
    for i in range (p1):
        for j in range (p2):
            M[n+i,c+j]=round(m[i,j])
    return()
            
def add_matrix_rounded(M,n,c,m,p1,p2): #pareil que add_matrix mais arrondi et supprime les coeff <0
    for i in range (p1):
        for j in range (p2):
            if m[i,j] >= 0 :
                M[n+i,c+j]=round(m[i,j])
            else :
                 M[n+i,c+j]=0            
    return()

def DCT_bloc(M): #applique la DCT à des blocs de 8*8 Attention ne marche que avec des matrices de taille mutiples de 8 (n*8) !
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y))
    q=x//8
    r=x%8
    #pour les blocs de 8
    p=8
    C=mdct(8)
    CT=np.transpose(C)
    for i in range (q): #def la sous 
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mDCT=C.dot(m).dot(CT) #calcul de sa DCT (domaine fréquentiel)
            compression(mDCT) #compression selon la methode utilisé dans la fct 
            add_matrix(F, n, c, mDCT, p,p) #ajout dans la matrice finale 
    #pour les blocs restants 
    #pour les matrices de taille r*8
    # i=8*q 
    # for j in range (q-1): #on ne prend pas la dernière sous matrice de taille r*r
    #         c=j*8 #def le debut de la colonne la sous matrice à prendre
    #         m=M[i:i+r,c:c+8]#sous matrice de taille r*8
    #         mDCT=C.dot(m).dot(CT) #calcul de sa DCT (domaine temporel)
    #         compression(mDCT) #compression selon la methode utilisé dans la fct 
    #         mDCTi=CT.dot(mDCT).dot(C) #remise dans le domaine spatial
    #         add_matrix(F, n, c, mDCTi,r,8) #ajout dans la matrice finale 
    #ne marche pas 
    return(F)
         
def DCTi_bloc(M): #applique la DCT inverse à des blocs de 8*8 Attention ne marche que avec des matrices de taille mutiples de 8 (n*8) !
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y))
    q=x//8
    r=x%8
    p=8
    C=mdct(8)
    CT=np.transpose(C)
    for i in range (q): #def la sous 
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mDCTi=CT.dot(m).dot(C) #calacul de sa DCT inverseremise dans le domaine spatial
            add_matrix_rounded(F, n, c, mDCTi, p,p) #ajout dans la matrice finale 
    return(F)

#mise des coeff de l'image sous forme de matrice 
imgo = Image.open(r"/Users/nathan/stinkbug.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc_petit.png")
img = np.array(imgo) #met l'image sous la forme d'une matrice
n,c =img.shape
#

#mise de l'image sous forme carré de taille (k*8)*(k*8)
if n>=c:
    img=img[:(c//8)*8,:(c//8)*8]
else :
    img=img[:(n//8)*8,:(n//8)*8]
#

imDCT=DCT_bloc(img)
imDCTi=DCTi_bloc(imDCT)

#affcher image finale
new_im = Image.fromarray(imDCTi)
new_im.show()

#DCT totale
n,c =img.shape
C=mdct(n)
CT=np.transpose(C)
total_DCT=C.dot(img).dot(CT)

new_im_total_DCT = Image.fromarray(total_DCT)
new_im_total_DCT.show()


l=imDCT.tolist()
plt.hist(np.ravel(imDCT), bins="auto",range=(-25,25),histtype='bar',density='true')
plt.plot()

# plt.hist(np.ravel(total_DCT), bins="auto",range=(-25,25),histtype='bar',density='true')
# plt.plot()


##permet de voir la différence entre l'image ds le domaine spatial et fréquentiel 
# #mise en place des axes X et Y
# x=np.linspace(0,c-1,c)
# y=np.linspace(0,n-1,n)
# X,Y=np.meshgrid(x,y)
# #

# #graph image originale
# figo=plt.figure()
# original = figo.add_subplot(111, projection='3d')
# original.plot_surface(X,Y,img, cmap=cm.coolwarm)
# #

# #graph image après DTC (domaine temporel)
# figf = plt.figure()
# final = figf.add_subplot(111, projection='3d')
# final.set_zlim(-500, 500) #met une limite pour avoir un graph plus adapté (coeff très grand devant)
# final.plot_surface(X,Y,imDCT, cmap=cm.coolwarm)
# #
# plt.show()
##














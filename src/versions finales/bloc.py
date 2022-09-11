#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:40:15 2020

@author: nathan
"""

#module transformée en bloc 

import numpy as np
import scipy.fftpack as scifft



def add_matrix(M,n,c,m,p1,p2):  #injecte les sous matrices de taille p1*p2 
                                #dans la matrice M à partir de l'indice (n,c)
    for i in range (p1):
        for j in range (p2):
            M[n+i][c+j]=np.copy(m[i,j])
    return()

def add_matrix_rounded(M,n,c,m,p1,p2):  #pareil que add_matrix mais arrondi 
    for i in range (p1):                #et supprime les coeff <0
        for j in range (p2):
            if np.abs(m[i,j]) >= 0 :
                M[n+i][c+j]=np.abs(np.round(m[i,j]))
            else :
                 M[n+i,c+j]=0            
    return()

def DCT(M,compressionDCT): #applique la DCT à des blocs de 8*8 d'une matrice M
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y),dtype=np.complex128)
    q=x//8
    #pour les blocs de 8
    p=8 
    for i in range (q): #def la sous matrice
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mDCT=scifft.dctn(m,norm = 'ortho') #calcul de sa DCT 
            mDCT=compressionDCT(mDCT) #compression selon la fct 
            add_matrix(F, n, c, mDCT, p,p) #ajout dans la matrice finale 
            
    return(F)

def DCTi(M): #applique la DCT inverse à des blocs de 8*8 d'une matrice M
    x,y =M.shape    
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y))
    q=x//8
    #r=x%8
    p=8
    for i in range (q): #def la sous matrice
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mDCTi=scifft.idctn(m,norm = 'ortho') #calcul de sa DCT inversere
            add_matrix_rounded(F, n, c, mDCTi, p,p) #ajout dans matrice finale 
    return(F)

def FT(M,compressionFT):  #applique la DFT à des blocs de 8*8 d'une matrice M
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y),dtype=np.complex128)
    q=x//8
    #r=x%8
    #pour les blocs de 8
    p=8 
    for i in range (q): #def la sous matrice
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=np.copy(M[n:n+8,c:c+8])#sous matrice de taille 8*8
            mFT=np.fft.fft2(m) #calcul de sa DFT (domaine fréquentiel)
            #np.fft.fftshift(mFT)
            mFT=compressionFT(mFT) #compression selon la fct 
            add_matrix(F, n, c, mFT, p,p) #ajout dans la matrice finale 
    return(F)

def FTi(M):     #applique la DFT inverse à des blocs de 8*8 d'une matrice M
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y),dtype=np.complex128)
    q=x//8
    #r=x%8
    p=8
    for i in range (q): #def la sous matrice
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mFTi=np.real(np.fft.ifft2(m)) #calacul de sa DFT inverse
            #np.fft.ifftshift(mFTi)
            add_matrix_rounded(F, n, c, mFTi, p,p) #ajout dans la matrice finale 
    F=np.real(F)
    return(F)    


def normalize_img(IMG): #normalise les valeurs des coeff et les code sur 8bits
    norm=np.zeros((IMG.shape),dtype=float)
    maxi=np.amax(IMG)
    mini=np.amin(IMG)
    print(maxi,mini)
    for i in range (len(IMG)):
        for j in range (len(IMG)):
            norm[i][j]=int(255-255*(maxi-IMG[i][j])/(maxi-mini))
    return(np.array(norm))
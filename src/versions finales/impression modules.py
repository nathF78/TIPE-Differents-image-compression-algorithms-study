#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Nathan Foucher N°:17225
"""

# =============================================================================
# module transformée en bloc 
# =============================================================================

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

def filtre_coupe_bande_horiz(fft,fi,ff): #fi: freq finitiale #ff : freq finale
    n=fft.shape[1]
    for j in range (n//2,n):
        if (j-n//2)/n > fi and (j-n//2)/n<ff:
            for i in range (fft.shape[0]) :
                fft[i][j]=0
                fft[i][-j]=0
    return(fft)


# =============================================================================
# module PSNR 
# =============================================================================

import numpy as np 
  
def PSNR(original, compressed): 
    mse = np.mean((original - compressed) ** 2) #calcul la moyenne des diffs
    if(mse == 0):  # MSE=0 si il n'y a pas de bruit dans le signal
        return 100  #dans ce cas rien ne sert de calculer le PSNR
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse)) 
    return psnr 

# =============================================================================
# module codage RLE
# =============================================================================
import numpy as np


def zigzag(M):
    #assert M.shape[0]==M.shape[1] #vérifions que la matrice est carrée 
    n=len(M)
    
    sections=[0]*(n*2-1)
    for i in range (n*2-1):
        sections[i]=[]
        
    for i in range(n): 
        for j in range(n): 
            a=i+j 
            if(a%2 ==0): 
      
                #ajout au début
                sections[a].insert(0,M[i][j]) 
            else: 
      
                #ajout à la fin de la liste
                sections[a].append(M[i][j]) 
    F=[]
    for i in sections: 
        for j in i: 
            F.append(j)
    return(F)

def zigzagi(M):
    n=int(np.sqrt(len(M)))
    F=[]
    a=0
    #création d'un tableau contenant les listes diagonales
    for i in range (1,n+1): #jusqu'a diagonale 
        b=a+i
        F.append(M[a:b])
        a=b
    for i in range (n-1,0,-1): #après diagonale 
        b=a+i
        F.append(M[a:b])
        a=b
    for i in range (len(F)):    #inverser les listes à un indice impaire
        if (i%2!=0):
            F[i].reverse()
   #ajout des listes dans la mtrice finale 
    A=np.zeros((n,n),dtype=complex)
    n=len(F)
    for i in range(n//2):     #matrice finale avant diagonale 
        for j in range (len(F[i])):
            A[i-j][j]=F[i][j]
    for i in range(n//2+1):     #matrice finale après diagonale 
        for j in range (len(F[i])):
            A[n//2-(i-j)][n//2-j]=F[n-1-i][len(F[n-1-i])-1-j]  
    return(A)


def RLE(M):
    F=[]
    b=0
    for i in range (len(M)):
        if M[i]==0:
            b+=1
        else :
            if b==0 :
                F.append(M[i]) #si pas de 0 on ajoute la valeur 
            else :
                F.append("#{int}".format(int=b)) # rajoute#nb de 0
                F.append(M[i])
            b=0
    #faire pour les elements restants 
    if b!=0 :
        F.append("#{int}".format(int=b))
    return(F)
                
def RLEi(M):
    F=[]
    for i in range (len(M)):
        if "#" in str(M[i]):
            l=len(M[i])
            for i in range (int(M[i][1:l])):
                F.append(0)
        else :
            F.append(M[i])
    return(F)

    F=[]
    for i in range (len(M)):
        if "#" in str(M[i]):
            for i in range (int(M[i][1])):
                F.append(0)
        else :
            F.append(M[i])
    return(F)
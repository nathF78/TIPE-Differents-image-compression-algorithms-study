#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:41:54 2020

@author: nathan
"""


from PIL import Image
import numpy as np
import scipy.fftpack as scifft
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
import time






def zizag(M):
    #assert M.shape[0]==M.shape[1] #vérifions que la matrice est carrée 
    n=len(M)
    
    solution=[0]*(n*2-1)
    for i in range (n*2-1):
        solution[i]=[]
        
    for i in range(n): 
        for j in range(n): 
            a=i+j 
            if(a%2 ==0): 
      
                #add at beginning 
                solution[a].insert(0,M[i][j]) 
            else: 
      
                #add at end of the list 
                solution[a].append(M[i][j]) 
    F=[]
    for i in solution: 
        for j in i: 
            F.append(j)
    
    return(F)

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
        for j in range (6,n):
            mDCT[i,j]=0
    for j in range (0,6):
        for i in range (6,n):
            mDCT[i,j]=0
    #
    # #TEST supression du 1er coeff
    #mDCT[0,0]=0
    # #

    return()

def add_matrix(M,n,c,m,p1,p2): #injecte les sous matrices de taille p1*p2 dans la matrice de taille n*c
    for i in range (p1):
        for j in range (p2):
            M[n+i,c+j]=np.round(np.real((m[i,j])))
    return()
            
def add_matrix_rounded(M,n,c,m,p1,p2): #pareil que add_matrix mais arrondi et supprime les coeff <0
    for i in range (p1):
        for j in range (p2):
            if m[i,j] >= 0 :
                M[n+i,c+j]=np.round(m[i,j])
            else :
                 M[n+i,c+j]=0            
    return()

def DCT_bloc(M): #applique la DCT à des blocs de 8*8 Attention ne marche que avec des matrices de taille mutiples de 8 (n*8) !
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y))
    q=x//8
    #r=x%8
    #pour les blocs de 8
    p=8 
    for i in range (q): #def la sous 
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mDCT=scifft.dct(m,norm = 'ortho') #calcul de sa DCT (domaine fréquentiel)
            compression(mDCT) #compression selon la methode utilisé dans la fct 
            add_matrix(F, n, c, mDCT, p,p) #ajout dans la matrice finale 

    return(F)
         
def DCTi_bloc(M): #applique la DCT inverse à des blocs de 8*8 Attention ne marche que avec des matrices de taille mutiples de 8 (n*8) !
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y))
    q=x//8
    #r=x%8
    p=8
    for i in range (q): #def la sous 
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mDCTi=scifft.idct(m,norm = 'ortho') #calacul de sa DCT inverseremise dans le domaine spatial
            add_matrix_rounded(F, n, c, mDCTi, p,p) #ajout dans la matrice finale 
    return(F)

def FT_bloc(M):
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y))
    q=x//8
    #r=x%8
    #pour les blocs de 8
    p=8 
    for i in range (q): #def la sous 
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mFT=np.fft.fft2(m) #calcul de sa DCT (domaine fréquentiel)
            #np.fft.fftshift(fftimage)
            #compression(mFT) #compression selon la methode utilisé dans la fct 
            add_matrix(F, n, c, mFT, p,p) #ajout dans la matrice finale 
    return(F)

def FTi_bloc(M):
    x,y =M.shape
    assert x==y #vérifie que l'image est bien carrée 
    F=np.zeros((x,y))
    q=x//8
    #r=x%8
    p=8
    for i in range (q): #def la sous 
        n=i*8 #def le debut de la ligne la sous matrice à prendre
        for j in range (q): 
            c=j*8 #def le debut de la colonne la sous matrice à prendre
            m=M[n:n+8,c:c+8]#sous matrice de taille 8*8
            mFTi=np.real(np.fft.ifft2(m)) #calacul de sa DCT inverseremise dans le domaine spatial
            add_matrix_rounded(F, n, c, mFTi, p,p) #ajout dans la matrice finale 
    return(F)    



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
#
t1=time.process_time()
imDCT=DCT_bloc(img)
t2=time.process_time()
temps_compression = t2-t1
print("temps de compression DCT :",temps_compression)
imDCTi=DCTi_bloc(imDCT)
t3=time.process_time()
temps_decompression=t3-t2
print("temps de décompression DCT :",temps_decompression)

#affcher image finale
new_im = Image.fromarray(imDCTi)
new_im.show()

#FT 
t4=time.process_time()
imFT=FT_bloc(img)
t5=time.process_time()
temps_compression = t5-t4
print("temps de compression FT :",temps_compression)
imFTi=FTi_bloc(imFT)
t6=time.process_time()
temps_decompression=t6-t5
print("temps de décompression FT :",temps_decompression)

#affcher image finale
new_im = Image.fromarray(imFTi)
new_im.show()


#DCT totale
# n,c =img.shape
# C=mdct(n)
# CT=np.transpose(C)
# total_DCT=scifft.dct(img)

# new_im_total_DCT = Image.fromarray(total_DCT)
# new_im_total_DCT.show()

#DCTi de l'image totale 

# DCTi=total_DCT
#compression(DCTi)
# total_DCTi=scifft.dct(total_DCT)
# new_im_total_DCTi = Image.fromarray(total_DCTi)
# new_im_total_DCTi.show()




# l=imDCT.tolist()
# plt.hist(np.ravel(imDCT), bins="auto",range=(-25,25),histtype='bar',density='true')
# plt.plot()

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














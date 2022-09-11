#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:40:54 2021

@author: nathan
"""

import bloc
import RLE
from PIL import Image 
import numpy as np
import PSNR
import time
import matplotlib.pyplot as plt

# img=np.zeros((8,8))
# for i in range (0,8):
#     for j in range (0,8):
#         img[i][j]=(randint(1, 255))
    
#mise des coeff de l'image sous forme de matrice 
#imgo = Image.open(r"/Users/nathan/stinkbug.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/versions finales/cos(3 et 8hz).PNG")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc_petit.png")
#imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/points.png")
imgo = Image.open(r"/Users/nathan/Documents/Prépa/PSI/TIPE/Python/lena_gray.bmp")
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
                
    return(solution)

def compressionDCT(mDCT): #utilise la manière au choix de compresser les sous matrices 8*8
    #suppression de tous les coeff à la moitié de la matrice 
    n=len(mDCT)
    p=7
    p=n-p
    for i in range (0,n):
        for j in range (p,n):
            mDCT[i,j]=0
    for j in range (0,n):
        for i in range (p,n):
            mDCT[i,j]=0
            
def compressionmutu(m,p): #utilise la manière au choix de compresser les sous matrices 8*8
    #suppression de tous les coeff à la moitié de la matrice 
    n=len(m)*2-1 #max p=8*2
    m=zizag(m)
    for i in range (n-1,n-p-1,-1):
        m[i]=[0]*len(m[i])
        F=[]
    for i in m: 
        for j in i: 
            F.append(j)
    print(F)
    F=RLE.zizagi(F)
    return(F)


                     
def compressionFT(mFT):
    p=6
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

PSNRft=[]
PSNRdct=[]
tempsft=[]
tempsdct=[]
tempsdft=[]
tempsddct=[]
P=[]

P.append(0)
t1=time.perf_counter()
DCT=bloc.DCT(img, rien)
A=DCT
DCT=RLE.zizag(DCT)
DCT=RLE.RLE(DCT)
tempsdct.append(time.perf_counter()-t1)
t1=time.perf_counter()
DCT=RLE.RLEi(DCT)
DCT=RLE.zizagi(DCT)
imDCTf=bloc.DCTi(DCT)
tempsddct.append(time.perf_counter()-t1) #decompression faite 
PSNRdct.append(PSNR.PSNR(img,imDCTf))
print("temps DCT :",tempsdct)
print("PSNR DCT: ",PSNRdct)

t1=time.perf_counter()
FT=bloc.FT(img, rien)
FT=RLE.zizag(FT)
FT=RLE.RLE(FT)
tempsft.append(time.perf_counter()-t1)
t1=time.perf_counter()
FT=RLE.RLEi(FT)
FT=RLE.zizagi(FT)
imTf=bloc.FTi(FT)
tempsdft.append(time.perf_counter()-t1)
PSNRft.append(PSNR.PSNR(img,imTf))
print("temps FT :",tempsft)
print("PSNR FT: ",PSNRft)
a=8
new_im = Image.fromarray(imDCTf)
new_im.show()
new_im = Image.fromarray(imTf)
new_im.show()
for p in range (11,12):
    def compressionp(m):
        return(compressionmutu(m,p))
    
    if p<=7:
        P.append(P[len(P)-1]+p)
    else :
        P.append(P[len(P)-1]+a)
        a=a-1
    
    t1=time.perf_counter()
    DCT=bloc.DCT(img, compressionp)
    A=DCT
    DCT=RLE.zizag(DCT)
    DCT=RLE.RLE(DCT)
    tempsdct.append(time.perf_counter()-t1) #compression faite 
    t1=time.perf_counter()
    DCT=RLE.RLEi(DCT)
    DCT=RLE.zizagi(DCT)
    imDCTf=bloc.DCTi(DCT)
    tempsddct.append(time.perf_counter()-t1) #decompression faite 
    PSNRdct.append(PSNR.PSNR(img,imDCTf))
    print("temps DCT :",tempsdct )
    print("PSNR DCT: ",PSNRdct)
    
    t1=time.perf_counter()
    FT=bloc.FT(img, compressionp)
    FT=RLE.zizag(FT)
    FT=RLE.RLE(FT)
    tempsft.append(time.perf_counter()-t1)
    t1=time.perf_counter()
    FT=RLE.RLEi(FT)
    FT=RLE.zizagi(FT)
    imTf=bloc.FTi(FT)
    tempsdft.append(time.perf_counter()-t1)
    PSNRft.append(PSNR.PSNR(img,imTf))
    print("temps FT :",tempsft )
    print("PSNR FT: ",PSNRft)
    
    #new_im = Image.fromarray(imDCTf)
    #new_im = Image.fromarray(imDCTf)
    #new_im=new_im.convert("RGB")
    #new_im.save("/Users/nathan/Documents/Prépa/PSI/TIPE/Python/versions finales/compression/hey#{int}.jpg".format(int=P[len(P)-1]*100/64))
    new_im = Image.fromarray(imTf)
    new_im.show()
# PSNRft=PSNRft[1:]
# PSNRdct=PSNRdct[1:]
# tempsft=tempsft[1:]
# tempsdct=tempsdct[1:]
# tempsdft=tempsdft[1:]
# tempsddct=tempsddct[1:]
# P=P[1:]




# new_im = Image.fromarray(imDCTf)
# new_im.show()
# new_im = Image.fromarray(imTf)
# new_im.show()
# P=np.multiply(P,100/64)
# plt.figure(0)
# plt.plot(P,PSNRdct,label="PSNR DCT (dB)")
# plt.plot(P,PSNRft,label="PSNR FFT (dB)")
# plt.plot(P,[30]*(len(P)),":r")
# plt.legend(loc='upper right')
# plt.xlabel("taux de compression(%)")
# plt.ylabel("PSNR (dB)")
# plt.figure(1)
# plt.plot(P,tempsdct,label="temps compression dct")
# plt.plot(P,tempsft,label="temps compression fft")
# plt.legend(loc='upper right')
# plt.xlabel("taux de compression(%)")
# plt.ylabel("temps (s)")
# plt.figure(2)
# plt.plot(P,tempsddct,label="temps décompression dct")
# plt.plot(P,tempsdft,label="temps décompression fft")
# plt.legend(loc='upper right')
# plt.xlabel("taux de compression(%)")
# plt.ylabel("temps (s)")
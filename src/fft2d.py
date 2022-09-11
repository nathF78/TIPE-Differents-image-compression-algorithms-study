#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:13:43 2020

@author: nathan
"""

import numpy as np
import pylab
from PIL import Image

def delete_inf(A):
    n,c=np.shape(A)
    for i in range (n):
        for j in range (c):
            if A[i,j] >= 10000000 :
                A[i,j]=0
    return(A)

def normalize_img(IMG):
    
    IMG=IMG/np.max(IMG)
    IMG=IMG*255
    #supprime les valeurs négatives
    IMG=IMG/2
    IMG=IMG+254/2
    #
    IMG=np.around(IMG)
    IMG=255-IMG
    return(IMG)

def passe_bas_horizontale(freq,FFT,fc): 
    for i in range (len(freq)):
        if freq[i]>=fc:
            for j in  range (len(FFT)):
                FFT[j,i]=0
        if freq[i]<=-fc: #ne pas oublier que la transformée de fourrier est une fct impaire
            for j in  range (len(FFT)):
                FFT[j,i]=0
    return()
        
def passe_bas_verticale(freq,FFT,fc): 
    for i in range (len(freq)):
        if freq[i]>=fc:
            for j in  range (len(FFT)):
                FFT[i,j]=0
        if freq[i]<=-fc: #ne pas oublier que la transformée de fourrier est une fct impaire
            for j in  range (len(FFT)):
                FFT[i,j]=0
    return()
        

def afficher_fft(fftimage,log):
    fftimage1 = np.copy(np.fft.fftshift(fftimage)) #centre la TF (ne pas oublier de faire shift inverse)
    amp=np.abs(fftimage1)
    amp=np.abs(fftimage1)/amp.max()
    if log==True: 
        amp=np.log10(amp)
    pylab.imshow(amp,"Greys",extent=[-0.5,0.5,-0.5,0.5])
    pylab.xlabel("fx")
    pylab.ylabel("fy")
    if log != True :#donne aussi une image de la FFT en sortie 
        amp=normalize_img(amp)
        new_im= Image.fromarray(amp)
        new_im.show()

def afficher_ifft(fftimage): #fonctionne ssi echelle log n'a pas été activée 
    ifftimage = np.copy(np.real(np.fft.ifft2(fftimage)))
    new_im= Image.fromarray(ifftimage)
    new_im.show()


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
imgo = Image.open(r"/Users/nathan/Desktop/rectangle.PNG")
img = np.array(imgo) #met l'image sous la forme d'une matrice
#r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
#img=0.2989*r + 0.5870*g + 0.1140*b 
n,c =img.shape
#

fttimage = np.fft.fft2(img)
axefreq = np.fft.fftfreq(len(fttimage),1)
#afficher_fft(fttimage,True)

fc=0.02
#passe_bas_horizontale(axefreq,fttimage,fc)
#passe_bas_verticale(axefreq,fttimage,fc)
afficher_fft(fttimage,False)
afficher_ifft(fttimage)








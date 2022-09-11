#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 09:24:15 2020

@author: nathan
"""

import numpy as np 
  
def PSNR(original, compressed): 
    mse = np.mean((original - compressed) ** 2) #calcul la moyenne des diffs
    if(mse == 0):  # MSE=0 si il n'y a pas de bruit dans le signal
        return 100  #dans ce cas rien ne sert de calculer le PSNR
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse)) 
    return psnr 
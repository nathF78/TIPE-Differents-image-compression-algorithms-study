#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:11:06 2021

@author: nathan
"""

import PSNR
from PIL import Image 
import numpy as np

img1 = Image.open("/Users/nathan/Desktop/hey.png")
img2=Image.open("/Users/nathan/Desktop/tmpjvtapgb1.PNG")

img1 = np.array(img1)
img2 = np.array(img2)
img2=img2[:1000,:1000]

print(PSNR.PSNR(img1, img2))
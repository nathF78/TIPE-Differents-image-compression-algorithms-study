# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:15:55 2020

@author: nathan
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm



im_1 = Image.open(r"/Users/nathan/Documents/Prépa/MPSI/Info/Tp/Tp 6/noir_et_blanc.png")
Z = np.array(im_1)
print(Z)
n,c =Z.shape
print(n,c)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=np.linspace(0,c-1,c)
y=np.linspace(0,n-1,n)

X,Y=np.meshgrid(x,y)



ax.plot_surface(X,Y,Z, cmap=cm.coolwarm)
plt.show()
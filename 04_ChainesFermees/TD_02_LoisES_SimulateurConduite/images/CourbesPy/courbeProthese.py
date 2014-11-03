# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 22:23:15 2014
Tracé de courbes relatif au sujet de concours Mines Ponts 2013 :
Prothèse active transtibiale

@author: Xavier Pessoles
"""
import matplotlib.pyplot as plt
import numpy as np
#plt.close(all)

a=0.117
b=0.039
x=linspace(-25,15,200)
plt.plot(x,1000.*sqrt(b*b+a*a+2*a*b*sin(x*math.pi/180)))
plt.ylabel("Course du vérin $\\lambda$ (en mm)")
plt.xlabel("Angle $\\alpha$ (en degrés)")
plt.grid()
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:20:53 2024

@author: Juan Puyo
"""

import numpy as np
from linregress_w import linregress_w as linr
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y= np.array([2,4,6,8,10])
dy= np.array([0.5,0.7,0.5,0.4,0.8])


lin_reg = linr(x,y,dy)


f= lambda x: lin_reg.slope()*x+lin_reg.intercept()

x_p= np.linspace(min(x),max(x),500)

plt.scatter(x,y,c="r")
plt.grid()
plt.errorbar(x, y, yerr= dy, linestyle="")

plt.plot(x_p,f(x_p),c="k",linestyle="--")

print(lin_reg.slope(),"$\pm$",lin_reg.err_slope(),"\n",lin_reg.intercept(),
      "$\pm$",lin_reg.err_intercept())



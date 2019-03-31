# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 01:03:40 2018

@author: jian
"""

import numpy as np
import matplotlib.pyplot as plt
steps=10

disOrder=np.zeros(10)

for i in range(10):
    disOrder[i]=2.0*(4.0/2.0)**(i*1.0/(steps-1))
print(disOrder)


for i in [16,32,48]:
    s=np.load("data3Log"+str(i)+".npy")*i**0
    plt.semilogx(disOrder,s,'.-')

plt.xlabel("disorder strength $\delta J$",fontsize=20)
plt.ylabel("$ \chi_{SG} /L^{  } $",fontsize=20)
#plt.legend(["8","10","12","14","16"],loc=4)

plt.show()



for i in [16,32,48]:
    s=np.load("data3Log"+str(i)+".npy")*i**0
    plt.plot(disOrder,s,'.-')

plt.xlabel("disorder strength $\delta J$",fontsize=20)
plt.ylabel("$ \chi_{SG} /L^{2} $",fontsize=20)
plt.legend(["8","10","12","14","16"],loc=4)

plt.show()
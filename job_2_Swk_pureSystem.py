# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:35:30 2018

@author: wangj
"""

from hamiltonian import *
from PPFtfim import *
import matplotlib.pyplot as plt


M=simplePureHamiltonian(20,1,1,0)
plt.matshow(M)
plt.colorbar()
plt.show()

t=tfim(M)
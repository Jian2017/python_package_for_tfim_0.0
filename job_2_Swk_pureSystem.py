# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:35:30 2018

@author: wangj
"""

from hamiltonian import *
from PPFtfim import *
import matplotlib.pyplot as plt
import numpy as np


M=simplePureHamiltonian(80,3.1416,0,0)
#plt.matshow(M)
#plt.colorbar()
#plt.show()

t=tfim(M)

AABB=t.AABBt0
#plt.matshow(AABB)
#plt.colorbar()
#plt.show()

swk2=t.correlator_dynamics_sector(5,35,0.05,30)
swk=t.correlator_dynamics_sector_AABB(5,35,0.05,30)


print(np.max(np.abs(swk2-swk)))

plt.matshow(swk.real)
plt.colorbar()
plt.matshow(swk.imag)
plt.colorbar()
plt.show()

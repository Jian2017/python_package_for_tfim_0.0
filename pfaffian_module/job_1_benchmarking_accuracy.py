# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:35:56 2018

@author: jian
"""

from pf import pfaffian, pf


import numpy as np

N=200
steps=10
dd=np.zeros(steps)
for i in range(steps):
    X=np.random.random((2*N,2*N))
    T=X.transpose()-X
    dd[i]=abs(pf(T)-pfaffian(T))/abs(pf(T))   # relative error makes sense
dd.max()
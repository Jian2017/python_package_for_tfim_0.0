# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:40:37 2018

@author: jian
"""
import matplotlib.pyplot as plt
import numpy as np
from pf import pf, pf2, pfaffian_householder

import time

def howlong1(matrixSize,matrixNum):
    start = time.time()
    for i in range(matrixNum):        
        X=np.random.random((2*matrixSize,2*matrixSize))
        S=X.transpose()-X
        pf(S)
    end= time.time()
    return (end-start)
def howlong2(matrixSize,matrixNum):
    start = time.time()
    for i in range(matrixNum):        
        X=np.random.random((2*matrixSize,2*matrixSize))
        S=X.transpose()-X
        pfaffian_householder(S)
    end= time.time()
    return (end-start)

    
    
matrixNum=40
steps=14
dd=np.zeros(steps)
xx=dd+0
dd2=dd+0
for i in range(steps):
    xx[i]=i*20+20

for i in range(steps):
    print(i)
    dd[i]=howlong1(int(xx[i]),matrixNum)/matrixNum
    #dd2[i]=howlong2(int(xx[i]),matrixNum)/matrixNum
    
plt.plot(xx,dd,'o-',xx,dd2,'.-')
plt.xlabel("dimension of matrix")
plt.ylabel("average time per matrix")
plt.title("average time per real random matrix")

plt.show()
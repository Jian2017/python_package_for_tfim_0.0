#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:05:50 2018

@author: jian
"""

from package.hamiltonian import job3_H

from package.PPFtfim import tfim
import matplotlib.pyplot as plt
import numpy as np

import multiprocessing



L=32

STEPS=64
dt=0.5

RR=128




M=job3_H(4*L,0)

t=tfim(M)
cnt=t.correlator_dynamics_sector(L,3*L,dt,STEPS)

swk2=t.Cnt2Swk(cnt)
plt.matshow(swk2.real,cmap="YlGn")
plt.colorbar()
plt.show()




Ms=np.zeros((RR,M.shape[0],M.shape[1]))
cnts=np.zeros((RR,cnt.shape[0],cnt.shape[1]),dtype=complex)


for i in range(RR):
    Ms[i,:,:]=job3_H(4*L,i)
    
'''
for i in range(RR):
    print(i)
    cnts[i,:,:]=tfim(Ms[i,:,:]).correlator_dynamics_sector(L,3*L,dt,STEPS)
'''




def ff(i):
    return tfim(Ms[i,:,:]).correlator_dynamics_sector(L,3*L,dt,STEPS)



cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cores)
    
xs=np.array(range(RR))

cnts=pool.map(ff, xs )
pool.close()


cnt=np.mean(cnts,axis=0)



plt.matshow(cnt.real)
plt.show()



swk2=t.Cnt2Swk(cnt)
plt.matshow(swk2.real,cmap="YlGn")
plt.colorbar()
plt.show()


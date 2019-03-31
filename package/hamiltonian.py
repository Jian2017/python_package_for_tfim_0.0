# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 01:58:17 2018

random matrix constructor

@author: wangj
"""

import numpy as np


def simplePureHamiltonian(L,h,lam1,lam2=0,lamlam1=0,lamlam2=0):
    M=np.zeros((L,L))
    for i in range(L):
        M[i,i]=h
    
    for i in range(L-1):
        M[i,i+1]=-lam1
        
    for i in range(L-2):
        M[i,i+2]=-lam2
        
    return M


def DisorderedHamiltonian(L,disOrder):
    
    lam1=1
    lam2=-0.3
    h=1
    
    M=np.zeros((L,L))
    for i in range(L):
        M[i,i]=h
    
    for i in range(L-1):
        M[i,i+1]=-(lam1+np.random.uniform(-disOrder,disOrder))
        
    for i in range(L-2):
        M[i,i+2]=-lam2
        
    return M



def job3_H(L,seed):
    
    np.random.seed(seed)
    
    lam1=1
    lam2=0
    
    hS=0.2
    hL=3.0
    pL=0.6
    

    
    M=np.zeros((L,L))
    for i in range(L):
        M[i,i]=binDistribute(hS,hL,pL)
    
    for i in range(L-1):
        M[i,i+1]=-lam1
        
    for i in range(L-2):
        M[i,i+2]=-lam2
        
    return M


def binDistribute(hS,hL,pL):
    if np.random.uniform(0, 1)<pL:
        return hL
    else:
        return hS

    


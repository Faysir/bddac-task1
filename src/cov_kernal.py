# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 16:26:15 2014
cov_kernal: return the covarience matrix of the features
        input:
            #X: the feature data
            #theta:the hyper para, a column vector
@author: mountain
"""
import numpy as np
from numpy import matlib

def cov_kernal(X,theta):
    #return the covarience matrix
    #X: the feature data
    #theta:the hyper para, a column vector
    
    row,col=X.shape
    K=matlib.zeros([row,col])
    for i in range(row):
        for j in range(col):
            x1=X[i]
            x2=X[j]
            K[i,j]=theta[0]*np.exp(-0.5*np.dot(np.square(x1-x2),theta[1:-2]))+theta[-2]+(i==j)/theta[-1]
            K[j,i]=K[i,j]
    return K
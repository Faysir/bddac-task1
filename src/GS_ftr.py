# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 16:05:25 2014
GS_ftr: construct the Gaussian feature based on the feature obtained by LSA

@author: mountain
"""
import numpy as np
from cov_kernal import cov_kernal

class GS_ftr(object):
    def __init__(self,src_ftr,tar_ftr,theta):
        self.src_ftr=src_ftr
        self.tar_ftr=tar_ftr
        self.theta=theta
        self.src_num,self.ftr_dim=src_ftr.shape
        self.tar_num,self.ftr_dim=tar_ftr.shape

        
        
    #obtain the covarience matrix of the source domain features
    def K_src(self):
        self.Ksrc=cov_kernal(self.src_ftr,self.theta)
    
    #obtain the covarience matrix of the target domain features
    def K_tar(self):
        self.Ktar=cov_kernal(self.tar_ftr,self.theta)
        
    def P_prior(self,flg):
        if flg=="src":
            return 1/np.sqrt(((2*np.pi)**(self.ftr_dim*self.src_num))*(linalg.det(self.Ksrc)**self.ftr_dim))\
                    *np.exp(-0.5*(np.trace(self.Ksrc*self.src_ftr*self.src_ftr.T)))
        elif flg=="tar":
            return 1/np.sqrt(((2*np.pi)**(self.ftr_dim*self.tar_num))*(linalg.det(self.Ktar)**self.tar_num))\
                    *np.exp(-0.5*(np.trace(self.Ktar*self.tar_ftr*self.tar_ftr.T)))
                
    def KLDA_J(self):
        
        
    def P_latent:
        
    def P_theta:
        
    def P_poster
        
    def P_log_poster:
    
    
        
        
        
        



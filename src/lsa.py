# -*- coding: utf-8 -*-
"""
Created on Sat Jul 05 13:03:23 2014
LSA: Latent Semantic Analysis 
__init__:
        input: word_dict:the dict {word:the label of id}
               id_count:the number of the id

build_matrix: construct the matrix of the word and the id
              obtain a dict of the word and its label
        self.A[word,id_label]=the times of the word occured in id
        self.word_lbl={word:word_label}

TF_IDF: convert the element in self.A to the TF_IDF value
        self.A[word,id_label]=tf_idf_value_of_the _word

cal_lsa: calculate the svd decomposition of the self.A
        self.u,self.s,self.vt=svd(self.A)

        
@author: mountain
"""
import numpy as np

class LSA(object):
    def __init__(self,word_dict,id_count):
        self.word_dict=word_dict
        self.id_count=id_count
        
    def build_matrix(self):
        self.word_lbl={}
        self.words=[k for k in self.word_dict.keys()]
        self.A=np.zeros([len(self.words),self.id_count])
        for i,k in enumerate(self.words):
            for d in self.word_dict[k]:
                self.A[i,d]+=1
                self.word_lbl[k]=i
    
    def TF_IDF(self):
        words_per_doc=np.sum(self.A,axis=0)
        doc_per_word=np.sum(self.A,axis=1)
        row,col=self.A.shape
        for i in range(row):
            for j in range(col):
                self.A[i,j]=self.A[i,j]/words_per_doc[j]*np.log(col)/doc_per_word[i]

    
    def cal_lsa(self):
        self.build_matrix()
        self.TF_IDF()
        self.U,self.S,self.Vt=np.linalg.svd(self.A)
                
    
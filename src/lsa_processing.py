# -*- coding: utf-8 -*-
"""
Created on Mon Jul 07 17:39:10 2014

@author: mountain
"""

from lsa import LSA
from read_and_write import write_dict_into_utf8,write_dict_into_GB18030
import json

#the file of the words_id_dict
f=file(r'../result/test.json')
word_dict=json.load(f,encoding = "UTF-8", strict=False)

#the total number of the  samples
id_count=11463;

lsa_word_id=LSA(word_dict,id_count)

#save the word and its corresponding row number in the lsa matrix
#       eg:word1-6 represents the word1 is in row 6
#       the row number begins with 0
utf8path='../result/words_num_uft8.json'
write_dict_into_utf8(utf8path,lsa_word_id.word_lbl)
GBpath='../result/words_num.json'
write_dict_into_GB18030(GBpath,lsa_word_id.word_lbl)

#do the latent semantic analysis
U,S,Vt=lsa_word_id.cal_lsa()

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:40:53 2013

@author: zhu
"""
from collections import Counter
import jieba
import jieba.analyse
import pandas as pd
import numpy as np 



filename= 'c:/Python27/data/appeal.xlsx'
df=pd.read_excel(filename,'SQL Results')
df=df['GROUP_REASON']
ls=list(df)
txt=''.join(ls)

'''
cut=list(jieba.cut(txt))
cut_freq=Counter(cut)
l=cut_freq.most_common(50)
for i in range(len(l)):
    print l[i][0],l[i][1] 
'''
tags=jieba.analyse.extract_tags(txt, 50 , withWeight=True)
rank=[]
for i in range(len(tags)):
    rank.append((tags[i][0],txt.count(tags[i][0])))

rank_sort = sorted(rank,key=lambda item:item[1],reverse=True)
for i in range(len(tags)):
    print rank_sort[i][0], rank_sort[i][1]
 
    
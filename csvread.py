# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 09:02:58 2015

@author: admin
"""

import pandas as pd
import codecs as cd 

filename='C:\SecondHalf_zhu\Tasks\冯静\cust1.csv'
f=cd.open(path)
count=0
pdf=pd.read_csv(filename, header=None, sep=",", na_filter=False, low_memory=False)
pdtest=pdf.head()



for line in f:
    print line 
    count+=1
    if count==10:
        break

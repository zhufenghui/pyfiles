# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 12:12:00 2015

@author: admin
"""

import random as r
import numpy as np 
l= [r.random() for i in range(100)]
count=0
for i in range(len(l)):
    print i 
    count+=1
    print l[i]
    print i
    
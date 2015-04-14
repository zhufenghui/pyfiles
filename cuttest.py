# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 16:18:00 2015

@author: admin
"""
 
import jieba
import sys 
sys.path.append("../") 
#jieba.load_userdict('c:/Python27/pyfiles/userdict.txt')
s1=u'创新办'
s2=u'云计算'
s3=u'八一双鹿'
jieba.add_word(s1,100)
jieba.add_word(s2,100)
jieba.add_word(s3,100)
test_sent = "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿"

print ", ".join(jieba.cut(test_sent))
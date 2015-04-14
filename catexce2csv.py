# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:31:28 2015

@author: admin
"""

import pandas as pd #导入pandas模块
import os #导入python os模块
def get_xls_file():
   """返回一个由当前工作目录中xls文件组成的list"""
   cwd = os.getcwd()
   temp = list(os.walk(cwd))
   xls_file = [i for i in temp[0][2] \
           if os.path.splitext(i)[1] == '.xls']  #扩展名分离
   return xls_file
def xls_to_pd(xlsfile):
   """将一个xls文件组成的list,装换成pandas数据模式，"""
   cwd = os.getcwd()
   pd_file = [pd.ExcelFile(os.path.join(cwd, name)).parse('data')\
              for name in xlsfile]
   pd_cat = pd.concat(pd_file)
   return pd_cat
a = get_xls_file()
b = xls_to_pd(a)
b.to_csv(filename)
'''
当前工作目录中所有的xls文件都已经做合成了一个csv文件，
可以用excel打开，选择用“，”分割，导入即可
'''
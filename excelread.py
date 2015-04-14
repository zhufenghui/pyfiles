# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:23:05 2015

@author: admin
"""
# 分批次运行，先得到books， 再运行，利用print 来debug

import pandas as pd
import numpy as np 
import matplotlib as pl
import os
count=0
#ori_path='C:\SecondHalf_zhu\Tasks\冯静\样本数据'
ori_path='C:\Python27\data\sample'
def get_xls_books(ori_path): # get target filename and dir of a path 
    temp = list(os.walk(ori_path)) #tmp is list ,tmp[0]该目录文件路径和文件名， tmp[1]:子目录文件路径，文件名称 
    book_path=[]
    book_name=[]
    root=temp[0][0]
    for i in temp[0][2]:
      if os.path.splitext(i)[1] == '.xlsx': #splite filename 
          obj_path=os.path.join(root,i)
          book_path.append(obj_path)
          book_name.append(os.path.splitext(i)[0])
    return zip(book_path, book_name)
 
def get_xls_sheets(obj_path): #get all sheets of a object path
    xls=pd.ExcelFile(obj_path)  
    sheet_names=xls.sheet_names
    sheets=[xls.parse(i)  for i in range(0,len(sheet_names)) ]   # use parse can get dataframe saved into a list 
    return zip(sheet_names,sheets)

books=get_xls_books(ori_path)  # book paths list
#xls=pd.ExcelFile(books[0])
#print xls.parse(0).columns
 
for book in books:  # this loop get a book 
    bookname=book[1]
    bookpath=book[0]
    sheets=get_xls_sheets(bookpath)  # get all sheets and names from book path 
    for i in range(len(sheets)):  #operate each sheet, is range(len) not len 
        sheetname=sheets[i][0]
        name=bookname+'-'+sheetname+'.'+'csv' 
        pd_sheet=sheets[i][1] # dataFrame
        cols=pd_sheet.columns
        pdf=pd_sheet[[cols[17],cols[18],cols[4],cols[6],cols[8],cols[10],cols[19],cols[16]]]  # use emunerate function     
        pdf.columns=['area','patch','wangdian','operator','custid','servid','servtype','is_identify'] # rename 
        pdf1=pdf[pdf['is_identify']=='是']   #filter
        pdf2=pdf1.drop('is_identify',1)     
        pdf2.to_csv(os.path.join(ori_path,name), header=None, index=None)




'''
for pd_sheets in pd_files:
     pd_sheets.to_csv()


use_cols=['STAMONTH','SERVID','PERMARK','STOPTYPE', 'AREAID','SERVSTATUS']
df=pd.read_csv(path,usecols=use_cols)
area_counts=df['AREAID'].value_counts()
cols=df.columns
for ind,col in enumerate(cols):
...     print ind,col
'''
 
 
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 16:49:24 2014

@author: admin
"""
import pandas as pd
import numpy as np 
import matplotlib as pl
#df=pd.read_csv('c:/Python27/data/servstate.csv',sep=','  ,
#error_bad_lines=False, index_col=False, dtype=unicode)

'''
dfh= pd.HDFStore('test2.h5')
chunker = pd.read_csv('c:/Python27/data/servstate.csv', iterator=True, chunksize=50000 )
dfh.append('df', pd.concat([chunk for chunk in chunker], ignore_index=True)) 


#df=pd.read_excel()
path='c:/Python27/data/test1.xls'
xls=pd.ExcelFile(path)
sheets=xls.sheet_namesdf=pd.read_csv('c:/Python27/data/serv2.csv')
 

path='c:/Python27/data/servstate.csv'
use_cols=['STAMONTH','SERVID','PERMARK','STOPTYPE', 'AREAID','SERVSTATUS']
df=pd.read_csv(path,usecols=use_cols)
area_counts=df['AREAID'].value_counts()

'''
path1= 'C:/Python27/data/myresult.xlsx'
path2= 'C:/Python27/data/oriresult.xlsx'
df_my=pd.read_excel(path1,'SQL Results')
df_ori=pd.read_excel(path2,'SQL Results')

df_my=df_my[df_my.columns[1:]]
df_ori= df_ori.rename(columns={u'客户编号':u'CUSTID'})
s=df_my.loc[:,'CUSTID'].astype(str)
isin_ori=s.isin(df_ori['CUSTID'])   #use columns rather than name
df_filter=df_my[isin_ori]
#df_filter.to_excel('C:/Python27/data/fail_match.xls')   #xlsx leads to luanma

#df_merge=pd.merge(df_fail,df_cash, on = 'NAME') 
 
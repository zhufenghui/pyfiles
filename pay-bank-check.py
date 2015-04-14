# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 14:44:01 2015

@author: admin
"""
import pandas as pd
import numpy as np 

path1= 'C:/Python27/data/bank.csv'
path2= 'C:/Python27/data/pay.csv'

df_bank=pd.read_csv(path1)
df_pay=pd.read_csv(path2)

df_bank=df_bank[df_bank.columns[1:]]
df_pay=df_pay[df_pay.columns[1:]]
df_pay_succeed=df_pay[df_pay['PAYSTATUS']==0] 
df_pay_succeed2=df_pay_succeed[['PAYWAY','FEES']]

#grouped=df_pay_succeed2.groupby('PAYWAY').sum()
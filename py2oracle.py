# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 16:21:32 2015

@author: admin
"""
import os 
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  #必须置于cx之前

import cx_Oracle as co
import pandas as pd 

filename='C:/SecondHalf_zhu/Tasks/邮储资料/userid.txt'
f=open(filename)
userid=[]
for line in f:
    line=line.strip()
    userid.append((line))
    
 
#dsn=co.makedsn('192.168.113.237','1521','boss1')  #ndb1 ,instance_name was used here , bidb2 uses service_name  
dsn=co.makedsn('192.168.113.226','11521','boss')
db=co.connect('zsboss','zsboss123',dsn)
cursor=db.cursor()
#cursor.execute ("drop TABLE tmp.zhu_test ")  
cursor.execute ("CREATE TABLE tmp.zhu_test(userid VARCHAR2(32))")  
cursor.prepare("INSERT INTO tmp.zhu_test(userid) VALUES (:1)")
cursor.executemany(None, userid)
db.commit()


'''
for i in range(len(userid)):
    s='insert into tmp.zhu_test(userid)values'+'('+'\''+userid[i]+'\''+')'
     #print sql
    cursor.execute(sql)

row=cursor.fetchall() # 必须是一个查询的cursor
print row[0]
cursor.close()
db.close
'''
  
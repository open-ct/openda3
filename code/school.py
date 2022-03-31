# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:35:38 2021

@author: Administrator
"""

import pandas as pd
import numpy as np

data=pd.read_excel('人员清理.xls')
data2=pd.read_excel('总作答人数.xls')
new_schools=data['SCHOOL_NAME'].unique()
old_schools=data2['school'].unique()
new_school=[]
old_school=[]

for temp in new_schools:
    temp_data=data[data['SCHOOL_NAME'].isin([temp])]
    a=len(temp_data)
    new_school.append(a)

for temp in old_schools:
    temp_data=data2[data2['school'].isin([temp])]
    a=len(temp_data)
    old_school.append(a)

#print(new_school)

#print(old_school)

res_all=[]
for i in range(len(new_school)):
    res=round(new_school[i]*100/old_school[i])
    res_all.append(str(res)+'%')
    
print(res_all)
print(new_schools)
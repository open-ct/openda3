# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:07:58 2021

@author: Administrator
"""

import os 
import re
import pandas as pd
from PIL import Image
import numpy as np
file_dir='E:\openct\images'
Task_name=[]
ID=[]
Path=[]
Name=[]
School=[]
N=[]
X=[]
Xs=[]
num=-888
Num=[]
Task_name=[]
for root,dirs,files in os.walk(file_dir):
    for i in range(len(files)):
        temppath='E:\images'+'\\'+files[i]
        Path.append(temppath)
        Id=re.findall(r'\d{11}',files[i])
        ID.append(Id[0])
        tempname=re.findall(r'(?<=\-).*(?=\-)',files[i])
        Name.append(tempname[0])
        school=re.search(r'\-(.+)\-(.*).png',files[i])
        tempschool=school.group(2)
        School.append(tempschool)
        Task_name.append('31')
        N.append('N')
        X.append('*')
        Xs.append('*|')
        Num.append(num)
        num-=1
    data={'默认值N':N,'准考证号':ID,'题号':Task_name,'姓名':Name,'学校':School,'默认值N':N,'默认值0':np.linspace(0,0,len(files)),'图像路径':Path,'默认值-888':Num,'默认值3':Xs,'默认值':X}
    df=pd.DataFrame(data)
    df.to_excel('接口文件(图片).xls')

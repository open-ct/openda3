import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import re

data=pd.read_csv("2021-08-13-10-59-14_EXPORT_CSV_3250598_565_0.csv")
data['task_answers'] = data.task_answers.astype(str)
data['user'] = data.user.astype(str)

input1=[]
input2=[]
input3=[]
input4=[]
canvas11=[]
canvas12=[]
canvas21=[]
canvas22=[]
canvas23=[]
canvas24=[]
canvas31=[]
canvas32=[]
canvas33=[]
canvas41=[]
canvas42=[]
canvas43=[]
canvas44=[]
canvas45=[]

for i in range(len(data)):
    if not(pd.isnull(data['start_time'].iloc[i])):
        str_all_split=re.findall(r'\{\\\"canvas.*?deck\\.*?\}', data['task_answers'].iloc[i])
        if len(str_all_split)>0:
            tempinput1=re.findall(r'(?<=input\\\"\:\[\\\").*(?=\\\"\,\\\"\\)',str_all_split[0])
            if tempinput1:
                input1.append(tempinput1[0])
            else:
                input1.append('')
            tempcanvas1=re.findall(r'(?<=basic\\\"\:\[).*(?=\,)',str_all_split[0])
            tempcanvas11=re.findall(r'(?<=\\\").*(?=\\\"\,)',tempcanvas1[0])
            canvas11.append(tempcanvas11[0])
            tempcanvas12=re.findall(r'(?<=\,\\\").*(?=\\\"\])',tempcanvas1[0])
            canvas12.append(tempcanvas12[0])
        else:
            canvas11.append('')
            input1.append('')
            canvas12.append('')
        if len(str_all_split)>1:
            tempinput2=re.findall(r'(?<=input\\\"\:\[\\\").*(?=\\\"\,\\\"\\)',str_all_split[1])
            input2.append(tempinput2[0])
            tempcanvas2=re.findall(r'(?<=basic\\\"\:\[\\\").*(?=\\\"\])',str_all_split[1])
            #区分
            tempstring2=tempcanvas2[0].split('\\\",\\\"')
            try:
                canvas21.append(tempstring2[0])
            except:
                canvas21.append('')
            try:
                canvas22.append(tempstring2[1])
            except:
                canvas22.append('')
            try:
                canvas23.append(tempstring2[2])
            except:
                canvas23.append('')
            try:
                canvas24.append(tempstring2[3])
            except:
                canvas24.append('')       
        else:
            input2.append('')
            canvas21.append('')
            canvas22.append('')
            canvas23.append('')
            canvas24.append('')
        if len(str_all_split)>2:
            tempinput3=re.findall(r'(?<=input\\\"\:\[\\\").*(?=\\\"\,\\\"\\)',str_all_split[2])
            #print(tempinput3)
            if tempinput3:
                input3.append(tempinput3[0])
            else:
                input3.append('')
            tempcanvas3=re.findall(r'(?<=basic\\\"\:\[).*(?=\,)',str_all_split[2])
            #print(tempcanvas3)
            if tempcanvas3:
                tempcanvas31=re.findall(r'(?<=\\\").*(?=\\\"\,)',tempcanvas3[0])
                tempcanvas32=re.findall(r'(?<=\,\\\").*(?=\\\"\])',tempcanvas3[0])
            else:
                tempcanvas31=['']
                tempcanvas32=['']
            canvas31.append(tempcanvas31[0])
            canvas32.append(tempcanvas32[0])
        else:
            canvas31.append('')
            input3.append('')
            canvas32.append('')
        if len(str_all_split)>3:
            tempinput4=re.findall(r'(?<=input\\\"\:\[\\\").*(?=\\\"\,\\\"\\)',str_all_split[3])
            input4.append(tempinput4[0])
            tempcanvas4=re.findall(r'(?<=basic\\\"\:\[\\\").*(?=\\\"\])',str_all_split[3])
            #区分
            tempstring4=tempcanvas4[0].split('\\\",\\\"')
            try:
                canvas41.append(tempstring4[0])
            except:
                canvas41.append('')
            try:
                canvas42.append(tempstring4[1])
            except:
                canvas42.append('')
            try:
                canvas43.append(tempstring4[2])
            except:
                canvas43.append('')
            try:
                canvas44.append(tempstring4[3])
            except:
                canvas44.append('')
            try:
                canvas45.append(tempstring4[4])
            except:
                canvas45.append('')
        else:
            input4.append('')
            canvas41.append('')
            canvas42.append('')
            canvas43.append('')
            canvas44.append('')
            canvas45.append('')
            
        tempcanvas33=re.search(r'(?<=\"\{\\"basic\\\"\:\[\\\").*(?=\\\"\]\,\\\"sketch\\\")',data['task_answers'].iloc[i])
        if tempcanvas33:
            canvas33.append(tempcanvas33[0])
        else:
            canvas33.append('')

null=[]
for i in range(len(data)):
    if pd.isnull(data['start_time'].iloc[i]):
        null.append(i)
dataa=data[['user','name','school','start_time','stop_time']]
dataaa=dataa.drop(null)
dataaa['草稿1']=input1
dataaa['草稿2']=input2
dataaa['草稿3']=input3
dataaa['草稿4']=input4
    
dataaa['11']=canvas11
dataaa['12']=canvas12
dataaa['21']=canvas21
dataaa['22']=canvas22
dataaa['23']=canvas23
dataaa['24']=canvas24
dataaa['32']=canvas33
dataaa['33']=canvas31
dataaa['34']=canvas32
dataaa['41']=canvas41
dataaa['42']=canvas42
dataaa['43']=canvas43
dataaa['44']=canvas44
dataaa['45']=canvas45

dataaa['作文字数统计']=''

stunum=[]
for i in range(len(dataaa)):
    tempnum=re.findall(r'(?<=人文素养\/).*',dataaa['user'].iloc[i])
    stunum.append(tempnum[0])
    if not(pd.isnull(dataaa['34'].iloc[i])):
        count=len(dataaa['34'].iloc[i])
        dataaa['作文字数统计'].iloc[i]=count
dataaa['user']=stunum


dataaa.to_csv('测试数据分析.csv')

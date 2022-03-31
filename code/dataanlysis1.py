# -*- coding: utf-8 -*-

#Created on Mon Jun 28 18:25:58 2021

#@author: Administrator


import pandas as pd
import re

data=pd.read_csv('result_data.csv',encoding='gbk')

data['task_answers'] = data.task_answers.astype(str)

#计算时间
data['sum_time'] = pd.to_datetime(data['stop_time']) - pd.to_datetime(data['start_time'])
#区分两个课程
data_junior=data[data['school'].isin(['区二中实验初中'])]
data_senior=data[data['school'].isin(['南溪一中（高中）'])]

canvas1=[]
canvas2=[]
canvas3=[]
canvas4=[]
canvas5=[]
basic1=[]
basic2=[]
basic3=[]
basic4=[]
basic5=[]
basic6=[]
basic7=[]
basic8=[]
basic9=[]
basic10=[]
basic11=[]
basic12=[]
basic13=[]
sketch=[]

for i in range(len(data['task_answers'])):
    str_canvas=re.findall(r'canvas.*?]}',data['task_answers'].iloc[i])
    str_basic=re.findall(r'basic.*?"]',data['task_answers'].iloc[i])
    str_sketch=re.findall(r'https.*?.png',data['task_answers'].iloc[i])
    for j in range(len(str_canvas)):
        #str_canvas[j]=str_canvas[j].strip('canvas\":{\\"input":[')
        #str_canvas[j]=str_canvas[j].strip('],\\"deck\\":}",')
        str_canvas[j]=str_canvas[j].strip('canvas\":{\\"input":[],\\"deck\\":}",')
        if len(str_canvas[j])<1:
            str_canvas[j]=' '
    for k in range(len(str_basic)):
        #str_basic[k]=re.sub(r'basic.*?":\[','',str_basic[k])
        #str_basic[k]=re.sub(r'\],\\"deck.*?}",','',str_basic[k])
        #str_basic[k]=str_basic[k].split('\"')
        str_basic[k]=str_basic[k].strip(r'basic\":[]')
        str_basic[k]=re.sub(r'deck.*?}",','',str_basic[k])
        str_basic[k]=str_basic[k].split('\",')
        for m in range(len(str_basic[k])):
            str_basic[k][m]=str_basic[k][m].strip(r'\"')        
        if len(str_basic[k])<1:
            str_basic[i]='\\'
        
    if len(str_canvas)>=1:
        canvas1.append(str_canvas[0])
    else:
        canvas1.append(' ')
    if len(str_canvas)>=2:
        canvas2.append(str_canvas[1])
    else:
        canvas2.append(' ')
    if len(str_canvas)>=3:
        canvas3.append(str_canvas[2])
    else:
        canvas3.append(' ')
    if len(str_canvas)>=4:
        canvas4.append(str_canvas[3])
    else:
        canvas4.append(' ')
    if len(str_canvas)>=5:        
        canvas5.append(str_canvas[4])
    else:
        canvas5.append(' ')
    sketch.append(str_sketch)
    if len(str_basic)>=1:
        if len(str_basic[0])>=1:
            basic1.append(str_basic[0][1])
        else:
            basic1.append(' ')
        if len(str_basic[0])>=4:        
            basic2.append(str_basic[0][3])
    else:
        basic1.append(' ')
        basic2.append(' ')
        basic3.append(' ')
        basic4.append(' ')
        basic5.append(' ')
        basic6.append(' ')
        basic7.append(' ')
        basic8.append(' ')
        basic9.append(' ')
        basic10.append(' ')
        basic11.append(' ')
        basic12.append(' ')
        basic13.append(' ')
   
    basic3.append(str_basic[1][1])
    basic4.append(str_basic[1][3])
    basic5.append(str_basic[1][5])
    basic6.append(str_basic[1][7])
    basic7.append(str_basic[2][1])
    basic8.append(str_basic[3][1])
    basic9.append(str_basic[4][1])
    basic10.append(str_basic[4][3])
    basic11.append(str_basic[4][5])
    basic12.append(str_basic[4][7])
    basic13.append(str_basic[4][9])
sketch[10]=['https://cdn.open-ct.com/task-resources/%E8%91%A3%E6%99%93%E8%88%92/222.png']
#print(sketch)

print(len(basic3))
data['canvas1']=canvas1
data['canvas2']=canvas2
data['canvas3']=canvas3
data['canvas4']=canvas4
data['canvas5']=canvas5
data['sketch']=sketch
data['basic1']=basic1
data['basic2']=basic2
data['basic3']=basic3
data['basic4']=basic4
data['basic5']=basic5
data['basic6']=basic6
data['basic7']=basic7
data['basic8']=basic8
data['basic9']=basic9
data['basic10']=basic10
data['basic11']=basic11
data['basic12']=basic12
data['basic13']=basic13

#每道题的平均字符数
def average_words(data):
    sum=0
    for i in range(len(data)):
        sum+=len(data[i])
        
    return sum

#草稿本利用率
def book_effiency(data1,data2):
    sum1=0
    sum2=0
    for i in range(len(data1)):
        sum1+=len(data1)
    for i in range(len(data2)):
        sum1+=len(data2)
    average=sum1/sum2
    
    return average

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:32:19 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
import re

data=pd.read_csv('20210712人文素养场景一的过程性数据.csv',encoding='gbk')
#数据具体格式需要询问
#data=data.iloc[108:467]
stu_num=[]
basic=[]
ans1=[]
ans2=[]
deck=[]
time=[]

for i in range(len(data)):
    st=data.iloc[i]
    temp_time=re.findall(r'.*(?=\,yibin\/)',st[0])
    time.append(temp_time[0])
    temp_stu_name=re.findall(r'(?<=yibin\/我是学生\,).*(\d{6})',st[0])
    stu_num.append(temp_stu_name[0])
    temp_basic=re.findall(r'(?<=basic\"\"\:\[).*(?=\,\"\")',st[0])
    #basic.append(temp_basic)
    temp_ans1=re.findall(r'(?<=\"\").*(?=\"\"\,)',temp_basic[0])
    ans1.append(temp_ans1[0])
    temp_ans2=re.findall(r'(?<=\,\"\").*(?=\"\"\])',temp_basic[0])
    ans2.append(temp_ans2[0])
    temp_deck=re.findall(r'(?<=deck\"\"\:)\d*',st[0])
    deck.append(temp_deck[0])
    
df={'考号':stu_num,'时间':time,'答案1':ans1,'答案2':ans2,'页码':deck}
df['持续时间']=''
df['答案1字数统计']=''
df['答案2字数统计']=''
df=pd.DataFrame(df)

num=df['考号'].unique()
last_time=[]

for temp in num:
    temp_data=df[df['考号'].isin([temp])]
    temp_Deck=temp_data['页码'].tolist()
    head=[]
    head.append(0)
    bottom=[]
    for j in range(1,len(temp_Deck)-1):
        if (temp_Deck[j]!=temp_Deck[j+1])and(temp_Deck[j-1]==temp_Deck[j]):
            bottom.append(j)
            head.append(j+1)
    bottom.append(len(temp_Deck)-1)
    last_time=[]
    for k in range(len(head)):
        start=head[k]
        stop=bottom[k]
        start_time=temp_data['时间'].iloc[start]
        stop_time=temp_data['时间'].iloc[stop]
        lasttime=pd.to_datetime(stop_time)-pd.to_datetime(start_time)
        tempmin=lasttime.seconds/60
        last_time.append(tempmin)
    for i in range(len(bottom)):
        stop=bottom[i]
        temp_data['持续时间'].iloc[stop]=last_time[i]

ans1_count=[]
ans2_count=[]

for i in range(len(bottom)):
    ans1=temp_data['答案1'].iloc[bottom[i]]
    temp_data['答案1字数统计'].iloc[bottom[i]]=len(ans1)
    ans2=temp_data['答案2'].iloc[bottom[i]]
    temp_data['答案2字数统计'].iloc[bottom[i]]=len(ans2)
    
temp_data.to_excel('processing2.xls')   
    
        
        
        
    
        
        
    
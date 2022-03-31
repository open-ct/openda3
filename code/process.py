# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 16:20:40 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
import re

data_list=pd.read_csv('ticket_log_mianyang-人文素养.csv',chunksize=10000,error_bad_lines=False )
temp_data=[]
for chunk in data_list:
    temp_data.append(chunk)
data=pd.concat(temp_data)

data.columns=['时间','标签1','考号','题号','题目','答案','地区']
#data= data.drop(['标签1', '题目','地区'], axis=1)
deck=[]
for i in range(len(data)):
    a=data['答案'].iloc[i]
    try:
        temp_deck=re.findall(r'(?<=deck\"\:)\d*',a)
        deck.append(temp_deck[0])
    except:
        deck.append('')
data['deck']=deck
stu=data['考号'].unique()

scene1_time=[]
scene2_time=[]
scene3_time=[]
scene4_time=[]
scene5_time=[]

scene1_change=[]
scene2_change=[]
scene3_change=[]
scene4_change=[]
scene5_change=[]




for temp in stu:
    temp_data=data[data['考号'].isin([temp])]
    ans=temp_data['题号'].unique()
    change_sum=[]
    time_sum=[]
    for temp1 in ans:
        
        temp_temp_data=temp_data[temp_data['题号'].isin([temp1])]
        deck_list=list(temp_temp_data['deck'])
        deck_list_ar=np.array(deck_list)
        deck_list_ar=np.insert(deck_list_ar,0,0)
        #print(deck_list_ar)
        #每个场景切换次数
        change=0
        for i in range(1,len(deck_list)):
            if deck_list[i]!=deck_list[i-1]:
                change+=1
        change_sum.append(change)
        #统计首页的停留时间：先把所有都挑出来再和1做交集        
        temp_head=[]
        temp_bottom=[]
        for j in range(1,len(deck_list_ar)-1):
            #头
            if (deck_list_ar[j]!=deck_list_ar[j-1])and(deck_list_ar[j]==deck_list_ar[j+1]):
                temp_head.append(j-1)#减去加的0
            if (deck_list_ar[j]==deck_list_ar[j-1])and(deck_list_ar[j]!=deck_list_ar[j+1]):
                temp_bottom.append(j-1)
        if len(temp_head)!=len(temp_bottom):
            temp_bottom.append(len(deck_list)-1)
        arr1=[]
        for i in range(len(deck_list)):
            if deck_list[i]=='1':
                arr1.append(i)
        head = [val for val in temp_head if val in arr1]
        bottom = [val for val in temp_bottom if val in arr1]
        #求取对应的时间，如果head是空，则时间是第二个减第一个
        sum_time=0
        if len(head)!=0:
            for m in range(len(head)):
                start=head[m]
                stop=bottom[m]
                start_time=temp_temp_data['时间'].iloc[start]
                stop_time=temp_temp_data['时间'].iloc[stop]
                lasttime=pd.to_datetime(stop_time)-pd.to_datetime(start_time)
                tempmin=lasttime.seconds/60
            sum_time+=tempmin
            time_sum.append(round(sum_time,2))
        
        if len(head)==0:
            if len(temp_temp_data)>=2:
                start_time=temp_temp_data['时间'].iloc[0]
                stop_time=temp_temp_data['时间'].iloc[1]
                lasttime=pd.to_datetime(stop_time)-pd.to_datetime(start_time)
                tempmin=lasttime.seconds/60
                sum_time+=tempmin
                time_sum.append(round(sum_time,2))
            else:
                time_sum.append(0)
                
    #time=dict(zip(scene,time_sum))
    #changes=dict(zip(scene,change_sum))     
    #df_time=pd.DataFrame(time)
    try:
        scene1_time.append(time_sum[0])
    except:
        scene1_time.append(0)
    try:
        scene2_time.append(time_sum[1])
    except:
        scene2_time.append(0)
    try:
        scene3_time.append(time_sum[2])
    except:
        scene3_time.append(0)
    try:
        scene4_time.append(time_sum[3])
    except:
        scene4_time.append(0)
    try:
        scene5_time.append(time_sum[4])
    except:
        scene5_time.append(0)
    try:
        scene1_change.append(change_sum[0])
    except:
        scene1_change.append(0)
    try:
        scene2_change.append(change_sum[1])
    except:
        scene2_change.append(0)
    try:
        scene3_change.append(change_sum[2])
    except:
        scene3_change.append(0)
    try:
        scene4_change.append(change_sum[3])
    except:
        scene4_change.append(0)
    try:
        scene5_change.append(change_sum[4])
    except:
        scene5_change.append(0)
    print(str(temp)+'finish')
    #print(change_sum)#有5个元素的数组
    #print(time_sum)
df_time=pd.DataFrame()
df_time['场景一']=scene1_time
df_time['场景二']=scene2_time
df_time['场景三（一）']=scene3_time
df_time['场景三（二）']=scene4_time
df_time['场景四']=scene5_time
df_time.index=stu
df_time.to_excel('过程数据时间统计.xls')
df_change=pd.DataFrame()
df_change['场景一']=scene1_change
df_change['场景二']=scene2_change
df_change['场景三（一）']=scene3_change
df_change['场景三（二）']=scene4_change
df_change['场景四']=scene5_change
df_change.index=stu
df_change.to_excel('过程数据变化次数统计.xls')




            
            
        
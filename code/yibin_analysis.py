# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:52:36 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
import re

data=pd.read_excel('ticket_log_场景二：听清音.xlsx')
deck=[]
for i in range(len(data)):
    temp_deck=re.findall(r'(?<=deck\"\:)\d*',data['task_answer'].iloc[i])
    deck.append(temp_deck)
data['deck']=deck

stu=data['ticket_id'].unique()
scene_time=[]
scene_change=[]
for temp in stu:
    temp_data=data[data['ticket_id'].isin([temp])]
    change_sum=[]
    time_sum=[]
    deck_list=list(temp_data['deck'])
    deck_list_ar=np.array(deck_list)
    deck_list_ar=np.insert(deck_list_ar,0,0)
    change=0
    for i in range(1,len(deck_list)):
        if deck_list[i]!=deck_list[i-1]:
            change+=1
    change_sum.append(change)
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
            start_time=temp_data['timestamp'].iloc[start]
            stop_time=temp_data['timestamp'].iloc[stop]
            lasttime=pd.to_datetime(stop_time)-pd.to_datetime(start_time)
            tempmin=lasttime.seconds/60
        sum_time+=tempmin
        time_sum.append(round(sum_time,2))
        
        if len(head)==0:
            if len(temp_data)>=2:
                start_time=temp_data['timestamp'].iloc[0]
                stop_time=temp_data['timestamp'].iloc[1]
                lasttime=pd.to_datetime(stop_time)-pd.to_datetime(start_time)
                tempmin=lasttime.seconds/60
                sum_time+=tempmin
                time_sum.append(round(sum_time,2))
            else:
                time_sum.append(0)
    try:
        scene_time.append(time_sum[0])
    except:
        scene_time.append(0)
    try:
        scene_change.append(change_sum[0]+1)
    except:
        scene_change.append(1)

data['time']=scene_time
data['change']=scene_change
data.to_excel('场景二统计')
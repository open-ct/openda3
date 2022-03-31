# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:04:30 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib import gridspec

data=pd.read_excel('20210828宜宾测试——人文素养.xls')
clear=[]


for i in range(len(data)):
    count99=0
    count0=0
    t1_1=data['t1_1'].iloc[i]
    t2_1=data['t2_1'].iloc[i]
    t3_1=data['t3_1'].iloc[i]
    t4_1=data['t4_1'].iloc[i]
    t5_1=data['t5_1'].iloc[i]
    t6_1=data['t6_1'].iloc[i]
    t7_1=data['t7_1'].iloc[i]
    t7_2=data['t7_2'].iloc[i]
    t7_3=data['t7_3'].iloc[i]
    t8_1=data['t8_1'].iloc[i]
    t8_2=data['t8_2'].iloc[i]
    t8_3=data['t8_3'].iloc[i]
    t9_1=data['t9_1'].iloc[i]
    t9_2=data['t9_2'].iloc[i]
    t9_3=data['t9_3'].iloc[i]
    t9_4=data['t9_4'].iloc[i]
    t9_5=data['t9_5'].iloc[i]
    if t1_1==99.0:
        count99=count99+1
    if t2_1==99.0:
        count99=count99+1
    if t3_1==99.0:
        count99=count99+1
    if t4_1==99.0:
        count99=count99+1
    if t5_1==99.0:
        count99=count99+1
    if t6_1==99.0:
        count99=count99+1
    if t7_1==99.0:
        count99=count99+1
    if t7_2==99.0:
        count99=count99+1
    if t7_3==99.0:
        count99=count99+1
    if t8_1==99.0:
        count99=count99+1
    if t8_2==99.0:
        count99=count99+1
    if t8_3==99.0:
        count99=count99+1
    if t9_1==99.0:
        count99=count99+1
    if t9_2==99.0:
        count99=count99+1
    if t9_3==99.0:
        count99=count99+1
    if t9_4==99.0:
        count99=count99+1
    if t9_5==99.0:
        count99=count99+1
    if t1_1==0.0:
        count0=count0+1
    if t2_1==0.0:
        count0=count0+1
    if t3_1==0.0:
        count0=count0+1
    if t4_1==0.0:
        count0=count0+1
    if t5_1==0.0:
        count0=count0+1
    if t6_1==0.0:
        count0=count0+1
    if t7_1==0.0:
        count0=count0+1
    if t7_2==0.0:
        count0=count0+1
    if t7_3==0.0:
        count0=count0+1
    if t8_1==0.0:
        count0=count0+1
    if t8_2==0.0:
        count0=count0+1
    if t8_3==0.0:
        count0=count0+1
    if t9_1==0.0:
        count0=count0+1
    if t9_2==0.0:
        count0=count0+1
    if t9_3==0.0:
        count0=count0+1
    if t9_4==0.0:
        count0=count0+1
    if t9_5==0.0:
        count0=count0+1
    if (count99>=0)&(count0>=0)&(count0+count99==17):
        clear.append(i)
        #clear.append(i)
dataa=data.drop(clear)
dataa.to_excel('人员清理.xls')

'''
temp_num=list(dataa['t3_1'])
dict = {}
for key in temp_num:
    dict[key] = dict.get(key, 0) + 1
try:
    val05=dict.pop(0.5)
    dict[1]=dict[1]+val05
except:
    print('no')
try:
    val15=dict.pop(1.5)
    dict[2]=dict[2]+val15
except:
    print('no')

try:
    val25=dict.pop(2.5)
    dict[3]=dict[3]+val25
except:
    print('no')
try:
    val35=dict.pop(3.5)
    dict[4]=dict[4]+val35
except:
    print('no')
try:
    val45=dict.pop(4.5)
    dict[5]=dict[5]+val45
except:
    print('no')
try:
    val55=dict.pop(5.5)
    dict[6]=dict[6]+val55
except:
    print('no')
try:
    val65=dict.pop(6.5)
    dict[7]=dict[7]+val65
except:
    print('no')
try:
    val75=dict.pop(7.5)
    dict[8]=dict[8]+val75
except:print('no')
try:
    val85=dict.pop(8.5)
    dict[9]=dict[9]+val85
except:
    print('no')
try:
    val95=dict.pop(9.5)
    dict[10]=dict[10]+val95
except:
    print('no')
try:
    val105=dict.pop(10.5)
    dict[11]=dict[11]+val105
except:
    print('no')
try:
    val115=dict.pop(11.5)
    dict[12]=dict[12]+val115
except:
    print('no')

num_x=[]
num_y=[]



for score,num in dict.items():
    num_x.append(score)
    num_y.append(num)
    
print(np.mean(num_x))

print(np.median(num_x))

counts = np.bincount(num_x)
print(np.argmax(counts))


plt.figure(1)
gs = gridspec.GridSpec(6,1)
ax1=plt.subplot(gs[:5,0])
recs=plt.bar(num_x,num_y)

x=[rec.get_x() for rec in recs]#使用列表推导式获取bar的横坐标
y=[rec.get_height()+100 for rec in recs]#使用列表推导式获取bar的高度
w=[rec.get_width() for rec in recs]#使用列表推导式获取bar的宽度
textx=[x+width/2 for x,width in zip(x,w)]#计算标注的横坐标
result=[plt.text(x,y,str(np.round(y)),size=8,ha = 'center') for x,y in zip(textx,y)]#使用列表推导式标注高度信息
resut_x=[plt.text(x,-10,str(int(x)),size=8,ha='center') for x in textx]
    
plt.title('分数统计',size=20)
plt.ylabel('人数')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

ax2=plt.subplot(gs[-1,0])
plt.axis('off')
ax = plt.gca()
col_labels=[str(i)+'分' for i in num_x]
sum=0
for i in num_y:
    sum=sum+i
y_per=[]
for i in num_y:
    y_per.append(str(np.round(i*100/sum,2))+'%')
table=plt.table(cellText=[y_per],colWidths=[0.08]*len(y_per),colLabels=col_labels,loc='center',cellLoc='center')
table.set_fontsize(30) #字体大小
plt.show()'''
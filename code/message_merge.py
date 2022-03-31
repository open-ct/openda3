# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:24:15 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data919=pd.read_csv('20210919合并基础库-人文素养.csv',encoding='gbk')
dataprocess=pd.read_excel('过程数据时间统计.xls')
dataprocess_change=pd.read_excel('过程数据变化次数统计.xls')
datayw=pd.read_excel('20210918绵阳语文成绩.xlsx')
dataprocess=dataprocess.groupby(by='stu_code').max()
dataprocess=dataprocess.reset_index('stu_code')
dataprocess_change=dataprocess_change.groupby(by='stu_code').max()
dataprocess_change=dataprocess_change.reset_index('stu_code')
list1=data919['stu_code'].tolist()
list2=dataprocess['stu_code'].tolist()
tmp=list(set(list1).intersection(set(list2)))  
dataprocess_new=dataprocess[dataprocess['stu_code'].isin(tmp)]

data_new=pd.merge(data919,dataprocess_new,on='stu_code')
data_new=pd.merge(data_new,dataprocess_change,on='stu_code')
data_new=pd.merge(data_new,datayw,on='stu_code')

#data_new.to_excel('汇总表.xls')

sum_time1=sum_time2=sum_time3=sum_time4=0
dysum_change1=dysum_change2=dysum_change3=dysum_change4=0
sysum_change1=sysum_change2=sysum_change3=sysum_change4=0
sum1=sum2=sum3=sum4=0
sum_all1=sum_all2=sum_all3=sum_all4=0
for i in range(len(data_new)):
    if data_new['total_level'].iloc[i]==1:
        sum1+=1
        sum_time1=sum_time1+int(data_new['场景一'].iloc[i])
        dysum_change1=dysum_change1+int(data_new['场景四变化'].iloc[i])+1
        sysum_change1=sysum_change1+int(data_new['场景三（二）变化'].iloc[i])+1
        sum_all1=sum_all1+int(data_new['场景一变化'].iloc[i]+data_new['场景二变化'].iloc[i]+data_new['场景三（一）变化'].iloc[i]+data_new['场景三（二）变化'].iloc[i]+data_new['场景四变化'].iloc[i])
    if data_new['total_level'].iloc[i]==2:
        sum2+=1
        sum_time2=sum_time2+int(data_new['场景一'].iloc[i])
        dysum_change2=dysum_change2+int(data_new['场景四变化'].iloc[i])+1
        sysum_change2=sysum_change2+int(data_new['场景三（二）变化'].iloc[i])+1
        sum_all2=sum_all2+int(data_new['场景一变化'].iloc[i]+data_new['场景二变化'].iloc[i]+data_new['场景三（一）变化'].iloc[i]+data_new['场景三（二）变化'].iloc[i]+data_new['场景四变化'].iloc[i])
    if data_new['total_level'].iloc[i]==3:
        sum3+=1
        sum_time3=sum_time3+int(data_new['场景一'].iloc[i])
        dysum_change3=dysum_change3+int(data_new['场景四变化'].iloc[i])+1
        sysum_change3=sysum_change3+int(data_new['场景三（二）变化'].iloc[i])+1
        sum_all3=sum_all3+int(data_new['场景一变化'].iloc[i]+data_new['场景二变化'].iloc[i]+data_new['场景三（一）变化'].iloc[i]+data_new['场景三（二）变化'].iloc[i]+data_new['场景四变化'].iloc[i])
    if data_new['total_level'].iloc[i]==4:
        sum4+=1
        sum_time4=sum_time4+int(data_new['场景一'].iloc[i])
        dysum_change4=dysum_change4+int(data_new['场景四变化'].iloc[i])+1
        sysum_change4=sysum_change4+int(data_new['场景三（二）变化'].iloc[i])+1
        sum_all4=sum_all4+int(data_new['场景一变化'].iloc[i]+data_new['场景二变化'].iloc[i]+data_new['场景三（一）变化'].iloc[i]+data_new['场景三（二）变化'].iloc[i]+data_new['场景四变化'].iloc[i])

#print(sum_time1/sum1,sum_time2/sum2,sum_time3/sum3,sum_time4/sum4)
#print(sum1/len(data_new),sum2/len(data_new),sum3/len(data_new),sum4/len(data_new))
level=['水平一','水平二','水平三','水平四']
dydata=[dysum_change1/len(data_new),dysum_change2/len(data_new),dysum_change3/len(data_new),dysum_change4/len(data_new)]
sydata=[sysum_change1/len(data_new),sysum_change2/len(data_new),sysum_change3/len(data_new),sysum_change4/len(data_new)]
dy_av=np.mean(dydata)
sy_av=np.mean(sydata)

fig,ax=plt.subplots()
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
dy=ax.barh(level,dydata,label='单源访问页数')
sy=ax.barh(level,sydata,left=dydata,label='多源访问页数')

ax.set_title('不同水平学生单源题项和多源题项的访问页数统计图',size=20)
ax.legend()

plt.show()

school_score=[]
school_change=[]
school_change_dy=[]

schools=data_new['SCHOOL_NAME'].unique()

for temp in schools:
    temp_data=data_new[data_new['SCHOOL_NAME'].isin([temp])]
    sum_score=0
    sum_change=0
    sum_change_dy=0
    for i in range(len(temp_data)):
        sum_change_dy=sum_change_dy+int(data_new['场景四'].iloc[i]+1)
        sum_change=sum_change+int(data_new['场景三（二）变化'].iloc[i]+1)
        sum_score=sum_score+int(data_new['total_score'].iloc[i])
    
    school_change.append(sum_change/len(temp_data))
    school_score.append(sum_score/len(temp_data))
    school_change_dy.append(sum_change_dy/len(temp_data))
df=pd.DataFrame()
df['school']=schools
df['change']=school_change
df['dy_change']=school_change_dy
df['score']=school_score
df.sort_values(by='change',axis=0,ascending=False,inplace=True)
df['rank']=range(10,96,3)
#相关度为-0.23
ratio=df[['dy_change','change']].corr(method = 'pearson')

#导航图
'''
plt.figure(figsize=(10, 8))
x,y=df['rank'],df['score']
plt.scatter(x,y)
plt.xlabel('百分比排名')
plt.ylabel('平均阅读表现')
plt.vlines(x=df['rank'].mean(),ymin=560, ymax=575)
plt.hlines(y=df['score'].mean(),xmin=0,xmax=100)
plt.grid(True)
plt.title('多源项中的整体导航',size=15)
plt.show()'''


#关系图
'''
plt.figure(figsize=(10,8))
x,y=df['dy_change'],df['change']
plt.scatter(x,y)
plt.xlabel('单源项目停留时间均值')
plt.ylabel('多源项目停留时间均值')
plt.text(x=4,#文本x轴坐标 
         y=20.7, #文本y轴坐标
         s='相关系数为-0.23',bbox={
              'edgecolor':'b',#外框色
               'alpha': 0.5, #框透明度
               'pad': 6,#本文与框周围距离 
              })

plt.title('多源题项整体导航')
plt.show()
'''
'''
plt.figure(figsize=(10, 8))
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.plot(level,dydata,linestyle='-',marker = "o", linewidth=1.5,label='单源题项')
plt.plot(level,sydata,linestyle='-',marker = "x",linewidth=1.5,label='多源题项')
plt.xlabel('人文素养水平')
plt.ylabel('访问页数')
plt.legend()
plt.hlines(y=dy_av,xmin='水平一',xmax='水平四',color='black',linestyle='dashed')
plt.hlines(y=sy_av,xmin='水平一',xmax='水平四',color='black',linestyle='dashed')
plt.grid(True)
plt.title('人文素养水平与单源、多源题项访问页面的关系',size=15)
plt.show()
    
print(sum1,sum2,sum3,sum4)
print(dysum_change1/sum1,dysum_change2/sum2,dysum_change3/sum3,dysum_change4/sum4)
print(sysum_change1/sum1,sysum_change2/sum2,sysum_change3/sum3,sysum_change4/sum4)
print(sum_all1/sum1,sum_all2/sum2,sum_all3/sum3,sum_all4/sum4)'''

#相关度分析
'''   
a=data_new['语文总成绩'].corr(data_new['场景一'])
b=data_new['语文总成绩'].corr(data_new['场景二'])
c=data_new['语文总成绩'].corr(data_new['场景三（一）'])
d=data_new['语文总成绩'].corr(data_new['场景三（二）'])
e=data_new['语文总成绩'].corr(data_new['场景四'])
f=data_new['语文总成绩'].corr(data_new['场景一变化'])
g=data_new['语文总成绩'].corr(data_new['场景二变化'])
h=data_new['语文总成绩'].corr(data_new['场景三（一）变化'])
i=data_new['语文总成绩'].corr(data_new['场景三（二）变化'])
j=data_new['语文总成绩'].corr(data_new['场景四变化'])


print('场景一'+str(a))
print('场景二'+str(b))
print('场景三（一）'+str(c))
print('场景三（二）'+str(d))
print('场景四'+str(e))
print('场景一变化'+str(f))
print('场景二变化'+str(g))
print('场景三（一）变化'+str(h))
print('场景三（二）变化'+str(i))
print('场景四变化'+str(j))'''






import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_excel('20210731-2240人文素养作答情况.xlsx')
data_notnull=data.loc[data['客户端答题状态']=='完成']
data_notnull.columns=['准考证号','姓名','学校','开始答题时间','交卷时间','客户端答题状态','服务器端答题状态','答题数','Q1','Q1ans1','Q1ans2','Q2','Q2ans1','Q2ans2','Q2ans3','Q2ans4','Q3','Q3ans1','Q4','Q4ans1','Q4ans2','Q5','Q5ans1','Q5ans2','Q5ans3','Q5ans4','Q5ans5']
data_notnull['总时间'] = pd.to_datetime(data_notnull['交卷时间']) - pd.to_datetime(data_notnull['开始答题时间'])
time=[]
w_counts=[]
for i in range(len(data_notnull)):
    #时间统计
    a=data_notnull['总时间'].iloc[i].seconds/60
    time.append(a)
    #字数统计
    b=len(str(data_notnull['Q4ans2'].iloc[i]))
    w_counts.append(b)
data_notnull['总时间']=time
data_notnull['Q4ans2count']=w_counts

sum010=0
count010=0
sum1130=0
count1130=0
sum3160=0
count3160=0
sum6190=0
count6190=0
sum91120=0
count91120=0
sum120=0
count120=0
for i in range(len(data_notnull)):
    if 0<=data_notnull['总时间'].iloc[i]<=10:
        sum010=sum010+int(data_notnull['Q4ans2count'].iloc[i])
        count010+=1
    if 11<=data_notnull['总时间'].iloc[i]<=30:
        sum1130=sum1130+int(data_notnull['Q4ans2count'].iloc[i])
        count1130+=1
    if 31<=data_notnull['总时间'].iloc[i]<=60:
        sum3160=sum3160+int(data_notnull['Q4ans2count'].iloc[i])
        count3160+=1
    if 61<=data_notnull['总时间'].iloc[i]<=90:
        sum6190=sum6190+int(data_notnull['Q4ans2count'].iloc[i])
        count6190+=1
    if 91<=data_notnull['总时间'].iloc[i]<=120:
        sum91120=sum91120+int(data_notnull['Q4ans2count'].iloc[i])
        count91120+=1
    if data_notnull['总时间'].iloc[i]>120:
        sum120=sum120+int(data_notnull['Q4ans2count'].iloc[i])
        count120+=1
res010=round(sum010/count010,2)
res1130=round(sum1130/count1130,2)
res3160=round(sum3160/count3160,2)
res6190=round(sum6190/count6190,2)
res91120=round(sum91120/count91120,2)
res120=round(sum120/count120,2)
sns.set(style="white", context="notebook")
sns.set_style('whitegrid', {'font.sans-serif':['simhei','Arial']})
y=[res010,res1130,res3160,res6190,res91120,res120]
x=['0-10分钟','11-30分钟','31-60分钟','61-90分钟','91-120分钟','120+分钟']
sns.barplot(x, y, palette="BuPu_r")

plt.title('时间统计')
plt.ylabel('作文题字符数')

plt.show()
print(y)

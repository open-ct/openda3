import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import matplotlib.pyplot as plt

data=pd.read_excel('20210809-2300人文素养作答情况.xlsx')
day=9
fail_exit=0
for i in range(len(data)):
    if not(pd.isnull(data['start_time'].iloc[i])):
        expire=datetime.strptime(data['expire_time'].iloc[i],"%Y-%m-%dT%H:%M:%S+08:00").strftime("%Y-%m-%d %H:%M:%S")
        finish=datetime(2021, 8, day,23,30,0)
        a=pd.to_datetime(finish)-pd.to_datetime(expire)
        if pd.isnull(data['stop_time'].iloc[i]):
            if a.days>=0:
                fail_exit=fail_exit+1
print(fail_exit)

finish_onday=0
for i in range(len(data)):
    if not(pd.isnull(data['start_time'].iloc[i])):
        expire=datetime.strptime(data['expire_time'].iloc[i],"%Y-%m-%dT%H:%M:%S+08:00").strftime("%Y-%m-%d %H:%M:%S")
        finish=datetime(2021, 8, day,23,30,0)
        start_time=datetime.strptime(data['start_time'].iloc[i],"%Y-%m-%dT%H:%M:%S+08:00").strftime("%Y-%m-%d %H:%M:%S")
        start=datetime(2021, 8, day,0,0,0)
        a=pd.to_datetime(finish)-pd.to_datetime(expire)
        b=pd.to_datetime(start_time)-pd.to_datetime(start)
        if (a.days>=0) and (b.days>=0):
            finish_onday=finish_onday+1
print(finish_onday)

sum_finish=0
for i in range(len(data)):
    if not(pd.isnull(data['start_time'].iloc[i])):
        expire=datetime.strptime(data['expire_time'].iloc[i],"%Y-%m-%dT%H:%M:%S+08:00").strftime("%Y-%m-%d %H:%M:%S")
        finish=datetime(2021, 8, day,23,30,0)
        a=pd.to_datetime(finish)-pd.to_datetime(expire)
        if a.days>=0:
            sum_finish=sum_finish+1
print(sum_finish)

over150=0
Over=[]
for i in range(len(data)):
    a=pd.to_datetime(data['stop_time'].iloc[i])
    b=pd.to_datetime(data['start_time'].iloc[i])
    temp=a-b
    tempmin=temp.seconds/60
    if tempmin>150:
        over150=over150+1
        Over.append(i)
#print(over150)

null_index=[]
for i in range(len(data)):
    if (pd.isnull(data['start_time'].iloc[i]))or(pd.isnull(data['stop_time'].iloc[i])):
        null_index.append(i)
data=data.drop(null_index)
data=data.drop(Over)

data['last_time'] = pd.to_datetime(data['stop_time']) - pd.to_datetime(data['start_time'])
time=[]
for i in range(len(data)):
    a=data['last_time'].iloc[i].seconds/60
    time.append(a)

data['last_time']=time

onday=[]
for i in range(len(data)):
    start_time=datetime.strptime(data['start_time'].iloc[i],"%Y-%m-%dT%H:%M:%S+08:00").strftime("%Y-%m-%d %H:%M:%S")
    start=datetime(2021, 8, day,0,0,0)
    a=pd.to_datetime(start_time)-pd.to_datetime(start)
    if a.days>=0:
        onday.append(i)
data_onday=data.iloc[onday]


def time10(data_onday,name):
    
    sum010=sum1020=sum2030=sum3040=sum4050=sum5060=sum6070=sum7080=sum8090=sum90100=sum100110=sum110120=sum120=0
    count010=count1020=count2030=count3040=count4050=count5060=count6070=count7080=count8090=count90100=count100110=count110120=count120=0
    
    for i in range(len(data_onday)):
        if 0<=data_onday['last_time'].iloc[i]<=10:
            count010=count010+1
        if 10<data_onday['last_time'].iloc[i]<=20:
            count1020=count1020+1
        if 20<data_onday['last_time'].iloc[i]<=30:
            count2030=count2030+1
        if 30<data_onday['last_time'].iloc[i]<=40:
            count3040=count3040+1
        if 40<data_onday['last_time'].iloc[i]<=50:
            count4050=count4050+1
        if 50<data_onday['last_time'].iloc[i]<=60:
            count5060=count5060+1
        if 60<data_onday['last_time'].iloc[i]<=70:
            count6070=count6070+1
        if 70<data_onday['last_time'].iloc[i]<=80:
            count7080=count7080+1
        if 80<data_onday['last_time'].iloc[i]<=90:
            count8090=count8090+1
        if 90<data_onday['last_time'].iloc[i]<=100:
            count90100=count90100+1
        if 100<data_onday['last_time'].iloc[i]<=110:
            count100110=count100110+1
        if 110<data_onday['last_time'].iloc[i]<=120:
            count110120=count110120+1
        if data_onday['last_time'].iloc[i]>120:
            count120=count120+1
            
    x=['0-10分钟','10-20分钟','20-30分钟','30-40分钟','40-50分钟','50-60分钟','60-70分钟','70-80分钟','80-90分钟','90-100分钟','100-110分钟','110-120分钟','超过120分钟']
    y=[count010,count1020,count2030,count3040,count4050,count5060,count6070,count7080,count8090,count90100,count100110,count110120,count120]
    recs=plt.bar(x,y)
    
    x=[rec.get_x() for rec in recs]#使用列表推导式获取bar的横坐标
    y=[rec.get_height() for rec in recs]#使用列表推导式获取bar的高度
    w=[rec.get_width() for rec in recs]#使用列表推导式获取bar的宽度
    textx=[x+width/2 for x,width in zip(x,w)]#计算标注的横坐标
    result=[plt.text(x,y,str(np.round(y)),size=20,ha = 'center') for x,y in zip(textx,y)]#使用列表推导式标注高度信息
    
    plt.title(name,size=30)
    plt.ylabel('人数')
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    plt.show()
#time10(data_onday,'8月9日当日每隔10分钟的作答人数图')
#time10(data,'截至目前每隔10分钟的作答人数图')

def stu_timelast(data_onday,name):
    
    sum010=sum1020=sum2030=sum3040=sum4050=sum5060=sum6070=sum7080=sum8090=sum90100=sum100110=sum110120=sum120=0
    count010=count1020=count2030=count3040=count4050=count5060=count6070=count7080=count8090=count90100=count100110=count110120=count120=0
    
    for i in range(len(data_onday)):
        if 0<=data_onday['last_time'].iloc[i]<=10:
            count010=count010+1
        if 10<data_onday['last_time'].iloc[i]<=20:
            count1020=count1020+1
        if 20<data_onday['last_time'].iloc[i]<=30:
            count2030=count2030+1
        if 30<data_onday['last_time'].iloc[i]<=40:
            count3040=count3040+1
        if 40<data_onday['last_time'].iloc[i]<=50:
            count4050=count4050+1
        if 50<data_onday['last_time'].iloc[i]<=60:
            count5060=count5060+1
        if 60<data_onday['last_time'].iloc[i]<=70:
            count6070=count6070+1
        if 70<data_onday['last_time'].iloc[i]<=80:
            count7080=count7080+1
        if 80<data_onday['last_time'].iloc[i]<=90:
            count8090=count8090+1
        if 90<data_onday['last_time'].iloc[i]<=100:
            count90100=count90100+1
        if 100<data_onday['last_time'].iloc[i]<=110:
            count100110=count100110+1
        if 110<data_onday['last_time'].iloc[i]<=120:
            count110120=count110120+1
        if data_onday['last_time'].iloc[i]>120:
            count120=count120+1
            
    x=['0-10分钟','10-20分钟','20-30分钟','30-40分钟','40-50分钟','50-60分钟','60-70分钟','70-80分钟','80-90分钟','90-100分钟','100-110分钟','110-120分钟','超过120分钟']
    y=[count010,count1020,count2030,count3040,count4050,count5060,count6070,count7080,count8090,count90100,count100110,count110120,count120]
    #<=10
    print(y[0])
    #<=20
    print(y[0]+y[1])
    #<=30
    print(y[0]+y[1]+y[2])
    
    n_sum=count010+count1020+count2030+count3040+count4050+count5060+count6070+count7080+count8090+count90100+count100110+count110120+count120
    n=[count010/n_sum,count1020/n_sum,count2030/n_sum,count3040/n_sum,count4050/n_sum,count5060/n_sum,count6070/n_sum,count7080/n_sum,count8090/n_sum,count90100/n_sum,count100110/n_sum,count110120/n_sum,count120/n_sum]
    
    pic=plt.pie(n,labeldistance = 1.1,autopct = '%3.1f%%')                          
    plt.title(name,size=30)
    plt.legend(x)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    plt.show()
#stu_timelast(data_onday,'8月9日当日总体作答时长分布')
stu_timelast(data,'截至目前总体作答时长分布')
#print(data['last_time'].mean())
#print(data_onday['last_time'].mean())
def school_count(data,add):
    schools=data['school'].unique()
    num10=[]
    num_sum=[]
    per=[]
    for idx in schools:
        temp_data=data[data['school'].isin([idx])]
        sum=0
        for j in range(len(temp_data)):
            if temp_data['last_time'].iloc[j]<10:
                sum=sum+1
        num10.append(sum)
        num_sum.append(len(temp_data))
        per.append(round(sum/len(temp_data),2))
    dataa={'school':schools,'num10':num10,'num_sum':num_sum,'per':per}
    dataa=pd.DataFrame(dataa)
    dataa = dataa.sort_values(by='per',ascending=False)
    dataa.to_excel(add)
    print(schools)
    print(num10)
    print(num_sum)
    print(per)
#school_count(data,'sum.xls')
#school_count(data_onday,'onday.xls')

student=[]
time=[]
num=[]
#学校信息统计
for i in range(len(data)):
    if (data['school'].iloc[i]=='四川省江油市第一中学')or(data['school'].iloc[i]=='江油一中'):
        if data['last_time'].iloc[i]<=10:
            temp_time=round(data['last_time'].iloc[i],2)*60
            minute=int(temp_time//60)
            second=int(temp_time%60)
            if minute==0:
                timems=str(second)+'秒'
            else:
                timems=str(minute)+'分'+str(second)+'秒'
            student.append(data['name'].iloc[i])
            time.append(timems)
            num.append(data['user'].iloc[i])
dta={'考号':num,'学生':student,'时间':time}
dta=pd.DataFrame(dta)
dta.to_excel('四川江油一中统计.xls')

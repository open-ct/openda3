# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:12:42 2021

@author: admin
"""

import pandas as pd
from datetime import datetime

book = pd.read_excel(r'11.05ticket_user.xlsx')


for i in book.index:

    col1 = book['start_time'][i]

    col2 =book['stop_time'][i]
    
    if(isinstance(col1,str)  and isinstance(col2,str)):
        
        tm1=datetime.fromisoformat(col1)#,"%Y-%m-%d %H:%M:%S")
        tm2=datetime.fromisoformat(col2)#,"%Y-%m-%d %H:%M:%S")
        tm=(tm2-tm1).seconds
        
        book.loc[i, '时长(秒)'] = tm
        

book.to_excel(r'11.05ticket_user2.xlsx')


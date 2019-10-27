#先用新表做之前的事情，再先删掉有的，没有的扔出来一个表
#before start, manually put 资产标签号 to the leftmost column
import pandas as pd
import numpy as np
import datetime
starttime = datetime.datetime.now()
df1 = pd.read_csv('表一.csv', encoding='gbk',engine = 'python')#DataFrame small 
df2 = pd.read_csv('表二.csv', encoding='gbk',engine ='python',header = 8,index_col = 0)#DataFrame big, watch out header position

#zcbqh1 is a list of zcbqh in df1，these create a data frame with only zcbqh.
zcbqh1 = list(df1.loc[:,'资产标签号']) #small
df2 = df2.T
zcbqh2 = df2.columns

#keep = filter(lambda x: x in zcbqh1,zcbqh2)

#result = df2.filter(items = keep)

#result = result.T

#csv accepts ansi encoding  

print('a') 
result = df2.filter(items = filter(lambda x : x not in zcbqh1,zcbqh2))
result = result.T
  
  
result.to_csv('58万.csv',encoding = 'ansi') 

endtime = datetime.datetime.now()
print (endtime - starttime)


    
    
    
    
    
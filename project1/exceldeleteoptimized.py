import pandas as pd
import numpy as np


df1 = pd.read_csv('表一.csv', encoding='gbk',engine = 'python')#DataFrame small 
print('a')
df2 = pd.read_csv('表二.csv', encoding='gbk',engine ='python',header = 8)#DataFrame big, watch out header position

#zcbqh1 is a list of zcbqh in df1，these create a data frame with only zcbqh.
zcbqh1 = df1.loc[:,'资产标签号'] #small
zcbqh2 = df2.loc[:,'资产标签号'] #big


j = 0
print('a')

#if condition meets, delete the row. Remeber that this method that loops once only works for sorted dataframe.
for i in range(len(zcbqh2)):
    print(i)
    if zcbqh1.values[j] == zcbqh2.values[i]:
        print('delete')
        df2.drop(df2.index[i])
        j+=1

    
    
df2.to_csv('Result1.csv',encoding = 'ansi') #finally save as utf8-BOm in another file
    
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

data = [] #List

#if condition meets, add the data into the list. Remeber that this method that loops once only works for sorted dataframe.
for i in range(len(zcbqh2)):
    if zcbqh1.values[j] == zcbqh2.values[i]:
        data.append(df2.iloc[i,30]) #good way write location use:to get a slice.
        j += 1
     

print(data)    
    

#put the data info into the excel.    
for i in range(len(data)):
	df1.iloc[i,25] = data[i]
	print(df1.iloc[i,25])

    

#csv accepts ansi encoding    
df1.to_csv('Result1.csv',encoding = 'ansi') #finally save as utf8-BOm in another file
    
    
    
    
    
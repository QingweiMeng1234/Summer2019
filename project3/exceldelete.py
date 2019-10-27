import pandas as pd
import numpy as np

#before start, manually put 资产标签号 to the leftmost column
df1 = pd.read_csv('表一.csv', encoding='gbk',engine = 'python')#DataFrame small 
df2 = pd.read_csv('表二.csv', encoding='gbk',engine ='python',header = 8,index_col = 0)#DataFrame big, watch out header position

#collect zcbqh1 into a list that needs to be filtered out.
zcbqh1 = list(df1.loc[:,'资产标签号']) #small

#transpose it, so that the data used for criteria becomes the title.
df2 = df2.transpose()

#collect the data that needs to be kept
zcbqh2 = df2.columns

keep = filter(lambda x: x not in zcbqh1,zcbqh2)


#filter according to the list created.
df2 = df2.filter(items = keep)

#transpose again
df2 = df2.T

df2.to_csv('finalResult.csv',encoding = 'ansi') #finally save as utf8-BOm in another file
    
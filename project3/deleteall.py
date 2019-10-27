import pandas as pd
import numpy as np
import datetime4
import os
starttime = datetime.datetime.now()
#open files and store them as dataframes
#before start, manually put 资产标签号 of the biggest csv to the leftmost column, run the bat file to put all csvs into one csv
df = pd.read_csv('60万.csv',encoding = 'gbk',engine='python')
df1 = pd.read_csv('new.csv',encoding = 'gbk',engine='python')

#biggest table's zcbqh
df = df.T
allzcbqh = df.columns

#zcbqh needs to be deleted
zcbqh = df1.loc['资产标签号']

#what needs to be keeped in the biggest
keepb = filter(lambda x: x not in zcbqh,allzcbqh)

#the data is in the small form, but not in the biggest form
keeps = filter(lambda x: x not in allzcbqh,zcbqh)

#filter in the biggest table.
df = df.filter(items = keepb)

#filter in the small table.
small = df.query()


#transpose back
df = df.T
#write into the file.
df.to_csv('所有删除之后的结果.csv',encoding = 'ansi')
keep.to_csv('总表里面没有但是小表里面有的数据.csv',encoding = 'ansi')
endtime = datetime.datetime.now()
print (endtime - starttime)
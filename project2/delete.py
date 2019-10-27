import pandas as pd
import numpy as np
import datetime
starttime = datetime.datetime.now()
#open files and store them as dataframes
#before start, manually put 资产标签号 to the leftmost column
df = pd.read_csv('60万.csv',encoding = 'gbk',engine='python')
df1 = pd.read_csv('地铁.csv',encoding = 'gbk',engine='python')
df2 = pd.read_csv('电缆.csv',encoding = 'gbk',engine='python')
df3 = pd.read_csv('杆路.csv',encoding = 'gbk',engine='python')
df4 = pd.read_csv('共用设备.csv',encoding = 'gbk',engine='python')
df5 = pd.read_csv('光交箱.csv',encoding = 'gbk',engine='python')
df6 = pd.read_csv('光缆.csv',encoding = 'gbk',engine='python')
df7 = pd.read_csv('室分.csv',encoding = 'gbk',engine='python')
df8 = pd.read_csv('2018.09划拨管道（含已确认）.csv',encoding = 'gbk',engine='python')
print('a')

#put all zcbqh into one csv. data is a series
data = df1.loc[:,'资产标签号']
data += df2.loc[:,'资产标签号']
data += df3.loc[:,'资产标签号']
data += df4.loc[:,'资产标签号']
data += df5.loc[:,'资产标签号']
data += df6.loc[:,'资产标签号']
data += df7.loc[:,'资产标签号']
data += df8.loc[:,'资产标签号']
print(data)

#biggest table's zcbqh
df = df.T
allzcbqh = df.columns

#split into delete and keep
delete = filter(lambda x: x not in data,allzcbqh)
print('b')
keep = filter(lambda x: x not in allzcbqh,data)
print('c')
#filter in the biggest table.
df = df.filter(items = delete)
print('d')

#transpose back
df = df.T
#write into the file.
df.to_csv('所有删除之后的结果.csv',encoding = 'ansi')
keep.to_csv('总表里面没有但是小表里面有的数据.csv',encoding = 'ansi')
endtime = datetime.datetime.now()
print (endtime - starttime)
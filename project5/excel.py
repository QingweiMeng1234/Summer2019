import pandas as pd
import numpy as np
import datetime
import os
#part 1 补全4万条
starttime = datetime.datetime.now()
# #open files and store them as dataframes，put all deletes into one csv manually
# df = pd.read_csv('表二.csv',encoding = 'gbk',engine='python',header = 8)
# df1 = pd.read_csv('天府新区现场盘点（上市V2）201806.csv',encoding = 'gbk',engine='python')
       
# #sort df and df1, in order to match
# df = df.sort_values('资产标签号')
# df1 = df1.sort_values('资产标签号')
# df1.to_csv('天府新区现场盘点（上市V2）补全部分,sorted.csv',encoding = 'ansi')
# keep = df.loc[df['资产标签号'].isin(df1['资产标签号'])]
# #filter out what needed to be put in
# keep = keep.filter(items = ['成本','资产净值','资产净额','残值','本期折旧额','本年折旧额','员工姓名','地点说明'])
 
# keep.to_csv('天府新区现场盘点（上市V2）补全部分.csv',encoding = 'ansi')

# #manually copy keep on the right of df1


#part 2 筛选那些在2019表里，那些不在2019表里
df2019 = pd.read_csv('CUX_CMCC资产明细报表-3889FA-201906.csv',encoding = 'gbk',engine='python',header = 8)
dfpart1 = pd.read_csv('天府新区现场盘点（上市V2）补全部分,sorted.csv',encoding = 'gbk',engine='python')
#in 2019
keep1 = dfpart1.loc[dfpart1['资产标签号'].isin(df2019['资产标签号'])]
#not in 2019
keep2 = dfpart1.loc[~dfpart1['资产标签号'].isin(df2019['资产标签号'])]

keep1.to_csv('天府新区现场盘点（上市V2）补全,在2019年表里.csv',encoding = 'ansi')
keep2.to_csv('天府新区现场盘点（上市V2）补全,不在2019年表里.csv',encoding = 'ansi')
endtime = datetime.datetime.now()
print (endtime - starttime)
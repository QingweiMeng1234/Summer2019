import pandas as pd
import numpy as np
import datetime
import os
starttime = datetime.datetime.now()
#open files and store them as dataframes，put all deletes into one csv manually
df = pd.read_csv('Copy of CUX_CMCC资产明细报表-3889FA-201906.csv',encoding = 'gbk',engine='python',header = 8)


# result = pd.DataFrame()
# for i,j in df.groupby(['location','project_code']): # i are the values in the columns, a tuple; g is a dataframe with all information.
 # #按照相同的地址和项目编号分类   
    # if j['启用日期'].drop_duplicates().size > 1: #如果有两个日期的话，即有不同日期的话
        # result = pd.concat([result,j]) #把它加入dataframe,but concat one by one is too slow since it involves many copying. a better way is below
        
# result.to_csv('2.csv',encoding = 'ansi',index = False)


#同一地点超过10条
keep = []
for i,j in df.groupby(['location','project_code']): 
    if j['资产标签号'].size > 9:
        keep.append(j)

result = pd.concat(keep,axis = 0)
result.to_csv('3.csv',encoding = 'ansi',index = False)



endtime = datetime.datetime.now()
print (endtime - starttime)

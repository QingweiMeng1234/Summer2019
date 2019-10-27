import pandas as pd
import numpy as np
import datetime
import os
#part 1
# starttime = datetime.datetime.now()
# #open files and store them as dataframes，put all deletes into one csv manually
# df = pd.read_csv('CUX_CMCC资产明细报表-3889FA-201906.csv',encoding = 'gbk',engine='python',header = 8)
# df1 = pd.read_csv('4万条抽出来补全的数据结果.csv',encoding = 'gbk',engine='python')
      
# #201906中有的部分
# keep1 = df1.loc[df1['资产标签号'].isin(df['资产标签号'])]

# #201906中没有的部分
# keep2 = df1.loc[~df1['资产标签号'].isin(df['资产标签号'])]
 
# keep1.to_csv('2018年补全的4万条中201906总表中有的部分.csv',encoding = 'ansi',index = False)
# keep2.to_csv('2018年补全的4万条中201906总表中无的部分.csv',encoding = 'ansi',index = False)

# endtime = datetime.datetime.now()
# print (endtime - starttime)

#part 2
# starttime = datetime.datetime.now()

# df = pd.read_csv('CUX_CMCC资产明细报表-3889FA-201906.csv',encoding = 'gbk',engine='python',header = 8)

# os.chdir('D:\Python\Excel\project4\project4_outputs')#maybe redundant

# files = os.listdir('D:\Python\Excel\project4\project4_outputs')

# for file in files:
    # if file[len(file)-3:len(file)] == 'csv':
        # print(file)
        # #read each file
        # df1 = pd.read_csv(file,encoding = 'gbk',engine='python')
        # #filter data according to the instruction
        # #201906中有的部分
        # keep1 = df1.loc[df1['资产标签号'].isin(df['资产标签号'])]

        # #201906中没有的部分
        # keep2 = df1.loc[~df1['资产标签号'].isin(df['资产标签号'])]
        
        # #dont try to write into excel, too slow(27min). write into csv then manually transfer into excel(2min)
        # keep1.to_excel('%s中201906总表中有的部分.xlsx'%file[:len(file)-4],encoding = 'unicode',index = False)
        # keep2.to_excel('%s中201906总表中无的部分.xlsx'%file[:len(file)-4],encoding = 'unicode',index = False)
# endtime = datetime.datetime.now()
# print (endtime - starttime)

#part 4
starttime = datetime.datetime.now()
#open files and store them as dataframes，put all deletes into one csv manually
df2019 = pd.read_csv('CUX_CMCC资产明细报表-3889FA-201906.csv',encoding = 'gbk',engine='python',header = 8)
df2018 = pd.read_csv('201806剔除哑资源和4万条.csv',encoding = 'gbk',engine='python')

#merge seems unusable because of different columns of each chart. 
     
# #在201906中，201806有的部分
# keep1 = df2019.loc[df2019['资产标签号'].isin(df2018['资产标签号'])]

#在201806中，201906有的部分
keep2 = df2018.loc[df2018['资产标签号'].isin(df2019['资产标签号'])]


keep1.to_csv('2018年和2019年都有的（1）.csv',encoding = 'ansi',index = False)
keep2.to_csv('2018年和2019年都有的（2）.csv',encoding = 'ansi',index = False)

endtime = datetime.datetime.now()
print (endtime - starttime)

import pandas as pd
import numpy as np
import datetime
import os
starttime = datetime.datetime.now()
#open files and store them as dataframes，put all deletes into one csv manually
df = pd.read_csv('60万.csv',encoding = 'gbk',engine='python')
dfd = pd.read_csv('alldeletes.csv',encoding = 'gbk',engine='python')
       
#this time, use isin() to filter


#things needs to be deleted(this is the fastest way)
keepbig = df.loc[~df['资产标签号'].isin(dfd['资产标签号'])]

#cells that needs to be thrown into an new file. ~ represents is not in
keepsmall = dfd.loc[~dfd['资产标签号'].isin(df['资产标签号'])]
 
keepbig.to_csv('201806剔除哑资源和4万条.csv',encoding = 'ansi')
keepsmall.to_csv('201806总表里无但哑资源有.csv',encoding = 'ansi')

endtime = datetime.datetime.now()
print (endtime - starttime)
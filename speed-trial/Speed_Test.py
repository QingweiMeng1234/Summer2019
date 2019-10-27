import pandas as pd
import numpy as np
import datetime
import os
starttime1 = datetime.datetime.now()

#run the bat file to put all csvs into one csv
#open files and store them as dataframes
df = pd.read_csv('表二.csv',encoding = 'gbk',engine='python',header = 8)
df1 = pd.read_csv('表一.csv',encoding = 'gbk',engine='python')
endtime1 = datetime.datetime.now()
#reading files takes 24 seconds
print (endtime1 - starttime1)

starttime2 = datetime.datetime.now()
#this time, use isin() to filter
#things needs to be deleted(this is the fastest way)，~ represents not
keep = df.loc[~df['资产标签号'].isin(df1['资产标签号'])]
endtime2 = datetime.datetime.now()
# deletion only takes 0.4 second
print (endtime2 - starttime2)
starttime3 = datetime.datetime.now()

#writes into file takes 16 seconds
keep.to_csv('keep.csv',encoding = 'ansi')

endtime3 = datetime.datetime.now()
print (endtime3 - starttime3)

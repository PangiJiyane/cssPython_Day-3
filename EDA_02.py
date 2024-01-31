# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:34:58 2024

@author: ccm
"""

import pandas as pd
import matplotlib.pyplot as plt
df= pd.pandas.read_csv("time_series_data.csv")
print(df.info())

df['Date']=pd.to_datetime(df['Date'],format="%Y-%m-%d")
print (df.info())

#plt.plot(df['Date'])                       
#df= pd.pandas.read_csv("time_series_data.chat files")                                                      
#df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time


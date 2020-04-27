#%%
from pathlib import Path

import requests
import numpy as np
import pandas as pd

import pandas_profiling
from pandas_profiling.utils.cache import cache_file

# %%
file_name = cache_file(
    "apple.csv",
    "https://raw.githubusercontent.com/anarinsk/adp-apple_mobility_trend/master/data/applemobilitytrends-2020-04-23.csv",
)
    
df = pd.read_csv(file_name)

#%%
tmplist = zip(df.columns[3:], "time_" +  df.columns[3:])
df.rename(columns = dict(tmplist), inplace=True)
#
df = pd.wide_to_long(df, stubnames='time', i=['geo_type', 'region', 'transportation_type'], j='date', sep='_', suffix='.*')
df = df.reset_index()
#
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d') 
df

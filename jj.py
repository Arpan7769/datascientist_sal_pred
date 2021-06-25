# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:43:51 2021

@author: DELL
"""
import numpy as np
import pandas as pd

df=pd.read_csv('salary_data_cleaned.csv')
df.drop('State', axis=1, inplace=True)
df['State']=df['Location'].apply(lambda x: x.split(', ')[-1])
print(df['State'])
df.to_csv('salary_data_cleaned.csv', index=False)
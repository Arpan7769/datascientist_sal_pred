# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:15:11 2021

@author: DELL
"""

import scraper as sc
import pandas as pd

path="C:/Users/DELL/Documents/datascientist_sal_pred/chromedriver"
df=sc.get_jobs('data scientist', 200, False, path, 15)

df.to_csv('data_new.csv')
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:47:40 2021

@author: DELL
"""
import pandas as pd

df=pd.read_csv('data1.csv')

#Salary Parsing
df=df[df['Salary Estimate']!='-1']
df['Salary Estimate']=df['Salary Estimate'].apply(lambda x: x.split('(')[0])

remove_kd=df['Salary Estimate'].apply(lambda x: x.lower().replace('$','').replace('k', ''))

min_sal=remove_kd.apply(lambda x: int(x.split(' ')[0]))
max_sal=remove_kd.apply(lambda x: int(x.split(' ')[2]))

df['min_sal']=min_sal
df['max_sal']=max_sal
df['avg_sal']=(df['min_sal']+df['max_sal'])/2

df['Location']=df['Location'].astype('str') 
                                     #.apply(lambda x: str(x))
#Location State
df.fillna(0)
df.replace('nan', '0, 0')
df['State']=df['Location'].apply(lambda x: x.split(', ')[-1])
df['State'].value_counts()

#Exploring columns
df.columns
df.info()

#Company's Age
df['Age']=df.Founded.apply(lambda x: x if x < 1 else 2020-x)

#Parsing job description

#Python
df['Python']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.Python.value_counts()

#R
df['R']=df['Job Description'].apply(lambda x: 1 if 'r' in x.lower() else 0)
df.R.value_counts()

#SQL
df['SQL']=df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.SQL.value_counts()

#aws
df['AWS']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.AWS.value_counts()

#SPARK
df['Spark']=df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.Spark.value_counts()

#Dropping irrelevant columns
df_clean=df
df_clean.to_csv('cleaned_data.csv', index=False)



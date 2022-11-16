# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 04:53 2022

@author: Annie Dhawan
"""


import pandas as pd
import numpy as np

df = pd.read_csv('glassdoor_jobs.csv')


#1st salary parsing
#getting to know if its hourly salary or the salary is provided by employer
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])
#removing k and dollars so that we will only have numbers
salary_min_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
#removing Per Hour and Employer Provided Salary:
salary_min_pe = salary_min_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))
#3 new salary cols
df['min_salary'] = salary_min_pe.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = salary_min_pe.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#2nd Company Name
df['Company Name'] = df['Company Name'].apply(lambda x: x.split('\n')[0])

#3rd state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#4th age of company
df['age'] = df['Founded'].apply(lambda x: x if x <1 else 2020 - x)


#5th from job discripption feature
# python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

# r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)


# spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)


# aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)


# excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)


#export to local computer in CSV Format.
df_output = df.drop(['Unnamed: 0'], axis =1)

df_output.to_csv('Glassdoor_salary_data_cleaned.csv',index = False)

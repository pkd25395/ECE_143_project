# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:56:44 2020

@author: azrae
"""
from collections import OrderedDict


import numpy as np
import pandas as pd

from bokeh.plotting import figure, output_file, show
from project_functions import merge_MinMax_Salary, count_members_by_column, clean_and_merge, plot_radial_column_chart


    
##===============Load Data =======================##

col_list = ["Job_title","Company","State","City","Min_Salary","Max_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]
files_list = ["Data_Job_NY.csv"
                ,"Data_Job_SF.csv"
                ,"Data_Job_TX.csv"
                ,"Data_Job_WA.csv"]
df_NY = pd.read_csv(files_list[0],usecols=col_list)
df_SF = pd.read_csv(files_list[1],usecols=col_list)
df_TX = pd.read_csv(files_list[2],usecols=col_list)
df_WA = pd.read_csv(files_list[3],usecols=col_list)

##===================CLEAN DATA===================##
##===================JOIN ALL DATAFRAMES===================##
df_allFrames = [df_NY, df_SF, df_TX, df_WA]
df_combined = clean_and_merge(df_allFrames)
df_minmax = merge_MinMax_Salary(df_combined)

df_minmaxAerospace = df_minmax[df_minmax["Industry"]=="Aerospace & Defense"]
#df_minmaxAerospace.to_csv('Aerospace.csv')
df_minmaxFinance = df_minmax[df_minmax["Industry"]=="Finance"]
df_minmaxBiotech = df_minmax[df_minmax["Industry"]=="Biotech & Pharmaceuticals"]
df_minmaxBusiness = df_minmax[df_minmax["Industry"]=="Business Services"]
df_minmaxInfoTech = df_minmax[df_minmax["Industry"]=="Information Technology"]


##===============GET TOP COMPANYS  ===========================#
top_companies_num = 3
top_company_Aerospace_dict = {}
top_company_Aerospace = list(df_minmaxAerospace['Company'].value_counts(sort=True).index[0:3])
top_company_Aerospace_count = df_minmaxAerospace['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_Aerospace_dict[top_company_Aerospace[i]] = top_company_Aerospace_count[i]
#print('Asrospace',top_company_Aerospace_dict)    

top_company_Finance_dict = {}
top_company_Finance = list(df_minmaxFinance['Company'].value_counts(sort=True).index[0:3])
top_company_Finance_count = df_minmaxFinance['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_Finance_dict[top_company_Finance[i]] = top_company_Finance_count[i]
#print('Finance',top_company_Finance_dict)    


top_company_Biotech_dict = {}
top_company_Biotech = list(df_minmaxBiotech['Company'].value_counts(sort=True).index[0:3])
top_company_Biotech_count = df_minmaxBiotech['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_Biotech_dict[top_company_Biotech[i]] = top_company_Biotech_count[i]
#print('Biotech',top_company_Biotech_dict)    

# get rid of repeated companys
top_company_Business_dict = {}
top_company_Business = list(df_minmaxBusiness['Company'].value_counts(sort=True).index[0:4])
top_company_Business_count = df_minmaxBusiness['Company'].value_counts(sort=True)[0:4].values
for i in range(top_companies_num + 1):
    top_company_Business_dict[top_company_Business[i]] = top_company_Business_count[i]
#print('Business',top_company_Business_dict) 

top_company_InfoTech_dict = {}
top_company_InfoTech = list(df_minmaxInfoTech['Company'].value_counts(sort=True).index[0:3])
top_company_InfoTech_count = df_minmaxInfoTech['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_InfoTech_dict[top_company_InfoTech[i]] = top_company_InfoTech_count[i]
#print('InfoTech',top_company_InfoTech_dict) 




##================Calculate the salarys and create the dataframe ===========================#
df_top_salary = OrderedDict({'Industry':['Asrospace','Finance','Biotech','Business','InfoTech']})

df_top_salary_Aerospace = {}
for company in top_company_Aerospace:

    total_salary = df_minmaxAerospace.loc[df_minmaxAerospace['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Aerospace_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Aerospace[company] = avg_salary 
    #print(company,avg_salary)
    
print('Aerospace')
print(df_top_salary_Aerospace)

for company in df_top_salary_Aerospace:
    df_top_salary[company] = df_top_salary_Aerospace[company]
    




df_top_salary_Finance = {}
for company in top_company_Finance:
    total_salary = df_minmaxFinance.loc[df_minmaxFinance['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Finance_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Finance[company] = avg_salary 
    #print(company,avg_salary)
    
print('Finance')
print(df_top_salary_Finance)

for company in df_top_salary_Finance:
    df_top_salary[company] = df_top_salary_Finance[company]
    
df_top_salary_Biotech = {}
for company in top_company_Biotech:
    total_salary = df_minmaxBiotech.loc[df_minmaxBiotech['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Biotech_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Biotech[company] = avg_salary 
    #print(company,avg_salary)
print('Biotech')
print(df_top_salary_Biotech)

for company in df_top_salary_Biotech:
    df_top_salary[company] = df_top_salary_Biotech[company]
    

df_top_salary_Business= {}
for company in top_company_Business:
    total_salary = df_minmaxBusiness.loc[df_minmaxBusiness['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Business_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Business[company] = avg_salary 
    #print(company,avg_salary)
# get rid of repeated companys 
df_top_salary_Business.pop('Booz Allen Hamilton Inc.')
print('Business')
print(df_top_salary_Business)

for company in df_top_salary_Business:
    df_top_salary[company] = df_top_salary_Business[company]

df_top_salary_InfoTech= {}
for company in top_company_InfoTech:
    total_salary = df_minmaxInfoTech.loc[df_minmaxInfoTech['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_InfoTech_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_InfoTech[company] = avg_salary 
    #print(company,avg_salary)

print('InfoTech')
print(df_top_salary_InfoTech)

for company in df_top_salary_InfoTech:
    df_top_salary[company] = df_top_salary_InfoTech[company]


df = pd.DataFrame(data=df_top_salary)
#print(df.head())

min_scale = 1000
max_scale = 10000
plot_radial_column_chart(df,min_scale,max_scale)


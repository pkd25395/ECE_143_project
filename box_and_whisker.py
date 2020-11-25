
'''
REDO THIS FOR ONLY for TOP 5 Industries: 
INDUSTRY                            COUNT
Finance                             181.0
Health Care                         193.0
Biotech & Pharmaceuticals           289.0
Business Services                   310.0
Information Technology              508.0

AND FOR TOP 5 COMPANIES of those Industries:
COMPANY                         COUNT
Banfield Pet Hospital              60
Booz Allen Hamilton                80
Genentech                         118
Veterinary Emergency Group        120
National Debt Relief              120
'''

import numpy as np
import pandas as pd
# conda install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
#ensure file bw_functions.py is in same directory as box_and_whisker.py
from project_functions import merge_MinMax_Salary, count_members_by_column

# want to create new dataframe from job listings csv to have
# a column with min or max corresponding to salary as the min or the max

col_list = ["Job_title","Company","State","City","Min_Salary","Max_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]
files_list = ["Data_Job_NY.csv"
                ,"Data_Job_SF.csv"
                ,"Data_Job_TX.csv"
                ,"Data_Job_WA.csv"]
df_NY = pd.read_csv(files_list[0],usecols=col_list)
df_SF = pd.read_csv(files_list[1],usecols=col_list)
df_TX = pd.read_csv(files_list[2],usecols=col_list)
df_WA = pd.read_csv(files_list[3],usecols=col_list)

#create dataframe with min and max salary merged to one salary column, with additional column indicating min or max
#do this for all geographic areas
df_NY_minmax = merge_MinMax_Salary(df_NY)
df_SF_minmax = merge_MinMax_Salary(df_SF)
df_TX_minmax = merge_MinMax_Salary(df_TX)
df_WA_minmax = merge_MinMax_Salary(df_WA)

##===================JOIN ALL DATAFRAMES===================##
frames_all = [df_NY_minmax, df_SF_minmax, df_TX_minmax, df_WA_minmax]
df_minmax = pd.concat(frames_all)

##===================COUNT NUMBER OF POSTS BY COMPANY===================##
print(count_members_by_column(df_minmax,"Industry"))
print(count_members_by_column(df_minmax,"Company"))

#create dataframe with only top 5 industries by number of posts
df_minmaxFinance = df_minmax[df_minmax["Industry"]=="Finance"]
df_minmaxHealthcare = df_minmax[df_minmax["Industry"]=="Health Care"]
df_minmaxBiotech = df_minmax[df_minmax["Industry"]=="Biotech & Pharmaceuticals"]
df_minmaxBusiness = df_minmax[df_minmax["Industry"]=="Business Services"]
df_minmaxInfoTech = df_minmax[df_minmax["Industry"]=="Information Technology"]
frames_topInd = [df_minmaxFinance, df_minmaxHealthcare, df_minmaxBiotech, df_minmaxBusiness, df_minmaxInfoTech]
df_minmax = pd.concat(frames_topInd)

#create dataframe with only top 5 companies by number of posts
df_minmaxMiddle = df_minmax[df_minmax["Company"]=="Middle Village Radiology"]
df_minmaxBooz = df_minmax[df_minmax["Company"]=="Booz Allen Hamilton"]
df_minmaxGenentech = df_minmax[df_minmax["Company"]=="Genentech"]
df_minmaxVetEmGroup = df_minmax[df_minmax["Company"]=="Veterinary Emergency Group"]
df_minmaxNatDebtRel = df_minmax[df_minmax["Company"]=="National Debt Relief"]
frames_Co = [df_minmaxMiddle, df_minmaxBooz, df_minmaxGenentech, df_minmaxVetEmGroup, df_minmaxNatDebtRel]
df_minmaxCo = pd.concat(frames_Co)

##===================FILTER OUTLIERS===================##
Q1 = df_minmax['Salary'].quantile(0.25)
Q3 = df_minmax['Salary'].quantile(0.75)
IQR = Q3 - Q1    #IQR is interquartile range. 

filter = (df_minmax['Salary'] >= Q1 - 1.5 * IQR) & (df_minmax['Salary'] <= Q3 + 1.5 *IQR)
df_minmax.loc[filter]  

##===================CREATE BOX & WHISKER PLOT===================##
sns.set(font_scale=0.65)
ax = sns.boxplot( x=df_minmax["Industry"], y=df_minmax["Salary"], hue=df_minmax["Min_Max"])
plt.title("Salary by Industry")
#add jitter plot over boxplot
#ax = sns.swarmplot(x=df_minmax["Industry"], y=df_minmax["Salary"], color='gray', s=1)
plt.show()
ax = sns.boxplot(x=df_minmaxCo["Company"], y=df_minmaxCo["Salary"], hue=df_minmaxCo["Min_Max"])
plt.title("Salary by Company")
plt.show()

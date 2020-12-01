
'''
Harker Russell, Team 19, ECE142, FA20

This script is made to generate box and whisker plots from glassdoor datasets
scraped from New York, Texas, Washington and San Francisco areas
over the spring of 2020. The idea is to see if there is an appreciable difference
in salary between different industries (5 with the most job posts), and the same 
between different companies within those industries. 

REDO THIS FOR ONLY for TOP 5 Industries: 
INDUSTRY                            COUNT
Aerospace & Defense                  252.0
Finance                              302.0
Biotech & Pharmaceuticals            518.0
Business Services                    620.0
Information Technology              1016.0

AND FOR TOP 5 COMPANIES of those Industries:
COMPANY                             COUNT
Facebook                              42
Amazon                                44
Leidos                                46
Genentech                            118
National Debt Relief                 120
'''
try:
    import numpy as np
    import pandas as pd
    # conda install seaborn
    import seaborn as sns
    import matplotlib.pyplot as plt
    #ensure file bw_functions.py is in same directory as box_and_whisker.py
    from project_functions import merge_MinMax_Salary, count_members_by_column, clean_and_merge, gen_and_disp_boxWhiskerPlot
except Exception as e:
    print("some modules are missing, try installing seaborn with 'conda install seaborn' and check that project_functions.py is in same directory")
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

##===================CLEAN DATA===================##
##===================JOIN ALL DATAFRAMES===================##
df_allFrames = [df_NY, df_SF, df_TX, df_WA]
df_combined = clean_and_merge(df_allFrames)
df_minmax = merge_MinMax_Salary(df_combined)

##===================Uncomment below to COUNT NUMBER OF POSTS BY INDUSTRY===================##
## to print to console uncommend the next line and run script
#print(count_members_by_column(df_minmax,"Industry"))
## to write count to csv uncomment next 2 lines and run script
#df_coCount = count_members_by_column(df_minmax,"Industry")
#df_coCount.to_csv('Data_Industry_Count.csv')

##===================CREATE DF W/ONLY TOP 5 INDUSTRIES WRT # OF POSTS===================##
df_minmaxFinance = df_minmax[df_minmax["Industry"]=="Aerospace & Defense"]
df_minmaxHealthcare = df_minmax[df_minmax["Industry"]=="Finance"]
df_minmaxBiotech = df_minmax[df_minmax["Industry"]=="Biotech & Pharmaceuticals"]
df_minmaxBusiness = df_minmax[df_minmax["Industry"]=="Business Services"]
df_minmaxInfoTech = df_minmax[df_minmax["Industry"]=="Information Technology"]
frames_topInd = [df_minmaxFinance, df_minmaxHealthcare, df_minmaxBiotech, df_minmaxBusiness, df_minmaxInfoTech]
df_minmax = pd.concat(frames_topInd)


##===================Uncomment below to COUNT NUMBER OF POSTS BY COMPANY===================##
## to print to console uncommend the next line and run script
#print(count_members_by_column(df_minmax,"Company"))
## to write count to csv uncomment next 2 lines and run script
#df_coCount = count_members_by_column(df_minmax,"Company")
#df_coCount.to_csv('Data_Company_Count.csv')

##===================CREATE DF W/ONLY TOP 5 INDUSTRIES WRT # OF POSTS===================##
df_minmaxAmazon = df_minmax[df_minmax["Company"]=="Amazon"]
df_minmaxFacebook = df_minmax[df_minmax["Company"]=="Facebook"]
df_minmaxLeidos = df_minmax[df_minmax["Company"]=="Leidos"]
df_minmaxGenentech = df_minmax[df_minmax["Company"]=="Genentech"]
df_minmaxNatDebtRel = df_minmax[df_minmax["Company"]=="National Debt Relief"]
frames_Co = [df_minmaxAmazon, df_minmaxFacebook, df_minmaxLeidos, df_minmaxGenentech, df_minmaxNatDebtRel]
df_minmaxCo = pd.concat(frames_Co)

##===================FILTER OUTLIERS===================##
Q1 = df_minmax['Salary'].quantile(0.25)
Q3 = df_minmax['Salary'].quantile(0.75)
IQR = Q3 - Q1    #IQR is interquartile range. 
filter = (df_minmax['Salary'] >= Q1 - 1.5 * IQR) & (df_minmax['Salary'] <= Q3 + 1.5 *IQR)
df_minmax.loc[filter]  

##===================CREATE & DISPLAY BOX & WHISKER PLOTS===================##

gen_and_disp_boxWhiskerPlot(df_minmax,"Salary by Industry","Industry","Salary","Min_Max")
""" sns.set(font_scale=1.1)
plt.figure(figsize=(12,8))
sns.boxplot( x=df_minmax["Industry"], y=df_minmax["Salary"], hue=df_minmax["Min_Max"])
plt.title("Salary by Industry") #1300x850
plt.show() """
plt.figure(figsize=(12,8))
sns.boxplot(x=df_minmaxCo["Company"], y=df_minmaxCo["Salary"], hue=df_minmaxCo["Min_Max"])
plt.title("Salary by Company")
plt.show()

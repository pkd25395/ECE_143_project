"""
This script is made to generate word clouds from glassdoor datasets
scraped from New York, Texas, Washington and San Francisco areas
over March and April 2020. The idea is to see the prevalence of key
terms from qualifications desired from companies looking for data scientists

REDO THIS FOR ONLY for TOP 5 Industries: 
INDUSTRY                            COUNT
Aerospace & Defense                  252.0
Finance                              302.0
Biotech & Pharmaceuticals            518.0
Business Services                    620.0
Information Technology              1016.0

AND FOR TOP 5 COMPANIES of those Industries:
COMPANY                         COUNT
Facebook                          42
Amazon                            44
Leidos                            46
Genentech                        118
National Debt Relief             120
"""
#try:
#import os
#import sys
import pandas as pd
#ensure file project_functions.py is accessible as word_clouds.py
from project_functions import remove_non_keywords, create_JobDescription_string, generate_and_display_wordcloud, clean_and_merge
#except Exception as e:
#    print("some modules are missing, try installing ")

#import .csvs as dataframes
col_list = ["Job_title","Company","State","City","Min_Salary","Max_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]
files_list =    ["Data_Job_NY.csv"
                ,"Data_Job_SF.csv"
                ,"Data_Job_TX.csv"
                ,"Data_Job_WA.csv"]
df_NY = pd.read_csv(files_list[0],usecols=col_list)
df_SF = pd.read_csv(files_list[1],usecols=col_list)
df_TX = pd.read_csv(files_list[2],usecols=col_list)
df_WA = pd.read_csv(files_list[3],usecols=col_list)

# remove non-data science jobs from dataset
""" df_NY = df_NY[df_NY['Max_Salary'] >= 0]
df_SF = df_SF[df_SF['Max_Salary'] >= 0]
df_TX = df_TX[df_TX['Max_Salary'] >= 0]
df_WA = df_WA[df_WA['Max_Salary'] >= 0] """
# remove by if data isn't in job description

#join all above dataframes into one dataframe
""" frames_all = [df_NY, df_SF, df_TX, df_WA]
df_combined = pd.concat(frames_all) """

# clean and merge data into single frame
df_allFrames = [df_NY, df_SF, df_TX, df_WA]
df_combined = clean_and_merge(df_allFrames)

##===============================================================================================##
## INDUSTRY
##===============================================================================================##

##===================CREATE JOB DESCRIPTION STRINGS BY INDUSTRY===================##
## Aerospace
str_Aero = create_JobDescription_string(df_combined,"Industry","Aerospace & Defense")
## Finance 
str_Finance = create_JobDescription_string(df_combined,"Industry","Finance")
## Biotech
str_Biotech = create_JobDescription_string(df_combined,"Industry","Biotech & Pharmaceuticals")
## Business
str_Business = create_JobDescription_string(df_combined,"Industry","Business Services")
## IT
str_IT = create_JobDescription_string(df_combined,"Industry","Information Technology")

##===================REMOVE ALL NON-KEYWORDS FROM STRINGS===================##
keyword_list = ["models","statistics","probability","machine learning","data science","numpy","pandas","sql","scikit-learn","r","databases","database","team",
"MSc","PhD","mathematics","computer science","physics","research","data","relational databases","python","c++","matlab","modeling","dbt","snowflake",
"mode analytics","fivetran","Census","amplitude","segment","tensorflow","optimization","prediction","engineering","data engineering","neural networks",
"bigquery","pyspark","degree","bachelor","bachelors","scala","data analysis","analysis","data visualization","algorithms","classification",
"model","java","javascript","caffe","deep learning","data processing","hpc","hadoop","ms","bs","m.s.","b.s.","masters","master","stem","postgres",
"software development","agile","querying","experience","skills","credentials","hands-on","communication","presentation","ownership"]
## Aerospace
str_Aero = remove_non_keywords(str_Aero, keyword_list)
## Finance 
str_Finance = remove_non_keywords(str_Finance, keyword_list)
## Biotech
str_Biotech = remove_non_keywords(str_Biotech, keyword_list)
## Business
str_Business = remove_non_keywords(str_Business, keyword_list)
## IT
str_IT = remove_non_keywords(str_IT, keyword_list)

##===================CREATE & DISPLAY WORDCLOUDS FOR INDUSTRIES===================##
## Aerospace
generate_and_display_wordcloud(str_Aero,"Aerospace & Defense","cloud.png") #8iGbRApyT.png")
## Finance
generate_and_display_wordcloud(str_Finance,"Finance","cloud.png") #dollar.jpg")
## Biotech
generate_and_display_wordcloud(str_Biotech,"Biotech & Pharmaceuticals","cloud.png") #flask.jpg")
## Business
generate_and_display_wordcloud(str_Business,"Business Services","cloud.png") #tie.jpg")
## IT
generate_and_display_wordcloud(str_IT,"Information Technology","cloud.png") #cursor.jpg")

##===============================================================================================##
## COMPANY
##===============================================================================================##

##===================CREATE JOB DESCRIPTION STRINGS BY COMPANY===================##
## Facebook
str_Facebook = create_JobDescription_string(df_combined,"Company","Facebook")
## Amazon 
str_Amazon = create_JobDescription_string(df_combined,"Company","Amazon")
## Leidos
str_Leidos = create_JobDescription_string(df_combined,"Company","Leidos")
## Genentech
str_Genentech = create_JobDescription_string(df_combined,"Company","Genentech")
## National Debt Relief
str_National = create_JobDescription_string(df_combined,"Company","National Debt Relief")

##===================REMOVE ALL NON-KEYWORDS FROM STRINGS===================##
## Facebook
#str_Facebook = remove_non_keywords(str_Facebook, keyword_list)
""" facebook is covid surge listing--not useful """
## Amazon 
str_Amazon = remove_non_keywords(str_Amazon, keyword_list)
## Leidos
str_Leidos = remove_non_keywords(str_Leidos, keyword_list)
## Genentech
str_Genentech = remove_non_keywords(str_Genentech, keyword_list)
## National Debt Relief
str_National = remove_non_keywords(str_National, keyword_list)

##===================CREATE & DISPLAY WORDCLOUDS FOR INDUSTRIES===================##
## Facebook
generate_and_display_wordcloud(str_Facebook,"Facebook","cloud.png") #8iGbRApyT.png")
## Amazon
generate_and_display_wordcloud(str_Amazon,"Amazon","cloud.png") #dollar.jpg")
## Leidos
generate_and_display_wordcloud(str_Leidos,"Leidos","cloud.png") #flask.jpg")
## Genetech
generate_and_display_wordcloud(str_Genentech,"Genentech","cloud.png") #cursor.jpg")
## National Debt Relief
generate_and_display_wordcloud(str_National,"National Debt Relief","cloud.png") #tie.jpg")
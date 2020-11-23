"""
This script is made to generate word clouds from glassdoor datasets
scraped from New York, Texas, Washington and San Francisco areas
over March and April 2020. The idea is to see the prevalence of key
terms from qualifications desired from companies looking for data scientists

DO THIS ONLY for TOP 5 Industries: 
INDUSTRY                            COUNT
Finance                             181.0
Health Care                         193.0
Biotech & Pharmaceuticals           289.0
Business Services                   310.0
Information Technology              508.0

AND FOR TOP 5 COMPANIES of those Industries:
COMPANY                         COUNT
Forescout Technologies Inc.        60 (Not Great)
Banfield Pet Hospital              60 (NO GOOD)
Booz Allen Hamilton                80
Genentech                         118
Veterinary Emergency Group        120 (Not Great)
National Debt Relief              120
"""
import pandas as pd
#ensure file wc_functions.py is in same directory as word_clouds.py
from wc_functions import remove_non_keywords, create_JobDescription_string, generate_and_display_wordcloud

#import .csvs as dataframes
col_list = ["Job_title","Company","State","City","Min_Salary","Max_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]
files_list = ["Data_Job_NY.csv"
                ,"Data_Job_SF.csv"
                ,"Data_Job_TX.csv"
                ,"Data_Job_WA.csv"]
df_NY = pd.read_csv(files_list[0],usecols=col_list)
df_SF = pd.read_csv(files_list[1],usecols=col_list)
df_TX = pd.read_csv(files_list[2],usecols=col_list)
df_WA = pd.read_csv(files_list[3],usecols=col_list)

# remove non-data science jobs from dataset
df_NY = df_NY[df_NY['Max_Salary'] >= 0]
df_SF = df_SF[df_SF['Max_Salary'] >= 0]
df_TX = df_TX[df_TX['Max_Salary'] >= 0]
df_WA = df_WA[df_WA['Max_Salary'] >= 0]

#create df only Job Desc and Industry
#df_NY_2col = df_NY[["Job_Desc","Industry"]].copy()
#df_SF_2col = df_SF[["Job_Desc","Industry"]].copy()
#df_TX_2col = df_TX[["Job_Desc","Industry"]].copy()
#df_WA_2col = df_WA[["Job_Desc","Industry"]].copy()

#join all above dataframes into one dataframe
#frames_all = [df_NY_2col, df_SF_2col, df_TX_2col, df_WA_2col]
frames_all = [df_NY, df_SF, df_TX, df_WA]
df_combined = pd.concat(frames_all)

##===================BY INDUSTRY===================##

#create string of all Job_Desc values by Industry, from combined dataframe.
## Health Care
str_HealthCare = create_JobDescription_string(df_combined,"Industry","Health Care")
## Finance 
str_Finance = create_JobDescription_string(df_combined,"Industry","Finance")
## IT
str_IT = create_JobDescription_string(df_combined,"Industry","Information Technology")
## Biotech
str_Biotech = create_JobDescription_string(df_combined,"Industry","Biotech & Pharmaceuticals")
## Business
str_Business = create_JobDescription_string(df_combined,"Industry","Business Services")

keyword_list = ["models","statistics","probability","machine learning","data science","numpy","pandas","sql","scikit-learn","r","databases","database","team",
"MSc","PhD","mathematics","computer science","physics","research","data","relational databases","python","c++","matlab","modeling","dbt","snowflake",
"mode analytics","fivetran","Census","amplitude","segment","tensorflow","optimization","prediction","engineering","data engineering","neural networks",
"bigquery","pyspark","degree","bachelor","bachelors","scala","data analysis","analysis","data visualization","algorithms","classification",
"model","java","javascript","caffe","deep learning","data processing","hpc","hadoop","ms","bs","m.s.","b.s.","masters","master","stem","postgres",
"software development","agile","querying","experience","skills","credentials","hands-on","communication","presentation","ownership"]

#remove all non-keywords from job descriptions for:
## Health Care
str_HealthCare = remove_non_keywords(str_HealthCare, keyword_list)
## Finance 
str_Finance = remove_non_keywords(str_Finance, keyword_list)
## IT
str_IT = remove_non_keywords(str_IT, keyword_list)
## Biotech
str_Biotech = remove_non_keywords(str_Biotech, keyword_list)
## Business
str_Business = remove_non_keywords(str_Business, keyword_list)

#create wordcloud object for:
## Health Care
generate_and_display_wordcloud(str_HealthCare,"Health Care","cloud.png") #8iGbRApyT.png")
## Finance
generate_and_display_wordcloud(str_Finance,"Finance","cloud.png") #dollar.jpg")
## IT
generate_and_display_wordcloud(str_IT,"Information Technology","cloud.png") #cursor.jpg")
## Biotech
generate_and_display_wordcloud(str_Biotech,"Biotech & Pharmaceuticals","cloud.png") #flask.jpg")
## Business
generate_and_display_wordcloud(str_Business,"Business Services","cloud.png") #tie.jpg")

##===================BY COMPANY===================##

#create string of all Job_Desc values by Company, from combined dataframe.
## Forescout Technologies Inc.
str_Forescout = create_JobDescription_string(df_combined,"Company","Forescout Technologies Inc.")
## Booz Allen Hamilton 
str_Booz = create_JobDescription_string(df_combined,"Company","Booz Allen Hamilton")
## Genentech
str_Genentech = create_JobDescription_string(df_combined,"Company","Genentech")
## Veterinary Emergency Group
str_Veterinary = create_JobDescription_string(df_combined,"Company","Veterinary Emergency Group")
## National Debt Relief
str_National = create_JobDescription_string(df_combined,"Company","National Debt Relief")

#remove all non-keywords from job descriptions for:
## Forescout Technologies Inc.
str_Forescout = remove_non_keywords(str_Forescout, keyword_list)
## Booz Allen Hamilton 
str_Booz = remove_non_keywords(str_Booz, keyword_list)
## Genentech
str_Genentech = remove_non_keywords(str_Genentech, keyword_list)
## Veterinary Emergency Group
str_Veterinary = remove_non_keywords(str_Veterinary, keyword_list)
## National Debt Relief
str_National = remove_non_keywords(str_National, keyword_list)

#create wordcloud object for:
## Forescout Technologies Inc.
generate_and_display_wordcloud(str_Forescout,"Forescout Technologies Inc.","cloud.png") #8iGbRApyT.png")
## Booz Allen Hamilton
generate_and_display_wordcloud(str_Booz,"Booz Allen Hamilton","cloud.png") #dollar.jpg")
## Genetech
generate_and_display_wordcloud(str_Genentech,"Genentech","cloud.png") #cursor.jpg")
## Veterinary Emergency Group
generate_and_display_wordcloud(str_Veterinary,"Veterinary Emergency Group","cloud.png") #flask.jpg")
## National Debt Relief
generate_and_display_wordcloud(str_National,"National Debt Relief","cloud.png") #tie.jpg")
"""
Harker Russell, Team 19, ECE142, FA20

This script is made to generate word clouds from glassdoor datasets
scraped from New York, Texas, Washington and San Francisco areas
over the spring of 2020. The idea is to see the prevalence of key
terms from qualifications desired from companies looking for data scientists

REDO THIS FOR ONLY for TOP 5 Industries: 
INDUSTRY                            COUNT
Aerospace & Defense                 126
Finance                             151
Biotech & Pharmaceuticals           259
Business Services                   310
Information Technology              508

AND FOR TOP 5 COMPANIES of those Industries:
COMPANY                             COUNT
Facebook                              21*Not very useful for wordcloud due to Covid Surge Description
Amazon                                22*Not very useful for wordcloud due to Covid Surge Description
Leidos                                23*Not very useful for wordcloud due to Covid Surge Description
Genentech                             59
National Debt Relief                  60
"""
try:
    import numpy as np
    import pandas as pd
    #ensure file project_functions.py is in same dir as word_clouds.py
    from project_functions import remove_non_keywords, create_JobDescription_string, generate_and_display_wordcloud, clean_and_merge
except Exception as e:
    print("some modules are missing, check that project_functions.py is accessable")

##===================READ CSV DATA IN AS DATAFRAMES===================##
col_list = ["Job_title","Company","State","City","Min_Salary","Max_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]
files_list =    ["Data_Job_NY.csv"
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
df_combined = clean_and_merge(df_allFrames) # project_functions

##===============================================================================================##
## INDUSTRY
##===============================================================================================##

##===================CREATE JOB DESCRIPTION STRINGS BY INDUSTRY===================##
## Aerospace
str_Aero = create_JobDescription_string(df_combined,"Industry","Aerospace & Defense") # project_functions
## Finance 
str_Finance = create_JobDescription_string(df_combined,"Industry","Finance") # project_functions
## Biotech
str_Biotech = create_JobDescription_string(df_combined,"Industry","Biotech & Pharmaceuticals") # project_functions
## Business
str_Business = create_JobDescription_string(df_combined,"Industry","Business Services") # project_functions
## IT
str_IT = create_JobDescription_string(df_combined,"Industry","Information Technology") # project_functions

##===================CREATE LIST OF 'KEYWORDS'===================##
keyword_list = ["models","statistics","probability","machine learning","data science","numpy","pandas","sql","scikit-learn","r","databases","database","team",
"MSc","PhD","mathematics","computer science","physics","research","data","relational databases","python","c++","matlab","modeling","dbt","snowflake",
"mode analytics","fivetran","Census","amplitude","segment","tensorflow","optimization","prediction","engineering","data engineering","neural networks",
"bigquery","pyspark","degree","bachelor","bachelors","scala","data analysis","analysis","data visualization","algorithms","classification",
"model","java","javascript","caffe","deep learning","data processing","hpc","hadoop","ms","bs","m.s.","b.s.","masters","master","stem","postgres",
"software development","agile","querying","experience","skills","credentials","hands-on","communication","presentation","ownership"]

##===================REMOVE ALL NON-KEYWORDS FROM STRINGS===================##
## Aerospace
str_Aero = remove_non_keywords(str_Aero, keyword_list) # project_functions
## Finance 
str_Finance = remove_non_keywords(str_Finance, keyword_list) # project_functions
## Biotech
str_Biotech = remove_non_keywords(str_Biotech, keyword_list) # project_functions
## Business
str_Business = remove_non_keywords(str_Business, keyword_list) # project_functions
## IT
str_IT = remove_non_keywords(str_IT, keyword_list) # project_functions

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
""" Facebook is covid surge listing--not useful, therefore not plotted """
## Amazon 
#str_Amazon = remove_non_keywords(str_Amazon, keyword_list)
""" Amazon is covid surge listing--not useful, therefore not plotted """
## Leidos
#str_Leidos = remove_non_keywords(str_Leidos, keyword_list)
""" Leidos is covid surge listing--not useful, therefore not plotted """
## Genentech
str_Genentech = remove_non_keywords(str_Genentech, keyword_list)
## National Debt Relief
str_National = remove_non_keywords(str_National, keyword_list)

##===================CREATE & DISPLAY WORDCLOUDS FOR COMPANIES===================##
## Facebook
#generate_and_display_wordcloud(str_Facebook,"Facebook","cloud.png") #8iGbRApyT.png")
""" Facebook is covid surge listing--not useful, therefore not plotted """
## Amazon
#generate_and_display_wordcloud(str_Amazon,"Amazon","cloud.png") #dollar.jpg")
""" Amazon is covid surge listing--not useful, therefore not plotted """
## Leidos
#generate_and_display_wordcloud(str_Leidos,"Leidos","cloud.png") #flask.jpg")
""" Leidos is covid surge listing--not useful, therefore not plotted """
## Genetech
generate_and_display_wordcloud(str_Genentech,"Genentech","cloud.png") #cursor.jpg")
## National Debt Relief
generate_and_display_wordcloud(str_National,"National Debt Relief","cloud.png") #tie.jpg")
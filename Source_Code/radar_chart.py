"""
Pratyush Dwivedi, Team 19, ECE142, FA20

This script is made to generate radar chart from glassdoor datasets
scraped from New York, Texas, Washington and San Francisco areas
over the spring of 2020. The idea is plot the top 5 job titles
in the top 5 industries as listed below:

INDUSTRY                            COUNT
Aerospace & Defense                  252.0
Finance                              302.0
Biotech & Pharmaceuticals            518.0
Business Services                    620.0
Information Technology              1016.0
"""

import pandas as pd
from project_functions import clean_data, merge_field,plot_job_title_radar

##===============Load Data =======================##

sf = pd.read_csv(r'Data_Job_SF.csv')
ny = pd.read_csv(r'Data_Job_NY.csv')
tx = pd.read_csv(r'Data_Job_TX.csv')
wa = pd.read_csv(r'Data_Job_WA.csv')

##===============Clean Data =======================##

sf_clean = clean_data(sf)
wa_clean = clean_data(wa)
tx_clean = clean_data(tx)
ny_clean = clean_data(ny)

df_clean = [sf_clean,wa_clean,tx_clean,ny_clean]

##===============Merge Data =======================##

mdict = merge_field('Industry',df_clean)

##===============Plot Data =======================##

plot_job_title_radar('Information Technology',mdict['Information Technology'],[0,10,20,30,40,50,60],70)
plot_job_title_radar('Business Services',mdict['Business Services'],[0,5,10,15,20],25)
plot_job_title_radar('Biotech & Pharmaceuticals',mdict['Biotech & Pharmaceuticals'],[0,1,2,3],4)
plot_job_title_radar('Finance',mdict['Finance'],[0,5,10,15,20,25,30],35)
plot_job_title_radar('Aerospace & Defense',mdict['Aerospace & Defense'],[0,2,4,6,8,10],12)
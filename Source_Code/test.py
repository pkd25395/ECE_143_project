# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:58:40 2020

@author: jakey
"""
#========= DATA FOR SCATTERPLOTS TO PLOT =========#
from altair import Chart
import altair as alt
import pandas as pd
from project_functions import clean_data, merge_field, salary_v_rating_scatter, salary_v_listings_scatter, add_seniority

# Read csv files into dataframes
sf = pd.read_csv(r'Source_Code/Data_Job_SF.csv')
ny = pd.read_csv(r'Source_Code/Data_Job_NY.csv')
tx = pd.read_csv(r'Source_Code/Data_Job_TX.csv')
wa = pd.read_csv(r'Source_Code/Data_Job_WA.csv')

# Filter the data and combine them
sf_clean = clean_data(sf)
wa_clean = clean_data(wa)
tx_clean = clean_data(tx)
ny_clean = clean_data(ny)
sf_clean = clean_data(sf)
wa_clean = clean_data(wa)
tx_clean = clean_data(tx)
ny_clean = clean_data(ny)

df_clean = [sf_clean,wa_clean,tx_clean,ny_clean]

# Choose how we want data to be organized
mdict = merge_field('Seniority',df_clean)

# Choose what entries we specifcally want to plot
df_chart = pd.concat([mdict['Senior'], mdict['Entry']], ignore_index=True)

print(df_chart)



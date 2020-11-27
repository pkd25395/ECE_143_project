# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:49:26 2020

@author: jakey
"""
import pandas as pd
from project_functions import clean_data, merge_field
import altair as alt

sf = pd.read_csv(r'Data_Job_SF.csv')
ny = pd.read_csv(r'Data_Job_NY.csv')
tx = pd.read_csv(r'Data_Job_TX.csv')
wa = pd.read_csv(r'Data_Job_WA.csv')
sf_clean = clean_data(sf)
wa_clean = clean_data(wa)
tx_clean = clean_data(tx)
ny_clean = clean_data(ny)
df_clean = [sf_clean,wa_clean,tx_clean,ny_clean]
mdict = merge_field('Industry',df_clean)

print(mdict['Accounting & Legal'])
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:34:16 2020

@author: jakey
"""

import pandas as pd
from project_functions import clean_data, merge_field, salary_v_rating_scatter
import altair as alt

alt.renderers.enable('notebook')

sf = pd.read_csv(r'Source_Code/Data_Job_SF.csv')
ny = pd.read_csv(r'Source_Code/Data_Job_NY.csv')
tx = pd.read_csv(r'Source_Code/Data_Job_TX.csv')
wa = pd.read_csv(r'Source_Code/Data_Job_WA.csv')
sf_clean = clean_data(sf)
wa_clean = clean_data(wa)
tx_clean = clean_data(tx)
ny_clean = clean_data(ny)
df_clean = [sf_clean,wa_clean,tx_clean,ny_clean]
mdict = merge_field('Industry',df_clean)
df_chart = pd.concat([mdict['Health Care'], mdict['Information Technology'], mdict['Finance'], 
                      mdict['Business Services'], mdict['Aerospace & Defense'], mdict['Biotech & Pharmaceuticals']],
                    ignore_index=True)

chart = salary_v_rating_scatter(df_chart,'Industry')

print(chart)
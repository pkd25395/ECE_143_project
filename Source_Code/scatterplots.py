# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:34:16 2020

@author: jakey
"""

import pandas as pd
from project_functions import clean_data, merge_field, salary_v_rating_scatter, salary_v_listings_scatter
import altair as alt

##============== Load in necessary data =================##

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

# chart = salary_v_rating_scatter(mdict['Finance'],'Industry')
# chart.show()

"""
Choose what you want to plot by uncommenting what you want to plot. This is 
helpful because this is not in a notebook so it renders in a browser one at a
time, so to look at the next plot you need to close the tab it rendered on.

"""

##=================== Salary vs. Ratings Scatterplot by Industry ===================##
# mdict = merge_field('Industry',df_clean)
# df_chart = pd.concat([mdict['Business Services'],mdict['Information Technology'],mdict['Biotech & Pharmaceuticals']],
#                       ignore_index=True)

# chart = salary_v_rating_scatter(df_chart,'Industry',separate=True)
# chart.show()

##=================== Salary vs. Ratings Scatterplot by Company ===================##
# df_chart = pd.concat([mdict['Information Technology'], mdict['Finance'], mdict['Business Services'], 
#                       mdict['Aerospace & Defense'], mdict['Biotech & Pharmaceuticals']],
#                       ignore_index=True)

# # Choose how we want data to be organize
# mdict = merge_field('Company',df_clean)

# # Choose what entries we specifcally want to plot
# df_chart = pd.concat([mdict['Genentech'], mdict['Leidos'], 
#                       mdict['Amazon'], mdict['Facebook'], mdict['Booz Allen Hamilton'],
#                       mdict['Capital One'], mdict['BAE Systems USA']],
#                     ignore_index=True)

# # Create and display plot
# chart = salary_v_rating_scatter(df_chart, 'Company')
# chart.show()


#=================== Salary vs. Listings Scatterplot ===================##
# Choose how we want data to be organize
mdict = merge_field('Industry',df_clean)

# Choose what entries we specifcally want to plot
# Company
# df_chart = pd.concat([mdict['Genentech'], mdict['National Debt Relief'], mdict['Leidos'], mdict['BAE Systems USA'],
#                       mdict['Facebook'], mdict['Amazon'], mdict['Booz Allen Hamilton']],
#                     ignore_index=True)
# Inudstry
df_chart = pd.concat([mdict['Information Technology'], mdict['Finance'], mdict['Business Services'], 
                      mdict['Aerospace & Defense'], mdict['Biotech & Pharmaceuticals']],
                      ignore_index=True)

# Create and display plot
chart = salary_v_listings_scatter(df_chart, 'Industry')
chart.show()
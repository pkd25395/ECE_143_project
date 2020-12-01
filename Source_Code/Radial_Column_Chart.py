# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:56:44 2020

@author: azrae
"""
from collections import OrderedDict
from io import StringIO
from math import log, sqrt

import numpy as np
import pandas as pd

from bokeh.plotting import figure, output_file, show
from project_functions import merge_MinMax_Salary, count_members_by_column, clean_and_merge

def plot_radial_column_chart(df,min_scale,max_scale):
    '''
    This function reading the dataframe and plot the corresponding radial column chart
    ----------
    df : A corresponding dataframe that needs to be plot

    '''
    assert isinstance(df,pd.DataFrame), 'input needs to be a pandas dataframe'
    assert isinstance(min_scale,int) and isinstance(max_scale,int), 'min scale and max scale needs to be int'
    
    # set company bar color
    companys = [column for column in df.columns]
    companys = companys[1::]
    colors = ["#0d3362","#c64737", "black" ] * 5
    company_color = OrderedDict({companys[i]:colors[i] for i in range(len(companys))})
    print()
    
    # set industry section color
    industry_color = OrderedDict([
    ("Asrospace", "#FFFFE0"), # Yellow
    ("Finance", "#FF69B4"), # Pink
    ("Biotech", "#9370DB"),  # Purple
    ("Business", "#00BFFF"), # Blue
    ("InfoTech", "#F0FFF0"), # Green
    ])
    
    # adjust graph board size
    width = 1000
    height = 1000
    # adjust graph circule size
    inner_radius = 50           
    outer_radius = 350 
    
    # magic equal that scale the value to the radius (I don't know how it works)
    # minr = min_scale you want for the data (be reasonable)
    # maxr = max_scale you want for the data (be reasonable)
    minr = sqrt(log(min_scale * 1E4))
    maxr = sqrt(log(max_scale * 1E4))
    a = (outer_radius - inner_radius) / (minr - maxr)
    b = inner_radius - a * maxr

    def rad(mic):
        return abs(a * np.sqrt(np.log(mic * 1E4)) + b)

    big_angle = 2.0 * np.pi / (len(df) + 1 ) # divide the circules based on the length of df(sections)
    small_angle = big_angle / 7 # divide the sections again for bar positions
    
    # create the figure and plot the background
    p = figure(plot_width=width, plot_height=height, title="",
               x_axis_type=None, y_axis_type=None,
               x_range=(-420, 420), y_range=(-420, 420),
               min_border=0, outline_line_color="black",
               background_fill_color="#f0e1d2")


    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # plot the sections circule
    # angle for each sections
    angles = np.pi/2 - big_angle/2 - df.index.to_series()*big_angle 
    # color for each sections
    colors = [industry_color[industry] for industry in df.Industry]
    p.annular_wedge(
        0, 0, inner_radius, outer_radius, -big_angle+angles, angles, color=colors,
        )   


    # radial axes

    p.annular_wedge(0, 0, inner_radius-10, outer_radius+10,
                -big_angle+angles, -big_angle+angles, color="black")
    
    # plot the company bars
    
    company_index = 0
    for section in range(len(angles)):
        company_angle = angles[section]
        company_rad = rad(df[companys[company_index]])[section]
        company = companys[company_index]
        company_index += 1 
        
        p.annular_wedge(0, 0, inner_radius, company_rad,
                -big_angle+company_angle+5*small_angle, -big_angle+company_angle+6*small_angle,
                color=company_color[company])

        company_rad = rad(df[companys[company_index]])[section]
        company = companys[company_index]
        company_index += 1 
        p.annular_wedge(0, 0, inner_radius, company_rad,
                -big_angle+company_angle+3*small_angle, -big_angle+company_angle+4*small_angle,
                color=company_color[company])
        
        company_rad = rad(df[companys[company_index]])[section]
        company = companys[company_index]
        company_index += 1 
        p.annular_wedge(0, 0, inner_radius, company_rad,
                -big_angle+company_angle+1*small_angle, -big_angle+company_angle+2*small_angle,
                color=company_color[company])
    


    # industry labels
    labels = np.power(10.0, np.arange(3, 4))
    radii = a * np.sqrt(np.log(labels * 1E4)) + b
    xr = radii[0]*np.cos(np.array(-big_angle/2 + angles))
    yr = radii[0]*np.sin(np.array(-big_angle/2 + angles))
    label_angle=np.array(-big_angle/2+angles)
    label_angle[label_angle < -np.pi/2] += np.pi # easier to read labels on the left side
    p.text(xr, yr, df['Industry'], angle=label_angle,
       text_font_size="12px", text_align="center", text_baseline="middle")

    # OK, these hand drawn legends are pretty clunky, will be improved in future release
    industry_legends_x = [-100 for n in range(len(industry_color))]
    industry_legends_y = [400 - 50*n for n in range(len(industry_color))]
    p.circle(industry_legends_x, industry_legends_y, color=list(industry_color.values()), radius=5)
    
    industry_legends_x = [-90 for n in range(len(industry_color))]
    p.text(industry_legends_x, industry_legends_y, text=["Industry-" + industry for industry in industry_color.keys()],
           text_font_size="9px", text_align="left", text_baseline="middle")
    
    
    # company labels
    company_labels_x = [-80,-80,-80] * 5
 
    company_labels_y = [390,380,370,340,330,320,290,280,270,240,230,220,190,180,170]
    p.circle(company_labels_x, company_labels_y,color=list(company_color.values()), radius=3)
    
    company_labels_x = [-70,-70,-70] * 5
    p.text(company_labels_x, company_labels_y, text=["" + company for company in company_color.keys()],
       text_font_size="9px", text_align="left", text_baseline="middle")
    
    show(p)
    
##===============Load Data =======================##

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

df_minmaxAerospace = df_minmax[df_minmax["Industry"]=="Aerospace & Defense"]
#df_minmaxAerospace.to_csv('Aerospace.csv')
df_minmaxFinance = df_minmax[df_minmax["Industry"]=="Finance"]
df_minmaxBiotech = df_minmax[df_minmax["Industry"]=="Biotech & Pharmaceuticals"]
df_minmaxBusiness = df_minmax[df_minmax["Industry"]=="Business Services"]
df_minmaxInfoTech = df_minmax[df_minmax["Industry"]=="Information Technology"]


##===============GET TOP COMPANYS  ===========================#
top_companies_num = 3
top_company_Aerospace_dict = {}
top_company_Aerospace = list(df_minmaxAerospace['Company'].value_counts(sort=True).index[0:3])
top_company_Aerospace_count = df_minmaxAerospace['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_Aerospace_dict[top_company_Aerospace[i]] = top_company_Aerospace_count[i]
#print('Asrospace',top_company_Aerospace_dict)    

top_company_Finance_dict = {}
top_company_Finance = list(df_minmaxFinance['Company'].value_counts(sort=True).index[0:3])
top_company_Finance_count = df_minmaxFinance['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_Finance_dict[top_company_Finance[i]] = top_company_Finance_count[i]
#print('Finance',top_company_Finance_dict)    


top_company_Biotech_dict = {}
top_company_Biotech = list(df_minmaxBiotech['Company'].value_counts(sort=True).index[0:3])
top_company_Biotech_count = df_minmaxBiotech['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_Biotech_dict[top_company_Biotech[i]] = top_company_Biotech_count[i]
#print('Biotech',top_company_Biotech_dict)    

# get rid of repeated companys
top_company_Business_dict = {}
top_company_Business = list(df_minmaxBusiness['Company'].value_counts(sort=True).index[0:4])
top_company_Business_count = df_minmaxBusiness['Company'].value_counts(sort=True)[0:4].values
for i in range(top_companies_num + 1):
    top_company_Business_dict[top_company_Business[i]] = top_company_Business_count[i]
#print('Business',top_company_Business_dict) 

top_company_InfoTech_dict = {}
top_company_InfoTech = list(df_minmaxInfoTech['Company'].value_counts(sort=True).index[0:3])
top_company_InfoTech_count = df_minmaxInfoTech['Company'].value_counts(sort=True)[0:3].values
for i in range(top_companies_num):
    top_company_InfoTech_dict[top_company_InfoTech[i]] = top_company_InfoTech_count[i]
#print('InfoTech',top_company_InfoTech_dict) 




##================Calculate the salarys and create the dataframe ===========================#
df_top_salary = OrderedDict({'Industry':['Asrospace','Finance','Biotech','Business','InfoTech']})

df_top_salary_Aerospace = {}
for company in top_company_Aerospace:

    total_salary = df_minmaxAerospace.loc[df_minmaxAerospace['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Aerospace_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Aerospace[company] = avg_salary 
    #print(company,avg_salary)
    
print('Aerospace')
print(df_top_salary_Aerospace)

for company in df_top_salary_Aerospace:
    df_top_salary[company] = df_top_salary_Aerospace[company]
    




df_top_salary_Finance = {}
for company in top_company_Finance:
    total_salary = df_minmaxFinance.loc[df_minmaxFinance['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Finance_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Finance[company] = avg_salary 
    #print(company,avg_salary)
    
print('Finance')
print(df_top_salary_Finance)

for company in df_top_salary_Finance:
    df_top_salary[company] = df_top_salary_Finance[company]
    
df_top_salary_Biotech = {}
for company in top_company_Biotech:
    total_salary = df_minmaxBiotech.loc[df_minmaxBiotech['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Biotech_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Biotech[company] = avg_salary 
    #print(company,avg_salary)
print('Biotech')
print(df_top_salary_Biotech)

for company in df_top_salary_Biotech:
    df_top_salary[company] = df_top_salary_Biotech[company]
    

df_top_salary_Business= {}
for company in top_company_Business:
    total_salary = df_minmaxBusiness.loc[df_minmaxBusiness['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_Business_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_Business[company] = avg_salary 
    #print(company,avg_salary)
# get rid of repeated companys 
df_top_salary_Business.pop('Booz Allen Hamilton Inc.')
print('Business')
print(df_top_salary_Business)

for company in df_top_salary_Business:
    df_top_salary[company] = df_top_salary_Business[company]

df_top_salary_InfoTech= {}
for company in top_company_InfoTech:
    total_salary = df_minmaxInfoTech.loc[df_minmaxInfoTech['Company'] == str(company), 'Salary'].sum()
    job_number = top_company_InfoTech_dict[company]
    avg_salary = total_salary // job_number
    df_top_salary_InfoTech[company] = avg_salary 
    #print(company,avg_salary)

print('InfoTech')
print(df_top_salary_InfoTech)

for company in df_top_salary_InfoTech:
    df_top_salary[company] = df_top_salary_InfoTech[company]


df = pd.DataFrame(data=df_top_salary)
#print(df.head())

min_scale = 1000
max_scale = 10000
plot_radial_column_chart(df,min_scale,max_scale)


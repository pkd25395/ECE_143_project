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
    ("Health Care", "#FFFFE0"), # Yellow
    ("Biotech & Pharmaceuticals", "#FF69B4"), # Pink
    ("Business Services", "#9370DB"),  # Purple
    ("Information Technology", "#00BFFF"), # Blue
    ("Finance", "#F0FFF0"), # Green
    ])
    
    # adjust graph board size
    width = 800
    height = 800
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
    company_labels_x = [-80,-40,0] * 5
    company_labels_y = [380]*3 + [330]*3 + [280]*3 + [230]*3 + [180]*3
    p.circle(company_labels_x, company_labels_y,color=list(company_color.values()), radius=3)
    
    company_labels_x = [-70,-30,10] * 5
    company_labels_y = [380]*3 + [330]*3 + [280]*3 + [230]*3 + [180]*3
    p.text(company_labels_x, company_labels_y, text=["" + company for company in company_color.keys()],
       text_font_size="9px", text_align="left", text_baseline="middle")
    
    show(p)
    
# load data

data = 'Fake_Data.csv'
df = pd.read_csv(data)
min_scale = 1000
max_scale = 10000
plot_radial_column_chart(df,min_scale,max_scale)

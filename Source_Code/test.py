# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:58:40 2020

@author: jakey
"""

def gen_and_disp_boxWhiskerPlot(in_df,chart_title,x_col,y_col,hue_col):
    """
    Description:    Takes dataframe in-str, generates WordCloud object and displays wordcloud for 'in-str'.
                    in particular this is for team 19, FA20, ECE143 project. 
    :param in_df:       in_df is dataframe, must have column of strings titled "Job_Desc" 
    :type in_df:        in_df must be pd.DataFrame type. 
    :param chart_title: chart_title should be title of graph. 
    :type chart_title:  chart_title must be of type str. 
    :param x_col:       x_col must be string, column of df.  
    :type x_col:        x_col must be of type str.   
    :param y_col:       y_col must be string, column of df.  
    :type y_col:        y_col must be of type str. 
    :param hue_col:     hue_col must be string, column of df. 
    :type hue_col:      hue_col must be of type str. 
    :author: Harker Russell 
    """
    # conda install -c conda-forge wordcloud
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    assert isinstance(in_df,pd.DataFrame), ':type in_df: in_df must be pd.DataFrame type'
    assert isinstance(chart_title,str), ":type chart_title:   in_str must be type str"
    assert isinstance(x_col,str), ":type x_col: x_col must be of type str"
    assert x_col in in_df, "no x_col column in input dataframe 'in_df'"
    assert isinstance(y_col,str), ":type y_col: y_col must be of type str"
    assert y_col in in_df, "no y_col column in input dataframe 'in_df'"
    assert isinstance(hue_col,str), ":type hue_col: y_col must be of type str"
    assert hue_col in in_df, "no hue_col column in input dataframe 'in_df'"

    sns.set(font_scale=1.1)
    plt.figure(figsize=(12,8))
    sns.boxplot( x=in_df[x_col], y=in_df[y_col], hue=in_df[hue_col])
    plt.title(chart_title) #1300x850
    plt.show()

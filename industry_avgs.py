# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:48:54 2020

@author: jakey
"""
import pandas as pd
import numpy as np
import glob

def industry_avgs(fnames, org, ascend = False):
    """
    Get the industry avgs and put them into a csv

    Parameters
    ----------
    fnames : list of strings
        List of csvs with their paths
    org : str
        How we want the csv sorted. You can do it by Rating, Min_Salary, Max_Salary
        and Entries
    ascend : bool, optional
        What order we want the resulting csv to be in. The default is False.

    Returns
    -------
    None.

    """
    
    assert isinstance(fnames, list)
    assert isinstance(org, str) or isinstance(org, list)
    assert isinstance(ascend, bool)
    
    org_choices = ['Rating', 'Min_Salary', 'Max_Salary', 'Entries']
    assert org in org_choices
    
    industries = list()
    ratings = list()
    min_salaries = list()
    max_salaries = list()
    entries = list()
    
    #assert isinstance(fname, str)
    for i in range(len(fnames)):
        
        assert isinstance(fnames[i], str)
        
        # load in industry into DataFrame
        industry = pd.read_csv(fnames[i])
        
        # get industry name from path
        start = fnames[i].find('\\') + len('\\')
        end = fnames[i].find('.csv')
        substring = fnames[i][start:end]
        industries.append(substring)
        
        # calculate avg ratings and put into list
        avg_ratings = round(industry['Rating'].sum() / industry.shape[0], 3)
        ratings.append(avg_ratings)
        
        # calculate avg min salaries
        min_salary = round(industry['Min_Salary'].sum() / industry.shape[0], 2)
        min_salaries.append(min_salary)

        # calculate avg max salaries
        max_salary = round(industry['Max_Salary'].sum() / industry.shape[0], 2)
        max_salaries.append(max_salary)
        
        # add in amount of data collected
        entries.append(industry.shape[0])
    
    avgs = pd.DataFrame({'Rating' : ratings, 'Min_Salary' : min_salaries, 
                         'Max_Salary' : max_salaries, 'Entries' : entries }, 
                        index = industries)
    
    avgs = avgs.sort_values(by=org, ascending=ascend)
    
    avgs.to_csv(r'industry_avgs.csv')



# This will obviously need to be changed for each person
path = 'C:/Users/jakey/Documents/ECE_143/ECE_143_project/industry_data/'

# Gets all the industry csv names and puts them into a list
fnames = glob.glob(path + '*.csv')
industry_avgs(fnames, 'Rating')
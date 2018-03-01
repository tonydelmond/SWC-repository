# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#saved as analysis.py
#%% Imports the library pandas with abbreviated call "pd"
import pandas as pd

#%% Imports the data set using the pandas library command to read csv file
dat = pd.read_csv('data/gapminder_gdp_europe.csv')

#%% Descriptive statistics for the data set imported
print(dat.describe())

#%%
dat = pd.read_csv('data/gapminder_gdp_oceania.csv')
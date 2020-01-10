from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind, ttest_ind_from_stats, ttest_rel
import pandas as pd
import numpy as np
import matplotlib as plt



df1 = pd.read_csv(r'https://raw.githubusercontent.com/msnyd/unit1project/master/1976_to_2015_Draftees.csv')
df2 = df1.copy()

print(df1.describe())
print(df1.isnull().sum())

'''
    So what I am doing here is that is that I am writing these data frames to csvs to use in my graph, these new dataframes are a bit smaller and make it easier to do
    calculations and make graphs with.
'''

df = df2[df2['All.Star'] != 0]
print(df.head())
#df.to_csv(r'C:/Users/Matt/Desktop/unit1project/only_all_stars.csv')

#this function will go into a column (in this case the All Star column) and change people who have gotten an all star appearence and chamge that to one and leave the rest as 0

def onesAndZeroes(number): 
    for i in range(1, 3960):
        if number >= 1:
            return 1
        if number == 0:
            return 0


#fix the x limit when plotting histograms, 61+ = undrafted players
def undrafted(numbers): 
    for i in range(1, 3960):
        if numbers > 60:
            numbers = 61
            return numbers
        if numbers < 60:
            numbers = numbers
            return numbers

df1 = df.copy()
df1['Appeared_As_All_Star'] = df1['All.Star'].apply(onesAndZeroes)
df1['Pick'] = df1['Pk'].apply(undrafted)

# df1.to_csv(r'C:/Users/Matt/Desktop/unit1project/nba_stats_mod.csv')
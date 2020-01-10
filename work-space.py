from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind, ttest_ind_from_stats, ttest_rel
import pandas as pd
import numpy as np
import matplotlib as plt

df1 = pd.read_csv(r'https://raw.githubusercontent.com/msnyd/unit1project/master/1976_to_2015_Draftees.csv')
df2 = df1.copy()

df = df2[df2['All.Star'] != 0]
print(df.head())
df.to_csv(r'C:/Users/Matt/Desktop/unit1project/only_all_stars.csv')

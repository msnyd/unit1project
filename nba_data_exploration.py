import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import os


'''
    The goal of my project is to find out if the NBA draft is a major determinant of the success of one's career.  In other words
    does a #1 pick in the draft have a better chance, statistically speaking, having a more successful career than someone who was 
    drafted at #27.  To do this, we have to define what constitutes a successful career, since there is no concrete answer to this
    I drew the line at saying a successful NBA career will, at the very least, have one All Star appearence.  I chose this because 
    being chosen to be an All Star involves 3 metrics, fan voting (50%), current player voting (25%), and basketball media voting (25%).
    Not only do all stars have to win the hearts of the fans, but also their peers and critics.
'''

#data file
df = pd.read_csv(r'C:\\Users\\Matt\\Desktop\\unit1project\\1976_to_2015_Draftees.csv')

pd.set_option('display.max_columns', None)
#print(df)
print(df.describe())
#print(df['All.Star'].value_counts())
#print(df.isnull().sum())


pio.templates.default = "plotly_dark"



# fig = px.bar(df, x='Pk', y='All.Star', hover_name = 'Player', color='All.Star')
# fig.show()

# figScatt = px.scatter(df, x='Pk', y='Points.per.Game', hover_name = 'Player', hover_data = 'Draft_Yr')
# figScatt.show()

'''
    What I want to do now is to convert all the people who have recieved an All Star appearence to 1.  This
    will tell me everyone who has recieved an All star appearence and will get rid of the "super star" outliers
    and will give me a less weighted projection on the number of people actually being an All Star in their career
'''

#this function will go into a column (in this case the All Star column) and change people who have gotten an all star appearence and chamge that to one and leave the rest as 0

def onesAndZeroes(number): 
    for i in range(1, 3960):
        if number >= 1:
            return 1
        if number == 0:
            return 0


#fix the x limit when plotting histograms, 61+ shows undrafted players
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

#print(df1.describe())

fig1 = px.bar(
    df1,
    title = 'Unweighted All Star Appearences per Draft Pick',
    x='Pick', 
    y='Appeared_As_All_Star', 
    hover_name = 'Player', 
    color='All.Star',
) 

# unweighted graph to show the amount of times each pick made it to an all star game
fig1.show()


fig2 = px.bar(
    df1,
    title = 'All Star Appearences per Draft Pick',
    x='Pick', 
    y='All.Star', 
    hover_name = 'Player', 
    color='All.Star',
)
fig2.show()

git init
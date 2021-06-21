import pandas as pd
from os import path

#3.2.1 - Load the at bat data into a DataFrame named dfb. You'll use it for the rest of the problems in this section:

DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'
dfb = pd.read_csv(path.join(DATA_DIR, '2018-season', 'atbats.csv'))

#3.2.2 - Add a column to dfb that gives the total number of extra base hits (which is anything that is not a single) 
# for each player. Do it two ways:

#A - Using basic arithmetic operators:
dfb['extra_base1'] = dfb['2B'] + dfb['3B'] + dfb['HR']

#B - Using a builtin Pandas function:
dfb['extra_base2'] = dfb[['2B', '3B', 'HR']].sum(axis=1)

#C - Prove that they're the same:
print((dfb['extra_base1'] == dfb['extra_base2']).all())

#3.2.3:
#A - What were the average values for hits, strikeouts, and homeruns?:
dfb[['H', 'SO', 'HR']].mean()

#B - How many times in our data did someone get 150 or more hits and 150 or more strikeouts?:
((dfb['H'] >= 150) & (dfb['SO'] >= 150)).sum()

#C - What percentage of players who had 150+ hits also had 150+ strikeouts?:
((dfb['H'] >= 150) & (dfb['SO'] >= 150)).sum() / (dfb['H'] >= 150).sum()

#D - What was the maximum number of at bats in our sample?:
dfb['AB'].max()

#E - Find the number of times each team is represented in our DataFrame:
dfb['team'].value_counts()

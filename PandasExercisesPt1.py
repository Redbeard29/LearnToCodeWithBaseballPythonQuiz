import pandas as pd
from os import path

DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'

#3.0.1 - Load the 2018 aggregated picthing data into a DataFrame named dfp. You'll use it for the
# rest of the problems in this section
dfp = pd.read_csv(path.join(DATA_DIR, '2018-season', 'pitches.csv'))

#3.0.2 - Use the dfp DataFrame to create another DataFrame, dfp50, that is the top 50 players
# by lowest ERA
dfp50 = dfp.sort_values('ERA').head(50)


#3.0.3 - Sort the dfp by first name in descending order.
dfp.sort_values('nameFirst', ascending=False, inplace=True)

#3.0.4 - What is the type of dfp.sort_values('W')?
'DataFrame'

#3.0.5:
#A - Make a new DataFrame, dfp_simple, with just the columns 'nameFirst', 'nameLast', 'W',
# 'L', 'ERA', in that order:
dfp_simple = dfp[['nameFirst', 'nameLast', 'W', 'L', 'ERA']]

#B - Rearrange dfp_simple so that the order is 'nameLast', 'nameFirst', 'ERA', 'W', 'L':
dfp_simple = dfp_simple[['nameLast', 'nameFirst', 'ERA', 'W', 'L']]

#C - Using the original dfp DataFrame, add the 'teamID' column to dfp_simple:
dfp_simple['teamID'] = dfp['teamID']

#D - Write a copy of dfp_simple to ./data/problems/dfp_simple.txt. Make it pipe delimited 
# isntead of comma delimited:
dfp_simple.to_csv(path.join(DATA_DIR, 'problems', 'dfp_simple.txt'), sep = '|')

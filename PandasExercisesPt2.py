import pandas as pd
from os import path

#3.1.1 - Load the at bat data into a DataFrame named dfb. You'll use it for the rest of the problems in this section:

DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'
dfb = pd.read_csv(path.join(DATA_DIR, '100-game-sample', 'atbats.csv'))

#3.1.2 - Add a column to dfb, 'runs_scored' that gives runs scored this at bat. Use 'b_score_start' and 
# 'b_score_end' columns:

dfb['runs_scored'] = dfb['b_score_end'] - dfb['b_score_start']

#3.1.3 - Add a colmn called 'ab_desc' that describes the at bat in the form '<batter> got a <event> vs <pitcher>'
dfb['ab_desc'] = dfb['batter'] + ' got a ' + dfb['event'] + ' vs ' + dfb['pitcher']

#3.1.4 - Add a boolean column to dfb called 'final_out' that indicates whether the at bat was the final out of the inning:
dfb['final_out'] = dfb['o'] == 3

#3.1.5 - Add a column 'len_last_name' that gives the length of the pitcher's last name:
def get_len_last_name(pitcher):
    last_name = pitcher.split('.')[-1]
    return len(last_name)

dfb['len_last_name'] = dfb['pitcher'].apply(get_len_last_name)

#Could also do this: dfb['len_last_name'] = (dfb['pitcher'].apply(lambda x: len(x.split('.')[-1])))

#3.1.6 - Change the 'ab_id' column to a string:
dfb['ab_id'] = dfb['ab_id'].astype(str)

#3.1.7:
#A - Replace all of the '_' with ' ' in all columns to make them more readable:
dfb.columns = [x.replace('_', ' ') for x in dfb.columns]

#B - Change it back to follow convention:
dfb.columns = [x.replace(' ', '_') for x in dfb.columns]

#3.1.8:
#A - Using the 'runs_scored' columns you created above, make a new column 'run_portion' that indicates
#the percentage of the batting team's total runs scored during this at bat:
dfb['run_portion'] = dfb['runs_scored']/dfb['b_score_end']

#B - There are missing values in this column - replace them all with -99:
dfb['run_portion'].fillna(-99, inplace=True)

#3.1.9 - Drop the 'run_portion' column:
dfb.drop('run_portion', axis=1, inplace=True)

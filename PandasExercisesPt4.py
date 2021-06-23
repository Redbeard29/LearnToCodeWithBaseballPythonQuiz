import pandas as pd
from os import path
import numpy as np

#3.3.1 - Load the pitcher data into a DataFrame named dfp. You'll use it for the rest of the problems in this section:
DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'
dfp = pd.read_csv(path.join(DATA_DIR, '2018-season', 'pitches.csv'))

#3.3.2 - Make a smaller DataFrame with just Yankees pitchers and only the columns: 'nameFirst', 'nameLast', 'G', 'ERA'.
#Do it two ways - using the loc syntax, and using the query syntax. (The abbreviation for Yankees is NYN in this dataset)
yanks_pitchers = (dfp['teamID'] == 'NYN')
dfp_nyy1 = dfp.loc[yanks_pitchers, ['nameFirst', 'nameLast', 'G', 'ERA']]
dfp_nyy2 = dfp.query("teamID == 'NYN'")[['nameFirst', 'nameLast', 'G', 'ERA']]
print((dfp_nyy1 == dfp_nyy2).all())

#3.3.3 - Make a DataFrame dfp_no_nyy with the same columns that is everyone EXCEPT Yankee players. Add the teamID column.
dfp_no_nyy = dfp.loc[(dfp['teamID'] != 'NYN'), ['nameFirst', 'nameLast', 'G', 'ERA', 'teamID']]

#3.3.4:
#A: Are there any duplicates by last name AND league (AL or NL) in our dfp DataFrame? How many?
print(dfp[['nameLast', 'lgID']].duplicated().any())
print(dfp[['nameLast', 'lgID']].duplicated().sum())
#B: Divide dfp into two separate DataFrames dfp_dups and dfp_nodups, one with the duplicates from part A, the other without.
dups = dfp[['nameLast', 'lgID']].duplicated(keep=False)
dfp_dups = dfp.loc[dups]
dfp_no_dups = dfp.loc[~dups]

print(dfp_no_dups.sample(10))

#3.3.5 - Add a new column to dfp called era_description with the values
#establish null value first:
dfp['era_description'] = np.nan
#A: 'stud' for players with an ERA 2.5 or under:
dfp.loc[dfp['ERA'] <= 2.5, 'era_description'] = 'stud'
#B: 'scrub' for ERA's > 5:
dfp.loc[dfp['ERA'] > 5, 'era_description'] = 'scrub'

#3.3.6 - Make a new DataFrame with only observations for which 'era_description' is missing. 
#A: Do this with both the loc syntax:
dfp_no_desc1 = dfp.loc[dfp['era_description'].isnull()]
#B: and query syntax:
dfp_no_desc2 = dfp.query("era_description.isnull()")


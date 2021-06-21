from PandasExercisesPt2 import DATA_DIR
import pandas as pd
from os import path

DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'

at_bats = pd.read_csv(path.join(DATA_DIR, '2018-season', 'atbats.csv'))
pp = pd.read_csv(path.join(DATA_DIR, '100-game-sample', 'pitches.csv'))

print(at_bats[['G', 'H', 'HR', 'AB', 'R']].mean())

at_bats['1B'] = (at_bats['H'] - at_bats[['2B', '3B', 'HR']].sum(axis=1))

#practice calling summary functions on booleans:
pp['fast_4seam'] = (pp['pitch_type'] == 'FF') & (pp['mph'] >= 100)

print(pp['fast_4seam'].mean())

print(pp['fast_4seam'].sum())

print((pp['mph'] > 104).any())

print((pp['mph'] >= 60).all())

#practice calling boolean summary functions on individual players:
print((at_bats[['H', 'SO']] > 200).any(axis=1).sample(10))

#how many players in our dataset went for more than either 200 hits or 200 strikeouts:
print((at_bats[['H', 'SO']] > 200).any(axis=1).sum())

#how many players in our dataset went for more than BOTH 200 hits AND 200 strikeouts:
print((at_bats[['H', 'SO']] > 200).all(axis=1).sum())

#What about more than 150 hits and strikeouts:
print((at_bats[['H', 'SO']] > 150).all(axis=1).sum())

#how many of each type of pitch was thrown in the 2018 season?:
print(pp['pitch_type'].value_counts())

#same thing but as a percentage:
print(pp['pitch_type'].value_counts(normalize=True))

#how many times was each type of pitch thrown per inning:
print(pd.crosstab(pp['i'], pp['pitch_type']).head(9))

#now as percentages:
print(pd.crosstab(pp['i'], pp['pitch_type'], normalize=True).head(9))
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
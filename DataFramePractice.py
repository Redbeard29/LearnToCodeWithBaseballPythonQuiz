import pandas as pd
from os import path
import numpy as np

DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'

pp = pd.read_csv(path.join(DATA_DIR, '100-game-sample', 'pitches.csv'))

#creating a new variable and assigning it to a simplified version of our pp DataFrame
pp['mph_max'] = 104.3
simple_pp = pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'pitch_type', 'mph', 'mph_max']]

#reassigning max_mph variable
pp['mph_max'] = 105.1
simple_pp = pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'pitch_type', 'mph', 'mph_max']]

#doing basic math with data from our pp DataFrame:
pp['sz_height'] = pp['sz_top'] - pp['sz_bot']
pp_sz = pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'sz_top', 'sz_bot', 'sz_height']].head(10)

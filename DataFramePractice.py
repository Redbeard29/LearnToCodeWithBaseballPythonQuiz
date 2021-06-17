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

#calculate distance of each pitch from middle of plate:
pp['distance_from_middle_of_plate'] = np.abs(pp['x0'])

#calculate the natura log^2 of spin rate:
pp['ln_spin_rate'] = np.log(pp['spin_rate'])

#add a constant 'season' variable throughout the entire DataFrame:
pp['season'] = 2018

#returning a random sample of data from our table:
print(pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'pitch_type', 'mph', 'season']].sample(10))

#creating a basic boolean column:
pp['is_a_FF'] = (pp['pitch_type'] == 'FF')

#using logical and and or with boolean columns:
pp['is_a_FF_or_SL'] = (pp['pitch_type'] == 'FF') | (pp['pitch_type'] == 'SL')
pp['fast_fastball'] = ((pp['pitch_type'] == 'FF') & (pp['mph'] >= 95))

#practice applying my own functions to a DataFrame:

def is_fastball(pitch):
    """
    Takes in a pitch as a string (Ex: 'CH', 'FF', 'FC') and determines whether or not it is a type of fastball.
    The types of fastballs we're working with are: cutter, four-seam, two-seam, sinker, and splitter.
    """
    return pitch in ['FC', 'FF', 'FT', 'SI', 'FS']

pp['is_fastball'] = pp['pitch_type'].apply(is_fastball)

#This could also be done in one step with a lambda function:

pp['is_fastball_alt'] = pp['pitch_type'].apply(lambda x: x in ['FC', 'FF', 'FT', 'SI', 'FS'])

pp.drop('is_fastball_alt', axis=1, inplace=True)

pp.rename(columns={'i': 'inning'}, inplace=True)

#renaming columns using a list comprehension:
pp.columns = [x.upper() for x in pp.columns]

#changing back because uppercase is not pandas convention:
pp.columns = [x.lower() for x in pp.columns]

#same concept using the .rename() function:
pp.rename(columns={'i': 'inning'}, inplace=True)


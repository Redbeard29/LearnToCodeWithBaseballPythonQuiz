import pandas as pd
from os import path
import numpy as np

DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'
games = pd.read_csv(path.join(DATA_DIR, '100-game-sample', 'games.csv'))
pp = pd.read_csv(path.join(DATA_DIR, '100-game-sample', 'pitches.csv'))

games.set_index('g_id', inplace=True)

first_game_id = 201800050

random_game_ids = [201800050, 201801909, 201800465]

random_games_with_args = games.loc[random_game_ids, ['home_team', 'away_team', 'date', 'attendance', 'elapsed_time']]

#returning a list of games that were delayed due to weather:
is_delayed = games['delay'] > 0
games_delayed = games.loc[is_delayed]

#games that had a long delay:
games_long_delay = games.loc[games['delay'] > 60]

is_a_long_game = games['elapsed_time'] > 200

long_and_delayed = games.loc[is_a_long_game & is_delayed]

#creating a pitcher_type column, and populating based on inning that pitcher is called:
pp['pitcher_type'] = np.nan

pp.loc[pp['i'] < 5, 'pitcher_type'] = 'starter'
pp.loc[
    (pp['i'] <= 7) &
    (pp['i'] >= 5), 'pitcher_type'] = 'middle reliever'
pp.loc[pp['i'] == 8, 'pitcher_type'] = 'setup'
pp.loc[pp['i'] >= 9, 'pitcher_type'] = 'closer'

print(pd.crosstab(pp['i'], pp['pitcher_type']))

games['is_delayed'] = games['delay'] > 0

print(games.query("is_delayed").head())

games.query("weather.str[0] == '9'")[['home_team', 'away_team', 'weather']].head()
import pandas as pd
from os import path

#importing filepath to Learn to Code with Baseball Folder
DATA_DIR = '/Users/benjaminsherman/Desktop/Documents/PersonalProjects/DataAnalyticsProjects/LearnToCodeWithBaseball/Files/ltcwbb-files-main/data'

#appending two more folders to get the specific file for these examples
players = pd.read_csv(path.join(DATA_DIR, '2018-season', 'players.csv'))

#printing the first three players
print(players.head(3))

#printing the list of all columns in the DataFrame
print(players.columns)

#printing the dimensions of the DataFrame
print(players.shape)

#printing only the names of the first 15 players in the DataFrame
print(players['name'].head(15))

#printing the name, height, weight, and debut date of the first 10 players in the DataFrame
print(players[['name', 'height', 'weight', 'debut']].head(10))

#returning a 'view' with the index value of our DataFrame set to the 'PlayerID' value
print(players.set_index('playerID').head(10))

#in order to reassign the index value to be the 'PlayerID' permanently:
players.set_index('playerID', inplace=True)

#reset the index value to the original numbers:
players.reset_index().head(10)

#return only the Cuban players, and store them in a variable:
players_cuba = players.loc[
    players['birthCountry'] == 'Cuba',
    ['name', 'height', 'weight', 'birthCountry']
]

#sorting Cuban players by weight:
players_cuba.sort_values('weight', inplace=True)

#adding in the Cuban players' batting arms:
players_cuba['bats'] = players['bats']

#save the players_cuba dataframe to a csv file:
players_cuba.to_csv(path.join(DATA_DIR, '2018-season', 'players_cuba.csv'))

#creating a debut_month variable from our debut variable to practice type conversion:
players['debut_month'] = players['debut'].astype(str).str[4:6]

#converting the debut_month back to int type:
players['debut_month'].astype(int).head(10)
roster_list = ['clayton kershaw', 'mookie betts', 'cody bellinger']

roster_list_upper = []

for player in roster_list:
    roster_list_upper.append(player.title())

roster_list_proper = [x.title() for x in roster_list]

last_names = [full_name.split(' ')[1] for full_name in roster_list]

roster_c_only = [x.title() for x in roster_list if x.startswith('c')]

salary_per_player = {
    'clayton kershaw': 31000000,
    'mookie betts': 27000000,
    'cody bellinger': 11500000
}

salary_m_per_upper_player = {
    name.upper(): salary/1000000 for name, salary in salary_per_player.items()}

sum_of_salaries = sum([salary for _, salary in salary_per_player.items()])

def hr_sweetspot(launch_angle, exit_velocity):
    return (25 <= launch_angle <= 35) and (exit_velocity >= 95)

#exercise 2.3:

def announce_pitch(player_name, pitch):
   return f"{player_name} with the {pitch}!"

#exercise 2.5:

def is_travisd(player_name):
    return player_name.replace("'", "").lower() == "travis darnaud"

#exercise 2.6:

def commentary(batting_avg):
    if batting_avg >= 300:
        return f'{batting_avg} is a good avg'
    else:
        return f"{batting_avg}'s not that good"

#exercise 2.7:

def commentary_plus_decimal(batting_avg):
    if batting_avg < 1:
        batting_avg = int(batting_avg*1000)

    return commentary(batting_avg)

#exercise 2.8:

dodgers_roster = ['clayton kershaw', 'cody bellinger', 'mookie betts']

#1:
print(dodgers_roster[0:2]),

#2:
print(dodgers_roster[:2])

#3:
print([name for name in roster_list if name.startswith('c')])

#4:
print([name for name in dodgers_roster if name != 'mookie betts'])

#exercise 2.9:
pitcher_info = {'starter': 'Kershaw', 'throws_right': False}

#A:
pitcher_info['starter'] = 'Joe Kelly'

#B:
def toggle_throws(pitcher):
    pitcher['throws_right'] = not pitcher['throws_right']
    return pitcher

#exercise 2.11:
my_roster_list = ['clayton kershaw', 'mookie betts', 'cody bellinger']

#A:
for player in my_roster_list:
    print(player.split(' ')[-1])

#B:
{player: len(player) for player in my_roster_list}

#exercise 2.12:
my_roster_dict = {'p': 'clayton kershaw', 'rf': 'mookie betts', '1b': 'cody bellinger'}

#A:
print([pos for pos in my_roster_dict])
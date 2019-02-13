import random
import os
team = []
print()
teamsize = int(input('Choose a team size: ').strip())
os.system('cls')
print('Input a name. Type \'done\' when you are finished.\n')
os.system('cls')
while True:
    name = input().lower().strip()
    if name != 'done':
        team.append(name)
    else:
        break
teamnum = 1
while len(team) > 0:
    array = []
    if len(team) >= teamsize:
        for x in range(teamsize):
            indiv = random.choice(team)
            array.append(indiv.capitalize())
            team.remove(indiv)
    else:
        for x in range(len(team)):
            indiv = random.choice(team)
            array.append(indiv.capitalize())
            team.remove(indiv)
    print(f'Team {teamnum}: {array}')\
    array = ', '.join(array)
    teamnum += 1
    array = []
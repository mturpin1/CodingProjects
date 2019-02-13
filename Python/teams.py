import random
import os
import time
people = []
input('''This is an application that will take in names for teams.
It will then give you teams of the specified size. Press \'Enter\' to continue...''')
os.system('cls')
peoples = int(input('Please enter how big each team will be: '))
while True:
    name = input('Please enter a name(when you are finished entering names, type \'done\'): ')
    if name == 'done':
        os.system('cls')
        break
    else:
        people.append(name)
while len(people) > 0:
    for x in range(0 , len(people)):
        print(f'Team {}{people[randPerson]}: Team {random.randint(1, teams)}')
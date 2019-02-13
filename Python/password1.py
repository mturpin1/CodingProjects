import os
database = {}
for x in range(3):
    database.update({input('Please enter a username: ') : input('Please enter a password for that username: ')})
    os.system('cls')
print('\nDatabase complete. All 3 users have signed up.\n')
os.system('cls')
username = input('Enter your username: ')
os.system('cls')
password = input('Enter your password: ')
os.system('cls')
for user in database:
    if username == user:
        if password == database[user]:
            print('\nCongratulations! You Have Successfully Logged In\n')
            break
        else:
            print('\nYour Password Is Incorrect\n')
            break
        break
    else:
        print('\nYour Username Is Not In The Database.\n')
        break
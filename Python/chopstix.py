import os
import time
import random
def rules():
        rule = raw_input('''To view the rules, press \'Enter\'.
To skip the rules, type \'skip\', then press \'Enter\'. . .''').lower()
        if rule == 'skip':
            os.system('clear')
            print('*gameplay goes here*')
            for x in range(50):
                for x in range(75):
                    number = random.randint(0, 9)
                    print(f'{number}', end = '')
            #gameplay()
        elif rule == '':
            os.system('clear')
            rules_1 = raw_input('''*the first set of rules for the game*''')
def chopstix():
    os.system('clear')
    welcome = raw_input('''Hello! Welcome to the Chopstix game. Please press \'Enter\' to begin. . .''')
    if welcome == '':
        os.system('clear')
        rules()
chopstix()
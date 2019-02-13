import os
import time
def welcome():
    name = input('Hello, and welcome to the PC Terminal. Please enter your name: ')
    login(name)
def login(name):
    pword = input('Hello, %s. Please enter a password (it must be 8 or more characters long): ' %(name))
    os.system('cls')
    pwordCheck = input('Please verify your password, %s: ' %(name))
    os.system('cls')
    if str(pword) == str(pwordCheck):
        os.system('cls')
        choice = input('Your passwords match; you are good to go! Type \'lin.(your username)\' to login: ')
        if choice == f'lin.{name}':
            print('[Code Goes Here]')
        else:
            print('Error')
    else:
        print('You made a mistake')
        time.sleep(3)
        os.system('cls')
        exit()
welcome()
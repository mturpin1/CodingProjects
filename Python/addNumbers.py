import os
import time
def addition():
    os.system('clear')
    sum = firstNumber # sets the variable 'sum1' to the value of the variable 'firstNumber'
    print sum, # prints the variable 'sum1'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to add:   ')
        if number.lower() == 'sum':
            print sum,
            raw_input()
        elif number.isdigit(): 
            sum += int(number)
            os.system('clear')
        elif number.lower() == 'sub' or number.lower() == 'subtract' or number.lower() == '-':
            subtraction()
        elif number.lower() == 'multiply' or number.lower() == '*' or number.lower() == 'x':
            division()
        elif number.lower() == 'division' or number.lower() == 'divide' or number.lower() == '/':
            division()
        else:
            print('Let\'s try that again. . .')
            time.sleep(1.0)

def subtraction():
    os.system('clear')
    difference = firstNumber # sets the variable 'difference' to the value of the variable 'firstNumber'
    print difference, # prints the variable 'difference'
    raw_input() # used 

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to subtract:   ')
        if number.lower() == 'difference':
            print difference,
            raw_input()
        elif number.isdigit(): 
            difference -= int(number)
            os.system('clear')
        elif number.lower() == 'add' or number.lower() == 'addition' or number.lower() == '+':
            addition()
        elif number.lower() == 'multiply' or number.lower() == '*' or number.lower() == 'x':
            multiply()
        elif number.lower() == 'division' or number.lower() == 'divide' or number.lower() == '/':
            division()
        else:
            print('Let\'s try that again. . .')
            time.sleep(1.0)

def multiplication():
    os.system('clear')
    product = firstNumber # sets the variable 'product' to the value of the variable 'firstNumber'
    print product, # prints the variable 'product'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to multiply:   ')
        if number.lower() == 'product':
            print product,
            raw_input()
        elif number.isdigit(): 
            product *= int(number)
            os.system('clear')
        elif number.lower() == 'add' or number.lower() == 'addition' or number.lower() == '+':
            addition()
        elif number.lower() == 'sub' or number.lower() == 'subtraction' or number.lower() == '-':
            subtraction()
        elif number.lower() == 'division' or number.lower() == 'divide' or number.lower() == '/':
            division()
        else:
            print('Let\'s try that again. . .')
            time.sleep(1.0)

def division():
    os.system('clear')
    quotient = firstNumber # sets the variable 'quotient' to the value of the variable 'firstNumber'
    print quotient, # prints the variable 'quotient'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to divide by:   ')
        if number.lower() == 'quotient':
            print quotient,
            raw_input()
        elif number.isdigit(): 
            quotient /= int(number)
            os.system('clear')
        elif number.lower() == 'add' or number.lower() == 'addition' or number.lower() == '+':
            addition()
        elif number.lower() == 'sub' or number.lower() == 'subtraction' or number.lower() == '-':
            subtraction()
        elif number.lower() == 'multiply' or number.lower() == '*' or number.lower() == 'x':
            multiplication()
        else:
            print('Let\'s try that again. . .')
            time.sleep(1.0)

os.system('clear')
firstNumber = int(raw_input('Enter the first number:    ')) # denotes the first number that the user wants to add
function = raw_input('''What function would you like to perform? –type \'addition\', \'subtraction\', \'multiplication\', or \'division\'.
Note: You can change this at any point throughout your use of this calculator:   ''').lower()

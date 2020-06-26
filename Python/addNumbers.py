import os
import time
os.system('clear')
firstNumber = int(raw_input('Enter the first number:    ')) # denotes the first number that the user wants to use for any calculation
result = int(firstNumber)
def addition():
    global result
    os.system('clear')
    print result, # prints the variable 'result'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to add:   ')
        if number.lower() == 'result':
            print result,
            raw_input()
        elif number.lower() == 'sub' or number.lower() == 'subtract' or number.lower() == '-':
            subtraction()
        elif number.lower() == 'multiply' or number.lower() == 'multiplication' or number.lower() == '*' or number.lower() == 'x':
            multiplication()
        elif number.lower() == 'division' or number.lower() == 'divide' or number.lower() == '/':
            division()
        elif number.lower().islower():
            print('Let\'s try that again. . .')
            time.sleep(1.0)
        else: 
            result += int(number)
            os.system('clear')
        
def subtraction():
    global result
    os.system('clear')
    print result, # prints the variable 'result'
    raw_input() # used 

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to subtract:   ')
        if number.lower() == 'result':
            print result,
            raw_input()
        elif number.lower() == 'add' or number.lower() == 'addition' or number.lower() == '+':
            addition()
        elif number.lower() == 'multiply' or number.lower() == 'multiplication' or number.lower() == '*' or number.lower() == 'x':
            multiply()
        elif number.lower() == 'division' or number.lower() == 'divide' or number.lower() == '/':
            division()
        elif number.lower().islower():
            print('Let\'s try that again. . .')
            time.sleep(1.0)
        else: 
            result -= int(number)
            os.system('clear')
        
def multiplication():
    global result
    os.system('clear')
    print result, # prints the variable 'result'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to multiply:   ')
        if number.lower() == 'result':
            print result,
            raw_input()
        elif number.lower() == 'add' or number.lower() == 'addition' or number.lower() == '+':
            addition()
        elif number.lower() == 'sub' or number.lower() == 'subtraction' or number.lower() == '-':
            subtraction()
        elif number.lower() == 'division' or number.lower() == 'divide' or number.lower() == '/':
            division()
        elif number.lower().islower():
            print('Let\'s try that again. . .')
            time.sleep(1.0)
        else: 
            result *= int(number)
            os.system('clear')
        
def division():
    global result
    os.system('clear')
    print result, # prints the variable 'result'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to divide by:   ')
        if number.lower() == 'result':
            print result,
            raw_input()
        elif number.lower() == 'add' or number.lower() == 'addition' or number.lower() == '+':
            addition()
        elif number.lower() == 'sub' or number.lower() == 'subtraction' or number.lower() == '-':
            subtraction()
        elif number.lower() == 'multiply' or number.lower() == 'multiplication' or number.lower() == '*' or number.lower() == 'x':
            multiplication()
        elif number.lower().islower():
            print('Let\'s try that again. . .')
            time.sleep(1.0)
        else: 
            result /= int(number)
            os.system('clear')
        
function_dict = {'addition':addition, 'subtraction':subtraction, 'multiplication':multiplication, 'division':division}
func = raw_input('''What function would you like to perform? -type \'addition\', \'subtraction\', \'multiplication\', or \'division\'.
Note: You can change this at any point throughout your use of this calculator:   ''').lower()

function_dict[func]()
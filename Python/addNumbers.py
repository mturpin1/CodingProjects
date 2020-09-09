import os
import time
os.system('clear')
firstNumber =float(raw_input('Enter the first number:    ')) # denotes the first number that the user wants to use for any calculation
result = float(firstNumber) # sets the result number for any operation in the calculator; all operations point back here
def addition():
    global result
    os.system('clear') # clears terminal
    print str(result).strip('.0'), # prints the variable 'result'; since this is a float, .strip('.0') removes the .0 that would appear at the end of any integer, to keep it clean, only putting decimals if it is needed
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to add to the previous number:   ')
        if number.lower() == 'result': # checks if the user wants to see the result of all operations so far
            print str(result).strip('.0'), # prints result of all operations so far
            raw_input() # allows the user to only move on when they're ready, by pressing Enter, instead of instantly restarting the loop
        elif number.lower() == 'sub' or number.lower() == 'subtract' or number.lower() == '-':
            subtraction()
        elif number.lower() == 'multiply' or number.lower() == 'multiplication' or number.lower() == '*' or number.lower() == 'x':
            multiplication()
        elif number.lower() == 'division' or number.lower() == 'divide' or number.lower() == '/':
            division()
        elif number.lower().islower():
            print('Let\'s try that again. . .')
            time.sleep(1.0) # lines 18-26 check if user wants to change operation, or if there is any other extraneous symbols/letters that don't do anything, and restarts the loop
        else: 
            result += float(number)
            os.system('clear') # if none of the above conditions are met, the calculator does the desired numerical operation
        
def subtraction():
    global result
    os.system('clear')
    print str(result).strip('.0'), # prints the variable 'result'
    raw_input() # used 

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to subtract from the previous number:   ')
        if number.lower() == 'result':
            print str(result).strip('.0'),
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
            result -= float(number)
            os.system('clear')
        
def multiplication():
    global result
    os.system('clear')
    print str(result).strip('.0'), # prints the variable 'result'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to multiply the previous number by:   ')
        if number.lower() == 'result':
            print str(result).strip('.0'),
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
            result *= float(number)
            os.system('clear')
        
def division():
    global result
    os.system('clear')
    print str(result).strip('.0'), # prints the variable 'result'
    raw_input()

    while True:
        os.system('clear')
        number = raw_input('Enter the number you want to divide the previous number by:   ')
        if number.lower() == 'result':
            print str(result).strip('.0'),
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
            result /= float(number)
            os.system('clear')
        
function_dict = {'addition':addition, 'subtraction':subtraction, 'multiplication':multiplication, 'division':division} # dictionary to store all functions, so they can be called with user input
func = raw_input('''What function would you like to perform? -type \'addition\', \'subtraction\', \'multiplication\', or \'division\'.
Note: You can change this at any point throughout your use of this calculator, merely by typing the name of the operation, or the operator itself:   ''').lower() # takes user input to call a function

function_dict[func]() # calls appropriate function, using user input to check the dictionary for the proper function desired
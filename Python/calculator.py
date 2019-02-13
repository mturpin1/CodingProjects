num1 = int(input('Give me the first number.   '))
oper = input('What is the operation?   ')
num2 = int(input('Give me the second number.   '))
def calculator(num1, oper, num2):
    if oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2) 
    elif oper == '*':
        print(num1 * num2) 
    elif oper == '/':
        print(int(num1 / num2)) 
calculator(num1, oper, num2)
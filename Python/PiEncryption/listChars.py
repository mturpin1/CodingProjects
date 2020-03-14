import os
array = []
def inputSubroutine():
    inputVar = input('Please input the character you want added to the array(type \'end\' to end the program):   ')
inputSubroutine()
while (inputVar != 'end'):
    array.add(inputVar)
    os.system('cls')
    inputSubroutine()
print('Here is your array:  ',)
arrayCounter = 0
for x in range(array.len() - 1):
    print('f{array[arrayCounter]}',)
    arrayCounter += 1
print(f' \'{array[arrayCounter]}\'')
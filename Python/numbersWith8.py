import os
numberOfTicks = int(input("Input the number of ticks that can be used:   "))
iterations = 100 * ((numberOfTicks / 2) - (numberOfTicks % 2))
ticksPerNumber = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
uniqueNumbers = []
startingNumber = 0
def ticksInANumber(startingNumber):
    if len(str(startingNumber)) == 1:
        anotherTicksPerNumber = ticksPerNumber[startingNumber]
    elif len(startingNumber) >= 2:
        number = 0
        anotherTicksPerNumber = 0
        for x in range(len(startingNumber)):
            moreTicksPerNumber = ticksPerNumber[startingNumber(number)]
            anotherTicksPerNumber = anotherTicksPerNumber + moreTicksPerNumber
            number += 1
for x in range(iterations):
    ticksInANumber(startingNumber)
    if anotherTicksPerNumber == numberOfTicks:
        uniqueNumbers.add(number)
print '{}' .format(uniqueNumbers[0]),
number1 = 1
for x in range((len(uniqueNumbers) - 1)):
    print ', {}' .format(uniqueNumbers[number1]),
    number1 +=1

import os
numberOfTicks = input("Input the number of ticks that can be used:   ")
ticksPerNumber = {"0": "6", "1": "2", "2": "5", "3": "5", "4": "4", "5": "5", "6": "6", "7": "3", "8": "7", "9": "6"}
uniqueNumbers = []
startingNumber = 0
def ticksInANumber(startingNumber):
    if len(startingNumber) = 1:
        anotherTicksPerNumber = ticksPerNumber[f"{startinNumber}"]
    elif len(startingNumber) > 1:
        number = 0
        anotherTicksPerNumber = 0
        for x in range(len(startingNumber)):
            
while True:
    
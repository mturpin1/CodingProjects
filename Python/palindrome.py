import os

first_letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
second_letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
third_letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

firstLetter = 0
secondLetter = 0
thirdLetter = 0

for x in range(26):
    1stLetter = first_letter[firstLetter]
    firstLetter +=1
    for x in range(26):
        2ndLetter = second_letter[secondLetter]
        secondLetter +=1
        for x in range(26):
            3rdLetter = third_letter[thirdLetter]
            thirdLetter +=1
            print(f"")


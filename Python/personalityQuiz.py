import os
firstLetter = {'E': [0], 'I': [0]}
secondLetter = {'S': [0], 'N': [0]}
thirdLetter = {'T': [0], 'F': [0]}
fourthLetter = {'P': [0], 'J': [0]}
q1_1 = input('Do you enjoy being around people? (Y/N)   ').lower().strip()
while q1_1 != 'y' or q1_1 != 'n':
    if q1_1 == 'y':
        firstLetter['E'][0] += 1
        break
    elif q1_1 == 'n':
        firstLetter['I'][0] += 1
        break
    else:
        q1_1 = input('Do you enjoy being around people? (Y/N)   ').lower().strip()     
q1_2 = input('Do you agree with the following statement: \'I get energy from being alone\'? (Y/N)   ').lower().strip()
while q1_2 != 'y' or q1_2 != 'n':
    if q1_2 == 'y':
        firstLetter['I'][0] += 1
        break
    elif q1_2 == 'n':
        firstLetter['E'][0] += 1
        break
    else:
        q1_2 = input('Do you agree with the following statement: \'I get energy from being alone\'? (Y/N)   ').lower().strip()
q1_3 = input('Do you prefer to hang out alone? (Y/N)   ').lower().strip()
while q1_3 != 'y' or q1_3 != 'n':
    if q1_3 == 'y':
        firstLetter['I'][0] += 1
        break
    elif q1_3 == 'n':
        firstLetter['E'][0] += 1
        break
    else:
        q1_3 = input('Do you prefer to hang out alone? (Y/N)   ').lower().strip()    
q2_1 = input('Do you agree with the following statement: \'I remember events as snapshots of what actually happened.\'? (Y/N)   ').lower().strip()
while q2_1 != 'y' or q2_1 != 'n':
    if q2_1 == 'y':
        secondLetter['S'][0] += 1
        break
    elif q2_1 == 'n':
        secondLetter['N'][0] += 1
        break
    else:
        q2_1 = input('Do you agree with the following statement: \'I remember events as snapshots of what actually happened.\'? (Y/N)   ').lower().strip()      
q2_2 = input('Do you agree with the following statement: \'I remember events by what I read \"between the lines\" about their meaning.\'? (Y/N)   ').lower().strip()
while q2_2 != 'y' or q2_2 != 'n':
    if q2_2 == 'y':
        secondLetter['N'][0] += 1
        break
    elif q2_2 == 'n':
        secondLetter['S'][0] += 1
        break
    else:
        q2_2 = input('Do you agree with the folloring statement: \'I remember events by what I read \"between the lines\" about their meaning.\'? (Y/N)   ').lower().strip()      
q2_3 = input('Do you agree with the following statement: \'I trust experience first and trust words and symbols less.\'? (Y/N)   ').lower().strip()
while q2_3 != 'y' or q2_3 != 'n':
    if q2_3 == 'y':
        secondLetter['S'][0] += 1
        break
    elif q2_3 == 'n':
        secondLetter['N'][0] += 1
        break
    else:
        q2_3 = input('Do you agree with the following statement: \'I trust experience first and trust words and symbols less.\'? (Y/N)   ').lower().strip()      
q3_1 = input('Do you agree with the following statement: \'I notice inconsistencies.\'? (Y/N)   ').lower().strip()
while q3_1 != 'y' or q3_1 != 'n':
    if q3_1 == 'y':
        thirdLetter['T'][0] += 1
        break
    elif q3_1 == 'n':
        thirdLetter['F'][0] += 1
        break
    else:
        q3_1 = input('Do you agree with the following statement: \'I notice inconsistencies.\'? (Y/N)   ').lower().strip()      
q3_2 = input('Do you agree with the following statement: \'I enjoy technical and scientific fields where logic is important.\'? (Y/N)   ').lower().strip()
while q3_2 != 'y' or q3_2 != 'n':
    if q3_2 == 'y':
        thirdLetter['T'][0] += 1
        break
    elif q3_2 == 'n':
        thirdLetter['F'][0] += 1
        break
    else:
        q3_2 = input('Do you agree with the following statement: \'I enjoy technical and scientific fields where logic is important.\'? (Y/N)   ').lower().strip()     
q3_3 = input('Do you agree with the following statement: \'I believe telling the truth is more important than being tactful.\'? (Y/N)   ').lower().strip()
while q3_3 != 'y' or q3_3 != 'n':
    if q3_3 == 'y':
        thirdLetter['T'][0] += 1
        break
    elif q3_3 == 'n':
        thirdLetter['F'][0] += 1
        break
    else:
        q3_3 = input('Do you agree with the following statement: \'I believe telling the truth is more important than being tactful.\'? (Y/N)   ').lower().strip()      
q4_1 = input('Do you agree with the following statement: \'I like to have things decided for me.\'? (Y/N)   ').lower().strip()
while q4_1 != 'y' or q4_1 != 'n':
    if q4_1 == 'y':
        fourthLetter['J'][0] += 1
        break
    elif q4_1 == 'n':
        fourthLetter['P'][0] += 1
        break
    else:
        q4_1 = input('Do you agree with the following statement: \'I like to have things decided for me.\'? (Y/N)   ').lower().strip()      
q4_2 = input('Do you agree with the following statement: \'I appear to be task oriented.\'? (Y/N)   ').lower().strip()
while q4_2 != 'y' or q4_2 != 'n':
    if q4_2 == 'y':
        fourthLetter['J'][0] += 1
        break
    elif q4_2 == 'n':
        fourthLetter['P'][0] += 1
        break
    else:
        q4_2 = input('Do you agree with the following statement: \'I appear to be task oriented.\'? (Y/N)   ').lower().strip()      
q4_3 = input('Do you agree with the following statement: \'I like to make a list of things to do.\'? (Y/N)   ').lower().strip()
while q4_3 != 'y' or q4_3 != 'n':
    if q4_3 == 'y':
        fourthLetter['J'][0] += 1
        break
    elif q4_3 == 'n':
        fourthLetter['P'][0] += 1
        break
    else:
        q4_3 = input('Do you agree with the following statement: \'I like to make a list of things to do.\'? (Y/N)   ').lower().strip()      
if firstLetter['E'] > firstLetter['I']:
    letter1 = 'E'
else:
    letter1 = 'I'
if secondLetter['S'] > secondLetter['N']:
    letter2 = 'S'
else:
    letter2 = 'N'
if thirdLetter['T'] > thirdLetter['F']:
    letter3 = 'T'
else:
    letter3 = 'F'
if fourthLetter['P'] > fourthLetter['J']:
    letter4 = 'P'
else:
    letter4 = 'J'
print(f'Your personality type is {letter1}{letter2}{letter3}{letter4}')
import random
abc = '!#$%&\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
numbers = '1234567890'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters = '!#$%&\()*+,-./:;<=>?@]^_`{|}~'
passwordType = input('What would you like to include: All Characters (\'AC\'), Numbers (\'N\'), Uppercase Letters (\'UL\'), or Just Characters (\'JC\')? ')
passwordLength = input('How long should the password be?   ')
if passwordType == 'AC' or passwordType == 'Ac' or passwordType == 'aC' or passwordType == 'ac':
   for x in range(int(passwordLength)):
       print(abc[random.randint(0, 91)], end ='')
elif passwordType == 'N' or passwordType == 'n':
   for x in range(int(passwordLength)):
       print(numbers[random.randint(0, 9)], end ='')
elif passwordType == 'UL' or passwordType == 'Ul' or passwordType == 'uL' or passwordType == 'ul':
   for x in range(int(passwordLength)):
       print(upperCase[random.randint(0, 25)], end ='')
elif passwordType == 'JC' or passwordType == 'Jc' or passwordType == 'jC' or passwordType == 'jc':
   for x in range(int(passwordLength)):
       print(characters[random.randint(0, 28)], end ='')
else:
   print('You screwed up. Plz try again...')
print('\n')
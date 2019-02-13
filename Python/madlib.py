import os
def madLibs():
    words = []
    input('Hello, and welcome to Mad Libs! Press \'Enter\' to continue...')
    input('''Instructions-The program will ask you for 15 words(noun, adjective, verb, etc.)
After you have given all 15 words, the program will print a story, using the random words you have chosen.
Hold on to your hat, you may create some interesting stories! Press \'Enter\' to continue...\n''')
    os.system('cls')
    words.append(input('Please type an adjective: '))
    words.append(input('Please type an adjective: '))
    words.append(input('Please type an adjective: '))
    words.append(input('Please type a type of bird: '))
    words.append(input('Please type a room in the house: '))
    words.append(input('Please type a verb (past tense): '))
    words.append(input('Please type a verb: '))
    words.append(input('Please type a relative\'s name: '))
    words.append(input('Please type a noun: '))
    words.append(input('Please type a liquid: '))
    words.append(input('Please type averb ending in -ing: '))
    words.append(input('Please type apart of the body (plural): '))
    words.append(input('Please type a plural noun: '))
    words.append(input('Please type averb ending in -ing: '))
    words.append(input('Please type a noun: '))
    os.system('cls')
    print(f'''It was a {words[0]}, cold {words[1]} day. I woke up to the {words[2]} smell of {words[3]} roasting in the {words[4]} downstairs. I {words[5]} 
down the stairs to see if I could help {words[6]} the dinner. My mom said, \"See if {words[7]} needs a fresh {words[8]}.\" So 
I carried a tray of glasses full of {words[9]} into the {words[10]} room. When I got there, I couldn\'t believe my {words[11]}! There
were {words[12]} {words[13]} on the {words[14 ]}!''')
    restart = input('Would you like to restart? (Y/N): ')
    if restart == 'Y' or restart == 'y':
        madLibs()
    else:
        exit()
madLibs()
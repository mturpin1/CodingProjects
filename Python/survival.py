h = 100
import time
def survival():
    def question1_1(welcome):
        q1_1 = input('''
Hello, %s. You are stranded in the desert.
Your job is to survive. Good Luck!
Press \'Enter\' to continue... ''' %(welcome))
        if q1_1 == '':
            desert1_1()
        else:
            question1_1(welcome)
    def desert1_1():
        d1_1 = input('''
YOU HAVE RUN OUT OF WATER

Do you decide to find civilization (\'C\')
        OR
Do you decide to find your own water (\'W\')
''')
        if d1_1 == 'C' or d1_1 == 'c':
            desert2_1()
        elif d1_1 == 'W' or d1_1 == 'w':
            desert2_2()
        else:
            desert1_1()
    def desert2_1():
        d2_1 = input('''
YOU COME UPON A TOWN THAT HAS WATER, BUT ALSO A DEADLY PLAGUE

Do you decide to go into the village (\'V\')
        OR
Do you decide to move on (\'M\')
''')
        if d2_1 == 'V' or d2_1 == 'v':
            desert3_1()
        elif d2_1 == 'M' or d2_1 == 'm':
            desert3_2()
        else:
            desert2_1()
    def desert2_2():
        d2_2 = input('''
YOU KNOW YOU HAVE TO DIG TO FIND WATER

Do you decide to dig your own well (\'O\')
        OR
Do you decide to enlarge an existing hole (\'E\')
''')
        if d2_2 == 'O' or d2_2 == 'o':
            desert3_3()
        elif d2_2 == 'E' or d2_2 == 'e':
            desert3_4()
        else:
            desert2_2()
    def desert3_1():
        d3_1 = input('''
YOU FIND WATER IN THE TOWN

Do you decide to drink the water immediately(you are nearly dying of thirst) (\'I\')
        OR
Do you decide to boil the water (\'B\')
''')
        if d3_1 == 'I' or d3_1 == 'i':
            desert4_1(welcome)
        elif d3_1 == 'B' or d3_1 == 'b':
            desert4_2(welcome)
        else:
            desert3_1()
    def desert3_2():
        d3_2 = input('''
YOU COME UPON A TRUCK ON THE SIDE OF THE DESERT ROAD

Do you decide to keep moving (\'M\')
        OR
Do you decide to help the trucker (\'H\')
''')
        if d3_2 == 'M' or d3_2 == 'm':
            desert4_3(welcome)
        elif d3_2 == 'H' or d3_2 == 'h':
            desert4_4(welcome)
        else:
            desert3_2()
    def desert3_3():
        d3_3 = input('''
YOU DECIDE TO DIG YOUR OWN HOLE

Do you decide to dig a deep well (\'D\')
        OR
Do you decide to dig a shallow hole covered with plastic (\'S\')
''')
        if d3_3 == 'D' or d3_3 == 'd':
            desert4_5(welcome)
        elif d3_3 == 'S' or d3_3 == 's':
            desert4_6(welcome)
        else:
            desert3_3()
    def desert3_4():
        d3_4 = input('''
YOU HAVE FOUND AN APPARENTLY EMPTY SNAKE BURROW

Do you decide to dig right away (\'R\')
        OR
Do you decide to make sure it is cleared out first (\'C\')
''')
        if d3_4 == 'R' or d3_4 == 'r':
            global h
            h -= 25 
            desert4_7(welcome)
        elif d3_4 == 'C' or d3_4 == 'c':
            desert4_8(welcome)
        else:
            desert1_1()
    def desert4_1(welcome):
        global h
        h -= 100 
        d4_1 = input('''
Health Remaining = %s
You decided to find civilization, then you chose to go into the town with the plague.
You decided to drink the water right away without boiling it, and you got the plague from the water.
GAME OVER - YOU DIED, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_1 == 'R' or d4_1 == 'r':
            survival()
        else:
            exit()
    def desert4_2(welcome):
        global h
        d4_2 = input('''
Health Remaining = %s
You decided to find civilization, then you chose to go into the town with the plague.
You decided to boil the water before drinking it, and you killed the germs in the water.
GAME OVER - YOU WIN, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_2 == 'R' or d4_2 == 'r':
            survival()
        else:
            exit()
    def desert4_3(welcome):
        global h
        h -= 100 
        d4_3 = input('''
Health Remaining = %s
You decided to find civilization, then decided to move on from the town with the plague. 
You move on from the broken down truck, but can't find anything/anyone else.
GAME OVER - YOU DIED, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_3 == 'R' or d4_3 == 'r':
            survival()
        else:
            exit()
    def desert4_4(welcome):
        global h
        d4_4 = input('''
Health Remaining = %s
You decided to find civilization, then decided to move on from the town with the plague. 
You decide to help the driver of the broken down truck, and your mechanical knowledge helped you fix the guy's truck.
He gives you some water and food, and you get a ride to the nearest town.
GAME OVER - YOU WIN, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_4 == 'R' or d4_4 == 'r':
            survival()
        else:
            exit()
    def desert4_5(welcome):
        global h
        h -= 100 
        d4_5 = input('''
Health Remaining = %s
You decide to find your own water, and then decide to dig your own well.
You decide to dig a deep well, but it is too deep, and you can't get to the water at the bottom.
GAME OVER - YOU DIED, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_5 == 'R' or d4_5 == 'r':
            survival()
        else:
            exit()
    def desert4_6(welcome):
        global h
        d4_6 = input('''
Health Remaining = %s
You decide to find your own water, and then decide to dig your own well.
You decide to dig a shallow well covered with plastic to catch condensation; your well is perfect, and you collect over a quart of water.
GAME OVER - YOU WIN, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_6 == 'R' or d4_6 == 'r':
            survival()
        else:
            exit()
    def desert4_7(welcome):
        global h
        h -= 100 
        d4_7 = input('''
Health Remaining = %s
You decide to find you own water, and then decide to enlarge an existing hole.
You decide to clear out an old snake burrow without checking for other animals first; you didn't clear out the scorpions who moved in--you get stung multiple times.
GAME OVER - YOU DIED, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_7 == 'R' or d4_7 == 'r':
            survival()
        else:
            exit()
    def desert4_8(welcome):
        global h
        d4_8 = input('''
Health Remaining = %s
You decide to find you own water, and then decide to enlarge an existing hole.
You decide to check for other animals first; you clear out the scorpions, and find water after a little digging.
GAME OVER - YOU WIN, %s
To play again, press \'R\'
''' %(h, welcome))
        if d4_8 == 'R' or d4_8 == 'r':
            survival()
        else:
            exit()
    question1_1(welcome)
welcome = input('''Hello, and welcome to the Survival Game.
What is your name: ''')
time.sleep(3)
survival()
import random
import os
import time
print(input('''Hello, and welcome to the rock-paper-scissors game. I am sure that you know how this goes.
You will be playing 5 rounds agains the computer. Whoever wins the most out of those 5 is the champion!
Press \'Enter\' to continue...'''))
os.system('cls')
player = ''
opp = ''
numOfPlays = 0
playerScore = 0
oppScore = 0
def rps():
    global player
    global opp
    global numOfPlays
    global playerScore
    global oppScore
    player = int(input('What would you like to choose? (\'1\' for rock, \'2\' for paper, and \'3\' for scissors): '))
    opp = random.randint(1, 3)
    if player == 1 and opp == 1:
        numOfPlays += 1
        print(f'''Draw. You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 1 and opp == 2:
        numOfPlays += 1
        oppScore += 1
        print(f'''You Lose...You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 1 and opp == 3:
        numOfPlays += 1
        playerScore += 1
        print(f'''You Win! You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 2 and opp == 1:
        numOfPlays += 1
        playerScore += 1
        print(f'''You Win! You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 2 and opp == 2:
        numOfPlays += 1
        print(f'''Draw. You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 2 and opp == 3:
        numOfPlays += 1
        oppScore += 1
        print(f'''You Lose...You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 3 and opp == 1:
        numOfPlays += 1
        oppScore += 1
        print(f'''You Lose...You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 3 and opp == 2:
        numOfPlays += 1
        playerScore += 1
        print(f'''You Win! You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
    elif player == 3 and opp == 3:
        numOfPlays += 1
        print(f'''Draw. You chose {player}-opponenet chose {opp}
        Player Score-{playerScore}
        Opponent Score-{oppScore}''')
        time.sleep(2)
        os.system('cls')
        numOfPlays += 1
for x in range(5):
    rps()
if playerScore > oppScore:
    print('You Are The Rock-Paper-Scissors Champion!')
elif oppScore > playerScore:
    print('You Lost The Championship...')
else:
    print('The Championship Is A Draw!')


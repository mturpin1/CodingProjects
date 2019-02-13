import os
import time
words = []
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
words.append(input('Type a random word: '))
time.sleep(3)
os.system('cls')
print('Here is your list: [%s, %s, %s, %s, %s, %s, %s, %s, %s, and %s]'
%(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7], words[8], words[9]))
time.sleep(3)
os.system('cls')
del words[4]
print('Here is your list without the 5th item: [%s, %s, %s, %s, %s, %s, %s, %s, and %s]'
%(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7], words[8]))
time.sleep(3)
os.system('cls')
words.remove('%s' %(words[0]))
print('Here is your list without the 1st item: [%s, %s, %s, %s, %s, %s, %s, and %s]'
%(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7]))
time.sleep(3)
os.system('cls')
words.pop(2)
print('Here is your list without the 3rd item: [%s, %s, %s, %s, %s, %s, and %s]'
%(words[0], words[1], words[2], words[3], words[4], words[5], words[6]))
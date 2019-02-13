import os
plainText = input('Please enter a word you would like encrypted - ').lower().strip()
key = int(input('Please enter an encryption key (it can be any whole number) - '))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encryptedText = ''
for letter in plainText:
    index = alphabet.find(letter)
    encryptedText += (alphabet[(index + key) % 26])
os.system('cls')
print(f'Here is your encrypted text - {encryptedText}')
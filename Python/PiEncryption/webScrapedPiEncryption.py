from bs4 import BeautifulSoup #import beautifulsoup module
import requests #imports requests module
import lxml #imports lxml module
import time #imports time module
import os #imports os module

timeBoi = int(time.strftime('%M%S'))  
timeBoi1 = int(time.strftime('%M'))
timeBoi2 = int(time.strftime('%S'))

url = "https://www.piday.org/million/" #connects to webpage

soup = BeautifulSoup(requests.get(url).text, 'lxml') #pyulls date from webpage, using lxml module to specify a parser

pseudoPi = soup.find('div', {"id": "million_pi"}) #finds the <div> tag in the webpage with the id of 'million_pi'

pi = float(pseudoPi) #sets variable 'pi' to a string version of the data just pulled

plainText = ' !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~' 
text = input('Please input the text you want encrypted:   ')

piNum = 0 #sets piNum to 0, which will be used to iterate through pulling the correct number of digits of pi from the <div>

newPi = '' #empty str, where the loop adds the appropriate number of digits of pi

for piNum in range(int(len(text)) + 1): #runs the loop for the length of the 'text' var, plus 1(to compensate for the period in the 'million_pi' <div>)
    newPi += (pi[piNum + 35]) #adds the appropriate number of digits of pi to the 'newPi' var; iterates through the 'pi' var pulled from the webpage, plus 35 to compensate for the tags in the <div>, before the actual numbers of pi

input(f'{newPi}')

encryptedText = '' #empty str var, where the 'for' loop throws the encrypted text after it has been processed

newPiNum = 0 #sets the new Pi iteration number to 0 for the following loop

for char in text: #runs the loop for as many characters are in the 'text' var
    if newPi[newPiNum] == '.': #checks if 'newPi[newPiNum]' is a period. . .
        encryptedText += 'n' #adds a '0' to the 'encryptedText' var, for checking purposes
        newPiNum =+ 1 #adds a '0' to the 'newPiNume' var, in order to keep iterating through the digits of the 'newPi' var
    else: #checks if the number in 'newPi' var the with the index 'newPiNum' is a number
        '''encryptionNumber = (int(newPi[newPiNum])) 
        index = plainText.find(char)
        encryptedText += (plainText[(index + encryptionNumber + timeBoi)] % 95)'''
        encryptedText += 'y' #if the character is a digit, add a '1' to the 'encryptedText' var, for checking purposes
        newPiNum += 1 #add a '1' to the 'newPiNum' var, in order to keep iterating through the digits of the 'newPi' var

print(encryptedText) #prints the 'encryptedText' var

'''
timeBoi1 = str(timeBoi1)
timeBoi2 = str(timeBoi2)
print(timeBoi1 + encryptedText + timeBoi2)'''
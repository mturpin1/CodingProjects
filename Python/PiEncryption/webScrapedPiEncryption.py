from bs4 import BeautifulSoup
import requests
import lxml
import time

timeBoi1 = int(time.strftime('%M'))
timeBoi2 = int(time.strftime('%S'))

url = "https://www.piday.org/million/" 

soup = BeautifulSoup(requests.get(url).text, 'lxml')

pseudoPi = soup.find('div', {"id": "million_pi"})

pi = str(pseudoPi)

piNum = 0

piRange = (int(input('Please enter how many digits of pi you want printed:   ')))

for piNum in range(int(piRange)):
    print(pi[piNum + 35], end ="")

'''    
plainText = ' !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~' 
text = raw_input('Please input the text you want encrypted:   ')

piNum = 0

encryptedText = ''

for char in pi:
    if char.isdigit():
        encryptionNumber = (int(pi[piNumber]))
        index = plainText.find(char)
        encryptedText += (plainText[(index + encryptionNumber + timeBoi) % 95])
        piNum += 1
    else:
        piNum =+ 1

timeBoi1 = str(timeBoi1)
timeBoi2 = str(timeBoi2)
print(timeBoi1 + encryptedText + timeBoi2)
'''
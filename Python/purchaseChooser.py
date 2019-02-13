import os
import time
stuff = []
print('''Welcome to the purchase chooser, you rich jerk.
Must be so hard to pick what you wanna buy with daddy's money.''')
time.sleep(3)
os.system('cls')
stuff.append(input('Name an item on your wishlist: '))
stuff.append(input('Name another item on your wishlist: '))
stuff.append(input('Name another item on your wishlist: '))
stuff.append(input('Name another item on your wishlist: '))
stuff.append(input('Name another item on your wishlist: '))
stuff.append(input('Name another item on your wishlist: '))
stuff.append(input('Name another item on your wishlist: '))
stuff.append(input('Name another item on your wishlist: '))
print(input('''YOUR WISHLIST
1-%s
2-%s
3-%s
4-%s
5-%s
6-%s
7-%s
8-%s'''
%(stuff[0], stuff[1], stuff[2], stuff[3], stuff[4], stuff[5], stuff[6], stuff[7])))
stuff.remove(input('Choose the item you really don\'t need: '))
os.system('cls')
print('''YOUR NEW WISHLIST
1-%s
2-%s
3-%s
4-%s
5-%s
6-%s
7-%s'''
%(stuff[0], stuff[1], stuff[2], stuff[3], stuff[4], stuff[5], stuff[6]))
stuff.pop(int(input('Choose the number of an item that is too expensive right now: ')))
os.system('cls')
print('''YOUR NEW WISHLIST
1-%s
2-%s
3-%s
4-%s
5-%s
6-%s'''
%(stuff[0], stuff[1], stuff[2], stuff[3], stuff[4], stuff[5]))
stuff.pop(int(input('Choose the number of an item you can wait to buy: ')))
os.system('cls')
print('''YOUR NEW WISHLIST
1-%s
2-%s
3-%s
4-%s
5-%s'''
%(stuff[0], stuff[1], stuff[2], stuff[3], stuff[4]))
stuff.pop(int(input('Choose the number of an item you can borrow from a friend: ')))
os.system('cls')
print('''YOUR NEW WISHLIST
1-%s
2-%s
3-%s
4-%s'''
%(stuff[0], stuff[1], stuff[2], stuff[3]))
stuff.pop(int(input('Choose the number of an item you could probably find around your house: ')))
os.system('cls')
print('''YOUR NEW WISHLIST
1-%s
2-%s
3-%s'''
%(stuff[0], stuff[1], stuff[2]))
stuff.pop(int(input('Choose the number of an item could probably make yourself: ')))
os.system('cls')
print('''YOUR NEW WISHLIST
1-%s
2-%s'''
%(stuff[0], stuff[1]))
stuff.pop(int(input('Choose the number of an item you want the least: ')))
os.system('cls')
print('You should buy the %s you have always wanted.' %(stuff[0]))
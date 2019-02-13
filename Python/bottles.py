import time
def bottlesSong():
    bottles = int(input('How many bottles of Sprite are starting on the wall? '))
    bottles2 = bottles
    while bottles >= 0:
        if bottles > 1:
            print(f'''{bottles} bottles of Sprite on the wall, {bottles} bottles of Sprite
Take one down, pass it around, {bottles - 1} bottles of Sprite on the wall''')
        elif bottles == 1:
            print(f'''{bottles} bottle of Sprite on the wall, {bottles} bottle of Sprite
Take one down, pass it around, {bottles - 1} bottles of Sprite on the wall''')
        elif bottles == 0:
            print(f'''No more bottles of Sprite on the wall, no more bottles of Sprite.
Go to the store and buy some more, {bottles2} bottles of Sprite on the wall.\n''')
            restart = input('Would you like to start the song over? (\'Yes\' or \'No\') ')
            if restart == 'NO' or restart == 'no' or restart == 'No' or restart == 'nO':
                exit()
            else:
                bottlesSong()
        time.sleep(.1)
        bottles -= 1 
bottlesSong()
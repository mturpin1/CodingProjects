names = ['emily', 'derek', 'jacob', 'anthony', 'layla', 'alex', 'nathan', 'esquiely', 'william', 'elliot', 'nathan', 'ellis', 'ian', 'micah', 'carlos', 'david', 'grace', 'austin']
i = 0
listNum = 1
while i < len(names):
    if names[i][0] == 'a' or names[i][0] == 'j' or names[i][0] == 'i' or names[i][0] == 'e' or names[i][0] == 'b' or names[i][0] == 'x':
        print(f'{listNum}. {names[i]} will be a wonderful student.')
    elif names[i][0] == names[i][0] == 'y' or names[i][0] == 'e' or names[i][0] == 'o' or names[i][0] == 'd' or names[i][0] == 'q' or names[i][0] == 'l':
        print(f'{listNum}. {names[i]} will be an awful student.')
    else:
        print(f'{listNum}. {names[i]} will be a boring student.')
    i += 1
    listNum += 1    

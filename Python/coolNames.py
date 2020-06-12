import random
name = raw_input('Enter the name you want to change:   ').lower()
vowels = 'aeiouy'
hardSounds = 'bdgjmnptv'
hardSoftSounds = 'cks'
softSounds = 'fhlr'
weirdSounds = 'qwxz'
newName = ''
for char in name:
    if char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4] or char == vowels[5]:
        changeNumber = random.randint(0, len(vowels))
        index = vowels.find(char)
        newName += (vowels[(index + changeNumber) % len(vowels)])
    elif char == hardSounds[0] or char == hardSounds[1] or  char == hardSounds[2] or char == hardSounds[3] or char == hardSounds[4] or char == hardSounds[5] or char == hardSounds[6] or char == hardSounds[7] or char == hardSounds[8]:
        changeNumber = random.randint(0, len(hardSounds))
        index = hardSounds.find(char)
        newName += (hardSounds[(index + changeNumber) % len(hardSounds)])
    elif char == hardSoftSounds[0] or char == hardSoftSounds[1] or char == hardSoftSounds[2]:
        changeNumber = random.randint(0, len(hardSoftSounds))
        index = hardSoftSounds.find(char)
        newName += (hardSoftSounds[(index + changeNumber) % len(hardSoftSounds)])
    elif char == softSounds[0] or char == softSounds[1] or char == softSounds[2] or char == softSounds[3]:
        changeNumber = random.randint(0, len(softSounds))
        index = softSounds.find(char)
        newName += (softSounds[(index + changeNumber) % len(softSounds)])
    elif char == weirdSounds[0] or char == weirdSounds[1] or char == weirdSounds[2] or char == weirdSounds[3]:
        changeNumber = random.randint(0, len(weirdSounds))
        index = weirdSounds.find(char)
        newName += (weirdSounds[(index + changeNumber) % len(weirdSounds)])
    else:
        newName += char
print('Your new name is ' + newName.capitalize())
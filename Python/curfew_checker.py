age = input('How old are you?: ')
age = int(age)
time = input('What hour is it?: ')
time = int(time)
def curfew_check():
    if age >= 0 and age <= 12:
        print('\"Get off the computer, please.\"')
    elif (age > 12 and age <= 16) and (time >= 0 and time <= 8):
        print('\"You should be asleep!\"')
    elif (age > 12 and age <= 16) and (time > 8 and time <= 20):
        print('\"You are good!\"')
    elif (age > 12 and age <= 16) and (time > 20 and time <= 24):
        print('\"Your curfew is up!\"')
    elif (age >= 17 and age <= 18) and (time >= 0 and time <= 6):
        print('\"You should be asleep!\"')
    elif (age >= 17 and age <= 18) and (time > 6 and time <= 22):
        print('\"You are good!\"')
    elif (age >= 17 and age <= 18) and (time > 22 and time <= 24):
        print('\"Your curfew is up!\"')
    elif age > 18:
        print('\"Do whatever you want!\"')
curfew_check()

time = input('What hour is it?')
time = int(time)
if time >= 7 and time <=11:
    print('Good Morning!')
elif time > 11 and time <= 17:
    print('Good Afternoon!')
elif time > 17 and time <= 22:
    print('Good Evening!')
else:
    print('Good Night!')








'''
if the time is between 7am and 11am
  say 'Good morning'
otherwise, if the time is between 11am and 5pm
  say 'Good afternoon'
otherwise, if the time is between 5pm and 10pm
  say 'Good evening'
otherwise
  say 'Good night'
'''
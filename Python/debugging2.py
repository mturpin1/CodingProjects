time = int(input('What hour is it? '))

def time_checker(time):
  if time >= 0 and time <= 5:
    print('It is night.')
  elif time > 5 and time <= 12:
    print('It is morning.')
  elif  time > 12 and time <=17:
    print('It is afternoon.')
  elif time > 17 and time <= 20:
    print('It is evening.')
  elif time > 20 and time <= 24:
    print('It is night.')
time_checker(time)
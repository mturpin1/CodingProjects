num = int(input('How old are you? '))

def vote_check(age):
  if num <= 18:
    print('You cannot vote!')
  else:
    print('You can definitely vote!')
vote_check(num)
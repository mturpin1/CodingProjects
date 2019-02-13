color = input('Pick a color. ')
def color_choice(color):
  if color == 'red' or color == 'Red':
    print('You chose red.')
  elif color == 'blue' or color == 'Blue':
    print('You chose blue.')
  elif color == 'orange' or color == 'Orange':
    print('You chose orange.')
  else:
    print('You screwed something up.')
color_choice(color)
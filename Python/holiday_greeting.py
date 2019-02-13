welcome = input('Welcome to the Holiday Card Builder! Press \'Enter\' to continue.')
def holiday_greeting(holiday_greeting = '\"Happy Mother\'s Day, Mom! -- From Your Favorite Child\"'):
    who_to = input('Who is this card to? ')
    who_from = input('Who is this card from? ')
    holiday = input('What holiday is this card for? ')
    print ('\"Happy %s, %s! - From %s\"' %(holiday, who_to, who_from))

holiday_greeting()
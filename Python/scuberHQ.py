block = input('Welcome to Scuber. Please give me the street number of your destination.   ')
def distance_from_hq(block):
    if int(block) > int(42):
        print('You are %s blocks away from Scuber Headquarters.' %((int(block) - 42)/13))
        print('You are %s feet away from Scuber Headquarters.' %(((int(block) - 42)/13)*264))
        print('You are %s miles away from Scuber Headquarters.' %((((int(block) - 42)/13)*264)/5280))
    elif int(block) < int(42):
        print('You are %s blocks away from Scuber Headquarters.' %((42 - int(block))/13))
        print('You are %s feet away from Scuber Headquarters.' %(((42 - int(block))/13)*264))
        print('You are %s miles away from Scuber Headquarters.' %((((42 - int(block))/13)*264)/5280))
        

    


distance_from_hq(block)



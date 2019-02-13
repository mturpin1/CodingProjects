'''
1. Write a function called no_puppies that takes in a number of puppies as an argument.
If the number of puppies is greater than zero then this function should return "No more puppies!"
otherwise it should return "Well done, Rachel!"
'''
# code your solution on line 7

def no_puppies():
    puppies = input('Enter the number of puppies: ')
    puppies = int(puppies)
    if puppies > 0:
        print('\"No more puppies!\"')
    else:
        print('\"Well done, Rachel!\"')
no_puppies()

#remove the # symbol on line 10 when you're ready to test the function
#no_puppies()
'''
2. Rachel's animal accumulation has been going well and we're going to cut her some slack.
Write a new function called less_puppies that takes in a number of puppies as an argument
and tells Rachel good job when she gets less than 3 puppies, to slow down if she's found exactly 3 puppies,
and to get back on her animal restriction if she gets more than 3 puppies.
'''
# code your solution on line 17

def less_puppies():
    puppies2 = input('Enter the number of puppies: ')
    puppies2 = int(puppies2)
    if puppies2 < 3:
        print('\"Good job, Rachel!\"')
    elif puppies2 == 3:
        print('\"Slow down, Rachel!\"')
    elif puppies2 > 3:
        print('\"Get back on your animal restriction, Rachel!\"')
less_puppies()

#remove the # symbol on line 21 when you're ready to test the function
#less_puppies()
'''
3. We've decided to give Rachel a little more control over her puppy obsession.
Write a function called some_puppies that takes in two arguments -
the number of puppies she has found and a maximum puppy allowance.
This function should tell Rachel good job if she gets less than half her maximum allowance
and to get back on her puppy restriction when she exceeds her maximum.
'''
# code your solution on line 28

def some_puppies():
    puppy_allowance = input('Enter the maximum puppy allowance for Rachel: ')
    puppy_allowance = int(puppy_allowance)
    puppies3 = input('Enter the number of puppies: ')
    puppies3 = int(puppies3)
    if puppies3 < (puppy_allowance/2):
        print('\"Good job, Rachel!\"')
    elif puppies3 > puppy_allowance:
        print('\"Get back on your puppy restriction, Rachel!\"')
    else:
        print('\"Can\'t say good job, can\'t say bad job, Rachel.')
some_puppies()



#remove the # symbol on line 33 when you're ready to test the function
#some_puppies()
'''
BONUS (complete only if you have leftover time before the solution is shown)
# 4. Rachel has decided to track both her puppy allowance AND her cat allowance.
# Write a function called new_animal accumulation that takes in two arguments - number of puppies and number of cats.
# As long as she gets zero puppies OR zero cats this function should return "Good job!".
# If she gets 1 or more puppies AND 1 or more cats it should tell her she should really slow back down!
'''
# code your solution on line 39

def new_animal_accumulation():
    dogs = input('Enter the number of puppies: ')
    dogs = int(dogs)
    cats = input('Enter the number of cats: ')
    cats = int(cats)
    if dogs == 0 or cats == 0:
        print('\"Good job, Rachel!\"')
    elif dogs >= 1 and cats >= 1:
        print('\"You really need to slow back down, Rachel!\"')
new_animal_accumulation()

#remove the # symbol on line 45 when you're ready to test the function
#new_animal()
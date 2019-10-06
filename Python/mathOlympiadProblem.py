m = input("Enter the value that \'m\' will equal(it must be the square of an integer):   ")
a = input("Enter the value that you want check for \'a\':   ")
b = 0
for x in range(100):
    answer = ((a^2) + (b^2) / (a * b + 1))
    if answer == m:
        print ("The value of \'b\' when \'m\' = %s and \'a\' = %s is %s." % (m, a, b))
        print ("The value of \'a\' when \'m\' = %s and \'b\' = %s is %s." % (m, a, b))
        b += 1
    elif answer != m:
        b += 1
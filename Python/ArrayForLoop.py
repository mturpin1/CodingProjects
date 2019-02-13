students = ['emily', 'derek', 'anthony', 'jacob', 'layla', 'alex', 'william', 'ellis', 'nathan', 'elliott', 'ian', 'bryan', 'edward', 'joseph', 'payton', 'clarence', 'devin', 'carlos', 'austin', 'david', 'grace', 'micah', 'esqueily']
for student in students:
    if student[0] == 'l':
        print(f'{student.capitalize()} will be a wonderful student.')
    elif student[0] == 'j':
        print(f'{student.capitalize()} will be a terrible student.')
    else:
        print(f'{student.capitalize()} will be a boring student.')
students = ['Emily', 'Derek', 'Anthony', 'Jacob', 'Layla', 'Alexander', 'William', 'Ellis', 'Nathan', 'Elliot', 'Ian', 'Bryan', 'Edward', 'Joseph', 'Payton', 'Clarence', 'Devin', 'Carlos', 'Austin', 'David', 'Grace', 'Micah', 'Esqueily']
i = 0
seatNumber = 1
while i <= len(students):
    if i < len(students):
        print(f'{students[i]} is in seat #{seatNumber}')
    elif i == len(students):
        exit()
    i += 1
    seatNumber += 1
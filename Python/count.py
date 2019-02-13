import time
count = 1
print(f'{count} is my favorite number.')
count += 1
while count >= 2 and count <= 13:
    print(f'{count} is my new favorite number.')
    time.sleep(.25)
    count += 1
count -= 1 
print(f'Okay, {count} is my actual favorite number.')
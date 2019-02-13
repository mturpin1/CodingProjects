levitation_force = 0
print(f'''Your levitation force is at {levitation_force}\n''')
while levitation_force <= 10:
    if levitation_force >= 0 and levitation_force < 10:
        spell = input('''What spell would you like to cast? ''')
        if spell == str('wingardium leviosa'):
            levitation_force += 1
            print(f'''\nYour levitation force is at {levitation_force}\n''')
        elif spell.lower != 'wingardium leviosa':
            print('\nYou need to practice your spell-casting!')
            levitation_force -= 1
            print(f'Your levitation force is at {levitation_force}\n')
    elif levitation_force == 10:
        print('The feather is now floating!')
        break
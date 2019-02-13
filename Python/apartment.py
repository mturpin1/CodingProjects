apartments={
    'A': {
        '101': ['Adalyn','Liberty'],
        '102': ['Skye','Aspen'],
        '103': ['Matthias','Russo'],
        '104': ['Julianne','Wesley']
    },
    'B': {
        '101': ['Davis','Haley'],
        '102': ['Maeve','Haven'],
        '103': ['Jamar','Makenzie'],
        '104': ['Jayce','Santino']
    },
    'C': {
        '101': ['Emmy','Makena'],
        '102': ['Rolando','Keyleigh'],
        '103': ['Amina','Aaden'],
        '104': ['Rishi','Dale']
    },
    'D':{
        '101': ['Hadley','Griffin '],
        '102': ['Nelson ','Kole '],
        '103': ['Kaeden ','Evelin '],
        '104': ['Helen ','Belinda ']
    }
}

bldg = input('What building? ').upper().strip()
unit = input('What unit? ').strip()
print(f'The residents in Building {bldg} Unit {unit} are {apartments[bldg][unit][0]} and {apartments[bldg][unit][1]}')

nfl = {
    'NFC': {
        'North': ['Bears', 'Packers', 'Vikings', 'Lions'],
        'South': ['Saints', 'Panthers', 'Buccaneers', 'Falcons'],
        'East': ['Redskins', 'Cowboys', 'Eag;es', 'Giants'],
        'West': ['Rams', 'Seahawks', 'Cardinals', '49ers']
    },
    'AFC': {
      'North': ['Bengals', 'Ravens', 'Steelers', 'Browns'],
        'South': ['Titans', 'Texans', 'Jaguars', 'Colts'],
        'East': ['Patriots', 'Dolphins', 'Jets', 'Bills'],
        'West': ['Chiefs', 'Chargers', 'Broncos', 'Raiders']
    }
}
con = input('In which conference are you searching? ').upper().strip()
div = input('What division are you searching for? ').capitalize().strip()
print(f'The teams in the {con} Conference, {div} division are {nfl[con][div][0]}, {nfl[con][div][1]}, {nfl[con][div][2]}, and {nfl[con][div][3]}')
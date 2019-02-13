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
con = input('Pick a conference: ')
div = input('Pick a division: ')
for conference in nfl:
    if conference == con:
        print(conference.keys())
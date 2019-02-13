weather = {
    'usa': {
        'new york city': {
            'high': 57,
            'low': 45,
            'humidity': '51%',
            'rain chance': '0%'
        },
        'new orleans': {
            'high': 83,
            'low': 70,
            'humidity': '63%',
            'rain chance': '0%'
        },
        'san francisco': {
            'high': 71,
            'low': 54,
            'humidity': '64%',
            'rain chance': '0%'
        },
        'seattle': {
            'high': 54,
            'low': 49,
            'humidity': '82%',
            'rain chance': '77%'
        },
        'atlanta': {
            'high': 71,
            'low': 50,
            'humidity': '45%',
            'rain chance': '3%'
        },
    },
    'uk': {
        'london': {
            'high': 49,
            'low': 34,
            'humidity': '73%',
            'rain chance': '7%'
        },
        'stirling': {
            'high': 47,
            'low': 33,
            'humidity': '82%',
            'rain chance': '23%'
        },
        'manchester': {
            'high': 48,
            'low': 34,
            'humidity': '73%',
            'rain chance': '0%'
        },
        'belfast': {
            'high': 49,
            'low': 36,
            'humidity': '66%',
            'rain chance': '24%'
        },
        'newcastle': {
            'high': 45,
            'low': 33,
            'humidity': '86%',
            'rain chance': '14%'
        }
    },
    'italy': {
        'rome': {
            'high': 67,
            'low': 50,
            'humidity': '59%',
            'rain chance': '99%'
        },
        'milan': {
            'high': 57,
            'low': 54,
            'humidity': '77%',
            'rain chance': '53%'
        },
        'naples': {
            'high': 87,
            'low': 68,
            'humidity': '65%',
            'rain chance': '4%'
        },
        'turin': {
            'high': 50,
            'low': 45,
            'humidity': '94%',
            'rain chance': '71%'
        },
        'palermo': {
            'high': 68,
            'low': 64,
            'humidity': '83%',
            'rain chance': '62%'
        }
    }
}
country = input('What country would you like the weather for? (\'usa\', \'uk\', or \'italy\'): ')
measure = input('What measure of the weather would you like for that country? (\'high\', \'low\', \'humidity\', or \'rain\'): ')
city = 0
for city in weather[country]:
    if measure == 'humidity' or measure == 'rain':
        print(f'The {measure} today in {weather[country][city]} is {weather[country][city][measure]} chance.')
    elif measure == 'high' or measure == 'low':
        print(f'The {measure} today in {weather[country][city]} is {weather[country][city][measure]} degrees Fahrenheit.')
    city += 1
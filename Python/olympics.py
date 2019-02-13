olympics = {
    'rome': '1960',
    'tokyo': '1964',
    'mexico': '1968',
    'munich': '1972',
    'montreal': '1976',
    'moscow': '1980',
    'los angeles': '1984',
    'seoul': '1988',
    'barcelona': '1992',
    'atlanta': '1996',
    'sydney': '2000',
    'athens': '2004',
    'beijing': '2008',
    'london': '2012',
    'rio': '2016',
    'future tokyo': '2020',
    'future paris': '2024',
    'future los angeles': '2028'
}
for city_year in olympics:
    if int(olympics[city_year]) < 2018:
        print(f'The {city_year.title()} Olympics were held in {olympics[city_year]}.')
    elif int(olympics[city_year]) >= 2018:    
        print(f'The {city_year.title()} Olympics will be held in {olympics[city_year]}.')
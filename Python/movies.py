movies = {
   'comedy': {
       'romantic': ['Crazy, Stupid, Love', 'Clueless', 'Bridget Jone\'s Diary', 'Notting Hill', 'Your Sister\' Sister'],
       'sitcom': ['An L.A. Minute', 'Action Point', 'Show Dogs', 'Nobody\'s Fool', 'Overboard'],
       'goofy': ['Swiss Army Man', 'Goon', 'Enough Said', 'Beautiful Girls', 'Bernie']
   },
   'horror': {
       'real life': ['Psycho', 'The Exorcist', 'The Hills Have Eyes', 'The Entity', 'The Amityville Horror'],
       'supernatural': ['The Ring', 'The Conjuring', 'The Grudge', 'Insidious', 'Dark Skies'],
       'thriller': ['It Follows', 'Sinister', 'Get Out', 'Saw', 'It']
   },
   'action': {
       'fantasy': ['The Lord of the Rings', 'The Avengers', 'The Dark Knight', 'Star Wars', 'Pirates of the Carribean'],
       'adventure': ['Indiana Jones', 'Iron Man(Original)', 'Jurassic Park', 'The Matrix', 'Avengers: Infinity War'],
       'crime': ['Heat', 'Hostage', 'Taken', 'Hitman', 'Baby Driver']
   }
}
print(', '.join(movies.keys()))
category = input('Please choose a major category from the list above:   ').lower().strip()
print(', '.join(movies[category]))
subCategory = input('Please choose a sub-category from the list above:   ').lower().strip()
print(f'''You should try one of the 5 following movies:
-{movies[category][subCategory][0]}
-{movies[category][subCategory][1]}
-{movies[category][subCategory][2]}
-{movies[category][subCategory][3]}
-{movies[category][subCategory][4]}''')

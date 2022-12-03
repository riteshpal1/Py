movies = ['Dhol','Bahubali','Jab tak hai jaan','PK']
stars  = ['🌟🌟🌟🌟','🌟🌟🌟🌟🌟','🌟','🌟🌟🌟🌟🌟']

for movies, star in zip(movies, stars):
  print(f'{movies:<16} {star}')

my_bands = ['satellite lost', 'deep pockets', 'make it plain', 'bearchild', 'lux courageous', 'gracer', 'janthina', 'sidefires', 'circle the sun']
print(my_bands)
print(sorted(my_bands))
print(my_bands)
print(len(my_bands))
message ='How many bands have you been in?'
print(f'{message}')
print(len(my_bands))
message = 'Which one was your favorite?'
print(message)
print(f'My most favorite band to play in was {my_bands[5].title()}.')
message = 'What was your least favorite band to play in?'
print(message)
print(f'My least favorite band to play in was {my_bands[4].title()}.')
my_bands.sort()
print(my_bands)
my_bands.reverse()
print(my_bands)
my_bands.sort()
print(my_bands)
shortest_band = my_bands.pop(1)
print(shortest_band.title())
longest_band = my_bands.pop(1)
print(longest_band.title())
print(my_bands)
print(f'This is my newest band: \n\t{my_bands[2].title()}')


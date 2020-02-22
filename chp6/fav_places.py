# Make a dictionary called fav_places.
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person
# Loop through the dictionary, and print each person's name and their favorite place.

fav_places = {
	'ryan b': ['long island', 'la'], 
	'justin w': ['seattle','new york'],
	'conor h': ['new york']
	}

fav_places['ryan b'] = 'long island', 'lousiville'

for person, places in fav_places.items():
	if len(places) == 1:
		print(f"\n{person.title()} your favorite place is:")
	else:
		print(f"\n{person.title()} your favorite places are:")

	for place in places:
		print(f"\t{place.title()}")
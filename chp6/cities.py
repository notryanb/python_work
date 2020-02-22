# Make a dictionary called cities.
# Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and on fact about that city.
# The keys for each city's dictionary should be something like country, pop, and fact.
# Print the name of each city and all of the information you have stored about it.

cities = {
	'new york': {
		'country': 'united states',
		'population': '8.5 million',
		'fact': 'if you can make it in New York, you can make it anywhere'
		},

	'london': {
		'country': 'england',
		'population': '8.9 million',
		'fact': 'London has 170 museums'
		},

	'dubai': {
		'country': 'india',
		'population': '3.3 million',
		'fact': 'Arabic is the official language'
		}
	}

for city, city_info in cities.items():
	print(f"\n{city.title()}")
	country = f"{city_info['country']}"
	population = f"{city_info['population']}"
	fact = f"{city_info['fact']}"

	print(f"Country: {country.title()}")
	print(f"Population: {population.title()}")
	print(f"Fact: {fact}.")






# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such as Santiago, Chile.
# Store the function in a module called city_functions.py
# Modify function so it requires a third parameter, population.

def city_country(city, country, population=''):
	"""Neatly formats a city, country string"""
	if population:
		city_and_country = f"{city}, {country} {population}"
	else:
		city_and_country = f"{city}, {country}"
	return city_and_country.title()




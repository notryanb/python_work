# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such as Santiago, Chile.
# Store the function in a module called city_functions.py

def city_country(city, country):
	"""Neatly formats a city, country string"""
	city_and_country = f"{city}, {country}"
	return city_and_country.title()




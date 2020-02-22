# Write a function called city_country() that takes in the name of a city and country.
# The function should retrun a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city_name, country_name):
	if country_name == 'usa':
		city_and_country = f"{city_name.title()}, {country_name.upper()}"
	else:
		city_and_country = f"{city_name.title()}, {country_name.title()}"
	return city_and_country

city_coun = city_country('new york', 'usa')
print(city_coun)

city_coun = city_country('moscow', 'russia')
print(f'\n{city_coun}')

city_coun = city_country('san jose', 'costa rica')
print(f'\n{city_coun}')
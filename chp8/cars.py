# Write a function that stores infomration about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature.
# Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
# Print the dictionary that's returned to make sure all the information was stored corectly

def make_car(make, model, color, **car_options):
	"""Build dictionary for car"""
	car_options['car_make'] = make
	car_options['car_model'] = model
	car_options['car_color'] = color
	return car_options

car_made = make_car('toyota', 'RAV4', 'gold', power_steering=True)
print(car_made)
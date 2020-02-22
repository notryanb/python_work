# Write a function that accepts a list of items a person wants on a sandwhich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwhich that's being ordered.
# Call the function three times, using a different number of agruments each time.

def sandwhich(*sandwhich_toppings):
	"""Accepts list ot toppings a person wants on a sandwhich and prints summary"""
	print(f"\nHere is a summary of the sandwhich you are ordering:")
	for topping in sandwhich_toppings:
		print(f"{topping.title()}")

sandwhich('jalepenos', 'olives', 'roasted red peppers')

sandwhich('sprouts', 'tomato','cucumber')

sandwhich('green peppers', 'avocado', 'radish')


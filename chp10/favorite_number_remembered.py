# Write a program that prompts for the user's favorite number.
# Use json.dump() to store this number in a file.
# Write a separate program that reads in this value and prints the message,
# "I know your favorite number it's _____"

import json

filename = 'fav_number_2.json'
try:
	with open(filename) as f:
		fav_number = json.load(f)
except FileNotFoundError:
	fav_number = input("What's your favorite number?")
	with open(filename, 'w') as f:
		json.dump(fav_number, f)
		print(f"Your favorite number is {fav_number}")
else:
	print(f"I already know your favorite number it's {fav_number}")



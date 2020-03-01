# Write a program that prompts for the user's favorite number.
# Use json.dump() to store this number in a file.
# Write a separate program that reads in this value and prints the message,
# "I know your favorite number it's _____"

import json

fav_number = input("What's your favorite number?")

filename = 'fav_number.json'
with open(filename, 'w') as f:
	json.dump(fav_number, f)
	print(f"I know your favorite number it's {fav_number}")

	

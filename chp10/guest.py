# Write a program that prompts the user for their name.
filename = 'guest.txt'

name = input("What is your name?")

# When they respond, write their name to a file called guest.txt
with open(filename, 'w') as file_object:
	file_object.write(f"{name}")
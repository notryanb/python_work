# Write a loop that prompts the users for their name.
# When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt
# Make sure each entry appears on a new line in the file.
filename = 'guest_book.txt'

while True:
	prompt = "What is your name?"
	prompt += "(enter 'quit' when finished)"
	message = input(prompt)

	if message == 'quit':
		break
	else:
		print(f"Welcome {message}")

	with open(filename, 'a') as file_object:
		file_object.write(f"\n{message}")
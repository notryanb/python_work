# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file that stores all the responses.

filename = 'programming_poll.txt'


with open(filename, 'a') as file_object:
	while True:
		prompt = "Why do you like programming?"
		prompt += "(enter 'quit' when done)"
		message = input(prompt)

		if message == 'quit':
			break

		file_object.write(f"\n{message}")
	
	




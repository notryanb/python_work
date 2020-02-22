# Write a program that prompts for two numbers.
# Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.

print("Give me two number to add together:")
print("(enter 'q' to quit)")


def convert_to_number(user_input):
	"""This converts a value to number or will throw exception if not a number"""
	try:
		return int(user_input)
	except ValueError:
		return float(user_input)

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	try:
		answer = convert_to_number(first_number) + convert_to_number(second_number)
	except ValueError:
		print("Please enter a number!!!")
	else:
		print('{0:.2f}'.format(answer))
		print(answer)


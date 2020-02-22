# Write a function called make_shirt() that accepts a size and the text
# of a message that should be printed on a shirt.
# The function should print a sentence summarizing the size of the shirt
# and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt(shirt_size, shirt_text):
	"""Defines shirt size and text"""
	print(f"Your shirt is a {shirt_size} size, and has the text {shirt_text} printed on it!")

make_shirt('medium', 'FTP')
make_shirt(shirt_text = 'FTP', shirt_size = 'medium')

# Modify the make_shirt() function so that shirts are large by default 
# with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.

def make_shirt(shirt_size = 'large', shirt_text = 'I love Python'):
	"""Defines shirt size and text"""
	print(f"Your shirt is a {shirt_size} size, and has the text {shirt_text} printed on it!")

make_shirt()
make_shirt('medium')
make_shirt('small', 'FTP')
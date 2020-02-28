# Make two files, cats.txt and dogs.txt. 
# Store at least three names of cats in the first file and three names of dogs in the second file.
# Write a program that tries to read these files and print the contents of the file to the screen.

def read_print_filename(filename):
	"""Reads and prints filename, displays a message if not found"""
	try:
		with open(filename, encoding='utf 8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist")
	else:
		print(contents)

filename = ['cats.txt','dogs.txt']
for file in filename:
	read_print_filename(file)

# Wrap your code in a try-except block to catch the FileNotFoundError,
# and print a friendly message if a file is missing.
# Move one of the files to a different location on your system,
# and make sure the code in the except block executes properly.
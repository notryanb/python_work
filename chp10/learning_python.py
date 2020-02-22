# Write a program that reads the file and prints what you wrote three times.

filename = 'learning_python.txt'

# Print the contents once by reading in the entire file,
with open(filename) as file_object:
	contents = file_object.read()

print(contents)

# once by looping over the file object,

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())

# and once by storing the lines in a list and then working with them outside the with block.

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
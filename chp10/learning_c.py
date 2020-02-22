# Read in each line from learning_python.txt and replace the word Python with the name of another language, such as C.
# Print each modified line to the screen.

filename = 'learning_python.txt'


with open(filename) as file_object:
	for line in file_object:
		line = line.replace("Python", "C")
		print(line.strip())


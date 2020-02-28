# Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you'd like to analyze.
# Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase appears in a string.
# Write a program that reads the files you found at Project Futenberg and determines how many times the word 'the' appears in each text.

def count_string(filename, phrase):
	"""This method counts how many times a string appears in a text file"""
	try:
		with open(filename, encoding='utf 8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"{filename} not found, please search for another!")
	else:
	# Count the approximate number of this word in a file
		words = contents.split()
		num_phrase = words.count(f"{phrase}")
		print(f"The file {filename} has about {num_phrase} instances of '{phrase}' in its text!")



filename = ['call_of_the_wild.txt', 'beowolf.txt', 'dracula.txt', 'tintin.txt']
for file in filename:
	count_string(file,'their')

# This will be an approximation because it will also count words such as 'then' and 'there'.
# Try counting 'the', with a space in the string, and see how much lower your count is.
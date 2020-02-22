# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confustion, let's call it a glossary.
# Think of five programming words you've learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning,
# or print the word on one line and then print its meaning indented on a second line.
# Use the newline character [\n] to insert a blank line between each word-meaning pair in your output

# python_glossary = {
# 	'list': 'a group of items',
# 	'range': 'values signfying the begining and end of a series',
# 	'dictionary': 'a series of key-value pairs',
# 	'f-string': 'a method to format print statements into a continous string',
# 	'for loop': 'a method to loop through a series of data while applying the same procedure'
# 	}

# print(f"List:\n{python_glossary['list']}")
# print(f"\nRange:\n{python_glossary['range']}")
# print(f"\nDictionary:\n{python_glossary['dictionary']}")
# print(f"\nF-string:\n{python_glossary['f-string']}")
# print(f"\nFor loop:\n{python_glossary['for loop']}")

# Now that you know how to loop through a di ctionay, clean up  the code from Exercise 6.3
# Replace the series of print() calls with a loop that runs through the dictionary's keys and values.
# When you're sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meaning shsould automatically be included in the output. 

python_glossary = {
	'list': 'a group of items',
	'range': 'values signfying the begining and end of a series',
	'dictionary': 'a series of key-value pairs',
	'f-string': 'a method to format print statements into a continous string',
	'for loop': 'a method to loop through a series of data while applying the same procedure',
	'set': 'a collection in which each item must be unique',
	'keys': 'a method that returns a list of all the keys',
	'get': 'a method that sets a default value to be returned if the key does not exist',
	'if statement': 'conditional test to provide an action if conditions are met',
	'if-else statement': 'conditional test where an action is taken if one condition is met, and a different action in all others',
	'if-elif-else statement': 'multiple conditional test are run until one passes. When a test passes, the coee following that test is executed'
	}

no_line = {'list'}

for term, definition in python_glossary.items():

	if term in no_line:
		print(f"{term.title()}: \n{definition}.")
	else:
		print(f"\n{term.title()}: \n{definition}.")
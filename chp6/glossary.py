# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confustion, let's call it a glossary.
# Think of five programming words you've learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning,
# or print the word on one line and then print its meaning indented on a second line.
# Use the newline character [\n] to insert a blank line between each word-meaning pair in your output

python_glossary = {
	'list': 'a group of items',
	'range': 'values signfying the begining and end of a series',
	'dictionary': 'a series of key-value pairs',
	'f-string': 'a method to format print statements into a continous string',
	'for loop': 'a method to loop through a series of data while applying the same procedure'
	}

print(f"List:\n{python_glossary['list']}")
print(f"\nRange:\n{python_glossary['range']}")
print(f"\nDictionary:\n{python_glossary['dictionary']}")
print(f"\nF-string:\n{python_glossary['f-string']}")
print(f"\nFor loop:\n{python_glossary['for loop']}")
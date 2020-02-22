# Use the code in fav_languages.py
# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll.
# If they have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.

fav_lang = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'ryan': 'rust'
	}

poll = {'jen', 'justin', 'edward', 'ryan', 'lou'}

for name in poll:
	if name in fav_lang.keys():
		print(f"{name.title()}, thanks for responding!")

	if name not in fav_lang.keys():
		print(f"{name.title()}, please take our poll by clicking on the link below!")


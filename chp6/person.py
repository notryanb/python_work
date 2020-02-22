# Use a dictionary to store infomration about a person you know
# Store their first name, last name, age and the city in which they live.
# You should have keys such as first_name, last_name, age and city.
# Print each piece of information stored in your dictionary.

person_0 = {
	'first_name': 'justin',
	'last_name': 'williams',
	'age': '38',
	'city': 'brooklyn',
	}

# Make two new dictionaries representing different people,
# and store all three dictionaries in a list called people.

person_1 = {
	'first_name': 'ryan',
	'last_name': 'blecher',
	'age': 'unknown',
	'city': 'huntington station'
	}

person_2 = {
	'first_name': 'conor',
	'last_name': 'hickey',
	'age': '38',
	'city': 'woodside',
	}

people = [person_0, person_1, person_2]

# Loop through your list of people.

for person in people:

# As you loop through the list, print everything you know about each person.

	full_name = f"{person['first_name']} {person['last_name']}"
	print(f"\nName: {full_name.title()}")
	print(f"Age: {person['age'].title()}")
	print(f"City: {person['city'].title()}")
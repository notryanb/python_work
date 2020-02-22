# Use a dictionary to store people's favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person's name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

# fav_num = {
# 	'ryan': 16,
# 	'joe': 4,
# 	'tia': 3,
# 	'lou': 666,
# 	'justin': 19
# }

# print(f"Ryan's favorite number is {fav_num['ryan']}!")
# print(f"\nJoe's favorite number is {fav_num['joe']}!")
# print(f"\nTia's favorite number is {fav_num['tia']}!")
# print(f"\nLou's favorite number is {fav_num['lou']}!")
# print(f"\nJustin's favorite number is {fav_num['justin']}!")

# Modify the above program so each person can have more than one favorite number.
# Print each person's name along with their favorite numbers.

fav_num = {
	'ryan': [16, 44],
	'joe': [4, 18],
	'tia': [3,12],
	'lou': [666],
	'justin': [19, 4]
}

for name, numbers in fav_num.items():
	if len(numbers) == 1:
		print(f"\n{name.title()}'s favorite number is:")
	else:
		print(f"\n{name.title()}'s favorite numbers are:")

	for number in numbers:
		print(f"\t{number}")


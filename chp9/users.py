# Make a class call Users.

class Users:
	"""A way to record user profiles"""

# Create two attributes called first_name and last_name,
# and then several other attributes that are typically stored in a user profile.
	def __init__(self, first_name, last_name, age, sex, fav_instrument):
		"""Intialize attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.fav_instrument = fav_instrument

# Make a method called describe_user() that prints a summary of the user's information.

	def describe_user(self):
		"""Prints a summary of the user's info"""
		print(f"\nHere is a summary the user's info:")
		print(f"First name: {self.first_name.title()} \nLast Name: {self.last_name.title()} \nAge: {self.age} \
			\nSex: {self.sex} \nFavorite instrument: {self.fav_instrument}")


# Make another method call greet_user() that prints a personalized greeting to the user.
	def greet_user(self):
		"""Prints a personalized greeting to the user"""
		full_name = f"{self.first_name} {self.last_name}"
		print(f"\nHello {full_name.title()}, welcome to the group!!!")

# Create several instances representing different users, 

user_1 = Users('justin', 'williams', 38, 'male', 'piano')
user_2 = Users('ryan', 'blecher', 35, 'male', 'drums')

# and call both methods for each user.
user_1.greet_user()
user_1.describe_user()
user_2.greet_user()
user_2.describe_user()
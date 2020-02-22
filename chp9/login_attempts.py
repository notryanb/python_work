# Make a class call Users.

class Users:
	"""A way to record user profiles"""

# Create two attributes called first_name and last_name,
# Add an attribute called login_attempts.
	def __init__(self, first_name, last_name, login_attempts):
		"""Intialize attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = login_attempts

	def login_status(self):
		"""Prints current login attempts"""
		full_name = f"{self.first_name} {self.last_name}"
		print(f"{full_name.title()} has {self.login_attempts} login attempts.")

# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
	def increment_login_attempts(self):
		"""This will increment login in attempts by 1"""
		self.login_attempts += 1

# Wrtie a method called reset_login_attempts() that resets the value of login_attempts to 0.
	def reset_login_attempts(self):
		"""This will reset login_attempts to zero"""
		self.login_attempts = 0
		print(f"{self.first_name.title()} {self.last_name.title()}'s login attempts have been reset to zero.")

# Create several instances representing different users, 
user_1 = Users('justin', 'williams', 25)
user_2 = Users('ryan', 'blecher', 11)

# Call increment_login_attempts() several times.
user_1.login_status()
user_1.increment_login_attempts()
user_1.login_status()
user_1.reset_login_attempts()
user_1.login_status()
user_2.login_status()
user_2.increment_login_attempts()
user_2.login_status()
user_2.increment_login_attempts()
user_2.login_status()
user_2.reset_login_attempts()
user_2.login_status()





# Print the value of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

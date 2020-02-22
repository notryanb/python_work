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

# Write a class called Admin that inherits from the Users class.
class Admin(Users):
	"""Inheirits from attributes from Users and gives Admin privilages"""
	def __init__(self, first_name, last_name, login_attempts):
		"""Initializes the aforementioned attributes"""
		super().__init__(first_name, last_name, login_attempts)
		self.privileges = ["can add post", "can delete post", "can ban user"]

# Write a method called show_privilages() that lists the administrator's set of privileges	
	def show_privleges(self):
		"""Lists the administrator's set of privileges"""
		print(f"Here is a list of the administrator's privileges: ")
		for privlege in self.privileges:
			print(f"\t{privlege}")

# Create an instance of Admin and call you method. 
my_admin = Admin('justin', 'williams', 11)
my_admin.increment_login_attempts()
my_admin.login_status()
my_admin.show_privleges()
# Make a class called Restaurant.

class Restaurant:
	"""A class that names a restaurant and identifies its food type"""

# The __init__() method for Restuarant should store two attributes: a restaurant_name and a cuisine_type.

	def __init__(self, restaurant_name, cuisine_type):
		"""Initalize and name and age attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

# Make a method called describe_restaurant() that prints these two pieces of information, 

	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} serves an ecceltic assortment of {self.cuisine_type} food.")

# and a method called open_restaurant() that prints a message indicating that the restaurant is open.

	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is now open!!!")

# Make an instance called restaurant from your class.

res_des = Restaurant('champs', 'vegan')

# Print the two attributes individually, and then call both methods.
print(f"{res_des.restaurant_name.title()}")
print(f"{res_des.cuisine_type}")
res_des.describe_restaurant()
res_des.open_restaurant()











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

# Write a class called IceCreamStand that inherits from the Restaurant class.
# Add an attribute called flavors that stores a list of ice cream flavors.
class IceCreamStand(Restaurant):
	"""Represents aspects of an ice cream stand."""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize aspects of the parent class.
		Then initialize attributes specific to ice cream stands."""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'strawberry', 'vanilla']

# Write a method that displays these flavors.
	def flavor_list(self):
		"""This lists the ice cream flavors available"""
		print(f"{self.restaurant_name.title()} has the following flavors: ")
		for flavor in self.flavors:
			print(f"\t{flavor.title()}")

# Create an instance of IceCreamStand, and call this method. 
# res_des = IceCreamStand('van leeuwen', 'vegan ice cream')
# res_des.open_restaurant()
# res_des.describe_restaurant()
# res_des.flavor_list()














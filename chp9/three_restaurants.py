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

# Create three different instances from the class.

res_des_1 = Restaurant('champs', 'vegan')
res_des_2 = Restaurant('selmat pagi', 'indonesian')
res_des_3 = Restaurant('little dokebi', 'korean')

# Call describe_restaurant from each instance.

res_des_1.describe_restaurant()
res_des_2.describe_restaurant()
res_des_3.describe_restaurant()












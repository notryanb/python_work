# Make a class called Restaurant.

class Restaurant:
	"""A class that names a restaurant and identifies its food type"""
# The __init__() method for Restuarant should store two attributes: a restaurant_name and a cuisine_type.
# Add an attribute called number_served with a default value of 0.

	def __init__(self, restaurant_name, cuisine_type):
		"""Initalize and name and age attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

# Make a method called describe_restaurant() that prints these two pieces of information, 
	def describe_restaurant(self):
		print(f"{self.restaurant_name.title()} serves an ecceltic assortment of {self.cuisine_type} food.")

# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is now open!!!")

	def cust_count(self):
		"""This method counts how many customers have been served"""
		print(f"{self.restaurant_name.title()} has served {self.number_served} customers!")

# Add a method called set_number_served() that lets you set the number of customers that have been served.
	def set_number_served(self, customers):
		"""This method displays customer's served"""
		self.number_served = customers
		
# Add a method called increment_number_served() that lets you increment the number of customers who've been served.
	def increment_number_served(self, customers):
		"""This allows for continous counting of customers"""
		self.number_served += customers

# Create an instance of restaurant from this class.
restaurant = Restaurant('champs', 'vegan')

# Print the number of customers the restaurant has served, and then change this value and print it again.
restaurant.set_number_served(100)
restaurant.cust_count()

restaurant.increment_number_served(45)
restaurant.cust_count()














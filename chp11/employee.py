# Write a class called Employee.
# The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attirbutes.
# Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.

class Employee:
	"""Calculates salary raise"""

	def __init__(self, first_name, last_name, annual_salary):
		"""Stores name and salary information"""
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, default_raise=5000):
		"""Adds $5,000 as raise by default, but also allows the entry of custom amount"""
		question = input("Please enter raise amount: ")
		if question == 5000:
			new_salary = default_raise + annual_salary
			print(f"New salary is ${new_salary}")
		else:
			new_salary = question + annual_salary
			print(f"New salary is ${new_salary}")


			




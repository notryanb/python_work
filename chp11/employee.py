# Write a class called Employee.
# The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes.
# Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.

class Employee:
	"""Calculates salary raise"""

	def __init__(self, first, last, salary):
		"""Stores name and salary information"""
		self.first = first
		self.last = last
		self.salary = salary

	def format_name_salary(self):
		"""Neatly formats full name and salary"""
		full_name_salary = f"{self.first} {self.last} {self.salary}"
		return full_name_salary.title()

	def give_raise(self, raise_amount = 5000):
		"""Adds $5,000 as raise to salary by default, or allows the entry of custom raise amount"""

		# This method should only have the responsibility of adding the employee's salary to the raise argument
		# No printing of data should be done here. The format_name_salary_method already can print the salary
		# NOTE: Can't use "raise" as a parameter name because it is a Python keywword for throwing an exception.
		self.salary += int(raise_amount)
	
# The following code needs to be commented our for the test to "work". 
# This is a good indication the following code could be a separate file. Typically
# Each class will have its own file and you main program logic will "live" away from it.

# my_employee = Employee('Justin', 'Williams', 80000)
# print(my_employee.format_name_salary())
# input_raise = input("Please enter a raise amount: ")
# my_employee.give_raise(input_raise)




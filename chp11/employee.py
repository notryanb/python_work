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

	def give_raise(self, raise_=5000):
		"""Adds $5,000 as raise to salary by default, or allows the entry of custom raise amount"""
		new_salary = self.salary + int(raise_)
		print(f"Your new salary is now {new_salary}")		

# my_employee = Employee('Justin', 'Williams', 80000)
# print(my_employee.format_name_salary())
# input_raise = input("Please enter a raise amount: ")
# my_employee.give_raise(input_raise)




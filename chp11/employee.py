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
		self.default_raise = 5000

	def format_name_salary(self):
		"""Neatly formats full name and salary"""
		full_name_salary = f"{self.first} {self.last} {self.salary}"
		return full_name_salary.title()

	def give_raise(self, custom_raise):
		"""Adds $5,000 as raise to salary by default, or allows the entry of custom raise amount"""
		if int(custom_raise) > self.default_raise:
			new_salary = self.salary + int(custom_raise)
		else:
			new_salary = self.salary + self.default_raise
		print(f"Your new salary is now {new_salary}")		

my_employee = Employee('Justin', 'Williams', 80000)
print(my_employee.format_name_salary())
input_raise = input("Please enter a raise amount: ")
my_employee.give_raise(input_raise)




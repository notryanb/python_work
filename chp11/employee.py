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
		"""Neatly formats full and salary, prints statement"""
		first_name = input("Please enter your first name:  ")
		last_name = input("Please enter your last name: ")
		annual_salary = input("Please enter your annual salary: ")
		full_name = f"{first_name} {last_name}"
		print(f"{full_name.title()} your annual salary is currently {annual_salary}")

	def give_raise(self, default_raise=5000):
		"""Adds $5,000 as raise to salary by default, or allows the entry of custom raise amount"""
		question = input("Please enter raise amount: ")
		question = int(question)
		if question != 5000:
			new_salary = question + self.salary
			print(f"New salary is ${new_salary}")
		else:
			new_salary = default_raise + self.salary
			print(f"New salary is ${new_salary}")

my_employee = Employee('Justin', 'Williams', 80000)
my_employee.format_name_salary()
my_employee.give_raise()


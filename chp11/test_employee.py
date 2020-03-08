# Write a test case for Employee.
# Write two test methods, test_give_default_raise() and test_give_custom_raise().
# Use the seUp() method so you don't have to create a new employee instance in each test method.
# Run your test case, and make sure both tests pass.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""

	# def setUp():
	# 	"""Create a question and set of responses for all test methods"""
	# 	employee = "Please enter your first name, last name and current salary"
	# 	self.my_employee = Employee(employee)
	# 	self.response = ['justin', 'williams', 80000]

	def test_format_name_salary(self):
		"""Tests if name and salary are formatted corrctly"""

		# Set up the object you want to test, in this case, a new Employee with first name, last name, and salary
		my_employee = Employee('justin', 'williams', 80_000)
		
		# The assertion that the `format_name_salary()` outputs what you expect for the above class
		self.assertEqual(my_employee.format_name_salary(), 'Justin Williams 80000')

	def test_give_default_raise(self):
		"""Tests if default raise works"""

		# Set up the object you want to test, in this case, a new Employee with first name, last name, and salary
		my_employee = Employee('justin', 'williams', 80_000)		
		my_employee.give_raise()
		# The assertion that the `format_name_salary()` outputs what you expect for the above class
		self.assertEqual(my_employee.salary, 85_000)


	def test_give_custom_raise(self):
		"""Tests if entering custom raise works"""

		# Set up the object you want to test, in this case, a new Employee with first name, last name, and salary
		my_employee = Employee('justin', 'williams', 80_000)
		my_employee.give_raise(12345)
		# The assertion that the `format_name_salary()` outputs what you expect for the above class
		self.assertEqual(my_employee.salary, 92_345)

	def test_give_custom_raise_multiple_times(self):
		"""Tests if entering custom raise works"""

		# Set up the object you want to test, in this case, a new Employee with first name, last name, and salary
		my_employee = Employee('justin', 'williams', 80_000)
		my_employee.give_raise()
		my_employee.give_raise(12345)
		my_employee.give_raise(0)
		# The assertion that the `format_name_salary()` outputs what you expect for the above class
		self.assertEqual(my_employee.salary, 97_345)

if __name__ == '__main__':
    unittest.main()

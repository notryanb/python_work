# Write a test case for Employee.
# Write two test methods, test_give_default_raise() and test_give_custom_raise().
# Use the seUp() method so you don't have to create a new employee instance in each test method.
# Run your test case, and make sure both tests pass.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""

	def test_give_custom_raise(self):
		"""Tests if name and salary are formatted corrctly"""
		my_employee = format_name_salary('justin', 'williams', 80000)
		my_employee.format_name_salary()
		self.assertEqual(my_employee, 'Justin Williams 80000')

if __name__ == '__main__':
    unittest.main()

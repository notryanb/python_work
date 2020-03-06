# Write a test case for Employee.
# Write two test methods, test_give_default_raise() and test_give_custom_raise().
# Use the seUp() method so you don't have to create a new employee instance in each test method.
# Run your test case, and make sure both tests pass.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""

	def test_full_name_raise(self):
		"""Test that full name and salary formatted correctly"""
		my_employee = format_name_salary('Justin', 'Williams', 80000)
		self.assertEqual(format_name_salary, 'Justin Williams 80000')

	# def test_give_default_raise():



	# def test_give_custom_raise():
	# 	pass

if __name__ == '__main__':
    unittest.main()

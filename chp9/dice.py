# Make a class Die with one attribute called sides, which has a default value of 6.

# Make a 6-sided die and roll it 10 times.
import random

class Die:
	"""A class describing a Die"""

	def __init__(self, sides):
		"""Initializes sides"""
		self.sides = sides

# Write a method called roll_die() that prints a random number between 1,
# and the number of sides the die has.

	def roll_die(self):
		"""Prints a random number between 1 and the numbrer of sides the die has"""
		print(f"Here is a random number between 1 and {self.sides}: ")
		print(random.randint(1, int(self.sides)))

roll = Die(10)
roll.roll_die()



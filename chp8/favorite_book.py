# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as One of my favorite books is
# Alice in Wonderland. Call the function, making sure to include a book title 
# as an agrument in the function call.

def favorite_book(title):
	"""This passes favorite book info into the function and prints it"""
	print(f"Your favorite book is {title.title()}!")

favorite_book('diet for a new america')
# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.

sandwich_orders = ['tofu sandwich', 'hummus sandwich', 'avocado sandwich', 'chikn sandwich']
finished_sandwiches = []

# Loop through the list of sandwhich orders and print a message for each order,
# such as I made your tuna sandwhich.

while sandwich_orders:
	making_sandwich = sandwich_orders.pop()
	print(f"I made your {making_sandwich}!")

# As each sandwich is made, move it to the list of finished sandwiches.
	finished_sandwiches.append(making_sandwich)

# After all the sandwiches have been made, print a message listing each sandwich that was made.
print(f"Here is a final list of all the sandwiches that were made: ")

for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich.title()}")
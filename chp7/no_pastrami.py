# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Ensure the sandwich 'pastrami' appears three times.
# Then make an empty list called finished_sandwiches.

sandwich_orders = ['pastrami sandwich', 'pastrami sandwich','tofu sandwich', 'hummus sandwich', 'avocado sandwich', 'chikn sandwich', 'pastrami sandwich']
finished_sandwiches = []

# Add code near the begining of the program to print a message saying the deli has run out of pastrami,
# then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.

print("Attention, Attention, the deli has run out of pastrami!!!")

while 'pastrami sandwich' in sandwich_orders:
	sandwich_orders.remove('pastrami sandwich')

# Loop through the list of sandwhich orders and print a message for each order,
# such as I made your tuna sandwhich.

while sandwich_orders:
	making_sandwich = sandwich_orders.pop()
	print(f"\nI made your {making_sandwich}!")

# As each sandwich is made, move it to the list of finished sandwiches.
	finished_sandwiches.append(making_sandwich)

# After all the sandwiches have been made, print a message listing each sandwich that was made.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

print(f"\nHere is a final list of all the sandwiches that were made: ")

for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich.title()}")
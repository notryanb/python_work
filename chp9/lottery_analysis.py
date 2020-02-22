# Make a list or tuple containing a series of 10 numbers and five letters.

import random

ticket_choices = ['a', 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 'b', 'c', 'e', 'f']

winning_ticket = []

# Randomly select four numbers or ltters from the list and print a message
# saying that any ticket matching these four numbers or letters wins a prize.
print(f"Any ticket matching these four number or letters wins a prize!!!")
for x in range(0,4):
	randdom_selection = random.choice(ticket_choices)
	winning_ticket.append(randdom_selection)
	has_winning_ticket = False
	count = 0
print(winning_ticket)

# Make a list or tuple called my_ticket.
while not has_winning_ticket:
	my_ticket = []

# Write a loop that keeps pulling numbers until your ticket wins.
	for x in range(0,4):
		randdom_selection = random.choice(ticket_choices)
		my_ticket.append(randdom_selection)
		has_winning_ticket = my_ticket == winning_ticket
		count += 1

print(f"\nHere is my winning ticket! \n{my_ticket}")

# Print a message reporting how many times the loop had to run to give you a winning ticket.
print(f"\nThis loop had to run {count} times to give you a winning ticket!")
	





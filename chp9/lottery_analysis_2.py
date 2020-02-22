# Make a list or tuple containing a series of 10 numbers and five letters.

import random

rand_list = ['a', 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 'b', 'c', 'e', 'f']

# Randomly select four numbers or ltters from the list and print a message
# saying that any ticket matching these four numbers or letters wins a prize.

print(f"Any ticket matching these four number or letters wins a prize!!!")

for x in range(0,4):
	rand_select = random.choice(rand_list)
	print(rand_select)

# Make a list or tuple called my_ticket.

my_ticket = []

while x in range(0,4):
	winning_ticket = random.choice(rand_list)
	winning_ticket == rand_select
	count +=1
	print(count)





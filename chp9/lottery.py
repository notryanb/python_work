# Make a list or tuple containing a series of 10 numbers and five letters.

import random

rand_list = ['a', 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 'b', 'c', 'e', 'f']

# Randomly select four numbers or ltters from the list and print a message
# saying that any ticket matching these four numbers or letters wins a prize.

print(f"Any ticket matching these four number or letters wins a prize!!!")

rand_select_1 = random.choice(rand_list)
rand_select_2 = random.choice(rand_list)
rand_select_3 = random.choice(rand_list)
rand_select_4 = random.choice(rand_list)

print(f"{rand_select_1}\n{rand_select_2}\n{rand_select_3}\n{rand_select_4}")



# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message saying they'll have to wait for a table.
# Otherwise, report that their table is ready.

question = input("How many people would you like to make this reserveration for? ")
question = int(question)

if question >= 8:
	print("\nYou will have to wait for a bigger table.")
else:
	print("\nYour table is ready!!!")
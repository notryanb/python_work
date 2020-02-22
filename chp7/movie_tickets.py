# A movie theater charges different ticket prices depending ona person's age.
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

question = "\n What is your age?"
question += "\n(when done enter quit)"

while True:
	answer = input(question)
	if answer == 'quit':
		break
	answer = int(input(question))
	if answer < 3:
		print("Your ticket is free!")
	elif answer < 12:
		print("Your ticket is $10!")
	else:
		print("Your ticket is $15!.")


# while True:
# 	answer = int(input(question))
# 	if answer < 3:
# 		print("Your ticket is free!")
# 	elif answer < 12:
# 		print("Your ticket is $10!")
# 	else:
# 		print("Your ticket is $15!.")


# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world,
# where would you go?
# Include a block of code that prints the results of the poll.

dream_vaca = {}

polling_active = True

while polling_active:
	name = input("What is your name?")
	question = input("\nIf you could visit one place in the world, where would you go?")

	dream_vaca[name] = question

	repeat = input("Would anyone else like to respons? (yes/no) ")
	if repeat == 'no':
		polling_active = False

print(f"\nPoll Results:")
for name, question in dream_vaca.items():
	print(f"\n\t{name.title()} would like to goto {question.title()}.")
	


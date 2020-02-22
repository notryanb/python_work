# fizz buzz program
# for every number from 0 to 100
# print fizz if the number is divisable by 3
# print buzz if the numbrer is divisable by 5
# if neither print the number
onehundred = range(0,101)
message = ''
for number in onehundred:
	message += ' '
	if number == 0:
		message += str(number)
	elif number %3 == 0 and number %5 == 0:
		message += 'fizzbuzz'.upper()
	elif number %3 == 0:
		message += 'fizz'.title()
	elif number %5 == 0:
		message += 'buzz'.title()
	else: 
		message += str(number)

print(message)






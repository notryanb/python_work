# ordinal numbers indicate their position in a list, such as 1st or 2nd
# most ordinal numbers end in th, except 1, 2 and 3.
# store the numbers 1 through 9 in a list.
# loop through the list.
# use if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

# ord_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in range(1,10):
	if number == 1:
		print(f'{number}st')
	elif number == 2:
		print(f"\n{number}nd")
	elif number == 3:
		print(f'\n{number}rd')
	else:
		print(f"\n{number}th")

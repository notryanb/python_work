odd_numbers = []
for value in range(0,19,2):
	odd = value +1
	odd_numbers.append(odd)

print(odd_numbers)

odd_numbers = [value +1 for value in range(0,19,2)]
print(odd_numbers)
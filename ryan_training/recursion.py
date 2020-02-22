
# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120

# We want to take any number and multiply it by the next lowest number.

def main():
	result = factorial(5)
	print(str(result))

def factorial(number):
	print("Calling a factorial with:" + str(number))
	if number == 0:
		return 1


#5! = 5 * 4!

	return number * factorial(number - 1)


if __name__ == "__main__":
	main()
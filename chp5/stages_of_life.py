# write and if-elif-else chain that determines a person's stage of life.
# set a value for the variable age, and then:

age = 66

# if the person is less than 2 years old, print a message that the person is a baby.

if age < 2:
	print("You are a baby!!!")

# if the person is at least 2 years old but less thatn 4, print a message that the person is a toddler.

elif age >= 2 and age < 4:
	print("You are a toddler!")

# if the person is at least 4 years old but less than 13, print a message that the person is a kid. 

elif age >= 4 and age < 13:
	print("You are a kid!")

# if the person is at least 13 years old but less than 20, print a message that the person is a teenager.

elif age >= 13 and age < 20:
	print("You are a teen!")

# if the person is at least 20 years old but less than 65, print a message that the person is an adult.

elif age >= 20 and age < 65:
	print("You are and adult!")

# if the person is age 65 or older, print a message that the person is an elder. 

else:
	print("You are an elder.")
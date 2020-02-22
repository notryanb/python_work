# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you'll add that topping to their pizza

prompt = "\nEnter the toppings you would like on your pizza:"
prompt += "\n(enter done when complete)"

topping = ""
while topping != 'done':
	topping = input(prompt)

	if topping != 'done':
		print(f"\nWe will add {topping} to your pizza!")

# Active variable
# active = True
# while active:
# 	topping = input(prompt)

# 	if topping == 'done':
# 		active = False
# 	else:
# 		print(f"We will add the {topping} to your pizza!!!")

# Break Statement
# while True:
# 	topping = input(prompt)

# 	if topping == 'done':
# 		break
# 	else:
# 		print(f"\nGreat, I will add {topping} to your order!")
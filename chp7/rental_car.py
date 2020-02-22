# Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as "Let me see if I can find you a Subaru"

question = "What kind of rental car would you like? "

car = input(question)
print(f"\nLet me see if I can find you a {car.title()}.")
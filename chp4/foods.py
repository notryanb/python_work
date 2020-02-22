my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:\n")
for food in my_foods:
	print(food.title())

print("\nMy friend's favorite foods are:\n")
for food in friend_foods:
	print(food.title())

print(f'\nThe last three items in my list are {my_foods[1:4]}')
print(f'\nThe two items from the middle of my list are {my_foods[1:3]}')
print(f'\nThe frist three items from my list are {my_foods[0:3]}')

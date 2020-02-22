fav_pizza = ['vinnies', 'screamers',"paulie gs", "archies"]
friend_pizza = fav_pizza[:]

fav_pizza.append('three brothers')
friend_pizza.append("mario's")

print("My favorite pizza shops are:")
for pizza_shop in fav_pizza:
	print(pizza_shop.title())

print("\nMy friend's favorite pizza shops are:")
for pizza_shop in friend_pizza:
	print(pizza_shop.title())


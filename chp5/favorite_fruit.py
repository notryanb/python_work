# make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# make a list of your three favorite fruits and call it favortie_fruits
# write five if statements
# each should check whether a cetain kind of fruit is in your list. 
# if the fruit is in your list, the if block should print a statement, such as You really like bananas!


fav_fruits = ['bananas', 'grapefruit', 'oranges']

if 'bananas' in fav_fruits:
	print("You really love bananas!")

if 'grapefruit' in fav_fruits:
	print("You really love grapefruit!!!")

if 'oranges' in fav_fruits:
	print("You must really love oranges!")

if 'oranges' and 'grapefruit' in fav_fruits:
	print("You must really love citrus fruits!")

if 'blueberries' not in fav_fruits:
	print("What happened to the blueberries???")
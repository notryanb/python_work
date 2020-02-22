# Make a separate file that imports that imports Restaurant.

from ice_cream_stand import Restaurant

# Make a Restaurant instance, and call one of Restaurant's methods
# to show that the import statement is working properly.

fav_res = Restaurant('champs', 'vegan')
fav_res.open_restaurant()
fav_res.describe_restaurant()



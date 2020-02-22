# the following 5 conditional tests are to help me understand why each line evalutates to True or False
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

fav_cereal = 'granola'
print("\nIs fav_cereal == 'granola'? I predict True")
print(fav_cereal == 'granola')
print(fav_cereal == 'cornflakes')

fav_band = 'type o negative'
print("\nIs fav_band == 'type o negative'? I predict True")
print(fav_band == 'type o negative')
print(fav_band == 'pearl jam')

fav_brew_method = 'v60 pour over'
print("\nIs my fav_brew_method == 'v60 pour over'? I predict True")
print(fav_brew_method == 'v60 pour over')
print(fav_brew_method == 'drip')

fav_bass = 'pbass'
print("\nIs my fav_bass = 'pbass'? I predict True")
print(fav_bass == 'pbass')
print(fav_bass == 'jbass')

# this next series of exercises will further test my knowledge of conditional tests

# tests for equality and inequality with strings
fav_saying = "Oh, that little guy over their? Don't worry about that little guy over there!"
saying = "Little Pip"
st_quote = "Oh, that little guy over their? Don't worry about that little guy over there!"
print("\nIs 'fav_saying == 'saying', I predict False")
print(fav_saying == saying)
print("\nIs 'fav_saying' == 'st_quote', I predict True")
print(fav_saying == st_quote)

# tests using the lower() method

sean = "I like to write everything in lowercase."
Justin = "I like to write everything in lowercase."
print(f'\n{Justin.lower()}' == f'\n{sean.lower()}')
print(sean == Justin)

# numerical tests involving equality and inequality
first_number = 1
second_number = 2
print(first_number == second_number)
print(first_number != second_number)

# greater than and less than

print("\nIs 'first_number > second_number? I think not!")
print(first_number > second_number)
print("\nIs 'second_number' > 'first_number? I think so!!!")
print(second_number > first_number)

# greater than or equal to
print("\nIs 'second_number' >= 'second_number?, I think so!!!")
print(second_number >= second_number)
print("\nIs 'first_number' >= 'second_number'? I think not!!!")
print(first_number >= second_number)

# less than or equal to
print("\nIs 'first_number' <= 'second_number'? I predict True!!!")
print(first_number <= second_number)

# tests using the and keyword and the or keyword
print("\nIs 'first_number' and 'second_number' == to 3?, I predict True")
print(first_number == 1 and second_number == 2)
print("\nIs 'first_number' and 'second_number' == 2, I predict False")
print(first_number == 2 and second_number == 1)
print("\nIs 'first_number' or 'second_number' == 1?, I predict True")
print(first_number == 1 or second_number == 1)
print("\nIs 'first_number' or 'second_number' == 3?, I predict False")
print(first_number == 3 or second_number ==3)

# test whether an item is in a list
# test whether an item is not in a list
names = ['joey', 'bobby', 'billy', 'harold', 'ricky']
fav_name = 'joey'
least_fav_name = 'karl'

if fav_name in names:
	print(f"\n{fav_name.title()}, is my favorite name")

if least_fav_name in names:
	print(f"{least_fav_name.title()}, is my least favorite name")
else:
	print(f"\nWhere is {least_fav_name.title()}?")




# do the following to create a program that simulates how websites ensure that everyone has a unqiue username.
# make a list of five or more usernames called current_users.
# make another list of five usernames called new_users. 
# make sure one or two of the new usernames are also in the current_users list.
# loop through the new_users list to see if each new username has already been used.
# if it has, print a message that the person will need to enter a new username.
# if a username has not been used, print a message saying that the username is available.
# make sure your comparison is case insenitive. 
# if 'John' has been used, 'JOHN' should not be accepted. 
# (to do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ['Ryan', 'Justin', 'Matt', 'Darren', 'Conor']

new_users = ['Joe', 'Tia', 'ryan', 'Lou', 'justin']

current_users = {user.lower() for user in current_users}
new_users = {user.lower() for user in new_users}

for user in new_users:
	if user in current_users:
		print(f"{user.title()}, you will need to enter a new username!")
	else:
		print(f"{user.title()}, this username is available.")

print("\nThanks for signing up!")

# make a list of five or more usernames, including the name 'admin'.
# imagine you are writing code that will print a greeting to each user after they log in to a website.
# loop through the list, and print a greeting to each user:
# if the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# otherwise, print a generic greeting such as Hello Jaden, thank you for logging in again.

# username = ['admin', 'matt', 'darren', 'conor', 'justin']

# username = []

# for name in username:
# 	if name == 'admin':
# 		print(f'Hey {name.title()}, would you like to see a status report?')
# 	elif name in username:
# 		print(f"Hey {name.title()}, thanks for logging in again!")
# 	else:
		# print("We need some users!!!")

# add an if test to hello_admin.py to make sure the list of users is not empty
# if the list is empty, print the message We need to find some users!
# remove all the usernames from your list, and make sure the correct message is printed.


username = []

if username:
	for name in username:
		if name == 'admin':
			print(f'Hey {name.title()}, would you like to see a status report?')
		elif name in username:
			print(f"Hey {name.title()}, thanks for logging in again!")
else:
	print("We need some users!!!")

# make a list of five or more usernames, including the name 'admin'.
# imagine you are writing code that will print a greeting to each user after they log in to a website.
# loop through the list, and print a greeting to each user:
# if the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# otherwise, print a generic greeting such as Hello Jaden, thank you for logging in again.

username = ['admin', 'matt', 'darren', 'conor', 'justin']

for name in username:
	if name == 'admin':
		print(f'Hey {name.title()}, would you like to see a status report?')
	else:
		print(f"Hey {name.title()}, thanks for logging in again!")

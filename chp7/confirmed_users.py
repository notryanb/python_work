# Start with users that need to be verified,
# and an empty list to hold confirmed users.

uncofirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while uncofirmed_users:
	current_user = uncofirmed_users.pop()

	print(f"Verifying user: {current_user.title()}!")
	confirmed_users.append(current_user)

# Display all confirmed users.

print("\nThe following uysers have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
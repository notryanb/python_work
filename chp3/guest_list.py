guest_list = ['george harrison', 'shannon hoon', 'nate mendel']
message = "\nOn behalf of vegetarians all over the world, you are invited to this cordial meal. \n\tPlease RSVP with your response promptly"
print(f"Dear {guest_list[0].title()}, {message}")
print(f"Dear {guest_list[1].title()}, {message}")
print(f"Dear {guest_list[-1].title()}, {message}")
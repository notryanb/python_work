# Make a list containing a series of short text messages.

text_messages = ["How are you?", "Where have you been?", "Yo, what's up?", "chilling like a villian"]

# Pass the list to a function called show_message(), which prints each text message.

def show_message(message):
	for message in text_messages:
		print(f"\n{message}")

show_message(text_messages)
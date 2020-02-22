# Make a list containing a series of short text messages.

text_messages = ["How are you?", "Where have you been?", "Yo, what's up?", "chilling like a villian"]
sent_messages = []

# Write a funtion called send_messages() that prints each text message and moves each message to a new list called,
# sent_messages as it's printed.

def send_messages(text_messages, sent_messages):
	while text_messages:
		sending_message = text_messages.pop()
		print(f"\nPrinting message: {sending_message}")
		sent_messages.append(sending_message)
	

send_messages(text_messages[:], sent_messages)

# After calling the function, print both of your lists to make sure the messages were moved correctly.

print(text_messages)

print(sent_messages)
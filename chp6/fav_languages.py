fav_lang = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'ryan': 'rust'
	}

# indent = {'jen'}

# indented = {'edward'}

for name, language in fav_lang.items():
	print(f"{name.title()}'s favorite computer language is {language.title()}.")

# for name in fav_lang.keys():

# 	if name in indent:
# 		print(f"\n{name.title()}")

# 	else:
# 		print(name.title())

# if 'ryan' not in fav_lang.keys():
# 	print(f"\nRyan, please take our poll!")

# for name in sorted(fav_lang):

# 	if name in indented:
# 		print(f"\n{name.title()}, thanks for takeing the poll!")

# 	else:
# 		print(f"{name.title()}, thanks for taking the poll!")

# print("\nThe following languages have been mentioned:")
# for language in  set(fav_lang.values()):
# 	print(language.title())


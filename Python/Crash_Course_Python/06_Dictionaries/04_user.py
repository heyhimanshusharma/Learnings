# Looping Through All Key-Value Pairs

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

favourite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
	print(language.title())
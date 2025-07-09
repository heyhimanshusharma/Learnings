# Ask user their name
name = input("WWhat's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split()

# Say Hello to user
print(f"Hello, {first}")
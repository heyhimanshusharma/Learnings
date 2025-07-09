# Ask user their name
name = input("What's your name? ")

# .strip() removes extra white spaces
name = name.strip()
 
# .capitalize capitalizes only the initial letter
name = name.capitalize()

# .title() capitalizes first letter of every word
name = name.title()

# Formatted strings are a way to embed expressions inside string
print(f"hello, {name}")
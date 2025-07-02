age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f'Your admisson fees is ${price}.')

# Using Multiple elif Blocks
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f'Your admisson cost is ${price}.')

# Omitting the else Block
age = 12

if age <4:
	price = 0
elif age <18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

print(f'Your admisson cost is ${price}.')
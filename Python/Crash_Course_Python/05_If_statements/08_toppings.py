requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'pepporoni':
		print(f'Adding {requested_topping}')
	else:
		print(f'Adding {requested_topping}')


print('\nFinished making your pizza')

# Checking That a List Is Not Empty
requested_topping = []

if requested_topping:
	for requested_topping in requested_toppings:
		print(f'Adding {requested_topping}')
	print('\nFinished making your pizza.')
else:
	print('Are you sure you want a plain pizza?')

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepporoni', 'pineapple', 
'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}.')
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print('\nFinished making your pizza.')
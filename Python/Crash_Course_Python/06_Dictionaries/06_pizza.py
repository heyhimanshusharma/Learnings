# store information about pizza being ordered
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese']
}
# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza"
	"with the followinf toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)
prompt = "\nEnter the toppings you would like to have"
prompt += "\nEnter 'quit' to exit. "

active = True

while active:
    message = input(prompt)

    if message != 'quit':
        active = False
    else:
        print(prompt)
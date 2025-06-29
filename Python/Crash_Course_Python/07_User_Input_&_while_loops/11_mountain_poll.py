responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the name's person name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday.")

    # store the responses in dictionary
    responses[name] = [response]

    # find out if anyone else is going to take the poll
    repeat = input("Would you like another person to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n---Poll Results---")

for name, response in responses.item():
    print(f"{name} would you like to climb {response}")
prompt = input("What is your name po? ")

file_name = 'guests.txt'

with open(file_name, 'w') as file_object:
    file_object.write(prompt)

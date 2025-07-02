try:
    with open('cats.txt') as file_object:
        cats= file_object.read()
    print(cats)
    
    with open('dogs.txt') as file_object:
        dogs = file_object.read()
    print(dogs)
except FileNotFoundError:
    print("We could'nt find your dogs. Ahem! your dogs.txt file")

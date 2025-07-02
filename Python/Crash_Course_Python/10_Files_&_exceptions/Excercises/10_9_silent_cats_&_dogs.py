try:
    with open('cats.txt') as file_cats:
        cats = file_cats.read()
    print(cats)

    with open('dogs.txt') as file_dogs:
        dogs = file_dogs.read()
    print(dogs)

except FileNotFoundError:
    pass
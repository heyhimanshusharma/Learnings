class Dog:
    def __init__(self, name, breed, owner): # Init method for Data fields
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self): # Method/func
        print("Woof woof")

class Owner:
    def __init__(self, name, address, contact):
        self.name = name

owner1 = Owner("Himanshu", "Whitefield", "7721088212")
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)

owner2 = Owner("Louisa", "Manila", "8626089")
dog2 = Dog("Tyson", "German Shepherd", owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
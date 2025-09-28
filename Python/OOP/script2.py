class Dog:
    def __init__(self, name, breed): # Init method for Data fields
        self.name = name
        self.breed = breed

    def bark(self): # Method/func
        print("Woof woof")

class Owner:
    def __init__(self, name, address, contact):
        self.name = name
        

dog1 = Dog("Bruce", "Scottish Terrier")
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Tyson", "German Shepherd")
dog2.bark()
print(dog2.name)
print(dog2.breed)
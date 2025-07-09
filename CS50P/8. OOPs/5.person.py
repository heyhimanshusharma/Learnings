class Person:
    name = "Himanshu"
    occupation = "Student"
    networth = 1000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.info()
a = Person()
a.name = "louisa"
a.occupation = "Nurse"
print(a.name, a.occupation)
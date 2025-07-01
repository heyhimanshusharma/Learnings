class User:

    def __init__(self, first_name, last_name, email=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def describe_user(self):
        print(f"User's full name is {self.first_name} {self.last_name}")

    def greer_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

user1 = User('Himanshu', 'Sharma')
user1.describe_user()
user1.greer_user()

user2 = User('Saurabh', 'Aanbhule')
user2.describe_user()
user2.greer_user()
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_atempts = 0
    
    def describe_user(self):
        print(f"User's full name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_atempts += 1
    
    def reset_login_attempts(self):
        self.login_atempts = 0

user1 = User('Himanshu', 'Sharma')
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"login attempts: {user1.login_atempts}")
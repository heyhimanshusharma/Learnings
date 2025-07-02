import json

username = input("Whats your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print("We'll remember you when you come back {username}")

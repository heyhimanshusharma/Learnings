import json

prompt = input("What's your favorite number? ")

filename = 'fav_num.json'
with open(filename, 'w') as file_object:
    json.dump(prompt, file_object)
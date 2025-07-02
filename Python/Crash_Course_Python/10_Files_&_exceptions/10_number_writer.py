import json

filename = 'numbers.json'
with open(filename) as f:
    print(json.load(f))
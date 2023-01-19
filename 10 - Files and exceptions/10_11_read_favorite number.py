import json

with open('number.json', 'r') as file:
    number = json.load(file)

print(number)
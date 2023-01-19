import json

number = input("Enter your favorite number: ")

with open('number.json', 'w') as file:
    json.dump(number, file)
import json

try:
    with open('number.json', 'r') as file:
        num = json.load(file)
        print(num)
except FileNotFoundError:
    num = input("Number not found, enter your favorite number: ")
    print(num)
    with open('number.json', 'w') as file:
        json.dump(num, file)
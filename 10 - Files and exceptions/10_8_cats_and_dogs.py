try:
    with open('cats.txt') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content)

try:
    with open('dogs.txt') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content)
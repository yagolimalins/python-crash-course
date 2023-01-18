try:
    with open('cats.txt') as file:
        content = file.read()
except FileNotFoundError:
    pass
else:
    print(content)

try:
    with open('dogs.txt') as file:
        content = file.read()
except FileNotFoundError:
    pass
else:
    print(content)
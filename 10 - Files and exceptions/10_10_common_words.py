try:
    with open('alice.txt', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content.lower().count('the'))
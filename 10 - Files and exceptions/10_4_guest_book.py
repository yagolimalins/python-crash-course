while True:
    name = input('Enter your name: ')
    with open('guest_book.txt', 'a') as file:
        file.write(name + '\n')
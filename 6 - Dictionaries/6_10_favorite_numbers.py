favorite_numbers = {'yago': [6, 9, 5],
                    'edgar': [8, 2, 6],
                    'eliana': [9, 12, 28],
                    'alicia': [67, 42, 31],
                    'darlan': [90, 80, 70],
                    }

for person, numbers in favorite_numbers.items():
    print("Os números favoritos de " + person.title() + " são:")
    for number in numbers:
        print(number)
    print()
print()

for name in favorite_numbers.keys():
    print(name.title())
print()

for numbers in favorite_numbers.values():
    for number in numbers:
        print(number)
    print()
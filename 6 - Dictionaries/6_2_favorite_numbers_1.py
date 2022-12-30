favorite_numbers = {'yago': 6,
                    'edgar': 3,
                    'eliana': 9,
                    'alicia': 2,
                    'darlan': 8,
                    }

for person, number in favorite_numbers.items():
    print("O número favorito de " + person.title() + " é " + str(number))

for name in favorite_numbers.keys():
    print(name.title())

for value in favorite_numbers.values():
    print(value)
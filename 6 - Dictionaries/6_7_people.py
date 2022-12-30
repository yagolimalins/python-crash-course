person_1 = {'name': 'edgar',
            'last_name': 'azevedo',
            'age': 26,
            'city': 'maceió',
            }
person_2 = {'name': 'yago',
            'last_name': 'lima',
            'age': 29,
            'city': 'maceió',
            }
person_3 = {'name': 'eliana',
            'last_name': 'queiroz',
            'age': 26,
            'city': 'maceió',
            }

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items():
        print(key + ": " + str(value))
    print()
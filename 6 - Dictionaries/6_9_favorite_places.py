favorite_places = {'yago': ['home', 'university', 'stage'],
                   'edgar': ['home', 'estrela de alagoas'],
                   'eliana': ['home', 'university'],
                   }

for person, places in favorite_places.items():
    print(person.title() + ": ")
    for place in places:
        print(place)
    print()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

pool_people = ['yago', 'jen', 'edgar', 'phil']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
    
print()

for person in pool_people:
    if person in favorite_languages.keys():
        print(person.title() + " you already took the pool!")
    elif person not in favorite_languages.keys():
        print(person.title() + " you should take the pool!")
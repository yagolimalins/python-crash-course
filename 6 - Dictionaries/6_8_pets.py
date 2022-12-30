pichuiu = {'kind': 'cat',
           'owner': 'eliana'
           }

pipoquinha = {'kind': 'cat',
              'owner': 'edgar'
              }

luna = {'kind': 'cat',
        'owner': 'maria eduarda'
        }

pets = [pichuiu, pipoquinha, luna]

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + str(value))
    print()
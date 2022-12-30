rivers = {'amazonas': 'brazil',
          'yangtze': 'china',
          'nile': 'egypt',
          }

for river, country in rivers.items():
    print("The " + river.title() + " river runs through " + country.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
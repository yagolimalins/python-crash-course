cities = {'hong kong': {'country': 'China', 'population': '7400000', 'fact': 'was colonized by the british people'},
        'london': {'country': 'England', 'population': '7000000', 'fact': 'the famous Big Ben is located there'},
        'macau': {'country': 'China', 'population': '658000', 'fact': 'was colonized by Portugal'}
        }


for key,value in cities.items():
    print("city: "+ key.title())
    data = value
    for data, content in value.items():
        print(data + ": " + content)
    print()
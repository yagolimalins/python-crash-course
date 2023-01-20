from city_functions import city_country


print("Enter 'q' at any time to quit.")

while True:
    city = input("Plese give me a city name: ")
    if city == 'q':
        break
    country = input('Please give me a country name: ')
    if country == 'q':
        break
    population = input('Please give me city\'s population: ')
    if population == 'q':
        break

    city = city_country(city, country, population)
    print("Formated city and country name: " + city)
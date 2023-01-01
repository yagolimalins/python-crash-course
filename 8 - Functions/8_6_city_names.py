def city_country(city, country):
    formatted_string = city.title() + ', ' + country.title()
    return formatted_string

city = city_country('maceió', 'brazil')
print(city)

city = city_country('são paulo', 'brazil')
print(city)

city = city_country('new york', 'united states of america')
print(city)
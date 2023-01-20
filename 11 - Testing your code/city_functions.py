def city_country(city, country, population=''):
    city_country = city + ', ' + country
    city_country_population = city.title() + ', ' + country.title() + ' - population ' + population
    if population == '':
        return city_country.title()
    elif population != '':
        return city_country_population
def city_country(city, country):
    name_country = f"{city.title()} is in {country.title()}"
    return name_country

place = city_country('jaipur', 'india')
print(place)
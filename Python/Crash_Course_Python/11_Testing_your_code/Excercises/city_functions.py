def get_formatted_name(city, country, population=''):
    if population:
        full_name = f"{city} {country} {population}"
    else:
        full_name = f"{city} {country}"
    return full_name.title()
    # print(full_name.title())
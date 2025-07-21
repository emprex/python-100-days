river_name = {
    'nile': 'egypt',
    'thames': 'united kingdom',
    'danube': 'slovakia'
}

for name, country in river_name.items():
    print(f"The {name.capitalize()} runs through {country.capitalize()}")

# print the key

for name in river_name.keys():
    print(name.capitalize())


# print the value 

for name in river_name.values():
    print(name.capitalize())


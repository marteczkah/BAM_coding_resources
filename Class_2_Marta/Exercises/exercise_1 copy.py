capital_cities = {"England": "London", "Germany": "Berlin", "Poland": "Warsaw", "Norway": "Oslo"}
print(capital_cities['Germany'])

#3
capital_cities['France'] = "Paris"

#4
print(capital_cities.keys())

#5
print(capital_cities.values())

#6
del capital_cities["England"]

#7
capital_cities['Poland'] = ['Warsaw', 'Krakow']

print(capital_cities)
#8
print(capital_cities['Poland'][1])